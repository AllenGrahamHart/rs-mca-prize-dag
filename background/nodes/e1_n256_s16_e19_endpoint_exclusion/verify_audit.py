#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def main() -> None:
    for checker in (
        "experiments/prize_resolution/e19_profile_parity_probe_check.py",
        "experiments/prize_resolution/e19_four_profile_census_check.py",
        "experiments/prize_resolution/e19_four_profile_norm_check.py",
    ):
        subprocess.run(
            [sys.executable, checker],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=30,
            check=True,
        )
    print(
        "E1_N256_S16_E19_ENDPOINT_EXCLUSION_AUDIT_PASS "
        "checkers=3 mutations=3"
    )


if __name__ == "__main__":
    main()
