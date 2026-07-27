#!/usr/bin/env python3
"""Compute exact norms of all primitive exceptional E27 profile vectors."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
PRODUCTION = HERE / "e27_six_profile_joint_census_result.json"
AUDIT = HERE / "e27_six_profile_joint_census_audit_result.json"
RESULT = HERE / "e27_six_profile_exceptional_norm_result.json"
BATCH_SIZE = 16

app = modal.App("e1-n256-e27-six-profile-exceptional-norm")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=100)
def run_flint(batch_index: int, vectors: list[dict[str, object]]) -> dict[str, object]:
    import time

    from flint import fmpz_poly

    started = time.monotonic()
    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    norms = []
    for vector in vectors:
        positions = [int(value) for value in vector["positions"]]
        coefficients = [int(value) for value in vector["coefficients"]]
        dense = [0] * (max(positions) + 1)
        for position, coefficient in zip(positions, coefficients):
            dense[position] = coefficient
        norms.append(abs(int(cyclotomic.resultant(fmpz_poly(dense)))))
    return {"batch": batch_index, "norms": norms, "worker_seconds": time.monotonic() - started}


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=100)
def run_pari(batch_index: int, vectors: list[dict[str, object]]) -> dict[str, object]:
    import subprocess
    import time

    started = time.monotonic()
    script = []
    for vector in vectors:
        terms = [
            f"({int(coefficient)})*x^{int(position)}"
            for position, coefficient in zip(vector["positions"], vector["coefficients"])
        ]
        script.append(f"print(abs(polresultant(x^128+1,{'+'.join(terms)})));")
    completed = subprocess.run(
        ["gp", "-q"],
        input="\n".join(script) + "\n",
        capture_output=True,
        check=True,
        text=True,
        timeout=55,
    )
    norms = [int(line) for line in completed.stdout.splitlines() if line.strip()]
    return {"batch": batch_index, "norms": norms, "worker_seconds": time.monotonic() - started}


@app.local_entrypoint()
def main() -> None:
    production = json.loads(PRODUCTION.read_text())
    audit = json.loads(AUDIT.read_text())
    production_sha256 = hashlib.sha256(PRODUCTION.read_bytes()).hexdigest()
    if not production["complete"]:
        raise RuntimeError("E27 production census is incomplete")
    if not audit["complete"] or not audit["agreement"]:
        raise RuntimeError("E27 direct census audit is incomplete")
    if audit["production_sha256"] != production_sha256:
        raise RuntimeError("E27 direct census audit does not pin production")
    vectors = [
        match
        for row in production["rows"]
        for match in row["matches"]
        if int(match["conductor"]) == 1
    ]
    if len(vectors) != sum(int(value) for value in production["summary"]["full_above_cutoff"]):
        raise RuntimeError("primitive E27 exception count mismatch")
    batches = [vectors[start : start + BATCH_SIZE] for start in range(0, len(vectors), BATCH_SIZE)]
    batch_indices = list(range(len(batches)))
    flint_rows: list[dict[str, object]] = []
    pari_rows: list[dict[str, object]] = []

    def flatten(rows: list[dict[str, object]]) -> list[int]:
        return [
            int(norm)
            for row in sorted(rows, key=lambda item: int(item["batch"]))
            for norm in row["norms"]
        ]

    def write_checkpoint(complete: bool) -> dict[str, object]:
        flint_norms = flatten(flint_rows)
        pari_norms = flatten(pari_rows)
        agreement = len(flint_norms) == len(vectors) and flint_norms == pari_norms
        packet: dict[str, object] = {
            "schema": "e1-e27-six-profile-exceptional-norm-v1",
            "complete": complete,
            "agreement": agreement,
            "production_sha256": production_sha256,
            "audit_sha256": hashlib.sha256(AUDIT.read_bytes()).hexdigest(),
            "batch_size": BATCH_SIZE,
            "expected_batches": len(batches),
            "completed_flint_batches": len(flint_rows),
            "completed_pari_batches": len(pari_rows),
            "vectors": vectors,
            "flint_norms": flint_norms,
            "pari_norms": pari_norms,
            "flint_worker_seconds": sum(float(row["worker_seconds"]) for row in flint_rows),
            "pari_worker_seconds": sum(float(row["worker_seconds"]) for row in pari_rows),
        }
        if agreement:
            maximum = max(flint_norms)
            packet["summary"] = {
                "vectors": len(vectors),
                "distinct_norms": len(set(flint_norms)),
                "maximum_norm": maximum,
                "maximum_norm_bits": maximum.bit_length(),
                "norm_at_or_above_2_250": sum(value >= 2**250 for value in flint_norms),
                "maximizing_indices": [
                    index for index, value in enumerate(flint_norms) if value == maximum
                ],
            }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return packet

    write_checkpoint(False)
    try:
        for row in run_flint.map(batch_indices, batches):
            flint_rows.append(row)
        write_checkpoint(False)
        for row in run_pari.map(batch_indices, batches):
            pari_rows.append(row)
    except BaseException:
        write_checkpoint(False)
        print(
            "E27_SIX_PROFILE_EXCEPTIONAL_NORM_INCOMPLETE "
            f"flint={len(flint_rows)}/{len(batches)} pari={len(pari_rows)}/{len(batches)}"
        )
        raise
    packet = write_checkpoint(
        len(flint_rows) == len(batches)
        and len(pari_rows) == len(batches)
        and flatten(flint_rows) == flatten(pari_rows)
    )
    print("E27_SIX_PROFILE_EXCEPTIONAL_NORM " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E27_SIX_PROFILE_EXCEPTIONAL_NORM_AGREEMENT {packet['agreement']}")
    print(f"E27_SIX_PROFILE_EXCEPTIONAL_NORM_RESULT {RESULT}")
