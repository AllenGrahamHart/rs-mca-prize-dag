#!/usr/bin/env python3
"""Run the independent E24 router checker."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CHECKER = ROOT / "experiments/prize_resolution/e24_profile_parity_probe_check.py"


def main() -> None:
    completed = subprocess.run(
        [sys.executable, str(CHECKER)], cwd=ROOT, capture_output=True,
        text=True, timeout=30, check=True,
    )
    assert "l1=14 profiles=9 survivors=6 templates=154 floor=3056582144 mutations=2" in completed.stdout
    print("E1_N256_S16_E24_PROFILE_PARITY_LIGHT_REDUCTION_AUDIT_PASS independent_checker=1")


if __name__ == "__main__":
    main()
