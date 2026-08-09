#!/usr/bin/env python3
"""Reconstruct pairing-8 norm roots independently on Modal."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
PRIMARY = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_xi3_pairing8_"
    "template_adapter_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_xi3_pairing8_"
    "independent_roots_result.json"
)
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell12-pairing8-independent-roots")
image = modal.Image.debian_slim(python_version="3.12").pip_install(
    "sympy==1.14.0"
)


@app.function(image=image, cpu=1.0, memory=4096, timeout=900, max_containers=20)
def audit(profile):
    import warnings

    import sympy as sp
    from sympy.polys.domains import ZZ
    from sympy.polys.galoistools import gf_gcd, gf_pow_mod, gf_sub
    from sympy.utilities.exceptions import SymPyDeprecationWarning

    warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)

    def require(condition, message):
        if not condition:
            raise RuntimeError(message)

    text = profile["expression"]
    require(
        hashlib.sha256(text.encode()).hexdigest() == profile["sha256"],
        "profile digest",
    )
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
            require(degree not in coefficients, "duplicate polynomial degree")
            coefficients[degree] = coefficient % PRIME
    coefficients = {
        degree: value for degree, value in coefficients.items() if value
    }
    require(
        (max(coefficients, default=-1), len(coefficients))
        == (profile["degree"], profile["terms"]),
        "profile shape",
    )
    degree = max(coefficients, default=-1)
    require(degree >= 0, "nonzero polynomial")
    polynomial = [
        coefficients.get(power, 0) for power in range(degree, -1, -1)
    ]
    if degree == 0:
        roots = []
    else:
        frobenius = gf_pow_mod([1, 0], PRIME, polynomial, PRIME, ZZ)
        root_part = gf_gcd(
            polynomial,
            gf_sub(frobenius, [1, 0], PRIME, ZZ),
            PRIME,
            ZZ,
        )
        root_degree = len(root_part) - 1
        x = sp.symbols("x")
        expression = sum(
            value * x ** (root_degree - index)
            for index, value in enumerate(root_part)
        )
        _, factors = sp.factor_list(expression, modulus=PRIME)
        roots = []
        for factor, _ in factors:
            row = sp.Poly(factor, x, modulus=PRIME)
            require(row.degree() == 1, "root part split")
            leading, constant = (
                int(value) % PRIME for value in row.all_coeffs()
            )
            roots.append(-constant * pow(leading, -1, PRIME) % PRIME)
        roots = sorted(set(roots))
    return {
        "sha256": profile["sha256"],
        "degree": profile["degree"],
        "terms": profile["terms"],
        "roots": roots,
    }


@app.local_entrypoint()
def main():
    payload = json.loads(PRIMARY.read_text())
    profiles = {}
    for row in payload["rows"]:
        for value in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                profile = value[side]
                profiles.setdefault(profile["sha256"], profile)
    rows = list(audit.map(
        profiles.values(), order_outputs=True, return_exceptions=True
    ))
    failures = [repr(row) for row in rows if isinstance(row, BaseException)]
    if failures:
        raise RuntimeError(f"independent root failures: {failures}")
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-cell12-xi3-pairing8-"
            "independent-roots-v1"
        ),
        "field": PRIME,
        "source_primary_sha256": hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
        "rows": sorted(rows, key=lambda row: row["sha256"]),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "profiles": len(rows),
        "roots": sum(len(row["roots"]) for row in rows),
        "maximum_degree": max(row["degree"] for row in rows),
    }, sort_keys=True))
