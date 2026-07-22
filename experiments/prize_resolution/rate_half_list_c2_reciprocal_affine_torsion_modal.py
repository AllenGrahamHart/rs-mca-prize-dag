#!/usr/bin/env python3
"""Bounded reciprocal-affine torsion screen for the c=2 collision shard.

Pre-registration
----------------
Decision: for every progression modulus

    p=k*2^40-1,
    ceil(sqrt(3*2^128)) <= p < 2^65,

test the fixed trace recurrence left by the proved reciprocal affine
collapse:

    R_0=-2/3,  R_(j+1)=R_j^2-2,  require R_40=2.

PASS: complete exact coverage and no modular hit. This excludes every prime
in the reciprocal maximal-degree selected-antipodal affine shard.

FAIL: emit every (k,p) modular hit and its trace. A hit must still be proved
prime and pass all source, Euler, gap, and canonical gates.

INCOMPLETE: every shard returns its next k, rolling digest, and partial hits.

Resources: 16 independent one-CPU, 512-MiB, 60-second shards, returning at
50 seconds with partial output. The recorded total cost ceiling is $0.25.
No automatic retry is authorized.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from pathlib import Path

import modal


APP_NAME = "rate-half-list-c2-reciprocal-affine-torsion"
ORDER = 1 << 40
LOW_SQUARE = 3 * (1 << 128)
HIGH = 1 << 65
SHARDS = 16

app = modal.App(APP_NAME)
image = modal.Image.debian_slim(python_version="3.12")


def interval() -> tuple[int, int, int]:
    lower = math.isqrt(LOW_SQUARE)
    if lower * lower < LOW_SQUARE:
        lower += 1
    start = (lower + 1 + ORDER - 1) // ORDER
    stop = HIGH // ORDER + 1
    return lower, start, stop


def tasks() -> list[tuple[int, int, int]]:
    _, start, stop = interval()
    width = (stop - start + SHARDS - 1) // SHARDS
    return [
        (index, start + index * width, min(stop, start + (index + 1) * width))
        for index in range(SHARDS)
        if start + index * width < stop
    ]


def trace_values(modulus: int, levels: int) -> list[int]:
    value = -2 * pow(3, -1, modulus) % modulus
    values = [value]
    for _ in range(levels):
        value = (value * value - 2) % modulus
        values.append(value)
    return values


@app.function(
    image=image,
    cpu=1,
    memory=512,
    timeout=60,
    max_containers=SHARDS,
)
def scan_shard(task: tuple[int, int, int]) -> dict[str, object]:
    shard, start, stop = task
    began = time.monotonic()
    hits: list[dict[str, object]] = []
    rolling = hashlib.sha256()
    processed = 0
    skipped_factor_three = 0
    next_index = start

    for k_value in range(start, stop):
        modulus = k_value * ORDER - 1
        code = 0
        if modulus % 3 == 0:
            code = 2
            skipped_factor_three += 1
        else:
            trace = trace_values(modulus, 40)
            if trace[-1] == 2:
                code = 1
                hits.append({"k": k_value, "p": modulus, "trace": trace})

        rolling.update(k_value.to_bytes(4, "little"))
        rolling.update(bytes((code,)))
        processed += 1
        next_index = k_value + 1

        if (processed & 4095) == 0 and time.monotonic() - began >= 50.0:
            break

    return {
        "shard": shard,
        "start": start,
        "stop": stop,
        "next": next_index,
        "processed": processed,
        "skipped_factor_three": skipped_factor_three,
        "complete": next_index == stop,
        "hits": hits,
        "digest": rolling.hexdigest(),
        "seconds": time.monotonic() - began,
    }


@app.local_entrypoint()
def main() -> None:
    lower, start, stop = interval()
    assert (start, stop, stop - start) == (29_058_991, 33_554_433, 4_495_442)
    assert trace_values(31, 5)[-1] == 2

    work = tasks()
    results = list(scan_shard.map(work, order_outputs=False))
    results.sort(key=lambda item: int(item["shard"]))
    coverage = [(int(item["start"]), int(item["stop"])) for item in results]
    expected = [(task[1], task[2]) for task in work]
    hits = [hit for item in results for hit in item["hits"]]
    source = Path(__file__)
    payload = {
        "app": APP_NAME,
        "decision": "fiber_two_cycle_c2_reciprocal_affine_torsion_screen",
        "order": ORDER,
        "lower_characteristic": lower,
        "upper_characteristic_exclusive": HIGH,
        "k_start": start,
        "k_stop": stop,
        "expected_candidates": stop - start,
        "processed": sum(int(item["processed"]) for item in results),
        "skipped_factor_three": sum(
            int(item["skipped_factor_three"]) for item in results
        ),
        "coverage_exact": coverage == expected,
        "all_complete": all(bool(item["complete"]) for item in results),
        "hits": hits,
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "cost_ceiling_usd": 0.25,
        "shards": results,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    print(
        "RATE_HALF_LIST_C2_RECIPROCAL_AFFINE_TORSION "
        f"processed={payload['processed']} "
        f"complete={payload['all_complete']} "
        f"coverage={payload['coverage_exact']} hits={len(hits)}"
    )

