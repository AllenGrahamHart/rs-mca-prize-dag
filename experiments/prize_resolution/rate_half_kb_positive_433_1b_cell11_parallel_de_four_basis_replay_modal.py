#!/usr/bin/env python3
"""Directly replay every candidate from the cell-11 parallel-DE norms."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
NORM = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_parallel_de_four_basis_norm_result.json"
)
TOWER = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_parallel_de_four_basis_replay_result.json"
)
REMOTE_NORM = "/root/norm.json"
REMOTE_TOWER = "/root/tower.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell11-parallel-de-replay")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(NORM, REMOTE_NORM)
    .add_local_file(TOWER, REMOTE_TOWER)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=8)
def replay(case):
    import sympy as sp

    epsilon_1, epsilon_2, cut_kind = case
    t, r, c, b = sp.symbols("t r c b")
    variables = (t, r, c, b)
    norm = json.loads(Path(REMOTE_NORM).read_text())
    norm_row = next(
        row for row in norm["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
        and row["cut_kind"] == cut_kind
    )
    tower = json.loads(Path(REMOTE_TOWER).read_text())
    tower_row = next(
        row for row in tower["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
        and row["c_row_index"] == 5
    )
    base = sp.sympify(tower_row["base"]["expression"])
    b_relation = sp.sympify(tower_row["b_relation"]["expression"])
    c_relation = sp.sympify(tower_row["c_relation"]["expression"])
    b_leading = sp.sympify(tower_row["b_leading"]["expression"])
    c_leading = sp.sympify(tower_row["c_leading"]["expression"])
    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    kernel_row = next(
        row for row in kernel_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    kernel = [sp.sympify(item["expression"]) for item in kernel_row["kernel"]]

    def roots(expression, variable):
        polynomial = sp.Poly(expression, variable, modulus=PRIME)
        if polynomial.is_zero:
            return None
        _, factors = sp.factor_list(polynomial.as_expr(), variable, modulus=PRIME)
        output = []
        for factor, _ in factors:
            row = sp.Poly(factor, variable, modulus=PRIME)
            if row.degree() != 1:
                continue
            leading, constant = (
                int(coefficient) % PRIME for coefficient in row.all_coeffs()
            )
            output.append(-constant*pow(leading, -1, PRIME) % PRIME)
        return sorted(set(output))

    def value(expression, point):
        return int(expression.subs({
            t: point.get("t", 0), r: point.get("r", 0),
            b: point.get("b", 0), c: point.get("c", 0),
        })) % PRIME

    route_boundary = []
    leading_boundary = []
    no_lift = []
    finite_rows = []
    witnesses = []
    unresolved = []
    for r_value in norm_row["candidate_roots"]:
        if any(item % PRIME == 0 for item in (
            r_value, r_value-1, r_value+1,
            r_value*r_value-1, r_value*r_value+1,
        )):
            route_boundary.append({"r": r_value, "stage": "R_GUARD"})
            continue
        t_roots = roots(base.subs(r, r_value), t)
        if t_roots is None:
            unresolved.append({"r": r_value, "reason": "FREE_T"})
            continue
        if not t_roots:
            no_lift.append({"r": r_value, "stage": "NO_T"})
        for t_value in t_roots:
            point_rt = {"r": r_value, "t": t_value}
            if any(item % PRIME == 0 for item in (
                t_value, t_value-1, t_value+1,
                t_value*t_value-1, t_value*t_value+1,
                t_value*t_value-r_value*r_value,
                t_value*t_value+r_value*r_value,
            )):
                route_boundary.append({**point_rt, "stage": "T_GUARD"})
                continue
            if value(b_leading, point_rt) == 0:
                leading_boundary.append({**point_rt, "stage": "B_LEADING"})
                continue
            b_roots = roots(b_relation.subs({r: r_value, t: t_value}), b)
            if b_roots is None:
                unresolved.append({**point_rt, "reason": "FREE_B"})
                continue
            if not b_roots:
                no_lift.append({**point_rt, "stage": "NO_B"})
            for b_value in b_roots:
                point_rtb = {**point_rt, "b": b_value}
                if b_value in (0, 1, PRIME-1):
                    route_boundary.append({**point_rtb, "stage": "B_GUARD"})
                    continue
                if value(c_leading, point_rtb) == 0:
                    leading_boundary.append({**point_rtb, "stage": "C_LEADING"})
                    continue
                c_polynomial = sp.Poly(
                    c_relation.subs({r: r_value, t: t_value, b: b_value}),
                    c, modulus=PRIME,
                )
                coefficient = int(c_polynomial.coeff_monomial(c)) % PRIME
                constant = int(c_polynomial.coeff_monomial(1)) % PRIME
                if coefficient == 0:
                    if constant == 0:
                        unresolved.append({**point_rtb, "reason": "FREE_C"})
                    continue
                c_value = -constant*pow(coefficient, -1, PRIME) % PRIME
                point = {**point_rtb, "c": c_value}
                if any(item % PRIME == 0 for item in (
                    c_value, c_value-1, c_value+1,
                    b_value-c_value, b_value+c_value,
                )):
                    route_boundary.append({**point, "stage": "FULL_GUARD"})
                    continue
                values = [value(expression, point) for expression in kernel]
                a_coefficients, b_coefficients = values[:3], values[3:6]
                label = -t_value*t_value % PRIME
                av = sum(item*pow(label, index, PRIME)
                         for index, item in enumerate(a_coefficients)) % PRIME
                bv = sum(item*pow(label, index, PRIME)
                         for index, item in enumerate(b_coefficients)) % PRIME
                if av == 0:
                    row = {**point, "missing_numerator": bv}
                    if bv:
                        finite_rows.append({
                            **row, "status": "MISSING_IMPOSSIBLE"
                        })
                    else:
                        unresolved.append({**row, "reason": "MISSING_FREE"})
                    continue
                missing = bv*pow(av, -1, PRIME) % PRIME

                def paired(left, right):
                    p0, p1, p2 = (
                        (b_item-left*a_item) % PRIME
                        for a_item, b_item in zip(a_coefficients, b_coefficients)
                    )
                    q0 = (b_coefficients[0]-right*a_coefficients[0]) % PRIME
                    q1 = (-b_coefficients[1]+right*a_coefficients[1]) % PRIME
                    q2 = (b_coefficients[2]-right*a_coefficients[2]) % PRIME
                    return (pow((p2*q0-p0*q2) % PRIME, 2, PRIME)
                            - (p2*q1-p1*q2)*(p1*q0-p0*q1)) % PRIME

                cut = (paired(missing, -missing % PRIME)
                       if cut_kind == "opposite"
                       else paired(-missing % PRIME, -missing % PRIME))
                finite = {**point, "missing": missing, "cut": cut,
                          "status": "ZERO" if cut == 0 else "NONZERO"}
                finite_rows.append(finite)
                if cut == 0:
                    witnesses.append(finite)

    return {
        "epsilon": [epsilon_1, epsilon_2], "cut_kind": cut_kind,
        "status": "COMPLETE" if not unresolved else "INCOMPLETE",
        "candidate_root_count": len(norm_row["candidate_roots"]),
        "route_boundary": route_boundary, "leading_boundary": leading_boundary,
        "no_lift": no_lift, "finite_rows": finite_rows,
        "witnesses": witnesses, "unresolved": unresolved,
        "excluded_generic": not witnesses and not unresolved,
    }


@app.local_entrypoint()
def main():
    cases = tuple(
        (epsilon_1, epsilon_2, cut_kind)
        for epsilon_1 in (-1, 1) for epsilon_2 in (-1, 1)
        for cut_kind in ("opposite", "equal_negative")
    )
    raw = list(replay.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "cut_kind": case[2],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell11-parallel-de-replay-v1",
        "field": PRIME,
        "scope": (
            "Complete deployed direct replay of every four-basis norm and "
            "inverse candidate for the cell-11 first-pair parallel-DE cuts."
        ),
        "source_norm_sha256": hashlib.sha256(NORM.read_bytes()).hexdigest(),
        "source_tower_sha256": hashlib.sha256(TOWER.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT), "cases": len(rows),
        "complete": sum(row.get("status") == "COMPLETE" for row in rows),
        "candidate_roots": sum(row.get("candidate_root_count", 0) for row in rows),
        "finite_points": sum(len(row.get("finite_rows", [])) for row in rows),
        "route_boundary": sum(len(row.get("route_boundary", [])) for row in rows),
        "leading_boundary": sum(len(row.get("leading_boundary", [])) for row in rows),
        "no_lift": sum(len(row.get("no_lift", [])) for row in rows),
        "witnesses": sum(len(row.get("witnesses", [])) for row in rows),
        "unresolved": sum(len(row.get("unresolved", [])) for row in rows),
    }, sort_keys=True))
