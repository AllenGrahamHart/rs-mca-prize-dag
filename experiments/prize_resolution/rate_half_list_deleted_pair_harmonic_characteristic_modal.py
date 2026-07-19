#!/usr/bin/env python3
"""Complete bounded screen for the remaining harmonic deleted-pair branch.

Pre-registration
----------------
Decision: determine whether an official split-quadratic characteristic can
support r^2-4r+1=0 with r of 2-power order dividing 2^40.

PASS: no modulus p=1 mod 2^40 in the exact B*=3 interval divides any required
Chebyshev trace; the complete q=-1 branch is excluded.

FAIL: print every (p, trace index) hit. Prime hits remain live and must be sent
through the remainder fourth-power test; composite hits are harmless.

Resources: 32 independent one-CPU, 512-MiB, 60-second shards. Each shard
returns at 50 seconds with its next index and partial hits. Conservative cost
cap: $0.25. No raw artifact or repository upload is required.
"""

from __future__ import annotations

import hashlib
import json
import math
import time

import modal


APP_NAME = "rate-half-list-deleted-pair-harmonic-characteristic"
ORDER = 1 << 40
LOW_SQUARE = 3 * (1 << 128)
HIGH = 1 << 65
SHARDS = 32

app = modal.App(APP_NAME)
image = modal.Image.debian_slim(python_version="3.12")


def interval() -> tuple[int, int, int]:
    lower = math.isqrt(LOW_SQUARE)
    if lower * lower < LOW_SQUARE:
        lower += 1
    start = (lower - 1 + ORDER - 1) // ORDER
    stop = (HIGH - 2) // ORDER + 1
    return lower, start, stop


def tasks() -> list[tuple[int, int, int]]:
    _, start, stop = interval()
    width = (stop - start + SHARDS - 1) // SHARDS
    return [
        (index, start + index * width, min(stop, start + (index + 1) * width))
        for index in range(SHARDS)
        if start + index * width < stop
    ]


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
    hits: list[dict[str, int]] = []
    processed = 0
    rolling = hashlib.sha256()
    next_index = start

    for k_value in range(start, stop):
        p_value = 1 + k_value * ORDER
        trace = 4
        hit_index = -1
        for index in range(1, 39):
            trace = (trace * trace - 2) % p_value
            if trace == 0:
                hit_index = index
                hits.append({"k": k_value, "p": p_value, "index": index})
                break

        rolling.update(k_value.to_bytes(4, "little"))
        rolling.update(hit_index.to_bytes(2, "little", signed=True))
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
        "complete": next_index == stop,
        "hits": hits,
        "digest": rolling.hexdigest(),
        "seconds": time.monotonic() - began,
    }


@app.local_entrypoint()
def main() -> None:
    lower, start, stop = interval()
    work = tasks()
    results = list(scan_shard.map(work, order_outputs=False))
    results.sort(key=lambda item: int(item["shard"]))

    coverage = [(int(item["start"]), int(item["stop"])) for item in results]
    expected = [(task[1], task[2]) for task in work]
    all_complete = all(bool(item["complete"]) for item in results)
    hits = [hit for item in results for hit in item["hits"]]
    payload = {
        "app": APP_NAME,
        "decision": "harmonic_q_minus_one_characteristic_screen",
        "order": ORDER,
        "lower_characteristic": lower,
        "upper_characteristic_exclusive": HIGH,
        "k_start": start,
        "k_stop": stop,
        "expected_candidates": stop - start,
        "processed": sum(int(item["processed"]) for item in results),
        "coverage_exact": coverage == expected,
        "all_complete": all_complete,
        "hits": hits,
        "shards": results,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    print(
        "RATE_HALF_DELETED_PAIR_HARMONIC_CHARACTERISTIC "
        f"processed={payload['processed']} complete={all_complete} "
        f"coverage={payload['coverage_exact']} hits={len(hits)}"
    )

