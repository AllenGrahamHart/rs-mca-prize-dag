#!/usr/bin/env python3
import hashlib, runpy, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_moving_xi_square_ell_audit.py"
EXPECTED = "e47a3e617f0fb5703d5104eae1caddd914f14fade759b5e74585cc85618a4409"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED: raise RuntimeError("audit helper hash")
sys.argv = [str(HELPER), "0", "0"]
runpy.run_path(str(HELPER), run_name="__main__")
