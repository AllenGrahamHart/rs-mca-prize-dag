#!/usr/bin/env python3
"""Independent dual-RS audit for the all-excess parameter gate."""

from functools import reduce


def evaluate(polynomial, value, modulus):
    result = 0
    for coefficient in reversed(polynomial):
        result = (result * value + coefficient) % modulus
    return result


def replay():
    modulus = 127
    slopes = list(range(2, 13))
    parameter_degree = 3
    x_degree = 4
    coefficient_polynomials = [
        [(i + 2) * (j + 3) % modulus for j in range(parameter_degree + 1)]
        for i in range(x_degree + 1)
    ]
    fibers = [
        [evaluate(polynomial, slope, modulus) for polynomial in coefficient_polynomials]
        for slope in slopes
    ]

    checks = 0
    for coefficient in range(x_degree + 1):
        for power in range(len(slopes) - parameter_degree - 1):
            total = 0
            for slope_index, slope in enumerate(slopes):
                derivative = 1
                for other in slopes:
                    if other != slope:
                        derivative = derivative * (slope - other) % modulus
                total += (
                    fibers[slope_index][coefficient]
                    * pow(slope, power, modulus)
                    * pow(derivative, modulus - 2, modulus)
                )
            assert total % modulus == 0
            checks += 1

    fibers[0][0] = (fibers[0][0] + 1) % modulus
    assert any(
        sum(
            fibers[index][0]
            * pow(slope, power, modulus)
            * pow(
                reduce(
                    lambda left, other: left * (slope - other) % modulus,
                    (other for other in slopes if other != slope),
                    1,
                ),
                modulus - 2,
                modulus,
            )
            for index, slope in enumerate(slopes)
        ) % modulus
        for power in range(len(slopes) - parameter_degree - 1)
    )
    return checks


if __name__ == "__main__":
    checks = replay()
    print(
        "RATE_HALF_SHAPE_A_ALL_EXCESS_PARAMETER_MDS_GATE_AUDIT_PASS "
        f"checks={checks}"
    )
