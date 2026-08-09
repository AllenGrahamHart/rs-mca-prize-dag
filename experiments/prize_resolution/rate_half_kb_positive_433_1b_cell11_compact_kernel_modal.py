#!/usr/bin/env python3
"""Compile the global coefficient kernel on the cell-11 common locus."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMMON = DIRECTORY / "rate_half_kb_positive_433_1b_common_vieta_compiler.py"
PRODUCT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
)
STRUCTURE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_complete_pivot_scout_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
)
REMOTE_COMMON = "/root/common.py"
REMOTE_PRODUCT = "/root/product.json"
REMOTE_STRUCTURE = "/root/structure.json"
PRIME = 2130706433
CELL = 11
PIVOT = 1

app = modal.App("rs-mca-positive-433-1b-cell11-compact-kernel")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
    .add_local_file(STRUCTURE, REMOTE_STRUCTURE)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=4)
def compile_kernel(signs):
    import functools
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from common import compile_cell

    epsilon_1, epsilon_2 = signs
    variables, _, metadata = compile_cell(CELL, epsilon_1, epsilon_2)
    t, r, c, b = variables
    labels = metadata["labels"]
    products = metadata["products"]
    q_values = metadata["q_values"]

    product_payload = json.loads(Path(REMOTE_PRODUCT).read_text())
    product_row = next(
        row for row in product_payload["rows"] if row["cell"] == CELL
    )
    raw_cofactors = tuple(
        sp.Poly(sp.sympify(value), *variables, modulus=PRIME)
        for value in product_row["kernel_cofactor_expressions"]
    )
    common_gcd = functools.reduce(sp.gcd, raw_cofactors)
    cofactors = []
    for value in raw_cofactors:
        quotient, remainder = sp.div(value, common_gcd)
        if not remainder.is_zero:
            raise RuntimeError("nonexact product-kernel gcd division")
        cofactors.append(quotient.as_expr())

    pivot_label = labels[PIVOT]
    pivot_scale = sp.expand(pivot_label * (1 - pivot_label))
    a_at_pivot = sp.expand(sum(
        cofactors[index] * pivot_label**index for index in range(3)
    ))
    gamma = sp.expand(q_values[PIVOT] * a_at_pivot)
    kernel = [
        *(sp.expand(pivot_scale * value) for value in cofactors),
        -gamma,
        gamma,
    ]
    kernel_polynomials = [
        sp.Poly(value, *variables, modulus=PRIME) for value in kernel
    ]
    kernel_gcd = functools.reduce(sp.gcd, kernel_polynomials)
    primitive_kernel = []
    for value in kernel_polynomials:
        quotient, remainder = sp.div(value, kernel_gcd)
        if not remainder.is_zero:
            raise RuntimeError("nonexact final-kernel gcd division")
        primitive_kernel.append(quotient.as_expr())
    first = next(
        sp.Poly(value, *variables, modulus=PRIME)
        for value in primitive_kernel if value != 0
    )
    inverse = pow(int(first.LC()) % PRIME, -1, PRIME)
    primitive_kernel = [
        sp.Poly(inverse * value, *variables, modulus=PRIME).as_expr()
        for value in primitive_kernel
    ]

    product_rows = [
        [-product, -product * label, -product * label**2,
         1, label, label**2, 0, 0]
        for label, product in zip(labels, products)
    ]
    sum_rows = [
        [q_value, q_value * label, q_value * label**2,
         0, 0, 0, label, label**2]
        for label, q_value in zip(labels, q_values)
    ]
    row_dots = [
        sp.expand(sum(left * right for left, right in zip(row, primitive_kernel)))
        for row in [*product_rows, *sum_rows]
    ]
    identically_zero = [
        sp.Poly(value, *variables, modulus=PRIME).is_zero for value in row_dots
    ]

    structure_payload = json.loads(Path(REMOTE_STRUCTURE).read_text())
    structure_rows = [
        row for row in structure_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    ]
    signatures = {
        tuple(item["sha256"] for item in row["lex_basis"])
        for row in structure_rows
    }
    if len(structure_rows) != 6 or len(signatures) != 1:
        raise RuntimeError("cofactor-chart lex mismatch")
    lex_basis = [item["expression"] for item in structure_rows[0]["lex_basis"]]
    definitions = "\n".join(
        f"poly k{index}={expression};"
        for index, expression in enumerate(lex_basis, start=1)
    )

    def singular(expression):
        return str(
            sp.Poly(expression, *variables, modulus=PRIME).as_expr()
        ).replace("**", "^")

    row_definitions = "\n".join(
        f"poly v{index}={singular(value)};"
        for index, value in enumerate(row_dots)
    )
    reductions = "\n".join(
        f'print("ROW={index},BEGIN"); print(reduce(v{index},G)); '
        f'print("ROW={index},END");'
        for index in range(len(row_dots))
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
{row_definitions}
ideal G=k1,k2,k3,k4,k5,k6,k7,k8,z*({guard})-1; G=slimgb(G);
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
{reductions}
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=240,
        )
    except subprocess.TimeoutExpired as error:
        stdout = (
            error.stdout.decode("utf-8", errors="replace")
            if isinstance(error.stdout, bytes) else error.stdout or ""
        )
        return {
            "epsilon": list(signs),
            "status": "TIMEOUT",
            "partial_stdout": stdout[-4000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    remainders = []
    for index in range(len(row_dots)):
        match = re.search(
            rf"ROW={index},BEGIN\n(.*?)\nROW={index},END",
            process.stdout, re.DOTALL,
        )
        remainders.append(
            "".join(match.group(1).split()) if match else None
        )
    valid = (
        process.returncode == 0
        and "END" in process.stdout
        and "?" not in process.stdout
    )

    def summary(expression):
        polynomial = sp.Poly(expression, *variables, modulus=PRIME)
        text = str(polynomial.as_expr())
        return {
            "degree": int(polynomial.total_degree()),
            "terms": len(polynomial.terms()),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
            "expression": text,
        }

    def integer(label):
        match = re.search(rf"(?:^|\n){label}=(-?\d+)", process.stdout)
        return int(match.group(1)) if match else None

    return {
        "epsilon": list(signs),
        "status": "COMPLETE" if valid else "ERROR",
        "product_kernel_removed_gcd": summary(common_gcd.as_expr()),
        "final_kernel_removed_gcd": summary(kernel_gcd.as_expr()),
        "kernel": [summary(value) for value in primitive_kernel],
        "identically_zero_rows": identically_zero,
        "remainders": remainders,
        "all_rows_zero": remainders == ["0"] * len(row_dots),
        "common_dimension": integer("DIM"),
        "common_basis_size": integer("SIZE"),
        "lex_signature": list(next(iter(signatures))),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stdout_tail": process.stdout[-2000:],
        "stderr_tail": process.stderr[-1000:],
    }


@app.local_entrypoint()
def main():
    cases = tuple(
        (epsilon_1, epsilon_2)
        for epsilon_1 in (-1, 1) for epsilon_2 in (-1, 1)
    )
    raw = list(compile_kernel.map(
        cases, order_outputs=True, return_exceptions=True
    ))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case), "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell11-compact-kernel-v1",
        "field": PRIME,
        "cell": CELL,
        "pivot": PIVOT,
        "scope": (
            "Exact global coefficient kernels on the guarded cell-11 common "
            "locus; no outside or route claim."
        ),
        "source_common_sha256": hashlib.sha256(COMMON.read_bytes()).hexdigest(),
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "source_structure_sha256": hashlib.sha256(
            STRUCTURE.read_bytes()
        ).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {
                "epsilon": row.get("epsilon"),
                "status": row.get("status"),
                "kernel_shapes": (
                    [[item["degree"], item["terms"]] for item in row["kernel"]]
                    if row.get("kernel") else None
                ),
                "identically_zero_rows": row.get("identically_zero_rows"),
                "all_rows_zero": row.get("all_rows_zero"),
                "common_dimension": row.get("common_dimension"),
                "common_basis_size": row.get("common_basis_size"),
            }
            for row in rows
        ],
    }, sort_keys=True))
