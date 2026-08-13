#!/usr/bin/env python3
"""Exact FLINT norm census for every abstract profile-(4,4) energy 1/2 spectrum."""

from __future__ import annotations

from itertools import combinations, product
import json
import math
import time

import modal


B_PRIZE = 317494674775468773183020924238786383963
VALUATIONS = (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 16, 17, 18, 20)
COFACTOR_BOUND = 1_707_433
SHARDS = 8

app = modal.App("e1-profile44-abstract-energy12-norm-census")
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


def cofactors() -> tuple[int, ...]:
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
    return tuple(sorted(rows))


def cases() -> tuple[tuple[tuple[int, int], ...], ...]:
    rows = [((lag, sign),) for lag in range(1, 64) for sign in (-1, 1)]
    rows.extend(
        tuple(zip(lags, signs))
        for lags in combinations(range(1, 64), 2)
        for signs in product((-1, 1), repeat=2)
    )
    assert len(rows) == 126 + 7812
    return tuple(rows)


@app.function(image=image, cpu=1.0, memory=512, timeout=60, max_containers=SHARDS)
def compute(shard: int) -> dict[str, object]:
    from flint import fmpz, fmpz_poly

    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    legal_cofactors = cofactors()
    lower = B_PRIZE * 2**128
    upper = (B_PRIZE + 1) * 2**128 - 1
    viable = []
    counts = {"1": 0, "2": 0}
    valuation_counts: dict[str, int] = {}
    minimum_norm = None
    maximum_norm = None
    started = time.perf_counter()
    for index, spectrum in enumerate(cases()):
        if index % SHARDS != shard:
            continue
        degree = max(lag for lag, _ in spectrum)
        dense = [0] * (2 * degree + 1)
        dense[degree] = 20
        for lag, sign in spectrum:
            dense[degree - lag] += sign
            dense[degree + lag] += sign
        square_norm = abs(int(cyclotomic.resultant(fmpz_poly(dense))))
        norm = math.isqrt(square_norm)
        assert norm * norm == square_norm
        energy = len(spectrum)
        counts[str(energy)] += 1
        valuation = (norm & -norm).bit_length() - 1
        valuation_counts[str(valuation)] = valuation_counts.get(str(valuation), 0) + 1
        minimum_norm = norm if minimum_norm is None else min(minimum_norm, norm)
        maximum_norm = norm if maximum_norm is None else max(maximum_norm, norm)
        for cofactor in legal_cofactors:
            if norm % cofactor:
                continue
            candidate_prime = norm // cofactor
            if lower <= candidate_prime <= upper:
                viable.append(
                    {
                        "index": index,
                        "energy": energy,
                        "spectrum": spectrum,
                        "norm": str(norm),
                        "cofactor": cofactor,
                        "candidate_prime": str(candidate_prime),
                        "prime_mod_256": candidate_prime % 256,
                        "is_prime": bool(fmpz(candidate_prime).is_prime()),
                    }
                )
    return {
        "shard": shard,
        "complete": True,
        "counts": counts,
        "valuation_counts": valuation_counts,
        "minimum_norm": str(minimum_norm),
        "maximum_norm": str(maximum_norm),
        "viable": viable,
        "wall_seconds": time.perf_counter() - started,
    }


@app.local_entrypoint()
def main() -> None:
    returned = []
    for result in compute.map(range(SHARDS), order_outputs=False):
        returned.append(result)
        print(
            "PROFILE44_ENERGY12_PROGRESS "
            f"returned={len(returned)}/{SHARDS} shard={result['shard']} "
            f"seconds={result['wall_seconds']:.3f} viable={len(result['viable'])}",
            flush=True,
        )
    counts = {
        energy: sum(int(row["counts"][energy]) for row in returned)
        for energy in ("1", "2")
    }
    valuation_counts: dict[str, int] = {}
    for row in returned:
        for valuation, count in row["valuation_counts"].items():
            valuation_counts[valuation] = valuation_counts.get(valuation, 0) + int(count)
    packet = {
        "complete": len(returned) == SHARDS,
        "shards": SHARDS,
        "cofactors": len(cofactors()),
        "counts": counts,
        "valuation_counts": dict(sorted(valuation_counts.items(), key=lambda item: int(item[0]))),
        "minimum_norm": str(min(int(row["minimum_norm"]) for row in returned)),
        "maximum_norm": str(max(int(row["maximum_norm"]) for row in returned)),
        "viable": [item for row in returned for item in row["viable"]],
        "worker_seconds": sum(float(row["wall_seconds"]) for row in returned),
    }
    print(json.dumps(packet, sort_keys=True, separators=(",", ":")), flush=True)
