#!/usr/bin/env python3
"""Exact FLINT norm census for every abstract profile-(4,4) energy-four spectrum."""

from __future__ import annotations

from itertools import combinations, product
import json
import math
import time

import modal


B_PRIZE = 317494674775468773183020924238786383963
VALUATIONS = (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 16, 17, 18, 20)
COFACTOR_BOUND = 1_707_433
SHARDS = 128
MAX_CONTAINERS = 96

app = modal.App("e1-profile44-abstract-energy4-norm-census")
image = modal.Image.debian_slim().pip_install("python-flint")


def factor_odd(value: int) -> list[tuple[int, int]]:
    factors = []
    prime = 3
    while prime * prime <= value:
        if value % prime == 0:
            exponent = 0
            while value % prime == 0:
                value //= prime
                exponent += 1
            factors.append((prime, exponent))
        prime += 2
    if value > 1:
        factors.append((value, 1))
    return factors


def order_mod_256(value: int) -> int:
    residue = value % 256
    current = residue
    order = 1
    while current != 1:
        current = current * residue % 256
        order += 1
    return order


def cofactors() -> frozenset[int]:
    rows = []
    for valuation in VALUATIONS:
        odd = 1
        while (cofactor := (1 << valuation) * odd) <= COFACTOR_BOUND:
            if all(
                exponent % order_mod_256(prime) == 0
                for prime, exponent in factor_odd(odd)
            ):
                rows.append(cofactor)
            odd += 256
    assert len(rows) == len(set(rows)) == 1133
    return frozenset(rows)


def spectra():
    for lag in range(1, 64):
        for sign in (-2, 2):
            yield ((lag, sign),)
    for lags in combinations(range(1, 64), 4):
        for signs in product((-1, 1), repeat=4):
            yield tuple(zip(lags, signs))


@app.function(
    image=image,
    cpu=1.0,
    memory=512,
    timeout=90,
    max_containers=MAX_CONTAINERS,
)
def compute(shard: int) -> dict[str, object]:
    from flint import fmpz, fmpz_poly

    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    legal = cofactors()
    lower = B_PRIZE * 2**128
    upper = (B_PRIZE + 1) * 2**128 - 1
    viable = []
    interval_hits = 0
    processed = 0
    started = time.perf_counter()
    for index, spectrum in enumerate(spectra()):
        if index % SHARDS != shard:
            continue
        degree = spectrum[-1][0]
        dense = [0] * (2 * degree + 1)
        dense[degree] = 20
        for lag, coefficient in spectrum:
            dense[degree - lag] += coefficient
            dense[degree + lag] += coefficient
        square_norm = abs(int(cyclotomic.resultant(fmpz_poly(dense))))
        norm = math.isqrt(square_norm)
        assert norm * norm == square_norm

        minimum_cofactor = (norm + upper - 1) // upper
        maximum_cofactor = norm // lower
        assert maximum_cofactor - minimum_cofactor <= 1
        for cofactor in range(minimum_cofactor, maximum_cofactor + 1):
            interval_hits += 1
            if cofactor not in legal or norm % cofactor:
                continue
            candidate_prime = norm // cofactor
            viable.append(
                {
                    "index": index,
                    "spectrum": spectrum,
                    "norm": str(norm),
                    "cofactor": cofactor,
                    "candidate_prime": str(candidate_prime),
                    "prime_mod_256": candidate_prime % 256,
                    "is_prime": bool(fmpz(candidate_prime).is_prime()),
                }
            )
        processed += 1
    return {
        "shard": shard,
        "complete": True,
        "processed": processed,
        "interval_hits": interval_hits,
        "viable": viable,
        "wall_seconds": time.perf_counter() - started,
    }


@app.local_entrypoint()
def main() -> None:
    returned = []
    for result in compute.map(range(SHARDS), order_outputs=False):
        returned.append(result)
        print(
            "PROFILE44_ENERGY4_PROGRESS "
            f"returned={len(returned)}/{SHARDS} shard={result['shard']} "
            f"processed={result['processed']} seconds={result['wall_seconds']:.3f} "
            f"viable={len(result['viable'])}",
            flush=True,
        )
    packet = {
        "complete": len(returned) == SHARDS,
        "shards": SHARDS,
        "max_containers": MAX_CONTAINERS,
        "cofactors": len(cofactors()),
        "spectra": sum(int(row["processed"]) for row in returned),
        "interval_hits": sum(int(row["interval_hits"]) for row in returned),
        "viable": [item for row in returned for item in row["viable"]],
        "worker_seconds": sum(float(row["wall_seconds"]) for row in returned),
        "maximum_shard_seconds": max(float(row["wall_seconds"]) for row in returned),
    }
    print(json.dumps(packet, sort_keys=True, separators=(",", ":")), flush=True)
