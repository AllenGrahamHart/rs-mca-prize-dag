#!/usr/bin/env python3
"""Shard exact FLINT norms for every m=256 residual vector."""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
INPUT = HERE / "m256_residual_census_result.json"
OUTPUT = HERE / "m256_candidate_norms_result.json"
SHARDS = 32
B_PRIZE = 317494674775468773183020924238786383963

image = (
    modal.Image.debian_slim()
    .pip_install("python-flint")
    .add_local_file(str(INPUT), "/root/candidates.json", copy=True)
)
app = modal.App("e1-prize-m256-candidate-norms")


def row_key(row: dict[str, object]) -> tuple[int, ...]:
    return tuple(int(value) for value in row["positions"] + row["coefficients"])


@app.function(image=image, cpu=1.0, memory=512, timeout=60, max_containers=32)
def compute(shard: int) -> dict[str, object]:
    from flint import fmpz, fmpz_poly

    packet = json.loads(Path("/root/candidates.json").read_text())
    witnesses = packet["witnesses"]
    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    lower = B_PRIZE * 2**128
    upper = (B_PRIZE + 1) * 2**128 - 1
    counts = {str(energy): {"below": 0, "inside": 0, "above": 0}
              for energy in packet["energies"]}
    commitment = hashlib.sha256()
    maximum_below = None
    minimum_above = None
    interval_rows = []
    started = time.perf_counter()
    processed = 0
    for index in range(shard, len(witnesses), SHARDS):
        witness = witnesses[index]
        dense = [0] * 128
        for position, coefficient in zip(
            witness["positions"], witness["coefficients"]
        ):
            dense[int(position)] = int(coefficient)
        norm = abs(int(cyclotomic.resultant(fmpz_poly(dense))))
        assert norm % 256 == 0
        assert (norm & -norm).bit_length() - 1 == 8
        candidate = norm // 256
        row = {
            "index": index,
            "positions": witness["positions"],
            "coefficients": witness["coefficients"],
            "energy": witness["energy"],
            "norm": norm,
            "candidate": candidate,
        }
        commitment.update(
            (json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n").encode()
        )
        if candidate < lower:
            region = "below"
            if maximum_below is None or candidate > maximum_below["candidate"]:
                maximum_below = row
        elif candidate > upper:
            region = "above"
            if minimum_above is None or candidate < minimum_above["candidate"]:
                minimum_above = row
        else:
            region = "inside"
            row["candidate_mod_256"] = candidate % 256
            row["candidate_is_prime"] = bool(fmpz(candidate).is_prime())
            interval_rows.append(row)
        counts[str(witness["energy"])][region] += 1
        processed += 1
    return {
        "complete": True,
        "shard": shard,
        "processed": processed,
        "commitment_sha256": commitment.hexdigest(),
        "counts": counts,
        "maximum_below": maximum_below,
        "minimum_above": minimum_above,
        "interval_rows": interval_rows,
        "wall_seconds": time.perf_counter() - started,
    }


def write_packet(results: list[dict[str, object]]) -> None:
    complete = sorted(
        (result for result in results if result.get("complete") is True),
        key=lambda result: int(result["shard"]),
    )
    energies = [5, 9, 13, 17, 21, 25, 29, 33, 37]
    counts = {
        str(energy): {
            region: sum(int(result["counts"][str(energy)][region]) for result in complete)
            for region in ("below", "inside", "above")
        }
        for energy in energies
    }
    below_rows = [result["maximum_below"] for result in complete if result["maximum_below"]]
    above_rows = [result["minimum_above"] for result in complete if result["minimum_above"]]
    interval_rows = [row for result in complete for row in result["interval_rows"]]
    packet = {
        "schema": "e1-prize-m256-candidate-norms-v1",
        "complete": len(complete) == SHARDS,
        "input_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        "row_count": sum(int(result["processed"]) for result in complete),
        "prize_interval": [B_PRIZE * 2**128, (B_PRIZE + 1) * 2**128 - 1],
        "counts": counts,
        "interval_rows": interval_rows,
        "maximum_below": max(below_rows, key=lambda row: int(row["candidate"])) if below_rows else None,
        "minimum_above": min(above_rows, key=lambda row: int(row["candidate"])) if above_rows else None,
        "returned_shards": len(results),
        "errors": [result for result in results if result.get("complete") is not True],
        "worker_seconds": sum(float(result["wall_seconds"]) for result in complete),
        "shards": [
            {key: value for key, value in result.items()
             if key not in {"maximum_below", "minimum_above", "interval_rows"}}
            for result in complete
        ],
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main() -> None:
    results: list[dict[str, object]] = []
    for result in compute.map(range(SHARDS), order_outputs=False):
        results.append(result)
        write_packet(results)
        print(f"M256_CANDIDATE_NORMS_PROGRESS returned={len(results)}/{SHARDS}")
    complete = sum(result.get("complete") is True for result in results)
    interval = sum(len(result.get("interval_rows", [])) for result in results)
    print(f"M256_CANDIDATE_NORMS complete={complete}/{SHARDS} interval={interval}")
