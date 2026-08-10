#!/usr/bin/env python3
"""Bounded common saturations for repeated-BC 433-1b/O0b representatives."""

import hashlib
import itertools
import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMMON = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_vieta_compiler.py"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_saturation_result.json"
)
REMOTE_COMMON = "/root/repeat_common.py"
PRIME = 2130706433
CELL_REPRESENTATIVES = (0, 1, 3, 4, 6, 7, 9, 10, 11)

app = modal.App("rs-mca-positive-433-1b-o0b-repeat-saturation")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=36)
def saturate_representative(case):
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from repeat_common import compile_cell

    cell, epsilon_1, epsilon_2, bc_sign = case
    variables, equations, metadata = compile_cell(
        cell, epsilon_1, epsilon_2, bc_sign, strip_fast=True
    )
    t, r, c, b = variables
    labels = metadata["labels"]
    guards = [
        labels[left] - labels[right]
        for left in range(5) for right in range(left + 1, 5)
    ]
    guards.extend((
        r, t, b, c, b - 1, b + 1, c - 1, c + 1, b - c, b + c,
    ))
    guard_product = sp.prod(guards)

    def singular(expression):
        return str(
            sp.Poly(expression, t, r, c, b, modulus=PRIME).as_expr()
        ).replace("**", "^")

    equation_text = [singular(value) for value in equations]
    guard_text = singular(guard_product)
    definitions = "\n".join(
        f"poly f{index}={value};"
        for index, value in enumerate(equation_text)
    )
    program = f"""
ring R={PRIME},(z,t,r,c,b),(dp(1),dp(4));
option(redSB);
{definitions}
poly guard={guard_text};
ideal C=f0,f1,f2,z*guard-1;
ideal GC=std(C);
print("BEGIN_CHART");
print("DIM="+string(dim(GC))); print("SIZE="+string(size(GC)));
if ((size(GC)==1) && (GC[1]==1)) {{ print("CHART_UNIT=1"); }}
else {{ print("CHART_UNIT=0"); }}
print("END_CHART");
ideal F=f0,f1,f2,f3,f4,f5,z*guard-1;
ideal GF=std(F);
print("BEGIN_FULL");
print("DIM="+string(dim(GF))); print("SIZE="+string(size(GF)));
if ((size(GF)==1) && (GF[1]==1)) {{ print("FULL_UNIT=1"); }}
else {{ print("FULL_UNIT=0"); }}
print("END_FULL");
quit;
"""
    header = {
        "field": PRIME,
        "cell": cell,
        "epsilon": [epsilon_1, epsilon_2],
        "bc_sign": bc_sign,
        "singleton": metadata["singleton"],
        "matching": metadata["matching"],
        "equation_shapes": [
            {
                "degree": sp.Poly(value, *variables, modulus=PRIME).total_degree(),
                "terms": len(sp.Poly(value, *variables, modulus=PRIME).terms()),
            }
            for value in equations
        ],
        "equation_sha256": [digest(value) for value in equation_text],
        "guard_shape": {
            "degree": sp.Poly(guard_product, *variables, modulus=PRIME).total_degree(),
            "terms": len(sp.Poly(guard_product, *variables, modulus=PRIME).terms()),
        },
        "guard_sha256": digest(guard_text),
        "program_sha256": digest(program),
    }
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=150,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        stdout = decoded(error.stdout)[-8000:]
        return {
            **header,
            "status": "TIMEOUT",
            "chart_complete": "END_CHART" in stdout,
            "chart_unit": "CHART_UNIT=1" in stdout,
            "partial_stdout": stdout,
            "partial_stderr": decoded(error.stderr)[-2000:],
        }
    stdout = process.stdout
    valid = process.returncode == 0 and "END_FULL" in stdout and "?" not in stdout
    return {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "chart_complete": "END_CHART" in stdout,
        "chart_unit": "CHART_UNIT=1" in stdout,
        "full_unit": "FULL_UNIT=1" in stdout,
        "stdout": stdout[-8000:],
        "stderr": process.stderr[-2000:],
    }


@app.local_entrypoint()
def main():
    cases = tuple(itertools.product(
        CELL_REPRESENTATIVES, (-1, 1), (-1, 1), (-1, 1),
    ))
    raw = list(saturate_representative.map(
        cases, order_outputs=True, return_exceptions=True
    ))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "cell": case[0], "epsilon": list(case[1:3]),
                "bc_sign": case[3], "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-repeat-saturation-v1",
        "scope": (
            "Exact deployed-field guarded common-ideal scout on all 72 "
            "duplicate-role representatives; unit ideals prove only common "
            "class emptiness, while survivors/timeouts make no route claim."
        ),
        "source_sha256": hashlib.sha256(COMMON.read_bytes()).hexdigest(),
        "representative_cells": list(CELL_REPRESENTATIVES),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "status_counts": {
            status: sum(row["status"] == status for row in rows)
            for status in sorted({row["status"] for row in rows})
        },
        "chart_units": sum(row.get("chart_unit") is True for row in rows),
        "full_units": sum(row.get("full_unit") is True for row in rows),
        "full_survivors": sum(row.get("full_unit") is False
                              and row["status"] == "COMPLETE" for row in rows),
    }, sort_keys=True))

