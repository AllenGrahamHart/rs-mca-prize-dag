#!/usr/bin/env python3
"""Bounded screen for the c=1 parity harmonic residue classes.

Pre-registration
----------------
Decision: over every modulus p=1+k*2^40 in the exact official quadratic
field interval, test the two fixed torsion traces left by the proved c=1
parity harmonic field router:

H_P: u_0=8/5, u_(j+1)=u_j^2-2, require u_41=2.
H_R: v_1=16,  v_(j+1)=v_j^2-2, require v_41=2.

PASS: complete exact coverage and no hit for either trace. This excludes the
harmonic c=1 two-antipodal-denominator subbranch.

FAIL: emit every (k,p,branch) hit. A hit is only a candidate characteristic;
it must still pass primality, primary/secondary gaps, and canonical span.

INCOMPLETE: every shard returns its next k, rolling digest, and partial hits.

Resources: 32 independent one-CPU, 512-MiB, 60-second shards, returning at
50 seconds with partial output. The analogous 4,495,441-modulus 38-level
campaign completed in about 31 local CPU-seconds and under its $0.25 Modal
cap. This two-trace campaign has a conservative $0.50 total ceiling. No
automatic retry is authorized.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from pathlib import Path

import modal


APP_NAME = "rate-half-list-fiber-two-cycle-c1-parity-harmonic-characteristic"
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
    shard, start, stop = task
    began = time.monotonic()
    hits: list[dict[str, int | str]] = []
    rolling = hashlib.sha256()
    processed = 0
    skipped_factor_five = 0
    next_index = start

    for k_value in range(start, stop):
        modulus = 1 + k_value * ORDER
        code = 0
        if modulus % 5 == 0:
            code = 4
            skipped_factor_five += 1
        else:
            h_r_hit = trace_terminal(16, 40, modulus) == 2
            h_p_start = 8 * pow(5, -1, modulus) % modulus
            h_p_hit = trace_terminal(h_p_start, 41, modulus) == 2
            code = int(h_r_hit) + 2 * int(h_p_hit)
            if h_r_hit:
                hits.append({"k": k_value, "p": modulus, "branch": "H_R"})
            if h_p_hit:
                hits.append({"k": k_value, "p": modulus, "branch": "H_P"})

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
        "skipped_factor_five": skipped_factor_five,
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
    hits = [hit for item in results for hit in item["hits"]]
    source = Path(__file__)
    payload = {
        "app": APP_NAME,
        "decision": "fiber_two_cycle_c1_parity_harmonic_characteristic_screen",
        "order": ORDER,
        "lower_characteristic": lower,
        "upper_characteristic_exclusive": HIGH,
        "k_start": start,
        "k_stop": stop,
        "expected_candidates": stop - start,
        "processed": sum(int(item["processed"]) for item in results),
        "skipped_factor_five": sum(
            int(item["skipped_factor_five"]) for item in results
        ),
        "coverage_exact": coverage == expected,
        "all_complete": all(bool(item["complete"]) for item in results),
        "hits": hits,
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "cost_ceiling_usd": 0.50,
        "shards": results,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    print(
        "RATE_HALF_FIBER_TWO_CYCLE_C1_PARITY_HARMONIC_CHARACTERISTIC "
        f"processed={payload['processed']} "
        f"complete={payload['all_complete']} "
        f"coverage={payload['coverage_exact']} hits={len(hits)}"
    )

