from typing import TYPE_CHECKING, Any, Dict, Optional

from .. import endpoints, utils

if TYPE_CHECKING:
    from ..client import ChainupClient


def fetch(
    client: "ChainupClient",
    *,
    start_time: str,
    end_time: str,
    page: str = "1",
    limit: str = "20",
    transfer_type: Optional[str] = None,
    uid: Optional[str] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "startTime": utils.ensure_timestamp_ms(start_time),
        "endTime": utils.ensure_timestamp_ms(end_time),
        "page": page,
        "limit": limit,
    }
    if transfer_type:
        payload["transferType"] = transfer_type
    if uid:
        payload["uid"] = uid
    return client.request(endpoints.TRANSFER_RECORDS, payload)
