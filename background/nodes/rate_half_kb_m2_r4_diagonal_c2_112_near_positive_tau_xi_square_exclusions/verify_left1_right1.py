#!/usr/bin/env python3
import hashlib, runpy, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_tau_xi_square_direct.py"
EXPECTED = "8239d7f2aa3f3077ac9b36a3428e4e74bf2dec2fcc02704f64489f093414ca73"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED: raise RuntimeError("helper hash")
sys.argv = [str(HELPER), "1", "1"]
runpy.run_path(str(HELPER), run_name="__main__")
