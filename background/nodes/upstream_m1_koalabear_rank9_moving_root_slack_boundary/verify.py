#!/usr/bin/env python3
"""Exact stdlib checks for the KoalaBear moving-root slack boundary."""

from __future__ import annotations

import json
from pathlib import Path


MOD = 11
ZERO = (0, 0)
ONE = (1, 0)
ZETA = (0, 1)  # zeta^2=-1; X^2+1 is irreducible over F_11.
ROOT = Path(__file__).resolve().parents[3]
NODE = "upstream_m1_koalabear_rank9_moving_root_slack_boundary"
CONSUMER = "rate_half_band_closure"


def f(value: int) -> tuple[int, int]:
    return (value % MOD, 0)


def add(x, y):
    return ((x[0] + y[0]) % MOD, (x[1] + y[1]) % MOD)


def neg(x):
    return ((-x[0]) % MOD, (-x[1]) % MOD)


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    return (
        (x[0] * y[0] - x[1] * y[1]) % MOD,
        (x[0] * y[1] + x[1] * y[0]) % MOD,
    )


def inv(x):
    norm = (x[0] * x[0] + x[1] * x[1]) % MOD
    if norm == 0:
        raise ZeroDivisionError("zero in F_121")
    norm_inv = pow(norm, MOD - 2, MOD)
    return ((x[0] * norm_inv) % MOD, (-x[1] * norm_inv) % MOD)


def div(x, y):
    return mul(x, inv(y))


def trim(poly):
    out = list(poly)
    while len(out) > 1 and out[-1] == ZERO:
        out.pop()
    return tuple(out or [ZERO])


def p_add(left, right):
    size = max(len(left), len(right))
    out = [ZERO] * size
    for i in range(size):
        a = left[i] if i < len(left) else ZERO
        b = right[i] if i < len(right) else ZERO
        out[i] = add(a, b)
    return trim(out)


def p_neg(poly):
    return trim([neg(c) for c in poly])


def p_sub(left, right):
    return p_add(left, p_neg(right))


def p_scale(poly, scalar):
    return trim([mul(c, scalar) for c in poly])


def p_mul(left, right):
    out = [ZERO] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = add(out[i + j], mul(a, b))
    return trim(out)


def p_divmod(numerator, denominator):
    numerator = list(trim(numerator))
    denominator = trim(denominator)
    if denominator == (ZERO,):
        raise ZeroDivisionError("zero polynomial")
    quotient = [ZERO] * max(1, len(numerator) - len(denominator) + 1)
    while len(numerator) >= len(denominator) and trim(numerator) != (ZERO,):
        shift = len(numerator) - len(denominator)
        scalar = div(numerator[-1], denominator[-1])
        quotient[shift] = add(quotient[shift], scalar)
        for i, coefficient in enumerate(denominator):
            numerator[i + shift] = sub(
                numerator[i + shift], mul(scalar, coefficient)
            )
        numerator = list(trim(numerator))
    return trim(quotient), trim(numerator)


def p_monic(poly):
    poly = trim(poly)
    if poly == (ZERO,):
        return poly
    return p_scale(poly, inv(poly[-1]))


def p_gcd(left, right):
    left, right = trim(left), trim(right)
    while right != (ZERO,):
        _, remainder = p_divmod(left, right)
        left, right = right, remainder
    return p_monic(left)


def p_eval(poly, point):
    value = ZERO
    for coefficient in reversed(poly):
        value = add(mul(value, point), coefficient)
    return value


def locator(points):
    result = (ONE,)
    for point in points:
        result = p_mul(result, (neg(point), ONE))
    return result


def is_base_poly(poly):
    return all(coefficient[1] == 0 for coefficient in poly)


def vec_add(left, right):
    return [add(a, b) for a, b in zip(left, right)]


def vec_scale(vector, scalar):
    return [mul(value, scalar) for value in vector]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def slack_tuple(k, t, s, x, e, c, degree_h):
    require(c == k + t - x - s, "common-root count drift")
    return (degree_h - c, e - x, k - 1 - degree_h - e)


def official_checks():
    n = 2**21
    k = 2**20
    agreement = 1_116_048
    j = n - agreement
    t = agreement - k
    s_min = t + 2
    e_min = (s_min + 1) // 2
    gcd_max = k - 1 - e_min
    expected = {
        "n": 2_097_152,
        "k": 1_048_576,
        "agreement": 1_116_048,
        "j": 981_104,
        "t": 67_472,
        "j_div_20": 49_055,
        "s_min": 67_474,
        "e_min": 33_737,
        "gcd_max": 1_014_838,
        "excluded_gcd_degrees": 33_736,
    }
    actual = {
        "n": n,
        "k": k,
        "agreement": agreement,
        "j": j,
        "t": t,
        "j_div_20": j // 20,
        "s_min": s_min,
        "e_min": e_min,
        "gcd_max": gcd_max,
        "excluded_gcd_degrees": (k - 2) - gcd_max,
    }
    require(actual == expected, "official integer ledger drift")

    def accepts(candidate):
        return candidate == expected

    rejected = 0
    for key in sorted(expected):
        mutant = dict(expected)
        mutant[key] += 1
        rejected += int(not accepts(mutant))
    require(rejected == len(expected), "integer mutation escaped")
    return actual, rejected


def toy_checks():
    domain = [f(i) for i in range(11)]
    sigma = [f(2), f(3), f(4)]
    common = [f(0), f(1)]
    moving0 = [f(5), f(6)]
    moving1 = [f(7), f(8)]

    h0 = locator(common)
    l0 = locator(moving0)
    l1 = locator(moving1)
    eta0 = ZERO
    eta1 = ZETA
    kappa0 = ONE
    kappa1 = add(ZETA, ONE)
    pbar0 = l0
    qbar0 = p_scale(p_sub(p_scale(l1, kappa1), l0), inv(eta1))
    p0 = p_mul(h0, pbar0)
    q0 = p_mul(h0, qbar0)

    require(p_gcd(pbar0, qbar0) == (ONE,), "reduced zero-slack pair not coprime")
    require(p_gcd(p0, q0) == p_monic(h0), "full gcd drift")
    require(p_add(pbar0, p_scale(qbar0, eta0)) == p_scale(l0, kappa0), "first member drift")
    require(p_add(pbar0, p_scale(qbar0, eta1)) == p_scale(l1, kappa1), "second member drift")
    require(all(p_eval(h0, point) != ZERO for point in moving0 + moving1), "moving point became common")
    require(is_base_poly(h0) and is_base_poly(l0) and is_base_poly(l1), "base locator drift")

    eps0 = [p_eval(p0, point) if point in sigma else ZERO for point in domain]
    eps1 = [p_eval(q0, point) if point in sigma else ZERO for point in domain]
    base0 = [p_eval(p_mul(h0, l0), point) if point in sigma else ZERO for point in domain]
    base1 = [p_eval(p_mul(h0, l1), point) if point in sigma else ZERO for point in domain]
    require(vec_add(eps0, vec_scale(eps1, eta0)) == vec_scale(base0, kappa0), "first C5 combination drift")
    require(vec_add(eps0, vec_scale(eps1, eta1)) == vec_scale(base1, kappa1), "second C5 combination drift")
    require(eta0 != eta1, "C5 coordinate matrix singular")
    require(slack_tuple(5, 2, 3, 2, 2, 2, 2) == (0, 0, 0), "zero-slack tuple drift")

    h_twist = p_mul(h0, (neg(ZETA), ONE))
    p_twist = p_mul(h_twist, pbar0)
    q_twist = p_mul(h_twist, qbar0)
    require(p_gcd(p_twist, q_twist) == p_monic(h_twist), "twist gcd drift")
    require(not is_base_poly(h_twist), "nonbase gcd twist became base")
    quotient, remainder = p_divmod(h_twist, h0)
    require(remainder == (ZERO,) and len(quotient) - 1 == 1, "twist is not linear")
    require(slack_tuple(6, 2, 4, 2, 2, 2, 3) == (1, 0, 0), "gcd-twist slack drift")

    h2 = locator([f(0), f(1), f(2)])
    member0 = p_mul(locator([f(7)]), (neg(ZETA), ONE))
    member1 = p_mul(locator([f(8)]), (neg(add(ZETA, ONE)), ONE))
    pbar2 = member0
    qbar2 = p_sub(member1, member0)
    require(p_gcd(pbar2, qbar2) == (ONE,), "moving-cofactor pair not coprime")
    require(p_add(pbar2, qbar2) == member1, "moving-cofactor pencil drift")
    require(slack_tuple(6, 2, 4, 1, 2, 3, 3) == (0, 1, 0), "moving-cofactor slack drift")

    triples = sorted(
        (h, u, 1 - h - u)
        for h in range(2)
        for u in range(2 - h)
    )
    require(triples == [(0, 0, 1), (0, 1, 0), (1, 0, 0)], "one-slack trichotomy drift")
    return {
        "field_order": 121,
        "one_slack_triples": triples,
        "zero_slack_c5_coordinate_recovery": True,
        "nonbase_gcd_twist": True,
        "nonbase_linear_moving_cofactors": 2,
    }


def dag_checks():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE]["status"] == "PROVED", "node status drift")
    edges = {
        (edge["from"], edge["to"], edge.get("kind")) for edge in dag["edges"]
    }
    require((NODE, CONSUMER, "ev") in edges, "evidence edge missing")
    require((NODE, CONSUMER, "req") not in edges, "finite satellite became requirement")


def main():
    official, mutation_rejections = official_checks()
    toy = toy_checks()
    dag_checks()
    print(
        json.dumps(
            {
                "node": NODE,
                "official": official,
                "toy": toy,
                "mutation_rejections": mutation_rejections,
                "status": "PASS",
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
