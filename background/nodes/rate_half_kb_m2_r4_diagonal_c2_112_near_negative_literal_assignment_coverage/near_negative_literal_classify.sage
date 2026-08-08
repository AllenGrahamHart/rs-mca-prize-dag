#!/usr/bin/env sage
"""Classify one reduced near-negative literal assignment/root cell."""

import hashlib
import json
import os
import sys
import time


R = PolynomialRing(QQ, names=("b", "c", "w"), order="degrevlex")
b, c, w = R.gens()
K = R.fraction_field()
bK, cK, wK = map(K, R.gens())
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
ROOTS = {"A": K(1) / 2, "TA": K(2), "OB": K(1) / bK, "OI": bK}


def primitive(value):
    value = R(value)
    if not value:
        return value
    value = R(value / value.content())
    return -value if value.leading_coefficient() < 0 else value


def irreducible_factors(value):
    value = primitive(value)
    if not value or value.is_constant():
        return ()
    return tuple(primitive(factor) for factor, _ in value.factor())


def add_nonzero(factors, value):
    value = K(value)
    factors.update(irreducible_factors(value.numerator()))
    factors.update(irreducible_factors(value.denominator()))


def add_denominators(factors, value):
    for coefficient in KW(value):
        factors.update(irreducible_factors(K(coefficient).denominator()))


def edge(edge_id):
    left_id, right_id = EDGE_VERTICES[edge_id]
    left, right = VERTICES[left_id], VERTICES[right_id]
    return vector(K, (left * right, -(left + right), 1))


cell = os.environ["NEAR_NEGATIVE_CELL"]
saturation_mode = os.environ.get("NEAR_NEGATIVE_SATURATION_MODE", "rabinowitsch")
if saturation_mode not in ("rabinowitsch", "sequential"):
    raise RuntimeError(f"unknown saturation mode: {saturation_mode}")
assignment, root_id = cell.split("-")
if assignment not in ASSIGNMENTS or root_id not in ROOTS:
    raise RuntimeError(f"unknown cell: {cell}")
root = ROOTS[root_id]
dK = -1 / root

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
selected_rows = (0, 1, 3, 4)
matrix_selected = matrix_full.matrix_from_rows(selected_rows)
right_selected = vector(K, [right_hand[index] for index in selected_rows])
determinant = K(matrix_selected.det())
solution = matrix_selected.solve_right(right_selected)
consistency = K(matrix_full.row(2).dot_product(solution) - right_hand[2])

x0, x1, x2, x3 = solution
u = vector(KW, (
    x0 + x1 * W + x2 * W**2,
    x3 * (1 - W**2),
    -(x2 + x1 * W + x0 * W**2),
))


def residual(value):
    u_root = sum(u[index] * value**index for index in range(3))
    v_root = sum(v[index] * value**index for index in range(3))
    quotient, remainder = (u_root**2 - W * v_root**2).quo_rem((W - wK)**2)
    if remainder or quotient.degree() != 2:
        raise RuntimeError("forced square division")
    return quotient


observed = residual(cK) * residual(dK)
if observed.degree() != 4:
    raise RuntimeError("residual degree")
lead = K(observed[4])
observed = observed / lead
expected = (W - 1 / root)**2 * (W - 1 / dK)**2
mismatches = [K(observed[index] - expected[index]) for index in range(4)]

determinant_numerator = primitive(determinant.numerator())
consistency_numerator = primitive(consistency.numerator())
consistency_factorization = list(consistency_numerator.factor())
survivor_factors = [
    primitive(factor)
    for factor, _ in consistency_factorization
    if determinant_numerator.quo_rem(factor)[1]
]
expected_components = 1 if assignment.startswith("F") else 2
if len(survivor_factors) != expected_components:
    raise RuntimeError(f"survivor component count: {len(survivor_factors)}")

factors = set()
for value in (
    bK, bK - 1, bK + 1, bK - 2, 2 * bK - 1,
    cK, cK - 1, cK + 1, cK - 2, 2 * cK - 1,
    cK - bK, bK * cK - 1,
    dK, dK - 1, dK + 1, dK - 2, 2 * dK - 1,
    dK - bK, bK * dK - 1,
    cK - dK, cK * dK - 1, cK + dK,
    dK - root, wK, wK - 1, wK + 1,
    v_common[1], left - right, z, 1 - z**2,
    (wK - z) * (1 - wK * z), lead, determinant,
):
    add_nonzero(factors, value)
for value in (*target, *u, *v, observed, expected, *mismatches, consistency):
    add_denominators(factors, value)

p = 2130706433
Fp = GF(p)
S = PolynomialRing(Fp, names=("b", "c", "w"), order="degrevlex")
localizers = [S(item) for item in sorted(factors, key=str)]
localizer_product = S.one()
for factor in localizers:
    localizer_product *= factor

component_rows = []
for index, component in enumerate(survivor_factors):
    equations = [S(component)]
    equations.extend(S(primitive(value.numerator())) for value in mismatches)
    constant_remainder = S.ideal([S(component)]).reduce(equations[1])
    if constant_remainder:
        raise RuntimeError("constant identity after xi*d=-1")

    started = time.monotonic()
    if saturation_mode == "rabinowitsch":
        T = PolynomialRing(Fp, names=("y", "b", "c", "w"), order="degrevlex")
        y = T.gen(0)
        extended = [T(item) for item in equations]
        extended.append(1 - y * T(localizer_product))
        basis = T.ideal(extended).groebner_basis()
    else:
        current = S.ideal(equations)
        for factor in localizers:
            saturation = current.saturation(S.ideal([factor]))
            current = saturation if hasattr(saturation, "gens") else saturation[0]
        basis = current.groebner_basis()
    seconds = time.monotonic() - started
    unit = len(basis) == 1 and basis[0] == 1
    component_rows.append({
        "index": index,
        "factor": str(component),
        "factor_sha256": hashlib.sha256(str(component).encode()).hexdigest(),
        "equation_count": len(equations),
        "equation_tuple_sha256": hashlib.sha256(
            "\n".join(str(item) for item in equations).encode()
        ).hexdigest(),
        "basis_seconds": float(seconds),
        "basis_size": len(basis),
        "basis_sha256": hashlib.sha256(
            "\n".join(str(item) for item in basis).encode()
        ).hexdigest(),
        "unit_ideal": bool(unit),
        "saturation_mode": saturation_mode,
    })
    print("NEAR_NEGATIVE_COMPONENT_JSON " + json.dumps({
        "cell": cell,
        "component": component_rows[-1],
    }, sort_keys=True, separators=(",", ":"), default=int))
    sys.stdout.flush()

payload = {
    "schema": "kb-c2-112-near-negative-literal-cell-v1",
    "cell": cell,
    "assignment": assignment,
    "assignment_kind": "fixed-moving" if assignment.startswith("F") else "moving-moving",
    "common_vertex": common_id,
    "target_root": root_id,
    "minus_branch": str(dK),
    "consistency_factor_count": len(consistency_factorization),
    "survivor_component_count": len(survivor_factors),
    "localizer_count": len(localizers),
    "localizer_product_degree": int(localizer_product.total_degree()),
    "localizer_product_terms": int(len(localizer_product.dict())),
    "localizer_product_sha256": hashlib.sha256(str(localizer_product).encode()).hexdigest(),
    "saturation_mode": saturation_mode,
    "components": component_rows,
    "terminal": (
        "NEAR_NEGATIVE_LITERAL_UNIT"
        if all(item["unit_ideal"] for item in component_rows)
        else "NEAR_NEGATIVE_LITERAL_SURVIVOR"
    ),
}
print("NEAR_NEGATIVE_LITERAL_JSON " + json.dumps(
    payload, sort_keys=True, separators=(",", ":"), default=int
))
if payload["terminal"] != "NEAR_NEGATIVE_LITERAL_UNIT":
    raise RuntimeError(payload["terminal"])
