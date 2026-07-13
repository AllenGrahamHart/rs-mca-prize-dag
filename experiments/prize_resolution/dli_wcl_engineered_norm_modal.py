#!/usr/bin/env python3
"""Factor the banked six-term DLI norm and audit ambient splitting.

The round-5 witness uses

    1 - z^33 + z^40 - z^136 - z^143 + z^145,  z^256 = -1.

It supplies a terminal ``n'=512`` relation.  WCL-ZONE needs the same prime to
host the full production tower, whose top generated subgroup has order
``2^41``.  This Modal probe computes the exact cyclotomic norm, factors it,
and reports ``v_2(p-1)`` for every prime factor.  The norm is written locally
before factorization, so a worker timeout leaves a useful partial artifact.
"""

from __future__ import annotations

import json
import math
import re
import subprocess
from pathlib import Path

import modal


ORDER = 512
SUPPORT = ((0, 1), (33, -1), (40, 1), (136, -1), (143, -1), (145, 1))
OUTPUT = Path(__file__).with_name("dli_wcl_engineered_norm_result.json")

app = modal.App("rs-mca-dli-wcl-engineered-norm")
flint_image = modal.Image.debian_slim().pip_install("python-flint")
pari_image = modal.Image.debian_slim().apt_install("pari-gp")


def valuation_two(value: int) -> int:
    exponent = 0
    while value % 2 == 0:
        value //= 2
        exponent += 1
    return exponent


def parse_factor_output(output: str, integer: int) -> list[list[object]]:
    factors: list[list[object]] = []
    for line in output.splitlines():
        match = re.fullmatch(r"\s*(\d+)\s*:\s*(\d+)\s*", line)
        if match:
            prime, exponent = map(int, match.groups())
            factors.append([str(prime), exponent])
    product = 1
    for prime, exponent in factors:
        product *= int(prime) ** int(exponent)
    if not factors or product != integer:
        raise AssertionError("PARI factorization does not reconstruct integer")
    return factors


@app.function(image=flint_image, cpu=1, memory=1024, timeout=60)
def compute_norm() -> dict[str, object]:
    from flint import fmpz_poly

    coefficients = [0] * (ORDER // 2)
    for exponent, sign in SUPPORT:
        coefficients[exponent] = sign
    cyclotomic = fmpz_poly([1] + [0] * (ORDER // 2 - 1) + [1])
    polynomial = fmpz_poly(coefficients)
    norm = abs(int(cyclotomic.resultant(polynomial)))
    if norm == 0:
        raise AssertionError("six-term norm vanished")
    return {
        "order": ORDER,
        "support": [list(term) for term in SUPPORT],
        "norm": str(norm),
        "norm_bits": norm.bit_length(),
    }


@app.function(image=pari_image, cpu=2, memory=2048, timeout=180)
def factor_integer(integer_text: str) -> list[list[object]]:
    program = (
        f"n={integer_text};f=factor(n);"
        'for(i=1,matsize(f)[1],print(f[i,1]," : ",f[i,2]));quit()\n'
    )
    completed = subprocess.run(
        ["gp", "-q"],
        input=program,
        text=True,
        capture_output=True,
        timeout=170,
        check=True,
    )
    return parse_factor_output(completed.stdout, int(integer_text))


@app.function(image=pari_image, cpu=2, memory=2048, timeout=180)
def pocklington_certificate(prime_text: str) -> dict[str, object]:
    nodes: dict[str, dict[str, object]] = {}

    def factor(value: int) -> list[list[object]]:
        program = (
            f"n={value};f=factor(n);"
            'for(i=1,matsize(f)[1],print(f[i,1]," : ",f[i,2]));quit()\n'
        )
        completed = subprocess.run(
            ["gp", "-q"],
            input=program,
            text=True,
            capture_output=True,
            timeout=60,
            check=True,
        )
        return parse_factor_output(completed.stdout, value)

    def certify(candidate: int) -> None:
        key = str(candidate)
        if key in nodes:
            return
        if candidate < 10_000:
            if candidate < 2 or any(candidate % d == 0 for d in range(2, math.isqrt(candidate) + 1)):
                raise AssertionError(f"nonprime leaf {candidate}")
            nodes[key] = {"method": "trial"}
            return

        factors = factor(candidate - 1)
        for factor_text, _ in factors:
            certify(int(factor_text))
        witnesses: dict[str, int] = {}
        for factor_text, _ in factors:
            divisor = int(factor_text)
            for base in range(2, 100_000):
                if (
                    pow(base, candidate - 1, candidate) == 1
                    and math.gcd(pow(base, (candidate - 1) // divisor, candidate) - 1, candidate) == 1
                ):
                    witnesses[factor_text] = base
                    break
            else:
                raise AssertionError((candidate, divisor, "no Pocklington witness"))
        nodes[key] = {
            "method": "pocklington",
            "minus_one_factors": factors,
            "witnesses": witnesses,
        }

    root = int(prime_text)
    certify(root)
    return {"root": prime_text, "nodes": nodes}


@app.local_entrypoint()
def main() -> None:
    record = compute_norm.remote()
    OUTPUT.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print("DLI_WCL_NORM_PARTIAL " + json.dumps(record, sort_keys=True), flush=True)
    raw_factors = factor_integer.remote(str(record["norm"]))
    record["factors"] = [
        {
            "prime": prime_text,
            "exponent": exponent,
            "bits": int(prime_text).bit_length(),
            "v2_prime_minus_1": valuation_two(int(prime_text) - 1),
            "terminal_split_512": (int(prime_text) - 1) % 512 == 0,
            "ambient_split_2^41": (int(prime_text) - 1) % 2**41 == 0,
        }
        for prime_text, exponent in raw_factors
    ]
    record["ambient_factor_count"] = sum(
        int(factor["ambient_split_2^41"]) for factor in record["factors"]
    )
    large_factor = max(int(factor["prime"]) for factor in record["factors"])
    record["large_factor_minus_one_factors"] = factor_integer.remote(
        str(large_factor - 1)
    )
    record["large_factor_pocklington"] = pocklington_certificate.remote(
        str(large_factor)
    )
    OUTPUT.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print("DLI_WCL_NORM_RESULT " + json.dumps(record, sort_keys=True))
