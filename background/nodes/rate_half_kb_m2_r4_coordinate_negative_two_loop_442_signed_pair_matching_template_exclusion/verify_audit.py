#!/usr/bin/env python3
"""Independent audit of the 442 signed-pair template cut."""

import itertools
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def matchings(items):
    if not items:
        yield ()
        return
    first = items[0]
    for index in range(1, len(items)):
        second = items[index]
        for tail in matchings(items[1:index]+items[index+1:]):
            yield ((first, second),)+tail


def main() -> None:
    all_matchings = tuple(matchings(tuple(range(6))))
    aq_pairings = [pairs for pairs in all_matchings if (0, 1) in pairs]
    require(len(all_matchings) == 15 and len(aq_pairings) == 3, "matching census")

    l, b = sp.symbols("l b")
    rows = (
        (l**2-l+1, 4*b**2+b+4, (b+1)*(b**2-b+1), 30625),
        (l**2-l+1, 4*b**2+7*b+4, (b-1)*(b**2+b+1), 18225),
        (l**4+1, b**2-b*l**3+b*l-b+1, (b-1)*(b+1), 49),
        (l**4+1, b**2-2*b*l**3+2*b*l-b+1, b**2+1, 2401),
    )
    for relation, gate, factor, expected in rows:
        require(sp.resultant(relation, sp.resultant(gate, factor, b), l) == expected,
                "independent resultant")

    text = (NODE / "statement.md").read_text()
    require("`DF`" in text and "does not delete an entire" in text,
            "scope fence")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_TEMPLATE_AUDIT_PASS "
        "perfect_matchings=15 forbidden_per_cell=3 affected_cells=24"
    )


if __name__ == "__main__":
    main()
