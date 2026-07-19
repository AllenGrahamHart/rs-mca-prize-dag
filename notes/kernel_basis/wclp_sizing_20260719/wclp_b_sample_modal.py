#!/usr/bin/env python3
"""wclp_b_sample_modal.py -- SIZING PILOT for the (2,7) recursive-norm census.

Runs a deterministic sample of weight-7 router candidates (selected quadruple
{1,x,y,z} normalized, complementary triple with free product d = zeta^c;
identical cleared-cubic machinery as the audited (2,6) certificate:
  u = 1+x+y+z, A = e2{1,x,y,z}, B = e3{1,x,y,z}, w = uA - B - d,
  sigma_1 = -u^2, theta_1 = u*w, e3 = u^3 d, ten doublings,
  F = sigma_1024 - 3u^1024, G = theta_1024 - 3u^2048,
  recursive power-of-two norms, gcd, Norm(u)-saturation)
with per-candidate phase timing, plus one weight-6 control candidate per shard
(same container, audited pipeline) to calibrate against the (2,6) production
rate of 0.770 s/row.  Distinct saturated gcds are sample-factored with a 30s
per-value gp cap to size the factor stage.

No volume, no writes, no certificate claim.  cpu=1 so wall == CPU per row.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import modal

ORDER = 1024
DEGREE = 512
SHARDS = 10
W7_PER_SHARD = 16
FACTOR_SAMPLES_PER_SHARD = 6
FACTOR_TIMEOUT = 30
SEED = 20260719
OUTPUT = Path(__file__).with_name("wclp_b_sample_result.json")

app = modal.App("wclp-b-weight7-sizing-sample")
image = modal.Image.debian_slim().pip_install("python-flint").apt_install("pari-gp")


def legal_tuple(values: tuple[int, ...]) -> bool:
    if any(v % ORDER in (0, ORDER // 2) for v in values):
        return False
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if (values[i] - values[j]) % ORDER in (0, ORDER // 2):
                return False
    return True


def sample_candidates() -> tuple[list[tuple[int, int, int, int]], list[tuple[int, int, int]]]:
    import random

    rng = random.Random(SEED)
    w7: list[tuple[int, int, int, int]] = []
    while len(w7) < SHARDS * W7_PER_SHARD:
        a, b, e = (rng.randrange(1, ORDER) for _ in range(3))
        if legal_tuple((a, b, e)):
            w7.append((a, b, e, rng.randrange(ORDER)))
    w6: list[tuple[int, int, int]] = []
    while len(w6) < SHARDS:
        a, b = (rng.randrange(1, ORDER) for _ in range(2))
        if legal_tuple((a, b)):
            w6.append((a, b, rng.randrange(ORDER)))
    return w7, w6


@app.function(image=image, cpu=1, memory=4096, timeout=280, max_containers=12)
def measure_shard(
    payload: tuple[int, list[tuple[int, int, int, int]], tuple[int, int, int]],
) -> dict[str, object]:
    import math
    import subprocess
    import sys
    import time as time_mod

    from flint import fmpz_poly

    sys.set_int_max_str_digits(0)
    shard_index, w7_candidates, w6_candidate = payload
    shard_started = time_mod.monotonic()

    modulus = fmpz_poly([1] + [0] * (DEGREE - 1) + [1])

    def reduce(value: fmpz_poly) -> fmpz_poly:
        return value % modulus

    def multiply(left: fmpz_poly, right: fmpz_poly) -> fmpz_poly:
        return reduce(left * right)

    def monomial(exponent: int) -> fmpz_poly:
        coefficients = [0] * DEGREE
        exponent %= ORDER
        if exponent >= DEGREE:
            coefficients[exponent - DEGREE] = -1
        else:
            coefficients[exponent] = 1
        return fmpz_poly(coefficients)

    def recursive_norm(value: fmpz_poly) -> int:
        width = DEGREE
        current = value
        while width > 1:
            next_width = width // 2
            even = fmpz_poly([int(current[2 * i]) for i in range(next_width)])
            odd = fmpz_poly([int(current[2 * i + 1]) for i in range(next_width)])
            paired = even * even - fmpz_poly([0, 1]) * odd * odd
            coefficients = [int(paired[i]) for i in range(width)]
            for i in range(next_width, width):
                coefficients[i - next_width] -= coefficients[i]
            current = fmpz_poly(coefficients[:next_width])
            width = next_width
        return abs(int(current[0]))

    one = fmpz_poly([1])

    def run_candidate(selected: tuple[int, ...], c: int) -> dict[str, object]:
        """selected = exponents of the non-1 selected roots (2 for weight 6,
        3 for weight 7); complement is always a triple with product zeta^c."""
        t0 = time_mod.monotonic()
        roots = [monomial(v) for v in selected]
        d_value = monomial(c)
        # elementary symmetric functions of {1} + roots
        e1 = one
        e2 = fmpz_poly([0])
        e3 = fmpz_poly([0])
        for r in roots:
            e3 = reduce(e3 + multiply(e2, r))
            e2 = reduce(e2 + multiply(e1, r))
            e1 = reduce(e1 + r)
        u_value = e1
        w_value = reduce(multiply(u_value, e2) - e3 - d_value)
        u_squared = multiply(u_value, u_value)
        sigma = -u_squared
        theta = multiply(u_value, w_value)
        product_value = multiply(multiply(u_squared, u_value), d_value)
        u_power = u_value
        power = 1
        while power < ORDER:
            old_sigma, old_theta, old_product = sigma, theta, product_value
            sigma = reduce(old_sigma * old_sigma - 2 * old_theta)
            theta = reduce(old_theta * old_theta - 2 * old_product * old_sigma)
            product_value = reduce(old_product * old_product)
            u_power = reduce(u_power * u_power)
            power *= 2
        first = reduce(sigma - 3 * u_power)
        second = reduce(theta - 3 * multiply(u_power, u_power))
        recurrence_seconds = time_mod.monotonic() - t0

        first_zero = first == 0
        second_zero = second == 0
        t1 = time_mod.monotonic()
        first_norm = 0 if first_zero else recursive_norm(first)
        norm_first_seconds = time_mod.monotonic() - t1
        t2 = time_mod.monotonic()
        second_norm = 0 if second_zero else recursive_norm(second)
        norm_second_seconds = time_mod.monotonic() - t2
        t3 = time_mod.monotonic()
        u_norm = recursive_norm(u_value)
        norm_u_seconds = time_mod.monotonic() - t3
        if u_norm == 0:
            raise AssertionError("char-zero selected-sum vanisher")
        t4 = time_mod.monotonic()
        common = math.gcd(first_norm, second_norm)
        raw_gcd_bits = common.bit_length()
        while common:
            removable = math.gcd(common, u_norm)
            if removable == 1:
                break
            common //= removable
        saturate_seconds = time_mod.monotonic() - t4
        return {
            "selected": list(selected),
            "c": c,
            "first_zero": first_zero,
            "second_zero": second_zero,
            "first_norm_bits": first_norm.bit_length(),
            "second_norm_bits": second_norm.bit_length(),
            "u_norm_bits": u_norm.bit_length(),
            "raw_gcd_bits": raw_gcd_bits,
            "saturated_gcd_bits": common.bit_length(),
            "saturated_gcd": str(common) if 1 < common else None,
            "recurrence_seconds": round(recurrence_seconds, 6),
            "norm_first_seconds": round(norm_first_seconds, 6),
            "norm_second_seconds": round(norm_second_seconds, 6),
            "norm_u_seconds": round(norm_u_seconds, 6),
            "saturate_seconds": round(saturate_seconds, 6),
            "row_seconds": round(time_mod.monotonic() - t0, 6),
        }

    w6_row = run_candidate(tuple(w6_candidate[:2]), w6_candidate[2])
    w7_rows = [run_candidate(tuple(cand[:3]), cand[3]) for cand in w7_candidates]

    # gp startup baseline
    t = time_mod.monotonic()
    subprocess.run(
        ["gp", "-q", "-s", "536870912"],
        input="f=factor(2);quit()\n",
        text=True,
        capture_output=True,
        timeout=30,
        check=True,
    )
    gp_startup_seconds = round(time_mod.monotonic() - t, 6)

    # sample-factor distinct saturated gcds (weight-7 rows only)
    distinct = sorted(
        {int(row["saturated_gcd"]) for row in w7_rows if row["saturated_gcd"]}
    )
    factor_rows = []
    for value in distinct[:FACTOR_SAMPLES_PER_SHARD]:
        if time_mod.monotonic() - shard_started > 200:
            factor_rows.append({"gcd_bits": value.bit_length(), "status": "SKIPPED_BUDGET"})
            continue
        program = (
            f"n={value};f=factor(n);"
            "for(j=1,matsize(f)[1],if(!isprime(f[j,1]),error(\"nonprime\"));"
            "print(f[j,1],\":\",f[j,2]));quit()\n"
        )
        t = time_mod.monotonic()
        try:
            completed = subprocess.run(
                ["gp", "-q", "-s", "1073741824"],
                input=program,
                text=True,
                capture_output=True,
                timeout=FACTOR_TIMEOUT,
                check=True,
            )
            factors = []
            for line in completed.stdout.splitlines():
                if ":" in line:
                    p_text, e_text = line.split(":", 1)
                    factors.append((int(p_text), int(e_text)))
            if math.prod(p**e for p, e in factors) != value:
                raise AssertionError("incomplete factorization")
            factor_rows.append(
                {
                    "gcd_bits": value.bit_length(),
                    "factor_count": len(factors),
                    "max_prime_bits": max(p.bit_length() for p, _ in factors),
                    "max_v2_prime_minus_1": max(
                        ((p - 1 & -(p - 1)).bit_length() - 1 for p, _ in factors)
                    ),
                    "factor_seconds": round(time_mod.monotonic() - t, 6),
                    "status": "COMPLETE",
                }
            )
        except subprocess.TimeoutExpired:
            factor_rows.append(
                {
                    "gcd_bits": value.bit_length(),
                    "factor_seconds": round(time_mod.monotonic() - t, 6),
                    "status": "TIMEOUT_30S",
                }
            )
    return {
        "shard_index": shard_index,
        "w6_control": w6_row,
        "w7_rows": w7_rows,
        "factor_rows": factor_rows,
        "distinct_saturated_gcds": len(distinct),
        "gp_startup_seconds": gp_startup_seconds,
        "shard_seconds": round(time_mod.monotonic() - shard_started, 6),
    }


@app.local_entrypoint()
def main() -> None:
    started = time.monotonic()
    w7, w6 = sample_candidates()
    payloads = [
        (index, w7[index * W7_PER_SHARD : (index + 1) * W7_PER_SHARD], w6[index])
        for index in range(SHARDS)
    ]
    shards = []
    errors = []
    for row in measure_shard.map(payloads, order_outputs=False, return_exceptions=True):
        if isinstance(row, BaseException):
            errors.append(repr(row))
        else:
            shards.append(row)
    result = {
        "schema": "wclp-b-weight7-sizing-sample-v1",
        "scope": "sizing pilot only; no certificate claim",
        "seed": SEED,
        "shards": len(shards),
        "shard_errors": errors,
        "data": shards,
        "wall_seconds": round(time.monotonic() - started, 3),
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    w7_rows = [row for shard in shards for row in shard["w7_rows"]]
    print(
        "WCLP_B_SAMPLE "
        + json.dumps(
            {
                "shards": len(shards),
                "errors": len(errors),
                "w7_rows": len(w7_rows),
                "w6_controls": len(shards),
                "factor_rows": sum(len(s["factor_rows"]) for s in shards),
            },
            sort_keys=True,
        )
    )
