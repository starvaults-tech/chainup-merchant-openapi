from math import ceil
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Iterator

from .. import endpoints

if TYPE_CHECKING:
    from ..client import ChainupClient


def sub_fetch(
    client: "ChainupClient",
    *,
    start_date: str,
    end_date: str,
    page_num: str = "1",
    page_size: str = "10",
    origin_uid: Optional[str] = None,
    origin_uids: Optional[str] = None,
    contract_id: Optional[str] = None,
    contract_name: Optional[str] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "startDate": start_date,
        "endDate": end_date,
        "pageNum": page_num,
        "pageSize": page_size,
    }
    if origin_uid:
        payload["originUid"] = origin_uid
    if origin_uids:
        payload["originUids"] = origin_uids
    if contract_id:
        payload["contractId"] = contract_id
    if contract_name:
        payload["contractName"] = contract_name

    return client.request(endpoints.ENTRUSTED_RECORDS, payload)

def iter_fetch_all(
    client: "ChainupClient",
    *,
    start_date: str,
    end_date: str,
    page_size: int = 50,
    **filters,
) -> Iterator[Dict[str, Any]]:
    page = 1
    total_pages = None

    while True:
        resp = sub_fetch(
            client,
            start_date=start_date,
            end_date=end_date,
            page_num=str(page),
            page_size=str(page_size),
            **filters,
        )

        if resp.get("msg") != "success":
            break

        data = resp.get("data", {})
        records = data.get("dataList", [])
        total = data.get("total", 0)

        if total_pages is None:
            total_pages = ceil(total / page_size)

        for r in records:
            yield r

        if page >= total_pages:
            break

        page += 1

def fetch(
    client: "ChainupClient",
    *,
    start_date: str,
    end_date: str,
    page_size: int = 50,
    **filters,
) -> List[Dict[str, Any]]:
    return list(iter_fetch_all(
        client,
        start_date=start_date,
        end_date=end_date,
        page_size=page_size,
        **filters,
    ))
