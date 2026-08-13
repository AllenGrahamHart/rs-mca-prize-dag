#!/usr/bin/env python3
"""Independent full replay of the realized profile-(4,4) energy-five census."""

from __future__ import annotations

from itertools import combinations
import json
import math
import time

import modal


B_PRIZE = 317494674775468773183020924238786383963
SHARDS = 8

app = modal.App("e1-profile44-energy5-realized-norm-audit")
image = modal.Image.debian_slim().pip_install("python-flint")


def mask_for(a: int, b: int, c: int) -> int:
    support = (0, a, b, c)
    mask = 0
    for right_index in range(1, 4):
        right = support[right_index]
        for left_index in range(right_index):
            delta = right - support[left_index]
            if delta != 64:
                lag = min(delta, 128 - delta)
                mask ^= 1 << lag
    return mask


def masks() -> tuple[tuple[int, ...], tuple[int, ...]]:
    one = set()
    five = set()
    for a in range(1, 126):
        for b in range(a + 1, 127):
            for c in range(b + 1, 128):
                mask = mask_for(a, b, c)
                if mask.bit_count() == 1:
                    one.add(mask)
                elif mask.bit_count() == 5:
                    five.add(mask)
    assert len(one) == 31 and len(five) == 1785
    return tuple(sorted(one)), tuple(sorted(five))


def positions(mask: int) -> tuple[int, ...]:
    return tuple(lag for lag in range(1, 64) if mask >> lag & 1)


def spectra():
    one, five = masks()
    for mask in five:
        lags = positions(mask)
        for sign_bits in range(32):
            yield tuple(
                (lag, 1 if sign_bits >> index & 1 else -1)
                for index, lag in enumerate(lags)
            )
    for mask in one:
        odd_lag = positions(mask)[0]
        for even_lag in range(63, 0, -1):
            if even_lag == odd_lag:
                continue
            for sign_bits in range(4):
                yield tuple(
                    sorted(
                        (
                            (odd_lag, 1 if sign_bits & 1 else -1),
                            (even_lag, 2 if sign_bits & 2 else -2),
                        )
                    )
                )


@app.function(image=image, cpu=1.0, memory=512, timeout=60, max_containers=SHARDS)
def audit(shard: int) -> dict[str, object]:
    from flint import fmpz_poly

    phi = fmpz_poly([1] + [0] * 127 + [1])
    p_min = B_PRIZE << 128
    p_max = ((B_PRIZE + 1) << 128) - 1
    processed = 0
    interval_integers = 0
    exact_hits = []
    started = time.perf_counter()
    for index, spectrum in enumerate(spectra()):
        if index % SHARDS != shard:
            continue
        degree = max(lag for lag, _ in spectrum)
        coefficients = [0] * (2 * degree + 1)
        coefficients[degree] = 20
        for lag, value in spectrum:
            coefficients[degree - lag] = value
            coefficients[degree + lag] = value
        resultant = abs(int(phi.resultant(fmpz_poly(coefficients))))
        norm = math.isqrt(resultant)
        assert norm**2 == resultant
        first = (norm + p_max - 1) // p_max
        last = norm // p_min
        assert last - first <= 1
        for candidate in range(first, last + 1):
            interval_integers += 1
            if norm % candidate == 0:
                exact_hits.append((index, spectrum, str(norm), candidate))
        processed += 1
    return {
        "complete": True,
        "shard": shard,
        "processed": processed,
        "interval_integers": interval_integers,
        "hits": exact_hits,
        "wall_seconds": time.perf_counter() - started,
    }


@app.local_entrypoint()
def main() -> None:
    rows = list(audit.map(range(SHARDS), order_outputs=False))
    packet = {
        "complete": len(rows) == SHARDS,
        "shards": SHARDS,
        "spectra": sum(int(row["processed"]) for row in rows),
        "interval_integers": sum(int(row["interval_integers"]) for row in rows),
        "hits": [hit for row in rows for hit in row["hits"]],
        "worker_seconds": sum(float(row["wall_seconds"]) for row in rows),
        "maximum_shard_seconds": max(float(row["wall_seconds"]) for row in rows),
    }
    print(json.dumps(packet, sort_keys=True, separators=(",", ":")))
