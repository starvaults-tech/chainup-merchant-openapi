from __future__ import annotations

from functools import partial

from . import services


class ChainupServiceHub:
    """Facade aggregating all ChainUp API call helpers."""

    def __init__(self, client: "ChainupClient") -> None:
        # Market metadata
        self.contracts = partial(services.contracts.fetch, client)

        # Broker revenue
        self.broker_fee_share = partial(services.broker_fee_share.fetch, client)

        # Position data
        self.position_list = partial(services.position_list.fetch, client)
        self.position_detail = partial(services.position_detail.fetch, client)

        # Order and trade history
        self.entrusted_record = partial(services.entrusted_record.fetch, client)
        self.trade_record = partial(services.trade_record.fetch, client)

        # Transfers, balances, and risk
        self.transfer_records = partial(services.transfer_records.fetch, client)
        self.asset_summary = partial(services.asset_summary.fetch, client)
        self.risk_fund = partial(services.risk_fund.fetch, client)
        self.user_account_balance = partial(services.user_account_balance.fetch, client)
        self.transaction_funding_record = partial(
            services.transaction_funding_record.fetch, client
        )

        # Utility endpoints
        self.uid_list = partial(services.uid_list.fetch, client)


from typing import TYPE_CHECKING

if TYPE_CHECKING:  # avoid circular imports at runtime
    from .client import ChainupClient
