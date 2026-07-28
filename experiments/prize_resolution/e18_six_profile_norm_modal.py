#!/usr/bin/env python3
"""Compute dual exact cyclotomic norms for the full E18 residue."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
CENSUS = HERE / "e18_six_profile_census_result.json"
RESULT = HERE / "e18_six_profile_norm_result.json"
BATCH_SIZE = 1000

app = modal.App("e1-n256-e18-six-profile-norm")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=12)
def run_flint(batch: tuple[int, list[dict[str, object]]]) -> dict[str, object]:
    import time

    from flint import fmpz_poly

    batch_index, vectors = batch
    started = time.monotonic()
    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    norms = []
    for vector in vectors:
        dense = [0] * 128
        for position, coefficient in zip(vector["positions"], vector["coefficients"]):
            dense[int(position)] = int(coefficient)
        norms.append(abs(int(cyclotomic.resultant(fmpz_poly(dense)))))
    return {
        "batch": batch_index,
        "norms": norms,
        "worker_seconds": time.monotonic() - started,
    }


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=12)
def run_pari(batch: tuple[int, list[dict[str, object]]]) -> dict[str, object]:
    import subprocess
    import time

    batch_index, vectors = batch
    started = time.monotonic()
    script = []
    for vector in vectors:
        terms = "+".join(
            f"({int(coefficient)})*x^{int(position)}"
            for position, coefficient in zip(vector["positions"], vector["coefficients"])
        )
        script.append(f"print(abs(polresultant(x^128+1,{terms})));")
    completed = subprocess.run(
        ["gp", "-q"],
        input="\n".join(script) + "\n",
        capture_output=True,
        check=True,
        text=True,
        timeout=55,
    )
    norms = [int(line) for line in completed.stdout.splitlines() if line.strip()]
    if len(norms) != len(vectors):
        raise RuntimeError(
            f"batch {batch_index}: expected {len(vectors)} norms, got {len(norms)}"
        )
    return {
        "batch": batch_index,
        "norms": norms,
        "worker_seconds": time.monotonic() - started,
    }


def load_vectors() -> list[dict[str, object]]:
    packet = json.loads(CENSUS.read_text())
    if not packet["complete"]:
        raise RuntimeError("E18 census is incomplete")
    vectors = [
        match for row in packet["rows"] for match in row["primary"]["matches"]
    ]
    if len(vectors) != int(packet["summary"]["collected_full_conductor"]):
        raise RuntimeError("E18 full-conductor collection count mismatch")
    return vectors


@app.local_entrypoint()
def main() -> None:
    vectors = load_vectors()
    batches = [
        (index // BATCH_SIZE, vectors[index : index + BATCH_SIZE])
        for index in range(0, len(vectors), BATCH_SIZE)
    ]
    flint_rows: list[dict[str, object]] = []
    pari_rows: list[dict[str, object]] = []

    def flatten(rows: list[dict[str, object]]) -> list[int]:
        return [
            int(value)
            for row in sorted(rows, key=lambda item: int(item["batch"]))
            for value in row["norms"]
        ]

    def write_checkpoint(complete: bool, error: str | None = None) -> dict[str, object]:
        packet = {
            "schema": "e1-e18-six-profile-norm-v1",
            "complete": complete,
            "agreement": False,
            "vectors": len(vectors),
            "batch_size": BATCH_SIZE,
            "expected_batches": len(batches),
            "completed_flint": len(flint_rows),
            "completed_pari": len(pari_rows),
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "census_sha256": hashlib.sha256(CENSUS.read_bytes()).hexdigest(),
            "error": error,
            "flint": sorted(flint_rows, key=lambda row: int(row["batch"])),
            "pari": sorted(pari_rows, key=lambda row: int(row["batch"])),
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return packet

    write_checkpoint(False)
    try:
        for row in run_flint.map(batches):
            flint_rows.append(row)
            write_checkpoint(False)
        for row in run_pari.map(batches):
            pari_rows.append(row)
            write_checkpoint(False)
    except BaseException as error:
        write_checkpoint(False, f"{type(error).__name__}: {error}")
        print(
            "E18_SIX_PROFILE_NORM_INCOMPLETE "
            f"flint={len(flint_rows)}/{len(batches)} "
            f"pari={len(pari_rows)}/{len(batches)}"
        )
        raise
    flint_norms = flatten(flint_rows)
    pari_norms = flatten(pari_rows)
    if len(flint_norms) != len(vectors) or flint_norms != pari_norms:
        raise RuntimeError("FLINT/PARI E18 norm mismatch")
    valuations = [(norm & -norm).bit_length() - 1 for norm in flint_norms]
    odd_parts = [norm >> valuation for norm, valuation in zip(flint_norms, valuations)]
    profile_maxima = [
        max(
            (
                norm
                for norm, vector in zip(flint_norms, vectors)
                if int(vector["profile"]) == profile
            ),
            default=0,
        )
        for profile in range(6)
    ]
    profile_odd_maxima = [
        max(
            (
                odd
                for odd, vector in zip(odd_parts, vectors)
                if int(vector["profile"]) == profile
            ),
            default=0,
        )
        for profile in range(6)
    ]
    packet = write_checkpoint(True)
    packet["agreement"] = True
    packet["summary"] = {
        "vectors": len(vectors),
        "distinct_norms": len(set(flint_norms)),
        "maximum_norm": max(flint_norms),
        "maximum_norm_bits": max(flint_norms).bit_length(),
        "profile_maximum_norms": profile_maxima,
        "profile_maximum_bits": [value.bit_length() for value in profile_maxima],
        "norms_at_or_above_2_250": sum(norm >= 2**250 for norm in flint_norms),
        "maximum_odd_part": max(odd_parts),
        "maximum_odd_part_bits": max(odd_parts).bit_length(),
        "odd_parts_at_or_above_2_250": sum(odd >= 2**250 for odd in odd_parts),
        "maximum_valuation": max(valuations),
        "profile_maximum_odd_parts": profile_odd_maxima,
        "profile_maximum_odd_bits": [value.bit_length() for value in profile_odd_maxima],
        "maximizing_indices": [
            index for index, value in enumerate(flint_norms) if value == max(flint_norms)
        ],
        "odd_part_maximizing_indices": [
            index for index, value in enumerate(odd_parts) if value == max(odd_parts)
        ],
        "flint_worker_seconds": sum(float(row["worker_seconds"]) for row in flint_rows),
        "pari_worker_seconds": sum(float(row["worker_seconds"]) for row in pari_rows),
    }
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print("E18_SIX_PROFILE_NORM " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E18_SIX_PROFILE_NORM_AGREEMENT {packet['agreement']}")
    print(f"E18_SIX_PROFILE_NORM_RESULT {RESULT}")
