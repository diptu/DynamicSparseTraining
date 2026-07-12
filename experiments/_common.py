"""Shared helpers for the config-driven experiment scripts."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any


def load_config(path: str) -> dict[str, Any]:
    import yaml  # from the [experiments] extra

    with open(path) as f:
        return yaml.safe_load(f)


def config_arg_parser(description: str) -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=description)
    p.add_argument(
        "--config",
        required=True,
        help="path to an experiments/configs/*.yaml file",
    )
    return p


def ensure_parent(path: str) -> str:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    return path
