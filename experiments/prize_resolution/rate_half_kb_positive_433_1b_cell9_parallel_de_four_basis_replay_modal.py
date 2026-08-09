#!/usr/bin/env python3
"""Directly replay every cell-9 parallel-DE tower candidate."""

import hashlib
import itertools
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
NORM = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_parallel_de_four_basis_norm_result.json"
)
STRUCTURE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_global_common_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_compact_kernel_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_parallel_de_four_basis_replay_result.json"
)
REMOTE_NORM = "/root/norm.json"
REMOTE_STRUCTURE = "/root/structure.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell9-parallel-de-replay")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(NORM, REMOTE_NORM)
    .add_local_file(STRUCTURE, REMOTE_STRUCTURE)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=240, max_containers=8)
def replay(case):
    import re
    import sympy as sp

    epsilon_1, epsilon_2, cut_kind = case
    t, r, c, b = sp.symbols("t r c b")
    symbols = {"c": c, "b": b, "t": t, "r": r}

    def parse_singular(text):
        expression = 0
        for term in re.findall(r"[+-]?[^+-]+", text):
            sign = -1 if term.startswith("-") else 1
            unsigned = term.lstrip("+-")
            digits = re.match(r"\d*", unsigned).group()
            monomial = sp.Integer(sign * int(digits or "1"))
            for variable, exponent in re.findall(
                r"([cbtr])(\d*)", unsigned[len(digits):]
            ):
                monomial *= symbols[variable] ** int(exponent or "1")
            expression += monomial
        return sp.Poly(expression, c, b, t, r, modulus=PRIME).as_expr()

    norm = json.loads(Path(REMOTE_NORM).read_text())
    norm_rows = [
        row for row in norm["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
        and row["cut_kind"] == cut_kind
    ]
    if len(norm_rows) != 6 or any(
        row.get("status") != "COMPLETE" for row in norm_rows
    ):
        raise RuntimeError("incomplete norm chart cover")
    candidate_roots = sorted({
        value for row in norm_rows for value in row["candidate_roots"]
    })
    source_root_sets = {
        tuple(row["source_roots"]) for row in norm_rows
    }

    structure = json.loads(Path(REMOTE_STRUCTURE).read_text())
    structure_row = next(
        row for row in structure["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    basis = [parse_singular(item["expression"])
             for item in structure_row["lex_basis"]]
    base = basis[0]
    b_relations = basis[1:3]
    c_relations = basis[3:6]
    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    kernel_row = next(
        row for row in kernel_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    kernel = [sp.sympify(item["expression"])
              for item in kernel_row["kernel"]]

    def roots(expression, variable):
        polynomial = sp.Poly(expression, variable, modulus=PRIME)
        if polynomial.is_zero:
            return None
        _, factors = sp.factor_list(polynomial.as_expr(), variable, modulus=PRIME)
        output = []
        for factor, multiplicity in factors:
            row = sp.Poly(factor, variable, modulus=PRIME)
            if row.degree() != 1:
                continue
            leading, constant = (
                int(coefficient) % PRIME for coefficient in row.all_coeffs()
            )
            root = -constant*pow(leading, -1, PRIME) % PRIME
            output.extend([root] * int(multiplicity))
        return sorted(set(output))

    def value(expression, point):
        return int(expression.subs({
            t: point.get("t", 0), r: point.get("r", 0),
            b: point.get("b", 0), c: point.get("c", 0),
        })) % PRIME

    def guarded(point):
        r_value, t_value = point["r"], point["t"]
        b_value, c_value = point["b"], point["c"]
        return all(item % PRIME for item in (
            r_value, t_value, b_value, c_value,
            b_value-1, b_value+1, c_value-1, c_value+1,
            b_value-c_value, b_value+c_value,
            r_value*r_value-1, r_value*r_value+1,
            t_value*t_value-1, t_value*t_value+1,
            t_value*t_value-r_value*r_value,
            t_value*t_value+r_value*r_value,
        ))

    route_boundary = []
    no_lift = []
    finite_rows = []
    witnesses = []
    missing_free = []
    unresolved = []
    for r_value in candidate_roots:
        base_specialized = base.subs(r, r_value)
        t_roots = roots(base_specialized, t)
        if t_roots is None:
            unresolved.append({"r": r_value, "reason": "FREE_T"})
            continue
        if not t_roots:
            no_lift.append({"r": r_value, "stage": "NO_T"})
        for t_value in t_roots:
            point_rt = {"r": r_value, "t": t_value}
            if any(item % PRIME == 0 for item in (
                r_value, t_value, r_value*r_value-1,
                r_value*r_value+1, t_value*t_value-1,
                t_value*t_value+1, t_value*t_value-r_value*r_value,
                t_value*t_value+r_value*r_value,
            )):
                route_boundary.append(point_rt)
                continue
            b_root_sets = [
                roots(expression.subs({r: r_value, t: t_value}), b)
                for expression in b_relations
            ]
            if all(items is None for items in b_root_sets):
                unresolved.append({**point_rt, "reason": "FREE_B"})
                continue
            b_roots = sorted({
                item for items in b_root_sets if items is not None
                for item in items
            })
            if not b_roots:
                no_lift.append({**point_rt, "stage": "NO_B"})
            for b_value in b_roots:
                point_rtb = {**point_rt, "b": b_value}
                if b_value in (0, 1, PRIME-1):
                    route_boundary.append(point_rtb)
                    continue
                c_root_sets = [
                    roots(expression.subs({
                        r: r_value, t: t_value, b: b_value,
                    }), c)
                    for expression in c_relations
                ]
                if all(items is None for items in c_root_sets):
                    unresolved.append({**point_rtb, "reason": "FREE_C"})
                    continue
                c_roots = sorted({
                    item for items in c_root_sets if items is not None
                    for item in items
                })
                if not c_roots:
                    no_lift.append({**point_rtb, "stage": "NO_C"})
                for c_value in c_roots:
                    point = {**point_rtb, "c": c_value}
                    basis_values = [value(expression, point) for expression in basis]
                    if any(basis_values):
                        continue
                    if not guarded(point):
                        route_boundary.append(point)
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
                                **row, "status": "MISSING_IMPOSSIBLE",
                            })
                        else:
                            missing_free.append({
                                **row, "status": "MISSING_FREE",
                            })
                        continue
                    missing = bv*pow(av, -1, PRIME) % PRIME

                    def paired(left, right):
                        p0, p1, p2 = (
                            (b_item-left*a_item) % PRIME
                            for a_item, b_item in zip(
                                a_coefficients, b_coefficients
                            )
                        )
                        q0 = (b_coefficients[0]-right*a_coefficients[0]) % PRIME
                        q1 = (-b_coefficients[1]+right*a_coefficients[1]) % PRIME
                        q2 = (b_coefficients[2]-right*a_coefficients[2]) % PRIME
                        return (pow((p2*q0-p0*q2) % PRIME, 2, PRIME)
                                - (p2*q1-p1*q2)*(p1*q0-p0*q1)) % PRIME

                    cut = (
                        paired(missing, -missing % PRIME)
                        if cut_kind == "positive"
                        else paired(-missing % PRIME, -missing % PRIME)
                    )
                    finite = {
                        **point, "missing": missing, "cut": cut,
                        "status": "ZERO" if cut == 0 else "NONZERO",
                    }
                    finite_rows.append(finite)
                    if cut == 0:
                        witnesses.append(finite)

    return {
        "epsilon": [epsilon_1, epsilon_2],
        "cut_kind": cut_kind,
        "status": "COMPLETE" if not unresolved else "INCOMPLETE",
        "chart_source_root_sets_equal": len(source_root_sets) == 1,
        "source_roots": list(next(iter(source_root_sets))),
        "candidate_roots": candidate_roots,
        "candidate_root_count": len(candidate_roots),
        "route_boundary": route_boundary,
        "no_lift": no_lift,
        "finite_rows": finite_rows,
        "witnesses": witnesses,
        "missing_free": missing_free,
        "unresolved": unresolved,
    }


@app.local_entrypoint()
def main():
    cases = tuple(
        (*epsilon, cut_kind)
        for epsilon in itertools.product((-1, 1), repeat=2)
        for cut_kind in ("positive", "negative")
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
        "schema": "rate-half-kb-positive-433-1b-cell9-parallel-de-replay-v1",
        "field": PRIME,
        "scope": (
            "Complete deployed direct replay of every cell-9 four-basis norm "
            "and inverse candidate against all seven common-curve equations."
        ),
        "source_norm_sha256": hashlib.sha256(NORM.read_bytes()).hexdigest(),
        "source_structure_sha256": hashlib.sha256(
            STRUCTURE.read_bytes()
        ).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT), "cases": len(rows),
        "complete": sum(row.get("status") == "COMPLETE" for row in rows),
        "source_root_sets_equal": sum(
            bool(row.get("chart_source_root_sets_equal")) for row in rows
        ),
        "candidate_roots": sum(row.get("candidate_root_count", 0) for row in rows),
        "finite_points": sum(len(row.get("finite_rows", [])) for row in rows),
        "route_boundary": sum(len(row.get("route_boundary", [])) for row in rows),
        "no_lift": sum(len(row.get("no_lift", [])) for row in rows),
        "witnesses": sum(len(row.get("witnesses", [])) for row in rows),
        "missing_free": sum(len(row.get("missing_free", [])) for row in rows),
        "unresolved": sum(len(row.get("unresolved", [])) for row in rows),
        "rows": [{
            "epsilon": row.get("epsilon"), "cut_kind": row.get("cut_kind"),
            "status": row.get("status"),
            "candidates": row.get("candidate_root_count"),
            "finite": len(row.get("finite_rows", [])),
            "witnesses": len(row.get("witnesses", [])),
            "missing_free": len(row.get("missing_free", [])),
            "unresolved": len(row.get("unresolved", [])),
        } for row in rows],
    }, sort_keys=True))
