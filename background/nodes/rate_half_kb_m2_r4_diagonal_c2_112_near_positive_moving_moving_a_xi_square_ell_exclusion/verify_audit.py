#!/usr/bin/env python3
"""Run one independent moving-moving a-xi square-ell audit shard."""
import hashlib, os, runpy, sys
from pathlib import Path

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
HELPER = ROOT / "critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_moving_template_a_square_audit.py"
EXPECTED = "05a973b7a808ba45cdeca7bcdfdf6786ef460ac5bb382c17a203f11ff0b8b740"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED:
    raise RuntimeError("audit helper hash")
mode = os.environ.get("MOVING_A_SQUARE_ELL_AUDIT_MODE", "source")
sys.argv = [str(HELPER), mode, "--allocation", "square-ell"]
runpy.run_path(str(HELPER), run_name="__main__")
