#!/usr/bin/env python3
"""Run the exact E=36 inner-layer Schur census on Modal."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import modal


ROOT = Path(__file__).resolve().parents[3]
NOTES = (
    ROOT
    / "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes"
)
CPP = NOTES / "e36_bbb64_census.cpp"
OUTPUT = NOTES / "e36_bbb64_census_result.json"
SHARDS = 16
base = modal.Image.debian_slim().apt_install("g++")
image = (
    base.add_local_file(str(CPP), "/root/census.cpp", copy=True)
    .run_commands("g++ -O3 -std=c++17 /root/census.cpp -o /usr/local/bin/bbb64-census")
)
app = modal.App("e1-e36-bbb64-census")


@app.function(image=image, cpu=1.0, memory=256, timeout=120, max_containers=16)
def census_shard(shard: int) -> dict[str, object]:
    completed = subprocess.run(
        ["/usr/local/bin/bbb64-census", str(shard), str(SHARDS)],
        capture_output=True,
        check=True,
        text=True,
        timeout=110,
    )
    return json.loads(completed.stdout)


@app.local_entrypoint()
def main() -> None:
    results = list(census_shard.map(range(SHARDS), return_exceptions=True))
    complete = [result for result in results if isinstance(result, dict)]
    packet = {
        "schema": "e1-e36-bbb64-census-v1",
        "complete": len(complete) == SHARDS,
        "source_sha256": hashlib.sha256(CPP.read_bytes()).hexdigest(),
        "errors": [repr(result) for result in results if not isinstance(result, dict)],
        "results": complete,
        "processed": sum(int(result["processed"]) for result in complete),
        "best": max(complete, key=lambda result: int(result["best"]))
        if complete
        else None,
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print("E1_E36_BBB64_CENSUS " + repr(packet))
