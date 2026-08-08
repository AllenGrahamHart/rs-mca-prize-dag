#!/usr/bin/env python3
"""Independently verify the cell-4 xi5/xi6 endpoint exclusion."""

import ast
import hashlib
import itertools
import json
from pathlib import Path
import warnings

import sympy as sp
from sympy.utilities.exceptions import SymPyDeprecationWarning


warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi5_xi6_"
    "endpoint_compatibility_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi5_xi6_"
    "endpoint_compatibility_result.json"
)
STRUCTURE = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_result.json"
)
KERNEL = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_compact_kernel_result.json"
)
PINNED = {
    SCRIPT: "b57e59adca4fab77f4b5f5c191d3297517a31b3ac00f6c26008550a3957c09b3",
    RESULT: "5241a86b1c37000c7f8b10010ae397ea1a9db237d740cd33210d1ffc0ffa322e",
    STRUCTURE: "53e7e23afe164a94a677d2f3be044b1e25542d9c3d0ab6850efd1f0029002a33",
    KERNEL: "52d40fe51d713eeb6c92217d4bd0024dfd9fa29118c44cfa64592c0da350fdab",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_four_basis_tower_kernel",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
)
PRIME = 2130706433
IOTA = 16711679
SIGNS = set(itertools.product((-1, 1), repeat=2))
t, r, c, b = sp.symbols("t r c b")
VARIABLES = (t, r, c, b)
x = sp.symbols("x")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
    return {
        degree: coefficient
        for degree, coefficient in coefficients.items()
        if coefficient
    }


def verify_profile(profile, label):
    require(
        set(profile) == {"degree", "terms", "sha256", "expression"},
        f"{label} keys",
    )
    text = profile["expression"]
    require(
        hashlib.sha256(text.encode()).hexdigest() == profile["sha256"],
        f"{label} digest",
    )
    coefficients = parse_flint_polynomial(text)
    require(
        (max(coefficients, default=-1), len(coefficients))
        == (profile["degree"], profile["terms"]),
        f"{label} shape",
    )
    return coefficients


def verify_compact_profile(profile, label):
    require(
        set(profile) == {"degree", "terms", "sha256"},
        f"{label} keys",
    )
    require(
        profile["degree"] >= 0
        and profile["terms"] > 0
        and len(profile["sha256"]) == 64,
        f"{label} shape",
    )


def trim(polynomial):
    output = [coefficient % PRIME for coefficient in polynomial]
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def polynomial_remainder(dividend, divisor):
    work = trim(dividend)
    divisor = trim(divisor)
    require(divisor != [0], "nonzero polynomial divisor")
    inverse = pow(divisor[-1], -1, PRIME)
    while len(work) >= len(divisor) and work != [0]:
        shift = len(work) - len(divisor)
        scale = work[-1] * inverse % PRIME
        for index, coefficient in enumerate(divisor):
            work[shift + index] = (
                work[shift + index] - scale * coefficient
            ) % PRIME
        work = trim(work)
    return work


def polynomial_multiply_mod(left, right, modulus):
    product = [0] * (len(left) + len(right) - 1)
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            product[left_degree + right_degree] = (
                product[left_degree + right_degree]
                + left_coefficient * right_coefficient
            ) % PRIME
    return polynomial_remainder(product, modulus)


def polynomial_power_mod(base, exponent, modulus):
    output = [1]
    while exponent:
        if exponent & 1:
            output = polynomial_multiply_mod(output, base, modulus)
        base = polynomial_multiply_mod(base, base, modulus)
        exponent //= 2
    return output


def polynomial_subtract(left, right):
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        - (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def polynomial_gcd(left, right):
    left, right = trim(left), trim(right)
    while right != [0]:
        left, right = right, polynomial_remainder(left, right)
    inverse = pow(left[-1], -1, PRIME)
    return trim([coefficient * inverse for coefficient in left])


def field_roots(coefficients):
    polynomial = trim([
        coefficients.get(degree, 0)
        for degree in range(max(coefficients, default=0) + 1)
    ])
    require(polynomial != [0], "nonzero root polynomial")
    if len(polynomial) == 1:
        return []
    frobenius = polynomial_power_mod([0, 1], PRIME, polynomial)
    root_part = polynomial_gcd(
        polynomial,
        polynomial_subtract(frobenius, [0, 1]),
    )
    expression = sum(
        coefficient * x**degree
        for degree, coefficient in enumerate(root_part)
    )
    _, factors = sp.factor_list(expression, modulus=PRIME)
    roots = []
    for factor, multiplicity in factors:
        polynomial_factor = sp.Poly(factor, x, modulus=PRIME)
        require(polynomial_factor.degree() == 1, "field-root part splits linearly")
        leading, constant = (
            int(coefficient) % PRIME
            for coefficient in polynomial_factor.all_coeffs()
        )
        root = -constant * pow(leading, -1, PRIME) % PRIME
        roots.extend([root] * int(multiplicity))
    return sorted(set(roots))


def value(expression, point):
    substitutions = {
        t: point.get("t", 0),
        r: point.get("r", 0),
        c: point.get("c", 0),
        b: point.get("b", 0),
    }
    return int(sp.sympify(expression).subs(substitutions)) % PRIME


def quadratic_roots(expression, variable, point, label):
    polynomial = sp.Poly(expression, variable)
    coefficients = [
        value(polynomial.coeff_monomial(variable**degree), point)
        for degree in range(polynomial.degree() + 1)
    ]
    while coefficients and coefficients[-1] == 0:
        coefficients.pop()
    require(coefficients, f"{label} not free")
    degree = len(coefficients) - 1
    if degree == 0:
        return []
    if degree == 1:
        return [-coefficients[0] * pow(coefficients[1], -1, PRIME) % PRIME]
    require(degree == 2, f"{label} quadratic")
    constant, linear, leading = coefficients
    discriminant = (linear * linear - 4 * leading * constant) % PRIME
    inverse = pow(2 * leading, -1, PRIME)
    return sorted({
        (-linear + square_root) * inverse % PRIME
        for square_root in sp.sqrt_mod(discriminant, PRIME, all_roots=True)
    })


def t_guard(r_value, t_value):
    return (
        t_value
        * (t_value * t_value - 1)
        * (t_value * t_value + 1)
        * (t_value * t_value - r_value * r_value)
        * (t_value * t_value + r_value * r_value)
    ) % PRIME == 0


def terminal_signature(row):
    return (
        tuple((item.get("r"), item.get("t"), item["stage"])
              for item in row["boundary_rows"]),
        tuple((item["r"], item["t"], item["stage"])
              for item in row["no_lift_rows"]),
    )


def verify_payload(payload):
    require(
        payload["schema"]
        == "rate-half-kb-positive-433-1b-cell4-xi5-xi6-"
        "endpoint-compatibility-v1",
        "schema",
    )
    require(
        payload["field"] == PRIME
        and payload["source_structure_sha256"] == digest(STRUCTURE)
        and payload["source_kernel_sha256"] == digest(KERNEL),
        "source custody",
    )
    expected = {(epsilon, xi) for epsilon in SIGNS for xi in (5, 6)}
    actual = set()
    signatures = {}
    norm_shapes = []

    for row_index, row in enumerate(payload["rows"]):
        key = (tuple(row["epsilon"]), row["xi_index"])
        require(key in expected and key not in actual, "computed Cartesian row")
        actual.add(key)
        epsilon, xi = key
        require(
            row["status"] == "COMPLETE"
            and row["source_excluded"]
            and row["compatible_source_point_count"] == 0
            and row["compatible_source_points"] == []
            and row["unresolved"] == [],
            "complete source exclusion",
        )
        require(
            row["endpoint_kind"] == ("b" if xi == 5 else "c"),
            "endpoint role",
        )
        require(
            row["source_point_count"] == row["route_point_count"] == 0
            and row["finite_rows"] == []
            and row["target_boundary_rows"] == [],
            "no recovered source",
        )

        require(len(row["endpoint_compatibility_profiles"]) == 4,
                "four tower coordinates")
        for profile_index, profile in enumerate(
            row["endpoint_compatibility_profiles"]
        ):
            for part in ("numerator", "denominator"):
                verify_compact_profile(
                    profile[part],
                    f"row {row_index} coordinate {profile_index} {part}",
                )

        norm = row["endpoint_compatibility_norm"]
        numerator = verify_profile(norm["numerator"], f"row {row_index} norm n")
        denominator = verify_profile(norm["denominator"], f"row {row_index} norm d")
        require(
            (max(numerator), len(numerator), max(denominator), len(denominator))
            == (42, 39, 46, 47),
            "norm shape",
        )
        norm_shapes.append((norm["numerator"]["sha256"], norm["denominator"]["sha256"]))
        compatibility_roots = field_roots(numerator)
        require(
            row["compatibility_roots"] == compatibility_roots
            and row["compatibility_root_count"] == len(compatibility_roots) == 5,
            "complete compatibility roots",
        )

        candidate_roots = set(compatibility_roots)
        require(len(row["inverse_guards"]) == 5, "inverse guard count")
        for guard_index, guard in enumerate(row["inverse_guards"]):
            for part in ("numerator", "denominator"):
                coefficients = verify_profile(
                    guard[part],
                    f"row {row_index} guard {guard_index} {part}",
                )
                candidate_roots.update(field_roots(coefficients))
        candidate_roots.update(field_roots(denominator))
        require(
            row["candidate_roots"] == sorted(candidate_roots)
            and row["candidate_root_count"] == len(candidate_roots) == 7,
            "complete candidate-root union",
        )

        base = sp.sympify(row["base_relation"])
        b_relation = sp.sympify(row["b_relation"])
        c_relation = sp.sympify(row["c_relation"])
        require(
            sp.Poly(base, t).degree() == 2
            and sp.Poly(b_relation, b).degree() == 2
            and sp.Poly(c_relation, c).degree() == 1,
            "four-basis relation degrees",
        )
        boundaries = row["boundary_rows"]
        require(
            len(boundaries) == 7
            and sum(item["stage"] == "R_GUARD" for item in boundaries) == 5
            and sum(item["stage"] == "T_GUARD" for item in boundaries) == 2,
            "boundary partition",
        )
        require(
            {item["r"] for item in boundaries if item["stage"] == "R_GUARD"}
            == {0, 1, PRIME - 1, IOTA, PRIME - IOTA},
            "universal r guards",
        )
        for item in boundaries:
            if item["stage"] == "R_GUARD":
                r_value = item["r"]
                require(
                    r_value * (r_value * r_value - 1)
                    * (r_value * r_value + 1) % PRIME == 0,
                    "r guard",
                )
            else:
                require(
                    value(base, item) == 0 and t_guard(item["r"], item["t"]),
                    "t guard lift",
                )

        no_lifts = row["no_lift_rows"]
        require(len(no_lifts) == 2, "two no-b lifts")
        for item in no_lifts:
            require(item["stage"] == "NO_B_ROOT" and value(base, item) == 0,
                    "no-b base lift")
            require(
                quadratic_roots(b_relation, b, item, "b relation") == [],
                "complete no-b-root replay",
            )

        r_boundaries = {
            item["r"] for item in boundaries if item["stage"] == "R_GUARD"
        }
        for r_value in sorted(candidate_roots - r_boundaries):
            roots = quadratic_roots(base, t, {"r": r_value}, "base relation")
            observed = {
                item["t"]
                for item in boundaries
                if item["stage"] == "T_GUARD" and item["r"] == r_value
            } | {
                item["t"] for item in no_lifts if item["r"] == r_value
            }
            require(set(roots) == observed and len(roots) == 2,
                    "complete t-lift partition")

        touched = r_boundaries | {
            item["r"] for item in boundaries if item["stage"] == "T_GUARD"
        } | {item["r"] for item in no_lifts}
        require(touched == candidate_roots, "every candidate terminates")
        signatures[(epsilon, xi)] = terminal_signature(row)

    require(actual == expected and len(actual) == 8, "eight exact rows")
    require(len(set(norm_shapes)) == 8, "role/sign-specific norm custody")
    for epsilon in SIGNS:
        require(
            signatures[(epsilon, 5)] == signatures[(epsilon, 6)],
            "endpoint roles have identical terminal lift ledgers",
        )
    return 8, 480


def verify_source():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "class RationalFunction:",
        "common = numer.gcd(denom)",
        "endpoint_record = common_b if xi_index == 5 else c_pair",
        "(endpoint_square + missing_record) ** 2",
        "- source_sum_record * endpoint_square",
        "compatibility_norm = endpoint_compatibility.norm()",
        "candidate_roots.update(roots)",
        "cleared_compatibility != (",
        'raise ValueError("cleared endpoint compatibility replay failed")',
        "for xi_index in (5, 6)",
    ):
        require(snippet in source, f"source construction {snippet}")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED", "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"parent edge {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer edge")


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    verify_source()
    rows, raw_cases = verify_payload(json.loads(RESULT.read_text()))
    require((rows, raw_cases) == (8, 480), "aggregate scope")
    verify_dag()
    print(
        "cell=4 xi=5,6 rows=8 labels=30 quotient_orbits=18 "
        "raw_cases=480 candidates=56 source_points=0 witnesses=0"
    )


if __name__ == "__main__":
    main()
