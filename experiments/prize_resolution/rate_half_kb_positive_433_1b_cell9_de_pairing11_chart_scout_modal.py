#!/usr/bin/env python3
"""Scout the pinned pairing-11 compiler on the six cell-9 tower charts."""

import ast
import hashlib
import itertools
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
TEMPLATE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell4_de_pairing11_"
    "common_f_resultant_modal.py"
)
TOWER = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_four_basis_tower_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_compact_kernel_result.json"
)
BASE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_kernel_null_residual_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_de_pairing11_chart_scout_result.json"
)
FULL_RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_de_pairing11_chart_result"
)
REMOTE_TEMPLATE = "/root/template.py"
REMOTE_TOWER = "/root/tower.json"
REMOTE_KERNEL = "/root/kernel.json"
REMOTE_BASE = "/root/base.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell9-de-pairing11-chart-scout")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(TEMPLATE, REMOTE_TEMPLATE)
    .add_local_file(TOWER, REMOTE_TOWER)
    .add_local_file(KERNEL, REMOTE_KERNEL)
    .add_local_file(BASE, REMOTE_BASE)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=420, max_containers=12)
def evaluate(case):
    import time

    import sympy as sp

    epsilon_1, epsilon_2, sigma_c, sigma_o, xi_index, b_index, c_index = case
    tower = json.loads(Path(REMOTE_TOWER).read_text())
    tower_row = next(
        row for row in tower["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
        and row["b_row_index"] == b_index
        and row["c_row_index"] == c_index
    )
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

    lex_basis = [{"expression": "0"} for _ in range(6)]
    lex_basis[0]["expression"] = singular_text(tower_row["base"]["expression"])
    lex_basis[1]["expression"] = singular_text(
        tower_row["b_relation"]["expression"]
    )
    lex_basis[5]["expression"] = singular_text(
        tower_row["c_relation"]["expression"]
    )
    structure_path = Path("/tmp/cell9_structure.json")
    structure_path.write_text(json.dumps({
        "rows": [{
            "epsilon": [epsilon_1, epsilon_2],
            "chart": 0,
            "lex_basis": lex_basis,
        }]
    }))

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
    result = namespace["evaluate_case"](
        (epsilon_1, epsilon_2, sigma_c, sigma_o, xi_index)
    )

    b_leading = sp.sympify(tower_row["b_leading"]["expression"])
    c_leading = sp.sympify(tower_row["c_leading"]["expression"])
    base_payload = json.loads(Path(REMOTE_BASE).read_text())
    base_points = {
        tuple(row["point"][key] for key in ("r", "t", "b", "c"))
        for row in base_payload["rows"]
    }
    unresolved = []
    paid = []
    for item in result["unresolved"]:
        substitutions = {
            r: item.get("r", 0), t: item.get("t", 0),
            b: item.get("b", 0), c: item.get("c", 0),
        }
        point_key = tuple(item.get(key) for key in ("r", "t", "b", "c"))
        if (item["reason"] == "FREE_B"
                and int(b_leading.subs(substitutions)) % PRIME == 0):
            paid.append({**item, "stage": "CHART_B_LEADING"})
        elif (item["reason"] == "FREE_C"
              and int(c_leading.subs(substitutions)) % PRIME == 0):
            paid.append({**item, "stage": "CHART_C_LEADING"})
        elif item["reason"] == "MISSING_FREE" and point_key in base_points:
            paid.append({**item, "stage": "REGULARIZED_BASE"})
        else:
            unresolved.append(item)
    result["unresolved"] = unresolved
    result["paid_rows"] = paid
    result["status"] = "COMPLETE" if not unresolved else "INCOMPLETE"
    result["excluded"] = not unresolved and not result["witnesses"]
    result["b_row_index"] = b_index
    result["c_row_index"] = c_index
    return result


@app.local_entrypoint()
def main(limit: int = 0, full: bool = False):
    cases = tuple(
        (*epsilon, sigma_c, sigma_o, xi_index, b_index, c_index)
        for epsilon in itertools.product((-1, 1), repeat=2)
        for sigma_c in (-1, 1) for sigma_o in (-1, 1)
        for xi_index in (0, 2)
        for b_index in (2, 3) for c_index in (4, 5, 6)
    )
    if limit:
        cases = cases[:limit]
    raw = list(evaluate.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    full_rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            error = {
                "epsilon": list(case[:2]), "sigma": list(case[2:4]),
                "xi_index": case[4], "b_row_index": case[5],
                "c_row_index": case[6], "status": "REMOTE_ERROR",
                "error": repr(row),
            }
            rows.append(error)
            full_rows.append(error)
            continue
        certificate = dict(row)
        certificate.pop("timings", None)
        full_rows.append(certificate)
        rows.append({
            "epsilon": row["epsilon"], "sigma": row["sigma"],
            "xi_index": row["xi_index"], "pairing_index": 11,
            "b_row_index": row["b_row_index"],
            "c_row_index": row["c_row_index"],
            "status": row["status"], "excluded": row["excluded"],
            "target_root_count": row["target_root_count"],
            "candidate_root_count": row["candidate_root_count"],
            "source_point_count": row["source_point_count"],
            "route_point_count": row["route_point_count"],
            "finite_row_count": len(row["finite_rows"]),
            "boundary_row_count": len(row["boundary_rows"]),
            "paid_rows": row["paid_rows"],
            "target_boundary_count": len(row["target_boundary_rows"]),
            "colored_solution_count": row["colored_solution_count"],
            "witnesses": row["witnesses"],
            "unresolved": row["unresolved"],
        })
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell9-de-pairing11-chart-scout-v1",
        "field": PRIME,
        "scope": "Compact six-chart feasibility scout; no exclusion claim.",
        "source_template_sha256": hashlib.sha256(TEMPLATE.read_bytes()).hexdigest(),
        "source_tower_sha256": hashlib.sha256(TOWER.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    manifest = None
    if full:
        from tools.sharded_result import ShardedResultWriter

        metadata = {
            "field": PRIME,
            "scope": (
                "Exact six-chart execution of the pinned common-f "
                "pairing-11 compiler for cell-9 xi in {0,2}."
            ),
            "source_template_sha256": hashlib.sha256(
                TEMPLATE.read_bytes()
            ).hexdigest(),
            "source_tower_sha256": hashlib.sha256(TOWER.read_bytes()).hexdigest(),
            "source_kernel_sha256": hashlib.sha256(
                KERNEL.read_bytes()
            ).hexdigest(),
            "source_base_sha256": hashlib.sha256(BASE.read_bytes()).hexdigest(),
        }
        writer = ShardedResultWriter(
            FULL_RESULT, metadata=metadata, shard_records=32
        )
        for row in full_rows:
            writer.add(row)
        manifest = writer.close(complete=(
            len(full_rows) == 192
            and all(row.get("status") != "REMOTE_ERROR" for row in full_rows)
        ))
    print(json.dumps({
        "result": str(RESULT), "rows": len(rows),
        "manifest": None if manifest is None else str(manifest),
        "complete": sum(row["status"] == "COMPLETE" for row in rows),
        "excluded": sum(bool(row.get("excluded")) for row in rows),
        "colored": sum(row.get("colored_solution_count", 0) for row in rows),
        "witnesses": sum(len(row.get("witnesses", [])) for row in rows),
        "unresolved": sum(len(row.get("unresolved", [])) for row in rows),
        "paid": sum(len(row.get("paid_rows", [])) for row in rows),
        "summary": rows,
    }, sort_keys=True))
