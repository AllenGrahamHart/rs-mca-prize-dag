#!/usr/bin/env python3
"""Direct deployed-field saturation audit of the H6 exclusion."""

from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
DEPLOYED_PRIME = 2130706433
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
        for tail in matchings(items[1:index] + items[index + 1:]):
            yield ((first, items[index]),) + tail


def main() -> None:
    b, a, x, z = sp.symbols("b a x z")
    all_matchings = tuple(matchings(tuple(range(6))))
    checked = 0
    saturated = 0
    for tau in (-1, 1):
        row_coefficient = 1 if tau == -1 else 7
        p2 = 4*b**2 + row_coefficient*b + 4
        c = 2*(1 - b)/3 if tau == -1 else 2*(b + 1)
        gamma = b**2 - tau*b*c + c - 1
        alpha = c*(tau*b**3 - 1)
        beta = -b*c*(tau*b**2*c - tau*b**2 + b - tau*c)
        for sigma in (-1, 1):
            values_by_type = (
                (a, -sigma*b*a/c**2, x, -x, -a*x/b, a*x/b),
                (a, -sigma*b*c**2/a, x, -x,
                 -sigma*b*c**2*x/a**2, sigma*b*c**2*x/a**2),
            )
            for values in values_by_type:
                for index in REPRESENTATIVES:
                    equations = []
                    for left, right in all_matchings[index]:
                        y, value = values[left], values[right]
                        equation = gamma*y*value - alpha*(y + value) - beta
                        equations.append(sp.together(equation).as_numer_denom()[0])
                    if sigma == tau:
                        polynomials = (p2, *equations, z*(a**2 - b**2) - 1)
                        variables = (z, x, a, b)
                        saturated += 1
                    else:
                        polynomials = (p2, *equations)
                        variables = (x, a, b)
                    basis = sp.groebner(
                        polynomials, *variables, order="grevlex", method="f5b",
                        modulus=DEPLOYED_PRIME,
                    )
                    require(len(basis.polys) == 1 and basis.polys[0].as_expr() == 1,
                            f"direct unit ideal {tau}/{sigma}/{index}")
                    checked += 1

    text = (NODE / "statement.md").read_text()
    require("entire `(4,4,2)` common skeleton" in text and
            "does not close the `(4,3,3)`" in text, "scope fence")
    require(checked == 48 and saturated == 24, "audit coverage")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_H6_COMPLETE_AUDIT_PASS "
        "direct_ideals=48 collision_saturations=24 all_unit=1"
    )


if __name__ == "__main__":
    main()
