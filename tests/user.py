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
            data = client.services.position_list(
                origin_uid = "33739092",
                start_date = "2025-10-01 00:00:00",
                end_date   = "2025-10-18 00:00:00",
                page_num   = "1",
                page_size  = "10"
            )
            # data = client.services.contracts()
        except Exception as exc:
            print(f"Request failed: {exc}")
        else:
            print(json.dumps(data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
