#!/usr/bin/env python3
"""Run the complete n=32 ambient-Q high-cap scan on four Modal shards."""

from __future__ import annotations

import csv
import io
import json
from pathlib import Path
import subprocess
import time

import modal


HERE = Path(__file__).resolve().parent
RANGES = [(32769, 40959), (40960, 49151), (49152, 57343), (57344, 65535)]

app = modal.App("rs-mca-c2-ambient-q-highcap")
image = modal.Image.debian_slim().apt_install("g++").add_local_file(
    str(HERE / "scan.cpp"), "/root/scan.cpp"
)


def parse_rows(text: str) -> list[dict[str, int | bool]]:
    output = []
    for row in csv.DictReader(io.StringIO(text)):
        output.append({
            "q": int(row["q"]),
            "z0": int(row["z0"]),
            "c1": int(row["c1"]),
            "primitive": int(row["primitive"]),
            "fires": row["fires"] == "1",
            "z1": int(row["z1"]),
            "b0": int(row["b0"]),
            "j_fires": row["j_fires"] == "1",
        })
    return output


@app.function(image=image, cpu=2.0, memory=1024, timeout=150, max_containers=4)
def scan_shard(bounds: tuple[int, int]) -> dict[str, object]:
    low, high = bounds
    started = time.monotonic()
    subprocess.run(
        ["g++", "-O3", "-std=c++17", "/root/scan.cpp", "-o", "/tmp/scan"],
        check=True,
        capture_output=True,
        text=True,
        timeout=45,
    )
    try:
        process = subprocess.run(
            ["/tmp/scan", str(low), str(high)],
            check=True,
            capture_output=True,
            text=True,
            timeout=95,
        )
        return {
            "status": "PASS",
            "low": low,
            "high": high,
            "rows": parse_rows(process.stdout),
            "seconds": time.monotonic() - started,
        }
    except subprocess.TimeoutExpired as error:
        partial = error.stdout or ""
        if isinstance(partial, bytes):
            partial = partial.decode(errors="replace")
        return {
            "status": "TIMEOUT",
            "low": low,
            "high": high,
            "rows": parse_rows(partial),
            "seconds": time.monotonic() - started,
        }


@app.local_entrypoint()
def main(output: str = str(HERE / "results.json")) -> None:
    destination = Path(output)
    shards = []
    for result in scan_shard.map(RANGES, order_outputs=False):
        shards.append(result)
        payload = {
            "schema": "c2-ambient-q-highcap-v1",
            "ranges_requested": [list(bounds) for bounds in RANGES],
            "shards": sorted(shards, key=lambda shard: shard["low"]),
        }
        destination.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        print(json.dumps({key: value for key, value in result.items() if key != "rows"},
                         sort_keys=True), flush=True)
