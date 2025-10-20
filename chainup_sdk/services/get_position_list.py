from typing import TYPE_CHECKING, Any, Dict, Optional

from .. import endpoints

if TYPE_CHECKING:
    from ..client import ChainupClient


def fetch(
    client: "ChainupClient",
    origin_uid: str,
    *,
    start_date: str,
    end_date: str,
    page_num: str = "1",
    page_size: str = "10",
    status: Optional[str] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "originUid": origin_uid,
        "startDate": start_date,
        "endDate": end_date,
        "pageNum": page_num,
        "pageSize": page_size,
    }
    if status is not None:
        payload["status"] = status
    return client.request(endpoints.POSITION_LIST, payload)
