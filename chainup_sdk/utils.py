import base64
import json
import textwrap
import time
from datetime import datetime, timezone
from typing import Any, Dict, Optional


def sorted_json_dumps(payload: Dict[str, Any]) -> str:
    """Serialize payload to JSON with deterministic key ordering."""
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def build_sign_content(payload: Dict[str, Any], timestamp: str) -> str:
    """Concatenate the sorted JSON payload with the timestamp for signing."""
    return f"{sorted_json_dumps(payload)}{timestamp}"


def generate_timestamp_ms() -> str:
    """Return the current epoch timestamp in milliseconds as a string."""
    return str(int(time.time() * 1000))


def ensure_timestamp_ms(value: str) -> str:
    """Coerce ``value`` into a millisecond timestamp string.

    Accepts either an already well-formed millisecond timestamp or a
    ``yyyy-MM-dd HH:mm:ss`` datetime string (interpreted as UTC).
    """

    stripped = value.strip()
    if stripped.isdigit():
        return stripped

    try:
        dt = datetime.strptime(stripped, "%Y-%m-%d %H:%M:%S")
        dt = dt.replace(tzinfo=timezone.utc)
    except ValueError as exc:  # pragma: no cover - defensive branch
        raise ValueError(
            "Timestamp must be milliseconds string or 'yyyy-MM-dd HH:mm:ss'."
        ) from exc

    return str(int(dt.timestamp() * 1000))


def normalise_private_key(raw: str) -> str:
    """Return PEM-formatted private key string, accepting plain Base64 or escaped newlines."""
    cleaned = raw.strip()
    if "-----BEGIN" in cleaned and "\n" not in cleaned:
        cleaned = cleaned.replace("\\n", "\n")
    if "-----BEGIN" not in cleaned:
        body = cleaned.replace("\\n", "").replace("\n", "").replace(" ", "")
        wrapped = "\n".join(textwrap.wrap(body, 64))
        cleaned = f"-----BEGIN PRIVATE KEY-----\n{wrapped}\n-----END PRIVATE KEY-----"
    if not cleaned.endswith("\n"):
        cleaned = f"{cleaned}\n"
    return cleaned


def rsa_sign(content: str, private_key_pem: str, passphrase: Optional[bytes] = None) -> str:
    """Return a base64 encoded RSA signature for the provided content."""
    try:
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import padding
    except ImportError as exc:  # pragma: no cover - runtime guard
        raise RuntimeError(
            "cryptography package is required for RSA signing. Install with `pip install cryptography`."
        ) from exc

    private_key = serialization.load_pem_private_key(
        private_key_pem.encode("utf-8"),
        password=passphrase,
    )

    signature = private_key.sign(
        content.encode("utf-8"),
        padding.PKCS1v15(),
        hashes.SHA256(),
    )
    return base64.b64encode(signature).decode("utf-8")


def build_auth_headers(
    signature: str,
    timestamp: str,
) -> Dict[str, str]:
    """Assemble request headers expected by the ChainUp merchant API."""
    headers = {
        "X-CH-TS": timestamp,
        "Ex-ts": timestamp,
        "Ex-sign": signature,
    }
    return headers
