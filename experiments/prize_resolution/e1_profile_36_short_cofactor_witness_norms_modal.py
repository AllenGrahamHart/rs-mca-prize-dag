#!/usr/bin/env python3
"""Measure exact norms of the shortest-window profile-(3,6) witnesses."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


app = modal.App("e1-profile-36-short-cofactor-witness-norms")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")

B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
P_MAX = (B_PRIZE + 1) * 2**128 - 1

WITNESSES = (
    {
        "name": "mu2_E8",
        "cofactor": 1028,
        "expected_mu": 2,
        "expected_energy": 8,
        "state": ((25, 1), (35, 2), (45, -2), (55, 1), (79, 1),
                  (89, 2), (99, 1), (119, -1), (123, -1)),
    },
    {
        "name": "mu10_E13",
        "cofactor": 1024,
        "expected_mu": 10,
        "expected_energy": 13,
        "state": ((9, 1), (35, 2), (37, -2), (61, -1), (85, -1),
                  (87, 1), (89, 1), (111, -1), (113, -2)),
    },
)


def root_multiplicity(state: tuple[tuple[int, int], ...]) -> int:
    singleton_exponents = [exponent for exponent, value in state if abs(value) == 1]
    assert len(singleton_exponents) == 6
    for derivative in range(128):
        parity = sum(
            (derivative & ~exponent) == 0 for exponent in singleton_exponents
        ) % 2
        if parity:
            return derivative
    return 128


def energy(state: tuple[tuple[int, int], ...]) -> int:
    coefficients = dict(state)
    autocorrelation = [0] * 64
    support = sorted(coefficients)
    for left_index, left in enumerate(support):
        for right in support[left_index + 1 :]:
            delta = right - left
            product = coefficients[left] * coefficients[right]
            if delta < 64:
                autocorrelation[delta] += product
            elif delta > 64:
                autocorrelation[128 - delta] -= product
    return sum(value * value for value in autocorrelation[1:])


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=1)
def measure() -> list[dict[str, object]]:
    import subprocess
    import time

    from flint import fmpz, fmpz_poly

    started = time.monotonic()
    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    rows = []
    for witness in WITNESSES:
        state = witness["state"]
        mu = root_multiplicity(state)
        measured_energy = energy(state)
        assert mu == witness["expected_mu"]
        assert measured_energy == witness["expected_energy"]

        dense = [0] * 128
        for exponent, coefficient in state:
            dense[exponent] = coefficient
        flint_norm = abs(int(cyclotomic.resultant(fmpz_poly(dense))))

        polynomial = "+".join(
            f"({coefficient})*x^{exponent}" for exponent, coefficient in state
        )
        pari = subprocess.run(
            ["gp", "-q"],
            input=f"print(abs(polresultant(x^128+1,{polynomial})));\n",
            capture_output=True,
            check=True,
            text=True,
            timeout=50,
        )
        pari_norm = int(pari.stdout.strip())
        assert pari_norm == flint_norm

        valuation = (flint_norm & -flint_norm).bit_length() - 1
        cofactor = int(witness["cofactor"])
        divisible = flint_norm % cofactor == 0
        quotient = flint_norm // cofactor if divisible else None
        rows.append(
            {
                "name": witness["name"],
                "state": state,
                "mu": mu,
                "energy": measured_energy,
                "variance": 2 * measured_energy,
                "cofactor": cofactor,
                "norm": flint_norm,
                "norm_bits": flint_norm.bit_length(),
                "valuation": valuation,
                "norm_mod_257": flint_norm % 257,
                "divisible_by_cofactor": divisible,
                "quotient": quotient,
                "quotient_in_prize_interval": (
                    quotient is not None and P_MIN <= quotient <= P_MAX
                ),
                "quotient_is_prime": (
                    bool(fmpz(quotient).is_prime()) if quotient is not None else False
                ),
                "flint_pari_agree": flint_norm == pari_norm,
            }
        )
    elapsed = time.monotonic() - started
    for row in rows:
        row["batch_worker_seconds"] = elapsed
    return rows


@app.local_entrypoint()
def main() -> None:
    payload = {
        "schema": "e1-profile-36-short-cofactor-witness-norms-v1",
        "complete": False,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    try:
        payload["rows"] = measure.remote()
        payload["complete"] = True
    except Exception as error:
        payload["error"] = f"{type(error).__name__}: {error}"
    print("E1_PROFILE_36_SHORT_COFACTOR_WITNESS_NORMS " + json.dumps(payload, sort_keys=True))
