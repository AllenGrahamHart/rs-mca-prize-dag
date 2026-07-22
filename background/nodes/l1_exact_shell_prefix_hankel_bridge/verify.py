#!/usr/bin/env python3
"""Finite-field replay of the exact-shell prefix/Hankel bridge."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_exact_shell_prefix_hankel_bridge"


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * max(len(a), len(b))
    for i in range(len(out)):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
    return trim(out)


def neg(a: list[int], p: int) -> list[int]:
    return [(-x) % p for x in a]


def mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out)


def scale(a: list[int], c: int, p: int) -> list[int]:
    return trim([(c * x) % p for x in a])


def evaluate(a: list[int], x: int, p: int) -> int:
    out = 0
    for c in reversed(a):
        out = (out * x + c) % p
    return out


def locator(points: tuple[int, ...] | list[int], p: int) -> list[int]:
    out = [1]
    for x in points:
        out = mul(out, [(-x) % p, 1], p)
    return out


def interpolate(xs: tuple[int, ...] | list[int], ys: list[int], p: int) -> list[int]:
    out = [0]
    for i, x in enumerate(xs):
        basis = [1]
        den = 1
        for j, y in enumerate(xs):
            if i == j:
                continue
            basis = mul(basis, [(-y) % p, 1], p)
            den = den * (x - y) % p
        out = add(out, scale(basis, ys[i] * pow(den, -1, p), p), p)
    return trim(out)


def divide_exact(num: list[int], den: list[int], p: int) -> list[int]:
    rem = num[:]
    out = [0] * max(1, len(num) - len(den) + 1)
    inv_lead = pow(den[-1], -1, p)
    while len(rem) >= len(den) and rem != [0]:
        shift = len(rem) - len(den)
        c = rem[-1] * inv_lead % p
        out[shift] = c
        for i, value in enumerate(den):
            rem[i + shift] = (rem[i + shift] - c * value) % p
        trim(rem)
    assert rem == [0]
    return trim(out)


def coeff(poly: list[int], i: int) -> int:
    return poly[i] if i < len(poly) else 0


def agreement(poly: list[int], U: dict[int, int], H: tuple[int, ...], p: int) -> tuple[int, ...]:
    return tuple(x for x in H if evaluate(poly, x, p) == U[x])


def shell_replay() -> tuple[int, int]:
    p = 7
    H = tuple(range(6))
    k = 2
    words = (
        {x: 0 for x in H},
        {x: x * x % p for x in H},
        dict(zip(H, (0, 1, 4, 2, 3, 6))),
    )
    shell_checks = 0
    listed_total = 0
    for U in words:
        polys = [trim(list(cs)) for cs in itertools.product(range(p), repeat=k)]
        exact = {}
        for P in polys:
            A = agreement(P, U, H, p)
            exact.setdefault(len(A), []).append((tuple(P), A))
        for s in (3, 4):
            shell_polys = set()
            raw_by_poly: dict[tuple[int, ...], int] = {}
            for a in range(s, len(H) + 1):
                exact_supports = []
                for A in itertools.combinations(H, a):
                    I = interpolate(A, [U[x] for x in A], p)
                    if len(I) <= k:
                        raw_by_poly[tuple(I)] = raw_by_poly.get(tuple(I), 0) + 1
                        if agreement(I, U, H, p) == A:
                            exact_supports.append(A)
                            shell_polys.add(tuple(I))
                expected = {P for P, A in exact.get(a, []) if len(A) == a}
                found = {
                    tuple(interpolate(A, [U[x] for x in A], p))
                    for A in exact_supports
                }
                assert found == expected
                assert len(found) == len(exact_supports)
                shell_checks += len(exact_supports) + 1
            expected_list = {
                P for a, rows in exact.items() if a >= s for P, _ in rows
            }
            assert shell_polys == expected_list
            for P, count in raw_by_poly.items():
                agr = len(agreement(list(P), U, H, p))
                assert count == sum(math.comb(agr, a) for a in range(s, agr + 1))
            listed_total += len(expected_list)
    return shell_checks, listed_total


def source_bridge_replay() -> tuple[int, int, int]:
    p = 11
    H = tuple(range(8))
    k = 3
    C = (0, 1)
    outside = tuple(x for x in H if x not in C)
    petals = ((2, 3), (4, 5), (6, 7))
    alpha = {x: i + 1 for i, petal in enumerate(petals) for x in petal}
    Q = [2, 3]
    LC = locator(C, p)
    U = {x: evaluate(Q, x, p) for x in C}
    for x in outside:
        U[x] = (evaluate(Q, x, p) + alpha[x] * evaluate(LC, x, p)) % p

    listed = 0
    actual_checks = 0
    s = 4
    for cs in itertools.product(range(p), repeat=k):
        P = list(cs)
        A = agreement(P, U, H, p)
        if len(A) < s:
            continue
        listed += 1
        dset = tuple(x for x in C if x not in A)
        X = tuple(x for x in A if x not in C)
        d = len(dset)
        w = len(A) - k
        assert len(X) == d + w + 1
        F = locator(dset, p)
        retained = tuple(x for x in C if x not in dset)
        Lret = locator(retained, p)
        J = divide_exact(add(P, neg(Q, p), p), Lret, p)
        Jx = interpolate(X, [alpha[x] * evaluate(F, x, p) % p for x in X], p)
        assert J == Jx
        assert all(coeff(J, i) == 0 for i in range(d + 1, d + w + 1))
        assert all(evaluate(J, z, p) != 0 for z in dset)
        assert all(
            evaluate(J, y, p) != alpha[y] * evaluate(F, y, p) % p
            for y in outside if y not in X
        )
        actual_checks += 1

    chart_checks = 0
    nonzero_prefix = 0
    for d in range(len(C) + 1):
        for dset in itertools.combinations(C, d):
            F = locator(dset, p)
            retained = tuple(x for x in C if x not in dset)
            Lret = locator(retained, p)
            for w in range(1, len(H) - k + 1):
                xsize = d + w + 1
                if xsize > len(outside):
                    continue
                for X in itertools.combinations(outside, xsize):
                    J = interpolate(X, [alpha[x] * evaluate(F, x, p) % p for x in X], p)
                    I = add(Q, mul(Lret, J, p), p)
                    A = tuple(sorted(retained + X))
                    assert all(evaluate(I, x, p) == U[x] for x in A)
                    local = [coeff(J, d + 1 + r) for r in range(w)]
                    global_prefix = [coeff(I, k + r) for r in range(w)]
                    predicted = []
                    for r in range(w):
                        value = 0
                        for uidx in range(r, w):
                            li = k + r - (d + 1 + uidx)
                            if 0 <= li < len(Lret):
                                value += coeff(Lret, li) * local[uidx]
                        predicted.append(value % p)
                    assert predicted == global_prefix
                    assert all(x == 0 for x in local) == all(x == 0 for x in global_prefix)
                    if any(global_prefix):
                        nonzero_prefix += 1
                    chart_checks += 1
    assert listed >= 3
    assert nonzero_prefix > 0
    return listed, actual_checks, chart_checks


def dag_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in ("l1_core_defect_reduction", "pma_saturated_mixed_support_kernel"):
        assert (parent, NODE, "req") in edges
    for consumer in ("l1_mixed_petal_amplification", "imgfib"):
        assert (NODE, consumer, "ev") in edges


def main() -> None:
    shell_checks, listed_total = shell_replay()
    listed, actual, chart_checks = source_bridge_replay()
    dag_check()
    print(
        "L1_EXACT_SHELL_PREFIX_HANKEL_BRIDGE_PASS "
        f"shell_checks={shell_checks} listed_total={listed_total} "
        f"source_listed={listed} actual={actual} chart_checks={chart_checks}"
    )


if __name__ == "__main__":
    main()
