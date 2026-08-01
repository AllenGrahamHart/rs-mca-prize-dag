#!/usr/bin/env python3
"""Localized Singular tests for residual positive 433-1a product rank."""

import hashlib
import json
from pathlib import Path
import subprocess

import modal


APP_NAME = "rs-mca-positive-433-1a-product-base-singular"
COMPILER = Path(__file__).with_name(
    "rate_half_kb_positive_433_1a_product_base_rank_compiler.py"
)
REMOTE_COMPILER = "/root/rate_half_kb_positive_433_1a_product_base_rank_compiler.py"
PRIME = 2130706433

app = modal.App(APP_NAME)
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMPILER, REMOTE_COMPILER)
)


def quotient_square_variables(text):
    import sympy as sp

    b, c, r, t, R, T = sp.symbols("b c r t R T")
    polynomial = sp.Poly(sp.sympify(text), r, t, c, b, modulus=PRIME)
    output = 0
    for (r_degree, t_degree, c_degree, b_degree), coefficient in polynomial.terms():
        if r_degree % 2 or t_degree % 2:
            raise RuntimeError("odd source-root exponent")
        output += (int(coefficient) * R ** (r_degree // 2)
                   * T ** (t_degree // 2) * c ** c_degree * b ** b_degree)
    return str(sp.expand(output)).replace("**", "^")


@app.function(image=image, cpu=1.0, memory=1024, timeout=180, max_containers=4)
def test_cell(cell):
    compiler = subprocess.run(
        ["python3", REMOTE_COMPILER, "--cell", str(cell), "--dump"],
        capture_output=True,
        text=True,
        timeout=40,
    )
    if compiler.returncode:
        return {"cell": cell, "status": "COMPILER_ERROR", "stderr": compiler.stderr}
    payload = json.loads(compiler.stdout)
    equations = [quotient_square_variables(value)
                 for value in payload["stripped_expressions"]]
    guard = (
        "R*T*b*c*(b-1)*(b+1)*(c-1)*(c+1)*(b-c)*(b+c)"
        "*(R-1)*(R+1)*(T-1)*(T+1)*(T-R)*(T+R)"
    )
    program = [
        f"ring q={PRIME},(b,c,R,T,z),dp;",
        "option(redSB);",
    ]
    program.extend(f"poly f{index}={value};"
                   for index, value in enumerate(equations))
    program.extend([
        f"ideal I={','.join(f'f{index}' for index in range(len(equations)))},z*({guard})-1;",
        "ideal G=std(I);",
        'if (reduce(1,G)==0) { print("UNIT"); } else { print("NONUNIT"); }',
        "print(size(G));",
        "G[1];",
        "quit;",
    ])
    try:
        process = subprocess.run(
            ["Singular", "-q"],
            input="\n".join(program),
            capture_output=True,
            text=True,
            timeout=130,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "cell": cell,
            "status": "TIMEOUT",
            "stdout": error.stdout or "",
            "stderr": error.stderr or "",
        }
    return {
        "cell": cell,
        "status": "COMPLETE" if process.returncode == 0 else "SINGULAR_ERROR",
        "stdout": process.stdout[-2000:],
        "stderr": process.stderr[-2000:],
        "equation_degrees": [row["degree"] for row in payload["stripped"]],
        "equation_sha256": [row["sha256"] for row in payload["stripped"]],
        "program_sha256": hashlib.sha256(
            "\n".join(program).encode()
        ).hexdigest(),
    }


@app.local_entrypoint()
def main(cell: int = 1, cells: str = ""):
    selected = tuple(int(value) for value in cells.split(",") if value) \
        if cells else (cell,)
    print(json.dumps(list(test_cell.map(selected)), sort_keys=True))
