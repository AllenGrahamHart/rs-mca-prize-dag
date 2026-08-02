#!/usr/bin/env python3
"""Scout four exact lex projections of the deployed cell-3 common curve."""

import hashlib
import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMMON = DIRECTORY / "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_common_triangle_scout_result.json"
REMOTE_COMMON = "/root/rate_half_kb_positive_433_1a_common_vieta_compiler.py"
PRIME = 2130706433
ORDERS = (
    ("r", "c", "b", "t"),
    ("c", "r", "b", "t"),
    ("b", "r", "c", "t"),
    ("t", "r", "c", "b"),
)

app = modal.App("rs-mca-positive-433-1a-cell3-common-triangle-scout")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=4)
def project(order):
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_common_vieta_compiler import compile_cell

    variables, equations, metadata = compile_cell(3, -1, -1, strip_fast=True)
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
    order_text = ",".join(order)
    program = f"""
ring R={PRIME},(u,t,r,c,b),(dp(1),dp(4));
option(redSB);
{definitions}
poly guard={guard_text};
ideal F=f0,f1,f2,f3,f4,f5,u*guard-1;
ideal GF=std(F);
print("BEGIN_BLOCK_SUMMARY"); print(dim(GF)); print(size(GF));
ideal E=eliminate(GF,u);
ring P={PRIME},({order_text}),lp;
option(redSB);
ideal EP=imap(R,E);
ideal GP=std(EP);
print("BEGIN_LEX_SUMMARY"); print(dim(GP)); print(size(GP));
print("BEGIN_LEX_BASIS"); GP; print("END_LEX_BASIS");
quit;
"""
    header = {
        "field": PRIME,
        "cell": 3,
        "epsilon": [-1, -1],
        "order": list(order),
        "matching": metadata["matching"],
        "equation_sha256": [digest(value) for value in equation_text],
        "guard_sha256": digest(guard_text),
        "program_sha256": digest(program),
    }
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=250,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            **header,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout)[-120000:],
            "partial_stderr": decoded(error.stderr)[-4000:],
        }
    stdout = process.stdout
    valid = (
        process.returncode == 0
        and "END_LEX_BASIS" in stdout
        and "?" not in stdout
    )
    return {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "stdout": stdout[-120000:],
        "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main():
    rows = list(project.map(ORDERS, order_outputs=False, return_exceptions=True))
    normalized = []
    for row in rows:
        if isinstance(row, BaseException):
            normalized.append({"status": "REMOTE_ERROR", "error": repr(row)})
        else:
            normalized.append(row)
    normalized.sort(key=lambda row: tuple(row.get("order", ())))
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell3-common-triangle-scout-v1",
        "scope": (
            "Four exact deployed-field lex projections of the cell-3 "
            "common curve; no outside, route, K3, or Prize claim."
        ),
        "rows": normalized,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {"order": row.get("order"), "status": row.get("status")}
            for row in normalized
        ],
    }, sort_keys=True))
