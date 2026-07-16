#!/usr/bin/env python3
"""Size the terminal DLI weight-five affine/norm route on Modal.

This is a route-selection probe, not an exclusion certificate.  The Burnside
calculation is exact and is cross-checked against the banked weight-three and
weight-four class counts.  The norm sample is deterministic but nonexhaustive.
"""

from __future__ import annotations

import itertools
import json
import math
import random
import subprocess
import time
from pathlib import Path

import modal


ORDER = 512
HALF = ORDER // 2
MAX_WEIGHT = 6
SAMPLE_SEED = 20260713
OUTPUT = Path(__file__).with_name("dli_wcl_weight5_orbit_probe_result.json")

app = modal.App("rs-mca-dli-wcl-weight5-orbit-probe")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")


def valuation_two(value: int) -> int:
    exponent = 0
    while value and value % 2 == 0:
        value //= 2
        exponent += 1
    return exponent


def fixed_antipodal_free_counts(a: int, b: int) -> list[int]:
    """Count invariant antipodal-free subsets by size for x -> a*x+b."""
    cycle_of = [-1] * ORDER
    cycles: list[list[int]] = []
    for start in range(ORDER):
        if cycle_of[start] >= 0:
            continue
        cycle_id = len(cycles)
        cycle = []
        point = start
        while cycle_of[point] < 0:
            cycle_of[point] = cycle_id
            cycle.append(point)
            point = (a * point + b) % ORDER
        if point != start:
            raise AssertionError((a, b, start, point))
        cycles.append(cycle)

    counts = [0] * (MAX_WEIGHT + 1)
    counts[0] = 1
    for cycle_id, cycle in enumerate(cycles):
        partner_id = cycle_of[(cycle[0] + HALF) % ORDER]
        if partner_id == cycle_id or cycle_id > partner_id:
            continue
        if len(cycle) != len(cycles[partner_id]):
            raise AssertionError((a, b, cycle_id, partner_id))
        length = len(cycle)
        if length > MAX_WEIGHT:
            continue
        for size in range(MAX_WEIGHT - length, -1, -1):
            counts[size + length] += 2 * counts[size]
    return counts


@app.function(image=image, cpu=1, memory=512, timeout=120, max_containers=128)
def burnside_for_multiplier(a: int) -> dict[str, object]:
    if a % 2 != 1 or not 0 < a < ORDER:
        raise AssertionError(a)
    started = time.monotonic()
    totals = [0] * (MAX_WEIGHT + 1)
    for b in range(ORDER):
        counts = fixed_antipodal_free_counts(a, b)
        totals = [left + right for left, right in zip(totals, counts)]
    return {
        "a": a,
        "fixed_sums": totals,
        "seconds": round(time.monotonic() - started, 6),
    }


def deterministic_supports(size: int) -> list[dict[str, object]]:
    rng = random.Random(SAMPLE_SEED)
    seen: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    rows = []
    while len(rows) < size:
        exponents = tuple(sorted(rng.sample(range(HALF), 5)))
        signs = [rng.choice((-1, 1)) for _ in exponents]
        if signs[0] < 0:
            signs = [-sign for sign in signs]
        key = (exponents, tuple(signs))
        if key in seen:
            continue
        seen.add(key)
        rows.append({"sample_index": len(rows), "exponents": exponents, "signs": signs})
    return rows


@app.function(image=image, cpu=1, memory=1536, timeout=120, max_containers=128)
def factor_weight5_norm(row: dict[str, object]) -> dict[str, object]:
    from flint import fmpz_poly

    started = time.monotonic()
    coefficients = [0] * HALF
    for exponent, sign in zip(row["exponents"], row["signs"]):
        coefficients[int(exponent)] += int(sign)
    polynomial = fmpz_poly(coefficients)
    cyclotomic = fmpz_poly([1] + [0] * (HALF - 1) + [1])
    norm = abs(int(cyclotomic.resultant(polynomial)))
    if norm == 0:
        raise AssertionError("characteristic-zero vanisher")

    program = (
        f"n={norm};f=factor(n);"
        'for(i=1,matsize(f)[1],print(f[i,1]," : ",f[i,2]));quit()\n'
    )
    completed = subprocess.run(
        ["gp", "-q", "-s", "268435456"],
        input=program,
        text=True,
        capture_output=True,
        timeout=110,
        check=True,
    )
    factors = []
    product = 1
    for line in completed.stdout.splitlines():
        if ":" not in line:
            continue
        prime_text, exponent_text = (part.strip() for part in line.split(":", 1))
        prime = int(prime_text)
        exponent = int(exponent_text)
        factors.append(
            {
                "prime": prime_text,
                "exponent": exponent,
                "bits": prime.bit_length(),
                "v2_prime_minus_1": valuation_two(prime - 1),
            }
        )
        product *= prime**exponent
    if product != norm:
        raise AssertionError((norm, product, completed.stdout, completed.stderr))

    return {
        **row,
        "norm": str(norm),
        "norm_bits": norm.bit_length(),
        "factors": factors,
        "eligible": [
            factor
            for factor in factors
            if int(factor["prime"]) < 2**256 and factor["v2_prime_minus_1"] >= 41
        ],
        "seconds": round(time.monotonic() - started, 6),
    }


@app.local_entrypoint()
def main(sample_size: int = 256) -> None:
    started = time.monotonic()
    multipliers = list(range(1, ORDER, 2))
    burnside_rows = list(burnside_for_multiplier.map(multipliers))
    fixed_sums = [
        sum(int(row["fixed_sums"][weight]) for row in burnside_rows)
        for weight in range(MAX_WEIGHT + 1)
    ]
    group_order = ORDER * len(multipliers)
    if any(total % group_order for total in fixed_sums):
        raise AssertionError((group_order, fixed_sums))
    orbit_counts = [total // group_order for total in fixed_sums]
    expected = {3: 254, 4: 24979}
    for weight, count in expected.items():
        if orbit_counts[weight] != count:
            raise AssertionError((weight, orbit_counts[weight], count))

    supports = deterministic_supports(sample_size)
    factor_rows = list(factor_weight5_norm.map(supports, return_exceptions=True))
    errors = [repr(row) for row in factor_rows if isinstance(row, BaseException)]
    completed = [row for row in factor_rows if not isinstance(row, BaseException)]
    factor_records = [factor for row in completed for factor in row["factors"]]
    eligible = [factor for row in completed for factor in row["eligible"]]
    result = {
        "schema": "dli-wcl-weight5-orbit-probe-v1",
        "status": "COMPLETE" if not errors else "PARTIAL",
        "scope": "route selection only; norm sample is not exhaustive",
        "order": ORDER,
        "group_order": group_order,
        "raw_global_sign_quotient_counts": {
            str(weight): math.comb(HALF, weight) * 2 ** (weight - 1)
            for weight in range(3, MAX_WEIGHT + 1)
        },
        "affine_galois_orbit_counts": {
            str(weight): orbit_counts[weight] for weight in range(3, MAX_WEIGHT + 1)
        },
        "burnside_max_worker_seconds": max(float(row["seconds"]) for row in burnside_rows),
        "sample_seed": SAMPLE_SEED,
        "sample_requested": sample_size,
        "sample_completed": len(completed),
        "sample_errors": errors,
        "sample_factor_records": len(factor_records),
        "sample_distinct_prime_factors": len({factor["prime"] for factor in factor_records}),
        "sample_max_norm_bits": max((int(row["norm_bits"]) for row in completed), default=0),
        "sample_max_factor_seconds": max((float(row["seconds"]) for row in completed), default=0.0),
        "sample_max_v2_below_cap": max(
            (
                int(factor["v2_prime_minus_1"])
                for factor in factor_records
                if int(factor["prime"]) < 2**256
            ),
            default=0,
        ),
        "sample_eligible_count": len(eligible),
        "sample_rows": completed,
        "wall_seconds": round(time.monotonic() - started, 6),
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_WEIGHT5_ORBIT_PROBE "
        f"orbits_w3={orbit_counts[3]} orbits_w4={orbit_counts[4]} "
        f"orbits_w5={orbit_counts[5]} orbits_w6={orbit_counts[6]} "
        f"sample={len(completed)}/{sample_size} errors={len(errors)} "
        f"eligible={len(eligible)} max_v2={result['sample_max_v2_below_cap']}"
    )
