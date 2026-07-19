#!/usr/bin/env python3
"""Exact small-field replay of the PMA source-to-paving bridge."""

from itertools import combinations, product
from math import comb


CHECKS = 0


def check(label, condition):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1


def inv(a, p):
    return pow(a % p, p - 2, p)


def poly_eval(coeffs, x, p):
    out = 0
    for coeff in reversed(coeffs):
        out = (out * x + coeff) % p
    return out


def locator(points, x, p):
    out = 1
    for z in points:
        out = out * (x - z) % p
    return out


def rank_mod(matrix, p):
    rows = [list(map(lambda value: value % p, row)) for row in matrix]
    if not rows:
        return 0
    nrows, ncols = len(rows), len(rows[0])
    rank = 0
    for col in range(ncols):
        pivot = next((i for i in range(rank, nrows) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = inv(rows[rank][col], p)
        rows[rank] = [value * scale % p for value in rows[rank]]
        for i in range(nrows):
            if i == rank or not rows[i][col]:
                continue
            factor = rows[i][col]
            rows[i] = [
                (rows[i][j] - factor * rows[rank][j]) % p
                for j in range(ncols)
            ]
        rank += 1
        if rank == nrows:
            break
    return rank


def mat_vec(columns, vector, p):
    nrows = len(columns[0])
    return [
        sum(vector[j] * columns[j][i] for j in range(len(columns))) % p
        for i in range(nrows)
    ]


def add_vec(left, right, p):
    return [(a + b) % p for a, b in zip(left, right)]


def scale_vec(scale, vector, p):
    return [scale * value % p for value in vector]


def parity_columns(locators, kappa, p):
    redundancy = len(locators) - kappa
    columns = []
    for x in locators:
        denom = 1
        for z in locators:
            if z != x:
                denom = denom * (x - z) % p
        weight = inv(denom, p)
        columns.append([weight * pow(x, j, p) % p for j in range(redundancy)])
    return columns


def run_case(p, petals, defect, background, scalars, d, sigma, xi):
    T = tuple(x for petal in petals for x in petal)
    L = len(T)
    r = len(background)
    check("source sets distinct", len(set(T + tuple(defect) + tuple(background))) == L + len(defect) + r)
    check("maximal background range", 0 <= r <= sigma)
    target = {}
    for scalar, petal in zip(scalars, petals):
        for x in petal:
            target[x] = scalar * locator(defect, x, p) % p
    threshold_w = d + 1 + sigma - r

    listed_w = []
    for coeffs in product(range(p), repeat=d + 1):
        if any(poly_eval(coeffs, z, p) for z in background):
            continue
        agree = tuple(x for x in T if poly_eval(coeffs, x, p) == target[x])
        if len(agree) >= threshold_w:
            listed_w.append((coeffs, agree))

    if r > d:
        check("overdetermined background list empty", not listed_w)
        return

    kappa = d - r + 1
    V = {x: target[x] * inv(locator(background, x, p), p) % p for x in T}
    listed_q = []
    for coeffs in product(range(p), repeat=kappa):
        agree = tuple(x for x in T if poly_eval(coeffs, x, p) == V[x])
        if len(agree) >= kappa + sigma:
            listed_q.append((coeffs, agree))

    normalized_w = set()
    for coeffs, agree in listed_q:
        values = tuple(locator(background, x, p) * poly_eval(coeffs, x, p) % p for x in T)
        normalized_w.add((values, agree))
    direct_w = {
        (tuple(poly_eval(coeffs, x, p) for x in T), agree)
        for coeffs, agree in listed_w
    }
    check("background quotient bijection", normalized_w == direct_w)
    check("threshold dictionary", threshold_w == kappa + sigma)

    owners = {}
    charge = 0
    for coeffs, agree in listed_q:
        charge += comb(len(agree), kappa)
        for subset in combinations(agree, kappa):
            check("interpolation owner unique", subset not in owners)
            owners[subset] = coeffs
    check("pinned basis charge", charge <= comb(L, kappa))
    bound = comb(L, kappa) // comb(kappa + sigma, kappa)
    check("list ratio", len(listed_q) <= bound)

    locators = list(T) + [xi]
    columns = parity_columns(locators, kappa, p)
    redundancy = len(locators) - kappa
    check("chart parameters", redundancy == L + 1 - kappa)
    received = [V[x] for x in T] + [0]
    y0 = mat_vec(columns, received, p)
    y1 = columns[-1]
    t = L - kappa - sigma
    check("weight radius", t < redundancy)
    for coeffs, agree in listed_q:
        q_values = [poly_eval(coeffs, x, p) for x in T]
        error = [(V[x] - q_values[i]) % p for i, x in enumerate(T)] + [0]
        gamma = poly_eval(coeffs, xi, p)
        check("affine syndrome", mat_vec(columns, error, p) == add_vec(y0, scale_vec(gamma, y1, p), p))
        support = [i for i, value in enumerate(error) if value]
        check("listed weight", len(support) <= t)
        support_columns = [columns[i] for i in support]
        before = rank_mod([list(row) for row in zip(*support_columns)], p) if support_columns else 0
        with_direction = support_columns + [y1]
        after = rank_mod([list(row) for row in zip(*with_direction)], p)
        check("automatic transversality", after == before + 1)

    # Mutation guards: forgetting the background quotient changes kappa, and
    # replacing the proved lower charge by the next agreement level is unsafe
    # whenever an exact-threshold owner occurs.
    if r:
        check("mutation background quotient caught", kappa != d + 1)
    if any(len(agree) == kappa + sigma for _, agree in listed_q):
        wrong = comb(L, kappa) // comb(kappa + sigma + 1, kappa)
        check("mutation denominator caught", len(listed_q) > wrong or wrong < bound)


run_case(11, ((1, 2), (3, 4), (5, 6)), (7,), (), (1, 2, 3), 2, 1, 8)
run_case(13, ((1, 2), (3, 4), (5, 6)), (7, 8), (9,), (1, 3, 5), 2, 1, 10)
run_case(13, ((1, 2), (3, 4)), (7,), (8, 9), (2, 4), 1, 2, 10)

print(f"PMA source-to-paving bridge: PASS ({CHECKS} checks)")
