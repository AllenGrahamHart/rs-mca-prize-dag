#!/usr/bin/env python3
"""Benchmark the fast-energy primitive m16 exact engine."""

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
NO_DIAGNOSTIC_PATH = PREFIX / "e1_profile_36_mu4_m16_no_diagnostic_transform.py"
FAST_PATH = PREFIX / "e1_profile_36_mu4_m16_primitive_fast_energy_transform.py"
TWIST_PATH = PREFIX / "e1_profile_36_mu4_m16_primitive_twist_transform.py"
CAP_PATH = PREFIX / "e1_profile_36_mu4_m16_primitive_coarse_cap_transform.py"
BASE_PATH = PREFIX / "e1_profile_36_mu1_low_energy_exact.cpp"
ROOTS_PATH = PREFIX / "e1_profile_36_mu6_m64_fixed_roots.hpp"
PRODUCT_PATH = PREFIX / "e1_profile_36_mu4_m16_product_live.hpp"
BASELINE_PATH = PREFIX / "e1_profile_36_mu4_m16_direct_radius_benchmark_result.json"
OUTPUT = Path(
    "experiments/prize_resolution/"
    "e1_profile_36_mu4_m16_primitive_fast_twist_coarse_benchmark_result.json"
)

COUNT_KEYS = (
    "orbits", "triple_syndromes", "distance_tests", "radius_matches",
    "exact_sign_tests", "low_energy_vectors", "product_live_vectors",
    "fixed_below", "fixed_above", "fixed_unresolved",
)

app = modal.App("e1-profile-36-mu4-m16-primitive-fast-twist-coarse-benchmark")
image = (
    modal.Image.debian_slim()
    .apt_install("g++", "libboost-dev")
    .add_local_file(str(CPP_PATH), "/repo/experiments/prize_resolution/worker.cpp", copy=True)
    .add_local_file(str(NO_DIAGNOSTIC_PATH), "/repo/no_diagnostic.py", copy=True)
    .add_local_file(str(FAST_PATH), "/repo/fast.py", copy=True)
    .add_local_file(str(TWIST_PATH), "/repo/twist.py", copy=True)
    .add_local_file(str(CAP_PATH), "/repo/cap.py", copy=True)
    .add_local_file(str(BASE_PATH), "/repo/experiments/prize_resolution/e1_profile_36_mu1_low_energy_exact.cpp", copy=True)
    .add_local_file(str(ROOTS_PATH), "/repo/experiments/prize_resolution/e1_profile_36_mu6_m64_fixed_roots.hpp", copy=True)
    .add_local_file(str(PRODUCT_PATH), "/repo/experiments/prize_resolution/e1_profile_36_mu4_m16_product_live.hpp", copy=True)
    .run_commands(
        "python3 /repo/no_diagnostic.py /repo/experiments/prize_resolution/worker.cpp",
        "python3 /repo/fast.py /repo/experiments/prize_resolution/worker.cpp",
        "python3 /repo/twist.py /repo/experiments/prize_resolution/worker.cpp",
        "python3 /repo/cap.py /repo/experiments/prize_resolution/worker.cpp",
        "g++ -O3 -std=c++20 /repo/experiments/prize_resolution/worker.cpp -o /worker",
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


def parse_counts(summary: str) -> dict[str, int]:
    return {
        key: int(value)
        for key, value in re.findall(r"\b([a-z_]+)=([0-9]+)(?=\s|$)", summary)
    }


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=13)
def benchmark(item: tuple[int, list[int]]) -> dict[str, object]:
    q, orbit = item
    result = subprocess.run(
        ["/worker"], input=" ".join(map(str, orbit)) + "\n",
        text=True, capture_output=True, timeout=55,
    )
    return {
        "branch": "primitive", "odd_weight": q, "orbit": orbit,
        "returncode": result.returncode, "stdout": result.stdout,
        "stderr": result.stderr[-4000:],
    }


@app.local_entrypoint()
def main() -> None:
    atlas = json.loads(ORBIT_PATH.read_text())
    baseline_packet = json.loads(BASELINE_PATH.read_text())
    baseline = {
        (row["branch"], row["odd_weight"]): parse_counts(row["stdout"])
        for row in baseline_packet["rows"]
    }
    representatives: dict[int, list[int]] = {}
    for orbit in atlas["branches"]["primitive"]["orbits"]:
        representatives.setdefault(odd_chord_weight(orbit), orbit)
    tasks = sorted(representatives.items())
    returned = list(benchmark.map(tasks, order_outputs=True, return_exceptions=True))

    rows = []
    for task, value in zip(tasks, returned, strict=True):
        row = value if not isinstance(value, BaseException) else {
            "branch": "primitive", "odd_weight": task[0], "orbit": task[1],
            "returncode": None, "stdout": "", "stderr": repr(value),
        }
        counts = parse_counts(str(row["stdout"]))
        expected = baseline[("primitive", task[0])]
        exact_match = (
            row["returncode"] == 0
            and not row["stderr"]
            and all(key in counts for key in COUNT_KEYS)
            and counts["orbits"] == expected["orbits"]
            and counts["triple_syndromes"] == expected["triple_syndromes"]
            and all(
                2 * counts[key] == expected[key]
                for key in COUNT_KEYS
                if key not in {"orbits", "triple_syndromes"}
            )
            and counts.get("screen_below") == counts.get("screen_above")
            == counts.get("screen_near") == 0
        )
        row["counts"] = counts
        row["baseline_counts"] = expected
        row["exact_match"] = exact_match
        rows.append(row)
        print(
            f"q={task[0]} exact_match={exact_match} "
            f"{str(row['stdout']).strip() or row['stderr']}"
        )

    seconds = [
        float(re.search(r"\bseconds=([0-9.]+)$", row["stdout"].strip()).group(1))
        for row in rows
    ]
    result = {
        "schema": "e1-profile-36-mu4-m16-primitive-fast-twist-coarse-benchmark-v1",
        "complete": all(row["exact_match"] for row in rows),
        "representatives": len(tasks),
        "total_seconds": sum(seconds),
        "max_seconds": max(seconds),
        "rows": rows,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    assert result["complete"] and len(tasks) == 13
    print(
        "E1_PROFILE_36_MU4_M16_PRIMITIVE_FAST_TWIST_COARSE_BENCHMARK_PASS "
        f"orbits={len(tasks)} total_seconds={sum(seconds):.6f} "
        f"max_seconds={max(seconds):.6f} output={OUTPUT}"
    )


if __name__ == "__main__":
    main()
