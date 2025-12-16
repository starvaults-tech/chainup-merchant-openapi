from typing import TYPE_CHECKING, Any, Dict, Optional

from .. import endpoints, utils

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
    """Query trade fills for the specified window.

    Parameters
    ----------
    client:
        Active ``ChainupClient`` instance; typically ``client.services`` injects
        this dependency.
    start_time:
        Inclusive start timestamp. Accepts milliseconds as string or
        ``yyyy-MM-dd HH:mm:ss`` (UTC).
    end_time:
        Inclusive end timestamp. Accepts milliseconds as string or
        ``yyyy-MM-dd HH:mm:ss`` (UTC).
    page_num:
        Page index (string, default ``"1"``).
    page_size:
        Page size (string, default ``"10"``; API limit 1000).
    origin_uid:
        Optional spot uid filter; omit to retrieve all users under merchant.
    contract_id:
        Optional contract id filter; mutually exclusive with
        ``contract_name``.
    contract_name:
        Optional contract name filter; if both id and name provided, name wins.

    Returns
    -------
    dict
        Raw JSON from ``/v1/inner/get_trade_record``.
    """
    payload: Dict[str, Any] = {
        "startTime": utils.ensure_timestamp_ms(start_time),
        "endTime": utils.ensure_timestamp_ms(end_time),
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
