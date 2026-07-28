#!/usr/bin/env python3
"""Compute exact whole norms for every m=514 divisor-surviving vector."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
INPUT = HERE / "m514_low_variance_census_result.json"
OUTPUT = HERE / "m514_candidate_norms_result.json"
B_PRIZE = 317494674775468773183020924238786383963

image = (
    modal.Image.debian_slim()
    .pip_install("python-flint")
    .add_local_file(str(INPUT), "/root/candidates.json", copy=True)
)
app = modal.App("e1-prize-m514-candidate-norms")


@app.function(image=image, cpu=1.0, memory=512, timeout=60)
def compute() -> dict[str, object]:
    from flint import fmpz, fmpz_poly

    packet = json.loads(Path("/root/candidates.json").read_text())
    witnesses = [
        witness for witness in packet["witnesses"]
        if int(witness["root_exponent"]) >= 0
    ]
    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    lower = B_PRIZE * 2**128
    upper = (B_PRIZE + 1) * 2**128 - 1
    rows = []
    for witness in witnesses:
        dense = [0] * 128
        for position, coefficient in zip(
            witness["positions"], witness["coefficients"]
        ):
            dense[int(position)] = int(coefficient)
        norm = abs(int(cyclotomic.resultant(fmpz_poly(dense))))
        assert norm % 514 == 0
        candidate = norm // 514
        rows.append(
            {
                "positions": witness["positions"],
                "coefficients": witness["coefficients"],
                "energy": witness["energy"],
                "root_exponent": witness["root_exponent"],
                "norm": norm,
                "candidate": candidate,
                "candidate_in_prize_interval": lower <= candidate <= upper,
                "candidate_mod_256": candidate % 256,
                "candidate_is_prime": bool(fmpz(candidate).is_prime()),
            }
        )
    distinct_norms = sorted({int(row["norm"]) for row in rows})
    interval_rows = [row for row in rows if row["candidate_in_prize_interval"]]
    return {
        "schema": "e1-prize-m514-candidate-norms-v1",
        "complete": True,
        "input_witness_count": len(witnesses),
        "row_count": len(rows),
        "distinct_norm_count": len(distinct_norms),
        "minimum_norm": min(distinct_norms),
        "maximum_norm": max(distinct_norms),
        "prize_interval": [lower, upper],
        "interval_row_count": len(interval_rows),
        "interval_prime_row_count": sum(
            row["candidate_is_prime"] and row["candidate_mod_256"] == 1
            for row in interval_rows
        ),
        "rows": rows,
    }


@app.local_entrypoint()
def main() -> None:
    result = compute.remote()
    result["input_sha256"] = hashlib.sha256(INPUT.read_bytes()).hexdigest()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "M514_CANDIDATE_NORMS "
        f"complete={result['complete']} rows={result['row_count']} "
        f"distinct={result['distinct_norm_count']} "
        f"interval={result['interval_row_count']}"
    )
