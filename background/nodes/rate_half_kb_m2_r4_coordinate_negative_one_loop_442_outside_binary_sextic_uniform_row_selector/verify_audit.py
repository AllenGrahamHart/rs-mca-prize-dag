#!/usr/bin/env python3
"""Audit the uniform selector in isolated common sign-row processes."""

import subprocess
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SELECTOR = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_442_sextic_row_selector.py"
)
EXPECTED = "rows=(0, 1, 2) columns=(0, 1, 2) norm=1133299039"


def main():
    for epsilon_1, epsilon_2 in ((1, -1), (-1, 1), (-1, -1)):
        completed = subprocess.run(
            [sys.executable, str(SELECTOR),
             str(epsilon_1), str(epsilon_2)],
            check=True, capture_output=True, text=True, timeout=60,
        )
        if EXPECTED not in completed.stdout:
            raise RuntimeError(
                f"sign-row selector {epsilon_1},{epsilon_2}: "
                f"{completed.stdout.strip()}"
            )
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_ROW_AUDIT_PASS "
        "other_sign_rows=3 norm=1133299039"
    )


if __name__ == "__main__":
    main()
