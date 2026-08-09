#!/usr/bin/env python3
"""Scout the pinned xi=3 pairing-0 compiler on cell-9 charts."""

import ast
import hashlib
import itertools
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
TEMPLATE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing0_"
    "reciprocal_square_modal.py"
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
    "rate_half_kb_positive_433_1b_cell9_xi3_pairing0_chart_scout_result.json"
)
FULL_RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_xi3_pairing0_chart_result"
)
REMOTE_TEMPLATE = "/root/template.py"
REMOTE_TOWER = "/root/tower.json"
REMOTE_KERNEL = "/root/kernel.json"
REMOTE_BASE = "/root/base.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell9-xi3-pairing0-chart-scout")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(TEMPLATE, REMOTE_TEMPLATE)
    .add_local_file(TOWER, REMOTE_TOWER)
    .add_local_file(KERNEL, REMOTE_KERNEL)
    .add_local_file(BASE, REMOTE_BASE)
)


def _evaluate_case(case):
    import time

    import sympy as sp

    epsilon_1, epsilon_2, branch_index, sigma_o, b_index, c_index = case
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
        (epsilon_1, epsilon_2, branch_index, sigma_o)
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
    result["target_excluded"] = (
        not unresolved and result["witness_count"] == 0
    )
    result["excluded"] = result["target_excluded"]
    result["b_row_index"] = b_index
    result["c_row_index"] = c_index
    return result


@app.function(image=image, cpu=2.0, memory=4096, timeout=900, max_containers=48)
def evaluate(case):
    try:
        return {"case": list(case), "result": _evaluate_case(case)}
    except Exception as error:
        return {
            "case": list(case),
            "error": f"{type(error).__name__}: {error}",
        }


@app.local_entrypoint()
def main(
    limit: int = 0,
    full: bool = False,
    recovery_index: int = -1,
    recovery_indices: str = "",
):
    cases = tuple(
        (*epsilon, branch_index, sigma_o, b_index, c_index)
        for epsilon in itertools.product((-1, 1), repeat=2)
        for branch_index in range(3) for sigma_o in (-1, 1)
        for b_index in (2, 3) for c_index in (4, 5, 6)
    )
    result_path = RESULT
    full_result = FULL_RESULT
    selected_recovery_indices = ()
    if recovery_indices:
        selected_recovery_indices = tuple(
            int(value.strip()) for value in recovery_indices.split(",")
            if value.strip()
        )
        if (not selected_recovery_indices
                or len(set(selected_recovery_indices))
                != len(selected_recovery_indices)
                or any(index < 0 or index >= len(cases)
                       for index in selected_recovery_indices)):
            raise ValueError("invalid recovery index set")
        cases = tuple(cases[index] for index in selected_recovery_indices)
        suffix = "_recovery_" + "_".join(
            f"{index:03d}" for index in selected_recovery_indices
        )
        result_path = RESULT.with_name(RESULT.stem + suffix + RESULT.suffix)
        full_result = FULL_RESULT.with_name(FULL_RESULT.name + suffix)
    elif recovery_index >= 0:
        if recovery_index >= len(cases):
            raise ValueError("recovery index outside Cartesian case list")
        cases = (cases[recovery_index],)
        suffix = f"_recovery_{recovery_index:03d}"
        result_path = RESULT.with_name(RESULT.stem + suffix + RESULT.suffix)
        full_result = FULL_RESULT.with_name(FULL_RESULT.name + suffix)
    elif limit:
        cases = cases[:limit]
    rows = []
    writer = None
    if full:
        from tools.sharded_result import ShardedResultWriter

        writer = ShardedResultWriter(full_result, metadata={
            "field": PRIME,
            "scope": (
                "Exact six-chart execution of the pinned reciprocal-square "
                "compiler for cell-9 xi=3, pairing=0."
            ),
            "source_template_sha256": hashlib.sha256(TEMPLATE.read_bytes()).hexdigest(),
            "source_tower_sha256": hashlib.sha256(TOWER.read_bytes()).hexdigest(),
            "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
            "source_base_sha256": hashlib.sha256(BASE.read_bytes()).hexdigest(),
        }, shard_records=32)
    remote_errors = 0
    for envelope in evaluate.map(cases, order_outputs=False):
        case = tuple(envelope["case"])
        if "error" in envelope:
            error = {
                "epsilon": list(case[:2]), "branch_index": case[2],
                "sigma_o": case[3], "xi_index": 3,
                "pairing_index": 0, "b_row_index": case[4],
                "c_row_index": case[5], "status": "REMOTE_ERROR",
                "error": envelope["error"],
            }
            rows.append(error)
            if writer is not None:
                writer.add(error)
            remote_errors += 1
            continue
        row = envelope["result"]
        certificate = dict(row)
        certificate.pop("timings", None)
        if writer is not None:
            writer.add(certificate)
        rows.append({
            "epsilon": row["epsilon"],
            "branch_index": row["branch_index"], "sigma_o": row["sigma_o"],
            "xi_index": row["xi_index"], "pairing_index": 0,
            "b_row_index": row["b_row_index"],
            "c_row_index": row["c_row_index"],
            "status": row["status"], "excluded": row["excluded"],
            "target_norm_root_count": row["target_norm_root_count"],
            "candidate_root_count": row["candidate_root_count"],
            "source_point_count": row["source_point_count"],
            "route_point_count": row["route_point_count"],
            "finite_row_count": len(row["finite_rows"]),
            "boundary_row_count": len(row["boundary_rows"]),
            "paid_rows": row["paid_rows"],
            "target_boundary_count": len(row["target_boundary_rows"]),
            "yd_candidate_count": row["yd_candidate_count"],
            "final_pair_solution_count": row["final_pair_solution_count"],
            "witness_count": row["witness_count"],
            "witnesses": row["witnesses"],
            "unresolved": row["unresolved"],
        })
    rows.sort(key=lambda row: (
        tuple(row["epsilon"]), row["branch_index"], row["sigma_o"],
        row["b_row_index"], row["c_row_index"],
    ))
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell9-xi3-pairing0-chart-scout-v1",
        "field": PRIME,
        "scope": "Compact six-chart feasibility scout; no exclusion claim.",
        "source_template_sha256": hashlib.sha256(TEMPLATE.read_bytes()).hexdigest(),
        "source_tower_sha256": hashlib.sha256(TOWER.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    result_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    manifest = None
    if writer is not None:
        expected_rows = (
            len(selected_recovery_indices) if selected_recovery_indices
            else 1 if recovery_index >= 0 else 144
        )
        manifest = writer.close(
            complete=(len(rows) == expected_rows and not remote_errors)
        )
    print(json.dumps({
        "result": str(result_path), "rows": len(rows),
        "manifest": None if manifest is None else str(manifest),
        "complete": sum(row["status"] == "COMPLETE" for row in rows),
        "excluded": sum(bool(row.get("excluded")) for row in rows),
        "final_pair_solutions": sum(
            row.get("final_pair_solution_count", 0) for row in rows
        ),
        "witnesses": sum(row.get("witness_count", 0) for row in rows),
        "unresolved": sum(len(row.get("unresolved", [])) for row in rows),
        "paid": sum(len(row.get("paid_rows", [])) for row in rows),
        "summary": rows,
    }, sort_keys=True))
