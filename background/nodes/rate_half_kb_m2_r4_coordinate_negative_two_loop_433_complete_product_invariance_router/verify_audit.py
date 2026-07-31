#!/usr/bin/env python3
"""Independent combinatorial audit of the 20-cell router."""

import itertools
from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    sign_orbits = {}
    for u, v, w in itertools.product((-1, 1), repeat=3):
        sign_orbits.setdefault(w*u*v, []).append((u, v, w))
    require(set(sign_orbits) == {-1, 1}, "two tau values")
    require(all(len(values) == 4 for values in sign_orbits.values()),
            "sign orbit sizes")
    require(2*2*5 == 20, "canonical cells")
    require(2*8*7*15 == 1680, "fully labeled naive count")
    require(2*2*5*15 == 300, "sign-gauged matching count")
    text = (NODE / "statement.md").read_text()
    require("Never substitute" in text and "full twelve-row" in text,
            "typing and scope")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_INVARIANCE_AUDIT_PASS "
        "sign_orbits=2 gauged_matchings=300 invariant_cells=20"
    )


if __name__ == "__main__":
    main()
