#!/usr/bin/env python3
"""Independently reconstruct cell-9 pairing-5 roots by Frobenius/gcd."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
MANIFEST = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_de_pairing5_chart_result/manifest.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_de_pairing5_"
    "frobenius_roots_result.json"
)
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell9-de-pairing5-frobenius-roots")
image = modal.Image.debian_slim(python_version="3.12").pip_install(
    "python-flint==0.8.0"
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=600, max_containers=32)
def reconstruct(profile):
    from flint import fmpz_mod_poly_ctx

    text = profile["expression"]
    if hashlib.sha256(text.encode()).hexdigest() != profile["sha256"]:
        raise RuntimeError("profile digest")
    coefficients = {}
    if text != "0":
        for term in text.split(" + "):
            if "*x^" in term:
                coefficient, degree = term.split("*x^")
                coefficient, degree = int(coefficient), int(degree)
            elif term.startswith("x^"):
                coefficient, degree = 1, int(term[2:])
            elif term.endswith("*x"):
                coefficient, degree = int(term[:-2]), 1
            elif term == "x":
                coefficient, degree = 1, 1
            else:
                coefficient, degree = int(term), 0
            if degree in coefficients:
                raise RuntimeError("duplicate polynomial degree")
            coefficients[degree] = coefficient % PRIME
    coefficients = {
        degree: value for degree, value in coefficients.items() if value
    }
    if (max(coefficients, default=-1), len(coefficients)) != (
        profile["degree"], profile["terms"]
    ):
        raise RuntimeError("profile shape")
    context = fmpz_mod_poly_ctx(PRIME)
    polynomial = context([
        coefficients.get(degree, 0)
        for degree in range(max(coefficients, default=0) + 1)
    ])
    if polynomial.is_zero():
        raise RuntimeError("zero polynomial")
    if polynomial.degree() == 0:
        roots = []
        root_degree = 0
    else:
        x = context([0, 1])
        root_part = polynomial.gcd(pow(x, PRIME, polynomial) - x)
        root_degree = int(root_part.degree())
        _, factors = root_part.factor()
        roots = []
        for factor, multiplicity in factors:
            if int(factor.degree()) != 1 or int(multiplicity) != 1:
                raise RuntimeError("Frobenius root part is not squarefree linear")
            root = -int(factor[0]) * pow(int(factor[1]), -1, PRIME) % PRIME
            roots.append(root)
        roots = sorted(roots)
        if root_degree != len(roots):
            raise RuntimeError("root degree census")
        if any(polynomial(root) != 0 for root in roots):
            raise RuntimeError("reported nonroot")
    return {
        "sha256": profile["sha256"],
        "degree": profile["degree"],
        "terms": profile["terms"],
        "frobenius_root_degree": root_degree,
        "roots": roots,
    }


@app.local_entrypoint()
def main():
    from tools.sharded_result import iter_records, verify

    counts = verify(MANIFEST)
    profiles = {}
    for row in iter_records(MANIFEST):
        for value in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                profile = value[side]
                profiles.setdefault(profile["sha256"], profile)
    rows = list(reconstruct.map(
        profiles.values(), order_outputs=True, return_exceptions=True
    ))
    failures = [repr(row) for row in rows if isinstance(row, BaseException)]
    if failures:
        raise RuntimeError(f"Frobenius root failures: {failures}")
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-cell9-de-pairing5-"
            "frobenius-roots-v1"
        ),
        "field": PRIME,
        "method": "external FLINT gcd(P,x^p-x), factor squarefree root part",
        "source_manifest_sha256": hashlib.sha256(MANIFEST.read_bytes()).hexdigest(),
        "source_sharded_counts": counts,
        "rows": sorted(rows, key=lambda row: row["sha256"]),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "profiles": len(rows),
        "roots": sum(len(row["roots"]) for row in rows),
        "maximum_degree": max(row["degree"] for row in rows),
    }, sort_keys=True))
