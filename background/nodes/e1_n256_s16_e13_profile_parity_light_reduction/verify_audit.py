#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def main() -> None:
    run = subprocess.run([sys.executable, "experiments/prize_resolution/e13_profile_parity_probe_check.py"],
                         cwd=ROOT, capture_output=True, text=True, timeout=30, check=True)
    assert "l1=9 profiles=4 survivors=4 templates=111 floor=2203120896 mutations=1" in run.stdout
    print("E1_N256_S16_E13_PROFILE_PARITY_LIGHT_REDUCTION_AUDIT_PASS independent_checker=1")


if __name__ == "__main__":
    main()
