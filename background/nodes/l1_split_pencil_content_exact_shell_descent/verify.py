#!/usr/bin/env python3
"""Exhaustive F_7 replay of split-pencil coefficient-content descent."""

from __future__ import annotations

from itertools import combinations, product


def trim(f: tuple[int, ...], p: int) -> tuple[int, ...]:
    out = tuple(x % p for x in f)
    while len(out) > 1 and out[-1] == 0:
        out = out[:-1]
    return out or (0,)


def add(f: tuple[int, ...], g: tuple[int, ...], p: int) -> tuple[int, ...]:
    n = max(len(f), len(g))
    return trim(
        tuple((f[i] if i < len(f) else 0) + (g[i] if i < len(g) else 0) for i in range(n)),
        p,
    )


def neg(f: tuple[int, ...], p: int) -> tuple[int, ...]:
    return trim(tuple(-x for x in f), p)


def sub(f: tuple[int, ...], g: tuple[int, ...], p: int) -> tuple[int, ...]:
    return add(f, neg(g, p), p)


def mul(f: tuple[int, ...], g: tuple[int, ...], p: int) -> tuple[int, ...]:
    out = [0] * (len(f) + len(g) - 1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(tuple(out), p)


def divmod_poly(
    f: tuple[int, ...], g: tuple[int, ...], p: int
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    f = trim(f, p)
    g = trim(g, p)
    assert g != (0,)
    if len(f) < len(g):
        return (0,), f
    q = [0] * (len(f) - len(g) + 1)
    r = list(f)
    inv = pow(g[-1], -1, p)
    while len(r) >= len(g) and any(r):
        shift = len(r) - len(g)
        coeff = r[-1] * inv % p
        q[shift] = coeff
        for j, value in enumerate(g):
            r[shift + j] = (r[shift + j] - coeff * value) % p
        while len(r) > 1 and r[-1] == 0:
            r.pop()
    return trim(tuple(q), p), trim(tuple(r), p)


def monic(f: tuple[int, ...], p: int) -> tuple[int, ...]:
    f = trim(f, p)
    if f == (0,):
        return f
    inv = pow(f[-1], -1, p)
    return trim(tuple(inv * x for x in f), p)


def gcd_poly(f: tuple[int, ...], g: tuple[int, ...], p: int) -> tuple[int, ...]:
    f = trim(f, p)
    g = trim(g, p)
    while g != (0,):
        _, r = divmod_poly(f, g, p)
        f, g = g, r
    return monic(f, p)


def evaluate(f: tuple[int, ...], x: int, p: int) -> int:
    value = 0
    for coeff in reversed(f):
        value = (value * x + coeff) % p
    return value


def locator(points: tuple[int, ...], p: int) -> tuple[int, ...]:
    out = (1,)
    for x in points:
        out = mul(out, ((-x) % p, 1), p)
    return out


def interpolate(xs: tuple[int, ...], ys: tuple[int, ...], p: int) -> tuple[int, ...]:
    out = (0,)
    for i, x in enumerate(xs):
        basis = (1,)
        denom = 1
        for j, y in enumerate(xs):
            if i == j:
                continue
            basis = mul(basis, ((-y) % p, 1), p)
            denom = denom * (x - y) % p
        scale = ys[i] * pow(denom, -1, p) % p
        out = add(out, tuple(scale * z for z in basis), p)
    return trim(out, p)


def roots_on_h(f: tuple[int, ...], h: tuple[int, ...], p: int) -> tuple[int, ...]:
    return tuple(x for x in h if evaluate(f, x, p) == 0)


def main() -> None:
    p = 7
    h = tuple(range(p))
    n, k, m = len(h), 3, 3
    # c=0 and c=X(X-1) each agree four times; generic interpolants supply
    # exact-three members as well.
    u_values = (0, 0, 0, 0, 5, 6, 1)
    u_hat = interpolate(h, u_values, p)
    omega = locator(h, p)
    x_poly = (0, 1)
    histogram: dict[int, int] = {}
    codewords = 0

    for coeffs in product(range(p), repeat=k):
        c = trim(tuple(coeffs), p)
        agreements = tuple(x for x in h if evaluate(c, x, p) == u_values[x])
        if len(agreements) < m:
            continue
        codewords += 1
        for support in combinations(agreements, m):
            support_set = set(support)
            w = locator(tuple(x for x in h if x not in support_set), p)
            n_poly = mul(w, c, p)
            numerator = sub(n_poly, mul(w, u_hat, p), p)
            b, remainder = divmod_poly(numerator, omega, p)
            assert remainder == (0,)
            a = w
            content = gcd_poly(a, b, p)
            r = len(content) - 1
            assert r == len(agreements) - m
            assert set(roots_on_h(content, h, p)) == set(agreements) - support_set

            a0, rem_a = divmod_poly(a, content, p)
            b0, rem_b = divmod_poly(b, content, p)
            w0, rem_w = divmod_poly(w, content, p)
            n0, rem_n = divmod_poly(n_poly, content, p)
            assert rem_a == rem_b == rem_w == rem_n == (0,)
            assert gcd_poly(a0, b0, p) == (1,)
            assert n0 == mul(w0, c, p)
            assert set(roots_on_h(w0, h, p)) == set(h) - set(agreements)
            assert all(
                evaluate(n0, y, p) == evaluate(w0, y, p) * u_values[y] % p
                for y in h
            )

            # Polynomial-unimodular basis changes preserve the coefficient
            # ideal: (A,B)->(A,B-XA) and (A-XB,B).
            b_left = sub(b, mul(x_poly, a, p), p)
            a_right = sub(a, mul(x_poly, b, p), p)
            assert gcd_poly(a, b_left, p) == content
            assert gcd_poly(a_right, b, p) == content
            histogram[r] = histogram.get(r, 0) + 1

    assert codewords > 0
    assert histogram.get(0, 0) > 0
    assert histogram.get(1, 0) > 0
    print(
        "L1_SPLIT_PENCIL_CONTENT_EXACT_SHELL_DESCENT_PASS "
        f"codewords={codewords} members={sum(histogram.values())} histogram={histogram}"
    )


if __name__ == "__main__":
    main()
