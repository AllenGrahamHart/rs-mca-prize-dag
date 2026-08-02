#!/usr/bin/env python3
"""Scout two useful lex orders for each remaining positive common curve."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMMON = DIRECTORY / "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_remaining_lex_scout_result.json"
REMOTE_COMMON = "/root/rate_half_kb_positive_433_1a_common_vieta_compiler.py"
PRIME = 2130706433
TASKS = [
    {"cell": cell, "order": list(order)}
    for cell in (4, 9, 11, 12, 14)
    for order in (("c", "r", "b", "t"), ("r", "c", "b", "t"))
]

app = modal.App("rs-mca-positive-433-1a-remaining-lex-scout")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=2.0, memory=3072, timeout=150, max_containers=10)
def project(task):
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_common_vieta_compiler import compile_cell

    cell = task["cell"]
    order = task["order"]
    variables, equations, metadata = compile_cell(cell, -1, -1, strip_fast=True)
    t, r, c, b = variables
    labels = metadata["labels"]
    guards = [
        labels[left]-labels[right]
        for left in range(5) for right in range(left+1, 5)
    ]
    guards.extend((
        r, t, b, c, b-1, b+1, c-1, c+1, b-c, b+c,
    ))
    guard_product = sp.prod(guards)

    def singular(expression):
        return str(sp.Poly(expression, t, r, c, b,
                           modulus=PRIME).as_expr()).replace("**", "^")

    equation_text = [singular(value) for value in equations]
    guard_text = singular(guard_product)
    definitions = "\n".join(
        f"poly f{index}={value};" for index, value in enumerate(equation_text)
    )
    program = f"""
ring R={PRIME},(u,t,r,c,b),(dp(1),dp(4));
option(redSB);
{definitions}
poly guard={guard_text};
ideal F=f0,f1,f2,f3,f4,f5,u*guard-1;
ideal GF=std(F); ideal E=eliminate(GF,u);
ring P={PRIME},({','.join(order)}),lp;
option(redSB);
ideal EP=imap(R,E); ideal GP=std(EP);
print("BEGIN_LEX_SUMMARY"); print(dim(GP)); print(size(GP));
print("BEGIN_LEX_BASIS"); GP; print("END_LEX_BASIS");
quit;
"""
    header = {
        "field": PRIME,
        "cell": cell,
        "epsilon": [-1, -1],
        "order": order,
        "matching": metadata["matching"],
        "equation_sha256": [digest(value) for value in equation_text],
        "guard_sha256": digest(guard_text),
        "program_sha256": digest(program),
    }
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=120,
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
    valid = process.returncode == 0 and "END_LEX_BASIS" in stdout and "?" not in stdout
    basis = re.findall(r"^GP\[\d+\]=(.*)$", stdout, re.MULTILINE)
    return {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "basis_size": len(basis),
        "basis_sha256": [digest(value) for value in basis],
        "basis_chars": [len(value) for value in basis],
        "stdout": stdout[-120000:],
        "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main():
    rows = list(project.map(TASKS, order_outputs=True, return_exceptions=True))
    normalized = []
    for task, row in zip(TASKS, rows):
        if isinstance(row, BaseException):
            normalized.append({**task, "status": "REMOTE_ERROR", "error": repr(row)})
        else:
            normalized.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1a-remaining-lex-scout-v1",
        "scope": (
            "Two exact deployed-field lex projections for each remaining "
            "positive common curve; no outside, route, K3, or Prize claim."
        ),
        "rows": normalized,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {key: row.get(key) for key in
             ("cell", "order", "status", "basis_size", "basis_chars")}
            for row in normalized
        ],
    }, sort_keys=True))
