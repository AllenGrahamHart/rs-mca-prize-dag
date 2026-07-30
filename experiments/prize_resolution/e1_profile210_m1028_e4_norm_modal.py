#!/usr/bin/env python3
"""Run the profile-(2,10), m=1028, energy-four CRT norm screen on Modal."""

from __future__ import annotations

from hashlib import sha256
from itertools import combinations, product
import json
from math import comb
from pathlib import Path
import runpy

import modal


ROOT = Path(__file__).resolve().parents[2]
ENGINE_PATH = ROOT / "experiments/prize_resolution/e1_profile210_m1028_e3_modular_norm.py"
app = modal.App("e1-profile210-m1028-e4-norm")
image = modal.Image.debian_slim().add_local_file(
    str(ENGINE_PATH), "/engine.py", copy=True
)
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
P_MAX = (B_PRIZE + 1) * 2**128 - 1
COFACTOR = 1028


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


def autocorrelation_multiplicity(lags: tuple[int, ...]) -> int:
    exponents = []
    for lag in lags:
        exponents.extend((lag, 128 - lag))
    return next(
        (
            derivative
            for derivative in range(16)
            if sum(comb(exponent, derivative) for exponent in exponents) % 2
        ),
        16,
    )


def certify_first_lag_exact(first: int, engine_path: str) -> dict[str, object]:
    engine = runpy.run_path(engine_path)
    if not all(engine["is_prime"](prime) for prime in engine["PRIMES"]):
        raise RuntimeError("CRT primality check failed")
    exact_norm = engine["exact_norm"]
    chebyshev = chebyshev_polynomials(64)
    root = 3
    rational_prime = 257
    traces = [0] + [
        (
            pow(root, lag, rational_prime)
            + pow(pow(root, lag, rational_prime), -1, rational_prime)
        )
        % rational_prime
        for lag in range(1, 64)
    ]
    rows = []
    below = inside = above = 0
    minimum = None
    maximum = None
    supports = 0
    for tail in combinations(range(first + 1, 64), 3):
        lags = (first,) + tail
        if autocorrelation_multiplicity(lags) != 4:
            continue
        supports += 1
        for signs in product((-1, 1), repeat=4):
            if (
                18 + sum(sign * traces[lag] for sign, lag in zip(signs, lags))
            ) % rational_prime:
                continue
            value = [18]
            for sign, lag in zip(signs, lags):
                value = polynomial_add(value, chebyshev[lag], sign)
            norm = exact_norm(chebyshev[64], value)
            if norm % COFACTOR:
                raise RuntimeError(f"cofactor divisibility failed: {lags}, {signs}")
            quotient = norm // COFACTOR
            if quotient < P_MIN:
                below += 1
            elif quotient <= P_MAX:
                inside += 1
            else:
                above += 1
            minimum = quotient if minimum is None else min(minimum, quotient)
            maximum = quotient if maximum is None else max(maximum, quotient)
            rows.append(
                ",".join(map(str, lags + signs)) + f":{quotient}"
            )

    return {
        "first": first,
        "supports": supports,
        "hits": len(rows),
        "below": below,
        "inside": inside,
        "above": above,
        "minimum": minimum,
        "maximum": maximum,
        "digest": sha256("\n".join(rows).encode("ascii")).hexdigest(),
    }


@app.function(image=image, cpu=1.0, memory=512, timeout=60, max_containers=1)
def certify_first_lag(first: int) -> dict[str, object]:
    return certify_first_lag_exact(first, "/engine.py")


@app.local_entrypoint()
def main(
    output: str = "experiments/prize_resolution/e1_profile210_m1028_e4_norm_result.json",
) -> None:
    output_path = Path(output)
    rows = []
    for row in certify_first_lag.map(range(1, 61), order_outputs=False):
        rows.append(row)
        rows.sort(key=lambda item: int(item["first"]))
        checkpoint = {
            "schema": "e1-profile210-m1028-e4-norm-result-v1",
            "complete": len(rows) == 60,
            "completed_shards": len(rows),
            "expected_shards": 60,
            "rows": rows,
        }
        output_path.write_text(json.dumps(checkpoint, indent=2, sort_keys=True) + "\n")
        print(
            f"first={row['first']} hits={row['hits']} below={row['below']} "
            f"inside={row['inside']} above={row['above']}"
        )

    totals = {
        key: sum(int(row[key]) for row in rows)
        for key in ("supports", "hits", "below", "inside", "above")
    }
    if totals["hits"] != 8385:
        raise RuntimeError(f"target census drift: {totals}")
    if totals["inside"] or totals["above"]:
        raise RuntimeError(f"energy-four branch not excluded: {totals}")
    print(
        "E1_PROFILE210_M1028_E4_NORM_MODAL_PASS "
        f"shards={len(rows)} hits={totals['hits']} below={totals['below']}"
    )
