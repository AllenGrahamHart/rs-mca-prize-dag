#!/usr/bin/env sage
"""Classify one literal positive projective-boundary q-slice cell."""

import hashlib
import json
import os
import sys
import time


R = PolynomialRing(QQ, names=("b", "d"), order="degrevlex")
b, d = R.gens()
K = R.fraction_field()
bK, dK = map(K, R.gens())
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


def add_nonzero(factors, value):
    value = K(value)
    factors.update(irreducible_factors(value.numerator()))
    factors.update(irreducible_factors(value.denominator()))


def add_denominator(factors, value):
    for coefficient in KW(value):
        factors.update(irreducible_factors(K(coefficient).denominator()))


def residual_after_w2(value):
    quotient, remainder = KW(value).quo_rem(W**2)
    if remainder or quotient.degree() != 2:
        raise RuntimeError("projective W^2 residual")
    return quotient


cell = os.environ["BOUNDARY_CELL"]
saturation_mode = os.environ.get("BOUNDARY_SATURATION_MODE", "rabinowitsch")
if saturation_mode not in ("rabinowitsch", "sequential"):
    raise RuntimeError(f"unknown saturation mode: {saturation_mode}")
assignment, root_id = cell.split("-")
if assignment not in ASSIGNMENTS or root_id not in ROOTS:
    raise RuntimeError(f"unknown cell: {cell}")

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

# Homogeneous q=Y(T-dY), with source-boundary label w=0.
v = vector(KW, (-dK, 1 + W, -dK * W))
v_common = sum(v[index] * common**index for index in range(3))
z = -K(v_common[0]) / K(v_common[1])
vz = vector(K, (entry(z) for entry in v))
linear_1, linear_0 = vz[2], vz[1] + common * vz[2]
target = (
    (linear_0 + left * linear_1) * first
    + (linear_0 + right * linear_1) * second
) / (left - right)

coefficient_matrix = matrix(K, (
    (0, 0, 1, 0, 0),
    (1, 0, 0, dK, 0),
    *evaluation(z).rows(),
))
solution = coefficient_matrix.solve_right(vector(K, (0, 0, *target)))
if coefficient_matrix * solution != vector(K, (0, 0, *target)):
    raise RuntimeError("boundary reconstruction")
u = vector(KW, (
    solution[0] + solution[1] * W + solution[2] * W**2,
    solution[3] * (1 + W**2) + solution[4] * W,
    solution[2] + solution[1] * W + solution[0] * W**2,
))

u_d = sum(u[index] * dK**index for index in range(3))
v_d = sum(v[index] * dK**index for index in range(3))
finite = residual_after_w2(u_d**2 - W * v_d**2)
infinity = residual_after_w2(u[2]**2 - W * v[2]**2)
observed = finite * infinity
if observed.degree() != 4:
    raise RuntimeError("projective product degree")
root = ROOTS[root_id]
expected = (W - 1 / root) ** 2 * (W - 1 / dK) ** 2

equations_q = []
for index in range(4):
    raw = K(observed[index] - observed[4] * expected[index])
    equations_q.append(primitive(raw.numerator()))

factors = set()
for base in (
    b, b - 1, b + 1, b - 2, 2 * b - 1,
    d, d - 1, d + 1, d - 2, 2 * d - 1, d - b, b * d - 1,
):
    factors.update(irreducible_factors(base))
for value in (
    v_common[1], left - right, z, 1 - z**2,
    coefficient_matrix.det(), observed[4], dK - root,
):
    add_nonzero(factors, value)
for value in (*target, *solution, *u, *finite, *infinity, *observed, *expected):
    add_denominator(factors, value)
for equation in equations_q:
    if not equation:
        raise RuntimeError("unexpected zero boundary equation")

factor_strings = sorted(str(item) for item in factors)
p = 2130706433
Fp = GF(p)
S = PolynomialRing(Fp, names=("b", "d"), order="degrevlex")
equations = [S(item) for item in equations_q]
localizers = [S(R(text)) for text in factor_strings]
localizer_product = S.one()
for factor in localizers:
    localizer_product *= factor

compiled = {
    "schema": "kb-c2-112-near-positive-projective-boundary-literal-cell-v1",
    "cell": cell,
    "assignment": assignment,
    "assignment_kind": "fixed-moving" if assignment.startswith("F") else "moving-moving",
    "common_vertex": common_id,
    "target_root": root_id,
    "equation_count": len(equations),
    "equation_tuple_sha256": hashlib.sha256(
        "\n".join(str(item) for item in equations).encode()
    ).hexdigest(),
    "localizer_count": len(localizers),
    "localizer_product_degree": int(localizer_product.total_degree()),
    "localizer_product_terms": int(len(localizer_product.dict())),
    "localizer_product_sha256": hashlib.sha256(
        str(localizer_product).encode()
    ).hexdigest(),
    "saturation_mode": saturation_mode,
    "terminal": "LITERAL_BOUNDARY_COMPILED",
}
print("LITERAL_BOUNDARY_JSON " + json.dumps(
    compiled, sort_keys=True, separators=(",", ":")
))
sys.stdout.flush()

started = time.monotonic()
if saturation_mode == "rabinowitsch":
    T = PolynomialRing(Fp, names=("y", "b", "d"), order="degrevlex")
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
unit = len(basis) == 1 and basis[0] == 1
payload = {
    **compiled,
    "basis_seconds": float(time.monotonic() - started),
    "basis_size": len(basis),
    "basis_sha256": hashlib.sha256(
        "\n".join(str(item) for item in basis).encode()
    ).hexdigest(),
    "unit_ideal": bool(unit),
    "terminal": (
        "LITERAL_BOUNDARY_UNIT_IDEAL"
        if unit else "LITERAL_BOUNDARY_SURVIVOR"
    ),
}
print("LITERAL_BOUNDARY_JSON " + json.dumps(
    payload, sort_keys=True, separators=(",", ":")
))
sys.stdout.flush()
