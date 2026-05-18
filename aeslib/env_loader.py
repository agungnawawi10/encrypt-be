from __future__ import annotations

import os
from pathlib import Path


def _load_dotenv_file(dotenv_path: Path) -> dict[str, str]:
    values: dict[str, str] = {}

    if not dotenv_path.is_file():
        return values

    for raw_line in dotenv_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            values[key] = value

    return values


def get_aes_key() -> bytes:
    key_str = os.getenv("AES_KEY")

    if not key_str:
        dotenv_path = Path(__file__).resolve().parent.parent / ".env"
        key_str = _load_dotenv_file(dotenv_path).get("AES_KEY")

    if not key_str:
        raise RuntimeError("AES_KEY is not set in the environment or .env file")

    key = key_str.encode()
    if len(key) not in (16, 24, 32):
        raise ValueError(
            f"AES_KEY must be 16, 24 or 32 bytes long when encoded (got {len(key)})"
        )

    return key