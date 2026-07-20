#!/usr/bin/env python3
"""Bounded screen for exceptional anti-invariant c=1 parity lifts.

Pre-registration
----------------
Decision: in the nonsplit positive-quadratic shard

    p=1+k*2^40,  k odd,
    ceil(sqrt(3*2^128)) <= p < 2^65,

test the two fixed torsion traces left by the exact Frobenius factorization:

R1/R2: v_0=-8,  v_(j+1)=v_j^2-2, require v_40=2.
P1/P2: u_0=6/5, u_(j+1)=u_j^2-2, require u_40=2.

PASS: complete exact coverage and no hit. Together with the algebraic router,
this excludes every anti-invariant branch except R0.

FAIL: emit every (k,p,branch) hit. A hit is only a candidate characteristic;
it must still pass primality and all polynomial gates.

INCOMPLETE: every shard returns its next odd-index position, rolling digest,
and partial hits.

Resources: 16 independent one-CPU, 512-MiB, 60-second shards, returning at
50 seconds with partial output. This is half the modulus count and the same
per-modulus recurrence work as the completed $0.50 harmonic campaign. The
conservative total ceiling is $0.25. No automatic retry is authorized.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from pathlib import Path

import modal


APP_NAME = "rate-half-list-fiber-two-cycle-c1-parity-antiinvariant"
ORDER = 1 << 40
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
    first_odd = start if start % 2 else start + 1
    odd_count = (stop - first_odd + 1) // 2
    return lower, start, stop, odd_count


def tasks() -> list[tuple[int, int, int]]:
    _, _, _, count = interval()
    width = (count + SHARDS - 1) // SHARDS
    return [
        (index, index * width, min(count, (index + 1) * width))
        for index in range(SHARDS)
        if index * width < count
    ]


def trace_terminal(value: int, levels: int, modulus: int) -> int:
    for _ in range(levels):
        value = (value * value - 2) % modulus
    return value


@app.function(
    image=image,
    cpu=1,
    memory=512,
    timeout=60,
    max_containers=SHARDS,
)
def scan_shard(task: tuple[int, int, int]) -> dict[str, object]:
    shard, index_start, index_stop = task
    lower, start, _, _ = interval()
    del lower
    first_odd = start if start % 2 else start + 1
    began = time.monotonic()
    hits: list[dict[str, int | str]] = []
    rolling = hashlib.sha256()
    processed = 0
    skipped_factor_five = 0
    next_index = index_start

    for index in range(index_start, index_stop):
        k_value = first_odd + 2 * index
        modulus = 1 + k_value * ORDER
        code = 0
        if modulus % 5 == 0:
            code = 4
            skipped_factor_five += 1
        else:
            r_hit = trace_terminal(-8 % modulus, 40, modulus) == 2
            p_start = 6 * pow(5, -1, modulus) % modulus
            p_hit = trace_terminal(p_start, 40, modulus) == 2
            code = int(r_hit) + 2 * int(p_hit)
            if r_hit:
                hits.append({"k": k_value, "p": modulus, "branch": "R12"})
            if p_hit:
                hits.append({"k": k_value, "p": modulus, "branch": "P12"})

        rolling.update(k_value.to_bytes(4, "little"))
        rolling.update(bytes((code,)))
        processed += 1
        next_index = index + 1

        if (processed & 4095) == 0 and time.monotonic() - began >= 50.0:
            break

    return {
        "shard": shard,
        "index_start": index_start,
        "index_stop": index_stop,
        "next_index": next_index,
        "processed": processed,
        "skipped_factor_five": skipped_factor_five,
        "complete": next_index == index_stop,
        "hits": hits,
        "digest": rolling.hexdigest(),
        "seconds": time.monotonic() - began,
    }


@app.local_entrypoint()
def main() -> None:
    lower, start, stop, odd_count = interval()
    work = tasks()
    results = list(scan_shard.map(work, order_outputs=False))
    results.sort(key=lambda item: int(item["shard"]))
    coverage = [
        (int(item["index_start"]), int(item["index_stop"]))
        for item in results
    ]
    expected = [(task[1], task[2]) for task in work]
    hits = [hit for item in results for hit in item["hits"]]
    source = Path(__file__)
    payload = {
        "app": APP_NAME,
        "decision": "fiber_two_cycle_c1_parity_antiinvariant_screen",
        "order": ORDER,
        "lower_characteristic": lower,
        "upper_characteristic_exclusive": HIGH,
        "k_start": start,
        "k_stop": stop,
        "odd_candidates": odd_count,
        "processed": sum(int(item["processed"]) for item in results),
        "skipped_factor_five": sum(
            int(item["skipped_factor_five"]) for item in results
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
        "RATE_HALF_FIBER_TWO_CYCLE_C1_PARITY_ANTIINVARIANT "
        f"processed={payload['processed']} "
        f"complete={payload['all_complete']} "
        f"coverage={payload['coverage_exact']} hits={len(hits)}"
    )

