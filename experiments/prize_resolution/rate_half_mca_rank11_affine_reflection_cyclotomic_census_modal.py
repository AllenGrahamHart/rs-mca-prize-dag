#!/usr/bin/env python3
"""Complete official affine-reflection cyclotomic census on Modal."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


APP_NAME = "rate-half-mca-rank11-affine-reflection-cyclotomic-census"
P = 2_130_706_433
N = 2**21
INDEX = 1016
GENERATOR = 3
SHARD_SIZE = 11
SOURCE = Path(__file__).with_name(
    "rate_half_mca_rank11_affine_reflection_cyclotomic_census.cpp"
)
SOURCE_SHA256 = "a910d1f447cf2f0895a5b050a2de79de57831c7ca22679065c2cdc53b948a00b"

app = modal.App(APP_NAME)
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("g++", "time")
    .add_local_file(SOURCE, "/root/census.cpp")
)


@app.function(image=image, cpu=1.0, memory=768, timeout=60, max_containers=93)
def census_shard(bounds: tuple[int, int]) -> dict[str, object]:
    lo, hi = bounds
    began = time.monotonic()
    binary = Path("/tmp/census")
    compile_result = subprocess.run(
        ["g++", "-O3", "-std=c++17", "/root/census.cpp", "-o", str(binary)],
        capture_output=True,
        text=True,
        timeout=15,
    )
    if compile_result.returncode != 0:
        return {
            "event": "SHARD_ERROR",
            "lo": lo,
            "hi": hi,
            "stage": "compile",
            "stderr": compile_result.stderr[-4000:],
        }
    completed = subprocess.run(
        ["/usr/bin/time", "-f", "RSS_KB=%M WALL=%e", str(binary), str(lo), str(hi)],
        capture_output=True,
        text=True,
        timeout=50,
    )
    rows = []
    for line in completed.stdout.splitlines():
        fields = line.split("\t")
        if len(fields) == 4:
            rows.append([int(field) for field in fields])
    return {
        "event": "SHARD_RESULT",
        "lo": lo,
        "hi": hi,
        "exit": completed.returncode,
        "rows": rows,
        "stderr": completed.stderr[-4000:],
        "seconds": time.monotonic() - began,
    }


@app.local_entrypoint()
def main() -> None:
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if source_hash != SOURCE_SHA256:
        raise RuntimeError(f"source hash mismatch: {source_hash}")
    bounds = [
        (lo, min(lo + SHARD_SIZE, INDEX))
        for lo in range(0, INDEX, SHARD_SIZE)
    ]
    returned = list(
        census_shard.map(bounds, order_outputs=True, return_exceptions=True)
    )
    shards = []
    failures = []
    for bound, row in zip(bounds, returned):
        if isinstance(row, Exception):
            failures.append({"bounds": bound, "exception": repr(row)})
        else:
            shards.append(row)
            if row.get("exit") != 0 or len(row.get("rows", [])) != bound[1] - bound[0]:
                failures.append(row)
    rows = sorted(
        (entry for shard in shards for entry in shard.get("rows", [])),
        key=lambda entry: entry[0],
    )
    result = {
        "schema": "rate-half-mca-rank11-affine-reflection-cyclotomic-census-result-v1",
        "app": APP_NAME,
        "source_sha256": source_hash,
        "p": P,
        "domain_order": N,
        "index": INDEX,
        "primitive_generator": GENERATOR,
        "shard_size": SHARD_SIZE,
        "shard_count": len(bounds),
        "completed_shards": len(shards),
        "failures": failures,
        "rows": rows,
        "status": "COMPLETE" if not failures and len(rows) == INDEX else "INCOMPLETE",
        "nonclaim": "A complete exact census is proof input only after the independent checker passes.",
    }
    if rows:
        counts = [entry[2] for entry in rows]
        result.update({
            "count_sum": sum(counts),
            "maximum_reflection_points": max(counts),
            "maximizing_indices": [entry[0] for entry in rows if entry[2] == max(counts)],
        })
    print("AFFINE_REFLECTION_CENSUS_RESULT " + json.dumps(result, sort_keys=True), flush=True)
