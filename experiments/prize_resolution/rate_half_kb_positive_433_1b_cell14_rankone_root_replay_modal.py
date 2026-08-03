#!/usr/bin/env python3
"""Independently replay all field-root gcds in the cell-14 rank-one ledger."""

import base64
import hashlib
import json
from pathlib import Path
import zlib

import modal


DIRECTORY = Path(__file__).parent
PRIME = 2130706433
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_rankone_root_replay_result.json"
SHARDS = (
    ("simple", "rate_half_kb_positive_433_1b_cell14_rankone_simple_full_result.json",
     "resultant_zlib_base64", "resultant_sha256", "r"),
    ("df_chain", "rate_half_kb_positive_433_1b_cell14_rankone_df_chain_full_result.json",
     "outer_zlib_base64", "outer_sha256", "r"),
    ("ef_chain", "rate_half_kb_positive_433_1b_cell14_rankone_ef_chain_full_result.json",
     "outer_zlib_base64", "outer_sha256", "r"),
    ("bf_targetfree", "rate_half_kb_positive_433_1b_cell14_rankone_bf_targetfree_full_result.json",
     "polynomial_zlib_base64", "polynomial_sha256", "x"),
    ("cf_targetfree", "rate_half_kb_positive_433_1b_cell14_rankone_cf_targetfree_full_result.json",
     "polynomial_zlib_base64", "polynomial_sha256", "x"),
)
REMOTE_PREFIX = "/root/"

app = modal.App("rs-mca-positive-433-1b-cell14-rankone-root-replay")
image = modal.Image.debian_slim(python_version="3.12").pip_install("python-flint==0.8.0")
for _, filename, _, _, _ in SHARDS:
    image = image.add_local_file(DIRECTORY / filename, REMOTE_PREFIX+filename)


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


@app.function(image=image, cpu=1.0, memory=1024, timeout=360, max_containers=5)
def replay_shard(specification):
    from flint import fmpz_mod_poly_ctx

    name, filename, blob_key, hash_key, variable_name = specification
    path = Path(REMOTE_PREFIX+filename)
    payload = json.loads(path.read_text())
    context = fmpz_mod_poly_ctx(PRIME)
    variable = context([0, 1])

    def parse_polynomial(text):
        coefficients = {}
        for term in text.split(" + "):
            if "*" in term:
                coefficient_text, monomial = term.split("*", 1)
                coefficient = int(coefficient_text)
            elif term.startswith(variable_name):
                coefficient = 1
                monomial = term
            else:
                coefficient = int(term)
                monomial = ""
            if not monomial:
                exponent = 0
            elif monomial == variable_name:
                exponent = 1
            else:
                prefix = variable_name+"^"
                if not monomial.startswith(prefix):
                    raise ValueError(f"unexpected monomial: {monomial}")
                exponent = int(monomial[len(prefix):])
            if exponent in coefficients:
                raise ValueError("duplicate exponent")
            coefficients[exponent] = coefficient % PRIME
        polynomial = context([
            coefficients.get(index, 0)
            for index in range(max(coefficients, default=0)+1)
        ])
        if sum(bool(polynomial[index]) for index in range(int(polynomial.degree())+1)) != len(coefficients):
            raise ValueError("zero or merged parsed coefficient")
        return polynomial

    rows = []
    for source in payload["rows"]:
        text = zlib.decompress(base64.b64decode(source[blob_key])).decode()
        if hashlib.sha256(text.encode()).hexdigest() != source[hash_key]:
            raise ValueError("stored eliminant hash mismatch")
        polynomial = parse_polynomial(text)
        if name == "simple":
            claimed_degree = max(source["resultant_degrees"])
            claimed_terms = source["resultant_terms"]
        elif name.endswith("chain"):
            claimed_degree = max(source["outer_degrees"])
            claimed_terms = source["outer_terms"]
        else:
            claimed_degree = source["polynomial_degree"]
            claimed_terms = source["polynomial_terms"]
        if int(polynomial.degree()) != claimed_degree:
            raise ValueError("eliminant degree mismatch")
        term_count = sum(
            bool(polynomial[index]) for index in range(int(polynomial.degree())+1)
        )
        if term_count != claimed_terms:
            raise ValueError("eliminant term-count mismatch")

        field_gcd = polynomial.gcd(pow(variable, PRIME, polynomial)-variable)
        _, factors = field_gcd.factor()
        roots = []
        for factor, _ in factors:
            if int(factor.degree()) != 1:
                raise ValueError("field-root gcd contains nonlinear factor")
            roots.append(
                -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
            )
        roots.sort()
        if roots != source["field_roots"]:
            raise ValueError("independent field-root set mismatch")
        if int(field_gcd.degree()) != source["field_root_gcd_degree"]:
            raise ValueError("independent field-root degree mismatch")
        case = [
            *source["epsilon"], *source["sigma"],
            source["xi_index"], source["pairing_index"],
        ]
        rows.append({
            "case": case,
            "eliminant_sha256": source[hash_key],
            "field_gcd_sha256": hashlib.sha256(field_gcd.str().encode()).hexdigest(),
            "field_root_count": len(roots),
            "field_roots_sha256": hashlib.sha256(
                json.dumps(roots, separators=(",", ":")).encode()
            ).hexdigest(),
            "status": "PASS",
        })
    rows.sort(key=lambda row: row["case"])
    return {
        "name": name,
        "file": filename,
        "file_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "case_count": len(rows),
        "field_root_count": sum(row["field_root_count"] for row in rows),
        "pass_count": sum(row["status"] == "PASS" for row in rows),
        "rows": rows,
    }


@app.local_entrypoint()
def main():
    rows = list(replay_shard.map(SHARDS, order_outputs=False))
    rows.sort(key=lambda row: row["name"])
    payload = {
        "schema": "rate-half-kb-positive-433-1b-cell14-rankone-root-replay-v1",
        "scope": "Independent FLINT replay of every stored eliminant field-root gcd.",
        "field": PRIME,
        "source_script_sha256": sha256_file(Path(__file__)),
        "case_count": sum(row["case_count"] for row in rows),
        "field_root_count": sum(row["field_root_count"] for row in rows),
        "pass_count": sum(row["pass_count"] for row in rows),
        "shards": rows,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "case_count": payload["case_count"],
        "field_root_count": payload["field_root_count"],
        "pass_count": payload["pass_count"],
    }, sort_keys=True))
