#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def main() -> None:
    run = subprocess.run(
        [sys.executable, "experiments/prize_resolution/e19_profile_parity_probe_check.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=30,
        check=True,
    )
    assert "l1=11 profiles=5 survivors=4 templates=8 floor=158783488 mutations=1" in run.stdout
    print(
        "E1_N256_S16_E19_PROFILE_PARITY_LIGHT_REDUCTION_AUDIT_PASS "
        "independent_checker=1"
    )


if __name__ == "__main__":
    main()
