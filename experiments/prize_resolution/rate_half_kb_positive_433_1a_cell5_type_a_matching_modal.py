#!/usr/bin/env python3
"""Bounded exact target-free type-A matching pilot for positive cell 5."""

import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMMON = DIRECTORY / "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
REMOTE_COMMON = "/root/rate_half_kb_positive_433_1a_common_vieta_compiler.py"
REMOTE_KERNEL = "/root/rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell5-type-a-matching")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=1.0, memory=1536, timeout=120)
def test_matching():
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_cell5_sparse_edge_probe import (
        sparse_product_kernel,
    )
    from rate_half_kb_positive_433_1a_common_vieta_compiler import compile_cell

    common_variables, equations, _ = compile_cell(
        5, -1, -1, strip_fast=True
    )
    t, r, c, b = common_variables
    u, v, w = sp.symbols("u v w")
    variables = (u, v, w, t, r, c, b)
    a2, a0, _, _, _ = sparse_product_kernel()
    delta = t**2 * (t**2 - 1)
    beta = -t * (1 + b) * sum(
        a2[index] * t ** (2 * index) for index in range(3)
    )

    def evaluate(coefficients, value):
        return sum(coefficients[index] * value**index for index in range(3))

    evaluations = {
        "du": evaluate(a2, u), "nu": evaluate(a0, u),
        "dmu": evaluate(a2, -u), "nmu": evaluate(a0, -u),
        "dv": evaluate(a2, v), "nv": evaluate(a0, v),
        "dmv": evaluate(a2, -v), "nmv": evaluate(a0, -v),
        "dw": evaluate(a2, w), "nw": evaluate(a0, w),
        "dmw": evaluate(a2, -w), "nmw": evaluate(a0, -w),
        "dx": evaluate(a2, -t**2), "nx": evaluate(a0, -t**2),
    }

    def singular(expression):
        return str(sp.Poly(expression, *variables, modulus=PRIME).as_expr()) \
            .replace("**", "^")

    common_text = [singular(value) for value in equations[:3]]
    definitions = "\n".join(
        f"poly {name}={singular(value)};"
        for name, value in evaluations.items()
    )
    beta_text = singular(beta)
    program = f"""
ring R={PRIME},(u,v,w,t,r,c,b),dp;
poly f0={common_text[0]};
poly f1={common_text[1]};
poly f2={common_text[2]};
{definitions}
poly beta={beta_text};
poly p1=nv*du+nu*dv;
poly p2=nw*dmu+nmu*dw;
poly p3=nmv*nmw*dx-b*c*nx*dmv*dmw;
poly s=u*beta^2*(u-1)^2*nx*nmu*dx*dmu
       +{singular(delta**2)}*nu*du*(nmu*dx-nx*dmu)^2;
ideal I=f0,f1,f2,p1,p2,p3,s;
ideal G=std(I);
print(\"TYPE_A\");
print(dim(G));
print(size(G));
print(vdim(G));
quit;
"""
    header = {
        "cell": 5,
        "epsilon": [-1, -1],
        "template": "A",
        "variables": [str(value) for value in variables],
        "common_equations": [
            {
                "degree": sp.Poly(value, *variables, modulus=PRIME).total_degree(),
                "terms": len(sp.Poly(value, *variables, modulus=PRIME).terms()),
            }
            for value in equations[:3]
        ],
        "evaluation_term_range": [
            min(len(sp.Poly(value, *variables, modulus=PRIME).terms())
                for value in evaluations.values()),
            max(len(sp.Poly(value, *variables, modulus=PRIME).terms())
                for value in evaluations.values()),
        ],
    }
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=100,
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
            "one unsaturated deployed-field target-free type-A matching "
            "pilot; no route, row, or Prize conclusion"
        ),
        "result": test_matching.remote(),
    }, sort_keys=True))
