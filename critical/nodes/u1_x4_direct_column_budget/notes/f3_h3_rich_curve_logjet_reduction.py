#!/usr/bin/env python3
"""Replay the h=3 rich-curve logarithmic jet reduction."""

from __future__ import annotations

import random
from dataclasses import dataclass
from itertools import product


def trim(poly: list[int], p: int) -> list[int]:
    out = [x % p for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
    return trim(out, p)


def sub(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p
    return trim(out, p)


def scale(a: list[int], c: int, p: int) -> list[int]:
    return trim([(c * x) % p for x in a], p)


def mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out, p)


def derivative(a: list[int], p: int) -> list[int]:
    if len(a) <= 1:
        return [0]
    return trim([(i * a[i]) % p for i in range(1, len(a))], p)


def pow_poly(a: list[int], e: int, p: int) -> list[int]:
    out = [1]
    base = trim(a, p)
    while e:
        if e & 1:
            out = mul(out, base, p)
        base = mul(base, base, p)
        e //= 2
    return out


def monomial_x(a: int) -> list[int]:
    return [0] * a + [1]


def eval_poly(poly: list[int], x: int, p: int) -> int:
    acc = 0
    for coeff in reversed(poly):
        acc = (acc * x + coeff) % p
    return acc


def degree(poly: list[int]) -> int:
    trimmed = list(poly)
    while len(trimmed) > 1 and trimmed[-1] == 0:
        trimmed.pop()
    return len(trimmed) - 1


def product_polys(polys: list[list[int]], p: int) -> list[int]:
    out = [1]
    for poly in polys:
        out = mul(out, poly, p)
    return out


def random_quad(rng: random.Random, p: int) -> list[int]:
    poly = [rng.randrange(p) for _ in range(3)]
    if poly == [0, 0, 0]:
        poly[0] = 1
    return trim(poly, p)


def rational_derivative(num: list[int], den: list[int], p: int) -> tuple[list[int], list[int]]:
    top = sub(mul(derivative(num, p), den, p), mul(num, derivative(den, p), p), p)
    bottom = mul(den, den, p)
    return top, bottom


def eval_rational(num: list[int], den: list[int], x: int, p: int) -> int | None:
    den_x = eval_poly(den, x, p)
    if den_x == 0:
        return None
    return eval_poly(num, x, p) * pow(den_x, -1, p) % p


@dataclass(frozen=True)
class Maps:
    ps: tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]
    qs: tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]

    def p_list(self) -> list[list[int]]:
        return [list(poly) for poly in self.ps]

    def q_list(self) -> list[list[int]]:
        return [list(poly) for poly in self.qs]


def build_s(ps: list[list[int]], qs: list[list[int]], p: int) -> list[int]:
    factors = [monomial_x(1)]
    for poly_p, poly_q in zip(ps, qs):
        factors.append(poly_p)
        factors.append(poly_q)
    return product_polys(factors, p)


def build_m_poly(
    ps: list[list[int]],
    qs: list[list[int]],
    a: int,
    bs: tuple[int, int, int],
    h: int,
    p: int,
) -> list[int]:
    """Return M = S * d/dX log(X^a prod_i (P_i/Q_i)^(h b_i))."""

    terms: list[list[int]] = []
    if a:
        factors = []
        for poly_p, poly_q in zip(ps, qs):
            factors.append(poly_p)
            factors.append(poly_q)
        terms.append(scale(product_polys(factors, p), a, p))

    for i, b_i in enumerate(bs):
        if b_i == 0:
            continue
        factors = [monomial_x(1)]
        for index, (poly_p, poly_q) in enumerate(zip(ps, qs)):
            if index == i:
                continue
            factors.append(poly_p)
            factors.append(poly_q)
        outside = product_polys(factors, p)
        wronskian = sub(
            mul(derivative(ps[i], p), qs[i], p),
            mul(ps[i], derivative(qs[i], p), p),
            p,
        )
        terms.append(scale(mul(outside, wronskian, p), h * b_i, p))

    total = [0]
    for term in terms:
        total = add(total, term, p)
    return total


def reduced_w_polys(
    ps: list[list[int]],
    qs: list[list[int]],
    a: int,
    bs: tuple[int, int, int],
    h: int,
    max_j: int,
    p: int,
) -> tuple[list[int], list[list[int]]]:
    """Return S and W_j where S^j m^(j) = m W_j."""

    s_poly = build_s(ps, qs, p)
    m_poly = build_m_poly(ps, qs, a, bs, h, p)
    s_deriv = derivative(s_poly, p)
    ws = [[1]]
    for j in range(max_j):
        w_j = ws[-1]
        next_w = add(
            mul(s_poly, derivative(w_j, p), p),
            mul(sub(m_poly, scale(s_deriv, j, p), p), w_j, p),
            p,
        )
        ws.append(next_w)
    return s_poly, ws


def monomial_rational(
    ps: list[list[int]],
    qs: list[list[int]],
    a: int,
    bs: tuple[int, int, int],
    h: int,
    p: int,
) -> tuple[list[int], list[int]]:
    num = monomial_x(a)
    den = [1]
    for poly_p, poly_q, b_i in zip(ps, qs, bs):
        num = mul(num, pow_poly(poly_p, h * b_i, p), p)
        den = mul(den, pow_poly(poly_q, h * b_i, p), p)
    return num, den


def check_case(
    maps: Maps,
    p: int,
    h: int,
    a_values: list[int],
    b_values: list[tuple[int, int, int]],
    max_j: int,
) -> tuple[int, int]:
    ps = maps.p_list()
    qs = maps.q_list()
    checked_evals = 0
    max_reduced_degree = 0
    for a, bs in product(a_values, b_values):
        s_poly, ws = reduced_w_polys(ps, qs, a, bs, h, max_j, p)
        s_degree = degree(s_poly)
        num, den = monomial_rational(ps, qs, a, bs, h, p)
        rational_jets = [(num, den)]
        for _ in range(max_j):
            rational_jets.append(rational_derivative(*rational_jets[-1], p))

        for j, w_j in enumerate(ws):
            reduced = mul(monomial_x(a), w_j, p)
            max_reduced_degree = max(max_reduced_degree, degree(reduced))
            if degree(reduced) > a + j * (s_degree - 1):
                raise AssertionError(
                    ("degree bound", p, h, a, bs, j, degree(reduced), s_degree)
                )

            jet_num, jet_den = rational_jets[j]
            for x in range(p):
                s_x = eval_poly(s_poly, x, p)
                if s_x == 0:
                    continue
                jet_x = eval_rational(jet_num, jet_den, x, p)
                term_x = eval_rational(num, den, x, p)
                if jet_x is None or term_x is None:
                    continue
                lhs = pow(s_x, j, p) * jet_x % p
                rhs = term_x * eval_poly(w_j, x, p) % p
                if lhs != rhs:
                    raise AssertionError(
                        ("jet identity", p, h, a, bs, j, x, lhs, rhs)
                    )
                checked_evals += 1
    return checked_evals, max_reduced_degree


def random_maps(seed: int, p: int) -> Maps:
    rng = random.Random(seed)
    ps = tuple(tuple(random_quad(rng, p)) for _ in range(3))
    qs = tuple(tuple(random_quad(rng, p)) for _ in range(3))
    return Maps(ps=ps, qs=qs)


def main() -> None:
    controlled = Maps(
        ps=((0, 1), (0, 3), (0, 5)),
        qs=((1,), (1,), (1,)),
    )
    cases = [
        (101, 5, controlled),
        (193, 8, controlled),
        (257, 4, random_maps(20260708, 257)),
        (769, 6, random_maps(20260709, 769)),
    ]
    total_evals = 0
    max_reduced_degree = 0
    for index, (p, h, maps) in enumerate(cases):
        evals, deg_seen = check_case(
            maps=maps,
            p=p,
            h=h,
            a_values=[0, 1, 2, 5],
            b_values=[(0, 0, 0), (1, 0, 2), (2, 1, 1), (1, 2, 2)],
            max_j=4,
        )
        total_evals += evals
        max_reduced_degree = max(max_reduced_degree, deg_seen)
        print(f"case {index}: p={p} h={h} evaluations={evals}")

    print("log-jet identity evaluations checked:", total_evals)
    print("max reduced numerator degree observed:", max_reduced_degree)
    print("degree bound: deg(X^a W_j) <= a + j(deg S - 1) <= a + 12j")
    print("condition-count corollary: RC-RED(13)")
    print("H3_RICH_CURVE_LOGJET_REDUCTION_PASS")


if __name__ == "__main__":
    main()
