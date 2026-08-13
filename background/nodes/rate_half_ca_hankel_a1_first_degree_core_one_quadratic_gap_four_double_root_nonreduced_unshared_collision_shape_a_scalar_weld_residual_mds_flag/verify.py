#!/usr/bin/env python3
"""Replay the residual-MDS degree-drop flag over F_101."""

import argparse


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def multiply(left, right, prime):
    product = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] = (product[i + j] + a * b) % prime
    while len(product) > 1 and product[-1] == 0:
        product.pop()
    return product


def evaluate(polynomial, value, prime):
    result = 0
    for coefficient in reversed(polynomial):
        result = (result * value + coefficient) % prime
    return result


def power_linear(root, exponent, prime):
    result = [1]
    for _ in range(exponent):
        result = multiply(result, [-root % prime, 1], prime)
    return result


def replay(mutation=None):
    mutation = mutation or {}
    prime = mutation.get("prime", 101)
    source = list(range(1, mutation.get("source_stop", 10)))
    incidence_size = mutation.get("incidence_size", 2)
    excess = mutation.get("excess", 3)
    padding_degree = mutation.get("padding_degree", 1)
    parameter_degree = mutation.get("parameter_degree", 5)
    delta = mutation.get("delta", 40)
    padding_root = mutation.get("padding_root", 20)
    residual_root = mutation.get("residual_root", 30)

    require(prime == 101, "fixture field")
    require(len(source) == 9, "fixture source size")
    require(incidence_size == 2 and excess == 3, "fixture profile")
    require(padding_degree == 1 and parameter_degree == 5, "fixture degrees")
    incidence = source[:incidence_size]
    complement = source[incidence_size:]
    require(
        len(set(source + [delta, padding_root, residual_root]))
        == len(source) + 3,
        "fixture point separation",
    )

    actual = [1]
    for point in incidence:
        actual = multiply(actual, [-point % prime, 1], prime)
    padding = power_linear(padding_root, padding_degree, prime)
    generic_degree = incidence_size + padding_degree + excess
    generic_coefficient = [1] + [0] * (generic_degree - 1) + [1]
    row_scalars = [
        evaluate(generic_coefficient, point, prime) for point in source
    ]
    require(all(row_scalars), "nonzero row scalars")

    row_surplus = len(source) - generic_degree
    parity_start = row_surplus + padding_degree - 1
    require(row_surplus == 3 and parity_start == 3, "fixture parity start")

    cases = 0
    parity_checks = 0
    row_checks = 0
    for drop in range(excess + 1):
        residual = power_linear(residual_root, excess - drop, prime)
        fiber = multiply(multiply(actual, padding, prime), residual, prime)
        require(
            len(fiber) - 1 == generic_degree - drop,
            "specialized fiber degree drop",
        )

        residual_values = []
        for point, row_scalar in zip(source, row_scalars):
            fiber_value = evaluate(fiber, point, prime)
            row_value = fiber_value * pow(row_scalar, prime - 2, prime) % prime
            require(
                row_scalar * row_value % prime == fiber_value,
                "row-scalar specialization",
            )
            require(
                (row_value == 0) == (point in incidence),
                "row incidence pattern",
            )
            for parameter in (0, delta, 70):
                biform_value = (
                    fiber_value
                    + pow(parameter - delta, parameter_degree, prime)
                    * evaluate(generic_coefficient, point, prime)
                ) % prime
                monic_row_value = (
                    pow(parameter - delta, parameter_degree, prime)
                    + row_value
                ) % prime
                require(
                    biform_value == row_scalar * monic_row_value % prime,
                    "global row factorization",
                )
                row_checks += 1
            if point not in incidence:
                denominator = (
                    evaluate(actual, point, prime)
                    * evaluate(padding, point, prime)
                ) % prime
                require(denominator, "residual parity denominator")
                residual_values.append(
                    (
                        point,
                        row_scalar
                        * row_value
                        * pow(denominator, prime - 2, prime)
                        % prime,
                    )
                )

        require(
            all(
                value == evaluate(residual, point, prime)
                for point, value in residual_values
            ),
            "residual value reconstruction",
        )
        parities = []
        for power in range(parity_start + drop + 1):
            value = 0
            for point, residual_value in residual_values:
                derivative = 1
                for other, _ in residual_values:
                    if other != point:
                        derivative = derivative * (point - other) % prime
                value = (
                    value
                    + residual_value
                    * pow(point, power, prime)
                    * pow(derivative, prime - 2, prime)
                ) % prime
            parities.append(value)
            parity_checks += 1
        require(
            parities[:parity_start] == [0] * parity_start,
            "base residual-MDS parities",
        )
        require(
            parities[parity_start:parity_start + drop] == [0] * drop,
            "extra residual-MDS zero run",
        )
        require(
            parities[parity_start + drop] == residual[-1] == 1,
            "first nonzero residual-MDS parity",
        )
        cases += 1

    require(cases == 4, "fixture case count")
    require(parity_checks == 22, "fixture parity count")
    require(row_checks == 108, "fixture row check count")
    return cases, parity_checks, row_checks


def tamper_selftest():
    mutations = [
        {"prime": 103},
        {"source_stop": 9},
        {"incidence_size": 3},
        {"excess": 2},
        {"padding_degree": 2},
        {"parameter_degree": 4},
        {"padding_root": 9},
        {"residual_root": 8},
    ]
    rejected = 0
    for mutation in mutations:
        try:
            replay(mutation)
        except (AssertionError, IndexError):
            rejected += 1
    require(rejected == len(mutations), "hostile mutation rejection")
    return rejected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    cases, parities, rows = replay()
    suffix = ""
    if args.tamper_selftest:
        suffix = f" mutations={tamper_selftest()}/8"
    print(
        "RATE_HALF_SHAPE_A_SCALAR_WELD_RESIDUAL_MDS_FLAG_PASS "
        f"cases={cases} parities={parities} rows={rows}{suffix}"
    )


if __name__ == "__main__":
    main()
