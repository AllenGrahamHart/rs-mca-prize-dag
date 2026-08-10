#!/usr/bin/env python3
"""Independently certify every base-field root of the cell-11 endpoint eliminants."""

import hashlib
import json
from pathlib import Path
import re

import modal


DIRECTORY = Path(__file__).parent
PILOT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_endpoint_compatibility_pilot_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_endpoint_eliminant_frobenius_roots_result.json"
)
REMOTE_PILOT = "/root/pilot.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell11-endpoint-frobenius-roots")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(PILOT, REMOTE_PILOT)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=8)
def audit(row):
    from sympy.polys.domains import ZZ
    from sympy.polys.galoistools import gf_gcd, gf_pow_mod, gf_sub

    def require(condition, message):
        if not condition:
            raise RuntimeError(message)

    text = row["r_elimination"]
    require(text.startswith("Er[1]="), "single elimination generator")
    expression = text.split("=", 1)[1]
    coefficients = {}
    for term in re.findall(r"[+-]?[^+-]+", expression):
        sign = -1 if term.startswith("-") else 1
        unsigned = term.lstrip("+-")
        match = re.fullmatch(r"(?:(\d+))?r(?:(\d+))?|(?:(\d+))", unsigned)
        require(match is not None, f"unparsed term: {term}")
        if match.group(3) is not None:
            coefficient = sign * int(match.group(3))
            degree = 0
        else:
            coefficient = sign * int(match.group(1) or "1")
            degree = int(match.group(2) or "1")
        require(degree not in coefficients, "duplicate degree")
        coefficients[degree] = coefficient % PRIME
    degree = max(coefficients)
    expected_degree = 32
    require(degree == expected_degree, "endpoint eliminant degree")
    polynomial = [
        coefficients.get(power, 0) for power in range(degree, -1, -1)
    ]
    require(polynomial[0] == 1, "monic eliminant")
    x_to_p = gf_pow_mod([1, 0], PRIME, polynomial, PRIME, ZZ)
    root_gcd = gf_gcd(
        polynomial,
        gf_sub(x_to_p, [1, 0], PRIME, ZZ),
        PRIME,
        ZZ,
    )
    root_count = len(root_gcd) - 1
    roots = (
        [(-int(root_gcd[1]) * pow(int(root_gcd[0]), -1, PRIME)) % PRIME]
        if root_count == 1 else []
    )
    return {
        "epsilon": row["epsilon"],
        "endpoint": row["endpoint"],
        "degree": degree,
        "terms": len(coefficients),
        "eliminant_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "frobenius_remainder_sha256": hashlib.sha256(
            json.dumps(x_to_p, separators=(",", ":")).encode()
        ).hexdigest(),
        "root_gcd": [int(value) for value in root_gcd],
        "root_count": root_count,
        "roots": roots,
    }


@app.local_entrypoint()
def main():
    payload = json.loads(PILOT.read_text())
    rows = list(audit.map(
        payload["rows"], order_outputs=True, return_exceptions=True
    ))
    failures = [repr(row) for row in rows if isinstance(row, BaseException)]
    if failures:
        raise RuntimeError(f"independent rootlessness failures: {failures}")
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-cell11-endpoint-"
            "eliminant-frobenius-roots-v1"
        ),
        "field": PRIME,
        "method": "independent galoistools gcd(E(r), r^p-r)",
        "source_pilot_sha256": hashlib.sha256(PILOT.read_bytes()).hexdigest(),
        "complete": len(rows) == 8 and all(
            row["root_count"] == 1 and len(row["roots"]) == 1
            for row in rows
        ),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": len(rows),
        "degrees": sorted({row["degree"] for row in rows}),
        "roots": sum(row["root_count"] for row in rows),
        "complete": output["complete"],
    }, sort_keys=True))
