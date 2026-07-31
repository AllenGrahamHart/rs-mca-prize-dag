#!/usr/bin/env python3
"""Independent alternate-chain audit of the complete H8-L-minus cut."""

from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
DE_REPRESENTATIVES = (3, 4, 5, 9, 10, 11)
DEPLOYED_PRIME = 2130706433


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


def audit_values(values, indices, gamma, alpha, first_var, second_var, p4, b):
    checked = 0
    for index in indices:
        equations = []
        for left, right in MATCHINGS[index]:
            y, z = values[left], values[right]
            equations.append(sp.together(gamma*(y*z+1)-alpha*(y+z)).as_numer_denom()[0])
        # Share the second equation, unlike the primary verifier.
        r21 = sp.resultant(equations[1], equations[0], first_var)
        r23 = sp.resultant(equations[1], equations[2], first_var)
        obstruction = sp.factor(sp.resultant(r21, r23, second_var))
        factors = sp.factor_list(obstruction)[1]
        require(factors, f"alternate factor coverage {index}")
        for factor, _ in factors:
            norm = sp.resultant(p4, factor, b)
            integer_norm = abs(int(norm)) if norm.is_Integer else None
            require(norm != 0 and (
                integer_norm is None or integer_norm == 1 or DEPLOYED_PRIME % integer_norm
            ),
                    f"alternate deployed norm {index}")
        checked += 1
    return checked


b, a, x, q = sp.symbols("b a x q")
P4 = b**4-2*b**3+b**2-2*b+1
C = (b-2)*(b**2+1)/b
GAMMA = b+C
ALPHA = -b*C*(b-1)
MATCHINGS = tuple(matchings(tuple(range(6))))


def main() -> None:
    checked = 0
    for sigma in (-1, 1):
        kappa = sigma*C**2
        de_values = (a, kappa/a, x, -x, kappa*x/a**2, -kappa*x/a**2)
        checked += audit_values(
            de_values, DE_REPRESENTATIVES, GAMMA, ALPHA, x, a, P4, b
        )
        df_values = (a, q, sigma*a*q/C**2, -1, q/a, -q/a)
        checked += audit_values(
            df_values, range(15), GAMMA, ALPHA, q, a, P4, b
        )

    text = (NODE / "statement.md").read_text()
    require("five common rows" in text and "does not delete another" in text,
            "scope fence")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_H8L_MINUS_COMPLETE_AUDIT_PASS "
        f"alternate_resultant_chains={checked} all_factor_norms=deployed_nonzero"
    )


if __name__ == "__main__":
    main()
