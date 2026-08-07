#!/usr/bin/env python3
"""Symbolic degree compiler for private-linear normal-form rank minors."""

from __future__ import annotations

from itertools import product


P = 101
ParamExp = tuple[int, int, int]
ParamPoly = dict[ParamExp, int]
YPoly = list[ParamPoly]


def clean(poly: ParamPoly) -> ParamPoly:
    return {monom: coeff % P for monom, coeff in poly.items() if coeff % P}


def const(c: int) -> ParamPoly:
    return clean({(0, 0, 0): c})


def var(index: int) -> ParamPoly:
    exp = [0, 0, 0]
    exp[index] = 1
    return {tuple(exp): 1}


def p_add(a: ParamPoly, b: ParamPoly) -> ParamPoly:
    out = dict(a)
    for monom, coeff in b.items():
        out[monom] = (out.get(monom, 0) + coeff) % P
    return clean(out)


def p_neg(a: ParamPoly) -> ParamPoly:
    return {monom: (-coeff) % P for monom, coeff in a.items()}


def p_mul(a: ParamPoly, b: ParamPoly) -> ParamPoly:
    out: ParamPoly = {}
    for (la, ea, ta), ca in a.items():
        for (lb, eb, tb), cb in b.items():
            monom = (la + lb, ea + eb, ta + tb)
            out[monom] = (out.get(monom, 0) + ca * cb) % P
    return clean(out)


def y_trim(poly: YPoly) -> YPoly:
    out = [clean(coeff) for coeff in poly]
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out


def y_mul(a: YPoly, b: YPoly) -> YPoly:
    out = [{} for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            if y:
                out[i + j] = p_add(out[i + j], p_mul(x, y))
    return y_trim(out)


def y_pow(poly: YPoly, exponent: int) -> YPoly:
    out = [const(1)]
    base = poly
    while exponent:
        if exponent & 1:
            out = y_mul(out, base)
        base = y_mul(base, base)
        exponent //= 2
    return out


def y_shift(poly: YPoly, shift: int) -> YPoly:
    return [{} for _ in range(shift)] + poly


def factor_y_minus_param(kind: str) -> YPoly:
    if kind == "zero":
        return [{}, const(1)]
    if kind == "one":
        return [const(-1), const(1)]
    if kind == "lambda":
        return [p_neg(var(0)), const(1)]
    if kind == "eta":
        return [p_neg(var(1)), const(1)]
    if kind == "theta":
        return [p_neg(var(2)), const(1)]
    raise ValueError(kind)


def column_poly(a: int, b1: int, b2: int, b3: int, h_order: int, b_count: int) -> YPoly:
    poly = y_shift([const(1)], a)
    factors = (
        ("zero", h_order * b1),
        ("one", h_order * b2),
        ("lambda", h_order * (b_count - 1 - b2)),
        ("eta", h_order * b3),
        ("theta", h_order * (b_count - 1 - b3)),
    )
    for kind, exponent in factors:
        poly = y_mul(poly, y_pow(factor_y_minus_param(kind), exponent))
    return poly


def param_degrees(poly: ParamPoly) -> tuple[int, int, int, int, int]:
    if not poly:
        return (0, 0, 0, 0, 0)
    max_lambda = max(exp[0] for exp in poly)
    max_eta = max(exp[1] for exp in poly)
    max_theta = max(exp[2] for exp in poly)
    max_eta_theta = max(exp[1] + exp[2] for exp in poly)
    max_total = max(sum(exp) for exp in poly)
    return max_lambda, max_eta, max_theta, max_eta_theta, max_total


def normal_form_matrix(a_count: int, b_count: int, h_order: int) -> list[list[ParamPoly]]:
    degree_cap = (a_count - 1) + 3 * h_order * (b_count - 1)
    columns = []
    for a in range(a_count):
        for b1, b2, b3 in product(range(b_count), repeat=3):
            columns.append(column_poly(a, b1, b2, b3, h_order, b_count))
    return [
        [column[row] if row < len(column) else {} for column in columns]
        for row in range(degree_cap + 1)
    ]


def det(poly_matrix: list[list[ParamPoly]]) -> ParamPoly:
    n = len(poly_matrix)
    if n == 0:
        return const(1)
    if n == 1:
        return poly_matrix[0][0]
    total: ParamPoly = {}
    for col in range(n):
        entry = poly_matrix[0][col]
        if not entry:
            continue
        minor = [
            [row[j] for j in range(n) if j != col]
            for row in poly_matrix[1:]
        ]
        term = p_mul(entry, det(minor))
        total = p_add(total, p_neg(term) if col % 2 else term)
    return total


def verify_entries(a_count: int, b_count: int, h_order: int) -> dict[str, int]:
    max_lam = max_eta_theta = max_total = 0
    columns = 0
    entries = 0
    for a in range(a_count):
        for b1, b2, b3 in product(range(b_count), repeat=3):
            column = column_poly(a, b1, b2, b3, h_order, b_count)
            columns += 1
            lam_bound = h_order * (b_count - 1 - b2)
            eta_bound = h_order * b3
            theta_bound = h_order * (b_count - 1 - b3)
            for entry in column:
                entries += 1
                d_lam, d_eta, d_theta, d_eta_theta, d_total = param_degrees(entry)
                if d_lam > lam_bound or d_eta > eta_bound or d_theta > theta_bound:
                    raise AssertionError((a, b1, b2, b3, param_degrees(entry)))
                if d_eta_theta > h_order * (b_count - 1):
                    raise AssertionError((a, b1, b2, b3, d_eta_theta))
                if d_total > 2 * h_order * (b_count - 1):
                    raise AssertionError((a, b1, b2, b3, d_total))
                max_lam = max(max_lam, d_lam)
                max_eta_theta = max(max_eta_theta, d_eta_theta)
                max_total = max(max_total, d_total)
    return {
        "columns": columns,
        "entries": entries,
        "max_lambda": max_lam,
        "max_eta_theta": max_eta_theta,
        "max_total": max_total,
    }


def verify_minors(a_count: int, b_count: int, h_order: int) -> list[tuple[int, int, int, int]]:
    mat = normal_form_matrix(a_count, b_count, h_order)
    checks = []
    samples = (
        (0, 1, 2),
        (0, 2, 4),
        (1, 3, 5),
    )
    for rows in samples:
        cols = rows
        sub = [[mat[row][col] for col in cols] for row in rows]
        minor = det(sub)
        r = len(rows)
        d_lam, _, _, d_eta_theta, d_total = param_degrees(minor)
        if d_lam > r * h_order * (b_count - 1):
            raise AssertionError((rows, d_lam))
        if d_eta_theta > r * h_order * (b_count - 1):
            raise AssertionError((rows, d_eta_theta))
        if d_total > 2 * r * h_order * (b_count - 1):
            raise AssertionError((rows, d_total))
        checks.append((r, d_lam, d_eta_theta, d_total))
    return checks


def main() -> None:
    print("h=3 private-linear normal-form minor-degree compiler")
    for a_count, b_count, h_order in ((2, 2, 2), (3, 3, 2), (2, 4, 3)):
        row = verify_entries(a_count, b_count, h_order)
        minor_checks = verify_minors(a_count, b_count, h_order)
        print(
            f"A={a_count} B={b_count} H={h_order} columns={row['columns']} "
            f"entries={row['entries']} max_lambda={row['max_lambda']} "
            f"max_eta_theta={row['max_eta_theta']} max_total={row['max_total']} "
            f"minor_checks={minor_checks}"
        )
    print("entry bounds: deg_lambda <= H(B-1), deg_eta+theta <= H(B-1)")
    print("r-minor total degree bound: <= 2 r H(B-1)")
    print("H3_PRIVATE_LINEAR_MINOR_DEGREE_COMPILER_PASS")


if __name__ == "__main__":
    main()
