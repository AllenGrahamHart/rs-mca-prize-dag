#!/usr/bin/env python3
"""Run the complete reverse-direct cofactor-32 audit on Modal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


ROOT = Path("/repo") if Path("/repo").is_dir() else Path(__file__).resolve().parents[2]
PREFIX = ROOT / "experiments/prize_resolution"
ORBIT_PATH = PREFIX / "e1_profile_36_mu5_m32_chord_orbits.json"
AUDIT_PATH = PREFIX / "e1_profile_36_mu5_m32_direct_radius_reverse_audit.cpp"
PRIMARY_PATH = PREFIX / "e1_profile_36_mu5_m32_direct_radius.cpp"
BASE_PATH = PREFIX / "e1_profile_36_mu1_low_energy_exact.cpp"
ROOTS_PATH = PREFIX / "e1_profile_36_mu6_m64_fixed_roots.hpp"
PRODUCT_PATH = PREFIX / "e1_profile_36_mu5_m32_product_live.hpp"
PRIMARY_RESULT_PATH = PREFIX / "e1_profile_36_mu5_m32_direct_radius_result.json"
OUTPUT = Path(
    "experiments/prize_resolution/"
    "e1_profile_36_mu5_m32_direct_radius_reverse_audit_result.json"
)

PROOF_KEYS = (
    "orbits",
    "sign_assignments",
    "triple_syndromes",
    "radius_matches",
    "exact_sign_tests",
    "low_energy_vectors",
    "product_live_vectors",
    "fixed_below",
    "fixed_above",
    "fixed_unresolved",
)
EXPECTED = {
    "orbits": 19840,
    "sign_assignments": 634880,
    "triple_syndromes": 187441971200,
    "radius_matches": 84923111400,
    "exact_sign_tests": 679384891200,
    "low_energy_vectors": 339892636,
    "product_live_vectors": 239131808,
    "fixed_below": 239131588,
    "fixed_above": 220,
    "fixed_unresolved": 0,
}

app = modal.App("e1-profile-36-mu5-m32-radius-reverse-audit")
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


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=100)
def audit_batch(batch_index: int, batch: list[list[int]]) -> dict[str, object]:
    payload = "".join(" ".join(map(str, orbit)) + "\n" for orbit in batch)
    result = subprocess.run(
        ["/worker"], input=payload, text=True, capture_output=True, timeout=55
    )
    summary = result.stdout.strip()
    counts = {
        key: int(value)
        for key, value in re.findall(r"\b([A-Za-z_0-9]+)=([0-9]+)(?=\s|$)", summary)
    }
    seconds_match = re.search(r"\bseconds=([0-9]+(?:\.[0-9]+)?)$", summary)
    valid = (
        result.returncode == 0
        and not result.stderr
        and summary.startswith("PASS engine=reverse-direct ")
        and all(key in counts for key in PROOF_KEYS)
        and seconds_match is not None
    )
    return {
        "batch": batch_index,
        "orbits": len(batch),
        "returncode": result.returncode,
        "stderr": result.stderr[-4000:],
        "summary": summary,
        "valid": valid,
        "counts": counts,
        "worker_seconds": float(seconds_match.group(1)) if seconds_match else None,
    }


def write_packet(
    atlas: dict[str, object], expected_batches: int, rows: list[dict[str, object]]
) -> dict[str, object]:
    ordered = sorted(rows, key=lambda row: int(row["batch"]))
    counts: dict[str, int] = {}
    worker_seconds: list[float] = []
    for row in ordered:
        if row["valid"]:
            for key, value in row["counts"].items():
                counts[key] = counts.get(key, 0) + int(value)
            worker_seconds.append(float(row["worker_seconds"]))
    packet = {
        "schema": "e1-profile-36-mu5-m32-direct-radius-reverse-audit-result-v1",
        "complete": len(ordered) == expected_batches and all(row["valid"] for row in ordered),
        "orbit_file_sha256": hashlib.sha256(ORBIT_PATH.read_bytes()).hexdigest(),
        "audit_engine_sha256": hashlib.sha256(AUDIT_PATH.read_bytes()).hexdigest(),
        "primary_engine_sha256": hashlib.sha256(PRIMARY_PATH.read_bytes()).hexdigest(),
        "primary_result_sha256": hashlib.sha256(PRIMARY_RESULT_PATH.read_bytes()).hexdigest(),
        "fixed_roots_sha256": hashlib.sha256(ROOTS_PATH.read_bytes()).hexdigest(),
        "product_header_sha256": hashlib.sha256(PRODUCT_PATH.read_bytes()).hexdigest(),
        "affine_orbits": atlas["affine_orbits"],
        "expected_batches": expected_batches,
        "completed_batches": len(ordered),
        "counts": counts,
        "total_worker_seconds": sum(worker_seconds),
        "max_worker_seconds": max(worker_seconds, default=0.0),
        "rows": ordered,
    }
    temporary = OUTPUT.with_suffix(OUTPUT.suffix + ".tmp")
    temporary.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    temporary.replace(OUTPUT)
    return packet


@app.local_entrypoint()
def main(batch_size: int = 12) -> None:
    atlas = json.loads(ORBIT_PATH.read_text())
    primary = json.loads(PRIMARY_RESULT_PATH.read_text())
    assert primary["complete"]
    for audit_key, primary_key in (
        ("orbits", "orbits"),
        ("triple_syndromes", "distance_tests"),
        ("radius_matches", "radius_matches"),
        ("exact_sign_tests", "exact_sign_tests"),
        ("low_energy_vectors", "low_energy_vectors"),
        ("product_live_vectors", "product_live_vectors"),
        ("fixed_below", "fixed_below"),
        ("fixed_above", "fixed_above"),
        ("fixed_unresolved", "fixed_unresolved"),
    ):
        assert EXPECTED[audit_key] == primary["counts"][primary_key]

    orbits = atlas["orbits"]
    batches = [orbits[start : start + batch_size] for start in range(0, len(orbits), batch_size)]
    tasks = list(enumerate(batches))
    completed: list[dict[str, object]] = []
    packet = write_packet(atlas, len(tasks), completed)
    for position, (task, returned) in enumerate(
        zip(
            tasks,
            audit_batch.starmap(tasks, order_outputs=True, return_exceptions=True),
            strict=True,
        ),
        start=1,
    ):
        batch_index, batch = task
        row = returned if not isinstance(returned, BaseException) else {
            "batch": batch_index,
            "orbits": len(batch),
            "returncode": None,
            "stderr": repr(returned),
            "summary": "",
            "valid": False,
            "counts": {},
            "worker_seconds": None,
        }
        completed.append(row)
        packet = write_packet(atlas, len(tasks), completed)
        if position % 16 == 0 or position == len(tasks) or not row["valid"]:
            print(
                f"progress={position}/{len(tasks)} batch={batch_index} "
                f"valid={row['valid']} fixed_above={packet['counts'].get('fixed_above', 0)}"
            )

    counts = packet["counts"]
    assert packet["complete"]
    for key, expected in EXPECTED.items():
        assert counts.get(key) == expected, (key, counts.get(key), expected)
    assert sum(value for key, value in counts.items() if key.startswith("live_E")) == EXPECTED["product_live_vectors"]
    assert sum(value for key, value in counts.items() if key.startswith("above_E")) == EXPECTED["fixed_above"]
    print(
        "E1_PROFILE_36_MU5_M32_RADIUS_REVERSE_AUDIT_PASS "
        f"orbits={counts['orbits']} fixed_below={counts['fixed_below']} "
        f"fixed_above={counts['fixed_above']} output={OUTPUT}"
    )


if __name__ == "__main__":
    main()
