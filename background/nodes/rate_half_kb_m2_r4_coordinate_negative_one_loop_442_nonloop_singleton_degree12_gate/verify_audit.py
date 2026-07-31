#!/usr/bin/env python3
"""Independent finite-field audit of the degree-12 gate."""


def factors(value, prime):
    return (
        (value**3-value**2-value-1) % prime,
        (value**3+value**2+value-1) % prime,
        (value**6-2*value**5+7*value**4-8*value**3
         +7*value**2-2*value+1) % prime,
    )


def main():
    roots_41 = {
        value: tuple(index for index, result in enumerate(factors(value, 41))
                     if result == 0)
        for value in range(1, 41)
        if 0 in factors(value, 41)
    }
    expected = {10: (2,), 13: (1,), 19: (0,), 37: (2,)}
    if roots_41 != expected:
        raise RuntimeError("F_41 degree-12 roots")
    if factors(10, 41)[2] != 0:
        raise RuntimeError("known common witness")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_DEGREE12_AUDIT_PASS "
        "field=41 roots=4 witness_b=10 sextic=1"
    )


if __name__ == "__main__":
    main()
