#!/usr/bin/env python3
"""Run the complete direct radius census on the imprimitive mu-six atlas."""

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

COUNT_KEYS = (
    "orbits", "triple_syndromes", "distance_tests", "radius_matches",
    "exact_sign_tests", "low_energy_vectors", "product_live_vectors",
    "screen_below", "screen_above", "screen_near", "fixed_below",
    "fixed_above", "fixed_unresolved",
)

app = modal.App("e1-profile-36-mu6-m64-imprimitive-direct-radius")
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


@app.function(image=image, cpu=2.0, memory=256, timeout=240, max_containers=64)
def classify_batch(batch: list[list[int]]) -> dict[str, object]:
    payload = "".join(" ".join(map(str, orbit)) + "\n" for orbit in batch)
    result = subprocess.run(
        ["/worker"], input=payload, text=True, capture_output=True, timeout=230
    )
    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr[-4000:],
        "orbits": len(batch),
    }


@app.local_entrypoint()
def main(
    shards: int = 64,
    output: str = (
        "experiments/prize_resolution/"
        "e1_profile_36_mu6_m64_imprimitive_direct_radius_result.json"
    ),
) -> None:
    atlas = json.loads(ORBIT_PATH.read_text())
    batches = [atlas["orbits"][index::shards] for index in range(shards)]
    rows = list(classify_batch.map(batches, order_outputs=True, return_exceptions=True))
    normalized = []
    counts = {key: 0 for key in COUNT_KEYS}
    worker_seconds = []
    for index, row in enumerate(rows):
        if isinstance(row, BaseException):
            normalized.append({
                "returncode": None, "stdout": "", "stderr": repr(row),
                "orbits": len(batches[index]),
            })
        else:
            normalized.append(row)
        summary = str(normalized[-1]["stdout"]).strip()
        parsed = dict(re.findall(r"([a-z_]+)=([0-9]+)(?=\s|$)", summary))
        assert summary.startswith("PASS ") and all(key in parsed for key in COUNT_KEYS)
        for key in COUNT_KEYS:
            counts[key] += int(parsed[key])
        seconds_match = re.search(r"\bseconds=([0-9]+(?:\.[0-9]+)?)$", summary)
        assert seconds_match
        worker_seconds.append(float(seconds_match.group(1)))
        print(
            f"shard={index} returncode={normalized[-1]['returncode']} "
            f"orbits={normalized[-1]['orbits']} {summary}"
        )
    result = {
        "schema": "e1-profile-36-mu6-m64-imprimitive-direct-radius-result-v1",
        "complete": all(
            row["returncode"] == 0 and not row["stderr"] for row in normalized
        ),
        "orbit_file_sha256": hashlib.sha256(ORBIT_PATH.read_bytes()).hexdigest(),
        "engine_sha256": hashlib.sha256(CPP_PATH.read_bytes()).hexdigest(),
        "fixed_roots_sha256": hashlib.sha256(FIXED_ROOTS_PATH.read_bytes()).hexdigest(),
        "affine_orbits": atlas["affine_orbits"],
        "shards": shards,
        "counts": counts,
        "total_worker_seconds": sum(worker_seconds),
        "max_worker_seconds": max(worker_seconds),
        "rows": normalized,
    }
    Path(output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    assert result["complete"] and counts["orbits"] == atlas["affine_orbits"]
    print(
        "E1_PROFILE_36_MU6_M64_IMPRIMITIVE_DIRECT_RADIUS_PASS "
        f"orbits={counts['orbits']} live={counts['product_live_vectors']} "
        f"below={counts['fixed_below']} above={counts['fixed_above']} "
        f"unresolved={counts['fixed_unresolved']} output={output}"
    )


if __name__ == "__main__":
    main()
