#!/usr/bin/env python3
"""Apply the pinned pairing-11 compiler to source-role cell 5."""

import ast
import hashlib
import itertools
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
TEMPLATE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing11_"
    "quadratic_resultant_signfree_modal.py"
)
TOWER = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_xi3_pairing11_"
    "template_adapter_result.json"
)
REMOTE_TEMPLATE = "/root/template.py"
REMOTE_TOWER = "/root/tower.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell11-xi3-pairing11-adapter")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(TEMPLATE, REMOTE_TEMPLATE)
    .add_local_file(TOWER, REMOTE_TOWER)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=8)
def evaluate(case):
    import time

    import sympy as sp

    tower = json.loads(Path(REMOTE_TOWER).read_text())
    t, r, c, b = sp.symbols("t r c b")
    variables = (t, r, c, b)

    def singular_text(expression):
        terms = []
        for exponents, coefficient in sp.Poly(
            sp.sympify(expression), *variables, modulus=PRIME
        ).terms():
            monomial = str(int(coefficient) % PRIME)
            for variable, exponent in zip(variables, exponents):
                if exponent:
                    monomial += str(variable)
                    if exponent != 1:
                        monomial += str(exponent)
            terms.append(monomial)
        return "+".join(terms) if terms else "0"

    rows = []
    for row in tower["rows"]:
        if row["c_row_index"] != 6:
            continue
        lex_basis = [{"expression": "0"} for _ in range(6)]
        lex_basis[0]["expression"] = singular_text(row["base"]["expression"])
        lex_basis[1]["expression"] = singular_text(
            row["b_relation"]["expression"]
        )
        lex_basis[5]["expression"] = singular_text(
            row["c_relation"]["expression"]
        )
        rows.append({
            "epsilon": row["epsilon"], "chart": 0, "lex_basis": lex_basis,
        })
    structure_path = Path("/tmp/cell11_structure.json")
    structure_path.write_text(json.dumps({"rows": rows}))

    tree = ast.parse(Path(REMOTE_TEMPLATE).read_text())
    function = next(
        node for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == "evaluate_case"
    )
    function.decorator_list = []
    module = ast.fix_missing_locations(ast.Module(body=[function], type_ignores=[]))
    namespace = {
        "hashlib": hashlib,
        "json": json,
        "Path": Path,
        "time": time,
        "PRIME": PRIME,
        "REMOTE_STRUCTURE": str(structure_path),
        "REMOTE_KERNEL": REMOTE_KERNEL,
    }
    exec(compile(module, REMOTE_TEMPLATE, "exec"), namespace)
    result = namespace["evaluate_case"](case)

    epsilon = list(case[:2])
    tower_row = next(
        row for row in tower["rows"]
        if row["epsilon"] == epsilon and row["c_row_index"] == 6
    )
    b_leading = sp.sympify(tower_row["b_leading"]["expression"])
    c_leading = sp.sympify(tower_row["c_leading"]["expression"])
    unresolved = []
    for item in result["unresolved"]:
        substitutions = {
            r: item.get("r", 0), t: item.get("t", 0),
            b: item.get("b", 0), c: item.get("c", 0),
        }
        if (
            item["reason"] == "FREE_B"
            and int(b_leading.subs(substitutions)) % PRIME == 0
        ):
            result["boundary_rows"].append({
                **item, "stage": "CELL11_B_LEADING",
            })
        elif (
            item["reason"] == "FREE_C"
            and int(c_leading.subs(substitutions)) % PRIME == 0
        ):
            result["boundary_rows"].append({
                **item, "stage": "CELL11_C_LEADING",
            })
        else:
            unresolved.append(item)
    result["unresolved"] = unresolved
    result["status"] = "COMPLETE" if not unresolved else "INCOMPLETE"
    result["target_excluded"] = not unresolved and result["witness_count"] == 0
    return result


@app.local_entrypoint()
def main(limit: int = 0):
    cases = tuple(
        (*epsilon, sigma_c)
        for epsilon in itertools.product((-1, 1), repeat=2)
        for sigma_c in (-1, 1)
    )
    if limit:
        cases = cases[:limit]
    raw = list(evaluate.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]),
                "sigma_c": case[2],
                "xi_index": 3,
                "pairing_index": 11,
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            certificate = dict(row)
            certificate.pop("timings", None)
            rows.append(certificate)
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-cell11-xi3-pairing11-adapter-v1"
        ),
        "field": PRIME,
        "scope": (
            "Cell-11 execution of the pinned quadratic-resultant sign-free "
            "compiler for xi=3, pairing 11; adapter evidence until audited."
        ),
        "source_template_sha256": hashlib.sha256(TEMPLATE.read_bytes()).hexdigest(),
        "source_tower_sha256": hashlib.sha256(TOWER.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {key: row.get(key) for key in (
                "epsilon", "sigma_c", "pairing_index", "status",
                "candidate_root_count", "source_point_count",
                "route_point_count", "z_candidate_count",
                "q_candidate_count", "final_pair_solution_count",
                "witness_count", "target_excluded", "unresolved",
            )}
            for row in rows
        ],
    }, sort_keys=True))
