#!/usr/bin/env python3
"""Direct residual replay for the cell-11 positive-DE pairing-9 packet."""

import ast
import hashlib
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
SCRIPT = EXP / (
    "rate_half_kb_positive_433_1b_cell11_positive_de_pairing9_"
    "template_adapter_modal.py"
)
TEMPLATE = EXP / (
    "rate_half_kb_positive_433_1b_cell4_positive_de_pairing9_"
    "nested_quadratic_modal.py"
)
RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell11_positive_de_pairing9_"
    "template_adapter_result.json"
)
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
ROOT_SCRIPT = EXP / (
    "rate_half_kb_positive_433_1b_cell11_positive_de_pairing9_"
    "frobenius_roots_modal.py"
)
ROOT_RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell11_positive_de_pairing9_"
    "frobenius_roots_result.json"
)
P = 2130706433
ROOT_TOTAL = 114
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


def evaluate_sparse(coefficients, value):
    degrees = sorted(coefficients, reverse=True)
    if not degrees:
        return 0
    result = coefficients[degrees[0]]
    previous = degrees[0]
    for degree in degrees[1:]:
        result = (
            result * pow(value, previous - degree, P) + coefficients[degree]
        ) % P
        previous = degree
    return result * pow(value, previous, P) % P


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
        "fmpz_mod_poly_ctx",
        "polynomial.gcd(pow(x, PRIME, polynomial) - x)",
        "root_part.factor()",
        '"frobenius_root_degree": root_degree',
    ):
        require(snippet in root_source, f"Frobenius root method: {snippet}")

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
    require(len(profiles) == 33, "unique polynomial census")
    root_payload = json.loads(ROOT_RESULT.read_text())
    require(
        root_payload["schema"]
        == (
            "rate-half-kb-positive-433-1b-cell11-positive-de-pairing9-"
            "frobenius-roots-v1"
        )
        and root_payload["field"] == P
        and root_payload["method"]
        == "external FLINT gcd(P,x^p-x), factor squarefree root part"
        and root_payload["source_primary_sha256"]
        == hashlib.sha256(RESULT.read_bytes()).hexdigest(),
        "external root custody",
    )
    root_rows = {row["sha256"]: row for row in root_payload["rows"]}
    require(set(root_rows) == set(profiles), "external root profile cover")
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
            and audited["frobenius_root_degree"] == len(audited["roots"])
            and audited["roots"] == sorted(set(audited["roots"])),
            "external root row",
        )
        require(
            all(evaluate_sparse(coefficients, value) == 0
                for value in audited["roots"]),
            "reported root evaluation",
        )
        ROOT_CACHE[key] = audited["roots"]
    require(
        sum(len(row["roots"]) for row in root_rows.values()) == ROOT_TOTAL
        and max(row["degree"] for row in root_rows.values()) == 11056,
        "external root totals",
    )

    profile_visits = 0
    uf_count = 0
    lift_count = 0
    colored_count = 0
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
        for finite in row["finite_rows"]:
            if finite["status"] != "CHECKED":
                continue
            point = {r: finite["r"], t: finite["t"],
                     b: finite["b"], c: finite["c"]}
            values = [int(value.subs(point)) % P for value in kernel]
            a_values, b_values = values[:3], values[3:6]
            de = finite["de"]
            require(de == finite["missing"], "DE recovery")
            second_de = -de % P
            for u_value in finite["u_roots"]:
                require(paired(a_values, b_values, second_de, u_value) == 0,
                        "u-pair root")
            for f_value in finite["f_roots"]:
                require(paired(a_values, b_values, de,
                               finite["b"] * f_value % P) == 0,
                        "f-pair root")
            require(len(finite["uf_rows"]) ==
                    len(finite["u_roots"]) * len(finite["f_roots"]),
                    "Cartesian uf replay")
            for uf_row in finite["uf_rows"]:
                uf_count += 1
                u_value, f_value = uf_row["u"], uf_row["f"]
                relation = (
                    pow((u_value*u_value + de*f_value*f_value) % P, 2, P)
                    - finite["source_sum"]*f_value*f_value*u_value*u_value
                ) % P
                require(relation == uf_row["relation"], "missing relation replay")
                if relation:
                    require(uf_row["status"] == "MISSING_RELATION_NONZERO",
                            "nonzero relation terminal")
                    continue
                lift_count += 1
                require(f_value != 0, "unexpected zero-f survivor")
                d_value = u_value * pow(f_value, -1, P) % P
                require(d_value != 0, "unexpected zero-d survivor")
                e_value = de * pow(d_value, -1, P) % P
                v_value = e_value * f_value % P
                colored = paired(
                    a_values, b_values,
                    sigma_o * v_value % P,
                    sigma_c * finite["c"] * f_value % P,
                )
                require(
                    (d_value, e_value, v_value)
                    == (uf_row["d"], uf_row["e"], uf_row["v"])
                    and colored == uf_row["colored_cut"] % P
                    and colored != 0
                    and uf_row["status"] == "COLORED_PAIR_NONZERO",
                    "colored-pair terminal",
                )
                colored_count += 1
    require(profile_visits == 160, "profile replay count")
    require((uf_count, lift_count, colored_count) == (256, 32, 32),
            "direct residual census")
    print(
        "PASS positive pairing-9 adapter audit: profiles=160 unique=33 "
        f"roots={ROOT_TOTAL} uf=256 lifts=32 colored=32"
    )


if __name__ == "__main__":
    main()
