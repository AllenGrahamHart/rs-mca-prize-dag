#!/usr/bin/env python3
"""Test the cell-4 xi0/pairing0 target-free outside cut exactly."""

import hashlib
import itertools
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
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell4_compact_kernel_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell4_xi0_pairing0_target_free_result.json"
)
REMOTE_COMMON = "/root/common.py"
REMOTE_PRODUCT = "/root/product.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433
CELL = 4
PIVOT = 1

app = modal.App("rs-mca-positive-433-1b-cell4-xi0-pairing0-target-free")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=8)
def decide(case):
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from common import compile_cell

    epsilon_1, epsilon_2, chart = case
    variables, _, metadata = compile_cell(CELL, epsilon_1, epsilon_2)
    t, r, c, b = variables
    labels = metadata["labels"]
    products = metadata["products"]
    q_values = metadata["q_values"]

    product_rows = [
        [-product, -product * label, -product * label**2,
         1, label, label**2, 0]
        for label, product in zip(labels, products)
    ]
    sum_rows = [
        [q_value, q_value * label, q_value * label**2,
         0, 0, 0, -label * (1 - label)]
        for label, q_value in zip(labels, q_values)
    ]
    base_rows = [*product_rows, sum_rows[PIVOT]]
    equations = [
        sp.expand(sp.Matrix([*base_rows, sum_rows[index]]).det(
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
    product_payload = json.loads(Path(REMOTE_PRODUCT).read_text())
    product_row = next(
        row for row in product_payload["rows"] if row["cell"] == CELL
    )
    cofactor = sp.sympify(product_row["stripped_expressions"][chart])
    product_kernel = tuple(
        sp.sympify(value)
        for value in product_row["kernel_cofactor_expressions"]
    )
    pivot_kernel_scale = sp.expand(sum(
        product_kernel[index] * labels[PIVOT] ** index
        for index in range(3)
    ))

    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    kernel_row = next(
        row for row in kernel_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    kernel = tuple(sp.sympify(value["expression"]) for value in kernel_row["kernel"])
    a_coefficients = kernel[:3]
    b_coefficients = kernel[3:6]

    def evaluate(coefficients, value):
        return sp.expand(sum(
            coefficient * value**index
            for index, coefficient in enumerate(coefficients)
        ))

    missing_label = -t * t
    a_missing = evaluate(a_coefficients, missing_label)
    b_missing = evaluate(b_coefficients, missing_label)
    missing_record = sp.cancel(b_missing / a_missing)

    def paired(left, right):
        p0, p1, p2 = (
            b_value - left * a_value
            for a_value, b_value in zip(a_coefficients, b_coefficients)
        )
        q0 = b_coefficients[0] - right * a_coefficients[0]
        q1 = -b_coefficients[1] + right * a_coefficients[1]
        q2 = b_coefficients[2] - right * a_coefficients[2]
        return (p2 * q0 - p0 * q2)**2 - (
            p2 * q1 - p1 * q2
        ) * (p1 * q0 - p0 * q1)

    target_free_rational = sp.cancel(paired(missing_record, -missing_record))
    target_numerator, target_denominator = sp.fraction(target_free_rational)
    target_numerator = sp.Poly(
        target_numerator, *variables, modulus=PRIME
    ).primitive()[1].monic().as_expr()
    target_denominator = sp.Poly(
        target_denominator, *variables, modulus=PRIME
    ).primitive()[1].monic().as_expr()

    guards = []
    seen = set()
    for expression in [cofactor, pivot_kernel_scale, *route_guards]:
        value = sp.Poly(expression, *variables, modulus=PRIME)
        if value.total_degree() == 0:
            continue
        normalized = value.monic().as_expr()
        key = str(normalized)
        if key not in seen:
            seen.add(key)
            guards.append(normalized)

    def singular(expression):
        return str(
            sp.Poly(expression, *variables, modulus=PRIME).as_expr()
        ).replace("**", "^")

    equation_definitions = "\n".join(
        f"poly q{index}={singular(value)};"
        for index, value in enumerate(equations)
    )
    guard_definitions = "\n".join(
        f"poly h{index}={singular(value)};"
        for index, value in enumerate(guards)
    )
    common_saturations = "\n".join(
        f"ideal H{index}=h{index}; "
        f"list GS{index}=sat(G,H{index}); G=GS{index}[1]; G=slimgb(G);"
        for index in range(len(guards))
    )
    missing_saturations = "\n".join(
        f"list MS{index}=sat(Jmissing,H{index}); "
        f"Jmissing=MS{index}[1]; Jmissing=slimgb(Jmissing);"
        for index in range(len(guards))
    )
    target_saturations = "\n".join(
        f"list TS{index}=sat(Jtarget,H{index}); "
        f"Jtarget=TS{index}[1]; Jtarget=slimgb(Jtarget);"
        for index in range(len(guards))
    )
    program = f"""
LIB "elim.lib";
ring R={PRIME},(t,r,c,b),dp;
option(redSB);
{equation_definitions}
{guard_definitions}
poly am={singular(a_missing)};
poly cut={singular(target_numerator)};
ideal I=q0,q1,q2; ideal G=slimgb(I);
{common_saturations}
ideal Jmissing=G,am; Jmissing=slimgb(Jmissing);
{missing_saturations}
ideal Jtarget=G,cut; Jtarget=slimgb(Jtarget);
{target_saturations}
ideal Er=eliminate(Jtarget,t*c*b); Er=slimgb(Er);
print("BEGIN");
print("COMMON_DIM="+string(dim(G))); print("COMMON_SIZE="+string(size(G)));
print("MISSING_DIM="+string(dim(Jmissing)));
print("MISSING_SIZE="+string(size(Jmissing)));
if ((size(Jmissing)==1) && (Jmissing[1]==1)) {{ print("MISSING_UNIT=1"); }}
else {{ print("MISSING_UNIT=0"); }}
print("TARGET_DIM="+string(dim(Jtarget)));
print("TARGET_SIZE="+string(size(Jtarget)));
if ((size(Jtarget)==1) && (Jtarget[1]==1)) {{ print("TARGET_UNIT=1"); }}
else {{ print("TARGET_UNIT=0"); }}
print("ER_DIM="+string(dim(Er))); print("ER_SIZE="+string(size(Er)));
print("ER_BEGIN"); Er; print("ER_END");
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=270,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "epsilon": [epsilon_1, epsilon_2],
            "chart": chart,
            "status": "TIMEOUT",
            "target_numerator_profile": {
                "degree": sp.Poly(target_numerator, *variables, modulus=PRIME).total_degree(),
                "terms": len(sp.Poly(target_numerator, *variables, modulus=PRIME).terms()),
            },
            "partial_stdout": (error.stdout or "")[-4000:],
            "partial_stderr": (error.stderr or "")[-1000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }

    stdout = process.stdout

    def integer(label):
        match = re.search(rf"(?:^|\n){label}=(-?\d+)", stdout)
        return int(match.group(1)) if match else None

    elimination = re.search(r"ER_BEGIN\n(.*?)\nER_END", stdout, re.DOTALL)
    elimination_text = "".join(elimination.group(1).split()) if elimination else None
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout

    def profile(expression):
        polynomial = sp.Poly(expression, *variables, modulus=PRIME)
        text = str(polynomial.as_expr())
        return {
            "degree": polynomial.total_degree(),
            "terms": len(polynomial.terms()),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
        }

    return {
        "epsilon": [epsilon_1, epsilon_2],
        "chart": chart,
        "status": "COMPLETE" if valid else "ERROR",
        "common_dimension": integer("COMMON_DIM"),
        "common_basis_size": integer("COMMON_SIZE"),
        "missing_boundary_dimension": integer("MISSING_DIM"),
        "missing_boundary_size": integer("MISSING_SIZE"),
        "missing_boundary_unit": "MISSING_UNIT=1" in stdout,
        "target_dimension": integer("TARGET_DIM"),
        "target_basis_size": integer("TARGET_SIZE"),
        "target_unit": "TARGET_UNIT=1" in stdout,
        "r_elimination_dimension": integer("ER_DIM"),
        "r_elimination_size": integer("ER_SIZE"),
        "r_elimination": elimination_text,
        "a_missing_profile": profile(a_missing),
        "target_numerator_profile": profile(target_numerator),
        "target_denominator_profile": profile(target_denominator),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-1000:],
    }


@app.local_entrypoint()
def main(
    signs: str = "-1:-1",
    charts: str = "0",
):
    selected_signs = tuple(
        tuple(int(value) for value in pair.split(":"))
        for pair in signs.split(",") if pair
    )
    selected_charts = tuple(int(value) for value in charts.split(",") if value)
    cases = tuple(
        (epsilon_1, epsilon_2, chart)
        for (epsilon_1, epsilon_2), chart in itertools.product(
            selected_signs, selected_charts
        )
    )
    raw = list(decide.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "chart": case[2],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell4-xi0-pairing0-v1",
        "field": PRIME,
        "scope": (
            "Exact generic target-free cut for cell 4, xi0, pairing0; "
            "no other pairing, full cell, orbit, or route claim."
        ),
        "source_common_sha256": hashlib.sha256(COMMON.read_bytes()).hexdigest(),
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {
                key: row.get(key) for key in (
                    "epsilon", "chart", "status", "common_dimension",
                    "common_basis_size", "missing_boundary_dimension",
                    "missing_boundary_size", "missing_boundary_unit",
                    "target_dimension", "target_basis_size", "target_unit",
                    "r_elimination_dimension", "r_elimination_size",
                    "a_missing_profile", "target_numerator_profile",
                    "target_denominator_profile",
                )
            }
            for row in rows
        ],
    }, sort_keys=True))
