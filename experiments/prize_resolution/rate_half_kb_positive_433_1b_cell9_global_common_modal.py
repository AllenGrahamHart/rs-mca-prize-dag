#!/usr/bin/env python3
"""Compare cell 9's global rank-five common locus with its compact chart."""

import argparse
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
    "rate_half_kb_positive_433_1b_cell9_sign_structure_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_global_common_result.json"
)
REMOTE_COMMON = "/root/common.py"
REMOTE_PRODUCT = "/root/product.json"
REMOTE_STRUCTURE = "/root/structure.json"
PRIME = 2130706433
CELL = 9
PIVOT = 1

app = modal.App("rs-mca-positive-433-1b-cell9-global-common")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
    .add_local_file(STRUCTURE, REMOTE_STRUCTURE)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=420, max_containers=4)
def global_common(epsilon):
    import functools
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from common import compile_cell

    variables, _, metadata = compile_cell(CELL, *epsilon)
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

    product_payload = json.loads(Path(REMOTE_PRODUCT).read_text())
    product_row = next(
        row for row in product_payload["rows"] if row["cell"] == CELL
    )
    cofactors = tuple(
        sp.sympify(value) for value in product_row["stripped_expressions"]
    )
    raw_kernel = tuple(
        sp.Poly(sp.sympify(value), *variables, modulus=PRIME)
        for value in product_row["kernel_cofactor_expressions"]
    )
    kernel_gcd = functools.reduce(sp.gcd, raw_kernel)
    kernel = []
    for value in raw_kernel:
        quotient, remainder = sp.div(value, kernel_gcd)
        if not remainder.is_zero:
            raise RuntimeError("nonexact product-kernel gcd division")
        kernel.append(quotient.as_expr())
    pivot_scale = sp.expand(sum(
        kernel[index] * labels[PIVOT] ** index for index in range(3)
    ))
    route_guards = (
        b, c, r, t, b - 1, b + 1, c - 1, c + 1, b - c, b + c,
        r * r - 1, r * r + 1, t * t - 1, t * t + 1,
        t * t - r * r, t * t + r * r,
    )

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

    equations = tuple(strip_factors(value) for value in equations)

    structure_payload = json.loads(Path(REMOTE_STRUCTURE).read_text())
    structure_row = next(
        row for row in structure_payload["rows"]
        if row["epsilon"] == list(epsilon) and row["chart"] == 1
    )
    chart_basis = tuple(item["expression"] for item in structure_row["lex_basis"])

    def singular(expression):
        return str(
            sp.Poly(expression, *variables, modulus=PRIME).as_expr()
        ).replace("**", "^")

    definitions = "\n".join(
        f"poly q{index}={singular(value)};"
        for index, value in enumerate(equations)
    )
    cofactor_definitions = "\n".join(
        f"poly p{index}={singular(value)};"
        for index, value in enumerate(cofactors)
    )
    chart_definitions = "\n".join(
        f"poly k{index}={value};"
        for index, value in enumerate(chart_basis)
    )
    guard_product = sp.prod(route_guards)
    program = f"""
LIB "elim.lib";
ring R={PRIME},(t,r,c,b),dp;
option(redSB);
{definitions}
{cofactor_definitions}
poly h={singular(guard_product)};
poly pivot_scale={singular(pivot_scale)};
ideal I=q0,q1,q2; I=slimgb(I);
ideal H=h; list S=sat(I,H); ideal G=S[1]; G=slimgb(G);
ideal P={','.join(f'p{index}' for index in range(6))};
list T=sat(G,P); G=T[1]; G=slimgb(G);
ideal J=G,pivot_scale; J=slimgb(J);
list JS=sat(J,H); J=JS[1]; J=slimgb(J);
list JT=sat(J,P); J=JT[1]; J=slimgb(J);
print("BEGIN");
print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
print("PIVOT_SIZE="+string(size(J)));
if ((size(J)==1) && (J[1]==1)) {{ print("PIVOT_UNIT=1"); }}
else {{ print("PIVOT_UNIT=0"); }}
ring L={PRIME},(c,b,t,r),lp;
option(redSB);
ideal A=imap(R,G); A=std(A);
{chart_definitions}
ideal K={','.join(f'k{index}' for index in range(len(chart_basis)))}; K=std(K);
print("LEX_SIZE="+string(size(A)));
for (int arow=1; arow<=size(A); arow++) {{
  print("A="+string(arow-1)+":"+string(reduce(A[arow],K)));
}}
for (int krow=1; krow<=size(K); krow++) {{
  print("K="+string(krow-1)+":"+string(reduce(K[krow],A)));
}}
print("LEX_BEGIN"); A; print("LEX_END");
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=390,
        )
    except subprocess.TimeoutExpired as error:
        def decode(value):
            return (value.decode(errors="replace") if isinstance(value, bytes)
                    else value or "")
        return {
            "epsilon": list(epsilon), "status": "TIMEOUT",
            "partial_stdout": decode(error.stdout)[-4000:],
            "partial_stderr": decode(error.stderr)[-1000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    stdout = process.stdout

    def integer(label):
        match = re.search(rf"(?:^|\n){label}=(-?\d+)", stdout)
        return int(match.group(1)) if match else None

    def reductions(prefix):
        return [
            "".join(match.group(2).split())
            for match in re.finditer(
                rf"(?:^|\n){prefix}=(\d+):(.*?)(?=\n[AK]=|\nLEX_BEGIN)",
                stdout, re.DOTALL,
            )
        ]

    a_remainders = reductions("A")
    k_remainders = reductions("K")
    lex_match = re.search(r"LEX_BEGIN\n(.*?)\nLEX_END", stdout, re.DOTALL)
    lex_rows = re.findall(
        r"^A\[\d+\]=(.*?)(?=^A\[\d+\]=|\Z)",
        lex_match.group(1) if lex_match else "", re.MULTILINE | re.DOTALL,
    )
    lex_basis = ["".join(value.split()) for value in lex_rows]
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    return {
        "epsilon": list(epsilon),
        "status": "COMPLETE" if valid else "ERROR",
        "dimension": integer("DIM"),
        "basis_size": integer("SIZE"),
        "lex_basis_size": integer("LEX_SIZE"),
        "pivot_boundary_unit": "PIVOT_UNIT=1" in stdout,
        "global_in_chart_remainders": a_remainders,
        "chart_in_global_remainders": k_remainders,
        "ideals_equal": (
            len(a_remainders) == len(lex_basis)
            and len(k_remainders) == len(chart_basis)
            and all(value == "0" for value in [*a_remainders, *k_remainders])
        ),
        "lex_basis": [
            {
                "characters": len(value),
                "sha256": hashlib.sha256(value.encode()).hexdigest(),
                "expression": value,
            }
            for value in lex_basis
        ],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-1000:],
    }


@app.local_entrypoint()
def main(signs: str = "-1:-1"):
    selected = tuple(
        tuple(int(value) for value in pair.split(":"))
        for pair in signs.split(",") if pair
    )
    rows = list(global_common.map(selected, order_outputs=True))
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell9-global-common-v1",
        "field": PRIME,
        "cell": CELL,
        "pivot": PIVOT,
        "scope": (
            "Exact global product-rank-five common-locus saturation and "
            "comparison with chart 1; no outside, cell, route, K3, or Prize claim."
        ),
        "source_common_sha256": hashlib.sha256(COMMON.read_bytes()).hexdigest(),
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "source_structure_sha256": hashlib.sha256(STRUCTURE.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [{key: row.get(key) for key in (
            "epsilon", "status", "dimension", "basis_size", "lex_basis_size",
            "pivot_boundary_unit", "ideals_equal",
        )} for row in rows],
    }, sort_keys=True))
