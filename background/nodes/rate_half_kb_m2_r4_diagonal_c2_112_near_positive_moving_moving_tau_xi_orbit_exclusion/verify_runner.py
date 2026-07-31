#!/usr/bin/env python3
"""Hash-pinned dispatcher for the primary tau-orbit certificate."""
import hashlib
import runpy
import sys
from pathlib import Path

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
HELPER = ROOT / "critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_moving_template_probe.py"
EXPECTED = "deb385db95bf5737a7eef419af359714829c19b5a92a63d087f0fc3451afd32c"


def check_hash() -> None:
    if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED:
        raise RuntimeError("primary helper hash")


def run(allocation: str, mode: str) -> None:
    check_hash()
    sys.argv = [str(HELPER), "tau", allocation, mode, "--prove"]
    runpy.run_path(str(HELPER), run_name="__main__")


if __name__ == "__main__":
    check_hash()
    print("KB_C2_112_NEAR_MOVING_TEMPLATE_TAU_PRIMARY_DISPATCH_PASS")
