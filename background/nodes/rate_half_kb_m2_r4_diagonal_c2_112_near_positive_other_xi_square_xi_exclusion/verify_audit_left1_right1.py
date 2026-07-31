#!/usr/bin/env python3
import hashlib, runpy, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_moving_xi_square_xi_audit.py"
EXPECTED = "6c794fbb4b3da89ec4bbdbb0d803763e21a90ef47f118e0ab02845ae16022c5a"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED: raise RuntimeError("audit helper hash")
sys.argv = [str(HELPER), "1", "1"]
runpy.run_path(str(HELPER), run_name="__main__")
