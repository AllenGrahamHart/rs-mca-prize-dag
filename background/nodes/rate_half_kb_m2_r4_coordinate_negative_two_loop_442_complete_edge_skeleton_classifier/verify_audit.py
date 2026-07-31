#!/usr/bin/env python3
"""Independent audit of the 442 outside degree equations."""

from fractions import Fraction
from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def solve(r):
    d = [4-value for value in r]
    return (
        Fraction(d[0]+d[1]-d[2], 2),
        Fraction(d[0]+d[2]-d[1], 2),
        Fraction(d[1]+d[2]-d[0], 2),
    )


def main() -> None:
    same = solve((2, 0, 0))
    split = solve((1, 1, 0))
    require(sorted(same) == [1, 1, 3], "same attachment")
    require(split == (1, 2, 2), "split attachment")
    require(max(same) > 2 and max(split) <= 2, "injectivity cap")
    statement = (NODE / "statement.md").read_text()
    require("both meet" in statement and "distinct `I` pairs" in statement,
            "colored scope")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_SKELETON_AUDIT_PASS "
        "same=1,1,3_deleted split=1,2,2"
    )


if __name__ == "__main__":
    main()
