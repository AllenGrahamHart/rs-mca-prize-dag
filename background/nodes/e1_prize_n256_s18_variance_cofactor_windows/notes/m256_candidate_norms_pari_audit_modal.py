#!/usr/bin/env python3
"""Replay all m=256 shard commitments with independent PARI resultants."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
CENSUS = HERE / "m256_residual_census_result.json"
PRIMARY = HERE / "m256_candidate_norms_result.json"
OUTPUT = HERE / "m256_candidate_norms_pari_audit_result.json"
SHARDS = 32

image = (
    modal.Image.debian_slim()
    .apt_install("pari-gp")
    .add_local_file(str(CENSUS), "/root/census.json", copy=True)
    .add_local_file(str(PRIMARY), "/root/primary.json", copy=True)
)
app = modal.App("e1-prize-m256-candidate-norms-pari-audit")


@app.function(image=image, cpu=1.0, memory=512, timeout=60, max_containers=32)
def audit(shard: int) -> dict[str, object]:
    census = json.loads(Path("/root/census.json").read_text())
    primary = json.loads(Path("/root/primary.json").read_text())
    witnesses = census["witnesses"]
    primary_shard = next(row for row in primary["shards"] if row["shard"] == shard)
    indices = list(range(shard, len(witnesses), SHARDS))
    commands = []
    for index in indices:
        witness = witnesses[index]
        polynomial = "+".join(
            f"({int(coefficient)})*x^{int(position)}"
            for position, coefficient in zip(
                witness["positions"], witness["coefficients"]
            )
        )
        commands.append(f"print(abs(polresultant(x^128+1,{polynomial})))")
    started = time.perf_counter()
    completed = subprocess.run(
        ["gp", "-fq"],
        input="\n".join(commands) + "\nquit\n",
        capture_output=True,
        check=True,
        text=True,
        timeout=52,
    )
    norms = [int(line) for line in completed.stdout.splitlines() if line.strip()]
    assert len(norms) == len(indices)
    commitment = hashlib.sha256()
    counts = {str(energy): {"below": 0, "inside": 0, "above": 0}
              for energy in census["energies"]}
    lower, upper = map(int, primary["prize_interval"])
    for index, norm in zip(indices, norms):
        witness = witnesses[index]
        assert norm % 256 == 0
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
        region = "below" if candidate < lower else "above" if candidate > upper else "inside"
        counts[str(witness["energy"])][region] += 1
    assert commitment.hexdigest() == primary_shard["commitment_sha256"]
    assert counts == primary_shard["counts"]
    return {
        "complete": True,
        "shard": shard,
        "processed": len(norms),
        "commitment_sha256": commitment.hexdigest(),
        "primary_match": True,
        "wall_seconds": time.perf_counter() - started,
    }


def write_packet(results: list[dict[str, object]]) -> None:
    complete = sorted(
        (result for result in results if result.get("complete") is True),
        key=lambda result: int(result["shard"]),
    )
    packet = {
        "schema": "e1-prize-m256-candidate-norms-pari-audit-v1",
        "complete": len(complete) == SHARDS,
        "census_sha256": hashlib.sha256(CENSUS.read_bytes()).hexdigest(),
        "primary_sha256": hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
        "row_count": sum(int(result["processed"]) for result in complete),
        "primary_match": all(result["primary_match"] for result in complete),
        "returned_shards": len(results),
        "errors": [result for result in results if result.get("complete") is not True],
        "worker_seconds": sum(float(result["wall_seconds"]) for result in complete),
        "shards": complete,
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main() -> None:
    results: list[dict[str, object]] = []
    for result in audit.map(range(SHARDS), order_outputs=False):
        results.append(result)
        write_packet(results)
        print(f"M256_NORM_PARI_AUDIT_PROGRESS returned={len(results)}/{SHARDS}")
    print(
        "M256_NORM_PARI_AUDIT "
        f"complete={sum(result.get('complete') is True for result in results)}/{SHARDS}"
    )
