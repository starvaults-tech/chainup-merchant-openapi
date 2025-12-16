from typing import TYPE_CHECKING, Any, Dict

from .. import endpoints

if TYPE_CHECKING:
    from ..client import ChainupClient


def fetch(client: "ChainupClient") -> Dict[str, Any]:
    """取得合約列表。

    Returns:
        [{
            "symbol"          (str)   : 合約名稱,
            "pricePrecision"  (int)   : 價格精度,
            "side"            (int)   : 合約方向，0 反向、1 正向,
            "maxMarketVolume" (flaot) : 市價單最大下單數量,
            "multiplier"      (flaot) : 合約面值,
            "minOrderVolume"  (flaot) : 最小下單量,
            "maxMarketMoney"  (flaot) : 市價最大下單金額,
            "type"            (str)   : 合約類型，E 永續、W 周、N 次周、M 月、Q 季度,
            "maxLimitVolume"  (flaot) : 限價單最大下單數量,
            "maxValidOrder"   (int)   : 最大有效委託的訂單數量,
            "multiplierCoin"  (str)   : 合約面值單位,
            "minOrderMoney"   (flaot) : 最小下單金額,
            "maxLimitMoney"   (flaot) : 限價單最大下單金額,
            "contractId"      (int)   : 合約 ID,
            "status"          (int)   : 合約狀態，0 不可交易、1 可交易,
        },...]
    """
    return client.request(endpoints.CONTRACTS, {})
