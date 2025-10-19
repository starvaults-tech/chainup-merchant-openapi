from typing import TYPE_CHECKING, Any, Dict

from .. import endpoints

if TYPE_CHECKING:
    from ..client import ChainupClient


def fetch(
    client: "ChainupClient",
    *,
    start_date: str,
    end_date: str,
    page: str = "1",
    page_size: str = "1000",
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "startDate": start_date,
        "endDate": end_date,
        "page": page,
        "pageSize": page_size,
    }
    return client.request(endpoints.RISK_AMOUNT, payload)
