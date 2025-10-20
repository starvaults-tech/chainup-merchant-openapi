import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


from chainup_sdk import ChainupClient, utils


def load_env() -> None:
    env_path = Path(".env")
    if env_path.exists():
        load_dotenv(env_path)


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing environment variable: {name}")
    return value


def main() -> None:
    load_env()
    base_url = require_env("CHAINUP_BASE_URL")
    private_key = utils.normalise_private_key(require_env("PRI_KEY"))
    with ChainupClient(base_url, private_key=private_key) as client:
        try:
            data = client.services.contracts()
        except Exception as exc:
            print(f"Request failed: {exc}")
        else:
            print(json.dumps(data, indent=2, ensure_ascii=False))

        # 演示簽名流程，對照官方 signContent
        sample_payload = {
            "beginTime": "2000-01-01 00:00:00",
            "brokerId": "0000",
            "endTime": "2000-01-01 00:00:00",
            "limit": "10",
            "page": "1",
            "type": "1",
            "uid": "000000",
        }
        fake_timestamp = "946656000000"
        sign_content = utils.build_sign_content(sample_payload, fake_timestamp)
        signature = utils.rsa_sign(sign_content, private_key)
        print("signContent:", sign_content)
        print("signature:", signature)


if __name__ == "__main__":
    main()
