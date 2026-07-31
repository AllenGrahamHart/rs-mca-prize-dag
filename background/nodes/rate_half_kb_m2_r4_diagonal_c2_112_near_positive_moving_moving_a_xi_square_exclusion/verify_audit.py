#!/usr/bin/env python3
"""Run one independent moving-moving a-xi square audit shard."""
import hashlib, os, runpy, sys
from pathlib import Path

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
HELPER = ROOT / "critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_moving_template_a_square_audit.py"
EXPECTED = "00f0011278bded14421d839f69108cb019e935f711137b1dbc1d090db10dc748"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED:
    raise RuntimeError("audit helper hash")
mode = os.environ.get("MOVING_A_SQUARE_AUDIT_MODE", "source")
sys.argv = [str(HELPER), mode]
runpy.run_path(str(HELPER), run_name="__main__")
