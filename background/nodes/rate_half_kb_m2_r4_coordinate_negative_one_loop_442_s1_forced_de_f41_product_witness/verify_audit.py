#!/usr/bin/env python3
"""Independently audit the six residual product involution values."""


P = 41
ALPHA, BETA, GAMMA = 16, 16, 7
RESIDUAL = (35, 33, 21, 24, 3, 38)
EXPECTED_PAIRS = {frozenset(pair) for pair in ((35, 24), (33, 38), (21, 3))}


def involution(value):
    denominator = (GAMMA*value-ALPHA) % P
    if not denominator:
        raise RuntimeError("Mobius pole")
    return (ALPHA*value+BETA)*pow(denominator, -1, P) % P


def main():
    pairs = {frozenset((value, involution(value))) for value in RESIDUAL}
    if pairs != EXPECTED_PAIRS:
        raise RuntimeError(f"residual pairs: {pairs}")
    if any(involution(value) == value for value in RESIDUAL):
        raise RuntimeError("fixed residual product")
    common = (23, 10, 31, 5, 36)
    outside = (35, 33, 18, 24, 21, 3, 38)
    if len(set(common+outside)) != 12:
        raise RuntimeError("product injectivity")
    if len({value*value % P for value in (1, 10, 5, 15, 7, 18)}) != 6:
        raise RuntimeError("representative injectivity")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_F41_AUDIT_PASS "
        "pairs=35:24,33:38,21:3 products=12"
    )


if __name__ == "__main__":
    main()
