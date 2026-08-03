#!/usr/bin/env python3
"""Independently replay field-root sets in the fixed-a cell-14 chain ledger."""

import base64
import hashlib
import json
from pathlib import Path
import zlib

import modal


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_flint_profile_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_root_replay_result.json"
REMOTE_SOURCE = "/root/fixed-a-chain.json"
PRIME = 2130706433
SHARD_COUNT = 8

app = modal.App("rs-mca-positive-433-1b-cell14-fixed-a-root-replay")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(SOURCE, REMOTE_SOURCE)
)


@app.function(image=image, cpu=1.0, memory=1024, timeout=360, max_containers=8)
def replay_shard(shard_index):
    from flint import fmpz_mod_poly_ctx

    payload = json.loads(Path(REMOTE_SOURCE).read_text())
    context = fmpz_mod_poly_ctx(PRIME)
    variable = context([0, 1])

    def parse_polynomial(text):
        coefficients = {}
        for term in text.split(" + "):
            if "*" in term:
                coefficient_text, monomial = term.split("*", 1)
                coefficient = int(coefficient_text)
            elif term.startswith("r"):
                coefficient = 1
                monomial = term
            else:
                coefficient = int(term)
                monomial = ""
            if not monomial:
                exponent = 0
            elif monomial == "r":
                exponent = 1
            elif monomial.startswith("r^"):
                exponent = int(monomial[2:])
            else:
                raise ValueError(f"unexpected monomial: {monomial}")
            if exponent in coefficients:
                raise ValueError("duplicate exponent")
            coefficients[exponent] = coefficient % PRIME
        polynomial = context([
            coefficients.get(exponent, 0)
            for exponent in range(max(coefficients, default=0)+1)
        ])
        term_count = sum(
            bool(polynomial[index])
            for index in range(int(polynomial.degree())+1)
        )
        if term_count != len(coefficients):
            raise ValueError("parsed coefficient vanished or merged")
        return polynomial

    case_count = 0
    root_count = 0
    digest = hashlib.sha256()
    for row_index in range(shard_index, len(payload["rows"]), SHARD_COUNT):
        row = payload["rows"][row_index]
        text = zlib.decompress(base64.b64decode(row["outer_zlib_base64"])).decode()
        if hashlib.sha256(text.encode()).hexdigest() != row["outer_sha256"]:
            raise ValueError("stored eliminant hash mismatch")
        polynomial = parse_polynomial(text)
        if int(polynomial.degree()) != row["outer_degrees"][2]:
            raise ValueError("stored eliminant degree mismatch")
        term_count = sum(
            bool(polynomial[index])
            for index in range(int(polynomial.degree())+1)
        )
        if term_count != row["outer_terms"]:
            raise ValueError("stored eliminant term-count mismatch")
        root_gcd = polynomial.gcd(
            pow(variable, PRIME, polynomial)-variable
        )
        _, factors = root_gcd.factor()
        roots = []
        for factor, _ in factors:
            if int(factor.degree()) != 1:
                raise ValueError("field-root gcd contains a nonlinear factor")
            roots.append(
                -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
            )
        roots.sort()
        if roots != row["field_roots"]:
            raise ValueError("independent field-root set mismatch")
        digest.update(json.dumps([
            row["epsilon"], row["sigma"], row["xi_index"],
            row["pairing_index"], roots,
        ], separators=(",", ":")).encode())
        case_count += 1
        root_count += len(roots)
    return {
        "shard_index": shard_index,
        "status": "COMPLETE",
        "case_count": case_count,
        "root_count": root_count,
        "root_ledger_sha256": digest.hexdigest(),
    }


@app.local_entrypoint()
def main():
    shards = list(replay_shard.map(range(SHARD_COUNT), order_outputs=False))
    shards.sort(key=lambda row: row["shard_index"])
    payload = {
        "schema": "rate-half-kb-positive-433-1b-cell14-fixed-a-root-replay-v1",
        "field": PRIME,
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "source_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "status": "COMPLETE",
        "shard_count": SHARD_COUNT,
        "case_count": sum(row["case_count"] for row in shards),
        "root_count": sum(row["root_count"] for row in shards),
        "shards": shards,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "status": payload["status"],
        "case_count": payload["case_count"],
        "root_count": payload["root_count"],
    }, sort_keys=True))
