from typing import TYPE_CHECKING, Any, Dict

from .. import endpoints

if TYPE_CHECKING:
    from ..client import ChainupClient


def fetch(client: "ChainupClient", position_id: str) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"positionId": position_id}
    return client.request(endpoints.POSITION_DETAIL, payload)
