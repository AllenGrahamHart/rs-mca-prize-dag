#!/usr/bin/env python3
"""Run the complete reverse-direct audit for the once-divided m16 branch."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time

import modal


ROOT = Path("/repo") if Path("/repo").is_dir() else Path(__file__).resolve().parents[2]
PREFIX = ROOT / "experiments/prize_resolution"
ORBIT_PATH = PREFIX / "e1_profile_36_mu4_m16_chord_orbits.json"
AUDIT_PATH = PREFIX / "e1_profile_36_mu4_m16_two_divisions_reverse_audit.cpp"
PATCH_PATH = PREFIX / "e1_profile_36_mu4_m16_reverse_even_square.patch"
PRIMARY_PATH = PREFIX / "e1_profile_36_mu4_m16_direct_radius.cpp"
BASE_PATH = PREFIX / "e1_profile_36_mu1_low_energy_exact.cpp"
ROOTS_PATH = PREFIX / "e1_profile_36_mu6_m64_fixed_roots.hpp"
PRODUCT_PATH = PREFIX / "e1_profile_36_mu4_m16_product_live.hpp"
PRIMARY_RESULT_PATH = PREFIX / "e1_profile_36_mu4_m16_one_division_direct_radius_result.json"
OUTPUT = Path(
    "experiments/prize_resolution/"
    "e1_profile_36_mu4_m16_one_division_reverse_audit_result.json"
)

PROOF_KEYS = (
    "orbits", "sign_assignments", "triple_syndromes", "radius_matches",
    "exact_sign_tests", "low_energy_vectors", "product_live_vectors",
    "fixed_below", "fixed_above", "fixed_unresolved",
)
PRIMARY_COMPARISONS = {
    "orbits": "orbits",
    "triple_syndromes": "distance_tests",
    "radius_matches": "radius_matches",
    "exact_sign_tests": "exact_sign_tests",
    "low_energy_vectors": "low_energy_vectors",
    "product_live_vectors": "product_live_vectors",
    "fixed_below": "fixed_below",
    "fixed_above": "fixed_above",
    "fixed_unresolved": "fixed_unresolved",
}
EXPECTED = {
    "orbits": 9080,
    "sign_assignments": 290560,
    "triple_syndromes": 76819415040,
    "radius_matches": 73175732492,
    "exact_sign_tests": 585405859936,
    "low_energy_vectors": 6762240640,
    "product_live_vectors": 1816625504,
    "fixed_below": 1816625308,
    "fixed_above": 196,
    "fixed_unresolved": 0,
}

app = modal.App("e1-profile-36-mu4-m16-one-division-reverse-audit")
image = (
    modal.Image.debian_slim()
    .apt_install("g++", "libboost-dev", "patch")
    .add_local_file(str(AUDIT_PATH), "/repo/experiments/prize_resolution/worker.cpp", copy=True)
    .add_local_file(str(PATCH_PATH), "/repo/experiments/prize_resolution/worker.patch", copy=True)
    .add_local_file(
        str(PRIMARY_PATH),
        "/repo/experiments/prize_resolution/e1_profile_36_mu4_m16_direct_radius.cpp",
        copy=True,
    )
    .add_local_file(
        str(BASE_PATH),
        "/repo/experiments/prize_resolution/e1_profile_36_mu1_low_energy_exact.cpp",
        copy=True,
    )
    .add_local_file(
        str(ROOTS_PATH),
        "/repo/experiments/prize_resolution/e1_profile_36_mu6_m64_fixed_roots.hpp",
        copy=True,
    )
    .add_local_file(
        str(PRODUCT_PATH),
        "/repo/experiments/prize_resolution/e1_profile_36_mu4_m16_product_live.hpp",
        copy=True,
    )
    .run_commands(
        "cd /repo/experiments/prize_resolution && patch worker.cpp worker.patch",
        "g++ -O3 -std=c++20 /repo/experiments/prize_resolution/worker.cpp -o /worker",
    )
)


def audit_orbit(orbit: list[int]) -> dict[str, object]:
    result = subprocess.run(
        ["/worker"], input=" ".join(map(str, orbit)) + "\n",
        text=True, capture_output=True, timeout=50,
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
        and counts["orbits"] == 1
        and counts["sign_assignments"] == 32
        and seconds_match is not None
    )
    return {
        "orbit": orbit,
        "returncode": result.returncode,
        "stderr": result.stderr[-4000:],
        "summary": summary,
        "valid": valid,
        "counts": counts,
        "worker_seconds": float(seconds_match.group(1)) if seconds_match else None,
    }


@app.function(image=image, cpu=4.0, memory=512, timeout=60, max_containers=100)
def audit_batch(batch_index: int, batch: list[list[int]]) -> dict[str, object]:
    started = time.monotonic()
    with ThreadPoolExecutor(max_workers=len(batch)) as executor:
        futures = [executor.submit(audit_orbit, orbit) for orbit in batch]
        subrows = [future.result() for future in futures]
    return {
        "batch": batch_index,
        "orbits": len(batch),
        "valid": all(row["valid"] for row in subrows),
        "worker_seconds": sum(float(row["worker_seconds"] or 0) for row in subrows),
        "task_wall_seconds": time.monotonic() - started,
        "subrows": subrows,
    }


def attach_primary_check(
    row: dict[str, object], primary_rows: dict[tuple[int, ...], dict[str, int]]
) -> None:
    for subrow in row["subrows"]:
        primary = primary_rows[tuple(subrow["orbit"])]
        counts = subrow["counts"]
        exact_match = (
            subrow["valid"]
            and all(counts[audit] == primary[direct] for audit, direct in PRIMARY_COMPARISONS.items())
        )
        subrow["primary_exact_match"] = exact_match
        subrow["primary_counts"] = primary
    row["valid"] = row["valid"] and all(
        subrow["primary_exact_match"] for subrow in row["subrows"]
    )


def write_packet(
    atlas: dict[str, object], expected_batches: int, rows: list[dict[str, object]]
) -> dict[str, object]:
    branch = atlas["branches"]["one_division"]
    ordered = sorted(rows, key=lambda row: int(row["batch"]))
    counts: dict[str, int] = {}
    worker_seconds: list[float] = []
    task_seconds: list[float] = []
    for row in ordered:
        if not row["valid"]:
            continue
        for subrow in row["subrows"]:
            for key, value in subrow["counts"].items():
                counts[key] = counts.get(key, 0) + int(value)
        worker_seconds.append(float(row["worker_seconds"]))
        task_seconds.append(float(row["task_wall_seconds"]))
    packet = {
        "schema": "e1-profile-36-mu4-m16-one-division-reverse-audit-result-v1",
        "complete": len(ordered) == expected_batches and all(row["valid"] for row in ordered),
        "branch": "one_division",
        "orbit_file_sha256": hashlib.sha256(ORBIT_PATH.read_bytes()).hexdigest(),
        "audit_engine_sha256": hashlib.sha256(AUDIT_PATH.read_bytes()).hexdigest(),
        "audit_patch_sha256": hashlib.sha256(PATCH_PATH.read_bytes()).hexdigest(),
        "primary_engine_sha256": hashlib.sha256(PRIMARY_PATH.read_bytes()).hexdigest(),
        "primary_result_sha256": hashlib.sha256(PRIMARY_RESULT_PATH.read_bytes()).hexdigest(),
        "fixed_roots_sha256": hashlib.sha256(ROOTS_PATH.read_bytes()).hexdigest(),
        "product_header_sha256": hashlib.sha256(PRODUCT_PATH.read_bytes()).hexdigest(),
        "affine_orbits": branch["affine_orbits"],
        "expected_batches": expected_batches,
        "completed_batches": len(ordered),
        "counts": counts,
        "total_worker_seconds": sum(worker_seconds),
        "total_task_wall_seconds": sum(task_seconds),
        "max_task_wall_seconds": max(task_seconds, default=0.0),
        "rows": ordered,
    }
    temporary = OUTPUT.with_suffix(OUTPUT.suffix + ".tmp")
    temporary.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    temporary.replace(OUTPUT)
    return packet


@app.local_entrypoint()
def main(batch_size: int = 4) -> None:
    atlas = json.loads(ORBIT_PATH.read_text())
    branch = atlas["branches"]["one_division"]
    primary = json.loads(PRIMARY_RESULT_PATH.read_text())
    assert primary["complete"]
    primary_rows = {
        tuple(subrow["orbit"]): subrow["counts"]
        for batch in primary["rows"]
        for subrow in batch["subrows"]
    }
    assert len(primary_rows) == branch["affine_orbits"] == 9080
    for audit_key, primary_key in PRIMARY_COMPARISONS.items():
        assert EXPECTED[audit_key] == primary["counts"][primary_key]

    orbits = branch["orbits"]
    batches = [orbits[start : start + batch_size] for start in range(0, len(orbits), batch_size)]
    tasks = list(enumerate(batches))
    completed: list[dict[str, object]] = []
    expected_hashes = {
        "orbit_file_sha256": hashlib.sha256(ORBIT_PATH.read_bytes()).hexdigest(),
        "audit_engine_sha256": hashlib.sha256(AUDIT_PATH.read_bytes()).hexdigest(),
        "audit_patch_sha256": hashlib.sha256(PATCH_PATH.read_bytes()).hexdigest(),
        "primary_engine_sha256": hashlib.sha256(PRIMARY_PATH.read_bytes()).hexdigest(),
        "primary_result_sha256": hashlib.sha256(PRIMARY_RESULT_PATH.read_bytes()).hexdigest(),
        "fixed_roots_sha256": hashlib.sha256(ROOTS_PATH.read_bytes()).hexdigest(),
        "product_header_sha256": hashlib.sha256(PRODUCT_PATH.read_bytes()).hexdigest(),
    }
    if OUTPUT.exists():
        previous = json.loads(OUTPUT.read_text())
        assert previous["schema"] == "e1-profile-36-mu4-m16-one-division-reverse-audit-result-v1"
        assert all(previous[key] == value for key, value in expected_hashes.items())
        assert previous["expected_batches"] == len(tasks)
        completed = list(previous["rows"])
        assert all(row["valid"] for row in completed)
    completed_indices = {int(row["batch"]) for row in completed}
    pending = [task for task in tasks if task[0] not in completed_indices]
    packet = write_packet(atlas, len(tasks), completed)
    for position, (task, returned) in enumerate(
        zip(
            pending,
            audit_batch.starmap(pending, order_outputs=True, return_exceptions=True),
            strict=True,
        ),
        start=len(completed) + 1,
    ):
        batch_index, batch = task
        row = returned if not isinstance(returned, BaseException) else {
            "batch": batch_index, "orbits": len(batch), "valid": False,
            "worker_seconds": 0.0, "task_wall_seconds": 0.0,
            "subrows": [], "error": repr(returned),
        }
        if row["subrows"]:
            attach_primary_check(row, primary_rows)
        completed.append(row)
        packet = write_packet(atlas, len(tasks), completed)
        if position % 32 == 0 or position == len(tasks) or not row["valid"]:
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
        "E1_PROFILE_36_MU4_M16_ONE_DIVISION_REVERSE_AUDIT_PASS "
        f"orbits={counts['orbits']} fixed_below={counts['fixed_below']} "
        f"fixed_above={counts['fixed_above']} output={OUTPUT}"
    )


if __name__ == "__main__":
    main()
