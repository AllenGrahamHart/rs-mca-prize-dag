#!/usr/bin/env python3
"""Independent roots and direct residual audit for cell-5 DE pairing 3."""

import ast
import hashlib
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_de_pairing3_template_adapter_modal.py"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_de_pairing3_nested_quadratic_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_de_pairing3_template_adapter_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell5_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_de_pairing3_independent_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_de_pairing3_independent_roots_result.json"
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


def paired(a_values, b_values, left, right):
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
    require("function.decorator_list = []" in source
            and 'node.name == "evaluate_case"' in source
            and 'compile(module, REMOTE_TEMPLATE, "exec")' in source,
            "AST adapter boundary")
    require(len([node for node in ast.parse(TEMPLATE.read_text()).body
                 if isinstance(node, ast.FunctionDef)
                 and node.name == "evaluate_case"]) == 1,
            "unique pinned template function")
    root_source = ROOT_SCRIPT.read_text()
    ast.parse(root_source)
    for snippet in ("gf_pow_mod", "gf_gcd", "sp.factor_list", "sorted(set(roots))"):
        require(snippet in root_source, f"independent root method: {snippet}")

    kernel_payload = json.loads(KERNEL.read_text())
    kernels = {
        tuple(row["epsilon"]): tuple(sp.sympify(value["expression"])
                                     for value in row["kernel"])
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
    require(len(profiles) == 53, "unique polynomial census")
    root_payload = json.loads(ROOT_RESULT.read_text())
    require(
        root_payload["schema"]
            == "rate-half-kb-positive-433-1b-cell5-de-pairing3-independent-roots-v1"
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
        require((max(coefficients, default=-1), len(coefficients))
                == (profile["degree"], profile["terms"]), "profile shape")
        audited = root_rows[key]
        require((audited["degree"], audited["terms"])
                == (profile["degree"], profile["terms"])
                and audited["roots"] == sorted(set(audited["roots"])),
                "independent root row")
        ROOT_CACHE[key] = audited["roots"]
    require(sum(len(row["roots"]) for row in root_rows.values()) == 284
            and max(row["degree"] for row in root_rows.values()) == 3492,
            "independent root totals")

    profile_visits = uv_count = f_count = colored_count = f_boundary_count = 0
    for row in payload["rows"]:
        target_roots = roots(row["target_norm"]["numerator"])
        require(target_roots == row["target_roots"], "target-root replay")
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
        require(covered == set(row["candidate_roots"]), "candidate coverage")

        kernel = kernels[tuple(row["epsilon"])]
        sigma_c, sigma_o = row["sigma"]
        xi = row["xi_index"]
        eta = 1 if xi == 0 else -1
        for finite in row["finite_rows"]:
            if finite["status"] != "CHECKED":
                continue
            point = {r: finite["r"], t: finite["t"],
                     b: finite["b"], c: finite["c"]}
            values = [int(value.subs(point)) % P for value in kernel]
            a_values, b_values = values[:3], values[3:6]
            de = finite["de"]
            require(de == (finite["missing"] if xi == 0
                           else -finite["missing"] % P), "DE recovery")
            second_de = -de % P if xi == 0 else de
            for u in finite["u_roots"]:
                require(paired(a_values, b_values, de, u) == 0, "u-pair root")
            for v in finite["v_roots"]:
                require(paired(a_values, b_values, second_de, sigma_o * v % P) == 0,
                        "v-pair root")
            require(len(finite["uv_rows"])
                    == len(finite["u_roots"]) * len(finite["v_roots"]),
                    "Cartesian uv replay")
            for uv in finite["uv_rows"]:
                u, v = uv["u"], uv["v"]
                h = (de * pow(u + eta * v, 2, P)
                     - finite["source_sum"] * u * v) % P
                require(h == uv["h"], "missing-sum replay")
                if h:
                    require(uv["status"] == "MISSING_SUM_NONZERO"
                            and not uv["f_rows"], "nonzero H terminal")
                    continue
                uv_count += 1
                require(uv["status"] == "CHECKED", "zero H terminal")
                f_squared = u * v * pow(de, -1, P) % P
                require(f_squared == uv["f_squared"], "f-square recovery")
                for f_row in uv["f_rows"]:
                    f_value = f_row["f"]
                    require(f_value * f_value % P == f_squared, "f root")
                    f_count += 1
                    if f_value == 0:
                        require(f_row["status"] == "TARGET_BOUNDARY"
                                and f_row["failed_guards"] == ["nonzero_5"],
                                "zero-f boundary")
                        f_boundary_count += 1
                        continue
                    d_value = u * pow(f_value, -1, P) % P
                    e_value = v * pow(f_value, -1, P) % P
                    colored = paired(a_values, b_values,
                                     finite["b"] * f_value % P,
                                     sigma_c * finite["c"] * f_value % P)
                    require((d_value, e_value) == (f_row["d"], f_row["e"])
                            and colored == f_row["colored_cut"] % P
                            and colored != 0
                            and f_row["status"] == "COLORED_PAIR_NONZERO",
                            "colored-pair terminal")
                    colored_count += 1
    require(profile_visits == 320, "profile replay count")
    require((uv_count, f_count, colored_count, f_boundary_count)
            == (96, 144, 96, 48), "direct residual census")
    print("PASS cell-5 pairing-3 audit: unique=53 roots=284 uv=96 f=144")


if __name__ == "__main__":
    main()
