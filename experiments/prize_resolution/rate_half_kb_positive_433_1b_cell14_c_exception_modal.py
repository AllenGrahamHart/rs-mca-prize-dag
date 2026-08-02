#!/usr/bin/env python3
"""Compile the finite c-denominator exception in positive 433-1b cell 14."""

import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
PRODUCT = DIRECTORY / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_c_exception_result.json"
REMOTE_PRODUCT = "/root/product.json"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1b-cell14-c-exception")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=240, max_containers=4)
def compile_exception(signs):
    import sympy as sp

    epsilon_1, epsilon_2 = signs
    t, r, c, b = sp.symbols("t r c b")
    variables = (t, r, c, b)
    labels = (1, r*r, -r*r, -1, t*t)
    products = (-1, b, c, b*c, -b*c)
    sums = (0, 1+b, 1+c, b+c, b-c)
    roots = (1, r, epsilon_2*IOTA*r, epsilon_1*IOTA, t)
    q_values = tuple(sp.expand(root*edge_sum)
                     for root, edge_sum in zip(roots, sums))
    product_rows = [
        [-product, -product*label, -product*label**2,
         1, label, label**2, 0]
        for label, product in zip(labels, products)
    ]
    sum_rows = [
        [q_value, q_value*label, q_value*label**2,
         0, 0, 0, -label*(1-label)]
        for label, q_value in zip(labels, q_values)
    ]
    base_rows = [*product_rows, sum_rows[1]]
    equations = [
        sp.expand(sp.Matrix([*base_rows, sum_rows[index]]).det(method="domain-ge"))
        for index in (2, 3, 4)
    ]
    route_guards = [
        b, c, r, t,
        b-1, b+1, c-1, c+1, b-c, b+c,
        r*r-1, r*r+1, t*t-1, t*t+1,
        t*t-r*r, t*t+r*r,
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
    product_row = next(row for row in product_payload["rows"]
                       if row["cell"] == 14)
    cofactor = sp.sympify(product_row["stripped_expressions"][3])
    guards = [cofactor, *route_guards]

    def singular(expression):
        return str(sp.Poly(expression, *variables,
                           modulus=PRIME).as_expr()).replace("**", "^")

    equation_definitions = "\n".join(
        f"poly q{index}={singular(value)};"
        for index, value in enumerate(equations)
    )
    guard_definitions = "\n".join(
        f"poly h{index}={singular(value)};"
        for index, value in enumerate(guards)
    )
    saturation_stages = "\n".join(
        f"ideal H{index}=h{index}; "
        f"list S{index}=sat(G,H{index}); G=S{index}[1]; G=slimgb(G);"
        for index in range(len(guards))
    )
    open_exception_stages = "\n".join(
        f"ideal OH{index}=h{index}; "
        f"list OS{index}=sat(O,OH{index}); O=OS{index}[1]; O=slimgb(O);"
        for index in range(1, len(guards))
    )
    generators = ",".join(f"q{index}" for index in range(len(equations)))
    program = f"""
LIB "elim.lib";
ring R={PRIME},(t,r,c,b),dp;
option(redSB);
{equation_definitions}
{guard_definitions}
ideal I={generators}; ideal G=slimgb(I);
{saturation_stages}
ideal Etr=eliminate(G,c*b); Etr=slimgb(Etr);
poly dc=diff(G[1],c);
ideal J=G,dc; J=slimgb(J);
ring L={PRIME},(c,t,b,r),lp;
ideal K=imap(R,J); K=std(K);
print("BEGIN");
print("CLOSURE_DIM="+string(dim(K))); print("CLOSURE_SIZE="+string(size(K)));
if ((size(K)==1) && (K[1]==1)) {{ print("CLOSURE_UNIT=1"); }}
else {{ print("CLOSURE_UNIT=0"); print("LEX_BEGIN"); K; print("LEX_END"); }}
setring R;
ideal O=J;
{open_exception_stages}
print("OPEN_DIM="+string(dim(O))); print("OPEN_SIZE="+string(size(O)));
if ((size(O)==1) && (O[1]==1)) {{ print("OPEN_UNIT=1"); }}
else {{ print("OPEN_UNIT=0"); }}
print("END");
quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=210,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "epsilon": list(signs), "status": "TIMEOUT",
            "partial_stdout": (error.stdout or "")[-2000:],
            "partial_stderr": (error.stderr or "")[-1000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    stdout = process.stdout
    dimension = re.search(r"CLOSURE_DIM=(-?\d+)", stdout)
    basis_size = re.search(r"CLOSURE_SIZE=(\d+)", stdout)
    open_dimension = re.search(r"OPEN_DIM=(-?\d+)", stdout)
    open_size = re.search(r"OPEN_SIZE=(\d+)", stdout)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    return {
        "epsilon": list(signs),
        "status": "COMPLETE" if valid else "ERROR",
        "unit": "CLOSURE_UNIT=1" in stdout,
        "dimension": int(dimension.group(1)) if dimension else None,
        "basis_size": int(basis_size.group(1)) if basis_size else None,
        "open_unit": "OPEN_UNIT=1" in stdout,
        "open_dimension": (
            int(open_dimension.group(1)) if open_dimension else None
        ),
        "open_basis_size": int(open_size.group(1)) if open_size else None,
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-1000:],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
    }


@app.local_entrypoint()
def main():
    cases = tuple(itertools.product((-1, 1), (-1, 1)))
    rows = list(compile_exception.map(cases, order_outputs=True,
                                      return_exceptions=True))
    normalized_rows = []
    for case, row in zip(cases, rows):
        if isinstance(row, BaseException):
            normalized_rows.append({
                "epsilon": list(case), "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            normalized_rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell14-c-exception-v1",
        "field": PRIME,
        "scope": "Exact lex atlases for the finite c-denominator exception.",
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "rows": normalized_rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {key: row.get(key) for key in
             ("epsilon", "status", "unit", "dimension", "basis_size",
              "open_unit", "open_dimension", "open_basis_size")}
            for row in normalized_rows
        ],
    }, sort_keys=True))
