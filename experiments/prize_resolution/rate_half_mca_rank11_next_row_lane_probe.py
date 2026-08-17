#!/usr/bin/env python3
"""Replay one exact carrier-atlas lane at a requested adjacent row."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


parser = argparse.ArgumentParser()
parser.add_argument("kprime", type=int)
parser.add_argument("lanes")
args = parser.parse_args()

probe = load_module(
    "carrier_atlas_for_next_row",
    Path("rate_half_mca_rank11_k72_two_step_probe.py"),
)
selected = set(args.lanes.split(","))
print(json.dumps({str(args.kprime): probe.payment(args.kprime, selected)}, indent=2))
