"""The onkyo component."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.const import (
    ATTR_MANUFACTURER,
    ATTR_MODEL,
    CONF_HOST, 
    CONF_NAME
)
from homeassistant.helpers.entity import DeviceInfo


import eiscp


from .const import (
    COMMANDS,
    CONF_DEVICE_INFO,
    CONF_IDENTIFIER,
    CONF_MAX_VOLUME,
    CONF_RECEIVER,
    CONF_RECEIVER_MAX_VOLUME,
    CONF_SOURCES,
    DEFAULT_SOURCES,
    DOMAIN,
)
from .media_player import OnkyoDevice

PLATFORMS: list[Platform] = [Platform.MEDIA_PLAYER]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up an Onkyo/Pioneer Network Receiver from a config entry."""
    # receiver: eISCP = entry.data[CONF_RECEIVER]
    receiver: eISCP = eiscp.eISCP(entry.data[CONF_HOST])


    device_info = DeviceInfo(
        identifiers={(DOMAIN, entry.data[CONF_IDENTIFIER])},
        name=entry.data[CONF_NAME],
        manufacturer=entry.data[ATTR_MANUFACTURER],
        model=entry.data[ATTR_MODEL],
    )

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {
        CONF_RECEIVER: receiver,
        CONF_DEVICE_INFO: device_info,
    }

    # entry.async_on_unload(entry.add_update_listener(async_reload_entry))

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


# async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
#     """Unload a config entry."""
#     unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

#     await hass.data[DOMAIN][entry.entry_id][CONF_RECEIVER].async_disconnect()

#     if unload_ok:
#         hass.data[DOMAIN].pop(entry.entry_id)

#     return unload_ok


# async def async_reload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> None:
#     """Handle options update."""
#     await hass.config_entries.async_reload(config_entry.entry_id)
