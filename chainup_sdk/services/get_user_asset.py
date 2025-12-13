from typing import TYPE_CHECKING, Any, Dict, Optional

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
    uid: Optional[str] = None,
) -> Dict[str, Any]:
    """Return contract asset summary for a broker.

    Parameters
    ----------
    client:
        Active ``ChainupClient`` instance; usually ``client.services`` already
        binds this for you.
    start_date:
        Query window start in ``yyyy-MM-dd HH:mm:ss`` format.
    end_date:
        Query window end in ``yyyy-MM-dd HH:mm:ss`` format.
    page:
        Pagination cursor (default ``"1"``).
    page_size:
        Number of rows per page (default ``"1000"``).
    uid:
        Optional contract uid filter; omit to aggregate all users under the
        merchant.

    Returns
    -------
    dict
        Raw JSON response from ``/v1/inner/user_asset``.
    """
    payload: Dict[str, Any] = {
        "startDate": start_date,
        "endDate": end_date,
        "page": page,
        "pageSize": page_size,
    }
    if uid:
        payload["uid"] = uid
    return client.request(endpoints.USER_ASSET, payload)
