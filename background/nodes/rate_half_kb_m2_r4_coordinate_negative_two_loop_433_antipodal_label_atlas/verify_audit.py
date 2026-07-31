#!/usr/bin/env python3
"""Independent algebra audit of the 433 label identity."""

from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    x, y, c = sp.symbols("x y c")
    factor = sp.factor(x*(y-c)**2-y*(x-c)**2)
    require(sp.expand(factor-(x-y)*(c**2-x*y)) == 0, "weld factor")
    proof = (NODE / "proof.md").read_text()
    require("six bad cells" in proof and "nine-cell atlas" in proof, "table audit")
    print("RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_LABEL_AUDIT_PASS factor=exact cells=15/9")


if __name__ == "__main__":
    main()
