from typing import TYPE_CHECKING, Any, Dict, Optional

from .. import endpoints

if TYPE_CHECKING:
    from ..client import ChainupClient


def fetch(
    client: "ChainupClient",
    *,
    begin_time: str,
    end_time: str,
    page: str = "1",
    limit: str = "10",
    uid: Optional[str] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "beginTime": begin_time,
        "endTime": end_time,
        "page": page,
        "limit": limit,
    }
    if uid:
        payload["uid"] = uid
    return client.request(endpoints.LEDGER_RECORDS, payload)
