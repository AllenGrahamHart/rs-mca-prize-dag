#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def main() -> None:
    checks = (
        (
            "experiments/prize_resolution/e17_five_profile_census_check.py",
            "profile=2050 full=488",
        ),
        (
            "experiments/prize_resolution/e17_five_profile_norm_check.py",
            "hits=16 odd_max=",
        ),
    )
    for path, marker in checks:
        run = subprocess.run(
            [sys.executable, path],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=30,
            check=True,
        )
        assert marker in run.stdout
        if "norm" in path:
            assert "odd_hits=0" in run.stdout
    print(
        "E1_N256_S16_E17_FIVE_PROFILE_EXCLUSION_AUDIT_PASS "
        "checkers=2 engines=4 mutations=2"
    )


if __name__ == "__main__":
    main()
