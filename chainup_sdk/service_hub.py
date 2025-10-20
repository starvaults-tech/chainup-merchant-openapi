from __future__ import annotations

from functools import partial

from . import services


class ChainupServiceHub:
    """Facade aggregating all ChainUp API call helpers."""

    def __init__(self, client: "ChainupClient") -> None:
        # Market metadata
        self.contracts        = partial(services.get_contracts.fetch, client)

        # Broker revenue
        self.broker_fee_share = partial(services.get_broker_fee_share.fetch, client)

        # Position data
        self.position_list    = partial(services.get_position_list.fetch, client)
        self.position_detail  = partial(services.get_position_detail.fetch, client)

        # Order and trade history
        self.entrusted_record = partial(services.get_entrusted_record.fetch, client)
        self.trade_record     = partial(services.get_trade_record.fetch, client)

        # Transfers, balances, and risk
        self.transfer_records = partial(services.get_transfer_records.fetch, client)
        self.user_asset       = partial(services.get_user_asset.fetch, client)
        self.risk_amount      = partial(services.get_risk_amount.fetch, client)
        self.account_balance  = partial(services.get_account_balance.fetch, client)
        self.ledger_records   = partial(services.get_ledger_records.fetch, client)

        # Utility endpoints
        self.uid_list         = partial(services.get_uid_list.fetch, client)


from typing import TYPE_CHECKING

if TYPE_CHECKING:  # avoid circular imports at runtime
    from .client import ChainupClient
