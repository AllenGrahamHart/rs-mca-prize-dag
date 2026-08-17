#!/usr/bin/env python3
"""Collect every base-field root of the FFF generic-basis denominators."""

import hashlib
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_result.json"
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_fff_generic_t_denominator_roots_result.json"
)
REMOTE_SOURCE = "/root/generic.json"
PRIME = 2130706433
SOURCE_SHA256 = "c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-denominator-roots")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(SOURCE, REMOTE_SOURCE)
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


@app.function(image=image, cpu=1.0, memory=1536, timeout=180)
def collect_roots():
    from flint import fmpz_mod_poly_ctx

    started = time.perf_counter()
    source = json.loads(Path(REMOTE_SOURCE).read_text())
    denominators = source["row"]["unique_denominators"]
    require(len(denominators) == 44, "denominator count")
    context = fmpz_mod_poly_ctx(PRIME)
    variable = context([0, 1])

    def coefficients(polynomial):
        if polynomial.is_zero():
            return []
        return [
            int(polynomial[index])
            for index in range(int(polynomial.degree()) + 1)
        ]

    def monic(polynomial):
        if polynomial.is_zero():
            return polynomial
        leading = int(polynomial[int(polynomial.degree())])
        return polynomial * pow(leading, -1, PRIME)

    def field_part(polynomial):
        if int(polynomial.degree()) == 0:
            return context([1]), []
        root_part = monic(
            polynomial.gcd(pow(variable, PRIME, polynomial) - variable)
        )
        _, factors = root_part.factor()
        roots = []
        for factor, multiplicity in factors:
            require(multiplicity == 1, "square-free Frobenius gcd")
            require(int(factor.degree()) == 1, "nonlinear field factor")
            roots.append(
                -int(factor[0]) * pow(int(factor[1]), -1, PRIME) % PRIME
            )
        roots = sorted(set(roots))
        reconstructed = context([1])
        for root in roots:
            reconstructed *= variable - root
        require(monic(reconstructed) == root_part, "linear reconstruction")
        return root_part, roots

    lcm = context([1])
    rows = []
    for index, values in enumerate(denominators):
        polynomial = context(values)
        require(not polynomial.is_zero(), "zero denominator")
        lcm = monic(lcm.lcm(polynomial))
        root_part, roots = field_part(polynomial)
        rows.append({
            "index": index,
            "denominator_sha256": hashlib.sha256(
                json.dumps(values, separators=(",", ":")).encode()
            ).hexdigest(),
            "degree": int(polynomial.degree()),
            "field_root_polynomial": coefficients(root_part),
            "roots": roots,
        })

    combined_part, combined_roots = field_part(lcm)
    require(
        combined_roots == sorted({root for row in rows for root in row["roots"]}),
        "per-denominator root union",
    )
    rows_text = json.dumps(rows, separators=(",", ":"), sort_keys=True)
    return {
        "status": "COMPLETE",
        "method": "FLINT gcd(D,t^p-t), linear factorization, LCM union check",
        "denominator_count": len(denominators),
        "raw_degree_sum": sum(len(values) - 1 for values in denominators),
        "lcm_degree": int(lcm.degree()),
        "lcm_sha256": hashlib.sha256(
            json.dumps(coefficients(lcm), separators=(",", ":")).encode()
        ).hexdigest(),
        "field_root_polynomial": coefficients(combined_part),
        "roots": combined_roots,
        "root_count": len(combined_roots),
        "rows": rows,
        "rows_sha256": hashlib.sha256(rows_text.encode()).hexdigest(),
        "elapsed_seconds": time.perf_counter() - started,
    }


def write_checkpoint(row, collection_complete):
    RESULT.write_text(json.dumps({
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-denominator-roots-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-denominator-roots",
        "collection_complete": collection_complete,
        "field": PRIME,
        "source_sha256": SOURCE_SHA256,
        "launcher_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "row": row,
    }, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "source custody")
    write_checkpoint(None, False)
    try:
        row = collect_roots.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] == "COMPLETE"
    write_checkpoint(row, complete)
    print(json.dumps({
        "result": str(RESULT),
        "status": row["status"],
        "lcm_degree": row.get("lcm_degree"),
        "root_count": row.get("root_count"),
        "roots": row.get("roots"),
    }, sort_keys=True))
