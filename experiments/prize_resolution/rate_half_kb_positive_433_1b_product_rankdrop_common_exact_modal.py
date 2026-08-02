#!/usr/bin/env python3
"""Intersect 433-1b product-rank-drop loci with the exact common rank bound."""

import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMMON = DIRECTORY / "rate_half_kb_positive_433_1b_common_vieta_compiler.py"
PRODUCT = DIRECTORY / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_product_rankdrop_common_exact_result.json"
REMOTE_COMMON = "/root/common.py"
REMOTE_PRODUCT = "/root/product.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-rankdrop-common-exact")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=1.0, memory=3072, timeout=210, max_containers=8)
def decide_case(case):
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from common import ROLES, compile_cell

    cell, epsilon_1, epsilon_2 = case
    variables, _, metadata = compile_cell(cell, epsilon_1, epsilon_2)
    t, r, c, b = variables
    roots = metadata["roots"]
    labels = metadata["labels"]
    products = metadata["products"]
    sums = metadata["sums"]

    product_rows = [
        [-product, -product * label, -product * label**2,
         1, label, label**2, 0, 0]
        for product, label in zip(products, labels)
    ]
    sum_rows = [
        [q, q * label, q * label**2, 0, 0, 0, label, label**2]
        for root, label, edge_sum in zip(roots, labels, sums)
        for q in [sp.expand(root * edge_sum)]
    ]
    rows = [*product_rows, *sum_rows]

    product_payload = json.loads(Path(REMOTE_PRODUCT).read_text())
    product_row = next(row for row in product_payload["rows"]
                       if row["cell"] == cell)

    def singular(expression):
        return str(sp.Poly(expression, t, r, c, b, modulus=PRIME).as_expr()).replace(
            "**", "^"
        )

    matrix_entries = ",".join(singular(value) for row in rows for value in row)
    rank_equations = [value.replace("**", "^")
                      for value in product_row["stripped_expressions"]]
    definitions = "\n".join(
        f"poly f{index}={value};" for index, value in enumerate(rank_equations)
    )
    guard = (
        "r*t*b*c*(b-1)*(b+1)*(c-1)*(c+1)*(b-c)*(b+c)"
        "*(r^2-1)*(r^2+1)*(t^2-1)*(t^2+1)"
        "*(t^2-r^2)*(t^2+r^2)"
    )
    program = f"""
ring R={PRIME},(z,t,r,c,b),(dp(1),dp(4));
option(redSB);
{definitions}
matrix M[10][8]={matrix_entries};
ideal J=minor(M,8);
poly guard={guard};
ideal I=f0,f1,f2,f3,f4,f5,J,z*guard-1;
ideal G=std(I);
int common_dim=dim(G);
int common_size=size(G);
print("BEGIN_COMMON");
print("MINORS="+string(size(J)));
print("DIM="+string(common_dim));
print("SIZE="+string(common_size));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); }}
print("END_COMMON");
quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=180,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            "cell": cell,
            "epsilon": [epsilon_1, epsilon_2],
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout)[-4000:],
            "partial_stderr": decoded(error.stderr)[-2000:],
            "program_sha256": digest(program),
        }
    stdout = process.stdout
    valid = process.returncode == 0 and "END_COMMON" in stdout and "?" not in stdout
    dimension_match = re.search(r"DIM=(-?\d+)", stdout)
    size_match = re.search(r"SIZE=(\d+)", stdout)
    minor_match = re.search(r"MINORS=(\d+)", stdout)
    return {
        "cell": cell,
        "epsilon": [epsilon_1, epsilon_2],
        "singleton": ROLES[metadata["singleton"]],
        "matching": [[ROLES[value] for value in pair]
                     for pair in metadata["matching"]],
        "status": "COMPLETE" if valid else "ERROR",
        "unit": "UNIT=1" in stdout,
        "dimension": int(dimension_match.group(1)) if dimension_match else None,
        "basis_size": int(size_match.group(1)) if size_match else None,
        "minor_count": int(minor_match.group(1)) if minor_match else None,
        "stdout": stdout[-4000:],
        "stderr": process.stderr[-2000:],
        "program_sha256": digest(program),
    }


@app.local_entrypoint()
def main(cells: str = "0"):
    selected = tuple(int(value) for value in cells.split(",") if value)
    cases = tuple(itertools.product(selected, (-1, 1), (-1, 1)))
    raw_rows = list(decide_case.map(
        cases, order_outputs=True, return_exceptions=True,
    ))
    rows = []
    for case, row in zip(cases, raw_rows):
        if isinstance(row, BaseException):
            rows.append({
                "cell": case[0], "epsilon": list(case[1:]),
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-rankdrop-common-exact-v2",
        "scope": (
            "Exact full-common rank-at-most-seven ideals on the product-row "
            "rank-at-most-four branch, over the deployed field."
        ),
        "source_common_sha256": hashlib.sha256(COMMON.read_bytes()).hexdigest(),
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {"cell": row["cell"], "epsilon": row["epsilon"],
             "status": row["status"], "unit": row.get("unit")}
            for row in rows
        ],
    }, sort_keys=True))
