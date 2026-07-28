#!/usr/bin/env python3
"""Compute dual exact norms for the E26 top-mask primitive vectors."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
ACTUAL = HERE / "e26_six_odd_top_mask_actual_result.json"
RESULT = HERE / "e26_six_odd_top_mask_norm_result.json"

app = modal.App("e1-e26-six-odd-top-mask-norm")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=2)
def run_flint(vectors: list[dict[str, object]]) -> dict[str, object]:
    import time

    from flint import fmpz, fmpz_poly

    started = time.monotonic()
    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    rows = []
    for vector in vectors:
        positions = [int(value) for value in vector["positions"]]
        coefficients = [int(value) for value in vector["coefficients"]]
        dense = [0] * 128
        for position, coefficient in zip(positions, coefficients):
            dense[position] = coefficient
        norm = abs(int(cyclotomic.resultant(fmpz_poly(dense))))
        valuation = (norm & -norm).bit_length() - 1
        odd_part = norm >> valuation
        rows.append(
            {
                "norm": norm,
                "valuation": valuation,
                "odd_part": odd_part,
                "odd_part_is_prime": bool(fmpz(odd_part).is_prime()),
            }
        )
    return {"rows": rows, "worker_seconds": time.monotonic() - started}


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=2)
def run_pari(vectors: list[dict[str, object]]) -> dict[str, object]:
    import subprocess
    import time

    started = time.monotonic()
    script = []
    for vector in vectors:
        terms = "+".join(
            f"({int(coefficient)})*x^{int(position)}"
            for position, coefficient in zip(vector["positions"], vector["coefficients"])
        )
        script.append(
            f"n=abs(polresultant(x^128+1,{terms}));"
            "v=valuation(n,2);o=n/2^v;print(n);print(v);print(isprime(o));"
        )
    completed = subprocess.run(
        ["gp", "-q"],
        input="\n".join(script) + "\n",
        capture_output=True,
        check=True,
        text=True,
        timeout=55,
    )
    values = [int(line.strip()) for line in completed.stdout.splitlines() if line.strip()]
    if len(values) != 3 * len(vectors):
        raise RuntimeError(f"expected {3 * len(vectors)} PARI values, got {len(values)}")
    rows = []
    for index in range(len(vectors)):
        norm, valuation, prime = values[3 * index : 3 * index + 3]
        rows.append(
            {
                "norm": norm,
                "valuation": valuation,
                "odd_part": norm >> valuation,
                "odd_part_is_prime": bool(prime),
            }
        )
    return {"rows": rows, "worker_seconds": time.monotonic() - started}


def load_vectors() -> list[dict[str, object]]:
    packet = json.loads(ACTUAL.read_text())
    assert packet["complete"] is True and packet["completed_tasks"] == 32
    vectors = []
    for row in packet["rows"]:
        for vector in row["top"]:
            positions = [int(value) for value in vector["positions"]]
            assert math.gcd(256, *positions) == 1
            vectors.append(
                {
                    "task": int(row["task"]),
                    "profile": int(row["profile"]),
                    "light": row["light"],
                    "m3": int(vector["m3"]),
                    "positions": positions,
                    "coefficients": [int(value) for value in vector["coefficients"]],
                }
            )
    assert len(vectors) == 44
    return vectors


@app.local_entrypoint()
def main() -> None:
    vectors = load_vectors()
    packet: dict[str, object] = {
        "schema": "e1-e26-six-odd-top-mask-norm-v1",
        "complete": False,
        "agreement": False,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "actual_sha256": hashlib.sha256(ACTUAL.read_bytes()).hexdigest(),
        "vectors": vectors,
    }
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    try:
        flint = run_flint.remote(vectors)
        packet["flint"] = flint
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        pari = run_pari.remote(vectors)
        packet["pari"] = pari
    except BaseException as error:
        packet["error"] = f"{type(error).__name__}: {error}"
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        print("E26_SIX_ODD_TOP_MASK_NORM_INCOMPLETE")
        raise

    packet["agreement"] = flint["rows"] == pari["rows"]
    records = []
    for vector, norm_row in zip(vectors, flint["rows"]):
        records.append({**vector, **norm_row})
    candidates = [
        row
        for row in records
        if bool(row["odd_part_is_prime"])
        and 2**250 < int(row["odd_part"]) < 2**256
    ]
    packet["records"] = records
    packet["summary"] = {
        "vectors": len(records),
        "distinct_norms": len({int(row["norm"]) for row in records}),
        "maximum_norm": max(int(row["norm"]) for row in records),
        "maximum_norm_bits": max(int(row["norm"]).bit_length() for row in records),
        "odd_prime_parts": sum(bool(row["odd_part_is_prime"]) for row in records),
        "pair_floor_prime_candidates": len(candidates),
        "candidate_indices": [records.index(row) for row in candidates],
        "flint_worker_seconds": float(flint["worker_seconds"]),
        "pari_worker_seconds": float(pari["worker_seconds"]),
    }
    packet["complete"] = bool(packet["agreement"])
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print("E26_SIX_ODD_TOP_MASK_NORM " + json.dumps(packet["summary"], sort_keys=True))
