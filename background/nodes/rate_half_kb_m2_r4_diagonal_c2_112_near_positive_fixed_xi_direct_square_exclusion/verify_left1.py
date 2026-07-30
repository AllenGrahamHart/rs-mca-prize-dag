#!/usr/bin/env python3
"""Replay primary left-line shard one."""

import hashlib
import runpy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HELPER = (ROOT / "critical/nodes/rate_half_band_closure/notes/"
          "kb_c2_112_near_fixed_xi_square_direct.py")
EXPECTED = "7d3892fddcb4ab95f1fd6f6fa58127cf77c72c024e3272fab9511152df27db93"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED:
    raise RuntimeError("primary helper hash")
sys.argv = [str(HELPER), "1"]
runpy.run_path(str(HELPER), run_name="__main__")
