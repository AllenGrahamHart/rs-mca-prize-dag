#!/usr/bin/env python3
"""Independent entrypoint for the K'=83 active-cell route-cut replay."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve()
VERIFY = HERE.with_name("verify.py")


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    module = load_module("k83_pairwise_wall_primary", VERIFY)
    raise SystemExit(module.main())
