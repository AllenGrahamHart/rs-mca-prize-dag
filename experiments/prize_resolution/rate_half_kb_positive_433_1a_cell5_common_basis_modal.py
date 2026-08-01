#!/usr/bin/env python3
"""Print the localized deployed-field cell-5 common-curve basis on Modal."""

import hashlib
import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMPILER = DIRECTORY / "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
REMOTE_COMPILER = "/root/rate_half_kb_positive_433_1a_common_vieta_compiler.py"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell5-common-basis")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMPILER, REMOTE_COMPILER)
)


@app.function(image=image, cpu=1.0, memory=1024, timeout=120)
def print_basis():
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_common_vieta_compiler import compile_cell

    variables, equations, metadata = compile_cell(5, -1, -1, strip_fast=True)
    t, r, c, b = variables
    chart = equations[:3]
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
        return str(sp.Poly(expression, t, r, c, b, modulus=PRIME).as_expr()) \
            .replace("**", "^")

    chart_text = [singular(value) for value in chart]
    guard_text = singular(guard_product)
    program = f"""
ring R={PRIME},(t,r,c,b,z),dp;
option(redSB);
poly f0={chart_text[0]};
poly f1={chart_text[1]};
poly f2={chart_text[2]};
poly guard={guard_text};
ideal S=f0,f1,f2,z*guard-1;
ideal G=std(S);
print(\"BEGIN_SUMMARY\");
print(dim(G));
print(size(G));
print(vdim(G));
print(\"BEGIN_BASIS\");
G;
print(\"END_BASIS\");
quit;
"""
    header = {
        "cell": 5,
        "epsilon": [-1, -1],
        "field": PRIME,
        "chart_sha256": [
            hashlib.sha256(value.encode()).hexdigest() for value in chart_text
        ],
        "guard_sha256": hashlib.sha256(guard_text.encode()).hexdigest(),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "chart_shape": [
            {
                "degree": sp.Poly(value, *variables, modulus=PRIME).total_degree(),
                "terms": len(sp.Poly(value, *variables, modulus=PRIME).terms()),
            }
            for value in chart
        ],
        "guard_shape": {
            "degree": sp.Poly(guard_product, *variables, modulus=PRIME).total_degree(),
            "terms": len(sp.Poly(guard_product, *variables, modulus=PRIME).terms()),
        },
    }
    try:
        process = subprocess.run(
            ["Singular", "--quiet"],
            input=program,
            capture_output=True,
            text=True,
            timeout=100,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            **header,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout),
            "partial_stderr": decoded(error.stderr),
        }
    return {
        **header,
        "status": "COMPLETE" if process.returncode == 0 else "ERROR",
        "stdout": process.stdout,
        "stderr": process.stderr[-2000:],
    }


@app.local_entrypoint()
def main():
    print(json.dumps({
        "scope": (
            "one exact deployed-field localized common-curve basis; no "
            "outside, route, K3, row, or Prize conclusion"
        ),
        "result": print_basis.remote(),
    }, sort_keys=True))
