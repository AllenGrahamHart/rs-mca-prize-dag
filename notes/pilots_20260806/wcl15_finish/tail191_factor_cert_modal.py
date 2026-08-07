#!/usr/bin/env python3
"""Independently certify the final WCL `(1,5)` tail-191 factorization."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import modal


SOURCE = Path(__file__).with_name("tail191_cado_portable_v2_result.json")
SOURCE_SHA256 = "c093d5e05aea1e2b2851042e550f89cf44f093c8b1714c80780efd27b72ec608"
REMOTE_SOURCE = "/input/tail191_cado_result.json"
OUTPUT = Path(__file__).with_name("tail191_factor_cert.json")
NORM_TEXT = (
    "648504938724625892617537595827566622528651020454874372151735040370"
    "465231483079169"
)
EXPECTED_FACTORS = [
    2618025003265620701077592958097921,
    247707694890502006805474333259382717013127180289,
]
EXPECTED_RESULT_DIGEST = (
    "73b759d20b4d03bf05b8b71b3c629eea14849f5631752d66ccef3d1fe61bfd43"
)
CADO_IMAGE = (
    "registry.gitlab.inria.fr/cado-nfs/cado-nfs/factoring-full@"
    "sha256:d89bc19b6a1a9dd00b8c95cd97d60faca73ecbfc3ea71b5e20ec0403b1b3fc10"
)
CAP = 2**256
AMBIENT_V2 = 41

app = modal.App("rs-mca-wcl15-tail191-independent-factor-cert")
image = (
    modal.Image.debian_slim()
    .pip_install("python-flint")
    .add_local_file(str(SOURCE), REMOTE_SOURCE, copy=True)
)


def valuation_two(value: int) -> int:
    return (value & -value).bit_length() - 1


@app.function(image=image, cpu=1, memory=1024, timeout=120)
def certify() -> dict[str, object]:
    import time

    from flint import fmpz

    started = time.monotonic()
    raw = Path(REMOTE_SOURCE).read_bytes()
    source_sha256 = hashlib.sha256(raw).hexdigest()
    if source_sha256 != SOURCE_SHA256:
        raise AssertionError(("source SHA-256", source_sha256))
    packet = json.loads(raw)
    if (
        packet.get("schema") != "wcl15-tail191-cado-v1"
        or packet.get("status") != "DIVISOR_FOUND"
        or packet.get("return_code") != 0
        or packet.get("timed_out")
        or packet.get("forced_kill")
        or packet.get("norm") != NORM_TEXT
        or packet.get("result_digest") != EXPECTED_RESULT_DIGEST
        or packet.get("cado_image") != CADO_IMAGE
    ):
        raise AssertionError("CADO packet custody")

    factors = sorted(int(value) for value in packet["proper_divisors"])
    if factors != sorted(EXPECTED_FACTORS) or len(set(factors)) != 2:
        raise AssertionError(("factor custody", factors))
    norm = int(NORM_TEXT)
    if math.prod(factors) != norm:
        raise AssertionError("factor product")

    primality = [bool(fmpz(factor).is_prime()) for factor in factors]
    if primality != [True, True]:
        raise AssertionError(("composite returned factor", primality))
    rows = [
        {
            "prime": str(factor),
            "bits": factor.bit_length(),
            "v2_prime_minus_1": valuation_two(factor - 1),
            "below_2_256": factor < CAP,
            "official_gate": factor < CAP
            and valuation_two(factor - 1) >= AMBIENT_V2,
        }
        for factor in factors
    ]
    if [row["bits"] for row in rows] != [112, 158]:
        raise AssertionError(("factor bit lengths", rows))
    if [row["v2_prime_minus_1"] for row in rows] != [9, 12]:
        raise AssertionError(("factor valuations", rows))
    if any(row["official_gate"] for row in rows):
        raise AssertionError(("official-gate factor", rows))

    result = {
        "schema": "wcl15-tail191-independent-factor-cert-v1",
        "status": "COMPLETE",
        "source_sha256": source_sha256,
        "norm": NORM_TEXT,
        "norm_bits": norm.bit_length(),
        "factors": rows,
        "factor_product_exact": True,
        "primality_checks": len(factors),
        "maximum_v2_prime_minus_1": max(
            int(row["v2_prime_minus_1"]) for row in rows
        ),
        "high_gate_factors": [row for row in rows if row["official_gate"]],
        "seconds": round(time.monotonic() - started, 6),
    }
    result["certificate_digest"] = hashlib.sha256(
        json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return result


@app.local_entrypoint()
def main() -> None:
    result = certify.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("WCL15_TAIL191_FACTOR_CERT " + json.dumps(result, sort_keys=True))

