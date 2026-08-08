#!/usr/bin/env python3
"""Verify the cell-4 positive-DE pairing-12 32-case exclusion."""

import ast
import collections
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_positive_de_pairing12_"
    "nested_quadratic_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_positive_de_pairing12_"
    "nested_quadratic_result.json"
)
STRUCTURE = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_result.json"
)
KERNEL = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_compact_kernel_result.json"
)
PINNED = {
    SCRIPT: "6fe230daa08afdd875015dbcba465e6b9781281831b8adcbb2d5dc160969d7b8",
    RESULT: "20db08cfb00edd1346b6186958cebb493bff256dc27bab484418bc56e7d968e3",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_four_basis_tower_kernel",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
)
PRIME = 2130706433
IOTA = 16711679
SIGNS = set(itertools.product((-1, 1), repeat=2))
LANES = set(itertools.product((-1, 1), repeat=2))
MATCHING = ((0, 5), (1, 2), (3, 4))
t, r, c, b = sp.symbols("t r c b")
VARIABLES = (t, r, c, b)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def value(expression, point):
    substitutions = {
        t: point.get("t", 0),
        r: point.get("r", 0),
        c: point.get("c", 0),
        b: point.get("b", 0),
    }
    return int(sp.sympify(expression).subs(substitutions)) % PRIME


def parse_flint_polynomial(text):
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
        require(degree not in coefficients, "unique FLINT polynomial degree")
        coefficients[degree] = coefficient % PRIME
    return {degree: coefficient for degree, coefficient in coefficients.items()
            if coefficient}


def verify_full_profile(profile, label):
    require(set(profile) == {"degree", "terms", "sha256", "expression"},
            f"{label} keys")
    text = profile["expression"]
    require(hashlib.sha256(text.encode()).hexdigest() == profile["sha256"],
            f"{label} digest")
    coefficients = parse_flint_polynomial(text)
    degree = max(coefficients, default=-1)
    require((degree, len(coefficients)) ==
            (profile["degree"], profile["terms"]), f"{label} shape")
    return coefficients


def verify_compact_profile(profile, label):
    require(set(profile) == {"degree", "terms", "sha256"}, f"{label} keys")
    require(profile["degree"] >= 0 and profile["terms"] > 0 and
            len(profile["sha256"]) == 64, f"{label} compact profile")


def evaluate_polynomial(coefficients, point):
    output = 0
    for degree in range(max(coefficients, default=-1), -1, -1):
        output = (output * point + coefficients.get(degree, 0)) % PRIME
    return output


def paired(a_values, b_values, left, right):
    p0, p1, p2 = (
        (b_value - left*a_value) % PRIME
        for a_value, b_value in zip(a_values, b_values)
    )
    q0 = (b_values[0] - right*a_values[0]) % PRIME
    q1 = (-b_values[1] + right*a_values[1]) % PRIME
    q2 = (b_values[2] - right*a_values[2]) % PRIME
    return (
        pow((p2*q0 - p0*q2) % PRIME, 2, PRIME)
        - ((p2*q1 - p1*q2) % PRIME)
        * ((p1*q0 - p0*q1) % PRIME)
    ) % PRIME


def paired_coefficients(a_values, b_values, left, right_scale=1):
    p0, p1, p2 = (
        (b_value - left*a_value) % PRIME
        for a_value, b_value in zip(a_values, b_values)
    )
    a0 = (p2*b_values[0] - p0*b_values[2]) % PRIME
    a1 = right_scale*(-p2*a_values[0] + p0*a_values[2]) % PRIME
    b0 = (-p2*b_values[1] - p1*b_values[2]) % PRIME
    b1 = right_scale*(p2*a_values[1] + p1*a_values[2]) % PRIME
    c0 = (p1*b_values[0] + p0*b_values[1]) % PRIME
    c1 = right_scale*(-p1*a_values[0] - p0*a_values[1]) % PRIME
    return [
        (a0*a0 - b0*c0) % PRIME,
        (2*a0*a1 - b0*c1 - b1*c0) % PRIME,
        (a1*a1 - b1*c1) % PRIME,
    ]


def verify_roots(coefficients, roots, label):
    coefficients = [value % PRIME for value in coefficients]
    while coefficients and coefficients[-1] == 0:
        coefficients.pop()
    require(roots is not None and roots == sorted(set(roots)),
            f"{label} root format")
    degree = len(coefficients) - 1
    if degree < 0:
        raise RuntimeError(f"{label} identically zero")
    if degree == 0:
        require(not roots, f"{label} constant roots")
        return
    if degree == 1:
        expected = [-coefficients[0]*pow(coefficients[1], -1, PRIME) % PRIME]
        require(roots == expected, f"{label} linear roots")
        return
    require(degree == 2, f"{label} degree")
    constant, linear, leading = coefficients
    discriminant = (linear*linear - 4*leading*constant) % PRIME
    if discriminant == 0:
        expected = [-linear*pow(2*leading, -1, PRIME) % PRIME]
        require(roots == expected, f"{label} double root")
    elif pow(discriminant, (PRIME - 1)//2, PRIME) == PRIME - 1:
        require(not roots, f"{label} nonsquare roots")
    else:
        require(len(roots) == 2 and
                sum(roots) % PRIME == -linear*pow(leading, -1, PRIME) % PRIME and
                roots[0]*roots[1] % PRIME ==
                constant*pow(leading, -1, PRIME) % PRIME,
                f"{label} split roots")


def residual_signature(xi):
    products = ("de", "de", "-de", "df", "sigma_o*ef",
                "bf", "sigma_c*cf")
    sums = ("(d+e)^2", "(d+e)^2", "(d-e)^2", "(d+f)^2",
            "(e+sigma_o*f)^2", "(b+f)^2", "(c+sigma_c*f)^2")
    residual_products = products[:xi] + products[xi+1:]
    residual_sums = sums[:xi] + sums[xi+1:]
    return (
        products[xi], sums[xi],
        tuple((residual_products[left], residual_products[right])
              for left, right in MATCHING),
        tuple((residual_sums[left], residual_sums[right])
              for left, right in MATCHING),
    )


def boundary_key(item):
    return (
        item.get("r"), item.get("t"), item.get("b"), item.get("c"),
        item.get("u"), item.get("f"), item.get("v"), item.get("status"),
        tuple(item.get("failed_guards", ())),
    )


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell4-positive-de-pairing12-"
            "nested-quadratic-v1", "schema")
    require(payload["field"] == PRIME and
            payload["source_structure_sha256"] == digest(STRUCTURE) and
            payload["source_kernel_sha256"] == digest(KERNEL), "custody")
    kernels = {
        tuple(row["epsilon"]): tuple(
            sp.sympify(item["expression"]) for item in row["kernel"]
        )
        for row in json.loads(KERNEL.read_text())["rows"]
    }
    expected = {
        (epsilon, sigma, 0, 12)
        for epsilon in SIGNS for sigma in LANES
    }
    actual = set()
    candidate_counts = []
    source_counts = []
    uf_counts = []
    target_root_counts = []
    free_shapes = collections.Counter()
    norm_shapes = collections.Counter()
    guard_shapes = collections.Counter()
    norm_numerator_hashes = set()
    norm_denominator_hashes = set()
    aggregate = collections.Counter()

    for row_index, row in enumerate(payload["rows"]):
        key = (tuple(row["epsilon"]), tuple(row["sigma"]),
               row["xi_index"], row["pairing_index"])
        require(key in expected and key not in actual, "computed Cartesian row")
        actual.add(key)
        epsilon, sigma, xi, _ = key
        sigma_c, sigma_o = sigma
        require(row["status"] == "COMPLETE" and row["excluded"] and
                tuple(map(tuple, row["matching"])) == MATCHING and
                not row["witnesses"] and not row["unresolved"],
                "complete exclusion row")
        require((row["p_u_degree"], row["p_f_degree"],
                 row["uf_eliminant_degree"], row["remainder_degree"]) ==
                (2, 2, 8, 1), "nested-quadratic degrees")

        require(len(row["target_free_profiles"]) == 4,
                "four target-free coordinates")
        for profile_index, profile in enumerate(row["target_free_profiles"]):
            for part in ("numerator", "denominator"):
                verify_compact_profile(
                    profile[part], f"row {row_index} free {profile_index} {part}"
                )
            free_shapes[(profile["numerator"]["degree"],
                         profile["numerator"]["terms"],
                         profile["denominator"]["degree"],
                         profile["denominator"]["terms"])] += 1

        numerator = verify_full_profile(
            row["target_norm"]["numerator"], f"row {row_index} norm numerator"
        )
        denominator = verify_full_profile(
            row["target_norm"]["denominator"],
            f"row {row_index} norm denominator",
        )
        norm_shapes[(xi, len(numerator) and max(numerator), len(numerator),
                     len(denominator) and max(denominator),
                     len(denominator))] += 1
        norm_numerator_hashes.add(row["target_norm"]["numerator"]["sha256"])
        norm_denominator_hashes.add(row["target_norm"]["denominator"]["sha256"])
        require(row["target_roots"] == sorted(set(row["target_roots"])) and
                row["target_root_count"] == len(row["target_roots"]) and
                set(row["target_roots"]) <= set(row["candidate_roots"]),
                "target-root ledger")
        for root in row["target_roots"]:
            require(evaluate_polynomial(numerator, root) == 0 and
                    evaluate_polynomial(denominator, root) != 0,
                    "target norm root replay")
        require(row["candidate_roots"] == sorted(set(row["candidate_roots"])) and
                row["candidate_root_count"] == len(row["candidate_roots"]),
                "candidate-root ledger")

        require(len(row["inverse_guards"]) == 4, "inverse guard count")
        for guard in row["inverse_guards"]:
            numerator_guard = verify_full_profile(
                guard["numerator"], f"row {row_index} {guard['name']} numerator"
            )
            denominator_guard = verify_full_profile(
                guard["denominator"],
                f"row {row_index} {guard['name']} denominator",
            )
            guard_shapes[(guard["name"], max(numerator_guard, default=-1),
                          len(numerator_guard), max(denominator_guard, default=-1),
                          len(denominator_guard))] += 1

        base = sp.sympify(row["base_relation"])
        b_relation = sp.sympify(row["b_relation"])
        c_relation = sp.sympify(row["c_relation"])
        boundaries = row["boundary_rows"]
        require(len(boundaries) == 7 and
                sum(item["stage"] == "R_GUARD" for item in boundaries) == 5 and
                sum(item["stage"] == "T_GUARD" for item in boundaries) == 2,
                "boundary partition")
        for item in boundaries:
            if item["stage"] == "R_GUARD":
                r_value = item["r"]
                require(r_value*(r_value*r_value - 1)*
                        (r_value*r_value + 1) % PRIME == 0,
                        "r boundary guard")
            elif item["stage"] == "T_GUARD":
                require(value(base, item) == 0, "t-boundary base lift")
                r_value, t_value = item["r"], item["t"]
                require(t_value*(t_value*t_value - 1)*
                        (t_value*t_value + 1)*
                        (t_value*t_value - r_value*r_value)*
                        (t_value*t_value + r_value*r_value) % PRIME == 0,
                        "t boundary guard")
            else:
                raise RuntimeError("unexpected boundary stage")
        require({item["r"] for item in boundaries
                 if item["stage"] == "R_GUARD"} ==
                {0, 1, PRIME - 1, IOTA, PRIME - IOTA},
                "universal r boundaries")

        b_polynomial = sp.Poly(b_relation, b)
        require(b_polynomial.degree() == 2, "quadratic b relation")
        for item in row["no_lift_rows"]:
            require(item["stage"] == "NO_B_ROOT" and value(base, item) == 0,
                    "no-b base lift")
            leading, linear, constant = (
                value(coefficient, item)
                for coefficient in b_polynomial.all_coeffs()
            )
            require(leading != 0 and
                    pow((linear*linear - 4*leading*constant) % PRIME,
                        (PRIME - 1)//2, PRIME) == PRIME - 1,
                    "no-b nonsquare discriminant")

        kernel = kernels[epsilon]
        require(row["source_point_count"] == row["route_point_count"] ==
                len(row["finite_rows"]), "source-point count")
        relation_candidates = []
        local_boundaries = []
        local_colored_rows = 0
        local_relation_nonzero = 0
        for finite in row["finite_rows"]:
            require(finite["status"] == "CHECKED" and
                    value(base, finite) == value(b_relation, finite) ==
                    value(c_relation, finite) == 0, "finite source relation")
            r_value, t_value = finite["r"], finite["t"]
            b_value, c_value = finite["b"], finite["c"]
            route_guards = (
                b_value, c_value, r_value, t_value,
                b_value - 1, b_value + 1, c_value - 1, c_value + 1,
                b_value - c_value, b_value + c_value,
                r_value*r_value - 1, r_value*r_value + 1,
                t_value*t_value - 1, t_value*t_value + 1,
                t_value*t_value - r_value*r_value,
                t_value*t_value + r_value*r_value,
            )
            require(all(guard % PRIME for guard in route_guards),
                    "finite route guards")
            kernel_values = [value(expression, finite) for expression in kernel]
            a_values, b_values = kernel_values[:3], kernel_values[3:6]
            beta_0, beta_1 = kernel_values[6:]
            label = -t_value*t_value % PRIME
            a_missing = sum(coefficient*pow(label, degree, PRIME)
                            for degree, coefficient in enumerate(a_values)) % PRIME
            b_missing = sum(coefficient*pow(label, degree, PRIME)
                            for degree, coefficient in enumerate(b_values)) % PRIME
            require(a_missing != 0, "missing-record denominator")
            missing = b_missing*pow(a_missing, -1, PRIME) % PRIME
            de_value = missing if xi == 0 else -missing % PRIME
            second_de = -de_value % PRIME if xi == 0 else de_value
            source_sum = (
                label*pow((beta_0 + beta_1*label) % PRIME, 2, PRIME)
                * pow(a_missing, -2, PRIME)
            ) % PRIME
            require((finite["missing"], finite["de"], finite["source_sum"]) ==
                    (missing, de_value, source_sum) and de_value != 0,
                    "missing row replay")
            u_coefficients = paired_coefficients(
                a_values, b_values, second_de
            )
            f_coefficients = paired_coefficients(
                a_values, b_values, de_value, sigma_c*c_value % PRIME
            )
            verify_roots(u_coefficients, finite["u_roots"], "u paired cut")
            verify_roots(f_coefficients, finite["f_roots"], "f paired cut")
            expected_uf = {(u_value, f_value)
                           for u_value in finite["u_roots"]
                           for f_value in finite["f_roots"]}
            require({(item["u"], item["f"]) for item in finite["uf_rows"]} ==
                    expected_uf and len(finite["uf_rows"]) == len(expected_uf),
                    "complete uf Cartesian product")
            eta = 1 if xi == 0 else -1
            for uf_row in finite["uf_rows"]:
                u_value, f_value = uf_row["u"], uf_row["f"]
                relation = (
                    pow((u_value*u_value +
                         eta*de_value*f_value*f_value) % PRIME, 2, PRIME)
                    - source_sum*f_value*f_value*u_value*u_value
                ) % PRIME
                require(uf_row["relation"] == relation,
                        "missing-relation replay")
                if relation:
                    require(uf_row["status"] == "MISSING_RELATION_NONZERO",
                            "missing-relation terminal")
                    local_relation_nonzero += 1
                    continue
                relation_candidates.append(
                    (r_value, t_value, b_value, c_value, u_value, f_value)
                )
                if f_value == 0:
                    require(uf_row["status"] == "TARGET_BOUNDARY" and
                            uf_row["failed_guards"] == ["nonzero_5"],
                            "f-zero boundary")
                    local_boundaries.append({**finite, **uf_row})
                    continue
                d_value = u_value*pow(f_value, -1, PRIME) % PRIME
                require(d_value != 0, "nonzero reconstructed d")
                e_value = de_value*pow(d_value, -1, PRIME) % PRIME
                v_value = e_value*f_value % PRIME
                colored_cut = paired(
                    a_values, b_values,
                    sigma_o*v_value % PRIME,
                    b_value*f_value % PRIME,
                )
                require((uf_row["d"], uf_row["e"], uf_row["v"],
                         uf_row["colored_cut"]) ==
                        (d_value, e_value, v_value, colored_cut) and
                        colored_cut != 0 and
                        uf_row["status"] == "COLORED_PAIR_NONZERO",
                        "colored-pair terminal")
                local_colored_rows += 1

        require(row["uf_candidate_count"] == len(relation_candidates) and
                {tuple(item[key] for key in ("r", "t", "b", "c", "u", "f"))
                 for item in row["uf_candidates"]} == set(relation_candidates),
                "uf-candidate ledger")
        require(row["colored_solution_count"] == 0 and
                row["colored_solutions"] == [], "no colored solution")
        require({boundary_key(item) for item in row["target_boundary_rows"]} ==
                {boundary_key(item) for item in local_boundaries},
                "target-boundary ledger")
        touched = ({item["r"] for item in boundaries} |
                   {item["r"] for item in row["no_lift_rows"]} |
                   {item["r"] for item in row["finite_rows"]})
        require(touched == set(row["candidate_roots"]),
                "every candidate reaches a terminal")

        candidate_counts.append(row["candidate_root_count"])
        source_counts.append(row["source_point_count"])
        uf_counts.append(row["uf_candidate_count"])
        target_root_counts.append(row["target_root_count"])
        aggregate["relation_nonzero"] += local_relation_nonzero
        aggregate["colored_nonzero"] += local_colored_rows
        aggregate["target_boundaries"] += len(local_boundaries)

    require(actual == expected and len(actual) == 16, "16 computed rows")
    require(collections.Counter(candidate_counts) == {14: 16},
            "candidate-root census")
    require(collections.Counter(source_counts) == {20: 16},
            "source-point census")
    require(collections.Counter(uf_counts) == {8: 16},
            "uf-candidate census")
    require(collections.Counter(target_root_counts) == {13: 16},
            "target-root census")
    require(sum(candidate_counts) == 224 and sum(source_counts) == 320 and
            sum(uf_counts) == 128 and aggregate == {
                "relation_nonzero": 960,
                "colored_nonzero": 128,
                "target_boundaries": 0,
            }, "global terminal census")
    require(free_shapes == {
        (5586, 5587, 3661, 3560): 32,
        (5590, 5591, 3664, 3562): 32,
    }, "target-free shape census")
    require(norm_shapes == {
        (0, 8518, 7481, 3860, 3861): 16,
    }, "target-norm shape census")
    require(guard_shapes == {
        ("base_leading_0", 2, 3, 0, 1): 16,
        ("quad_inverse_1", 8, 7, 0, 1): 16,
        ("quad_inverse_2", 10, 11, 4, 4): 16,
        ("quad_inverse_3", 76, 68, 33, 34): 16,
    }, "inverse-guard shape census")
    require((len(norm_numerator_hashes), len(norm_denominator_hashes)) ==
            (4, 4), "specialized norm diversity")
    require(residual_signature(0) == residual_signature(1),
            "positive parallel-copy transport")
    return 16, 16


def verify_source():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "class RationalFunction:",
        "common = numer.gcd(denom)",
        "def polynomial_pseudo_remainder(",
        "p_u = paired_polynomial(PairPolynomial(second_de)",
        "variable_polynomial * sigma_c * c_pair",
        "uf_eliminant = (",
        "target_free = p_f_a * (",
        "target_norm = target_free.norm()",
        "candidate_roots.update(roots)",
        "eta*de_value*f_value*f_value",
        "colored_cut = paired_scalar(",
        'raise ValueError("direct target replay failed")',
        "for xi_index in (0,)",
    ):
        require(snippet in source, f"source construction {snippet}")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED",
            "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"parent edge {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    verify_source()
    computed, transported = verify_payload(json.loads(RESULT.read_text()))
    require(computed + transported == 32, "aggregate raw-case count")
    verify_dag()
    print(
        "cell=4 pairing=12 positive_DE=2 raw_cases=32 computed=16 "
        "transported=16 candidates=224 source_points=320 "
        "colored_nonzero=128 boundaries=0 witnesses=0"
    )


if __name__ == "__main__":
    main()
