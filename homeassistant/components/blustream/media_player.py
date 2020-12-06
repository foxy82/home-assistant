"""Connects to a Blustream HDBaseT Matrix."""
import logging

from pyblustream.matrix import Matrix
import voluptuous as vol

from homeassistant.components.media_player import (
    DEVICE_CLASS_TV,
    PLATFORM_SCHEMA,
    MediaPlayerEntity,
)
from homeassistant.components.media_player.const import (
    SUPPORT_SELECT_SOURCE,
    SUPPORT_TURN_OFF,
    SUPPORT_TURN_ON,
)
from homeassistant.config_entries import SOURCE_IMPORT
from homeassistant.const import CONF_HOST, CONF_NAME, CONF_PORT
import homeassistant.helpers.config_validation as cv

from .const import ATTR_MANUFACTURER, BLUSTREAM, DEFAULT_NAME, DOMAIN

_LOGGER = logging.getLogger(__name__)

SUPPORT_BLUSTREAM = SUPPORT_SELECT_SOURCE | SUPPORT_TURN_ON | SUPPORT_TURN_OFF

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_HOST): cv.string,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    }
)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Blustream platform."""
    host = config[CONF_HOST]
    port = config[CONF_PORT]
    m = Matrix()
    print(m)
    hass.async_create_task(
        hass.config_entries.flow.async_init(
            DOMAIN,
            context={"source": SOURCE_IMPORT},
            data={CONF_HOST: host, CONF_PORT: port},
        )
    )


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Add Blustream entities from a config_entry."""
    unique_id = config_entry.unique_id
    device_info = {
        "identifiers": {(DOMAIN, unique_id)},
        "name": DEFAULT_NAME,
        "manufacturer": ATTR_MANUFACTURER,
        "model": config_entry.title,
    }

    matrix = hass.data[DOMAIN][config_entry.entry_id][BLUSTREAM]
    async_add_entities([MatrixDevice(matrix, DEFAULT_NAME, unique_id, device_info)])


class MatrixDevice(MediaPlayerEntity):
    """Representation of a Matrix."""

    def __init__(self, client, name, unique_id, device_info):
        """Initialise."""
        self._matrix = client

    @property
    def name(self):
        """Return the name of the device."""
        # TODO IMPLEMENT THIS
        return self._name

    @property
    def device_class(self):
        """Set the device class to TV."""
        return DEVICE_CLASS_TV

    @property
    def unique_id(self):
        """Return a unique_id for this entity."""
        # TODO IMPLEMENT THIS
        return self._unique_id

    @property
    def device_info(self):
        """Return the device info."""
        # TODO IMPLEMENT THIS
        return self._device_info

    @property
    def state(self):
        """Return the state of the device."""
        # TODO IMPLEMENT THIS
        return self._state

    @property
    def source(self):
        """Return the current input source."""
        # TODO IMPLEMENT THIS
        return self._source

    @property
    def source_list(self):
        """List of available input sources."""
        # TODO IMPLEMENT THIS
        return self._source_list

    @property
    def supported_features(self):
        """Flag media player features that are supported."""
        return SUPPORT_BLUSTREAM

    async def async_turn_on(self):
        """Turn the media player on."""
        async with self._state_lock:
            await self.hass.async_add_executor_job(self._matrix.turn_on)

    async def async_turn_off(self):
        """Turn off media player."""
        async with self._state_lock:
            await self.hass.async_add_executor_job(self._matrix.turn_off)
