#!/usr/bin/env python3
"""Independent root and direct-lane audit for cell-5 pairing 11/14."""

import ast
import hashlib
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
SCRIPT = EXP / (
    "rate_half_kb_positive_433_1b_cell5_xi3_pairing11_"
    "template_adapter_modal.py"
)
TEMPLATE = EXP / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing11_"
    "quadratic_resultant_signfree_modal.py"
)
RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell5_xi3_pairing11_"
    "template_adapter_result.json"
)
TOWER = EXP / "rate_half_kb_positive_433_1b_cell5_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell5_compact_kernel_result.json"
ROOT_SCRIPT = EXP / (
    "rate_half_kb_positive_433_1b_cell5_xi3_pairing11_"
    "independent_roots_modal.py"
)
ROOT_RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell5_xi3_pairing11_"
    "independent_roots_result.json"
)
P = 2130706433
ROOT_CACHE = {}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def parse_flint(text):
    if text == "0":
        return {}
    coefficients = {}
    for term in text.split(" + "):
        if "*x^" in term:
            coefficient, degree = term.split("*x^")
            coefficient, degree = int(coefficient), int(degree)
        elif term.startswith("x^"):
            coefficient, degree = 1, int(term[2:])
        elif term.endswith("*x"):
            coefficient, degree = int(term[:-2]), 1
        elif term == "x":
            coefficient, degree = 1, 1
        else:
            coefficient, degree = int(term), 0
        require(degree not in coefficients, "duplicate polynomial degree")
        coefficients[degree] = coefficient % P
    return {degree: value for degree, value in coefficients.items() if value}


def roots(profile):
    return ROOT_CACHE[profile["sha256"]]


def paired_scalar(a_values, b_values, left, right):
    p0, p1, p2 = (
        (b_value - left * a_value) % P
        for a_value, b_value in zip(a_values, b_values)
    )
    q0 = (b_values[0] - right * a_values[0]) % P
    q1 = (-b_values[1] + right * a_values[1]) % P
    q2 = (b_values[2] - right * a_values[2]) % P
    return (
        pow((p2 * q0 - p0 * q2) % P, 2, P)
        - ((p2 * q1 - p1 * q2) % P) * ((p1 * q0 - p0 * q1) % P)
    ) % P


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    require(
        "function.decorator_list = []" in source
        and 'node.name == "evaluate_case"' in source
        and 'compile(module, REMOTE_TEMPLATE, "exec")' in source,
        "AST adapter boundary",
    )
    extracted = [
        node for node in ast.parse(TEMPLATE.read_text()).body
        if isinstance(node, ast.FunctionDef) and node.name == "evaluate_case"
    ]
    require(len(extracted) == 1, "unique pinned template function")
    root_source = ROOT_SCRIPT.read_text()
    ast.parse(root_source)
    for snippet in (
        "gf_pow_mod", "gf_gcd", "sp.factor_list", "sorted(set(roots))",
    ):
        require(snippet in root_source, f"independent root method: {snippet}")

    tower = json.loads(TOWER.read_text())
    leading = {
        tuple(row["epsilon"]): sp.sympify(row["b_leading"]["expression"])
        for row in tower["rows"] if row["c_row_index"] == 6
    }
    kernel_payload = json.loads(KERNEL.read_text())
    kernels = {
        tuple(row["epsilon"]): tuple(
            sp.sympify(value["expression"]) for value in row["kernel"]
        )
        for row in kernel_payload["rows"]
    }
    r, t, b, c = sp.symbols("r t b c")
    payload = json.loads(RESULT.read_text())
    profiles = {}
    for row in payload["rows"]:
        for value in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                profile = value[side]
                profiles.setdefault(profile["sha256"], profile)
    require(len(profiles) == 45, "unique polynomial census")
    root_payload = json.loads(ROOT_RESULT.read_text())
    require(
        root_payload["schema"]
        == (
            "rate-half-kb-positive-433-1b-cell5-xi3-pairing11-"
            "independent-roots-v1"
        )
        and root_payload["field"] == P
        and root_payload["source_primary_sha256"]
        == hashlib.sha256(RESULT.read_bytes()).hexdigest(),
        "independent root custody",
    )
    root_rows = {row["sha256"]: row for row in root_payload["rows"]}
    require(set(root_rows) == set(profiles), "independent root profile cover")
    for key, profile in profiles.items():
        text = profile["expression"]
        require(hashlib.sha256(text.encode()).hexdigest() == key, "profile digest")
        coefficients = parse_flint(text)
        require(
            (max(coefficients, default=-1), len(coefficients))
            == (profile["degree"], profile["terms"]),
            "profile shape",
        )
        audited = root_rows[key]
        require(
            (audited["degree"], audited["terms"])
            == (profile["degree"], profile["terms"])
            and audited["roots"] == sorted(set(audited["roots"])),
            "independent root row",
        )
        ROOT_CACHE[key] = audited["roots"]

    profile_visits = 0
    boundary_count = 0
    lift_count = 0
    lane_count = 0
    for row in payload["rows"]:
        target_roots = roots(row["target_norm"]["numerator"])
        require(target_roots == row["target_norm_roots"], "target-root replay")
        union = set(target_roots)
        for value in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                union.update(roots(value[side]))
                profile_visits += 1
        require(sorted(union) == row["candidate_roots"], "candidate-root union")
        covered = {
            item["r"]
            for field in ("boundary_rows", "no_lift_rows", "finite_rows")
            for item in row[field]
        }
        require(covered == set(row["candidate_roots"]), "direct candidate coverage")
        for item in row["boundary_rows"]:
            if item["stage"] != "CELL5_B_LEADING":
                continue
            expression = leading[tuple(row["epsilon"])]
            require(
                int(expression.subs({r: item["r"], t: item["t"]})) % P == 0,
                "cell-5 leading-boundary routing",
            )
            boundary_count += 1

        kernel = kernels[tuple(row["epsilon"])]
        for finite in row["finite_rows"]:
            for z_row in finite.get("z_rows", []):
                if not z_row.get("q_rows"):
                    continue
                point = {r: finite["r"], t: finite["t"],
                         b: finite["b"], c: finite["c"]}
                values = [int(value.subs(point)) % P for value in kernel]
                a_values, b_values = values[:3], values[3:6]
                missing = finite["missing"]
                source_sum = finite["source_sum"]
                z_value = z_row["z"]
                y_value = z_value * z_value % P
                require(
                    (1 + (2 * missing - source_sum) * y_value
                     + missing * missing * y_value * y_value) % P == 0,
                    "missing reciprocal relation",
                )
                require(z_row["d"] * z_value % P == 1, "reciprocal d lift")
                require(z_row["f"] == missing * z_value % P, "f recovery")
                for q_row in z_row["q_rows"]:
                    q_value = q_row["q"]
                    e_value = q_row["e"]
                    require(e_value == q_value * z_value % P, "e recovery")
                    require(
                        paired_scalar(
                            a_values, b_values, q_value,
                            finite["b"] * z_row["f"] % P,
                        ) == 0,
                        "bf-pair replay",
                    )
                    require(
                        paired_scalar(
                            a_values, b_values, q_value,
                            row["sigma_c"] * finite["c"] * z_row["f"] % P,
                        ) == 0,
                        "cf-pair replay",
                    )
                    lift_count += 1
                    for lane in q_row["lanes"]:
                        sigma_c, sigma_o = lane["sigma"]
                        require(sigma_c == row["sigma_c"], "fixed sigma-c lane")
                        final = paired_scalar(
                            a_values, b_values, -q_value % P,
                            sigma_o * e_value * z_row["f"] % P,
                        )
                        require(
                            final == lane["final_pair_cut"] % P
                            and final != 0
                            and lane["status"] == "THIRD_PAIR_NONZERO",
                            "final-pair direct replay",
                        )
                        lane_count += 1
    require(profile_visits == 112, "profile replay count")
    require(boundary_count == 0, "no leading-boundary terminals")
    require(lift_count == 24 and lane_count == 48, "direct lift/lane census")
    print(
        "PASS pairing-11 adapter audit: "
        "profiles=112 unique=45 boundary=0 lifts=24 lanes=48"
    )


if __name__ == "__main__":
    main()
