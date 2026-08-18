#!/usr/bin/env python3
"""Bounded official shifted-inversion falsification probe on Modal."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


APP_NAME = "rate-half-mca-rank11-shifted-inversion-probe"
TAU_SHARDS = 96
PARAMETERS_PER_SHARD = 64
THRESHOLD = 8740
SOURCE = Path(__file__).with_name("rate_half_mca_rank11_shifted_inversion_probe.cpp")
PREREGISTRATION = Path(__file__).with_name(
    "rate_half_mca_rank11_shifted_inversion_probe_preregistration.md"
)
OUTPUT = Path(__file__).with_name("rate_half_mca_rank11_shifted_inversion_probe_result.json")
ROWS_OUTPUT = Path(__file__).with_name("rate_half_mca_rank11_shifted_inversion_probe_rows.jsonl")
SOURCE_SHA256 = "2b4b73c5a9f828e0a669f338d225bd5365bd225f6e47adf61da76c78476f3f51"

app = modal.App(APP_NAME)
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("g++", "time")
    .add_local_file(SOURCE, "/root/probe.cpp")
)


@app.function(image=image, cpu=1.0, memory=768, timeout=60, max_containers=96)
def probe_shard(tau_index: int) -> dict[str, object]:
    began = time.monotonic()
    binary = Path("/tmp/shifted-inversion-probe")
    compile_result = subprocess.run(
        ["g++", "-O3", "-std=c++17", "/root/probe.cpp", "-o", str(binary)],
        capture_output=True,
        text=True,
        timeout=15,
    )
    if compile_result.returncode != 0:
        return {
            "event": "SHARD_ERROR",
            "tau_index": tau_index,
            "stage": "compile",
            "stderr": compile_result.stderr[-4000:],
        }
    try:
        completed = subprocess.run(
            ["/usr/bin/time", "-f", "RSS_KB=%M WALL=%e", str(binary), str(tau_index)],
            capture_output=True,
            text=True,
            timeout=43,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "event": "SHARD_TIMEOUT",
            "tau_index": tau_index,
            "stage": "execute",
            "stdout": (error.stdout or "")[-4000:],
            "stderr": (error.stderr or "")[-4000:],
            "seconds": time.monotonic() - began,
        }
    rows = []
    for line in completed.stdout.splitlines():
        fields = line.split("\t")
        if len(fields) != 8:
            continue
        rows.append(
            {
                "tau_index": int(fields[0]),
                "tau": int(fields[1]),
                "parameter_index": int(fields[2]),
                "kind": fields[3],
                "kappa": int(fields[4]),
                "total_points": int(fields[5]),
                "fixed_points": int(fields[6]),
                "nonfixed_points": int(fields[7]),
            }
        )
    return {
        "event": "SHARD_RESULT",
        "tau_index": tau_index,
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
    returned = list(
        probe_shard.map(
            list(range(TAU_SHARDS)),
            order_outputs=True,
            return_exceptions=True,
        )
    )
    shards = []
    failures = []
    for tau_index, row in enumerate(returned):
        if isinstance(row, Exception):
            failures.append({"tau_index": tau_index, "exception": repr(row)})
            continue
        shards.append(row)
        if row.get("exit") != 0 or len(row.get("rows", [])) != PARAMETERS_PER_SHARD:
            failures.append(row)
    rows = sorted(
        (entry for shard in shards for entry in shard.get("rows", [])),
        key=lambda entry: (entry["tau_index"], entry["parameter_index"]),
    )
    counts = sorted(entry["nonfixed_points"] for entry in rows)
    maximum = max(counts) if counts else None
    maximizing_rows = [entry for entry in rows if entry["nonfixed_points"] == maximum]
    quantiles = {}
    if counts:
        for label, numerator in (("q50", 50), ("q90", 90), ("q99", 99)):
            index = ((len(counts) - 1) * numerator) // 100
            quantiles[label] = counts[index]
    complete = not failures and len(rows) == TAU_SHARDS * PARAMETERS_PER_SHARD
    row_columns = [
        "tau_index",
        "tau",
        "parameter_index",
        "kind",
        "kappa",
        "total_points",
        "fixed_points",
        "nonfixed_points",
    ]
    compact_rows = [[entry[column] for column in row_columns] for entry in rows]
    rows_payload = "".join(
        json.dumps(row, separators=(",", ":")) + "\n" for row in compact_rows
    )
    ROWS_OUTPUT.write_text(rows_payload)
    result = {
        "schema": "rate-half-mca-rank11-shifted-inversion-probe-result-v1",
        "app": APP_NAME,
        "source_sha256": source_hash,
        "dispatcher_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "preregistration_sha256": hashlib.sha256(PREREGISTRATION.read_bytes()).hexdigest(),
        "p": 2130706433,
        "domain_order": 2**21,
        "tau_shards_planned": TAU_SHARDS,
        "parameters_per_shard": PARAMETERS_PER_SHARD,
        "planned_parameter_count": TAU_SHARDS * PARAMETERS_PER_SHARD,
        "completed_shards": sum(
            row.get("event") == "SHARD_RESULT"
            and row.get("exit") == 0
            and len(row.get("rows", [])) == PARAMETERS_PER_SHARD
            for row in shards
        ),
        "completed_parameter_count": len(rows),
        "threshold": THRESHOLD,
        "maximum_nonfixed_points": maximum,
        "maximizing_rows": maximizing_rows,
        "quantiles": quantiles,
        "failures": failures,
        "shard_metrics": [
            {
                "tau_index": row.get("tau_index"),
                "event": row.get("event"),
                "seconds": row.get("seconds"),
                "stderr": row.get("stderr"),
            }
            for row in shards
        ],
        "row_columns": row_columns,
        "rows_file": ROWS_OUTPUT.name,
        "rows_sha256": hashlib.sha256(rows_payload.encode()).hexdigest(),
        "status": "COMPLETE" if complete else "INCOMPLETE",
        "candidate_cap_falsified": maximum is not None and maximum >= THRESHOLD,
        "nonclaim": "A completed sample that does not reach the threshold is heuristic evidence, not a uniform bound.",
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "SHIFTED_INVERSION_PROBE_RESULT "
        + json.dumps(
            {
                "status": result["status"],
                "completed_shards": result["completed_shards"],
                "completed_parameter_count": len(rows),
                "maximum_nonfixed_points": maximum,
                "candidate_cap_falsified": result["candidate_cap_falsified"],
                "quantiles": quantiles,
                "failure_count": len(failures),
                "output": str(OUTPUT),
                "rows_output": str(ROWS_OUTPUT),
            },
            sort_keys=True,
        ),
        flush=True,
    )
