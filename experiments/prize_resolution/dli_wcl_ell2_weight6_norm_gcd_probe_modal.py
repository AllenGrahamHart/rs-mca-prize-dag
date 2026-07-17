#!/usr/bin/env python3
"""Benchmark the weight-six triple-cubic norm-gcd obstruction on Modal."""

from __future__ import annotations

import json
from pathlib import Path
from random import Random

import modal


OUTPUT = Path(__file__).with_name("dli_wcl_ell2_weight6_norm_gcd_probe_result.json")
RANDOM_OUTPUT = Path(__file__).with_name(
    "dli_wcl_ell2_weight6_random_adversary_result.json"
)
app = modal.App("rs-mca-dli-wcl-ell2-weight6-norm-gcd-probe")
image = modal.Image.debian_slim().pip_install("python-flint")
factor_image = modal.Image.debian_slim().apt_install("pari-gp")


def candidate_exponents(order: int) -> list[tuple[int, int, int]]:
    raw = (
        (1, 2, 3),
        (1, order // 4, order // 8),
        (order // 8, order // 4, 3),
        (order // 4 - 1, order // 4 + 1, order // 3),
    )
    half = order // 2
    return [
        candidate
        for candidate in raw
        if candidate[0] not in (0, half)
        and candidate[1] not in (0, half)
        and candidate[0] != candidate[1]
        and (candidate[0] - candidate[1]) % order != half
    ]


def random_candidate_exponents(
    order: int, count: int, seed: int
) -> list[tuple[int, int, int]]:
    rng = Random(seed)
    half = order // 2
    rows: set[tuple[int, int, int]] = set()
    while len(rows) < count:
        x, y, d = (rng.randrange(order) for _ in range(3))
        if x in (0, half) or y in (0, half):
            continue
        if x == y or (x - y) % order == half:
            continue
        rows.add((x, y, d))
    return sorted(rows)


@app.function(image=image, cpu=1, memory=1024, timeout=120, max_containers=32)
def same_embedding_test(
    payload: tuple[tuple[int, int, int], tuple[int, ...]]
) -> dict[str, object]:
    exponents, primes = payload

    def prime_factors(value: int) -> list[int]:
        factors = []
        divisor = 2
        while divisor * divisor <= value:
            if value % divisor == 0:
                factors.append(divisor)
                while value % divisor == 0:
                    value //= divisor
            divisor += 1
        if value > 1:
            factors.append(value)
        return factors

    def primitive_root(prime: int) -> int:
        factors = prime_factors(prime - 1)
        for candidate in range(2, prime):
            if all(
                pow(candidate, (prime - 1) // factor, prime) != 1
                for factor in factors
            ):
                return candidate
        raise AssertionError("primitive root not found")

    order = 1024
    rows = []
    for prime in primes:
        assert (prime - 1) % order == 0
        omega = pow(primitive_root(prime), (prime - 1) // order, prime)
        subgroup = [pow(omega, exponent, prime) for exponent in range(order)]
        subgroup_set = set(subgroup)
        exponent_of = {value: exponent for exponent, value in enumerate(subgroup)}
        embedding_hits = []
        guarded_hits = []
        for dilation in range(1, order, 2):
            x = pow(omega, dilation * exponents[0], prime)
            y = pow(omega, dilation * exponents[1], prime)
            d = pow(omega, dilation * exponents[2], prime)
            u = (1 + x + y) % prime
            if u == 0:
                continue
            a_value = (x + y + x * y) % prime
            b_value = x * y % prime
            w_value = (u * a_value - b_value - d) % prime
            sigma = -(u * u) % prime
            theta = u * w_value % prime
            product_value = pow(u, 3, prime) * d % prime
            u_power = u
            power = 1
            while power < order:
                old_sigma, old_theta, old_product = sigma, theta, product_value
                sigma = (old_sigma * old_sigma - 2 * old_theta) % prime
                theta = (
                    old_theta * old_theta - 2 * old_product * old_sigma
                ) % prime
                product_value = old_product * old_product % prime
                u_power = u_power * u_power % prime
                power *= 2
            first = (sigma - 3 * u_power) % prime
            second = (theta - 3 * u_power * u_power) % prime
            if first or second:
                continue
            embedding_hits.append(dilation)

            c_value = w_value * pow(u, -1, prime) % prime
            roots = [
                z
                for z in subgroup
                if (pow(z, 3, prime) + u * z * z + c_value * z - d)
                % prime
                == 0
            ]
            first_triple = {1, x, y}
            root_set = set(roots)
            union = first_triple | root_set
            guarded = (
                len(first_triple) == 3
                and len(root_set) == 3
                and first_triple.isdisjoint(root_set)
                and len(union) == 6
                and all((-value) % prime not in union for value in union)
                and root_set <= subgroup_set
            )
            if guarded:
                assert sum(union) % prime == 0
                assert sum(pow(value, 3, prime) for value in union) % prime == 0
                guarded_hits.append(
                    {
                        "dilation": dilation,
                        "union_exponents": sorted(exponent_of[value] for value in union),
                    }
                )
        rows.append(
            {
                "prime": str(prime),
                "v2_prime_minus_1": (prime - 1 & -(prime - 1)).bit_length() - 1,
                "embedding_hits": embedding_hits,
                "guarded_hits": guarded_hits,
            }
        )
    return {"exponents": list(exponents), "rows": rows}


@app.function(image=image, cpu=2, memory=4096, timeout=600, max_containers=32)
def norm_gcd(payload: tuple[int, tuple[int, int, int]]) -> dict[str, object]:
    import math
    import sys
    import time

    from flint import fmpz_poly

    sys.set_int_max_str_digits(0)

    order, exponents = payload
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

    started = time.monotonic()
    one = fmpz_poly([1])
    x_value = monomial(exponents[0])
    y_value = monomial(exponents[1])
    d_value = monomial(exponents[2])
    xy_value = multiply(x_value, y_value)
    u_value = one + x_value + y_value
    a_value = x_value + y_value + xy_value
    b_value = xy_value
    w_value = reduce(multiply(u_value, a_value) - b_value - d_value)

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
    recurrence_seconds = time.monotonic() - started

    first_started = time.monotonic()
    first_norm = 0 if first == 0 else abs(int(modulus.resultant(first)))
    first_seconds = time.monotonic() - first_started
    second_started = time.monotonic()
    second_norm = 0 if second == 0 else abs(int(modulus.resultant(second)))
    second_seconds = time.monotonic() - second_started
    common = math.gcd(first_norm, second_norm)
    u_norm = abs(int(modulus.resultant(u_value)))
    saturated_common = common
    while saturated_common:
        removable = math.gcd(saturated_common, u_norm)
        if removable == 1:
            break
        saturated_common //= removable

    coefficient_bits = max(
        (
            abs(int(polynomial[index])).bit_length()
            for polynomial in (first, second)
            for index in range(len(polynomial))
        ),
        default=0,
    )
    return {
        "order": order,
        "exponents": list(exponents),
        "status": "COMPLETE",
        "first_zero": first == 0,
        "second_zero": second == 0,
        "coefficient_bits": coefficient_bits,
        "first_norm_bits": first_norm.bit_length(),
        "second_norm_bits": second_norm.bit_length(),
        "u_norm_bits": u_norm.bit_length(),
        "gcd": str(common),
        "gcd_bits": common.bit_length(),
        "u_saturated_gcd": str(saturated_common),
        "u_saturated_gcd_bits": saturated_common.bit_length(),
        "recurrence_seconds": round(recurrence_seconds, 6),
        "first_norm_seconds": round(first_seconds, 6),
        "second_norm_seconds": round(second_seconds, 6),
        "seconds": round(time.monotonic() - started, 6),
    }


@app.function(
    image=factor_image,
    cpu=2,
    memory=4096,
    timeout=600,
    max_containers=32,
)
def factor_gcd(value_text: str) -> dict[str, object]:
    import subprocess
    import sys
    import time

    sys.set_int_max_str_digits(0)
    started = time.monotonic()
    program = (
        f"n={value_text};f=factor(n);"
        'for(i=1,matsize(f)[1],print(f[i,1]," : ",f[i,2]));quit()\n'
    )
    try:
        completed = subprocess.run(
            ["gp", "-q", "-s", "1073741824"],
            input=program,
            text=True,
            capture_output=True,
            timeout=580,
            check=True,
        )
    except subprocess.TimeoutExpired as exc:
        return {
            "gcd": value_text,
            "status": "TIMEOUT",
            "seconds": round(time.monotonic() - started, 6),
            "stdout_tail": (exc.stdout or "")[-1000:],
            "stderr_tail": (exc.stderr or "")[-1000:],
        }

    factors = []
    product = 1
    for line in completed.stdout.splitlines():
        if ":" not in line:
            continue
        prime_text, exponent_text = (part.strip() for part in line.split(":", 1))
        prime = int(prime_text)
        exponent = int(exponent_text)
        quotient = prime - 1
        valuation = 0
        while quotient and quotient % 2 == 0:
            quotient //= 2
            valuation += 1
        factors.append(
            {
                "prime": prime_text,
                "prime_bits": prime.bit_length(),
                "exponent": exponent,
                "v2_prime_minus_1": valuation,
            }
        )
        product *= prime**exponent
    status = "COMPLETE" if product == int(value_text) else "INCOMPLETE"
    return {
        "gcd": value_text,
        "status": status,
        "factors": factors,
        "seconds": round(time.monotonic() - started, 6),
    }


@app.local_entrypoint()
def main(
    factor_only: bool = False,
    random_count: int = 0,
    seed: int = 20260716,
) -> None:
    if factor_only:
        source = RANDOM_OUTPUT if random_count else OUTPUT
        result = json.loads(source.read_text())
        rows = result["rows"]
    else:
        if random_count:
            payloads = [
                (1024, candidate)
                for candidate in random_candidate_exponents(
                    1024, random_count, seed
                )
            ]
        else:
            orders = (64, 128, 256, 512, 1024)
            payloads = [
                (order, candidate)
                for order in orders
                for candidate in candidate_exponents(order)
            ]
        remote_rows = list(norm_gcd.map(payloads, return_exceptions=True))
        rows: list[dict[str, object]] = []
        for payload, row in zip(payloads, remote_rows):
            if isinstance(row, BaseException):
                rows.append(
                    {
                        "order": payload[0],
                        "exponents": list(payload[1]),
                        "status": "REMOTE_ERROR",
                        "error": repr(row),
                    }
                )
            else:
                rows.append(row)
        result = {
            "schema": "dli-wcl-ell2-weight6-norm-gcd-probe-v1",
            "scope": (
                "route falsification sample only; deterministic random candidates, not a certificate"
                if random_count
                else "route benchmark only; deterministic candidates, not a certificate"
            ),
            "random_count": random_count,
            "seed": seed if random_count else None,
            "rows": rows,
        }

    distinct_gcds = sorted(
        {
            row["u_saturated_gcd"]
            for row in rows
            if row["status"] == "COMPLETE" and int(row["u_saturated_gcd"]) > 1
        },
        key=int,
    )
    remote_factors = list(factor_gcd.map(distinct_gcds, return_exceptions=True))
    factor_rows = []
    for value, row in zip(distinct_gcds, remote_factors):
        if isinstance(row, BaseException):
            factor_rows.append(
                {"gcd": value, "status": "REMOTE_ERROR", "error": repr(row)}
            )
        else:
            factor_rows.append(row)
    result["factor_rows"] = factor_rows
    factor_map = {row["gcd"]: row for row in factor_rows}
    same_embedding_payloads = []
    for row in rows:
        factor_row = factor_map.get(str(row.get("u_saturated_gcd", "")))
        if not factor_row:
            continue
        primes = tuple(
            int(factor["prime"])
            for factor in factor_row.get("factors", [])
            if int(factor["v2_prime_minus_1"]) >= 11
        )
        if primes:
            same_embedding_payloads.append((tuple(row["exponents"]), primes))
    remote_same = list(
        same_embedding_test.map(same_embedding_payloads, return_exceptions=True)
    )
    same_embedding_rows = []
    for payload, row in zip(same_embedding_payloads, remote_same):
        if isinstance(row, BaseException):
            same_embedding_rows.append(
                {
                    "exponents": list(payload[0]),
                    "status": "REMOTE_ERROR",
                    "error": repr(row),
                }
            )
        else:
            same_embedding_rows.append({"status": "COMPLETE", **row})
    result["same_embedding_rows"] = same_embedding_rows
    destination = RANDOM_OUTPUT if random_count else OUTPUT
    destination.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    completed = [row for row in rows if row["status"] == "COMPLETE"]
    print(
        "DLI_WCL_ELL2_WEIGHT6_NORM_GCD_PROBE "
        + json.dumps(
            {
                "rows": len(rows),
                "complete": len(completed),
                "zero_pairs": sum(
                    bool(row["first_zero"]) and bool(row["second_zero"])
                    for row in completed
                ),
                "max_coefficient_bits": max(
                    (int(row["coefficient_bits"]) for row in completed), default=0
                ),
                "max_gcd_bits": max(
                    (int(row["gcd_bits"]) for row in completed), default=0
                ),
                "max_u_saturated_gcd_bits": max(
                    (int(row["u_saturated_gcd_bits"]) for row in completed),
                    default=0,
                ),
                "max_seconds": max(
                    (float(row["seconds"]) for row in completed), default=0
                ),
                "factor_complete": sum(
                    row["status"] == "COMPLETE" for row in factor_rows
                ),
                "factor_timeouts": sum(
                    row["status"] == "TIMEOUT" for row in factor_rows
                ),
                "max_factor_v2": max(
                    (
                        int(factor["v2_prime_minus_1"])
                        for row in factor_rows
                        for factor in row.get("factors", [])
                    ),
                    default=0,
                ),
                "same_embedding_cases": sum(
                    len(row.get("rows", [])) for row in same_embedding_rows
                ),
                "same_embedding_hits": sum(
                    len(prime_row["embedding_hits"])
                    for row in same_embedding_rows
                    for prime_row in row.get("rows", [])
                ),
                "guarded_hits": sum(
                    len(prime_row["guarded_hits"])
                    for row in same_embedding_rows
                    for prime_row in row.get("rows", [])
                ),
            },
            sort_keys=True,
        )
    )
