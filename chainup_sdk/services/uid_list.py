from typing import TYPE_CHECKING, Any, Dict

from .. import endpoints

if TYPE_CHECKING:
    from ..client import ChainupClient


def fetch(client: "ChainupClient", *, limit: str = "20", start_uid: str = "0") -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "limit": limit,
        "startUid": start_uid,
    }
    return client.request(endpoints.UID_INFO_LIST, payload)
