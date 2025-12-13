from typing import TYPE_CHECKING, Any, Dict, Optional

from .. import endpoints

if TYPE_CHECKING:
    from ..client import ChainupClient


def fetch(
    client: "ChainupClient",
    *,
    coin: str,
    uid: Optional[int] = None,
    page_size: str = "30",
    page_num: str = "1",
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "coin": coin,
        "pageSize": page_size,
        "pageNum": page_num,
    }
    if uid is not None:
        payload["uid"] = uid
    return client.request(endpoints.ACCOUNT_BALANCE, payload)