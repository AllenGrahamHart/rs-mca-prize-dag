#!/usr/bin/env python3
"""Probe the two exact cell-11 repeated-BC target curves and source lifts."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time

import modal


DIRECTORY = Path(__file__).parent
INPUT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_principal_input_result.json"
)
PROJECTION = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_principal_projection_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_curve_geometry_result.json"
)
REMOTE_INPUT = "/root/input.json"
REMOTE_PROJECTION = "/root/projection.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-o0b-cell11-curve-geometry")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(INPUT, REMOTE_INPUT)
    .add_local_file(PROJECTION, REMOTE_PROJECTION)
)


def _plane_polynomial(payload, bc_sign):
    row = next(
        item for item in payload["rows"]
        if item["epsilon"] == [-1, -1] and item["bc_sign"] == bc_sign
    )
    lines = row["elimination_output"].splitlines()
    return lines[-1]


def _parse_singular_plane(text, b, c):
    """Parse Singular's compact c5b3 notation without implicit syntax."""
    expression = 0
    for term in re.findall(r"[+-]?[^+-]+", text):
        match = re.fullmatch(r"([+-]?)(\d*)(?:c(\d*))?(?:b(\d*))?", term)
        if not match:
            raise ValueError(f"unsupported plane monomial: {term}")
        sign, coefficient, c_degree, b_degree = match.groups()
        scalar = int(coefficient) if coefficient else 1
        if sign == "-":
            scalar = -scalar
        def degree(value):
            return 0 if value is None else int(value or 1)
        expression += scalar * c ** degree(c_degree) * b ** degree(b_degree)
    return expression


@app.function(image=image, cpu=1.0, memory=3072, timeout=240, max_containers=2)
def probe(bc_sign):
    import sympy as sp

    started = time.perf_counter()
    source = json.loads(Path(REMOTE_INPUT).read_text())
    projected = json.loads(Path(REMOTE_PROJECTION).read_text())
    common = next(
        item for item in source["common_rows"]
        if item["epsilon"] == [-1, -1] and item["bc_sign"] == bc_sign
    )
    plane_text = _plane_polynomial(projected, bc_sign)

    b, c, x, y = sp.symbols("b c x y")
    plane = sp.Poly(_parse_singular_plane(plane_text, b, c), b, c,
                    modulus=PRIME)
    # SymPy does not implement multivariate finite-field factorization.  The
    # small-coefficient lift is factored over Q here; finite-field membership
    # and all source-lift statements remain certified by Singular below.
    factor_list = sp.factor_list(plane.as_expr())
    # Symmetric reduction is done exactly by a Groebner remainder rather than
    # expression-pattern substitution.
    symmetric_basis = sp.groebner(
        [x-b*c, y-b-c], b, c, x, y, modulus=PRIME, order="lex"
    )
    symmetric_remainder = symmetric_basis.reduce(plane.as_expr())[1]

    def singular(value):
        return value.replace("**", "^")

    definitions = "\n".join(
        f"poly f{index}={singular(value)};"
        for index, value in enumerate(common["equations"])
    )
    program = f"""
ring R={PRIME},(z,t,r,c,b),(dp(1),dp(4));
option(redSB);
{definitions}
poly common_guard={singular(common['guard'])};
ideal I=f0,f1,f2,f3,f4,f5,z*common_guard-1;
ideal G=std(I);
print("FULL_SIZE="+string(size(G)));
ideal ER=std(eliminate(G,z*t));
print("R_BEGIN"); print(ER); print("R_END");
ideal ET=std(eliminate(G,z*r));
print("T_BEGIN"); print(ET); print("T_END");
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=210,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "bc_sign": bc_sign, "status": "TIMEOUT",
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
            "partial_stdout": (error.stdout or "")[-12000:],
            "partial_stderr": (error.stderr or "")[-2000:],
            "seconds": time.perf_counter() - started,
        }

    def between(left, right):
        match = re.search(rf"{left}\n(.*?)\n{right}", process.stdout, re.DOTALL)
        return match.group(1).strip() if match else None

    bases = {
        "source_r": between("R_BEGIN", "R_END"),
        "source_t": between("T_BEGIN", "T_END"),
    }
    valid = (
        process.returncode == 0 and "END" in process.stdout
        and "?" not in process.stdout and all(bases.values())
    )
    factors = [
        {"factor": str(factor), "multiplicity": multiplicity}
        for factor, multiplicity in factor_list[1]
    ]
    return {
        "bc_sign": bc_sign,
        "status": "COMPLETE" if valid else "ERROR",
        "plane_polynomial": str(plane.as_expr()),
        "plane_total_degree": plane.total_degree(),
        "factor_unit": int(factor_list[0]),
        "factors_over_q": factors,
        "symmetric_xy": str(sp.Poly(
            symmetric_remainder, x, y, modulus=PRIME
        ).as_expr()),
        "basis_sizes": {
            key: len(value.splitlines()) if value else None
            for key, value in bases.items()
        },
        "full_basis_size": int(re.search(
            r"FULL_SIZE=(\d+)", process.stdout
        ).group(1)) if "FULL_SIZE=" in process.stdout else None,
        "bases": bases,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-2000:],
        "seconds": time.perf_counter() - started,
    }


@app.local_entrypoint()
def main():
    cases = (-1, 1)
    raw = list(probe.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "bc_sign": case, "status": "REMOTE_ERROR", "error": repr(row)
            })
        else:
            rows.append(row)
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-o0b-common-repeat-"
            "cell11-curve-geometry-v1"
        ),
        "scope": (
            "Exact plane-curve factorization, symmetric reduction, and staged "
            "source-coordinate elimination for representative cell-11 rows."
        ),
        "source_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        "projection_sha256": hashlib.sha256(PROJECTION.read_bytes()).hexdigest(),
        "status_counts": dict(sorted(Counter(
            row["status"] for row in rows
        ).items())),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "status_counts": output["status_counts"],
        "rows": [{
            "bc_sign": row["bc_sign"], "status": row["status"],
            "factors_over_q": row.get("factors_over_q"),
            "symmetric_xy": row.get("symmetric_xy"),
            "basis_sizes": row.get("basis_sizes"),
            "seconds": row.get("seconds"),
        } for row in rows],
    }, sort_keys=True))
