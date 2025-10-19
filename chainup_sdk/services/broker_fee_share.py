from typing import TYPE_CHECKING, Any, Dict, Optional

from .. import endpoints

if TYPE_CHECKING:
    from ..client import ChainupClient


def fetch(
    client: "ChainupClient",
    broker_id: str,
    begin_time: str,
    end_time: str,
    *,
    co_uid: Optional[str] = None,
    uid: Optional[str] = None,
    limit: str = "1000",
    page: str = "1",
    fee_type: str = "1",
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "brokerId": broker_id,
        "beginTime": begin_time,
        "endTime": end_time,
        "limit": limit,
        "page": page,
        "type": fee_type,
    }
    if co_uid:
        payload["coUid"] = co_uid
    if uid:
        payload["uid"] = uid
    return client.request(endpoints.BROKER_FEE_SHARE, payload)
