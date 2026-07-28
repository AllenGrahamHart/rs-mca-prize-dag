#!/usr/bin/env python3
"""Benchmark the independent fast reverse audit for primitive m16."""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess

import modal


ROOT = Path("/repo") if Path("/repo").is_dir() else Path(__file__).resolve().parents[2]
PREFIX = ROOT / "experiments/prize_resolution"
ORBIT_PATH = PREFIX / "e1_profile_36_mu4_m16_chord_orbits.json"
AUDIT_PATH = PREFIX / "e1_profile_36_mu4_m16_two_divisions_reverse_audit.cpp"
TWIST_PATH = PREFIX / "e1_profile_36_mu4_m16_primitive_reverse_twist_transform.py"
FAST_PATH = PREFIX / "e1_profile_36_mu4_m16_primitive_reverse_fast_energy_transform.py"
PRIMARY_CPP_PATH = PREFIX / "e1_profile_36_mu4_m16_direct_radius.cpp"
BASE_PATH = PREFIX / "e1_profile_36_mu1_low_energy_exact.cpp"
ROOTS_PATH = PREFIX / "e1_profile_36_mu6_m64_fixed_roots.hpp"
PRODUCT_PATH = PREFIX / "e1_profile_36_mu4_m16_product_live.hpp"
PRIMARY_RESULT_PATH = PREFIX / "e1_profile_36_mu4_m16_primitive_fast_direct_radius_result.json"
OUTPUT = Path(
    "experiments/prize_resolution/"
    "e1_profile_36_mu4_m16_primitive_reverse_fast_benchmark_result.json"
)

app = modal.App("e1-profile-36-mu4-m16-primitive-reverse-fast-benchmark")
image = (
    modal.Image.debian_slim()
    .apt_install("g++", "libboost-dev")
    .add_local_file(str(AUDIT_PATH), "/repo/experiments/prize_resolution/worker.cpp", copy=True)
    .add_local_file(str(TWIST_PATH), "/repo/twist.py", copy=True)
    .add_local_file(str(FAST_PATH), "/repo/fast.py", copy=True)
    .add_local_file(str(PRIMARY_CPP_PATH), "/repo/experiments/prize_resolution/e1_profile_36_mu4_m16_direct_radius.cpp", copy=True)
    .add_local_file(str(BASE_PATH), "/repo/experiments/prize_resolution/e1_profile_36_mu1_low_energy_exact.cpp", copy=True)
    .add_local_file(str(ROOTS_PATH), "/repo/experiments/prize_resolution/e1_profile_36_mu6_m64_fixed_roots.hpp", copy=True)
    .add_local_file(str(PRODUCT_PATH), "/repo/experiments/prize_resolution/e1_profile_36_mu4_m16_product_live.hpp", copy=True)
    .run_commands(
        "python3 /repo/twist.py /repo/experiments/prize_resolution/worker.cpp",
        "python3 /repo/fast.py /repo/experiments/prize_resolution/worker.cpp",
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


def parse_summary(summary: str) -> dict[str, int | float | str]:
    parsed: dict[str, int | float | str] = {}
    for token in summary.strip().split():
        if "=" not in token:
            continue
        key, value = token.split("=", 1)
        if key == "seconds":
            parsed[key] = float(value)
        elif value.isdigit():
            parsed[key] = int(value)
        else:
            parsed[key] = value
    return parsed


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
    primary_result = json.loads(PRIMARY_RESULT_PATH.read_text())
    primary_rows = {
        tuple(subrow["orbit"]): subrow["counts"]
        for batch in primary_result["rows"] for subrow in batch["subrows"]
    }
    representatives: dict[int, list[int]] = {}
    for orbit in atlas["branches"]["primitive"]["orbits"]:
        representatives.setdefault(odd_chord_weight(orbit), orbit)
    tasks = sorted(representatives.items())
    returned = list(benchmark.map(tasks, order_outputs=True, return_exceptions=True))
    comparisons = {
        "triple_syndromes": "distance_tests", "radius_matches": "radius_matches",
        "exact_sign_tests": "exact_sign_tests", "low_energy_vectors": "low_energy_vectors",
        "product_live_vectors": "product_live_vectors", "fixed_below": "fixed_below",
        "fixed_above": "fixed_above", "fixed_unresolved": "fixed_unresolved",
    }
    rows = []
    for task, value in zip(tasks, returned, strict=True):
        row = value if not isinstance(value, BaseException) else {
            "branch": "primitive", "odd_weight": task[0], "orbit": task[1],
            "returncode": None, "stdout": "", "stderr": repr(value),
        }
        parsed = parse_summary(str(row["stdout"]))
        primary = primary_rows[tuple(task[1])]
        exact_match = (
            row["returncode"] == 0 and not row["stderr"]
            and parsed.get("engine") == "reverse-direct"
            and parsed.get("orbits") == 1 and parsed.get("sign_assignments") == 16
            and all(parsed.get(audit) == primary[direct] for audit, direct in comparisons.items())
        )
        row["parsed"] = parsed
        row["primary_counts"] = primary
        row["exact_match"] = exact_match
        rows.append(row)
        print(f"q={task[0]} exact_match={exact_match} {str(row['stdout']).strip() or row['stderr']}")
    seconds = [float(row["parsed"]["seconds"]) for row in rows]
    result = {
        "schema": "e1-profile-36-mu4-m16-primitive-reverse-fast-benchmark-v1",
        "complete": all(row["exact_match"] for row in rows),
        "representatives": len(tasks), "total_seconds": sum(seconds),
        "max_seconds": max(seconds), "rows": rows,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    assert result["complete"] and len(tasks) == 13
    print(
        "E1_PROFILE_36_MU4_M16_PRIMITIVE_REVERSE_FAST_BENCHMARK_PASS "
        f"orbits={len(tasks)} total_seconds={sum(seconds):.6f} "
        f"max_seconds={max(seconds):.6f} output={OUTPUT}"
    )


if __name__ == "__main__":
    main()
