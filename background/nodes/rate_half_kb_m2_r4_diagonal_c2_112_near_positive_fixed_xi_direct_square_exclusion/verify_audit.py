#!/usr/bin/env python3
"""Replay independent left-line shard zero."""

import hashlib
import runpy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HELPER = (ROOT / "critical/nodes/rate_half_band_closure/notes/"
          "kb_c2_112_near_fixed_xi_square_direct_audit.py")
EXPECTED = "54b993280c506bc85976aaebd746b388c6ebb0ecbcb032bc513a96708310465f"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED:
    raise RuntimeError("audit helper hash")
sys.argv = [str(HELPER), "0", "0"]
runpy.run_path(str(HELPER), run_name="__main__")
