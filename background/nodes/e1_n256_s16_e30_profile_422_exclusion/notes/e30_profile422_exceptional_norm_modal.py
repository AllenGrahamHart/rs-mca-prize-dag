#!/usr/bin/env python3
"""Compute the two exceptional full-conductor profile-(4,2,2) norms."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
ACTUAL = HERE / "e30_profile422_exceptional_actual_result.json"
RESULT = HERE / "e30_profile422_exceptional_norm_result.json"

app = modal.App("e1-n256-e30-profile422-exceptional-norm")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")


@app.function(image=image, cpu=1.0, memory=256, timeout=60)
def run_flint(vectors: list[dict[str, list[int]]]) -> list[int]:
    from flint import fmpz_poly

    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    norms = []
    for vector in vectors:
        dense = [0] * (max(vector["positions"]) + 1)
        for position, coefficient in zip(vector["positions"], vector["coefficients"]):
            dense[int(position)] = int(coefficient)
        norms.append(abs(int(cyclotomic.resultant(fmpz_poly(dense)))))
    return norms


@app.function(image=image, cpu=1.0, memory=256, timeout=60)
def run_pari(vectors: list[dict[str, list[int]]]) -> list[int]:
    import subprocess

    script = []
    for vector in vectors:
        terms = [
            f"({int(coefficient)})*x^{int(position)}"
            for position, coefficient in zip(vector["positions"], vector["coefficients"])
        ]
        script.append(f"print(abs(polresultant(x^128+1,{'+'.join(terms)})));" )
    completed = subprocess.run(
        ["gp", "-q"],
        input="\n".join(script) + "\n",
        capture_output=True,
        check=True,
        text=True,
        timeout=55,
    )
    return [int(line) for line in completed.stdout.splitlines() if line.strip()]


@app.local_entrypoint()
def main() -> None:
    actual = json.loads(ACTUAL.read_text())
    vectors = actual["production"][0]["matches"]
    packet: dict[str, object] = {
        "schema": "e1-e30-profile422-exceptional-norm-v1",
        "complete": False,
        "agreement": False,
        "actual_sha256": hashlib.sha256(ACTUAL.read_bytes()).hexdigest(),
        "vectors": vectors,
        "flint_norms": [],
        "pari_norms": [],
    }
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    try:
        packet["flint_norms"] = run_flint.remote(vectors)
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        packet["pari_norms"] = run_pari.remote(vectors)
    except BaseException:
        print(f"E30_PROFILE422_EXCEPTIONAL_NORM_INCOMPLETE result={RESULT}")
        raise
    packet["agreement"] = packet["flint_norms"] == packet["pari_norms"]
    packet["complete"] = bool(packet["agreement"] and len(packet["flint_norms"]) == len(vectors) == 2)
    packet["summary"] = {
        "maximum_norm": max(packet["flint_norms"]),
        "maximum_norm_bits": max(int(value).bit_length() for value in packet["flint_norms"]),
        "norm_at_or_above_2_250": sum(int(value) >= 2**250 for value in packet["flint_norms"]),
    }
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print("E30_PROFILE422_EXCEPTIONAL_NORM " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E30_PROFILE422_EXCEPTIONAL_NORM_AGREEMENT {packet['agreement']}")
    print(f"E30_PROFILE422_EXCEPTIONAL_NORM_RESULT {RESULT}")
