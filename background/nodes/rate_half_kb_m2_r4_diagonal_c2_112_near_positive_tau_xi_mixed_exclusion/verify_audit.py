#!/usr/bin/env python3
"""Replay the reciprocal-xi fraction-free opposite-projection audit."""

import hashlib
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HELPER = (ROOT / "critical/nodes/rate_half_band_closure/notes/"
          "kb_c2_112_near_tau_xi_mixed_audit.py")
EXPECTED = "961da0a88eeb51a1fac3e100b1b2e844f2fa11ad78f7ead957abd630c4990a93"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED:
    raise RuntimeError("audit helper hash")
runpy.run_path(str(HELPER), run_name="__main__")
