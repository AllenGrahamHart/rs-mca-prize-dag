#!/usr/bin/env python3
"""Run the dual exact E<=6 classifiers for profile multiplicities 2 and 10."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess

import modal


ROOT = Path("/repo") if Path("/repo").is_dir() else Path(__file__).resolve().parents[2]
ORBIT_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu2_mu10_light_chord_orbits.json"
CPP_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu1_low_energy_exact.cpp"

app = modal.App("e1-profile-36-mu2-mu10-low-energy-exact")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(
        str(CPP_PATH),
        "/repo/experiments/prize_resolution/e1_profile_36_low_energy_exact.cpp",
        copy=True,
    )
    .run_commands(
        "g++ -O3 -std=c++20 "
        "/repo/experiments/prize_resolution/e1_profile_36_low_energy_exact.cpp "
        "-o /worker"
    )
)


@app.function(image=image, cpu=2.0, memory=2048, timeout=280, max_containers=24)
def classify_batch(mu: int, batch: list[list[int]], engine: str) -> dict[str, object]:
    payload = "".join(" ".join(map(str, orbit)) + "\n" for orbit in batch)
    argv = ["/worker"] + (["triple"] if engine == "triple-xor" else [])
    result = subprocess.run(
        argv, input=payload, text=True, capture_output=True, timeout=270
    )
    return {
        "mu": mu,
        "returncode": result.returncode,
        "stdout": result.stdout[-4000:],
        "stderr": result.stderr[-4000:],
        "orbits": len(batch),
    }


@app.local_entrypoint()
def main(
    shards: int = 24,
    mus: str = "2,10",
    engine: str = "pair-xor-plus-third",
    output: str = "experiments/prize_resolution/e1_profile_36_mu2_mu10_low_energy_exact_result.json",
) -> None:
    orbit_payload = json.loads(ORBIT_PATH.read_text())
    selected_mus = tuple(int(value) for value in mus.split(",") if value)
    assert selected_mus and set(selected_mus) <= {2, 10}
    tasks = []
    expected = {}
    for mu in selected_mus:
        target = orbit_payload["targets"][str(mu)]
        orbits = target["orbits"]
        expected[mu] = int(target["affine_orbits"])
        tasks.extend(
            (mu, orbits[index::shards], engine) for index in range(shards)
        )
    rows = list(classify_batch.starmap(tasks))
    for index, row in enumerate(rows):
        print(f"task={index} {row}")
    assert all(row["returncode"] == 0 and not row["stderr"] for row in rows)
    for mu in selected_mus:
        assert sum(int(row["orbits"]) for row in rows if row["mu"] == mu) == expected[mu]

    result = {
        "schema": "e1-profile-36-mu2-mu10-low-energy-exact-result-v1",
        "engine": engine,
        "orbit_file_sha256": hashlib.sha256(ORBIT_PATH.read_bytes()).hexdigest(),
        "engine_sha256": hashlib.sha256(CPP_PATH.read_bytes()).hexdigest(),
        "multiplicities": selected_mus,
        "affine_orbits": {str(mu): expected[mu] for mu in selected_mus},
        "shards_per_mu": shards,
        "passed": len(rows),
        "rows": rows,
    }
    output_path = Path(output)
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "E1_PROFILE_36_MU2_MU10_LOW_ENERGY_EXACT_PASS "
        f"engine={engine} multiplicities={selected_mus} "
        f"orbits={sum(expected.values())} "
        f"output={output}"
    )
