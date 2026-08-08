#!/usr/bin/env sage
"""Prove aligned-negative mismatch identities on every literal component."""

import hashlib
import json
import os


R = PolynomialRing(QQ, names=("b", "c", "d", "w"), order="degrevlex")
b, c, d, w = R.gens()
K = R.fraction_field()
bK, cK, dK, wK = map(K, R.gens())
KW = PolynomialRing(K, "W")
W = KW.gen()

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


def primitive(value):
    value = R(value)
    if not value:
        return value
    value = R(value / value.content())
    return -value if value.leading_coefficient() < 0 else value


def edge(edge_id):
    left_id, right_id = EDGE_VERTICES[edge_id]
    left, right = VERTICES[left_id], VERTICES[right_id]
    return vector(K, (left * right, -(left + right), 1))


assignment = os.environ["NEGATIVE_ASSIGNMENT"]
chart = os.environ["NEGATIVE_CHART"]
if assignment not in ASSIGNMENTS or chart not in ("generic", "sum-zero"):
    raise RuntimeError("assignment/chart")

first_id, second_id = ASSIGNMENTS[assignment]
first_vertices = set(EDGE_VERTICES[first_id])
second_vertices = set(EDGE_VERTICES[second_id])
common_id = next(iter(first_vertices & second_vertices))
right_id = next(iter(first_vertices - {common_id}))
left_id = next(iter(second_vertices - {common_id}))
common, right, left = (
    VERTICES[common_id], VERTICES[right_id], VERTICES[left_id]
)
first, second = edge(first_id), edge(second_id)

q0, q1 = cK * dK, -(cK + dK)
f = q0 + wK
g = -1 - wK * q0
m = q1 * (1 + wK)
v = vector(KW, (f + g * W, m * (1 - W), -(g + f * W)))
v_common = sum(v[index] * common**index for index in range(3))
z = -K(v_common[0]) / K(v_common[1])
vz = vector(K, (entry(z) for entry in v))
linear_1, linear_0 = vz[2], vz[1] + common * vz[2]
target = (
    (linear_0 + left * linear_1) * first
    + (linear_0 + right * linear_1) * second
) / (left - right)

matrix_full = matrix(K, (
    (1 + q0 * wK**2, wK * (1 + q0), wK**2 + q0, 0),
    (q1 * wK**2, q1 * wK, q1, 1 - wK**2),
    (1, z, z**2, 0),
    (0, 0, 0, 1 - z**2),
    (-z**2, -z, -1, 0),
))
right_hand = vector(K, (0, 0, *target))
omitted = 2 if chart == "generic" else 3
selected_rows = [index for index in range(5) if index != omitted]
matrix_selected = matrix_full.matrix_from_rows(selected_rows)
right_selected = vector(K, [right_hand[index] for index in selected_rows])
determinant = K(matrix_selected.det())
solution = matrix_selected.solve_right(right_selected)
consistency = K(
    matrix_full.row(omitted).dot_product(solution) - right_hand[omitted]
)

x0, x1, x2, x3 = solution
u = vector(KW, (
    x0 + x1 * W + x2 * W**2,
    x3 * (1 - W**2),
    -(x2 + x1 * W + x0 * W**2),
))

def residual(root):
    u_root = sum(u[index] * root**index for index in range(3))
    v_root = sum(v[index] * root**index for index in range(3))
    quotient, remainder = (u_root**2 - W * v_root**2).quo_rem((W - wK)**2)
    if remainder or quotient.degree() != 2:
        raise RuntimeError("forced square division")
    return quotient


observed = residual(cK) * residual(dK)
expected = (W - 1 / cK)**2 * (W - 1 / dK)**2
if observed.degree() != 4:
    raise RuntimeError("aligned residual degree")
lead = K(observed[4])
mismatches = [K(observed[index] / lead - expected[index]) for index in range(4)]


def zero_mod_relations(value, relations):
    numerator = primitive(K(value).numerator())
    relation_values = [primitive(K(item).numerator()) for item in relations]
    relation_values = [item for item in relation_values if item]
    if not relation_values:
        return bool(not numerator), "NO_RELATIONS"
    remainder = R.ideal(relation_values).reduce(numerator)
    return (
        bool(not remainder),
        hashlib.sha256(str(remainder).encode()).hexdigest(),
    )


constant_target = (cK * dK - 1) * (cK * dK + 1) / (cK**2 * dK**2)
determinant_numerator = primitive(determinant.numerator())
determinant_factors = [str(factor) for factor, _ in determinant_numerator.factor()]
cover_factor = "c + d" if chart == "generic" else "c*d + 1"
cover_pass = (
    (R(c + d) in [R(factor) for factor, _ in determinant_numerator.factor()])
    if chart == "generic"
    else (R(c * d + 1) in [R(factor) for factor, _ in determinant_numerator.factor()])
)

consistency_numerator = primitive(consistency.numerator())
consistency_factorization = list(consistency_numerator.factor())
survivor_factors = [
    primitive(factor)
    for factor, _ in consistency_factorization
    if determinant_numerator.quo_rem(factor)[1]
]
if not survivor_factors:
    raise RuntimeError("no survivor consistency factor")

component_rows = []
for component in survivor_factors:
    constant_relations = [component]
    if chart == "sum-zero":
        constant_relations.append(cK + dK)
    constant_pass, constant_remainder = zero_mod_relations(
        mismatches[0] - constant_target, constant_relations
    )

    if chart == "generic":
        specialization = {dK: -1 / cK}
        outer_value = K(
            (mismatches[1] - mismatches[3]).subs(specialization)
            - 4 * (cK**2 - 1) / cK
        )
        specialized_component = K(K(component).subs(specialization))
        outer_pass, outer_remainder = zero_mod_relations(
            outer_value, [specialized_component]
        )
    else:
        outer_pass = True
        outer_remainder = "NOT_NEEDED_SUM_ZERO"

    component_rows.append({
        "factor": str(component),
        "factor_sha256": hashlib.sha256(str(component).encode()).hexdigest(),
        "constant_identity_pass": bool(constant_pass),
        "constant_remainder": constant_remainder,
        "outer_identity_pass": bool(outer_pass),
        "outer_remainder": outer_remainder,
    })

constant_pass = all(row["constant_identity_pass"] for row in component_rows)
outer_pass = all(row["outer_identity_pass"] for row in component_rows)

payload = {
    "schema": "kb-c2-112-aligned-negative-literal-identity-v2",
    "assignment": assignment,
    "assignment_kind": "fixed-moving" if assignment.startswith("F") else "moving-moving",
    "common_vertex": common_id,
    "chart": chart,
    "omitted_row": int(omitted),
    "determinant_sha256": hashlib.sha256(str(determinant_numerator).encode()).hexdigest(),
    "determinant_factors": determinant_factors,
    "cover_factor": cover_factor,
    "cover_factor_pass": bool(cover_pass),
    "consistency_factor_count": len(consistency_factorization),
    "survivor_component_count": len(component_rows),
    "components": component_rows,
    "constant_identity_pass": bool(constant_pass),
    "outer_identity_pass": bool(outer_pass),
    "terminal": (
        "ALIGNED_NEGATIVE_LITERAL_IDENTITIES_PASS"
        if cover_pass and constant_pass and outer_pass
        else "ALIGNED_NEGATIVE_LITERAL_IDENTITY_FAILURE"
    ),
}
print("ALIGNED_NEGATIVE_LITERAL_JSON " + json.dumps(
    payload, sort_keys=True, separators=(",", ":"), default=int
))
if payload["terminal"] != "ALIGNED_NEGATIVE_LITERAL_IDENTITIES_PASS":
    raise RuntimeError(payload["terminal"])
