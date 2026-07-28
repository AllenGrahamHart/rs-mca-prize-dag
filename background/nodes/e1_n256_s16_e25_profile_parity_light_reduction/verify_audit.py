#!/usr/bin/env python3
"""Independent audit wrapper for the E25 route reduction."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CHECKER = ROOT / "experiments/prize_resolution/e25_profile_parity_probe_check.py"


def main() -> None:
    completed = subprocess.run(
        [sys.executable, str(CHECKER)], cwd=ROOT, capture_output=True, text=True, check=True
    )
    assert "l1=15 profiles=12 survivors=9 templates=111 floor=2203120896" in completed.stdout
    print("E1_N256_S16_E25_PROFILE_PARITY_LIGHT_REDUCTION_AUDIT_PASS independent_checker=1")


if __name__ == "__main__":
    main()
