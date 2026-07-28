#!/usr/bin/env python3
"""Benchmark one cofactor-16 orbit per branch and parity weight on Modal."""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess

import modal


ROOT = Path("/repo") if Path("/repo").is_dir() else Path(__file__).resolve().parents[2]
PREFIX = ROOT / "experiments/prize_resolution"
ORBIT_PATH = PREFIX / "e1_profile_36_mu4_m16_chord_orbits.json"
CPP_PATH = PREFIX / "e1_profile_36_mu4_m16_direct_radius.cpp"
BASE_PATH = PREFIX / "e1_profile_36_mu1_low_energy_exact.cpp"
ROOTS_PATH = PREFIX / "e1_profile_36_mu6_m64_fixed_roots.hpp"
PRODUCT_PATH = PREFIX / "e1_profile_36_mu4_m16_product_live.hpp"
OUTPUT = Path(
    "experiments/prize_resolution/e1_profile_36_mu4_m16_direct_radius_benchmark_result.json"
)

app = modal.App("e1-profile-36-mu4-m16-radius-benchmark")
image = (
    modal.Image.debian_slim()
    .apt_install("g++", "libboost-dev")
    .add_local_file(str(CPP_PATH), "/repo/experiments/prize_resolution/worker.cpp", copy=True)
    .add_local_file(str(BASE_PATH), "/repo/experiments/prize_resolution/e1_profile_36_mu1_low_energy_exact.cpp", copy=True)
    .add_local_file(str(ROOTS_PATH), "/repo/experiments/prize_resolution/e1_profile_36_mu6_m64_fixed_roots.hpp", copy=True)
    .add_local_file(str(PRODUCT_PATH), "/repo/experiments/prize_resolution/e1_profile_36_mu4_m16_product_live.hpp", copy=True)
    .run_commands("g++ -O3 -std=c++20 /repo/experiments/prize_resolution/worker.cpp -o /worker")
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


@app.function(image=image, cpu=1.0, memory=256, timeout=90, max_containers=45)
def benchmark(item: tuple[str, int, list[int]]) -> dict[str, object]:
    branch, q, orbit = item
    result = subprocess.run(
        ["/worker"], input=" ".join(map(str, orbit)) + "\n",
        text=True, capture_output=True, timeout=80,
    )
    return {
        "branch": branch, "odd_weight": q, "orbit": orbit,
        "returncode": result.returncode, "stdout": result.stdout,
        "stderr": result.stderr[-4000:],
    }


@app.local_entrypoint()
def main() -> None:
    atlas = json.loads(ORBIT_PATH.read_text())
    representatives: dict[tuple[str, int], list[int]] = {}
    for branch, packet in atlas["branches"].items():
        for orbit in packet["orbits"]:
            representatives.setdefault((branch, odd_chord_weight(orbit)), orbit)
    tasks = [
        (branch, q, orbit)
        for (branch, q), orbit in sorted(representatives.items())
    ]
    returned = list(benchmark.map(tasks, order_outputs=True, return_exceptions=True))
    rows = []
    for task, value in zip(tasks, returned, strict=True):
        row = value if not isinstance(value, BaseException) else {
            "branch": task[0], "odd_weight": task[1], "orbit": task[2],
            "returncode": None, "stdout": "", "stderr": repr(value),
        }
        rows.append(row)
        print(f"branch={task[0]} q={task[1]} {str(row['stdout']).strip() or row['stderr']}")
    result = {
        "schema": "e1-profile-36-mu4-m16-direct-radius-benchmark-v1",
        "complete": all(row["returncode"] == 0 and not row["stderr"] for row in rows),
        "representatives": len(tasks),
        "rows": rows,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    assert result["complete"]
    seconds = [
        float(re.search(r"\bseconds=([0-9.]+)$", row["stdout"].strip()).group(1))
        for row in rows
    ]
    print(
        "E1_PROFILE_36_MU4_M16_RADIUS_BENCHMARK_PASS "
        f"orbits={len(tasks)} total_seconds={sum(seconds):.6f} "
        f"max_seconds={max(seconds):.6f} output={OUTPUT}"
    )


if __name__ == "__main__":
    main()
