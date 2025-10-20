from typing import TYPE_CHECKING, Any, Dict

from .. import endpoints

if TYPE_CHECKING:
    from ..client import ChainupClient


def fetch(client: "ChainupClient") -> Dict[str, Any]:
    return client.request(endpoints.CONTRACTS, {})
