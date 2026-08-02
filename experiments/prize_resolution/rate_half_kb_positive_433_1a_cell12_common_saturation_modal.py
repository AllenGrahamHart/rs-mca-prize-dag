#!/usr/bin/env python3
"""Bounded deployed-field common saturations for the two cell-1 sign classes."""

import hashlib
import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMMON = DIRECTORY / "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell12_common_saturation_result.json"
REMOTE_COMMON = "/root/rate_half_kb_positive_433_1a_common_vieta_compiler.py"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell12-common-saturation")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=2)
def saturate_sign_class(signs):
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_common_vieta_compiler import compile_cell

    epsilon_1, epsilon_2 = signs
    variables, equations, metadata = compile_cell(
        1, epsilon_1, epsilon_2, strip_fast=True
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
print(dim(GC)); print(size(GC));
if ((size(GC)==1) && (GC[1]==1)) {{ print("CHART_UNIT=1"); }}
else {{ print("CHART_UNIT=0"); }}
print("END_CHART");
ideal F=f0,f1,f2,f3,f4,f5,z*guard-1;
ideal GF=std(F);
print("BEGIN_FULL");
print(dim(GF)); print(size(GF));
if ((size(GF)==1) && (GF[1]==1)) {{ print("FULL_UNIT=1"); }}
else {{ print("FULL_UNIT=0"); }}
print("END_FULL");
quit;
"""
    header = {
        "field": PRIME,
        "cell": 1,
        "epsilon": [epsilon_1, epsilon_2],
        "sign_product": epsilon_1 * epsilon_2,
        "matching": metadata["matching"],
        "equation_shape": [
            {
                "degree": sp.Poly(value, *variables, modulus=PRIME).total_degree(),
                "terms": len(sp.Poly(value, *variables, modulus=PRIME).terms()),
            }
            for value in equations
        ],
        "equation_sha256": [digest(value) for value in equation_text],
        "guard_shape": {
            "degree": sp.Poly(
                guard_product, *variables, modulus=PRIME
            ).total_degree(),
            "terms": len(sp.Poly(
                guard_product, *variables, modulus=PRIME
            ).terms()),
        },
        "guard_sha256": digest(guard_text),
        "program_sha256": digest(program),
    }
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=145,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            **header,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout)[-12000:],
            "partial_stderr": decoded(error.stderr)[-4000:],
        }
    stdout = process.stdout
    valid = process.returncode == 0 and "END_FULL" in stdout and "?" not in stdout
    return {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "chart_unit": "CHART_UNIT=1" in stdout,
        "full_unit": "FULL_UNIT=1" in stdout,
        "stdout": stdout[-12000:],
        "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main():
    signs = [(-1, -1), (-1, 1)]
    rows = list(saturate_sign_class.map(signs, return_exceptions=True))
    normalized = []
    for sign, row in zip(signs, rows):
        if isinstance(row, BaseException):
            normalized.append({
                "cell": 1,
                "epsilon": list(sign),
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            normalized.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell12-common-saturation-v1",
        "scope": (
            "Two exact deployed-field guard-saturated common ideals, one per "
            "cell-1 sign-product class. A full unit ideal deletes the common "
            "class; a survivor makes no outside, route, K3, or Prize claim."
        ),
        "rows": normalized,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {
                "epsilon": row.get("epsilon"),
                "status": row.get("status"),
                "chart_unit": row.get("chart_unit"),
                "full_unit": row.get("full_unit"),
            }
            for row in normalized
        ],
    }, sort_keys=True))
