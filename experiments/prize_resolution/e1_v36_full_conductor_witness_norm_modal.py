#!/usr/bin/env python3
"""Measure and primality-test the certified full-conductor V=36 witness."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


app = modal.App("e1-v36-full-conductor-witness-norm")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")
COEFFICIENTS = ((0, 2), (16, -2), (32, -1), (48, 1), (65, 1), (80, -1), (96, -2))


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=1)
def measure() -> dict[str, object]:
    import subprocess
    import time

    from flint import fmpz, fmpz_poly

    started = time.monotonic()
    dense = [0] * 128
    for exponent, coefficient in COEFFICIENTS:
        dense[exponent] = coefficient
    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    flint_norm = abs(int(cyclotomic.resultant(fmpz_poly(dense))))
    valuation = (flint_norm & -flint_norm).bit_length() - 1
    odd_part = flint_norm >> valuation
    flint_prime = bool(fmpz(odd_part).is_prime())

    polynomial = "+".join(
        f"({coefficient})*x^{exponent}" for exponent, coefficient in COEFFICIENTS
    )
    pari = subprocess.run(
        ["gp", "-q"],
        input=(
            f"n=abs(polresultant(x^128+1,{polynomial}));"
            "v=valuation(n,2);o=n/2^v;print(n);print(v);print(isprime(o));\n"
        ),
        capture_output=True,
        check=True,
        text=True,
        timeout=55,
    )
    lines = [line.strip() for line in pari.stdout.splitlines() if line.strip()]
    pari_norm, pari_valuation, pari_prime = int(lines[0]), int(lines[1]), int(lines[2])
    return {
        "agreement": (
            flint_norm == pari_norm
            and valuation == pari_valuation
            and flint_prime == bool(pari_prime)
        ),
        "coefficients": COEFFICIENTS,
        "norm": flint_norm,
        "norm_bits": flint_norm.bit_length(),
        "valuation": valuation,
        "odd_part": odd_part,
        "odd_part_bits": odd_part.bit_length(),
        "odd_part_mod_256": odd_part % 256,
        "odd_part_above_2_250": odd_part > 2**250,
        "odd_part_below_2_256": odd_part < 2**256,
        "odd_part_is_prime": flint_prime,
        "worker_seconds": time.monotonic() - started,
    }


@app.local_entrypoint()
def main() -> None:
    payload = {
        "schema": "e1-v36-full-conductor-witness-norm-v1",
        "complete": False,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    try:
        payload.update(measure.remote())
        payload["complete"] = True
    except Exception as error:
        payload["error"] = f"{type(error).__name__}: {error}"
    print("E1_V36_FULL_CONDUCTOR_WITNESS_NORM " + json.dumps(payload, sort_keys=True))
