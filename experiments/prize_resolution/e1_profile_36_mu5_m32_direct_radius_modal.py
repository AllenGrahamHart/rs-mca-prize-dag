#!/usr/bin/env python3
"""Run the complete multiplicity-five, cofactor-32 direct census on Modal."""

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
    "experiments/prize_resolution/e1_profile_36_mu5_m32_direct_radius_result.json"
)

COUNT_KEYS = (
    "orbits",
    "triple_syndromes",
    "distance_tests",
    "radius_matches",
    "exact_sign_tests",
    "low_energy_vectors",
    "product_live_vectors",
    "screen_below",
    "screen_above",
    "screen_near",
    "fixed_below",
    "fixed_above",
    "fixed_unresolved",
)

app = modal.App("e1-profile-36-mu5-m32-direct-radius")
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


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=100)
def classify_batch(batch_index: int, batch: list[list[int]]) -> dict[str, object]:
    payload = "".join(" ".join(map(str, orbit)) + "\n" for orbit in batch)
    result = subprocess.run(
        ["/worker", "verbose"],
        input=payload,
        text=True,
        capture_output=True,
        timeout=55,
    )
    lines = result.stdout.splitlines()
    summary = lines[-1] if lines else ""
    parsed = {
        key: int(value)
        for key, value in re.findall(r"\b([a-z_]+)=([0-9]+)(?=\s|$)", summary)
    }
    seconds_match = re.search(r"\bseconds=([0-9]+(?:\.[0-9]+)?)$", summary)
    valid = (
        result.returncode == 0
        and not result.stderr
        and summary.startswith("PASS ")
        and all(key in parsed for key in COUNT_KEYS)
        and seconds_match is not None
    )
    return {
        "batch": batch_index,
        "orbits": len(batch),
        "returncode": result.returncode,
        "stderr": result.stderr[-4000:],
        "summary": summary,
        "valid": valid,
        "counts": {key: parsed.get(key, 0) for key in COUNT_KEYS},
        "worker_seconds": float(seconds_match.group(1)) if seconds_match else None,
        "witnesses": [line for line in lines[:-1] if line.startswith("WITNESS ")],
    }


def write_packet(
    atlas: dict[str, object], expected_batches: int, rows: list[dict[str, object]]
) -> dict[str, object]:
    ordered = sorted(rows, key=lambda row: int(row["batch"]))
    counts = {key: 0 for key in COUNT_KEYS}
    witnesses: list[str] = []
    worker_seconds: list[float] = []
    for row in ordered:
        if row["valid"]:
            for key in COUNT_KEYS:
                counts[key] += int(row["counts"][key])
            witnesses.extend(str(value) for value in row["witnesses"])
            worker_seconds.append(float(row["worker_seconds"]))
    complete = len(ordered) == expected_batches and all(row["valid"] for row in ordered)
    packet = {
        "schema": "e1-profile-36-mu5-m32-direct-radius-result-v1",
        "complete": complete,
        "orbit_file_sha256": hashlib.sha256(ORBIT_PATH.read_bytes()).hexdigest(),
        "engine_sha256": hashlib.sha256(CPP_PATH.read_bytes()).hexdigest(),
        "fixed_roots_sha256": hashlib.sha256(FIXED_ROOTS_PATH.read_bytes()).hexdigest(),
        "product_header_sha256": hashlib.sha256(PRODUCT_HEADER_PATH.read_bytes()).hexdigest(),
        "affine_orbits": atlas["affine_orbits"],
        "expected_batches": expected_batches,
        "completed_batches": len(ordered),
        "counts": counts,
        "total_worker_seconds": sum(worker_seconds),
        "max_worker_seconds": max(worker_seconds, default=0.0),
        "witnesses": witnesses,
        "rows": ordered,
    }
    temporary = OUTPUT.with_suffix(OUTPUT.suffix + ".tmp")
    temporary.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    temporary.replace(OUTPUT)
    return packet


@app.local_entrypoint()
def main(batch_size: int = 16) -> None:
    atlas = json.loads(ORBIT_PATH.read_text())
    orbits = atlas["orbits"]
    batches = [orbits[start : start + batch_size] for start in range(0, len(orbits), batch_size)]
    tasks = list(enumerate(batches))
    completed: list[dict[str, object]] = []
    packet = write_packet(atlas, len(tasks), completed)
    for position, (task, returned) in enumerate(
        zip(
            tasks,
            classify_batch.starmap(tasks, order_outputs=True, return_exceptions=True),
            strict=True,
        ),
        start=1,
    ):
        batch_index, batch = task
        if isinstance(returned, BaseException):
            row: dict[str, object] = {
                "batch": batch_index,
                "orbits": len(batch),
                "returncode": None,
                "stderr": repr(returned),
                "summary": "",
                "valid": False,
                "counts": {key: 0 for key in COUNT_KEYS},
                "worker_seconds": None,
                "witnesses": [],
            }
        else:
            row = returned
        completed.append(row)
        packet = write_packet(atlas, len(tasks), completed)
        if position % 16 == 0 or position == len(tasks) or not row["valid"]:
            print(
                f"progress={position}/{len(tasks)} batch={batch_index} "
                f"valid={row['valid']} fixed_above={packet['counts']['fixed_above']}"
            )

    counts = packet["counts"]
    assert packet["complete"]
    assert counts["orbits"] == atlas["affine_orbits"] == 19840
    assert counts["triple_syndromes"] == counts["orbits"] * 295240
    assert counts["distance_tests"] == 32 * counts["triple_syndromes"]
    assert counts["exact_sign_tests"] == 8 * counts["radius_matches"]
    assert counts["product_live_vectors"] == (
        counts["fixed_below"] + counts["fixed_above"] + counts["fixed_unresolved"]
    )
    assert counts["screen_below"] == counts["fixed_below"]
    assert counts["screen_above"] == counts["fixed_above"]
    assert counts["screen_near"] == counts["fixed_unresolved"] == 0
    assert len(packet["witnesses"]) == counts["fixed_above"]
    print(
        "E1_PROFILE_36_MU5_M32_DIRECT_RADIUS_PASS "
        f"orbits={counts['orbits']} fixed_below={counts['fixed_below']} "
        f"fixed_above={counts['fixed_above']} output={OUTPUT}"
    )


if __name__ == "__main__":
    main()
