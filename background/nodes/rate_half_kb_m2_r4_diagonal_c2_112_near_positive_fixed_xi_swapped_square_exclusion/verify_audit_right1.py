#!/usr/bin/env python3
import hashlib, runpy, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_fixed_xi_square_direct_audit.py"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != "54b993280c506bc85976aaebd746b388c6ebb0ecbcb032bc513a96708310465f":
    raise RuntimeError("audit helper hash")
sys.argv = [str(HELPER), "0", "1", "--swap"]
runpy.run_path(str(HELPER), run_name="__main__")
