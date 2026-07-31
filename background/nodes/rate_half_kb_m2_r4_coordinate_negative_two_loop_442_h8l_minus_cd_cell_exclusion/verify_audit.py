#!/usr/bin/env python3
"""Independent resultant-chain audit of the H8-L-minus cell cut."""

from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
REPRESENTATIVES = (3, 4, 5, 9, 10, 11)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def matchings(items):
    if not items:
        yield ()
        return
    first = items[0]
    for index in range(1, len(items)):
        for tail in matchings(items[1:index]+items[index+1:]):
            yield ((first, items[index]),)+tail


def main() -> None:
    b, a, x = sp.symbols("b a x")
    p4 = b**4-2*b**3+b**2-2*b+1
    c = (b-2)*(b**2+1)/b
    gamma = b+c
    alpha = -b*c*(b-1)
    all_matchings = tuple(matchings(tuple(range(6))))

    checked = 0
    for sigma in (-1, 1):
        values = (a, sigma*a/c**2, x, -x, a*x, -a*x)
        for index in REPRESENTATIVES:
            equations = []
            for left, right in all_matchings[index]:
                y, z = values[left], values[right]
                equations.append(
                    sp.together(gamma*(y*z+1)-alpha*(y+z)).as_numer_denom()[0]
                )
            # Independent chain: share the second equation.
            r21 = sp.resultant(equations[1], equations[0], x)
            r23 = sp.resultant(equations[1], equations[2], x)
            obstruction = sp.factor(sp.resultant(r21, r23, a))
            factors = sp.factor_list(obstruction)[1]
            require(factors, f"factor coverage {sigma}/{index}")
            require(all(sp.resultant(p4, factor, b) != 0 for factor, _ in factors),
                    f"independent norms {sigma}/{index}")
            checked += 1

    text = (NODE / "statement.md").read_text()
    require("34 cells" in text and "does not delete the `H8-L" in text,
            "scope fence")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_H8L_MINUS_CD_AUDIT_PASS "
        f"independent_chains={checked} factor_norms=all_nonzero"
    )


if __name__ == "__main__":
    main()
