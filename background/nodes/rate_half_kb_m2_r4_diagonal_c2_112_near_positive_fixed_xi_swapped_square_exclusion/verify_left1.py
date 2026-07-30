#!/usr/bin/env python3
import hashlib, runpy, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_fixed_xi_square_direct.py"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != "d42b13b0cff26e448ad93e9925ce0e4283797d03c8a2f4d630175dddd457e5f3":
    raise RuntimeError("primary helper hash")
sys.argv = [str(HELPER), "1", "0", "--swap"]
runpy.run_path(str(HELPER), run_name="__main__")
