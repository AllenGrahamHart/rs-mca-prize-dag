#!/usr/bin/env python3
"""Replay the independent fraction-free opposite-projection audit."""

import hashlib
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HELPER = (ROOT / "critical/nodes/rate_half_band_closure/notes/"
          "kb_c2_112_near_fixed_xi_mixed_direct_audit.py")
EXPECTED = "694ecea074769c5fd5fc62645c490768ca9f620e15b2739d779bb145313690f7"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED:
    raise RuntimeError("audit helper hash")
runpy.run_path(str(HELPER), run_name="__main__")
