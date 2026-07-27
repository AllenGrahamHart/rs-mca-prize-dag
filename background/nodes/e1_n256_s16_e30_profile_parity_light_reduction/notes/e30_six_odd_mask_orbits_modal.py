#!/usr/bin/env python3
"""Classify all E30 six-odd masks and affine light-support orbits."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e30_six_odd_mask_orbits.cpp"
RESULT = HERE / "e30_six_odd_mask_orbits_result.json"
REMOTE_SOURCE = "/root/e30_six_odd_mask_orbits.cpp"
REMOTE_BINARY = "/root/e30_six_odd_mask_orbits"
SHARDS = 4

app = modal.App("e1-n256-e30-six-odd-mask-orbits")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(SOURCE, REMOTE_SOURCE, copy=True)
    .run_commands(f"g++ -O3 -std=c++17 {REMOTE_SOURCE} -o {REMOTE_BINARY}")
)


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=4)
def run_shard(shard: int) -> dict[str, object]:
    import subprocess
    import time

    started = time.monotonic()
    completed = subprocess.run(
        [REMOTE_BINARY, str(shard), str(SHARDS)],
        check=True,
        capture_output=True,
        text=True,
        timeout=55,
    )
    packet = json.loads(completed.stdout)
    packet["worker_seconds"] = time.monotonic() - started
    return packet


@app.local_entrypoint()
def main() -> None:
    shards: list[dict[str, object]] = []

    def write_checkpoint(complete: bool) -> dict[str, object]:
        merged: dict[int, set[tuple[int, ...]]] = {}
        for shard in shards:
            for row in shard["rows"]:
                merged.setdefault(int(row["odd_mask"]), set()).update(
                    tuple(map(int, orbit)) for orbit in row["orbits"]
                )
        rows = [
            {"odd_mask": mask, "orbits": [list(orbit) for orbit in sorted(orbits)]}
            for mask, orbits in sorted(merged.items())
        ]
        histogram: dict[str, int] = {}
        for row in rows:
            count = len(row["orbits"])
            histogram[str(count)] = histogram.get(str(count), 0) + 1
        packet = {
            "schema": "e1-e30-six-odd-mask-orbits-v1",
            "complete": complete,
            "completed_shards": len(shards),
            "expected_shards": SHARDS,
            "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "summary": {
                "normalized_six_odd_supports": sum(
                    int(shard["normalized_six_odd_supports"]) for shard in shards
                ),
                "distinct_odd_masks": len(rows),
                "affine_light_orbits": sum(len(row["orbits"]) for row in rows),
                "orbits_per_mask_histogram": histogram,
                "worker_seconds": sum(float(shard["worker_seconds"]) for shard in shards),
            },
            "rows": rows,
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return packet

    write_checkpoint(False)
    try:
        for shard in run_shard.map(range(SHARDS)):
            shards.append(shard)
            write_checkpoint(False)
    except BaseException:
        print(f"E30_SIX_ODD_MASK_ORBITS_INCOMPLETE completed={len(shards)}/{SHARDS}")
        raise
    packet = write_checkpoint(
        len(shards) == SHARDS and all(bool(shard["complete"]) for shard in shards)
    )
    print("E30_SIX_ODD_MASK_ORBITS " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E30_SIX_ODD_MASK_ORBITS_RESULT {RESULT}")
