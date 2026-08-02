#!/usr/bin/env python3
"""Localized principal common charts for positive 433-1b."""

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
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_principal_common_charts_result.json"
REMOTE_COMMON = "/root/common.py"
REMOTE_PRODUCT = "/root/product.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-principal-common-charts")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=210, max_containers=100)
def decide_chart(case):
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from common import ROLES, compile_cell

    cell, epsilon_1, epsilon_2, chart = case
    variables, equations, metadata = compile_cell(
        cell, epsilon_1, epsilon_2, strip_fast=True
    )
    t, r, c, b = variables
    product_payload = json.loads(Path(REMOTE_PRODUCT).read_text())
    product_row = next(row for row in product_payload["rows"]
                       if row["cell"] == cell)
    cofactor = product_row["stripped_expressions"][chart].replace("**", "^")

    def singular(expression):
        return str(sp.Poly(expression, t, r, c, b, modulus=PRIME).as_expr()).replace(
            "**", "^"
        )

    definitions = "\n".join(
        f"poly f{index}={singular(value)};"
        for index, value in enumerate(equations)
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
poly h={cofactor};
ideal I=f0,f1,f2,f3,f4,f5,z*({guard})*h-1;
ideal G=std(I);
print("BEGIN");
print("DIM="+string(dim(G)));
print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); print("GB_BEGIN"); G; print("GB_END"); }}
print("END");
quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=180,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "cell": cell, "epsilon": [epsilon_1, epsilon_2], "chart": chart,
            "status": "TIMEOUT", "partial_stdout": (error.stdout or "")[-2000:],
            "partial_stderr": (error.stderr or "")[-1000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    stdout = process.stdout
    dimension = re.search(r"DIM=(-?\d+)", stdout)
    basis_size = re.search(r"SIZE=(\d+)", stdout)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    return {
        "cell": cell,
        "epsilon": [epsilon_1, epsilon_2],
        "chart": chart,
        "singleton": ROLES[metadata["singleton"]],
        "matching": [[ROLES[value] for value in pair]
                     for pair in metadata["matching"]],
        "status": "COMPLETE" if valid else "ERROR",
        "unit": "UNIT=1" in stdout,
        "dimension": int(dimension.group(1)) if dimension else None,
        "basis_size": int(basis_size.group(1)) if basis_size else None,
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-1000:],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
    }


@app.local_entrypoint()
def main(cells: str = "0", charts: str = "0,1,2,3,4,5"):
    selected = tuple(int(value) for value in cells.split(",") if value)
    selected_charts = tuple(int(value) for value in charts.split(",") if value)
    cases = tuple(itertools.product(selected, (-1, 1), (-1, 1), selected_charts))
    raw = list(decide_chart.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "cell": case[0], "epsilon": list(case[1:3]), "chart": case[3],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-principal-common-charts-v1",
        "app": "rs-mca-positive-433-1b-principal-common-charts",
        "field": PRIME,
        "scope": (
            "Exact six-common-minor ideals localized at each nonzero product "
            "cofactor chart; outside rows and route exclusion are not decided."
        ),
        "source_common_sha256": hashlib.sha256(COMMON.read_bytes()).hexdigest(),
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "case_count": len(rows),
        "status_counts": {
            status: sum(row["status"] == status for row in rows)
            for status in sorted({row["status"] for row in rows})
        },
        "unit_count": sum(row.get("unit", False) for row in rows),
        "nonunit_count": sum(
            row["status"] == "COMPLETE" and not row.get("unit", False)
            for row in rows
        ),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "status_counts": {
            status: sum(row["status"] == status for row in rows)
            for status in sorted({row["status"] for row in rows})
        },
        "unit": sum(row.get("unit", False) for row in rows),
        "nonunit": sum(row["status"] == "COMPLETE" and not row.get("unit", False)
                       for row in rows),
        "nonunit_rows": [
            [row["cell"], *row["epsilon"], row["chart"],
             row.get("dimension"), row.get("basis_size")]
            for row in rows if row["status"] == "COMPLETE" and not row.get("unit", False)
        ],
    }, sort_keys=True))
