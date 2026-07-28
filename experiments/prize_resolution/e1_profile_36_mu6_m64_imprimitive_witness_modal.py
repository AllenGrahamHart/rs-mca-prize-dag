#!/usr/bin/env python3
"""Retain all rigorous high-side witnesses from the imprimitive atlas."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


ROOT = Path("/repo") if Path("/repo").is_dir() else Path(__file__).resolve().parents[2]
ORBIT_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu6_m64_imprimitive_chord_orbits.json"
CPP_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu6_m64_direct_radius.cpp"
BASE_CPP_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu1_low_energy_exact.cpp"
FIXED_ROOTS_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu6_m64_fixed_roots.hpp"
SHARDS = 64

app = modal.App("e1-profile-36-mu6-m64-imprimitive-witness")
image = (
    modal.Image.debian_slim()
    .apt_install("g++", "libboost-dev")
    .add_local_file(str(CPP_PATH), "/repo/experiments/prize_resolution/worker.cpp", copy=True)
    .add_local_file(
        str(BASE_CPP_PATH),
        "/repo/experiments/prize_resolution/e1_profile_36_mu1_low_energy_exact.cpp",
        copy=True,
    )
    .add_local_file(
        str(FIXED_ROOTS_PATH),
        "/repo/experiments/prize_resolution/e1_profile_36_mu6_m64_fixed_roots.hpp",
        copy=True,
    )
    .run_commands(
        "g++ -O3 -std=c++20 /repo/experiments/prize_resolution/worker.cpp -o /worker"
    )
)


@app.function(image=image, cpu=2.0, memory=256, timeout=180, max_containers=64)
def extract(shard_and_batch: tuple[int, list[list[int]]]) -> dict[str, object]:
    shard, batch = shard_and_batch
    payload = "".join(" ".join(map(str, orbit)) + "\n" for orbit in batch)
    result = subprocess.run(
        ["/worker", "verbose"], input=payload, text=True,
        capture_output=True, timeout=170,
    )
    return {
        "shard": shard, "returncode": result.returncode,
        "stdout": result.stdout, "stderr": result.stderr[-4000:],
        "orbits": len(batch),
    }


@app.local_entrypoint()
def main(
    output: str = (
        "experiments/prize_resolution/"
        "e1_profile_36_mu6_m64_imprimitive_witness_result.json"
    ),
) -> None:
    atlas = json.loads(ORBIT_PATH.read_text())
    tasks = [(shard, atlas["orbits"][shard::SHARDS]) for shard in range(SHARDS)]
    rows = list(extract.map(tasks, order_outputs=True, return_exceptions=True))
    normalized = []
    witnesses = []
    for task, row in zip(tasks, rows, strict=True):
        if isinstance(row, BaseException):
            normalized.append({
                "shard": task[0], "returncode": None, "stdout": "",
                "stderr": repr(row), "orbits": len(task[1]),
            })
        else:
            normalized.append(row)
        lines = str(normalized[-1]["stdout"]).strip().splitlines()
        summary = lines[-1] if lines else ""
        fixed_match = re.search(r"\bfixed_above=([0-9]+)\b", summary)
        shard_witnesses = [line for line in lines if line.startswith("WITNESS ")]
        assert fixed_match and len(shard_witnesses) == int(fixed_match.group(1))
        witnesses.extend(
            {"shard": task[0], "record": record} for record in shard_witnesses
        )
    result = {
        "schema": "e1-profile-36-mu6-m64-imprimitive-witness-result-v1",
        "complete": all(
            row["returncode"] == 0 and not row["stderr"] for row in normalized
        ),
        "orbit_file_sha256": hashlib.sha256(ORBIT_PATH.read_bytes()).hexdigest(),
        "engine_sha256": hashlib.sha256(CPP_PATH.read_bytes()).hexdigest(),
        "fixed_roots_sha256": hashlib.sha256(FIXED_ROOTS_PATH.read_bytes()).hexdigest(),
        "shards": SHARDS,
        "witness_count": len(witnesses),
        "witnesses": witnesses,
        "rows": normalized,
    }
    Path(output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    assert result["complete"] and len(witnesses) == 110
    print(
        "E1_PROFILE_36_MU6_M64_IMPRIMITIVE_WITNESS_PASS "
        f"witnesses={len(witnesses)} output={output}"
    )


if __name__ == "__main__":
    main()
