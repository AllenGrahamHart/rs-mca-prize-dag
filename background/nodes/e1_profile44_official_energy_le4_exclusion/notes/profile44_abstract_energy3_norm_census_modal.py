#!/usr/bin/env python3
"""Exact FLINT norm census for every abstract profile-(4,4) energy-three spectrum."""

from __future__ import annotations

from itertools import combinations, product
import json
import math
import time

import modal


B_PRIZE = 317494674775468773183020924238786383963
VALUATIONS = (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 16, 17, 18, 20)
COFACTOR_BOUND = 1_707_433
SHARDS = 16

app = modal.App("e1-profile44-abstract-energy3-norm-census")
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


def cofactors_by_valuation() -> dict[int, tuple[int, ...]]:
    rows: dict[int, list[int]] = {valuation: [] for valuation in VALUATIONS}
    for valuation in VALUATIONS:
        odd = 1
        while (cofactor := (1 << valuation) * odd) <= COFACTOR_BOUND:
            if all(
                exponent % order_mod_256(prime) == 0
                for prime, exponent in factor_odd(odd)
            ):
                rows[valuation].append(cofactor)
            odd += 256
    assert sum(map(len, rows.values())) == 1133
    return {valuation: tuple(values) for valuation, values in rows.items()}


def spectra():
    for lags in combinations(range(1, 64), 3):
        for signs in product((-1, 1), repeat=3):
            yield tuple(zip(lags, signs))


@app.function(image=image, cpu=1.0, memory=512, timeout=60, max_containers=SHARDS)
def compute(shard: int) -> dict[str, object]:
    from flint import fmpz, fmpz_poly

    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    cofactor_map = cofactors_by_valuation()
    lower = B_PRIZE * 2**128
    upper = (B_PRIZE + 1) * 2**128 - 1
    viable = []
    valuations: dict[str, int] = {}
    processed = 0
    started = time.perf_counter()
    for index, spectrum in enumerate(spectra()):
        if index % SHARDS != shard:
            continue
        degree = spectrum[-1][0]
        dense = [0] * (2 * degree + 1)
        dense[degree] = 20
        for lag, sign in spectrum:
            dense[degree - lag] += sign
            dense[degree + lag] += sign
        square_norm = abs(int(cyclotomic.resultant(fmpz_poly(dense))))
        norm = math.isqrt(square_norm)
        assert norm * norm == square_norm
        valuation = (norm & -norm).bit_length() - 1
        valuations[str(valuation)] = valuations.get(str(valuation), 0) + 1
        for cofactor in cofactor_map.get(valuation, ()):
            if norm % cofactor:
                continue
            candidate_prime = norm // cofactor
            if lower <= candidate_prime <= upper:
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
        "valuations": valuations,
        "viable": viable,
        "wall_seconds": time.perf_counter() - started,
    }


@app.local_entrypoint()
def main() -> None:
    returned = []
    for result in compute.map(range(SHARDS), order_outputs=False):
        returned.append(result)
        print(
            "PROFILE44_ENERGY3_PROGRESS "
            f"returned={len(returned)}/{SHARDS} shard={result['shard']} "
            f"processed={result['processed']} seconds={result['wall_seconds']:.3f} "
            f"viable={len(result['viable'])}",
            flush=True,
        )
    valuations: dict[str, int] = {}
    for row in returned:
        for valuation, count in row["valuations"].items():
            valuations[valuation] = valuations.get(valuation, 0) + int(count)
    packet = {
        "complete": len(returned) == SHARDS,
        "shards": SHARDS,
        "cofactors": sum(map(len, cofactors_by_valuation().values())),
        "spectra": sum(int(row["processed"]) for row in returned),
        "valuation_counts": dict(sorted(valuations.items(), key=lambda item: int(item[0]))),
        "viable": [item for row in returned for item in row["viable"]],
        "worker_seconds": sum(float(row["wall_seconds"]) for row in returned),
    }
    print(json.dumps(packet, sort_keys=True, separators=(",", ":")), flush=True)
