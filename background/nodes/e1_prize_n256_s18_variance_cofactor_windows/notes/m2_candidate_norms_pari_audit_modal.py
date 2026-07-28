#!/usr/bin/env python3
"""Replay the streamed m=2 residual with PARI and an independent census."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "m2_residual_candidates_audit.cpp"
PRIMARY = HERE / "m2_candidate_norms_result.json"
OUTPUT = HERE / "m2_candidate_norms_pari_audit_result.json"
SHARDS = 32
BUCKETS = 64
MODULUS = 1 << 256
ENERGIES = list(range(5, 50, 4))

image = (
    modal.Image.debian_slim()
    .apt_install("g++", "pari-gp")
    .add_local_file(str(SOURCE), "/root/candidates.cpp", copy=True)
    .add_local_file(str(PRIMARY), "/root/primary.json", copy=True)
    .run_commands(
        "g++ -O3 -std=c++17 /root/candidates.cpp -o /usr/local/bin/candidates"
    )
)
app = modal.App("e1-prize-m2-candidate-norms-pari-audit")


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


@app.function(image=image, cpu=1.0, memory=512, timeout=180, max_containers=32)
def audit(shard: int) -> dict[str, object]:
    primary = json.loads(Path("/root/primary.json").read_text())
    lower, upper = map(int, primary["prize_interval"])
    started = time.perf_counter()
    generated = subprocess.run(
        ["/usr/local/bin/candidates", str(shard)],
        capture_output=True,
        check=True,
        text=True,
        timeout=20,
    )
    candidates = [parse_candidate(line) for line in generated.stdout.splitlines()]
    commands = []
    for _, positions, coefficients in candidates:
        polynomial = "+".join(
            f"({coefficient})*x^{position}"
            for position, coefficient in zip(positions, coefficients)
        )
        commands.append(
            "n=abs(polresultant(x^128+1,"
            f"{polynomial}));"
            f"print(n,\",\",if(n%2==0&&n/2>={lower}&&n/2<={upper},"
            "isprime(n/2),-1))"
        )
    completed = subprocess.run(
        ["gp", "-fq"],
        input="\n".join(commands) + "\nquit\n",
        capture_output=True,
        check=True,
        text=True,
        timeout=150,
    )
    norm_flags = [
        tuple(int(value) for value in line.split(","))
        for line in completed.stdout.splitlines()
        if line.strip()
    ]
    assert len(norm_flags) == len(candidates)
    counts = {
        str(energy): {"below": 0, "inside_composite": 0, "inside_prime": 0, "above": 0}
        for energy in ENERGIES
    }
    fingerprint = empty_fingerprint()
    maximum_below = None
    minimum_above = None
    interval_rows = []
    for (energy, positions, coefficients), (norm, prime_flag) in zip(
        candidates, norm_flags
    ):
        assert norm % 2 == 0
        candidate = norm // 2
        row: dict[str, object] = {
            "positions": positions,
            "coefficients": coefficients,
            "energy": energy,
            "norm": norm,
            "candidate": candidate,
        }
        if candidate < lower:
            assert prime_flag == -1
            region = "below"
            if maximum_below is None or candidate > int(maximum_below["candidate"]):
                maximum_below = row
        elif candidate > upper:
            assert prime_flag == -1
            region = "above"
            if minimum_above is None or candidate < int(minimum_above["candidate"]):
                minimum_above = row
        else:
            assert prime_flag in (0, 1)
            is_prime = prime_flag == 1
            row["candidate_is_prime"] = is_prime
            region = "inside_prime" if is_prime else "inside_composite"
            interval_rows.append(row)
        update_fingerprint(fingerprint, row)
        counts[str(energy)][region] += 1
    return {
        "complete": True,
        "shard": shard,
        "processed": len(candidates),
        "counts": counts,
        "fingerprint": fingerprint,
        "maximum_below": maximum_below,
        "minimum_above": minimum_above,
        "interval_rows": interval_rows,
        "wall_seconds": time.perf_counter() - started,
    }


def combine_fingerprints(results: list[dict[str, object]]) -> list[dict[str, str | int]]:
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
    primary = json.loads(PRIMARY.read_text())
    complete = sorted(
        (result for result in results if result.get("complete") is True),
        key=lambda result: int(result["shard"]),
    )
    regions = ("below", "inside_composite", "inside_prime", "above")
    counts = {
        str(energy): {
            region: sum(int(result["counts"][str(energy)][region]) for result in complete)
            for region in regions
        }
        for energy in ENERGIES
    }
    fingerprint = combine_fingerprints(complete)
    below = [result["maximum_below"] for result in complete if result["maximum_below"]]
    above = [result["minimum_above"] for result in complete if result["minimum_above"]]
    interval_rows = [row for result in complete for row in result["interval_rows"]]
    packet = {
        "schema": "e1-prize-m2-candidate-norms-pari-audit-v1",
        "complete": len(complete) == SHARDS,
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "primary_sha256": hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
        "row_count": sum(int(result["processed"]) for result in complete),
        "counts": counts,
        "fingerprint": fingerprint,
        "primary_match": (
            len(complete) == SHARDS
            and counts == primary["counts"]
            and fingerprint == primary["fingerprint"]
        ),
        "interval_rows": interval_rows,
        "maximum_below": max(below, key=lambda row: int(row["candidate"])) if below else None,
        "minimum_above": min(above, key=lambda row: int(row["candidate"])) if above else None,
        "returned_shards": len(results),
        "errors": [result for result in results if result.get("complete") is not True],
        "worker_seconds": sum(float(result["wall_seconds"]) for result in complete),
        "shards": [
            {"shard": result["shard"], "processed": result["processed"], "wall_seconds": result["wall_seconds"]}
            for result in complete
        ],
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main() -> None:
    results: list[dict[str, object]] = []
    for result in audit.map(range(SHARDS), order_outputs=False):
        results.append(result)
        write_packet(results)
        print(f"M2_NORM_PARI_AUDIT_PROGRESS returned={len(results)}/{SHARDS}")
    complete = sum(result.get("complete") is True for result in results)
    inside = sum(len(result.get("interval_rows", [])) for result in results)
    print(f"M2_NORM_PARI_AUDIT complete={complete}/{SHARDS} inside={inside}")
