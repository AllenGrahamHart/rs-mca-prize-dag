#!/usr/bin/env sage
"""Test the M01-A-RL q-slice survivor against the first quotient norm."""

load("/near_literal_assignment_transport_audit.sage")

import hashlib
import json


recorded_factor_strings = {
    (assignment, orbit): factor_set(
        cache[assignment][1][f"{orbit}-RL"], "I"
    )
    for assignment in ("M01", "M02")
    for orbit in ("A", "TA")
}

p = 2130706433
Fp = GF(p)
PB = PolynomialRing(Fp, "x")
x = PB.gen()
modulus = x**2 + Fp(253153238) * x - Fp(400825962)
factorization = modulus.factor()
if len(factorization) == 1 and factorization[0][0].degree() == 2:
    E = GF(p**2, name="B", modulus=modulus)
    B = E.gen()
    b_roots = (B, B**p)
    residue_degree = 2
else:
    E = Fp
    b_roots = tuple(root for root, multiplicity in modulus.roots())
    residue_degree = 1


def edge(left, right):
    return vector(E, (left * right, -(left + right), E.one()))


def evaluation(point):
    return matrix(E, (
        (1, point, point**2, 0, 0),
        (0, 0, 0, 1 + point**2, point),
        (point**2, point, 1, 0, 0),
    ))


def projectively_equal(left, right):
    return left.degree() == right.degree() and all(
        left[i] * right[j] == left[j] * right[i]
        for i in range(left.degree() + 1)
        for j in range(i + 1, left.degree() + 1)
    )


def mismatch_digest(left, right):
    mismatches = []
    for i in range(left.degree() + 1):
        for j in range(i + 1, left.degree() + 1):
            value = left[i] * right[j] - left[j] * right[i]
            if value:
                mismatches.append(f"{i},{j}:{value}")
    return hashlib.sha256("\n".join(mismatches).encode()).hexdigest(), len(mismatches)


def run_root(assignment, orbit, b):
    c = E.one() / 2 if orbit == "A" else E(2)
    d = -E.one()
    w = E.one() / c
    target_root = E.one() / 2 if orbit == "A" else E(2)
    Wring = PolynomialRing(E, "W")
    W = Wring.gen()

    q0, q1 = c * d, -(c + d)
    f, g, m = q0 - w, 1 - w * q0, q1 * (1 - w)
    v = vector(Wring, (f + g * W, m * (1 + W), g + f * W))

    common = b if assignment == "M01" else E.one() / b
    right, left = E(2), E.one() / 2
    first, second = edge(right, common), edge(left, common)
    v_common = v[0] + common * v[1] + common**2 * v[2]
    z = -v_common[0] / v_common[1]
    vz = vector(E, (entry(z) for entry in v))
    linear_1, linear_0 = vz[2], vz[1] + common * vz[2]
    target = (
        (linear_0 + left * linear_1) * first
        + (linear_0 + right * linear_1) * second
    ) / (left - right)

    at_w, at_z = evaluation(w), evaluation(z)
    coefficient_matrix = matrix(E, (
        at_w[0] - q0 * at_w[2],
        at_w[1] - q1 * at_w[2],
        *at_z.rows(),
    ))
    solution = coefficient_matrix.solve_right(vector(E, (0, 0, *target)))
    u = vector(Wring, (
        solution[0] + solution[1] * W + solution[2] * W**2,
        solution[3] * (1 + W**2) + solution[4] * W,
        solution[2] + solution[1] * W + solution[0] * W**2,
    ))

    def g_at(t_value):
        u_value = sum(u[index] * t_value**index for index in range(3))
        v_value = sum(v[index] * t_value**index for index in range(3))
        return u_value**2 - W * v_value**2

    def evaluate_recorded(text):
        polynomial = R(text)
        value = E.zero()
        for exponents, coefficient in polynomial.dict().items():
            scalar = E(int(coefficient.numerator())) / E(int(coefficient.denominator()))
            value += scalar * b**exponents[0] * c**exponents[1] * d**exponents[2]
        return value

    localizer_values = [
        evaluate_recorded(text)
        for text in recorded_factor_strings[(assignment, orbit)]
    ]
    localizer_values.extend((b, c, d, c - d))
    complete_localizers_nonzero = all(value != 0 for value in localizer_values)

    residual_c, remainder_c = g_at(c).quo_rem((W - w)**2)
    residual_d, remainder_d = g_at(d).quo_rem((W - w)**2)
    endpoint_passes = (
        remainder_c == 0 and projectively_equal(residual_c, (W - E.one() / d)**2),
        remainder_d == 0 and projectively_equal(residual_d, (W - target_root)**2),
    )

    q_slice = g_at(c) * g_at(d)
    q_slice_target = (
        (W - w)**4 * (W - target_root)**2 * (W - E.one() / d)**2
    )
    q_slice_pass = projectively_equal(q_slice, q_slice_target)

    p_j_roots = (E(2), E.one() / 2, b, E.one() / b, c, d)
    resultant_j = Wring.one()
    for root in p_j_roots:
        resultant_j *= g_at(root)

    k5 = (
        (W - w) * (W - z) * (W - E.one() / z)
        * (W - target_root) * (W - E.one() / d)
    )
    chi_omega = (W - E.one() / target_root) * (W - d)
    first_target = k5**4 * chi_omega**2
    first_pass = projectively_equal(resultant_j, first_target)
    digest, mismatch_count = mismatch_digest(resultant_j, first_target)
    return {
        "assignment": assignment,
        "orbit": orbit,
        "b": str(b),
        "z": str(z),
        "complete_localizer_count": len(localizer_values),
        "complete_localizers_nonzero": bool(complete_localizers_nonzero),
        "endpoint_passes": tuple(bool(value) for value in endpoint_passes),
        "q_slice_pass": bool(q_slice_pass),
        "first_quotient_norm_pass": bool(first_pass),
        "first_mismatch_count": int(mismatch_count),
        "first_mismatch_sha256": digest,
    }


records = []
for orbit in ("A", "TA"):
    records.extend(run_root("M01", orbit, root) for root in b_roots)
    records.extend(run_root("M02", orbit, E.one() / root) for root in b_roots)
payload = {
    "schema": "kb-c2-112-near-positive-m01-a-rl-first-quotient-probe-v1",
    "cell": "M01-A-RL",
    "b_modulus": str(modulus),
    "b_modulus_sha256": hashlib.sha256(str(modulus).encode()).hexdigest(),
    "residue_degree": int(residue_degree),
    "orientations": len(records),
    "records": records,
    "terminal": (
        "FIRST_QUOTIENT_REJECTS_ALL"
        if all(
            row["complete_localizers_nonzero"]
            and all(row["endpoint_passes"])
            and row["q_slice_pass"]
            and not row["first_quotient_norm_pass"]
            for row in records
        )
        else "FIRST_QUOTIENT_SURVIVOR_OR_CONTROL_FAILURE"
    ),
}
print("M01_A_RL_FIRST_QUOTIENT_JSON " + json.dumps(
    payload, sort_keys=True, separators=(",", ":")
))

if payload["terminal"] != "FIRST_QUOTIENT_REJECTS_ALL":
    raise RuntimeError(payload["terminal"])
