#!/usr/bin/env python3
import hashlib, runpy, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_tau_xi_square_audit.py"
EXPECTED = "644dfa4b9c9ba8f601d8cffa00f18a481cbfbcb3c6482c17667c0a92639e657c"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED: raise RuntimeError("helper hash")
sys.argv = [str(HELPER), "0", "1"]
runpy.run_path(str(HELPER), run_name="__main__")
