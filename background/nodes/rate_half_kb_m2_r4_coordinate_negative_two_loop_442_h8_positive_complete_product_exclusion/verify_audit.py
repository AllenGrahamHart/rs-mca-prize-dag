#!/usr/bin/env python3
"""Audit the positive-H8 cut with the alternate resultant projection."""

from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
REPRESENTATIVES = (3, 4, 5, 9, 10, 11)
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
        for tail in matchings(items[1:index] + items[index + 1:]):
            yield ((first, items[index]),) + tail


def audit_values(values, indices, first_var, gamma, alpha, beta, p4, b):
    checked = 0
    for index in indices:
        equations = []
        for left, right in MATCHINGS[index]:
            y, z = values[left], values[right]
            equation = gamma*y*z - alpha*(y + z) - beta
            equations.append(sp.together(equation).as_numer_denom()[0])
        # This audit shares equation 1; the primary verifier shares equation 0.
        r21 = sp.resultant(equations[1], equations[0], first_var)
        r23 = sp.resultant(equations[1], equations[2], first_var)
        obstruction = sp.factor(sp.resultant(r21, r23, A))
        require(obstruction != 0, f"alternate projection {index}")
        factors = sp.factor_list(obstruction)[1]
        require(factors, f"alternate factor coverage {index}")
        for factor, _ in factors:
            norm = sp.cancel(sp.resultant(p4, factor, b))
            numerator, denominator = norm.as_numer_denom()
            require(norm != 0 and numerator.is_Integer and denominator.is_Integer,
                    f"alternate exact norm {index}")
            require(int(numerator) % DEPLOYED_PRIME and
                    int(denominator) % DEPLOYED_PRIME,
                    f"alternate deployed norm {index}")
        checked += 1
    return checked


B, A, X, Q = sp.symbols("b a x q")
P4 = B**4 - 2*B**3 - 5*B**2 - 2*B + 1
C = (-B**2 + 3*B + 3) / 2
P = (5*B**3 - 16*B**2 + 8*B + 8) / 23
GAMMA = B**2 - B*C + B + C
ALPHA = B*C*(B**2 + 1)
BETA = -B**2*C*(B**2 + B*C - B + C)
MATCHINGS = tuple(matchings(tuple(range(6))))


def main() -> None:
    checked = 0
    for sigma in (-1, 1):
        cd_values = (A, sigma*P*A/C**2, X, -X, A*X/P, -A*X/P)
        checked += audit_values(
            cd_values, REPRESENTATIVES, X, GAMMA, ALPHA, BETA, P4, B
        )
        de_values = (A, sigma*P*C**2/A, X, -X,
                     sigma*P*C**2*X/A**2, -sigma*P*C**2*X/A**2)
        checked += audit_values(
            de_values, REPRESENTATIVES, X, GAMMA, ALPHA, BETA, P4, B
        )
        df_values = (A, Q, sigma*A*Q/C**2, -P, P*Q/A, -P*Q/A)
        checked += audit_values(
            df_values, range(15), Q, GAMMA, ALPHA, BETA, P4, B
        )

    text = (NODE / "statement.md").read_text()
    require("Only `H6,tau=-1` and" in text and
            "does not delete either `H6`" in text, "scope fence")
    require(checked == 54, "complete alternate coverage")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_H8_POSITIVE_AUDIT_PASS "
        "alternate_resultant_chains=54 all_factor_norms=deployed_nonzero"
    )


if __name__ == "__main__":
    main()
