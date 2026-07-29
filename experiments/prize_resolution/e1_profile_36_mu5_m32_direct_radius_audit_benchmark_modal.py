#!/usr/bin/env python3
"""Benchmark the independent cofactor-32 reverse hash-block audit on Modal."""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess

import modal


ROOT = Path("/repo") if Path("/repo").is_dir() else Path(__file__).resolve().parents[2]
PREFIX = ROOT / "experiments/prize_resolution"
ORBIT_PATH = PREFIX / "e1_profile_36_mu5_m32_chord_orbits.json"
AUDIT_PATH = PREFIX / "e1_profile_36_mu5_m32_direct_radius_audit.cpp"
PRIMARY_PATH = PREFIX / "e1_profile_36_mu5_m32_direct_radius.cpp"
BASE_PATH = PREFIX / "e1_profile_36_mu1_low_energy_exact.cpp"
ROOTS_PATH = PREFIX / "e1_profile_36_mu6_m64_fixed_roots.hpp"
PRODUCT_PATH = PREFIX / "e1_profile_36_mu5_m32_product_live.hpp"
PRIMARY_BENCHMARK_PATH = PREFIX / "e1_profile_36_mu5_m32_direct_radius_benchmark_result.json"
OUTPUT = Path(
    "experiments/prize_resolution/"
    "e1_profile_36_mu5_m32_direct_radius_audit_benchmark_result.json"
)

app = modal.App("e1-profile-36-mu5-m32-radius-audit-benchmark")
image = (
    modal.Image.debian_slim()
    .apt_install("g++", "libboost-dev")
    .add_local_file(str(AUDIT_PATH), "/repo/experiments/prize_resolution/worker.cpp", copy=True)
    .add_local_file(str(PRIMARY_PATH), "/repo/experiments/prize_resolution/e1_profile_36_mu5_m32_direct_radius.cpp", copy=True)
    .add_local_file(str(BASE_PATH), "/repo/experiments/prize_resolution/e1_profile_36_mu1_low_energy_exact.cpp", copy=True)
    .add_local_file(str(ROOTS_PATH), "/repo/experiments/prize_resolution/e1_profile_36_mu6_m64_fixed_roots.hpp", copy=True)
    .add_local_file(str(PRODUCT_PATH), "/repo/experiments/prize_resolution/e1_profile_36_mu5_m32_product_live.hpp", copy=True)
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


@app.function(image=image, cpu=1.0, memory=768, timeout=90, max_containers=13)
def benchmark(item: tuple[int, list[int]]) -> dict[str, object]:
    q, orbit = item
    result = subprocess.run(
        ["/worker"], input=" ".join(map(str, orbit)) + "\n",
        text=True, capture_output=True, timeout=80,
    )
    return {
        "odd_weight": q,
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
    primary_rows = {
        int(row["odd_weight"]): row
        for row in json.loads(PRIMARY_BENCHMARK_PATH.read_text())["rows"]
    }
    normalized = []
    for task, returned in zip(tasks, rows, strict=True):
        if isinstance(returned, BaseException):
            row = {
                "odd_weight": task[0], "orbit": task[1], "returncode": None,
                "stdout": "", "stderr": repr(returned),
            }
        else:
            row = returned
        normalized.append(row)
        print(f"q={task[0]} {str(row['stdout']).strip() or row['stderr']}")
        audit_counts = dict(re.findall(r"\b([a-z_]+)=([0-9]+)(?=\s|$)", str(row["stdout"])))
        primary_counts = dict(re.findall(
            r"\b([a-z_]+)=([0-9]+)(?=\s|$)", primary_rows[task[0]]["stdout"]
        ))
        for audit_key, primary_key in (
            ("unique_triples", "radius_matches"),
            ("exact_sign_tests", "exact_sign_tests"),
            ("low_energy_vectors", "low_energy_vectors"),
            ("product_live_vectors", "product_live_vectors"),
            ("fixed_below", "fixed_below"),
            ("fixed_above", "fixed_above"),
            ("fixed_unresolved", "fixed_unresolved"),
        ):
            assert audit_counts[audit_key] == primary_counts[primary_key], (
                task[0], audit_key, audit_counts[audit_key], primary_counts[primary_key]
            )
    result = {
        "schema": "e1-profile-36-mu5-m32-direct-radius-audit-benchmark-v1",
        "complete": all(row["returncode"] == 0 and not row["stderr"] for row in normalized),
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
        "E1_PROFILE_36_MU5_M32_RADIUS_AUDIT_BENCHMARK_PASS "
        f"orbits={len(tasks)} total_seconds={sum(seconds):.6f} "
        f"max_seconds={max(seconds):.6f} output={OUTPUT}"
    )


if __name__ == "__main__":
    main()
