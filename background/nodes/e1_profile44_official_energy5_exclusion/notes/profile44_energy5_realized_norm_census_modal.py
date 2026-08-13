#!/usr/bin/env python3
"""Exact norm census for every realized profile-(4,4) energy-five spectrum."""

from __future__ import annotations

from itertools import combinations, product
import json
import math
import time

import modal


B_PRIZE = 317494674775468773183020924238786383963
PARENT_BOUND = 932_364
SHARDS = 8

app = modal.App("e1-profile44-energy5-realized-norm-census")
image = modal.Image.debian_slim().pip_install("python-flint")


def parity_mask(support: tuple[int, ...]) -> tuple[int, ...]:
    mask = set()
    for left, right in combinations(support, 2):
        delta = (right - left) % 128
        if delta == 64:
            continue
        lag = min(delta, 128 - delta)
        if lag in mask:
            mask.remove(lag)
        else:
            mask.add(lag)
    return tuple(sorted(mask))


def realized_masks() -> dict[int, tuple[tuple[int, ...], ...]]:
    rows = {1: set(), 5: set()}
    for tail in combinations(range(1, 128), 3):
        mask = parity_mask((0,) + tail)
        if len(mask) in rows:
            rows[len(mask)].add(mask)
    result = {weight: tuple(sorted(masks)) for weight, masks in rows.items()}
    assert len(result[1]) == 31 and len(result[5]) == 1785
    return result


def spectra():
    masks = realized_masks()
    for mask in masks[5]:
        for signs in product((-1, 1), repeat=5):
            yield tuple(zip(mask, signs))
    for (odd_lag,) in masks[1]:
        for even_lag in range(1, 64):
            if even_lag == odd_lag:
                continue
            for odd_sign in (-1, 1):
                for even_sign in (-2, 2):
                    yield tuple(sorted(((odd_lag, odd_sign), (even_lag, even_sign))))


@app.function(image=image, cpu=1.0, memory=512, timeout=60, max_containers=SHARDS)
def compute(shard: int) -> dict[str, object]:
    from flint import fmpz_poly

    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    lower = B_PRIZE * 2**128
    upper = (B_PRIZE + 1) * 2**128 - 1
    hits = []
    processed = 0
    unique_norms = set()
    valuations: dict[str, int] = {}
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
        unique_norms.add(norm)
        valuation = (norm & -norm).bit_length() - 1
        valuations[str(valuation)] = valuations.get(str(valuation), 0) + 1
        minimum_cofactor = (norm + upper - 1) // upper
        maximum_cofactor = norm // lower
        assert maximum_cofactor - minimum_cofactor <= 1
        for cofactor in range(minimum_cofactor, maximum_cofactor + 1):
            if cofactor <= PARENT_BOUND and norm % cofactor == 0:
                hits.append(
                    {
                        "index": index,
                        "spectrum": spectrum,
                        "norm": str(norm),
                        "cofactor": cofactor,
                        "candidate_prime": str(norm // cofactor),
                    }
                )
        processed += 1
    return {
        "complete": True,
        "shard": shard,
        "processed": processed,
        "unique_norms": len(unique_norms),
        "valuation_counts": valuations,
        "hits": hits,
        "wall_seconds": time.perf_counter() - started,
    }


@app.local_entrypoint()
def main() -> None:
    returned = []
    for row in compute.map(range(SHARDS), order_outputs=False):
        returned.append(row)
        print(
            "PROFILE44_ENERGY5_PROGRESS "
            f"returned={len(returned)}/{SHARDS} shard={row['shard']} "
            f"processed={row['processed']} seconds={row['wall_seconds']:.3f} "
            f"hits={len(row['hits'])}",
            flush=True,
        )
    valuations: dict[str, int] = {}
    for row in returned:
        for valuation, count in row["valuation_counts"].items():
            valuations[valuation] = valuations.get(valuation, 0) + int(count)
    packet = {
        "complete": len(returned) == SHARDS,
        "shards": SHARDS,
        "masks": {"1": 31, "5": 1785},
        "spectra": sum(int(row["processed"]) for row in returned),
        "shard_unique_norm_sum": sum(int(row["unique_norms"]) for row in returned),
        "valuation_counts": dict(sorted(valuations.items(), key=lambda item: int(item[0]))),
        "hits": [hit for row in returned for hit in row["hits"]],
        "worker_seconds": sum(float(row["wall_seconds"]) for row in returned),
    }
    assert packet["spectra"] == 1785 * 32 + 31 * 62 * 4 == 64808
    print(json.dumps(packet, sort_keys=True, separators=(",", ":")), flush=True)
