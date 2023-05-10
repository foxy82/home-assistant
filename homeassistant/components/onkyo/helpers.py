"""Helper functions for the Onkyo component."""
from __future__ import annotations

import logging

from eiscp import eISCP

from homeassistant.core import callback

_LOGGER = logging.getLogger(__name__)


def discover_connections(host: str | None = None
) -> list[eISCP]:
    """Discover all available connections on the network."""
    connections: dict[str, eISCP] = {}

    _LOGGER.info("Running Discovery for Onkyo Devices")
    results = eISCP.discover()
    _LOGGER.info(f"Discovery for Onkyo Devices complete. {len(results)} devices found")
    for receiver in results:
        if receiver.identifier not in connections:

            connections[receiver.identifier] = receiver
            # We only expect one connection when a host is provided.
            if host and receiver.host == host:
                return [receiver]

    # If we get here and we didn't find the specified host we didn't find required device
    if host:
        return []

    return list(connections.values())
