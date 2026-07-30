#!/usr/bin/env python3
import hashlib, runpy, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_moving_xi_square_ell.py"
EXPECTED = "d6033437617d00bdc80e1bacd7cade659d26acb4807ad83b16f66fc4b7ef8a9e"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED: raise RuntimeError("primary helper hash")
sys.argv = [str(HELPER), "1", "0", "--prove"]
runpy.run_path(str(HELPER), run_name="__main__")
