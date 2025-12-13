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
    """Retrieve contract position pages for the given spot uid.

    Parameters
    ----------
    client:
        Active ``ChainupClient`` instance injected by ``client.services``.
    origin_uid:
        Spot uid (``originUid``) whose positions you want to inspect.
    start_date:
        Query window start in ``yyyy-MM-dd HH:mm:ss`` format.
    end_date:
        Query window end in ``yyyy-MM-dd HH:mm:ss`` format.
    page_num:
        Current page index, expressed as string (default ``"1"``).
    page_size:
        Records per page (default ``"10"``; API caps at 1000).
    status:
        Optional warehouse status flag: ``"0"`` for history, ``"1"`` for
        current open positions, omit to fetch all.

    Returns
    -------
    dict
        Raw JSON payload from ``/v1/inner/get_position_list``.
    """
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
