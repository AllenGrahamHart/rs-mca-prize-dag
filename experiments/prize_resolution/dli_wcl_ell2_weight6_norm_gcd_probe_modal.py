#!/usr/bin/env python3
"""Benchmark the weight-six triple-cubic norm-gcd obstruction on Modal."""

from __future__ import annotations

import json
from pathlib import Path

import modal


OUTPUT = Path(__file__).with_name("dli_wcl_ell2_weight6_norm_gcd_probe_result.json")
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
def main(factor_only: bool = False) -> None:
    if factor_only:
        result = json.loads(OUTPUT.read_text())
        rows = result["rows"]
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
            "scope": "route benchmark only; deterministic candidates, not a certificate",
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
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
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
            },
            sort_keys=True,
        )
    )
