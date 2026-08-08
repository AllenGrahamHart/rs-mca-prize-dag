#!/usr/bin/env sage
"""Independent exact audit of the near-literal inversion transports.

This file does not import the PR #1140 compiler.  It reconstructs each
positive source form with a generic 5 x 5 solve, forms the two residual
quadratics, and checks the two literal transports and their cleared open
loci directly over QQ(b,c,d).
"""

import hashlib
import json


R = PolynomialRing(QQ, names=("b", "c", "d"), order="degrevlex")
b, c, d = R.gens()
K = R.fraction_field()
bK, cK, dK = map(K, R.gens())
KW = PolynomialRing(K, "W")
W = KW.gen()
wK = K(1) / cK

VERTICES = {
    "v0": K(2), "v1": K(1) / 2, "v2": bK, "v3": K(1) / bK,
}
EDGE_VERTICES = {
    "E01": ("v0", "v1"), "E02": ("v0", "v2"),
    "E03": ("v0", "v3"), "E12": ("v1", "v2"),
    "E13": ("v1", "v3"), "E23": ("v2", "v3"),
}
ASSIGNMENTS = {
    "F00": ("E01", "E02"), "F01": ("E01", "E03"),
    "F02": ("E01", "E12"), "F03": ("E01", "E13"),
    "F04": ("E02", "E23"), "F05": ("E03", "E23"),
    "F06": ("E12", "E23"), "F07": ("E13", "E23"),
    "M00": ("E02", "E03"), "M01": ("E02", "E12"),
    "M02": ("E03", "E13"), "M03": ("E12", "E13"),
}
B_MAP = {
    "F00": "F01", "F01": "F00", "F02": "F03", "F03": "F02",
    "F04": "F05", "F05": "F04", "F06": "F07", "F07": "F06",
    "M00": "M00", "M01": "M02", "M02": "M01", "M03": "M03",
}

ROOTS = {"A": K(1) / 2, "TA": K(2), "OB": K(1) / bK, "OI": bK}
TARGETS = {}
for orbit, root in ROOTS.items():
    TARGETS[f"{orbit}-RX"] = ((W - root) ** 2, (W - 1 / dK) ** 2)
    TARGETS[f"{orbit}-RL"] = ((W - 1 / dK) ** 2, (W - root) ** 2)
    TARGETS[f"{orbit}-RM"] = (
        (W - root) * (W - 1 / dK),
        (W - root) * (W - 1 / dK),
    )


def primitive(value):
    value = R(value)
    if not value:
        return value
    value = R(value / value.content())
    return -value if value.leading_coefficient() < 0 else value


def strip_units(value):
    value = K(value)
    denominator = R(value.denominator())
    assert denominator.is_monomial()
    value = R(value.numerator())
    if not value:
        return value
    unit = R.one()
    for generator in R.gens():
        valuation = min(monomial.degree(generator) for monomial in value.monomials())
        unit *= generator**valuation
    return primitive(value // unit)


def edge(edge_id):
    left_id, right_id = EDGE_VERTICES[edge_id]
    left, right = VERTICES[left_id], VERTICES[right_id]
    return vector(K, (left * right, -(left + right), 1))


def evaluation(point):
    return matrix(K, (
        (1, point, point**2, 0, 0),
        (0, 0, 0, 1 + point**2, point),
        (point**2, point, 1, 0, 0),
    ))


def add_rational_factors(container, value):
    value = K(value)
    for part in (value.numerator(), value.denominator()):
        part = strip_units(K(part))
        if not part.is_constant():
            container.append(part)


def build(assignment_id):
    first_id, second_id = ASSIGNMENTS[assignment_id]
    first_vertices, second_vertices = set(EDGE_VERTICES[first_id]), set(EDGE_VERTICES[second_id])
    common_id = next(iter(first_vertices & second_vertices))
    right_id = next(iter(first_vertices - {common_id}))
    left_id = next(iter(second_vertices - {common_id}))
    common, right, left = VERTICES[common_id], VERTICES[right_id], VERTICES[left_id]
    first, second = edge(first_id), edge(second_id)

    q0, q1 = cK * dK, -(cK + dK)
    f, g, m = q0 - wK, 1 - wK * q0, q1 * (1 - wK)
    v = vector(KW, (f + g * W, m * (1 + W), g + f * W))
    v_common = v[0] + common * v[1] + common**2 * v[2]
    z = -K(v_common[0]) / K(v_common[1])
    vz = vector(K, (entry(z) for entry in v))
    linear_1, linear_0 = vz[2], vz[1] + common * vz[2]
    target = (
        (linear_0 + left * linear_1) * first
        + (linear_0 + right * linear_1) * second
    ) / (left - right)

    at_w, at_z = evaluation(wK), evaluation(z)
    coefficient_matrix = matrix(K, (
        at_w[0] - q0 * at_w[2],
        at_w[1] - q1 * at_w[2],
        *at_z.rows(),
    ))
    solution = coefficient_matrix.solve_right(vector(K, (0, 0, *target)))
    assert coefficient_matrix * solution == vector(K, (0, 0, *target))
    u = vector(KW, (
        solution[0] + solution[1] * W + solution[2] * W**2,
        solution[3] * (1 + W**2) + solution[4] * W,
        solution[2] + solution[1] * W + solution[0] * W**2,
    ))

    residuals = []
    for root in (cK, dK):
        u_root = sum(u[index] * root**index for index in range(3))
        v_root = sum(v[index] * root**index for index in range(3))
        quotient, remainder = (u_root**2 - W * v_root**2).quo_rem((W - wK) ** 2)
        assert remainder == 0 and quotient.degree() == 2
        residuals.append(quotient)

    base_localizers = [R(b), R(c), R(d)]
    for value in (
        v_common[1], left - right, 1 - z**2, 1 - q0,
        (wK - z) * (1 - wK * z),
    ):
        add_rational_factors(base_localizers, value)

    systems = {}
    for target_id, target_pair in TARGETS.items():
        factors = list(base_localizers)
        for residual, target_poly in zip(residuals, target_pair):
            for index in (0, 1):
                raw = K(residual[index] - residual[2] * target_poly[index])
                add_rational_factors(factors, raw.denominator())
        systems[target_id] = factors
    return tuple(residuals), systems


def substitute(value, mode):
    substitutions = {bK: 1 / bK}
    if mode == "TW":
        substitutions.update({cK: 1 / cK, dK: 1 / dK})
    return K(K(value).subs(substitutions))


def transform_poly(poly, mode):
    poly = KW(poly)
    result = KW.zero()
    for index in range(poly.degree() + 1):
        exponent = poly.degree() - index if mode == "TW" else index
        result += substitute(poly[index], mode) * W**exponent
    return result


def projectively_equal(left, right):
    left, right = KW(left), KW(right)
    return left.degree() == right.degree() and all(
        left[i] * right[j] == left[j] * right[i]
        for i in range(left.degree() + 1)
        for j in range(i + 1, left.degree() + 1)
    )


FACTOR_CACHE = {}


def factor_set(factors, mode):
    result = set()
    for factor in factors:
        key = (mode, str(factor))
        if key not in FACTOR_CACHE:
            transformed = strip_units(substitute(factor, mode)) if mode != "I" else strip_units(factor)
            FACTOR_CACHE[key] = tuple(
                primitive(item) for item, _ in transformed.factor()
                if not item.is_constant()
            )
        result.update(str(item) for item in FACTOR_CACHE[key])
    return sorted(result)


def target_map(target_id, mode):
    orbit, allocation = target_id.split("-")
    if mode == "B":
        orbit = {"A": "A", "TA": "TA", "OB": "OI", "OI": "OB"}[orbit]
    else:
        orbit = {"A": "TA", "TA": "A", "OB": "OB", "OI": "OI"}[orbit]
    return f"{orbit}-{allocation}"


cache = {assignment: build(assignment) for assignment in ASSIGNMENTS}
checks = 0
for mode in ("B", "TW"):
    for assignment, destination in B_MAP.items():
        source_residuals, source_systems = cache[assignment]
        destination_residuals, destination_systems = cache[destination]
        assert all(
            projectively_equal(transform_poly(source_residuals[index], mode), destination_residuals[index])
            for index in (0, 1)
        )
        for target_id, target_pair in TARGETS.items():
            destination_target = target_map(target_id, mode)
            assert all(
                projectively_equal(transform_poly(target_pair[index], mode), TARGETS[destination_target][index])
                for index in (0, 1)
            )
            assert factor_set(source_systems[target_id], mode) == factor_set(
                destination_systems[destination_target], "I"
            )
            checks += 1

payload = {
    "schema": "kb-c2-112-near-literal-inversion-transport-audit-v1",
    "assignments": int(len(ASSIGNMENTS)),
    "target_variants": int(len(TARGETS)),
    "checks": int(checks),
    "solver": "generic_5x5_solve_right",
    "imports_pr1140_compiler": False,
    "affine_semantic_orbits": 42,
    "canonical_orbits_covered": 12,
    "residual_affine_orbits": 30,
    "terminal": "INDEPENDENT_TRANSPORT_AUDIT_PASS",
}
print(
    "NEAR_LITERAL_AUDIT_JSON "
    + json.dumps(payload, sort_keys=True, separators=(",", ":"), default=int)
)
