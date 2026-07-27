#!/usr/bin/env python3
"""Compute dual exact norms for every primitive E25 cubic exception."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
CENSUS = HERE / "e25_nine_profile_census_result.json"
RESULT = HERE / "e25_nine_profile_norm_result.json"
BATCH_SIZE = 1000

app = modal.App("e1-e25-nine-profile-norm")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=100)
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


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=100)
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
        script.append(f"print(abs(polresultant(x^128+1,{terms})));" )
    completed = subprocess.run(
        ["gp", "-q"],
        input="\n".join(script) + "\n",
        capture_output=True,
        check=True,
        text=True,
        timeout=55,
    )
    norms = [int(line.strip()) for line in completed.stdout.splitlines() if line.strip()]
    if len(norms) != len(vectors):
        raise RuntimeError(f"batch {batch_index}: expected {len(vectors)} norms, got {len(norms)}")
    return {
        "batch": batch_index,
        "norms": norms,
        "worker_seconds": time.monotonic() - started,
    }


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=2)
def prime_flint(values: list[int]) -> list[bool]:
    from flint import fmpz

    return [bool(fmpz(value).is_prime()) for value in values]


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=2)
def prime_pari(values: list[int]) -> list[bool]:
    import subprocess

    completed = subprocess.run(
        ["gp", "-q"],
        input="\n".join(f"print(isprime({value}));" for value in values) + "\n",
        capture_output=True,
        check=True,
        text=True,
        timeout=55,
    )
    result = [bool(int(line.strip())) for line in completed.stdout.splitlines() if line.strip()]
    if len(result) != len(values):
        raise RuntimeError(f"expected {len(values)} primality rows, got {len(result)}")
    return result


def load_vectors() -> list[dict[str, object]]:
    packet = json.loads(CENSUS.read_text())
    assert packet["complete"] is packet["agreement"] is True
    assert packet["completed_production"] == packet["completed_audit"] == 111
    vectors = []
    for row in packet["production"]:
        vectors.extend(
            vector for vector in row["matches"] if int(vector["conductor"]) == 1
        )
    assert len(vectors) == 16_984
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

    def write_checkpoint(complete: bool, error: str | None = None) -> dict[str, object]:
        packet = {
            "schema": "e1-e25-nine-profile-norm-v1",
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
            if len(flint_rows) % 4 == 0:
                write_checkpoint(False)
        for row in run_pari.map(batches):
            pari_rows.append(row)
            if len(pari_rows) % 4 == 0:
                write_checkpoint(False)
    except BaseException as error:
        write_checkpoint(False, f"{type(error).__name__}: {error}")
        print(
            "E25_NINE_PROFILE_NORM_INCOMPLETE "
            f"flint={len(flint_rows)}/{len(batches)} pari={len(pari_rows)}/{len(batches)}"
        )
        raise

    write_checkpoint(False)
    flint_rows.sort(key=lambda row: int(row["batch"]))
    pari_rows.sort(key=lambda row: int(row["batch"]))
    flint_norms = [int(value) for row in flint_rows for value in row["norms"]]
    pari_norms = [int(value) for row in pari_rows for value in row["norms"]]
    assert len(flint_norms) == len(pari_norms) == len(vectors)
    if flint_norms != pari_norms:
        raise RuntimeError("FLINT/PARI norm mismatch")

    valuations = [(norm & -norm).bit_length() - 1 for norm in flint_norms]
    odd_parts = [norm >> valuation for norm, valuation in zip(flint_norms, valuations)]
    eligible_values = sorted({value for value in odd_parts if 2**250 < value < 2**256})
    flint_prime = prime_flint.remote(eligible_values) if eligible_values else []
    pari_prime = prime_pari.remote(eligible_values) if eligible_values else []
    if flint_prime != pari_prime:
        raise RuntimeError("FLINT/PARI primality mismatch")
    prime_values = {
        value for value, is_prime in zip(eligible_values, flint_prime) if is_prime
    }
    candidate_indices = [
        index for index, value in enumerate(odd_parts) if value in prime_values
    ]
    candidate_records = [
        {
            "index": index,
            "vector": vectors[index],
            "norm": flint_norms[index],
            "valuation": valuations[index],
            "odd_part": odd_parts[index],
        }
        for index in candidate_indices
    ]
    profile_maxima = [
        max(
            (norm for norm, vector in zip(flint_norms, vectors) if int(vector["profile"]) == profile),
            default=-1,
        )
        for profile in range(9)
    ]
    packet = write_checkpoint(True)
    packet["agreement"] = True
    packet["summary"] = {
        "vectors": len(vectors),
        "distinct_norms": len(set(flint_norms)),
        "maximum_norm": max(flint_norms),
        "maximum_norm_bits": max(flint_norms).bit_length(),
        "profile_maximum_norms": profile_maxima,
        "profile_maximum_bits": [value.bit_length() if value >= 0 else -1 for value in profile_maxima],
        "norms_at_or_above_2_250": sum(norm >= 2**250 for norm in flint_norms),
        "eligible_distinct_odd_parts": len(eligible_values),
        "prime_eligible_odd_parts": len(prime_values),
        "candidate_vectors": len(candidate_indices),
        "candidate_indices": candidate_indices,
        "flint_worker_seconds": sum(float(row["worker_seconds"]) for row in flint_rows),
        "pari_worker_seconds": sum(float(row["worker_seconds"]) for row in pari_rows),
    }
    packet["candidate_records"] = candidate_records
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print("E25_NINE_PROFILE_NORM " + json.dumps(packet["summary"], sort_keys=True))
