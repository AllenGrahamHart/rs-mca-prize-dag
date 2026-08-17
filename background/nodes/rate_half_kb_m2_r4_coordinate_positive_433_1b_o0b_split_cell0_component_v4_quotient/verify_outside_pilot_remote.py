#!/usr/bin/env python3
"""Manifest registration shim for the canonical Modal pilot launcher."""

import hashlib
import importlib.util
from pathlib import Path

import modal


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
LAUNCHER = (ROOT / "experiments/prize_resolution" /
            "rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_modal.py")
LAUNCHER_SHA256 = "d1e49937e287e2542b0999f81a9afee0e6302c563f7c11f8ab01c6abf70ff2ec"

if hashlib.sha256(LAUNCHER.read_bytes()).hexdigest() != LAUNCHER_SHA256:
    raise RuntimeError("canonical launcher custody")

spec = importlib.util.spec_from_file_location("outside_pilot_modal", LAUNCHER)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
app = module.app
decide_case = module.decide_case
main = module.main
