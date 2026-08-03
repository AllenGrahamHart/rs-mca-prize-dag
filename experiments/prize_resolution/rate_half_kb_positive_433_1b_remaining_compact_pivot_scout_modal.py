#!/usr/bin/env python3
"""Scout compact common-curve pivots for the remaining positive 433-1b cells."""

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
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_result.json"
)
REMOTE_COMMON = "/root/common.py"
REMOTE_PRODUCT = "/root/product.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-remaining-compact-pivot-scout")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=8)
def scout(case):
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from common import compile_cell

    cell, epsilon_1, epsilon_2, chart, pivot = case
    variables, _, metadata = compile_cell(cell, epsilon_1, epsilon_2)
    t, r, c, b = variables
    roots = metadata["roots"]
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
    base_rows = [*product_rows, sum_rows[pivot]]
    equations = [
        sp.expand(sp.Matrix([*base_rows, sum_rows[index]]).det(
            method="domain-ge"
        ))
        for index in range(1, 5) if index != pivot
    ]

    product_payload = json.loads(Path(REMOTE_PRODUCT).read_text())
    product_row = next(
        row for row in product_payload["rows"] if row["cell"] == cell
    )
    cofactor = sp.sympify(product_row["stripped_expressions"][chart])
    product_kernel = tuple(
        sp.sympify(value)
        for value in product_row["kernel_cofactor_expressions"]
    )
    pivot_scale = sp.expand(sum(
        product_kernel[index] * labels[pivot] ** index for index in range(3)
    ))
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
    guards = []
    seen = set()
    for expression in [cofactor, *route_guards]:
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
    saturation_stages = "\n".join(
        f"ideal H{index}=h{index}; "
        f"list S{index}=sat(G,H{index}); G=S{index}[1]; G=slimgb(G);"
        for index in range(len(guards))
    )
    pivot_saturation_stages = "\n".join(
        f"list PS{index}=sat(Jpivot,H{index}); "
        f"Jpivot=PS{index}[1]; Jpivot=slimgb(Jpivot);"
        for index in range(len(guards))
    )
    quotient_saturation_stages = "\n".join(
        f"ideal LH{index}=imap(R,H{index}); "
        f"list QS{index}=sat(Q,LH{index}); Q=QS{index}[1]; Q=std(Q);"
        for index in range(len(guards))
    )
    quotient_reductions = "\n".join(
        f'print("QROW={index},BEGIN"); print(reduce(K[{index + 1}],Q)); '
        f'print("QROW={index},END");'
        for index in range(9)
    )
    generators = ",".join(f"q{index}" for index in range(len(equations)))
    program = f"""
LIB "elim.lib";
ring R={PRIME},(t,r,c,b),dp;
option(redSB);
{equation_definitions}
{guard_definitions}
poly pivot_scale={singular(pivot_scale)};
ideal I={generators}; ideal G=slimgb(I);
{saturation_stages}
ideal Jpivot=G,pivot_scale; Jpivot=slimgb(Jpivot);
{pivot_saturation_stages}
ideal Etr=eliminate(G,c*b); Etr=slimgb(Etr);
ideal Erb=eliminate(G,t*c); Erb=slimgb(Erb);
ideal Ebt=eliminate(G,r*c); Ebt=slimgb(Ebt);
ideal Erc=eliminate(G,t*b); Erc=slimgb(Erc);
print("BEGIN");
print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
print("PIVOT_DIM="+string(dim(Jpivot)));
print("PIVOT_SIZE="+string(size(Jpivot)));
if ((size(Jpivot)==1) && (Jpivot[1]==1)) {{ print("PIVOT_UNIT=1"); }}
else {{ print("PIVOT_UNIT=0"); }}
print("ETR_DIM="+string(dim(Etr))); print("ETR_SIZE="+string(size(Etr)));
print("ERB_DIM="+string(dim(Erb))); print("ERB_SIZE="+string(size(Erb)));
print("EBT_DIM="+string(dim(Ebt))); print("EBT_SIZE="+string(size(Ebt)));
print("ERC_DIM="+string(dim(Erc))); print("ERC_SIZE="+string(size(Erc)));
print("ETR_BEGIN"); Etr; print("ETR_END");
print("ERB_BEGIN"); Erb; print("ERB_END");
print("EBT_BEGIN"); Ebt; print("EBT_END");
print("ERC_BEGIN"); Erc; print("ERC_END");
ring L={PRIME},(c,b,t,r),lp;
option(redSB);
ideal K=imap(R,G); K=std(K);
ideal Q=K[1],K[2],K[6]; Q=std(Q);
{quotient_saturation_stages}
ideal KR=reduce(K,Q);
print("LEX_SIZE="+string(size(K)));
print("QUOTIENT_SIZE="+string(size(Q)));
if ((size(KR)==1) && (KR[1]==0)) {{ print("QUOTIENT_EXACT=1"); }}
else {{ print("QUOTIENT_EXACT=0"); }}
{quotient_reductions}
print("LEX_BEGIN"); K; print("LEX_END");
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=270,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            "cell": cell,
            "epsilon": [epsilon_1, epsilon_2],
            "chart": chart,
            "pivot": pivot,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout)[-4000:],
            "partial_stderr": decoded(error.stderr)[-1000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }

    stdout = process.stdout

    def integer(label):
        match = re.search(rf"(?:^|\n){label}=(-?\d+)", stdout)
        return int(match.group(1)) if match else None

    def projection_profile(name):
        match = re.search(
            rf"{name}_BEGIN\n(.*?)\n{name}_END", stdout, re.DOTALL
        )
        body = match.group(1) if match else ""
        rows = re.findall(
            rf"^{name.title()}\[\d+\]=(.*?)(?=^{name.title()}\[\d+\]=|\Z)",
            body, re.MULTILINE | re.DOTALL,
        )
        compact = []
        for row in rows:
            normalized = "".join(row.split())
            compact.append({
                "characters": len(normalized),
                "terms": len(re.findall(r"[+-]?[^+-]+", normalized)),
                "sha256": hashlib.sha256(normalized.encode()).hexdigest(),
                "expression": normalized if len(normalized) <= 2000 else None,
            })
        return compact

    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    quotient_remainders = []
    for index in range(9):
        match = re.search(
            rf"QROW={index},BEGIN\n(.*?)\nQROW={index},END",
            stdout, re.DOTALL,
        )
        quotient_remainders.append(
            "".join(match.group(1).split()) if match else None
        )
    lex_match = re.search(r"LEX_BEGIN\n(.*?)\nLEX_END", stdout, re.DOTALL)
    lex_body = lex_match.group(1) if lex_match else ""
    lex_rows = re.findall(
        r"^K\[\d+\]=(.*?)(?=^K\[\d+\]=|\Z)",
        lex_body, re.MULTILINE | re.DOTALL,
    )
    lex_basis = []
    for row in lex_rows:
        normalized = "".join(row.split())
        lex_basis.append({
            "characters": len(normalized),
            "terms": len(re.findall(r"[+-]?[^+-]+", normalized)),
            "sha256": hashlib.sha256(normalized.encode()).hexdigest(),
            "expression": normalized if len(normalized) <= 10000 else None,
        })
    return {
        "cell": cell,
        "epsilon": [epsilon_1, epsilon_2],
        "chart": chart,
        "pivot": pivot,
        "status": "COMPLETE" if valid else "ERROR",
        "dimension": integer("DIM"),
        "basis_size": integer("SIZE"),
        "pivot_boundary_dimension": integer("PIVOT_DIM"),
        "pivot_boundary_size": integer("PIVOT_SIZE"),
        "pivot_boundary_unit": "PIVOT_UNIT=1" in stdout,
        "projection_dimensions": {
            name.lower(): integer(f"{name}_DIM")
            for name in ("ETR", "ERB", "EBT", "ERC")
        },
        "projection_sizes": {
            name.lower(): integer(f"{name}_SIZE")
            for name in ("ETR", "ERB", "EBT", "ERC")
        },
        "projections": {
            name.lower(): projection_profile(name)
            for name in ("ETR", "ERB", "EBT", "ERC")
        },
        "lex_basis_size": integer("LEX_SIZE"),
        "lex_basis": lex_basis,
        "quotient_basis_size": integer("QUOTIENT_SIZE"),
        "quotient_remainders": quotient_remainders,
        "quotient_exact": quotient_remainders == ["0"] * 9,
        "equation_profiles": [
            {
                "degree": sp.Poly(value, *variables, modulus=PRIME).total_degree(),
                "terms": len(sp.Poly(value, *variables, modulus=PRIME).terms()),
            }
            for value in equations
        ],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-1000:],
    }


@app.local_entrypoint()
def main(
    cells: str = "4",
    signs: str = "-1:-1",
    charts: str = "0",
    pivots: str = "1,2,3,4",
):
    selected_cells = tuple(int(value) for value in cells.split(",") if value)
    selected_signs = tuple(
        tuple(int(value) for value in pair.split(":"))
        for pair in signs.split(",") if pair
    )
    selected_charts = tuple(int(value) for value in charts.split(",") if value)
    selected_pivots = tuple(int(value) for value in pivots.split(",") if value)
    cases = tuple(itertools.product(
        selected_cells, selected_signs, selected_charts, selected_pivots
    ))
    cases = tuple(
        (cell, epsilon[0], epsilon[1], chart, pivot)
        for cell, epsilon, chart, pivot in cases
    )
    raw = list(scout.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "cell": case[0], "epsilon": list(case[1:3]),
                "chart": case[3], "pivot": case[4],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-compact-pivot-scout-v3",
        "field": PRIME,
        "scope": (
            "Exact pivot-boundary and two-variable projection scout for "
            "remaining principal common curves; no outside or route claim."
        ),
        "source_common_sha256": hashlib.sha256(COMMON.read_bytes()).hexdigest(),
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {
                key: row.get(key) for key in (
                    "cell", "epsilon", "chart", "pivot", "status",
                    "dimension", "basis_size", "pivot_boundary_unit",
                    "pivot_boundary_dimension", "pivot_boundary_size",
                    "projection_dimensions", "projection_sizes",
                    "lex_basis_size", "quotient_basis_size",
                    "quotient_exact", "equation_profiles",
                )
            }
            for row in rows
        ],
    }, sort_keys=True))
