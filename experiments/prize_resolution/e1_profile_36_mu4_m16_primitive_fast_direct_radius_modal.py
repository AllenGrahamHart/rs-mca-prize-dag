#!/usr/bin/env python3
"""Run the complete fast primitive cofactor-16 primary census on Modal."""

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
CPP_PATH = PREFIX / "e1_profile_36_mu4_m16_direct_radius.cpp"
NO_DIAGNOSTIC_PATH = PREFIX / "e1_profile_36_mu4_m16_no_diagnostic_transform.py"
FAST_PATH = PREFIX / "e1_profile_36_mu4_m16_primitive_fast_energy_transform.py"
TWIST_PATH = PREFIX / "e1_profile_36_mu4_m16_primitive_twist_transform.py"
CAP_PATH = PREFIX / "e1_profile_36_mu4_m16_primitive_coarse_cap_transform.py"
BASE_PATH = PREFIX / "e1_profile_36_mu1_low_energy_exact.cpp"
ROOTS_PATH = PREFIX / "e1_profile_36_mu6_m64_fixed_roots.hpp"
PRODUCT_PATH = PREFIX / "e1_profile_36_mu4_m16_product_live.hpp"
OUTPUT = Path(
    "experiments/prize_resolution/"
    "e1_profile_36_mu4_m16_primitive_fast_direct_radius_result.json"
)

COUNT_KEYS = (
    "orbits", "triple_syndromes", "distance_tests", "radius_matches",
    "exact_sign_tests", "low_energy_vectors", "product_live_vectors",
    "screen_below", "screen_above", "screen_near", "fixed_below",
    "fixed_above", "fixed_unresolved",
)

app = modal.App("e1-profile-36-mu4-m16-primitive-fast-direct-radius")
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


def parse_worker(orbit: list[int]) -> dict[str, object]:
    result = subprocess.run(
        ["/worker", "verbose"], input=" ".join(map(str, orbit)) + "\n",
        text=True, capture_output=True, timeout=45,
    )
    lines = result.stdout.splitlines()
    summary = lines[-1] if lines else ""
    parsed = {
        key: int(value)
        for key, value in re.findall(r"\b([a-z_]+)=([0-9]+)(?=\s|$)", summary)
    }
    seconds_match = re.search(r"\bseconds=([0-9]+(?:\.[0-9]+)?)$", summary)
    valid = (
        result.returncode == 0 and not result.stderr
        and summary.startswith("PASS ")
        and all(key in parsed for key in COUNT_KEYS)
        and seconds_match is not None
    )
    return {
        "orbit": orbit, "returncode": result.returncode,
        "stderr": result.stderr[-4000:], "summary": summary, "valid": valid,
        "counts": {key: parsed.get(key, 0) for key in COUNT_KEYS},
        "worker_seconds": float(seconds_match.group(1)) if seconds_match else None,
        "witnesses": [line for line in lines[:-1] if line.startswith("WITNESS ")],
    }


@app.function(image=image, cpu=4.0, memory=512, timeout=60, max_containers=100)
def classify_batch(batch_index: int, batch: list[list[int]]) -> dict[str, object]:
    started = time.monotonic()
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(parse_worker, orbit) for orbit in batch]
        subrows = [future.result() for future in futures]
    counts = {key: 0 for key in COUNT_KEYS}
    witnesses: list[str] = []
    worker_seconds = 0.0
    for row in subrows:
        if row["valid"]:
            for key in COUNT_KEYS:
                counts[key] += int(row["counts"][key])
            witnesses.extend(str(value) for value in row["witnesses"])
            worker_seconds += float(row["worker_seconds"])
    return {
        "batch": batch_index, "orbits": len(batch),
        "valid": all(row["valid"] for row in subrows), "counts": counts,
        "worker_seconds": worker_seconds,
        "task_wall_seconds": time.monotonic() - started,
        "witnesses": witnesses, "subrows": subrows,
    }


def write_packet(
    atlas: dict[str, object], expected_batches: int, rows: list[dict[str, object]]
) -> dict[str, object]:
    branch = atlas["branches"]["primitive"]
    ordered = sorted(rows, key=lambda row: int(row["batch"]))
    counts = {key: 0 for key in COUNT_KEYS}
    witnesses: list[str] = []
    worker_seconds: list[float] = []
    task_seconds: list[float] = []
    for row in ordered:
        if row["valid"]:
            for key in COUNT_KEYS:
                counts[key] += int(row["counts"][key])
            witnesses.extend(str(value) for value in row["witnesses"])
            worker_seconds.append(float(row["worker_seconds"]))
            task_seconds.append(float(row["task_wall_seconds"]))
    packet = {
        "schema": "e1-profile-36-mu4-m16-primitive-fast-direct-radius-result-v1",
        "complete": len(ordered) == expected_batches and all(row["valid"] for row in ordered),
        "branch": "primitive",
        "orbit_file_sha256": hashlib.sha256(ORBIT_PATH.read_bytes()).hexdigest(),
        "base_engine_sha256": hashlib.sha256(CPP_PATH.read_bytes()).hexdigest(),
        "no_diagnostic_sha256": hashlib.sha256(NO_DIAGNOSTIC_PATH.read_bytes()).hexdigest(),
        "fast_transform_sha256": hashlib.sha256(FAST_PATH.read_bytes()).hexdigest(),
        "twist_transform_sha256": hashlib.sha256(TWIST_PATH.read_bytes()).hexdigest(),
        "cap_transform_sha256": hashlib.sha256(CAP_PATH.read_bytes()).hexdigest(),
        "fixed_roots_sha256": hashlib.sha256(ROOTS_PATH.read_bytes()).hexdigest(),
        "product_header_sha256": hashlib.sha256(PRODUCT_PATH.read_bytes()).hexdigest(),
        "affine_orbits": branch["affine_orbits"],
        "expected_batches": expected_batches, "completed_batches": len(ordered),
        "counts": counts, "total_worker_seconds": sum(worker_seconds),
        "total_task_wall_seconds": sum(task_seconds),
        "max_task_wall_seconds": max(task_seconds, default=0.0),
        "witnesses": witnesses, "rows": ordered,
    }
    temporary = OUTPUT.with_suffix(OUTPUT.suffix + ".tmp")
    temporary.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    temporary.replace(OUTPUT)
    return packet


@app.local_entrypoint()
def main(batch_size: int = 32, checkpoint_every: int = 16) -> None:
    atlas = json.loads(ORBIT_PATH.read_text())
    branch = atlas["branches"]["primitive"]
    orbits = branch["orbits"]
    batches = [orbits[start : start + batch_size] for start in range(0, len(orbits), batch_size)]
    tasks = list(enumerate(batches))
    completed: list[dict[str, object]] = []
    expected_hashes = {
        "orbit_file_sha256": hashlib.sha256(ORBIT_PATH.read_bytes()).hexdigest(),
        "base_engine_sha256": hashlib.sha256(CPP_PATH.read_bytes()).hexdigest(),
        "no_diagnostic_sha256": hashlib.sha256(NO_DIAGNOSTIC_PATH.read_bytes()).hexdigest(),
        "fast_transform_sha256": hashlib.sha256(FAST_PATH.read_bytes()).hexdigest(),
        "twist_transform_sha256": hashlib.sha256(TWIST_PATH.read_bytes()).hexdigest(),
        "cap_transform_sha256": hashlib.sha256(CAP_PATH.read_bytes()).hexdigest(),
        "fixed_roots_sha256": hashlib.sha256(ROOTS_PATH.read_bytes()).hexdigest(),
        "product_header_sha256": hashlib.sha256(PRODUCT_PATH.read_bytes()).hexdigest(),
    }
    if OUTPUT.exists():
        previous = json.loads(OUTPUT.read_text())
        assert previous["schema"] == "e1-profile-36-mu4-m16-primitive-fast-direct-radius-result-v1"
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
            classify_batch.starmap(pending, order_outputs=True, return_exceptions=True),
            strict=True,
        ),
        start=len(completed) + 1,
    ):
        batch_index, batch = task
        row = returned if not isinstance(returned, BaseException) else {
            "batch": batch_index, "orbits": len(batch), "valid": False,
            "counts": {key: 0 for key in COUNT_KEYS}, "worker_seconds": 0.0,
            "task_wall_seconds": 0.0, "witnesses": [], "subrows": [],
            "error": repr(returned),
        }
        completed.append(row)
        should_checkpoint = (
            position % checkpoint_every == 0
            or position == len(tasks) or not row["valid"]
        )
        if should_checkpoint:
            packet = write_packet(atlas, len(tasks), completed)
            print(
                f"progress={position}/{len(tasks)} batch={batch_index} "
                f"valid={row['valid']} fixed_above={packet['counts']['fixed_above']}"
            )

    packet = write_packet(atlas, len(tasks), completed)
    counts = packet["counts"]
    assert packet["complete"]
    assert counts["orbits"] == branch["affine_orbits"] == 39936
    assert counts["triple_syndromes"] == counts["orbits"] * 295240
    assert counts["distance_tests"] == counts["orbits"] * 16 * 295240
    assert counts["exact_sign_tests"] == 8 * counts["radius_matches"]
    assert counts["product_live_vectors"] == (
        counts["fixed_below"] + counts["fixed_above"] + counts["fixed_unresolved"]
    )
    assert counts["screen_below"] == counts["screen_above"] == counts["screen_near"] == 0
    assert counts["fixed_unresolved"] == 0
    assert len(packet["witnesses"]) == counts["fixed_above"]
    print(
        "E1_PROFILE_36_MU4_M16_PRIMITIVE_FAST_DIRECT_RADIUS_PASS "
        f"orbits={counts['orbits']} fixed_below={counts['fixed_below']} "
        f"fixed_above={counts['fixed_above']} output={OUTPUT}"
    )


if __name__ == "__main__":
    main()
