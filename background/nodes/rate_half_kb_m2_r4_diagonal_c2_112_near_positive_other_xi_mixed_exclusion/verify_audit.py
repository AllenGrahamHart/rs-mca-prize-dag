#!/usr/bin/env python3
"""Run selected independent other-xi mixed audit shards."""
import hashlib, os, runpy, sys
from pathlib import Path

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
HELPER = ROOT / "critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_moving_xi_mixed_audit.py"
EXPECTED = "37c91621450aaf70f7cf98ee37a943a694a904139d9c5cc7e49fbb037778e9fe"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED:
    raise RuntimeError("audit helper hash")
for mode in os.environ.get("MIXED_AUDIT_MODES", "source").split(","):
    sys.argv = [str(HELPER), mode]
    runpy.run_path(str(HELPER), run_name="__main__")
