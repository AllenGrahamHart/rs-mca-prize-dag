#!/usr/bin/env python3
"""Replay deployed roots of the cell-11 endpoint compatibility cuts."""

import hashlib
import json
from pathlib import Path
import re

import modal


DIRECTORY = Path(__file__).parent
PILOT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_endpoint_compatibility_pilot_result.json"
)
TOWER = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_endpoint_compatibility_replay_result.json"
)
REMOTE_PILOT = "/root/pilot.json"
REMOTE_TOWER = "/root/tower.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell11-endpoint-replay")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(PILOT, REMOTE_PILOT)
    .add_local_file(TOWER, REMOTE_TOWER)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=8)
def replay(case):
    import sympy as sp

    epsilon_1, epsilon_2, endpoint = case
    t, r, c, b = sp.symbols("t r c b")

    def parse_singular_univariate(text):
        value = text.split("=", 1)[-1]
        expression = 0
        for term in re.findall(r"[+-]?[^+-]+", value):
            sign = -1 if term.startswith("-") else 1
            unsigned = term.lstrip("+-")
            digits = re.match(r"\d*", unsigned).group()
            coefficient = sign * int(digits or "1")
            variable = re.search(r"r(\d*)", unsigned[len(digits):])
            exponent = int(variable.group(1) or "1") if variable else 0
            expression += coefficient*r**exponent
        return sp.Poly(expression, r, modulus=PRIME)

    def roots(polynomial, variable):
        value = sp.Poly(polynomial.as_expr(), variable, modulus=PRIME)
        _, factors = sp.factor_list(value.as_expr(), variable, modulus=PRIME)
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

    pilot = json.loads(Path(REMOTE_PILOT).read_text())
    pilot_row = next(row for row in pilot["rows"]
                     if row["epsilon"] == [epsilon_1, epsilon_2]
                     and row["endpoint"] == endpoint)
    eliminant = parse_singular_univariate(pilot_row["r_elimination"])
    r_roots = roots(eliminant, r)
    tower = json.loads(Path(REMOTE_TOWER).read_text())
    tower_row = next(row for row in tower["rows"]
                     if row["epsilon"] == [epsilon_1, epsilon_2]
                     and row["c_row_index"] == 5)
    base = sp.Poly(sp.sympify(tower_row["base"]["expression"]), t, r,
                   modulus=PRIME)
    b_relation = sp.Poly(sp.sympify(tower_row["b_relation"]["expression"]),
                         b, t, r, modulus=PRIME)
    c_relation = sp.Poly(sp.sympify(tower_row["c_relation"]["expression"]),
                         c, b, t, r, modulus=PRIME)
    b_leading = sp.sympify(tower_row["b_leading"]["expression"])
    c_leading = sp.sympify(tower_row["c_leading"]["expression"])

    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    kernel = [sp.sympify(item["expression"])
              for item in kernel_payload["rows"][0]["kernel"]]

    route_boundary = []
    leading_boundary = []
    no_lift = []
    generic_points = []
    lifted_points = 0
    for r_value in r_roots:
        if any(value % PRIME == 0 for value in (
            r_value, r_value-1, r_value+1,
            r_value*r_value-1, r_value*r_value+1,
        )):
            route_boundary.append({"r": r_value, "stage": "R_GUARD"})
            continue
        t_polynomial = sp.Poly(base.as_expr().subs(r, r_value), t, modulus=PRIME)
        t_roots = roots(t_polynomial, t)
        if not t_roots:
            no_lift.append({"r": r_value, "stage": "NO_T"})
        for t_value in t_roots:
            if any(value % PRIME == 0 for value in (
                t_value, t_value-1, t_value+1,
                t_value*t_value-1, t_value*t_value+1,
                t_value*t_value-r_value*r_value,
                t_value*t_value+r_value*r_value,
            )):
                route_boundary.append({"r": r_value, "t": t_value,
                                       "stage": "T_GUARD"})
                continue
            b_polynomial = sp.Poly(
                b_relation.as_expr().subs({r: r_value, t: t_value}),
                b, modulus=PRIME,
            )
            b_roots = roots(b_polynomial, b)
            if not b_roots:
                no_lift.append({"r": r_value, "t": t_value,
                                "stage": "NO_B"})
            for b_value in b_roots:
                substitutions = {r: r_value, t: t_value, b: b_value}
                if int(b_leading.subs(substitutions)) % PRIME == 0:
                    leading_boundary.append({**{str(k): v for k, v in substitutions.items()},
                                             "stage": "B_LEADING"})
                    continue
                c_polynomial = sp.Poly(
                    c_relation.as_expr().subs(substitutions), c, modulus=PRIME
                )
                coefficient = int(c_polynomial.coeff_monomial(c)) % PRIME
                constant = int(c_polynomial.coeff_monomial(1)) % PRIME
                if coefficient == 0:
                    leading_boundary.append({
                        "r": r_value, "t": t_value, "b": b_value,
                        "stage": "C_LEADING", "constant": constant,
                    })
                    continue
                c_value = -constant*pow(coefficient, -1, PRIME) % PRIME
                point = {"r": r_value, "t": t_value,
                         "b": b_value, "c": c_value}
                lifted_points += 1
                if int(c_leading.subs({**substitutions, c: c_value})) % PRIME == 0:
                    leading_boundary.append({**point, "stage": "C_LEADING"})
                    continue
                guards = (
                    b_value, c_value, b_value-1, b_value+1,
                    c_value-1, c_value+1, b_value-c_value, b_value+c_value,
                )
                if any(value % PRIME == 0 for value in guards):
                    route_boundary.append({**point, "stage": "TARGET_GUARD"})
                    continue
                values = [int(expression.subs({t: t_value, r: r_value,
                                               b: b_value, c: c_value})) % PRIME
                          for expression in kernel]
                label = -t_value*t_value % PRIME
                a_value = sum(values[index]*pow(label, index, PRIME)
                              for index in range(3)) % PRIME
                b_at_label = sum(values[index+3]*pow(label, index, PRIME)
                                 for index in range(3)) % PRIME
                if a_value == 0:
                    leading_boundary.append({**point, "stage": "MISSING_DENOM"})
                    continue
                missing = b_at_label*pow(a_value, -1, PRIME) % PRIME
                source_sum = (
                    label*pow((values[6]+values[7]*label) % PRIME, 2, PRIME)
                    * pow(a_value, -2, PRIME)
                ) % PRIME
                endpoint_value = b_value if endpoint == "b" else c_value
                compatibility = (
                    pow((endpoint_value*endpoint_value+missing) % PRIME,
                        2, PRIME)
                    - source_sum*endpoint_value*endpoint_value
                ) % PRIME
                if compatibility == 0:
                    generic_points.append({
                        **point, "missing": missing, "source_sum": source_sum,
                    })

    return {
        "epsilon": [epsilon_1, epsilon_2], "endpoint": endpoint,
        "status": "COMPLETE",
        "eliminant_degree": int(eliminant.degree()),
        "r_root_count": len(r_roots), "r_roots": r_roots,
        "lifted_point_count": lifted_points,
        "generic_point_count": len(generic_points),
        "generic_points": generic_points,
        "route_boundary": route_boundary,
        "leading_boundary": leading_boundary,
        "no_lift": no_lift,
    }


@app.local_entrypoint()
def main():
    cases = tuple(
        (epsilon_1, epsilon_2, endpoint)
        for epsilon_1 in (-1, 1) for epsilon_2 in (-1, 1)
        for endpoint in ("b", "c")
    )
    raw = list(replay.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "endpoint": case[2],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell11-endpoint-replay-v1",
        "field": PRIME,
        "scope": (
            "Complete deployed-root replay of cell-11 source-only endpoint "
            "compatibility eliminants; no residual matching claim."
        ),
        "source_pilot_sha256": hashlib.sha256(PILOT.read_bytes()).hexdigest(),
        "source_tower_sha256": hashlib.sha256(TOWER.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [{key: row.get(key) for key in (
            "epsilon", "endpoint", "status", "eliminant_degree",
            "r_root_count", "lifted_point_count", "generic_point_count",
        )} for row in rows],
    }, sort_keys=True))
