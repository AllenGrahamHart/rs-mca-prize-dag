#!/usr/bin/env python3
"""Reconstruct cell-11 pairings-3/4/5 norm roots independently on Modal."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
PRIMARIES = {
    str(pairing): DIRECTORY / (
        f"rate_half_kb_positive_433_1b_cell11_xi3_pairing{pairing}_"
        "template_adapter_result.json"
    )
    for pairing in (3, 4, 5)
}
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_xi3_pairings3_5_"
    "independent_roots_result.json"
)
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell11-pairings3-5-independent-roots")
image = modal.Image.debian_slim(python_version="3.12").pip_install(
    "python-flint==0.8.0"
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=900, max_containers=45)
def audit(profile):
    from flint import fmpz_mod_poly_ctx

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
    context = fmpz_mod_poly_ctx(PRIME)
    polynomial = context([
        coefficients.get(degree, 0)
        for degree in range(max(coefficients, default=0) + 1)
    ])
    require(not polynomial.is_zero(), "nonzero polynomial")
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
            require(
                int(factor.degree()) == 1 and int(multiplicity) == 1,
                "Frobenius root part is squarefree linear",
            )
            roots.append(
                -int(factor[0]) * pow(int(factor[1]), -1, PRIME) % PRIME
            )
        roots = sorted(roots)
        require(root_degree == len(roots), "root degree census")
        require(all(polynomial(root) == 0 for root in roots),
                "reported roots")
    return {
        "sha256": profile["sha256"],
        "degree": profile["degree"],
        "terms": profile["terms"],
        "frobenius_root_degree": root_degree,
        "roots": roots,
    }


@app.local_entrypoint()
def main():
    profiles = {}
    for path in PRIMARIES.values():
        payload = json.loads(path.read_text())
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
            "rate-half-kb-positive-433-1b-cell11-xi3-pairings3-5-"
            "independent-roots-v1"
        ),
        "field": PRIME,
        "source_primary_sha256": {
            pairing: hashlib.sha256(path.read_bytes()).hexdigest()
            for pairing, path in PRIMARIES.items()
        },
        "rows": sorted(rows, key=lambda row: row["sha256"]),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "profiles": len(rows),
        "roots": sum(len(row["roots"]) for row in rows),
        "maximum_degree": max(row["degree"] for row in rows),
    }, sort_keys=True))
