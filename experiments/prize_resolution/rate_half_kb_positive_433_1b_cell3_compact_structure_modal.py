#!/usr/bin/env python3
"""Probe the compact principal common curve for positive 433-1b cell 3."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
PRODUCT = DIRECTORY / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_compact_structure_result.json"
REMOTE_PRODUCT = "/root/product.json"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1b-cell3-compact-structure")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=4)
def analyze(case):
    import sympy as sp

    epsilon_1, epsilon_2, chart = case
    t, r, c, b = sp.symbols("t r c b")
    variables = (t, r, c, b)

    # Cell 3 has singleton AB and pairs (LA,AC), (BC+,BC-).
    roots = (1, t, epsilon_1 * IOTA, r, epsilon_2 * IOTA * r)
    labels = tuple(sp.expand(root * root) for root in roots)
    products = (-1, b, c, b * c, -b * c)
    sums = (0, 1 + b, 1 + c, b + c, b - c)
    q_values = tuple(
        sp.expand(root * edge_sum) for root, edge_sum in zip(roots, sums)
    )

    # The LA sum row gives beta_1=-beta_0.  Eliminate beta_1 and use the
    # guarded AB sum row with the five product rows as a rank-six base.
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
    base_rows = [*product_rows, sum_rows[1]]
    equations = [
        sp.expand(
            sp.Matrix([*base_rows, sum_rows[index]]).det(method="domain-ge")
        )
        for index in (2, 3, 4)
    ]

    product_payload = json.loads(Path(REMOTE_PRODUCT).read_text())
    product_row = next(
        row for row in product_payload["rows"] if row["cell"] == 3
    )
    cofactor = sp.sympify(product_row["stripped_expressions"][chart])
    product_kernel = tuple(
        sp.sympify(value) for value in product_row["kernel_cofactor_expressions"]
    )
    beta_scale = sp.expand(
        product_kernel[0]
        + product_kernel[1] * labels[1]
        + product_kernel[2] * labels[1] ** 2
    )
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

    normalized_guards = []
    seen = set()
    for expression in [cofactor, *route_guards]:
        value = sp.Poly(expression, *variables, modulus=PRIME)
        if value.total_degree() == 0:
            continue
        normalized = value.monic().as_expr()
        key = str(normalized)
        if key not in seen:
            seen.add(key)
            normalized_guards.append(normalized)

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
        for index, value in enumerate(normalized_guards)
    )
    saturation_stages = "\n".join(
        f"ideal H{index}=h{index}; "
        f"list S{index}=sat(G,H{index}); G=S{index}[1]; G=slimgb(G); "
        f'print("SAT={index},DIM="+string(dim(G))+",SIZE="+string(size(G)));'
        for index in range(len(normalized_guards))
    )
    beta_saturation_stages = "\n".join(
        f"list BS{index}=sat(Jbeta,H{index}); "
        f"Jbeta=BS{index}[1]; Jbeta=slimgb(Jbeta); "
        f'print("BETA_SAT={index},DIM="+string(dim(Jbeta))'
        f'+",SIZE="+string(size(Jbeta)));'
        for index in range(len(normalized_guards))
    )
    generators = ",".join(f"q{index}" for index in range(len(equations)))
    program = f"""
LIB "elim.lib";
ring R={PRIME},(t,r,c,b),dp;
option(redSB);
{equation_definitions}
{guard_definitions}
poly beta={singular(beta_scale)};
ideal I={generators};
ideal G=slimgb(I);
{saturation_stages}
ideal Jbeta=G,beta; Jbeta=slimgb(Jbeta);
{beta_saturation_stages}
ideal Ejt=eliminate(Jbeta,r*c*b); Ejt=slimgb(Ejt);
ideal Etr=eliminate(G,c*b); Etr=slimgb(Etr);
ideal Erb=eliminate(G,t*c); Erb=slimgb(Erb);
ideal Ebt=eliminate(G,r*c); Ebt=slimgb(Ebt);
ideal Erc=eliminate(G,t*b); Erc=slimgb(Erc);
print("BEGIN");
print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
print("JBETA_DIM="+string(dim(Jbeta))); print("JBETA_SIZE="+string(size(Jbeta)));
if ((size(Jbeta)==1) && (Jbeta[1]==1)) {{ print("BETA_UNIT=1"); }}
else {{ print("BETA_UNIT=0"); }}
print("EJT_DIM="+string(dim(Ejt))); print("EJT_SIZE="+string(size(Ejt)));
print("ETR_DIM="+string(dim(Etr))); print("ETR_SIZE="+string(size(Etr)));
print("ERB_DIM="+string(dim(Erb))); print("ERB_SIZE="+string(size(Erb)));
print("EBT_DIM="+string(dim(Ebt))); print("EBT_SIZE="+string(size(Ebt)));
print("ERC_DIM="+string(dim(Erc))); print("ERC_SIZE="+string(size(Erc)));
print("ETR_BEGIN"); Etr; print("ETR_END");
print("ERB_BEGIN"); Erb; print("ERB_END");
print("EBT_BEGIN"); Ebt; print("EBT_END");
print("ERC_BEGIN"); Erc; print("ERC_END");
print("EJT_BEGIN"); Ejt; print("EJT_END");
print("END");
quit;
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
            "epsilon": [epsilon_1, epsilon_2],
            "chart": chart,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout)[-12000:],
            "partial_stderr": decoded(error.stderr)[-2000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }

    stdout = process.stdout

    def parse_polynomial(body):
        expression = 0
        symbols = {"t": t, "r": r, "c": c, "b": b}
        for term in re.findall(r"[+-]?[^+-]+", "".join(body.split())):
            sign = -1 if term.startswith("-") else 1
            unsigned = term.lstrip("+-")
            digits = re.match(r"\d*", unsigned).group()
            coefficient = int(digits or "1") * sign
            monomial = sp.Integer(coefficient)
            for variable, exponent in re.findall(
                r"([trcb])(\d*)", unsigned[len(digits):]
            ):
                monomial *= symbols[variable] ** int(exponent or "1")
            expression += monomial
        return sp.Poly(expression, *variables, modulus=PRIME)

    def extract_ideal(name):
        match = re.search(
            rf"{name}_BEGIN\n(.*?)\n{name}_END", stdout, re.DOTALL
        )
        if match is None:
            return []
        body = match.group(1)
        rows = re.findall(
            rf"^{name.title()}\[\d+\]=(.*?)(?=^{name.title()}\[\d+\]=|\Z)",
            body,
            re.MULTILINE | re.DOTALL,
        )
        output = []
        for row in rows:
            polynomial = parse_polynomial(row)
            expression = str(polynomial.as_expr())
            output.append({
                "degree": polynomial.total_degree(),
                "terms": len(polynomial.terms()),
                "sha256": hashlib.sha256(expression.encode()).hexdigest(),
                "expression": expression,
            })
        return output

    def integer(label):
        match = re.search(rf"(?:^|\n){label}=(-?\d+)", stdout)
        return int(match.group(1)) if match else None

    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    return {
        "epsilon": [epsilon_1, epsilon_2],
        "chart": chart,
        "status": "COMPLETE" if valid else "ERROR",
        "dimension": integer("DIM"),
        "basis_size": integer("SIZE"),
        "beta_boundary_dimension": integer("JBETA_DIM"),
        "beta_boundary_size": integer("JBETA_SIZE"),
        "beta_boundary_unit": "BETA_UNIT=1" in stdout,
        "beta_t_projection_dimension": integer("EJT_DIM"),
        "beta_t_projection_size": integer("EJT_SIZE"),
        "beta_t_projection": extract_ideal("EJT"),
        "projection_dimensions": {
            name.lower(): integer(f"{name}_DIM")
            for name in ("ETR", "ERB", "EBT", "ERC")
        },
        "projection_sizes": {
            name.lower(): integer(f"{name}_SIZE")
            for name in ("ETR", "ERB", "EBT", "ERC")
        },
        "projections": {
            name.lower(): extract_ideal(name)
            for name in ("ETR", "ERB", "EBT", "ERC")
        },
        "equation_summaries": [
            {
                "degree": sp.Poly(value, *variables, modulus=PRIME).total_degree(),
                "terms": len(sp.Poly(value, *variables, modulus=PRIME).terms()),
                "sha256": hashlib.sha256(str(value).encode()).hexdigest(),
            }
            for value in equations
        ],
        "stdout_tail": stdout[-12000:],
        "stderr": process.stderr[-2000:],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
    }


@app.local_entrypoint()
def main(signs: str = "-1:-1", charts: str = "1"):
    selected_signs = tuple(
        tuple(int(value) for value in pair.split(":"))
        for pair in signs.split(",") if pair
    )
    cases = tuple(
        (epsilon_1, epsilon_2, int(chart))
        for epsilon_1, epsilon_2 in selected_signs
        for chart in charts.split(",") if chart
    )
    raw = list(analyze.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]),
                "chart": case[2],
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell3-compact-structure-v1",
        "field": PRIME,
        "scope": (
            "Exact compact common-curve projection probe for cell 3; "
            "no outside, route, K3, LIST, MCA, or Prize claim."
        ),
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {
                "epsilon": row.get("epsilon"),
                "chart": row.get("chart"),
                "status": row.get("status"),
                "dimension": row.get("dimension"),
                "basis_size": row.get("basis_size"),
                "beta_boundary_dimension": row.get("beta_boundary_dimension"),
                "beta_boundary_size": row.get("beta_boundary_size"),
                "beta_boundary_unit": row.get("beta_boundary_unit"),
                "beta_t_projection_dimension": row.get(
                    "beta_t_projection_dimension"
                ),
                "beta_t_projection_size": row.get("beta_t_projection_size"),
                "projection_dimensions": row.get("projection_dimensions"),
                "projection_sizes": row.get("projection_sizes"),
            }
            for row in rows
        ],
    }, sort_keys=True))
