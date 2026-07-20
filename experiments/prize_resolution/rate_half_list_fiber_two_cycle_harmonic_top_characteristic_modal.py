#!/usr/bin/env python3
"""Bounded screen for the doubled-order harmonic top-lift residue.

Pre-registration
----------------
Decision: on the matched c=0 two-antipodal-denominator cycle branch, test
whether any modulus in the exact official quadratic-field interval with
p=1 mod 2^41 satisfies the one remaining harmonic trace equation c_39=0,
where c_0=4 and c_(j+1)=c_j^2-2 mod p.

The proved old harmonic packet already excludes c_j=0 for 1<=j<=38 over
every p=1 mod 2^40 in this interval. The new field router proves that only
the split class p=1 mod 2^41 can contain an order-2^41 source lift. Thus this
campaign checks only c_39 and only even k in p=1+k*2^40.

PASS: complete exact coverage and no hit. This excludes the harmonic branch.
FAIL: emit every (k,p) hit. A hit is a candidate requiring primality and the
harmonic remainder fourth-power test; it is not a survivor by itself.
INCOMPLETE: emit the next ordinal and rolling digest for every stopped shard.

Resources: 16 independent one-CPU, 512-MiB, 60-second shards, returning at
50 seconds with partial output. This is half the candidate count of the prior
38-step campaign whose conservative cap was $0.25. The same $0.25 ceiling is
used here; no retry is authorized automatically.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from pathlib import Path

import modal


APP_NAME = "rate-half-list-fiber-two-cycle-harmonic-top-characteristic"
ORDER = 1 << 40
SPLIT_ORDER = 1 << 41
LOW_SQUARE = 3 * (1 << 128)
HIGH = 1 << 65
SHARDS = 16

app = modal.App(APP_NAME)
image = modal.Image.debian_slim(python_version="3.12")


def interval() -> tuple[int, int, int, int]:
    lower = math.isqrt(LOW_SQUARE)
    if lower * lower < LOW_SQUARE:
        lower += 1
    start = (lower - 1 + ORDER - 1) // ORDER
    stop = (HIGH - 2) // ORDER + 1
    first_even = start + (start & 1)
    count = max(0, (stop - first_even + 1) // 2)
    return lower, start, stop, count


def tasks() -> list[tuple[int, int, int, int]]:
    _, start, stop, count = interval()
    first_even = start + (start & 1)
    width = (count + SHARDS - 1) // SHARDS
    return [
        (shard, first_even, shard * width, min(count, (shard + 1) * width))
        for shard in range(SHARDS)
        if shard * width < count
    ]


@app.function(
    image=image,
    cpu=1,
    memory=512,
    timeout=60,
    max_containers=SHARDS,
)
def scan_shard(task: tuple[int, int, int, int]) -> dict[str, object]:
    shard, first_even, ordinal_start, ordinal_stop = task
    began = time.monotonic()
    hits: list[dict[str, int]] = []
    rolling = hashlib.sha256()
    processed = 0
    next_ordinal = ordinal_start

    for ordinal in range(ordinal_start, ordinal_stop):
        k_value = first_even + 2 * ordinal
        p_value = 1 + k_value * ORDER
        trace = 4
        for _ in range(39):
            trace = (trace * trace - 2) % p_value
        is_hit = trace == 0
        if is_hit:
            hits.append({"k": k_value, "p": p_value, "index": 39})

        rolling.update(k_value.to_bytes(4, "little"))
        rolling.update(bytes((int(is_hit),)))
        processed += 1
        next_ordinal = ordinal + 1

        if (processed & 4095) == 0 and time.monotonic() - began >= 50.0:
            break

    return {
        "shard": shard,
        "ordinal_start": ordinal_start,
        "ordinal_stop": ordinal_stop,
        "next_ordinal": next_ordinal,
        "processed": processed,
        "complete": next_ordinal == ordinal_stop,
        "hits": hits,
        "digest": rolling.hexdigest(),
        "seconds": time.monotonic() - began,
    }


@app.local_entrypoint()
def main() -> None:
    lower, start, stop, count = interval()
    work = tasks()
    results = list(scan_shard.map(work, order_outputs=False))
    results.sort(key=lambda item: int(item["shard"]))
    expected = [(task[2], task[3]) for task in work]
    coverage = [
        (int(item["ordinal_start"]), int(item["ordinal_stop"]))
        for item in results
    ]
    hits = [hit for item in results for hit in item["hits"]]
    source = Path(__file__)
    payload = {
        "app": APP_NAME,
        "decision": "fiber_two_cycle_harmonic_order_2_41_screen",
        "order": ORDER,
        "split_order": SPLIT_ORDER,
        "lower_characteristic": lower,
        "upper_characteristic_exclusive": HIGH,
        "k_start": start,
        "k_stop": stop,
        "parity": "even",
        "expected_candidates": count,
        "processed": sum(int(item["processed"]) for item in results),
        "coverage_exact": coverage == expected,
        "all_complete": all(bool(item["complete"]) for item in results),
        "hits": hits,
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "shards": results,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    print(
        "RATE_HALF_FIBER_TWO_CYCLE_HARMONIC_TOP_CHARACTERISTIC "
        f"processed={payload['processed']} complete={payload['all_complete']} "
        f"coverage={payload['coverage_exact']} hits={len(hits)}"
    )
