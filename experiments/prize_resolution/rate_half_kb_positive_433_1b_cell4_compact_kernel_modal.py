#!/usr/bin/env python3
"""Compile the global polynomial common kernel for positive 433-1b cell 4."""

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
    "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell4_compact_kernel_result.json"
)
REMOTE_COMMON = "/root/common.py"
REMOTE_PRODUCT = "/root/product.json"
PRIME = 2130706433
CELL = 4
PIVOT = 1

app = modal.App("rs-mca-positive-433-1b-cell4-compact-kernel")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
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
        cofactors[index] * pivot_label**index
        for index in range(3)
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
    rows = [*product_rows, *sum_rows]
    row_dots = [
        sp.expand(sum(left * right for left, right in zip(row, primitive_kernel)))
        for row in rows
    ]
    identically_zero = [
        sp.Poly(value, *variables, modulus=PRIME).is_zero for value in row_dots
    ]

    reduced_product_rows = [row[:6] + [0] for row in product_rows]
    reduced_sum_rows = [
        row[:6] + [-label * (1 - label)]
        for row, label in zip(sum_rows, labels)
    ]
    base_rows = [*reduced_product_rows, reduced_sum_rows[PIVOT]]
    equations = [
        sp.expand(sp.Matrix([*base_rows, reduced_sum_rows[index]]).det(
            method="domain-ge"
        ))
        for index in range(1, 5) if index != PIVOT
    ]
    route_guards = [
        b, c, r, t,
        b - 1, b + 1, c - 1, c + 1, b - c, b + c,
        r * r - 1, r * r + 1, t * t - 1, t * t + 1,
        t * t - r * r, t * t + r * r,
    ]

    def strip_factors(expression):
        value = sp.Poly(expression, *variables, modulus=PRIME)
        for factor in route_guards:
            divisor = sp.Poly(factor, *variables, modulus=PRIME)
            while True:
                quotient, remainder = sp.div(value, divisor)
                if not remainder.is_zero:
                    break
                value = quotient
        return value.monic().as_expr()

    equations = [strip_factors(value) for value in equations]

    def singular(expression):
        return str(
            sp.Poly(expression, *variables, modulus=PRIME).as_expr()
        ).replace("**", "^")

    equation_definitions = "\n".join(
        f"poly q{index}={singular(value)};"
        for index, value in enumerate(equations)
    )
    row_definitions = "\n".join(
        f"poly v{index}={singular(value)};"
        for index, value in enumerate(row_dots)
    )
    reductions = "\n".join(
        f'print("ROW={index},BEGIN"); print(reduce(v{index},G)); '
        f'print("ROW={index},END");'
        for index in range(len(row_dots))
    )
    program = f"""
ring R={PRIME},(t,r,c,b),dp;
option(redSB);
{equation_definitions}
ideal I=q0,q1,q2; ideal G=slimgb(I);
{row_definitions}
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
{reductions}
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=270,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "epsilon": list(signs),
            "status": "TIMEOUT",
            "partial_stdout": (error.stdout or "")[-4000:],
            "partial_stderr": (error.stderr or "")[-1000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }

    stdout = process.stdout
    remainders = []
    for index in range(len(row_dots)):
        match = re.search(
            rf"ROW={index},BEGIN\n(.*?)\nROW={index},END",
            stdout, re.DOTALL,
        )
        remainders.append("".join(match.group(1).split()) if match else None)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout

    def summary(expression):
        polynomial = sp.Poly(expression, *variables, modulus=PRIME)
        text = str(polynomial.as_expr())
        return {
            "degree": polynomial.total_degree(),
            "terms": len(polynomial.terms()),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
            "expression": text,
        }

    return {
        "epsilon": list(signs),
        "status": "COMPLETE" if valid else "ERROR",
        "product_kernel_removed_gcd": summary(common_gcd.as_expr()),
        "final_kernel_removed_gcd": summary(kernel_gcd.as_expr()),
        "kernel": [summary(value) for value in primitive_kernel],
        "identically_zero_rows": identically_zero,
        "reduced_remainders": remainders,
        "all_rows_zero_mod_common": all(value == "0" for value in remainders),
        "common_dimension": int(re.search(r"DIM=(-?\d+)", stdout).group(1)),
        "common_basis_size": int(re.search(r"SIZE=(\d+)", stdout).group(1)),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-1000:],
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
                "epsilon": list(case),
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell4-compact-kernel-v1",
        "field": PRIME,
        "cell": CELL,
        "pivot": PIVOT,
        "scope": (
            "Exact polynomial coefficient kernels on the guarded cell-4 "
            "principal common curve; no outside or route claim."
        ),
        "source_common_sha256": hashlib.sha256(COMMON.read_bytes()).hexdigest(),
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "source_structure_sha256": hashlib.sha256(STRUCTURE.read_bytes()).hexdigest(),
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
                "all_rows_zero_mod_common": row.get(
                    "all_rows_zero_mod_common"
                ),
                "common_basis_size": row.get("common_basis_size"),
            }
            for row in rows
        ],
    }, sort_keys=True))
