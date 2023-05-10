"""Constants used by the Onkyo component."""
from homeassistant.components.media_player import MediaPlayerEntityFeature
from eiscp.commands import COMMANDS

DOMAIN = "onkyo"

CONNECT_TIMEOUT = 5

CONF_IDENTIFIER = "identifier"
CONF_SOURCES = "sources"
CONF_ENABLED_SOURCES = "enabled_sources"
CONF_RECEIVER_MAX_VOLUME = "max_receiver_volume"
CONF_MAX_VOLUME = "max_volume"
CONF_RECEIVER = "receiver"
CONF_DEVICE_INFO = "device_info"

DEFAULT_SOURCES = {
    "tv": "TV",
    "dvd": "BluRay",
    "video3": "Game",
    "strm-box": "Stream Box",
    "video4": "Aux1",
    "fm": "Radio",
    "cd": "CD",
}

DEFAULT_SOURCE_NAMES = {
    value["name"][0]
    if isinstance(value["name"], tuple)
    else value["name"]: value["description"].replace("sets ", "")
    for value in COMMANDS["main"]["SLI"]["values"].values()
    if value["name"] not in ["07", "08", "09", "up", "down", "query"]
}
