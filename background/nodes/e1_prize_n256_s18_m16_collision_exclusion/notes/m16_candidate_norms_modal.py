#!/usr/bin/env python3
"""Stream exact FLINT norms for the analytic m=16 residual."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "m16_residual_candidates.cpp"
OUTPUT = HERE / "m16_candidate_norms_result.json"
SHARDS = 32
BUCKETS = 64
MODULUS = 1 << 256
ENERGIES = list(range(5, 54, 4))
B_PRIZE = 317494674775468773183020924238786383963

image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .pip_install("python-flint")
    .add_local_file(str(SOURCE), "/root/candidates.cpp", copy=True)
    .run_commands(
        "g++ -O3 -std=c++17 /root/candidates.cpp -o /usr/local/bin/candidates"
    )
)
app = modal.App("e1-prize-m16-candidate-norms")


def empty_fingerprint() -> list[dict[str, int]]:
    return [
        {"count": 0, "xor": 0, "sum": 0, "sum_square": 0}
        for _ in range(BUCKETS)
    ]


def parse_candidate(line: str) -> tuple[int, list[int], list[int]]:
    values = [int(value) for value in line.split("\t")]
    assert len(values) == 13
    return values[0], values[1:7], values[7:13]


def update_fingerprint(
    fingerprint: list[dict[str, int]], row: dict[str, object]
) -> None:
    encoded = (json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n").encode()
    digest = hashlib.sha256(encoded).digest()
    value = int.from_bytes(digest, "big")
    bucket = digest[0] & (BUCKETS - 1)
    target = fingerprint[bucket]
    target["count"] += 1
    target["xor"] ^= value
    target["sum"] = (target["sum"] + value) % MODULUS
    target["sum_square"] = (target["sum_square"] + value * value) % MODULUS


@app.function(image=image, cpu=1.0, memory=512, timeout=60, max_containers=32)
def compute(shard: int) -> dict[str, object]:
    from flint import fmpz, fmpz_poly

    started = time.perf_counter()
    generated = subprocess.run(
        ["/usr/local/bin/candidates", str(shard)],
        capture_output=True,
        check=True,
        text=True,
        timeout=15,
    )
    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    lower = B_PRIZE * 2**128
    upper = (B_PRIZE + 1) * 2**128 - 1
    counts = {
        str(energy): {"below": 0, "inside": 0, "above": 0}
        for energy in ENERGIES
    }
    fingerprint = empty_fingerprint()
    maximum_below = None
    minimum_above = None
    interval_rows = []
    processed = 0
    for line in generated.stdout.splitlines():
        energy, positions, coefficients = parse_candidate(line)
        dense = [0] * 128
        for position, coefficient in zip(positions, coefficients):
            dense[position] = coefficient
        norm = abs(int(cyclotomic.resultant(fmpz_poly(dense))))
        assert norm % 16 == 0
        assert (norm & -norm).bit_length() - 1 == 4
        candidate = norm // 16
        row: dict[str, object] = {
            "positions": positions,
            "coefficients": coefficients,
            "energy": energy,
            "norm": norm,
            "candidate": candidate,
        }
        update_fingerprint(fingerprint, row)
        if candidate < lower:
            region = "below"
            if maximum_below is None or candidate > int(maximum_below["candidate"]):
                maximum_below = row
        elif candidate > upper:
            region = "above"
            if minimum_above is None or candidate < int(minimum_above["candidate"]):
                minimum_above = row
        else:
            region = "inside"
            row["candidate_is_prime"] = bool(fmpz(candidate).is_prime())
            interval_rows.append(row)
        counts[str(energy)][region] += 1
        processed += 1
    return {
        "complete": True,
        "shard": shard,
        "processed": processed,
        "counts": counts,
        "fingerprint": fingerprint,
        "maximum_below": maximum_below,
        "minimum_above": minimum_above,
        "interval_rows": interval_rows,
        "wall_seconds": time.perf_counter() - started,
    }


def combine_fingerprints(
    results: list[dict[str, object]],
) -> list[dict[str, str | int]]:
    combined = empty_fingerprint()
    for result in results:
        for bucket, source in zip(combined, result["fingerprint"]):
            bucket["count"] += int(source["count"])
            bucket["xor"] ^= int(source["xor"])
            bucket["sum"] = (bucket["sum"] + int(source["sum"])) % MODULUS
            bucket["sum_square"] = (
                bucket["sum_square"] + int(source["sum_square"])
            ) % MODULUS
    return [
        {
            "count": bucket["count"],
            "xor": f"{bucket['xor']:064x}",
            "sum": f"{bucket['sum']:064x}",
            "sum_square": f"{bucket['sum_square']:064x}",
        }
        for bucket in combined
    ]


def write_packet(results: list[dict[str, object]]) -> None:
    complete = sorted(
        (result for result in results if result.get("complete") is True),
        key=lambda result: int(result["shard"]),
    )
    counts = {
        str(energy): {
            region: sum(
                int(result["counts"][str(energy)][region]) for result in complete
            )
            for region in ("below", "inside", "above")
        }
        for energy in ENERGIES
    }
    below = [result["maximum_below"] for result in complete if result["maximum_below"]]
    above = [result["minimum_above"] for result in complete if result["minimum_above"]]
    interval_rows = [row for result in complete for row in result["interval_rows"]]
    packet = {
        "schema": "e1-prize-m16-candidate-norms-v1",
        "complete": len(complete) == SHARDS,
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "row_count": sum(int(result["processed"]) for result in complete),
        "prize_interval": [
            B_PRIZE * 2**128,
            (B_PRIZE + 1) * 2**128 - 1,
        ],
        "counts": counts,
        "fingerprint": combine_fingerprints(complete),
        "interval_rows": interval_rows,
        "maximum_below": max(below, key=lambda row: int(row["candidate"])) if below else None,
        "minimum_above": min(above, key=lambda row: int(row["candidate"])) if above else None,
        "returned_shards": len(results),
        "errors": [
            result for result in results if result.get("complete") is not True
        ],
        "worker_seconds": sum(float(result["wall_seconds"]) for result in complete),
        "shards": [
            {
                "shard": result["shard"],
                "processed": result["processed"],
                "wall_seconds": result["wall_seconds"],
            }
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
        print(f"M16_CANDIDATE_NORMS_PROGRESS returned={len(results)}/{SHARDS}")
    complete = sum(result.get("complete") is True for result in results)
    interval = sum(len(result.get("interval_rows", [])) for result in results)
    print(f"M16_CANDIDATE_NORMS complete={complete}/{SHARDS} interval={interval}")
