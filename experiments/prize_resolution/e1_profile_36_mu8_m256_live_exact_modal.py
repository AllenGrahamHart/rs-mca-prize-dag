#!/usr/bin/env python3
"""Run the exact cofactor-256 live-chamber census on Modal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


ROOT = Path("/repo") if Path("/repo").is_dir() else Path(__file__).resolve().parents[2]
ORBIT_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu8_m256_chord_orbits.json"
CPP_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu8_m256_live_exact.cpp"
BASE_CPP_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu1_low_energy_exact.cpp"

app = modal.App("e1-profile-36-mu8-m256-live-exact")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(str(CPP_PATH), "/repo/experiments/prize_resolution/worker.cpp", copy=True)
    .add_local_file(
        str(BASE_CPP_PATH),
        "/repo/experiments/prize_resolution/e1_profile_36_mu1_low_energy_exact.cpp",
        copy=True,
    )
    .run_commands(
        "g++ -O3 -std=c++20 /repo/experiments/prize_resolution/worker.cpp -o /worker"
    )
)


@app.function(image=image, cpu=2.0, memory=768, timeout=180, max_containers=24)
def classify_batch(batch: list[list[int]], engine: str) -> dict[str, object]:
    payload = "".join(" ".join(map(str, orbit)) + "\n" for orbit in batch)
    argv = ["/worker"] + (["sorted"] if engine == "sorted-blocks" else [])
    result = subprocess.run(
        argv, input=payload, text=True, capture_output=True, timeout=170
    )
    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr[-4000:],
        "orbits": len(batch),
    }


@app.local_entrypoint()
def main(
    shards: int = 24,
    engine: str = "hash-blocks",
    output: str = (
        "experiments/prize_resolution/"
        "e1_profile_36_mu8_m256_live_exact_result.json"
    ),
) -> None:
    orbit_payload = json.loads(ORBIT_PATH.read_text())
    orbits = orbit_payload["orbits"]
    batches = [orbits[index::shards] for index in range(shards)]
    rows = list(classify_batch.starmap((batch, engine) for batch in batches))
    for index, row in enumerate(rows):
        lines = str(row["stdout"]).splitlines()
        summary = lines[-1] if lines else "NO_STDOUT"
        print(
            f"shard={index} returncode={row['returncode']} "
            f"orbits={row['orbits']} lines={len(lines)} {summary}"
        )
    assert all(row["returncode"] == 0 and not row["stderr"] for row in rows)
    assert sum(int(row["orbits"]) for row in rows) == orbit_payload["affine_orbits"]
    counts: dict[str, int] = {}
    candidate_lines = 0
    for row in rows:
        for line in str(row["stdout"]).splitlines():
            if line.startswith("CANDIDATE "):
                candidate_lines += 1
            if line.startswith("PASS "):
                for key, value in re.findall(r"([A-Za-z_0-9]+)=([0-9]+)", line):
                    counts[key] = counts.get(key, 0) + int(value)
    result = {
        "schema": "e1-profile-36-mu8-m256-live-exact-result-v1",
        "engine": engine,
        "orbit_file_sha256": hashlib.sha256(ORBIT_PATH.read_bytes()).hexdigest(),
        "engine_sha256": hashlib.sha256(CPP_PATH.read_bytes()).hexdigest(),
        "affine_orbits": orbit_payload["affine_orbits"],
        "shards": shards,
        "passed": len(rows),
        "counts": counts,
        "candidate_lines": candidate_lines,
        "rows": rows,
    }
    output_path = Path(output)
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "E1_PROFILE_36_MU8_M256_LIVE_EXACT_PASS "
        f"engine={engine} orbits={orbit_payload['affine_orbits']} "
        f"candidate_lines={candidate_lines} counts={counts} output={output}"
    )


if __name__ == "__main__":
    main()
