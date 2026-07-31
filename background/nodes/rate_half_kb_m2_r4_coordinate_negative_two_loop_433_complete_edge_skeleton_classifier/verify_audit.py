#!/usr/bin/env python3
"""Independent closed-form audit of the 433 outside degree equations."""

from fractions import Fraction
from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def internal_solution(r):
    d = [4-value for value in r]
    return (
        Fraction(d[0]+d[1]-d[2], 2),
        Fraction(d[0]+d[2]-d[1], 2),
        Fraction(d[1]+d[2]-d[0], 2),
    )


def main() -> None:
    same = internal_solution((2, 0, 0))
    split = internal_solution((1, 1, 0))
    require(sorted(same) == [1, 1, 3], "same-pair obstruction")
    require(split == (1, 2, 2), "split-pair solution")
    require(max(same) > 2 and max(split) <= 2, "injectivity cap")
    text = (NODE / "statement.md").read_text()
    require("five internal signed edge types for eta" in text, "eta scope")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_SKELETON_AUDIT_PASS "
        "same=1,1,3_deleted split=1,2,2"
    )


if __name__ == "__main__":
    main()
