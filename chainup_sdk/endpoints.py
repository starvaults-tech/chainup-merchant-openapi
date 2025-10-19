from dataclasses import dataclass


@dataclass(frozen=True)
class Endpoint:
    path: str
    method: str = "POST"


BROKER_FEE_SHARE  = Endpoint("/v1/inner/get_broker_fee_share_by_broker_ctime")
POSITION_LIST     = Endpoint("/v1/inner/get_position_list")
ENTRUSTED_RECORDS = Endpoint("/v1/inner/get_entrusted_record")
TRADE_RECORDS     = Endpoint("/v1/inner/get_trade_record")
POSITION_DETAIL   = Endpoint("/v1/inner/get_position_detail")
UID_INFO_LIST     = Endpoint("/v1/inner/get_uid_list")
TRANSFER_RECORDS  = Endpoint("/v1/inner/get_trans_records")
USER_ASSET        = Endpoint("/v1/inner/user_asset")
RISK_AMOUNT       = Endpoint("/v1/inner/risk_amount")
CONTRACTS         = Endpoint("/fapi/v1/contracts", method="GET")
ACCOUNT_BALANCE   = Endpoint("/v1/inner/user_account_balance")
LEDGER_RECORDS    = Endpoint("/v1/inner/transaction_funding_record")