#!/usr/bin/env python3
"""Exact low-memory modular norm census for profile-(2,10), m=1028, E=3."""

from __future__ import annotations

from hashlib import sha256
from itertools import combinations, product
import json
from math import comb
from pathlib import Path


B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
P_MAX = (B_PRIZE + 1) * 2**128 - 1
COFACTOR = 1028
PRIMES = (
    2147483647,
    2147483629,
    2147483587,
    2147483579,
    2147483563,
    2147483549,
    2147483543,
    2147483497,
    2147483489,
)
M1538_TYPES = (
    (11, 20, -1, -1),
    (14, 15, 1, 1),
    (18, 21, 1, -1),
    (19, 50, -1, 1),
    (36, 49, -1, 1),
)
M1538_QUOTIENTS = (
    94726573109454554355723205753386381132700979257546174561074519931854171378433,
    94726572813333334850450851147142254866189741290919693369950466971809955939327,
    94726573091729884801570429320134633068624255208740225490737339440982526158079,
    94726573091644995672964768686916625315139627899621468752369565038943115036671,
    94726573091678309360928070176107749808616100579343144696817893372730754023169,
)
EXPECTED_DIGEST = "d462adc241981e2e3aa9747a5ba582808d8ebf505e2df6a86fdad2df52a7d3cc"
EXPECTED_MINIMUM = 110037709021719095415927105791028375912712994655842773868558710185217329606913
EXPECTED_MAXIMUM = 120963671460232983862280624800699787448990635276721201666721603772949806841601


def is_prime(number: int) -> bool:
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return number > 1


def polynomial_add(
    first: list[int], second: list[int], multiplier: int = 1
) -> list[int]:
    result = [0] * max(len(first), len(second))
    for index in range(len(result)):
        result[index] = (
            (first[index] if index < len(first) else 0)
            + multiplier * (second[index] if index < len(second) else 0)
        )
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def chebyshev_polynomials(limit: int) -> list[list[int]]:
    polynomials = [[2], [0, 1]]
    for _ in range(2, limit + 1):
        polynomials.append(
            polynomial_add([0] + polynomials[-1], polynomials[-2], -1)
        )
    return polynomials


def trim_mod(polynomial: list[int], prime: int) -> list[int]:
    result = [coefficient % prime for coefficient in polynomial]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def remainder_mod(first: list[int], second: list[int], prime: int) -> list[int]:
    remainder = trim_mod(first, prime)
    divisor = trim_mod(second, prime)
    inverse_lead = pow(divisor[-1], -1, prime)
    while len(remainder) >= len(divisor) and any(remainder):
        factor = remainder[-1] * inverse_lead % prime
        shift = len(remainder) - len(divisor)
        for index, coefficient in enumerate(divisor):
            remainder[index + shift] = (
                remainder[index + shift] - factor * coefficient
            ) % prime
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
        if len(remainder) == 1 and remainder[0] == 0:
            break
    return remainder


def resultant_mod(
    first: list[int], second: list[int], prime: int
) -> int:
    left = trim_mod(first, prime)
    right = trim_mod(second, prime)
    result = 1
    while len(right) > 1:
        left_degree = len(left) - 1
        right_degree = len(right) - 1
        remainder = remainder_mod(left, right, prime)
        if len(remainder) == 1 and remainder[0] == 0:
            return 0
        remainder_degree = len(remainder) - 1
        if left_degree * right_degree % 2:
            result = -result
        result = (
            result
            * pow(right[-1], left_degree - remainder_degree, prime)
        ) % prime
        left, right = right, remainder
    return result * pow(right[0], len(left) - 1, prime) % prime


def exact_norm(modulus: list[int], value: list[int]) -> int:
    residue = 0
    product_modulus = 1
    for prime in PRIMES:
        next_residue = resultant_mod(modulus, value, prime)
        multiplier = (
            (next_residue - residue)
            * pow(product_modulus, -1, prime)
        ) % prime
        residue += product_modulus * multiplier
        product_modulus *= prime
    if product_modulus <= 18**64 or residue > 18**64:
        raise RuntimeError("CRT reconstruction range failed")
    return residue


def autocorrelation_multiplicity(lags: tuple[int, ...]) -> int:
    exponents = tuple(value for lag in lags for value in (lag, 128 - lag))
    return next(
        (
            derivative
            for derivative in range(16)
            if sum(comb(exponent, derivative) for exponent in exponents) % 2
        ),
        16,
    )


def census() -> dict[str, object]:
    if not all(is_prime(prime) for prime in PRIMES):
        raise RuntimeError("CRT primality check failed")
    chebyshev = chebyshev_polynomials(64)
    for row, quotient in zip(M1538_TYPES, M1538_QUOTIENTS):
        first, second, first_sign, second_sign = row
        value = polynomial_add(
            polynomial_add([18], chebyshev[first], first_sign),
            chebyshev[second],
            second_sign,
        )
        if exact_norm(chebyshev[64], value) != 1538 * quotient:
            raise RuntimeError("modular resultant self-test failed")

    traces = [0] + [
        (pow(3, lag, 257) + pow(pow(3, lag, 257), -1, 257)) % 257
        for lag in range(1, 64)
    ]
    rows = []
    for lags in combinations(range(1, 64), 3):
        if autocorrelation_multiplicity(lags) != 4:
            continue
        for signs in product((-1, 1), repeat=3):
            if (18 + sum(sign * traces[lag] for sign, lag in zip(signs, lags))) % 257:
                continue
            value = [18]
            for sign, lag in zip(signs, lags):
                value = polynomial_add(value, chebyshev[lag], sign)
            norm = exact_norm(chebyshev[64], value)
            if norm % COFACTOR:
                raise RuntimeError("cofactor divisibility failed")
            quotient = norm // COFACTOR
            rows.append((lags, signs, quotient))

    ledger = "\n".join(
        ",".join(map(str, lags + signs)) + f":{quotient}"
        for lags, signs, quotient in rows
    )
    payload = {
        "schema": "e1-profile210-m1028-e3-modular-norm-v1",
        "types": len(rows),
        "below": sum(quotient < P_MIN for _, _, quotient in rows),
        "inside": sum(P_MIN <= quotient <= P_MAX for _, _, quotient in rows),
        "above": sum(quotient > P_MAX for _, _, quotient in rows),
        "minimum": min(quotient for _, _, quotient in rows),
        "maximum": max(quotient for _, _, quotient in rows),
        "digest": sha256(ledger.encode("ascii")).hexdigest(),
        "crt_primes": list(PRIMES),
        "crt_modulus": __import__("math").prod(PRIMES),
        "norm_upper": 18**64,
    }
    if payload["types"] != 329 or payload["below"] or payload["inside"]:
        raise RuntimeError(f"energy-three branch not excluded: {payload}")
    if payload["minimum"] != EXPECTED_MINIMUM:
        raise RuntimeError("minimum quotient drift")
    if payload["maximum"] != EXPECTED_MAXIMUM:
        raise RuntimeError("maximum quotient drift")
    if payload["digest"] != EXPECTED_DIGEST:
        raise RuntimeError("norm ledger digest drift")
    return payload


def main(
    output: str = "experiments/prize_resolution/e1_profile210_m1028_e3_modular_norm_result.json",
) -> None:
    payload = census()
    Path(output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        "E1_PROFILE210_M1028_E3_MODULAR_NORM_PASS "
        f"types={payload['types']} above={payload['above']} "
        f"digest={payload['digest']}"
    )


if __name__ == "__main__":
    main()
