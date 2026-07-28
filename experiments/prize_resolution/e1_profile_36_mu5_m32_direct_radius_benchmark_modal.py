#!/usr/bin/env python3
"""Benchmark one multiplicity-five orbit per parity weight on Modal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


ROOT = Path("/repo") if Path("/repo").is_dir() else Path(__file__).resolve().parents[2]
ORBIT_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu5_m32_chord_orbits.json"
CPP_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu5_m32_direct_radius.cpp"
BASE_CPP_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu1_low_energy_exact.cpp"
FIXED_ROOTS_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu6_m64_fixed_roots.hpp"
PRODUCT_HEADER_PATH = ROOT / "experiments/prize_resolution/e1_profile_36_mu5_m32_product_live.hpp"
OUTPUT = Path(
    "experiments/prize_resolution/e1_profile_36_mu5_m32_direct_radius_benchmark_result.json"
)

app = modal.App("e1-profile-36-mu5-m32-radius-benchmark")
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
    .add_local_file(
        str(PRODUCT_HEADER_PATH),
        "/repo/experiments/prize_resolution/e1_profile_36_mu5_m32_product_live.hpp",
        copy=True,
    )
    .run_commands(
        "g++ -O3 -std=c++20 /repo/experiments/prize_resolution/worker.cpp -o /worker"
    )
)


def odd_chord_weight(support: list[int]) -> int:
    mask = 0
    for index, left in enumerate(support):
        for right in support[index + 1 :]:
            delta = right - left
            if delta == 64:
                continue
            lag = delta if delta < 64 else 128 - delta
            mask ^= 1 << (lag - 1)
    return mask.bit_count()


@app.function(image=image, cpu=1.0, memory=256, timeout=90, max_containers=13)
def benchmark(item: tuple[int, list[int]]) -> dict[str, object]:
    odd_weight, orbit = item
    result = subprocess.run(
        ["/worker"], input=" ".join(map(str, orbit)) + "\n",
        text=True, capture_output=True, timeout=80,
    )
    return {
        "odd_weight": odd_weight,
        "orbit": orbit,
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr[-4000:],
    }


@app.local_entrypoint()
def main() -> None:
    atlas = json.loads(ORBIT_PATH.read_text())
    representatives: dict[int, list[int]] = {}
    for orbit in atlas["orbits"]:
        representatives.setdefault(odd_chord_weight(orbit), orbit)
    tasks = sorted(representatives.items())
    rows = list(benchmark.map(tasks, order_outputs=True, return_exceptions=True))
    normalized = []
    for task, row in zip(tasks, rows, strict=True):
        if isinstance(row, BaseException):
            normalized.append({
                "odd_weight": task[0], "orbit": task[1], "returncode": None,
                "stdout": "", "stderr": repr(row),
            })
        else:
            normalized.append(row)
        print(f"q={task[0]} {str(normalized[-1]['stdout']).strip() or normalized[-1]['stderr']}")
    result = {
        "schema": "e1-profile-36-mu5-m32-direct-radius-benchmark-v1",
        "complete": all(
            row["returncode"] == 0 and not row["stderr"] for row in normalized
        ),
        "orbit_file_sha256": hashlib.sha256(ORBIT_PATH.read_bytes()).hexdigest(),
        "engine_sha256": hashlib.sha256(CPP_PATH.read_bytes()).hexdigest(),
        "representatives": len(tasks),
        "rows": normalized,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    assert result["complete"] and len(tasks) == 13
    seconds = [
        float(re.search(r"\bseconds=([0-9.]+)$", row["stdout"].strip()).group(1))
        for row in normalized
    ]
    print(
        "E1_PROFILE_36_MU5_M32_RADIUS_BENCHMARK_PASS "
        f"orbits={len(tasks)} total_seconds={sum(seconds):.6f} "
        f"max_seconds={max(seconds):.6f} output={OUTPUT}"
    )


if __name__ == "__main__":
    main()
