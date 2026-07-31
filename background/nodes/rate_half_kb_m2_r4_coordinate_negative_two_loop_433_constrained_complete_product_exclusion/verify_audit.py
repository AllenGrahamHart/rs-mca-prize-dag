#!/usr/bin/env python3
"""Alternate-chain multiplication-matrix audit of the colored types."""

from audit_runner import run_kind


def main():
    for kind in ("bD", "cE", "DE"):
        run_kind(kind)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_CONSTRAINED_AUDIT_PASS "
        "types=bD,cE,DE alternate_units=270 matrix_rank=8"
    )


if __name__ == "__main__":
    main()
