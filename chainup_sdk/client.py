from __future__ import annotations

from typing import Any, Dict, Optional

import requests

from .endpoints import Endpoint
from . import utils
from .service_hub import ChainupServiceHub


class ChainupClient:
    """Minimal HTTP client handling signing and dispatch."""

    def __init__(
        self,
        base_url: str,
        *,
        private_key: str,
        session: Optional[requests.Session] = None,
        timeout: int = 10,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.private_key_pem = utils.normalise_private_key(private_key)
        self.session = session or requests.Session()
        self.timeout = timeout
        self.services = ChainupServiceHub(self)

    def request(self, endpoint: Endpoint, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Compose signature and perform the ChainUp API call."""
        timestamp = utils.generate_timestamp_ms()
        sign_content = utils.build_sign_content(payload, timestamp)
        signature = utils.rsa_sign(sign_content, self.private_key_pem)

        headers = utils.build_auth_headers(signature, timestamp)
        response = self.session.request(
            endpoint.method,
            f"{self.base_url}{endpoint.path}",
            json=payload if endpoint.method != "GET" else None,
            params=payload if endpoint.method == "GET" else None,
            headers=headers,
            timeout=self.timeout,
        )
        # print(f"URL: {endpoint.method} {self.base_url}{endpoint.path}\nPayload: {payload}\nReturned Status: {response.status_code}\nBody {response.text}")
        response.raise_for_status()
        return response.json()

    def close(self) -> None:
        """Release the underlying HTTP session."""
        self.session.close()

    def __enter__(self) -> "ChainupClient":
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()
