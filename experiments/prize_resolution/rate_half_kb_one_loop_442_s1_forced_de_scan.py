#!/usr/bin/env python3
"""Scan the canonical S1 forced-DE sextic cell on the F_41 common witness."""

import math


P = 41
B = 10
C = 5
MATE = 18
ALPHA = 16
BETA = 16
GAMMA = 7
DELTA = (ALPHA*ALPHA+BETA*GAMMA) % P


def multiply(left, right):
    output = [0]*(len(left)+len(right)-1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            output[i+j] = (output[i+j]+first*second) % P
    return output


def residual_form(d, s):
    factors = (
        (d, C*MATE),
        (1, C*s*d),
        (1, d*d),
        (1, -s*d*d),
        (1, 0, -MATE*MATE*s*s),
    )
    coefficients = [1]
    for factor in factors:
        coefficients = multiply(coefficients, factor)
    return coefficients


def equation(coefficients, ell):
    transformed = 0
    for j in range(7):
        for q in range(max(0, ell-(6-j)), min(ell, j)+1):
            p = ell-q
            transformed += (
                coefficients[j]
                * math.comb(6-j, p)*math.comb(j, q)
                * pow(ALPHA, 6-j-p, P)*pow(BETA, p, P)
                * pow(GAMMA, j-q, P)*pow(-ALPHA, q, P)
            )
    return (transformed-pow(DELTA, 3, P)*coefficients[ell]) % P


def guarded(d, s):
    e = -MATE*pow(d, -1, P) % P
    f = s*d % P
    representative_squares = tuple(
        value*value % P for value in (1, B, C, d, e, f)
    )
    if len(set(representative_squares)) != 6:
        return False

    common = (-B*B, B, -B, C, -C)
    outside = (C*e, -C*f, -d*e, d*f, -d*d, e*f, -e*f)
    return len({value % P for value in common+outside}) == 12


def main():
    first_three = []
    invariant = []
    accepted = []
    for d in range(1, P):
        for s in range(1, P):
            coefficients = residual_form(d, s)
            if all(equation(coefficients, ell) == 0 for ell in range(3)):
                first_three.append((d, s))
                if all(equation(coefficients, ell) == 0
                       for ell in range(7)):
                    invariant.append((d, s))
                    if guarded(d, s):
                        accepted.append((d, s))

    expected = [(15, 34)]
    if first_three != expected or invariant != expected or accepted != expected:
        raise RuntimeError(
            f"unexpected survivor sets: {first_three}, {invariant}, {accepted}"
        )
    coefficients = residual_form(15, 34)
    if coefficients != [15, 27, 7, 12, 23, 1, 17]:
        raise RuntimeError(f"witness coefficients: {coefficients}")

    print(
        "S1_FORCED_DE_F41_SCAN_PASS "
        f"tested={(P-1)**2} first_three={len(first_three)} "
        f"invariant={len(invariant)} guarded={len(accepted)} "
        "d=15 e=7 f=18 s=34"
    )


if __name__ == "__main__":
    main()
