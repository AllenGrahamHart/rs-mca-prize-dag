#!/usr/bin/env python3
"""Independent deployed discriminant audit for the cell-0 quartics."""


P = 2130706433
QUADRATICS = (
    (-16711424, -255),
    (-256, -16711423),
    (16776958, 16711423),
    (-65280, 255),
    (256, -16711423),
    (16711424, -255),
    (65280, 255),
    (-16776958, 16711423),
)
EXPECTED_DISCRIMINANTS = {2130641919, 66911228, 2063795205, 64514}


def multiply(left, right):
    output = [0]*(len(left)+len(right)-1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            output[i+j] = (output[i+j]+first*second) % P
    return output


def main():
    discriminants = set()
    quartics = []
    for index in range(0, len(QUADRATICS), 2):
        first = QUADRATICS[index]
        second = QUADRATICS[index+1]
        quartics.append(multiply(
            [first[1] % P, first[0] % P, 1],
            [second[1] % P, second[0] % P, 1],
        ))
        for linear, constant in (first, second):
            discriminant = (linear*linear-4*constant) % P
            discriminants.add(discriminant)
            if pow(discriminant, (P-1)//2, P) != P-1:
                raise RuntimeError("quadratic is reducible")
    if discriminants != EXPECTED_DISCRIMINANTS or len(set(map(tuple, quartics))) != 4:
        raise RuntimeError("factor/discriminant ledger")
    print(
        "RATE_HALF_KB_ONE_LOOP_433_ALIGNED_AUDIT_PASS "
        f"quadratics={len(QUADRATICS)} discriminants={len(discriminants)}"
    )


if __name__ == "__main__":
    main()
