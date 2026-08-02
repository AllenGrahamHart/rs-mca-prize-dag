#!/usr/bin/env python3
"""Exact deployed-field rational points of finite 433-1b rank-drop schemes."""

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
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_rankdrop_fglm_profile_result.json"
REMOTE_COMMON = "/root/common.py"
REMOTE_PRODUCT = "/root/product.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-rankdrop-fglm-profile")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
)


@app.function(image=image, cpu=1.0, memory=3072, timeout=270, max_containers=20)
def profile_case(case):
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from common import compile_cell

    cell, epsilon_1, epsilon_2 = case
    variables, _, metadata = compile_cell(cell, epsilon_1, epsilon_2)
    t, r, c, b = variables
    rows = []
    for product, label in zip(metadata["products"], metadata["labels"]):
        rows.append([
            -product, -product * label, -product * label**2,
            1, label, label**2, 0, 0,
        ])
    for root, label, edge_sum in zip(
        metadata["roots"], metadata["labels"], metadata["sums"]
    ):
        q = sp.expand(root * edge_sum)
        rows.append([
            q, q * label, q * label**2,
            0, 0, 0, label, label**2,
        ])

    def singular(expression):
        return str(sp.Poly(expression, t, r, c, b, modulus=PRIME).as_expr()).replace(
            "**", "^"
        )

    entries = ",".join(singular(value) for row in rows for value in row)
    product_payload = json.loads(Path(REMOTE_PRODUCT).read_text())
    product_row = next(row for row in product_payload["rows"]
                       if row["cell"] == cell)
    definitions = "\n".join(
        f"poly f{index}={value.replace('**', '^')};"
        for index, value in enumerate(product_row["stripped_expressions"])
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
matrix M[10][8]={entries};
ideal J=minor(M,8);
ideal I=f0,f1,f2,f3,f4,f5,J,z*({guard})-1;
ideal G=std(I);
print("DP_DIM="+string(dim(G)));
print("DP_SIZE="+string(size(G)));
ring L={PRIME},(z,t,r,c,b),lp;
option(redSB);
ideal H=fglm(R,G);
print("LEX_BEGIN");
print("LEX_SIZE="+string(size(H)));
H;
print("LEX_END");
quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=240,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "cell": cell,
            "status": "TIMEOUT",
            "partial_stdout": (error.stdout or "")[-20000:],
            "partial_stderr": (error.stderr or "")[-4000:],
        }
    stdout = process.stdout
    eliminant_match = re.search(r"H\[1\]=(.*)", stdout)
    factors = []
    eliminant = None
    rational_points = []
    if eliminant_match:
        eliminant = eliminant_match.group(1).strip()
        parsed = re.sub(r"([a-zA-Z])(\d+)", r"\1**\2", eliminant)
        parsed = re.sub(r"(?<=\d)(?=[a-zA-Z])", "*", parsed)
        variable = sp.symbols("b")
        eliminant_polynomial = sp.Poly(sp.sympify(parsed), variable, modulus=PRIME)
        _, factor_rows = sp.factor_list(eliminant_polynomial.as_expr(), variable,
                                        modulus=PRIME)
        linear_roots = []
        for factor, multiplicity in factor_rows:
            polynomial = sp.Poly(factor, variable, modulus=PRIME).monic()
            factors.append({
                "degree": polynomial.degree(),
                "multiplicity": multiplicity,
                "expression": str(polynomial.as_expr()),
                "sha256": hashlib.sha256(
                    str(polynomial.as_expr()).encode()
                ).hexdigest(),
            })
            if polynomial.degree() == 1:
                leading, constant = (
                    int(value) % PRIME for value in polynomial.all_coeffs()
                )
                root = (-constant * pow(leading, -1, PRIME)) % PRIME
                linear_roots.extend([root] * multiplicity)

        basis_lines = {
            int(index): expression.strip()
            for index, expression in re.findall(r"H\[(\d+)\]=(.*)", stdout)
        }

        def parse_singular(expression):
            converted = re.sub(r"([a-zA-Z])(\d+)", r"\1**\2", expression)
            converted = re.sub(r"(?<=\d)(?=[a-zA-Z])", "*", converted)
            return sp.sympify(converted)

        symbols = {name: sp.symbols(name) for name in ("b", "c", "r", "t", "z")}
        for root in sorted(linear_roots):
            point = {"b": root}
            for basis_index, name in ((2, "c"), (3, "r"), (4, "t"), (5, "z")):
                expression = parse_singular(basis_lines[basis_index]).subs(
                    symbols["b"], root
                )
                polynomial = sp.Poly(expression, symbols[name], modulus=PRIME)
                coefficient = int(polynomial.coeff_monomial(symbols[name])) % PRIME
                constant = int(polynomial.coeff_monomial(1)) % PRIME
                point[name] = (-constant * pow(coefficient, -1, PRIME)) % PRIME
            bv, cv, rv, tv = (point[name] for name in ("b", "c", "r", "t"))
            guards = (
                rv, tv, bv, cv, bv - 1, bv + 1, cv - 1, cv + 1,
                bv - cv, bv + cv, rv*rv - 1, rv*rv + 1,
                tv*tv - 1, tv*tv + 1, tv*tv - rv*rv, tv*tv + rv*rv,
            )
            point["guard_nonzero"] = all(value % PRIME for value in guards)
            rational_points.append(point)
    return {
        "cell": cell,
        "epsilon": [epsilon_1, epsilon_2],
        "status": "COMPLETE" if (
            process.returncode == 0 and "LEX_END" in stdout and "?" not in stdout
        ) else "ERROR",
        "eliminant": eliminant,
        "factors": factors,
        "linear_factor_count": sum(
            row["multiplicity"] for row in factors if row["degree"] == 1
        ),
        "rational_points": rational_points,
        "stdout": stdout[-60000:],
        "stderr": process.stderr[-4000:],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
    }


@app.local_entrypoint()
def main(cells: str = "4,5,7,8,9,10,11,12,13,14"):
    selected = tuple(int(value) for value in cells.split(",") if value)
    cases = tuple(itertools.product(selected, (-1, 1), (-1, 1)))
    raw = list(profile_case.map(
        cases, order_outputs=True, return_exceptions=True,
    ))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "cell": case[0], "epsilon": list(case[1:]),
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-rankdrop-rational-classifier-v2",
        "scope": (
            "Exact FGLM eliminants, deployed-field factors, and guarded "
            "rational-point reconstruction for all 40 finite exceptional rows."
        ),
        "field": PRIME,
        "source_common_sha256": hashlib.sha256(COMMON.read_bytes()).hexdigest(),
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {"cell": row["cell"], "epsilon": row["epsilon"],
             "status": row["status"],
             "linear_factor_count": row.get("linear_factor_count"),
             "rational_points": len(row.get("rational_points", []))}
            for row in rows
        ],
    }, sort_keys=True))
