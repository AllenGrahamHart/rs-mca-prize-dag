#!/usr/bin/env python3
"""Exact same-fiber norm-GCD probe for the C36' arithmetic route.

The two targets are the complete rich locus at
``(n,p)=(8192,67657729)``. The probe recovers each ten-pair fiber directly.
For one reference pair and each of the other nine, it computes

    Norm((1-zeta^i)(1-zeta^j) - (1-zeta^u)(1-zeta^v))

as ``Res(X^(n/2)+1, f)`` using FLINT. Every norm must be nonzero and divisible
by ``p``. The decision datum is the exact GCD of the nine norms in each fiber:

* GCD equal to a power of ``p`` times the universal 2-adic factor supports a
  same-fiber ideal-generation route;
* a large cofactor fences the naive common-norm version of that route.

This is route-selection evidence only. The eighteen norms run as independent
60-second Modal tasks, and the local entrypoint prints each completed shard
before computing the GCD, so a failed shard leaves partial results.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import modal


ORDER = 8192
PRIME = 67_657_729
GENERATOR = 41_542_468
TARGETS = (40_697_698, 16_650_852)
OUTPUT = Path(__file__).with_name("h3_rich_norm_gcd_result.json")
EXPECTED_FIRST_PAIRS = (
    (751, 2815),
    (758, 7217),
    (808, 2323),
    (918, 1027),
    (1905, 7976),
    (3738, 5802),
    (4230, 5745),
    (4648, 6769),
    (5526, 5635),
    (5795, 7528),
)

app = modal.App("rs-mca-h3-rich-norm-gcd")
image = modal.Image.debian_slim().pip_install("python-flint")


def pair_vector(order: int, left: int, right: int) -> list[int]:
    half = order // 2
    coefficients = [0] * half
    for exponent, coefficient in (
        ((left + right) % order, 1),
        (left, -1),
        (right, -1),
    ):
        if exponent >= half:
            exponent -= half
            coefficient = -coefficient
        coefficients[exponent] += coefficient
    return coefficients


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


@app.function(image=image, cpu=1, memory=512, timeout=60)
def recover_fibers() -> dict[int, list[tuple[int, int]]]:
    shifted: dict[int, int] = {}
    root = GENERATOR
    for exponent in range(1, ORDER):
        shifted[(1 - root) % PRIME] = exponent
        root = root * GENERATOR % PRIME

    fibers: dict[int, list[tuple[int, int]]] = {}
    for target in TARGETS:
        pairs = set()
        for left_value, left_exponent in shifted.items():
            right_value = target * pow(left_value, -1, PRIME) % PRIME
            right_exponent = shifted.get(right_value)
            if right_exponent is not None:
                pairs.add(tuple(sorted((left_exponent, right_exponent))))
        fibers[target] = sorted(pairs)
    return fibers


@app.function(image=image, cpu=1, memory=1024, timeout=60, max_containers=18)
def collision_norm(
    payload: tuple[int, list[tuple[int, int]], int]
) -> dict[str, object]:
    from flint import fmpz_poly

    target, pairs, index = payload
    reference = pair_vector(ORDER, *pairs[0])
    other = pair_vector(ORDER, *pairs[index])
    difference = [left - right for left, right in zip(reference, other)]
    while difference and difference[-1] == 0:
        difference.pop()
    if not difference:
        raise AssertionError("duplicate coefficient vector")

    phi = fmpz_poly([1] + [0] * (ORDER // 2 - 1) + [1])
    obstruction = fmpz_poly(difference)
    norm = abs(int(phi.resultant(obstruction)))
    if norm == 0 or norm % PRIME:
        raise AssertionError((index, norm % PRIME))

    reconstructed = (1 - pow(GENERATOR, pairs[0][0], PRIME)) % PRIME
    reconstructed = (
        reconstructed * (1 - pow(GENERATOR, pairs[0][1], PRIME)) % PRIME
    )
    candidate = (
        (1 - pow(GENERATOR, pairs[index][0], PRIME))
        * (1 - pow(GENERATOR, pairs[index][1], PRIME))
    ) % PRIME
    if candidate != target or reconstructed != target:
        raise AssertionError((index, target, reconstructed, candidate))

    return {
        "target": target,
        "index": index,
        "pair": list(pairs[index]),
        "norm": str(norm),
        "norm_bits": norm.bit_length(),
        "p_valuation": valuation(norm, PRIME),
    }


@app.function(image=image, cpu=1, memory=2048, timeout=60, max_containers=2)
def collision_resultant(
    payload: tuple[int, list[tuple[int, int]]]
) -> dict[str, object]:
    from flint import fmpz_poly

    target, pairs = payload
    reference = pair_vector(ORDER, *pairs[0])
    differences = []
    for index in (1, 2):
        other = pair_vector(ORDER, *pairs[index])
        difference = [left - right for left, right in zip(reference, other)]
        while difference and difference[-1] == 0:
            difference.pop()
        differences.append(fmpz_poly(difference))
    common = differences[0].gcd(differences[1])
    common_at_generator = sum(
        int(coefficient) * pow(GENERATOR, exponent, PRIME)
        for exponent, coefficient in enumerate(common)
    ) % PRIME
    if common_at_generator == 0:
        raise AssertionError((target, "rational gcd absorbs the row root"))
    reduced = []
    for difference in differences:
        if difference % common:
            raise AssertionError((target, "nonexact rational gcd"))
        reduced.append(difference // common)
    value = abs(int(reduced[0].resultant(reduced[1])))
    if value == 0 or value % PRIME:
        raise AssertionError((target, value % PRIME))
    p_valuation = valuation(value, PRIME)
    cofactor = value // PRIME**p_valuation
    return {
        "target": target,
        "common_degree": common.degree(),
        "common_terms": sum(coefficient != 0 for coefficient in common),
        "resultant": str(value),
        "resultant_bits": value.bit_length(),
        "p_valuation": p_valuation,
        "cofactor_bits": cofactor.bit_length(),
    }


@app.local_entrypoint()
def main() -> None:
    fibers = recover_fibers.remote()
    if tuple(fibers[TARGETS[0]]) != EXPECTED_FIRST_PAIRS:
        raise AssertionError("first rich fiber differs from the banked recovery")
    if any(len(fibers[target]) != 10 for target in TARGETS):
        raise AssertionError({target: len(fibers[target]) for target in TARGETS})
    target_summaries: dict[int, dict[str, object]] = {}
    for target in TARGETS:
        print(f"H3_RICH_FIBER target={target} pairs={fibers[target]}", flush=True)

    payloads = [
        (target, fibers[target], index)
        for target in TARGETS
        for index in range(1, len(fibers[target]))
    ]
    rows: list[dict[str, object]] = []
    for result in collision_norm.map(payloads, return_exceptions=True):
        if isinstance(result, BaseException):
            print(f"H3_RICH_NORM_SHARD_ERROR {result!r}", flush=True)
            continue
        rows.append(result)
        print(
            "H3_RICH_NORM_SHARD "
            f"target={result['target']} index={result['index']} "
            f"pair={result['pair']} bits={result['norm_bits']} "
            f"p_valuation={result['p_valuation']}",
            flush=True,
        )

    if len(rows) != len(payloads):
        raise SystemExit(f"partial results: {len(rows)}/{len(payloads)}")

    for target in TARGETS:
        target_rows = sorted(
            (row for row in rows if row["target"] == target),
            key=lambda row: int(row["index"]),
        )
        norms = [int(str(row["norm"])) for row in target_rows]
        running = 0
        for count, norm in enumerate(norms, start=1):
            running = math.gcd(running, norm)
            running_valuation = valuation(running, PRIME)
            running_cofactor = running // PRIME**running_valuation
            print(
                "H3_RICH_NORM_RUNNING_GCD "
                f"target={target} norms={count} bits={running.bit_length()} "
                f"p_valuation={running_valuation} "
                f"cofactor_bits={running_cofactor.bit_length()}"
            )
        common = math.gcd(*norms)
        p_valuation = valuation(common, PRIME)
        cofactor = common // PRIME**p_valuation
        print(
            "H3_RICH_NORM_GCD_PASS "
            f"target={target} norms={len(norms)} "
            f"gcd_bits={common.bit_length()} p_valuation={p_valuation} "
            f"cofactor_bits={cofactor.bit_length()} cofactor={cofactor}"
        )
        target_summaries[target] = {
            "target": target,
            "pairs": [list(pair) for pair in fibers[target]],
            "norms": [str(norm) for norm in norms],
            "gcd": str(common),
            "p_valuation": p_valuation,
            "cofactor": str(cofactor),
        }

    resultant_rows: list[dict[str, object]] = []
    resultant_errors = 0
    for result in collision_resultant.map(
        [(target, fibers[target]) for target in TARGETS],
        return_exceptions=True,
    ):
        if isinstance(result, BaseException):
            print(f"H3_RICH_RESULTANT_ERROR {result!r}", flush=True)
            resultant_errors += 1
            continue
        resultant_rows.append(result)
        print(
            "H3_RICH_RESULTANT_PASS "
            f"target={result['target']} common_degree={result['common_degree']} "
            f"common_terms={result['common_terms']} "
            f"bits={result['resultant_bits']} "
            f"p_valuation={result['p_valuation']} "
            f"cofactor_bits={result['cofactor_bits']}"
        )
    if resultant_errors:
        raise SystemExit(f"resultant errors: {resultant_errors}")

    for result in resultant_rows:
        target_summaries[int(result["target"])]["reduced_resultant"] = result
    output = {
        "schema": "h3-rich-norm-gcd-v1",
        "order": ORDER,
        "prime": PRIME,
        "generator": GENERATOR,
        "targets": [target_summaries[target] for target in TARGETS],
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(f"H3_RICH_NORM_RESULT_WRITTEN {OUTPUT}")


if __name__ == "__main__":
    main()
