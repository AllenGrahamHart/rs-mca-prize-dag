#!/usr/bin/env python3
import hashlib, runpy, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_moving_xi_square_xi.py"
EXPECTED = "eaa987bf8cae660d24459305aa6c9893eb8bfb9782c638cf7cc6455deaef9e4c"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED: raise RuntimeError("helper hash")
sys.argv = [str(HELPER), "--square-xi-pair", "0", "1", "--prove"]
runpy.run_path(str(HELPER), run_name="__main__")
