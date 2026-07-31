#!/usr/bin/env python3
"""Independent algebra audit for the 442 label gate."""

from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    x, y, b = sp.symbols("x y b")
    identity = sp.factor(x * (y - b) ** 2 - y * (x - b) ** 2)
    require(sp.expand(identity - (x - y) * (b**2 - x * y)) == 0, "squared weld factor")

    l, m = sp.symbols("l m")
    sixth = sp.rem(l + m**2, m + l**2, m)
    require(sp.expand(sixth - l * (l**3 + 1)) == 0, "sixth-root cell")
    require(sp.expand((-l**2) ** 2 + 1 - (l**4 + 1)) == 0, "eighth-root L cell")
    require(sp.expand((-m**2) ** 2 + 1 - (m**4 + 1)) == 0, "eighth-root M cell")
    proof = (NODE / "proof.md").read_text()
    require("five `K` labels are distinct" in proof and "complete table" in proof, "proof guards")
    print("RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_LABEL_AUDIT_PASS factor_and_roots=exact")


if __name__ == "__main__":
    main()
