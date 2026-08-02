#!/usr/bin/env python3
"""Factor the cell-9 plane-chart exceptional scales over the deployed field."""

import hashlib
import json
from pathlib import Path
import re

import modal


DIRECTORY = Path(__file__).parent
PLANE = DIRECTORY / "rate_half_kb_positive_433_1a_cell9_plane_kernel_flint_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell9_exceptional_scale_factor_result.json"
REMOTE_PLANE = "/root/cell9_plane_kernel_flint.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell9-exceptional-scale-factor")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(PLANE, REMOTE_PLANE)
)


@app.function(image=image, cpu=2.0, memory=2048, timeout=120)
def factor_scales():
    from flint import fmpz_mod_mpoly_ctx

    payload_bytes = Path(REMOTE_PLANE).read_bytes()
    payload = json.loads(payload_bytes)["result"]
    context = fmpz_mod_mpoly_ctx.get(["b", "t"], PRIME)

    def parse_polynomial(value):
        output = {}
        for raw_term in re.findall(r"[+-]?[^+-]+", value.replace(" ", "")):
            sign = 1
            term = raw_term
            if term.startswith("+"):
                term = term[1:]
            elif term.startswith("-"):
                sign = -1
                term = term[1:]
            coefficient = 1
            exponents = {"b": 0, "t": 0}
            for factor in term.split("*"):
                if factor.isdigit():
                    coefficient = coefficient * int(factor) % PRIME
                    continue
                match = re.fullmatch(r"(b|t)(?:\^(\d+))?", factor)
                if match is None:
                    raise RuntimeError(f"cannot parse factor {factor!r}")
                variable, exponent = match.groups()
                exponents[variable] += int(exponent) if exponent else 1
            key = (exponents["b"], exponents["t"])
            output[key] = (output.get(key, 0) + sign * coefficient) % PRIME
        return context.from_dict({
            key: coefficient for key, coefficient in output.items() if coefficient
        })

    inputs = {
        "r_denominator": payload["r_denominator"],
        "c_denominator": payload["c_denominator"],
        "denominator_scale": payload["denominator_scale"],
        "common_projective_scale": payload["common_projective_scale"],
        "plane_leading_coefficient": payload["plane_leading_coefficient"],
        "projected_common_scale": payload["projected_common_scale"],
    }
    rows = []
    root_owners = {}
    for name, text in inputs.items():
        polynomial = parse_polynomial(text)
        content, factors = polynomial.factor()
        reconstruction = context.constant(int(content))
        factor_rows = []
        for factor, multiplicity in factors:
            reconstruction *= factor**multiplicity
            degrees = [int(value) for value in factor.degrees()]
            row = {
                "polynomial": factor.str(), "degrees": degrees,
                "total_degree": int(factor.total_degree()),
                "terms": len(list(factor.terms())),
                "multiplicity": int(multiplicity),
            }
            if degrees == [0, 1]:
                coefficients = {
                    monomial[1]: int(coefficient) % PRIME
                    for monomial, coefficient in factor.to_dict().items()
                }
                root = (
                    -coefficients.get(0, 0)
                    * pow(coefficients[1], -1, PRIME)
                ) % PRIME
                row["root"] = root
                root_owners.setdefault(root, []).append(name)
            factor_rows.append(row)
        if reconstruction != polynomial:
            raise RuntimeError(f"factor reconstruction failed: {name}")
        rows.append({
            "name": name, "content": int(content) % PRIME,
            "degrees": [int(value) for value in polynomial.degrees()],
            "factorization": factor_rows,
        })
    return {
        "status": "COMPLETE", "field": PRIME,
        "source_plane_sha256": hashlib.sha256(payload_bytes).hexdigest(),
        "rows": rows,
        "linear_roots": [
            {"t": root, "scales": sorted(owners)}
            for root, owners in sorted(root_owners.items())
        ],
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell9-exceptional-scale-factor-v1",
        "scope": (
            "Exact deployed-field factorization of the cell-9 plane-chart "
            "exceptional scales; no common-point, outside, orbit, or Prize claim."
        ),
        "result": factor_scales.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT), "status": output["result"].get("status"),
        "linear_roots": output["result"].get("linear_roots"),
        "factor_degrees": {
            row["name"]: [
                [factor["degrees"], factor["multiplicity"]]
                for factor in row["factorization"]
            ]
            for row in output["result"].get("rows", [])
        },
    }, sort_keys=True))
