from typing import TYPE_CHECKING, Any, Dict, Optional

from .. import endpoints

if TYPE_CHECKING:
    from ..client import ChainupClient


def fetch(
    client: "ChainupClient",
    *,
    start_time: str,
    end_time: str,
    page_num: str = "1",
    page_size: str = "10",
    origin_uid: Optional[str] = None,
    contract_id: Optional[str] = None,
    contract_name: Optional[str] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "startTime": start_time,
        "endTime": end_time,
        "pageNum": page_num,
        "pageSize": page_size,
    }
    if origin_uid:
        payload["originUid"] = origin_uid
    if contract_id:
        payload["contractId"] = contract_id
    if contract_name:
        payload["contractName"] = contract_name
    return client.request(endpoints.TRADE_RECORDS, payload)
