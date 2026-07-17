#!/usr/bin/env python3
"""Benchmark the exact power-of-two cyclotomic norm recursion on Modal."""

from __future__ import annotations

import json

import modal


app = modal.App("rs-mca-dli-wcl-weight6-recursive-norm-benchmark")
image = modal.Image.debian_slim().pip_install("python-flint")


@app.function(image=image, cpu=2, memory=4096, timeout=600)
def benchmark(exponents: tuple[int, int, int]) -> dict[str, object]:
    import math
    import time

    from flint import fmpz_poly

    order = 1024
    degree = order // 2
    modulus = fmpz_poly([1] + [0] * (degree - 1) + [1])

    def reduce(value: fmpz_poly) -> fmpz_poly:
        return value % modulus

    def multiply(left: fmpz_poly, right: fmpz_poly) -> fmpz_poly:
        return reduce(left * right)

    def monomial(exponent: int) -> fmpz_poly:
        exponent %= order
        coefficients = [0] * degree
        if exponent >= degree:
            coefficients[exponent - degree] = -1
        else:
            coefficients[exponent] = 1
        return fmpz_poly(coefficients)

    def recursive_norm(value: fmpz_poly) -> int:
        """Return Res(X^n+1,value) by repeatedly pairing alpha and -alpha."""

        width = degree
        current = value
        while width > 1:
            half = width // 2
            even = fmpz_poly([int(current[2 * index]) for index in range(half)])
            odd = fmpz_poly(
                [int(current[2 * index + 1]) for index in range(half)]
            )
            paired = even * even - fmpz_poly([0, 1]) * odd * odd
            coefficients = [int(paired[index]) for index in range(width)]
            for index in range(half, width):
                coefficients[index - half] -= coefficients[index]
            current = fmpz_poly(coefficients[:half])
            width = half
        return abs(int(current[0]))

    one = fmpz_poly([1])
    x_value = monomial(exponents[0])
    y_value = monomial(exponents[1])
    d_value = monomial(exponents[2])
    xy_value = multiply(x_value, y_value)
    u_value = one + x_value + y_value
    a_value = x_value + y_value + xy_value
    w_value = reduce(multiply(u_value, a_value) - xy_value - d_value)

    u_squared = multiply(u_value, u_value)
    sigma = -u_squared
    theta = multiply(u_value, w_value)
    product = multiply(multiply(u_squared, u_value), d_value)
    u_power = u_value
    power = 1
    while power < order:
        old_sigma, old_theta, old_product = sigma, theta, product
        sigma = reduce(old_sigma * old_sigma - 2 * old_theta)
        theta = reduce(old_theta * old_theta - 2 * old_product * old_sigma)
        product = reduce(old_product * old_product)
        u_power = reduce(u_power * u_power)
        power *= 2

    first = reduce(sigma - 3 * u_power)
    second = reduce(theta - 3 * multiply(u_power, u_power))

    recursive_started = time.monotonic()
    first_recursive = recursive_norm(first)
    second_recursive = recursive_norm(second)
    u_recursive = recursive_norm(u_value)
    recursive_seconds = time.monotonic() - recursive_started

    generic_started = time.monotonic()
    first_generic = 0 if first == 0 else abs(int(modulus.resultant(first)))
    second_generic = 0 if second == 0 else abs(int(modulus.resultant(second)))
    u_generic = abs(int(modulus.resultant(u_value)))
    generic_seconds = time.monotonic() - generic_started

    if (first_recursive, second_recursive, u_recursive) != (
        first_generic,
        second_generic,
        u_generic,
    ):
        raise AssertionError("recursive norm mismatch")

    common = math.gcd(first_recursive, second_recursive)
    saturated = common
    while saturated:
        removable = math.gcd(saturated, u_recursive)
        if removable == 1:
            break
        saturated //= removable

    return {
        "exponents": list(exponents),
        "first_norm_bits": first_recursive.bit_length(),
        "second_norm_bits": second_recursive.bit_length(),
        "saturated_gcd_bits": saturated.bit_length(),
        "recursive_seconds": round(recursive_seconds, 6),
        "generic_seconds": round(generic_seconds, 6),
        "speedup": round(generic_seconds / recursive_seconds, 3),
        "status": "EXACT_MATCH",
    }


@app.local_entrypoint()
def main() -> None:
    candidates = (
        (1, 2, 3),
        (1, 256, 128),
        (128, 256, 3),
        (255, 257, 341),
        (180, 211, 585),
        (116, 377, 334),
    )
    rows = list(benchmark.map(candidates, return_exceptions=True))
    output = []
    for candidate, row in zip(candidates, rows):
        if isinstance(row, BaseException):
            output.append(
                {
                    "exponents": list(candidate),
                    "status": "REMOTE_ERROR",
                    "error": repr(row),
                }
            )
        else:
            output.append(row)
    print(json.dumps({"schema": "dli-wcl-weight6-recursive-norm-benchmark-v1", "rows": output}, sort_keys=True))
