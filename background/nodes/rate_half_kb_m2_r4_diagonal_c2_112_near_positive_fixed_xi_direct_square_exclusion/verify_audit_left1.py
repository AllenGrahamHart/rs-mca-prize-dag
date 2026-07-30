#!/usr/bin/env python3
"""Replay independent left-line shard one."""

import hashlib
import runpy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HELPER = (ROOT / "critical/nodes/rate_half_band_closure/notes/"
          "kb_c2_112_near_fixed_xi_square_direct_audit.py")
EXPECTED = "96036a63c54b94beab3ce6d33b0237c6c78b7e9208ea37a770c00171159dcde5"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED:
    raise RuntimeError("audit helper hash")
sys.argv = [str(HELPER), "1", "0"]
runpy.run_path(str(HELPER), run_name="__main__")
