#!/usr/bin/env python3
"""Run the exact mu=1, E<=6 profile-(3,6) classifier on Modal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess

import modal


ROOT = Path("/repo") if Path("/repo").is_dir() else Path(__file__).resolve().parents[2]
ORBIT_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu1_light_chord_orbits.json"
CPP_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu1_low_energy_exact.cpp"

app = modal.App("e1-profile-36-mu1-low-energy-exact")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(
        str(CPP_PATH),
        "/repo/experiments/prize_resolution/e1_profile_36_mu1_low_energy_exact.cpp",
        copy=True,
    )
    .run_commands(
        "g++ -O3 -std=c++20 "
        "/repo/experiments/prize_resolution/e1_profile_36_mu1_low_energy_exact.cpp "
        "-o /worker"
    )
)


@app.function(image=image, cpu=2, memory=2048, timeout=280, max_containers=24)
def classify_batch(batch: list[list[int]], engine: str) -> dict[str, object]:
    payload = "".join(" ".join(map(str, orbit)) + "\n" for orbit in batch)
    argv = ["/worker"] + (["triple"] if engine == "triple-xor" else [])
    result = subprocess.run(
        argv, input=payload, text=True, capture_output=True, timeout=270
    )
    return {
        "returncode": result.returncode,
        "stdout": result.stdout[-4000:],
        "stderr": result.stderr[-4000:],
        "orbits": len(batch),
    }


@app.local_entrypoint()
def main(
    shards: int = 24,
    engine: str = "pair-xor-plus-third",
    output: str = "experiments/prize_resolution/e1_profile_36_mu1_low_energy_exact_result.json",
) -> None:
    payload = json.loads(ORBIT_PATH.read_text())
    orbits = payload["orbits"]
    batches = [orbits[index::shards] for index in range(shards)]
    rows = list(classify_batch.starmap((batch, engine) for batch in batches))
    passed = 0
    for index, row in enumerate(rows):
        print(f"shard={index} {row}")
        if row["returncode"] == 0:
            passed += 1
    assert sum(int(row["orbits"]) for row in rows) == payload["affine_orbits"]
    assert passed == shards
    result = {
        "schema": "e1-profile-36-mu1-low-energy-exact-result-v1",
        "engine": engine,
        "orbit_file_sha256": hashlib.sha256(ORBIT_PATH.read_bytes()).hexdigest(),
        "affine_orbits": payload["affine_orbits"],
        "shards": shards,
        "passed": passed,
        "rows": rows,
    }
    Path(output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "E1_PROFILE_36_MU1_LOW_ENERGY_EXACT_PASS "
        f"orbits={payload['affine_orbits']} shards={shards} output={output}"
    )
