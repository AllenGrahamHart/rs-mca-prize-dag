#!/usr/bin/env python3
"""Exact projective quarter certificate for the nu=0, b!=0, h=0 branch."""

from __future__ import annotations

import sympy as sp


Fp2 = tuple[int, int]
Poly = list[Fp2]
LABELS = ("1", "-1", "i", "-i")
PRIMES = (8191, 131071, 524287, 2147483647)
LARGEST = 2147483647
C0 = 241623698
C2 = 830673015
A_STAR = 844833809
B_STAR = 2002167159

U, V = sp.symbols("U V")
S_EXPR = 1 + U + V
Q_EXPR = U + V + U * V
E_EXPR = sp.expand(Q_EXPR * (4 * Q_EXPR - S_EXPR**2) - 3 * U * V * S_EXPR)
A_EXPR = 9 * Q_EXPR / S_EXPR**2 - 3
B_EXPR = 27 * U * V / S_EXPR**3 - A_EXPR - 1
assert sp.expand(sp.cancel(
    (9 * B_EXPR - 4 * A_EXPR**2 - 6 * A_EXPR) * S_EXPR**4
) + 81 * E_EXPR) == 0


def add(x: Fp2, y: Fp2, p: int) -> Fp2:
    return (x[0] + y[0]) % p, (x[1] + y[1]) % p


def neg(x: Fp2, p: int) -> Fp2:
    return -x[0] % p, -x[1] % p


def mul(x: Fp2, y: Fp2, p: int) -> Fp2:
    return ((x[0] * y[0] - x[1] * y[1]) % p,
            (x[0] * y[1] + x[1] * y[0]) % p)


def inverse(x: Fp2, p: int) -> Fp2:
    norm = (x[0] * x[0] + x[1] * x[1]) % p
    assert norm
    scalar = pow(norm, -1, p)
    return x[0] * scalar % p, -x[1] * scalar % p


def power(x: Fp2, exponent: int, p: int) -> Fp2:
    out = (1, 0)
    while exponent:
        if exponent & 1:
            out = mul(out, x, p)
        x = mul(x, x, p)
        exponent >>= 1
    return out


def label_value(label: str, p: int) -> Fp2:
    return {
        "1": (1, 0), "-1": (-1 % p, 0),
        "i": (0, 1), "-i": (0, -1 % p),
    }[label]


def trim(poly: Poly) -> Poly:
    while len(poly) > 1 and poly[-1] == (0, 0):
        poly.pop()
    return poly


def poly_mul(left: Poly, right: Poly, p: int) -> Poly:
    out = [(0, 0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = add(out[i + j], mul(x, y, p), p)
    return trim(out)


def poly_remainder(dividend: Poly, divisor: Poly, p: int) -> Poly:
    dividend, divisor = trim(dividend[:]), trim(divisor[:])
    inverse_leader = inverse(divisor[-1], p)
    while len(dividend) >= len(divisor) and dividend != [(0, 0)]:
        offset = len(dividend) - len(divisor)
        scale = mul(dividend[-1], inverse_leader, p)
        for index, value in enumerate(divisor):
            dividend[offset + index] = add(
                dividend[offset + index], neg(mul(scale, value, p), p), p
            )
        trim(dividend)
    return dividend


def poly_monic(poly: Poly, p: int) -> Poly:
    scalar = inverse(trim(poly)[-1], p)
    return [mul(value, scalar, p) for value in poly]


def poly_gcd(left: Poly, right: Poly, p: int) -> Poly:
    while right != [(0, 0)]:
        left, right = right, poly_remainder(left, right, p)
    return poly_monic(left, p)


def x_power_mod(exponent: int, modulus: Poly, p: int) -> Poly:
    out: Poly = [(1, 0)]
    base: Poly = [(0, 0), (1, 0)]
    while exponent:
        if exponent & 1:
            out = poly_remainder(poly_mul(out, base, p), modulus, p)
        base = poly_remainder(poly_mul(base, base, p), modulus, p)
        exponent >>= 1
    return out


def rational_mod(value: sp.Expr, p: int) -> int:
    value = sp.Rational(value)
    return int(value.p) % p * pow(int(value.q) % p, -1, p) % p


def gaussian_mod(value: sp.Expr, p: int) -> Fp2:
    expanded = sp.expand_complex(value)
    return rational_mod(sp.re(expanded), p), rational_mod(sp.im(expanded), p)


def symbolic_resultants() -> dict[tuple[str, str], sp.Poly]:
    symbolic = {"1": 1, "-1": -1, "i": sp.I, "-i": -sp.I}
    out = {}
    for epsilon_label in LABELS:
        for eta_label in LABELS:
            epsilon, eta = symbolic[epsilon_label], symbolic[eta_label]
            conjugate = sp.cancel(
                U**3 * V**3 * E_EXPR.subs({U: epsilon / U, V: eta / V})
            )
            out[(epsilon_label, eta_label)] = sp.Poly(
                sp.resultant(E_EXPR, conjugate, V), U, extension=sp.I
            )
    return out


def compatible_u_poly(resultant: sp.Poly, p: int, epsilon: Fp2) -> Poly:
    poly = [gaussian_mod(resultant.nth(index), p)
            for index in range(resultant.degree() + 1)]
    while poly[0] == (0, 0):
        poly.pop(0)  # Saturate the forbidden U=0 factor.
    poly = poly_monic(poly, p)
    remainder = x_power_mod(p + 1, poly, p)
    remainder[0] = add(remainder[0], neg(epsilon, p), p)
    return poly_gcd(poly, trim(remainder), p)


def expected_u_poly(p: int, epsilon: str, eta: str) -> Poly:
    one = [(1, 0)]
    x_plus_one = [(1, 0), (1, 0)]
    x2_plus_one = [(1, 0), (0, 0), (1, 0)]
    if (epsilon, eta) == ("1", "1"):
        return [(-1 % p, 0), (0, 0), (0, 0), (0, 0), (1, 0)]
    if (epsilon, eta) == ("1", "-1"):
        if p != LARGEST:
            return x_plus_one
        quadratic = [(1, 0), (-C2 % p, 0), (1, 0)]
        return poly_monic(poly_mul(x_plus_one, quadratic, p), p)
    if epsilon == "1" and eta in ("i", "-i"):
        return x2_plus_one
    if p == LARGEST and (epsilon, eta) == ("-1", "1"):
        return [(-1 % p, 0), (-C0 % p, 0), (1, 0)]
    if p == LARGEST and (epsilon, eta) == ("-1", "-1"):
        return [(-1 % p, 0), (C0, 0), (1, 0)]
    return one


def evaluate_e(u: Fp2, v: Fp2, p: int) -> Fp2:
    total = (0, 0)
    polynomial = sp.Poly(E_EXPR, U, V)
    for (u_degree, v_degree), coefficient in polynomial.terms():
        term = mul(power(u, u_degree, p), power(v, v_degree, p), p)
        total = add(total, mul((int(coefficient) % p, 0), term, p), p)
    return total


def projective_parameters(u: Fp2, v: Fp2, p: int) -> tuple[Fp2, Fp2]:
    one = (1, 0)
    total = add(add(one, u, p), v, p)
    pair = add(add(u, v, p), mul(u, v, p), p)
    assert total != (0, 0)
    a_value = add(
        mul((9, 0), mul(pair, power(inverse(total, p), 2, p), p), p),
        (-3 % p, 0), p,
    )
    b_value = add(
        mul((27, 0), mul(mul(u, v, p), power(inverse(total, p), 3, p), p), p),
        neg(add(a_value, one, p), p), p,
    )
    assert (mul((9, 0), b_value, p)
            == add(mul((4, 0), mul(a_value, a_value, p), p),
                   mul((6, 0), a_value, p), p))
    return a_value, b_value


def constant_packets(p: int) -> set[tuple[int, int]]:
    one, minus_one = (1, 0), (-1 % p, 0)
    i, minus_i = (0, 1), (0, -1 % p)
    roots = {
        one: [(0, 0), one],
        minus_one: [i, minus_i],
        i: [minus_one, minus_i, add(one, i, p)],
        minus_i: [minus_one, i, add(one, minus_i, p)],
    }
    out = set()
    for u, candidates in roots.items():
        for v in candidates:
            assert evaluate_e(u, v, p) == (0, 0)
            if (u == one or v in ((0, 0), one) or u == v
                    or add(add(one, u, p), v, p) == (0, 0)):
                continue
            if power(u, p + 1, p) not in map(lambda label: label_value(label, p), LABELS):
                continue
            if power(v, p + 1, p) not in map(lambda label: label_value(label, p), LABELS):
                continue
            a_value, b_value = projective_parameters(u, v, p)
            assert a_value[1] == b_value[1] == 0
            out.add((a_value[0], b_value[0]))
    return out


def quotient_packet(p: int, epsilon: int, eta: int,
                    c_value: int, d_value: int) -> tuple[int, int]:
    # Work in F_p[u]/(u^2-c_value*u-d_value).
    def qadd(x: Fp2, y: Fp2) -> Fp2:
        return add(x, y, p)

    def qneg(x: Fp2) -> Fp2:
        return neg(x, p)

    def qmul(x: Fp2, y: Fp2) -> Fp2:
        return ((x[0] * y[0] + d_value * x[1] * y[1]) % p,
                (x[0] * y[1] + x[1] * y[0]
                 + c_value * x[1] * y[1]) % p)

    def qinv(x: Fp2) -> Fp2:
        determinant = (x[0] * (x[0] + c_value * x[1])
                       - d_value * x[1] * x[1]) % p
        scalar = pow(determinant, -1, p)
        return ((x[0] + c_value * x[1]) * scalar % p,
                -x[1] * scalar % p)

    def qpower(x: Fp2, exponent: int) -> Fp2:
        out = (1, 0)
        while exponent:
            if exponent & 1:
                out = qmul(out, x)
            x = qmul(x, x)
            exponent >>= 1
        return out

    def evaluate_u(expression: sp.Expr) -> Fp2:
        polynomial = sp.Poly(expression, U)
        out, term, u_value = (0, 0), (1, 0), (0, 1)
        for index in range(polynomial.degree() + 1):
            out = qadd(out, qmul((int(polynomial.nth(index)) % p, 0), term))
            term = qmul(term, u_value)
        return out

    def as_v_poly(expression: sp.Expr) -> Poly:
        polynomial = sp.Poly(sp.expand(expression), V)
        return trim([evaluate_u(polynomial.nth(index))
                     for index in range(polynomial.degree() + 1)])

    def qpoly_remainder(dividend: Poly, divisor: Poly) -> Poly:
        dividend, divisor = trim(dividend[:]), trim(divisor[:])
        inverse_leader = qinv(divisor[-1])
        while len(dividend) >= len(divisor) and dividend != [(0, 0)]:
            offset = len(dividend) - len(divisor)
            scale = qmul(dividend[-1], inverse_leader)
            for index, value in enumerate(divisor):
                dividend[offset + index] = qadd(
                    dividend[offset + index], qneg(qmul(scale, value))
                )
            trim(dividend)
        return dividend

    def qpoly_gcd(left: Poly, right: Poly) -> Poly:
        while right != [(0, 0)]:
            left, right = right, qpoly_remainder(left, right)
        scalar = qinv(left[-1])
        return [qmul(value, scalar) for value in left]

    discriminant = (c_value * c_value + 4 * d_value) % p
    assert pow(discriminant, (p - 1) // 2, p) == p - 1
    transformed = sp.cancel(
        U**3 * V**3 * E_EXPR.subs({U: sp.Integer(epsilon) / U,
                                    V: sp.Integer(eta) / V})
    )
    common = qpoly_gcd(as_v_poly(E_EXPR), as_v_poly(transformed))
    assert len(common) == 2
    v_value = qmul(qneg(common[0]), qinv(common[1]))
    u_value = (0, 1)
    assert qpower(u_value, p + 1) == (epsilon % p, 0)
    assert qpower(v_value, p + 1) == (eta % p, 0)
    assert all(value != (0, 0) for value in
               (u_value, v_value, qadd(qadd((1, 0), u_value), v_value)))
    assert u_value != (1, 0) and v_value != (1, 0) and u_value != v_value

    total = qadd(qadd((1, 0), u_value), v_value)
    pair = qadd(qadd(u_value, v_value), qmul(u_value, v_value))
    a_value = qadd(qmul((9, 0), qmul(pair, qpower(qinv(total), 2))),
                   (-3 % p, 0))
    b_value = qadd(
        qmul((27, 0), qmul(qmul(u_value, v_value), qpower(qinv(total), 3))),
        qneg(qadd(a_value, (1, 0))),
    )
    assert qmul((9, 0), b_value) == qadd(
        qmul((4, 0), qmul(a_value, a_value)), qmul((6, 0), a_value)
    )
    assert a_value[1] == b_value[1] == 0
    return a_value[0], b_value[0]


def census() -> dict[int, set[tuple[int, int]]]:
    resultants = symbolic_resultants()
    output = {}
    for p in PRIMES:
        for epsilon_label in LABELS:
            for eta_label in LABELS:
                observed = compatible_u_poly(
                    resultants[(epsilon_label, eta_label)],
                    p,
                    label_value(epsilon_label, p),
                )
                expected = expected_u_poly(p, epsilon_label, eta_label)
                assert observed == expected, (p, epsilon_label, eta_label,
                                               observed, expected)
        parameters = constant_packets(p)
        if p == LARGEST:
            parameters.add(quotient_packet(p, 1, -1, C2, -1))
            parameters.add(quotient_packet(p, -1, 1, C0, 1))
            parameters.add(quotient_packet(p, -1, -1, -C0, 1))
        output[p] = parameters
    return output


def main() -> None:
    observed = census()
    expected = {
        8191: {(6, 20)},
        131071: {(6, 20)},
        524287: {(6, 20)},
        2147483647: {(6, 20), (A_STAR, B_STAR)},
    }
    assert observed == expected
    for p in PRIMES:
        print(f"p={p} projective_outer_parameters={sorted(observed[p])}")
    print("L1_M4_H3_NU0_H0_PROJECTIVE_QUARTER_CHECK_PASS")


if __name__ == "__main__":
    main()
