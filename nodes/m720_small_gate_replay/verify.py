#!/usr/bin/env python3
"""Light local replay of the n=16 M720 ground-truth gate rows."""

from __future__ import annotations

import itertools


def mu_n_generator(p: int, n: int) -> int:
    assert (p - 1) % n == 0
    e = (p - 1) // n
    a = 2
    while True:
        z = pow(a, e, p)
        if pow(z, n // 2, p) != 1:
            return z
        a += 1


def sig_general(exps: tuple[int, ...], pw: list[int], p: int, h: int) -> tuple[tuple[int, ...], int]:
    coef = [1] + [0] * h
    for a in exps:
        r = pw[a]
        for j in range(h, 0, -1):
            coef[j] = (coef[j] - r * coef[j - 1]) % p
    e = tuple(((-coef[j]) % p if (j & 1) else coef[j]) for j in range(1, h))
    e_h = (-coef[h]) % p if (h & 1) else coef[h]
    return e, e_h


def is_coset(A: tuple[int, ...], h: int, n: int) -> bool:
    if n % h:
        return False
    step = n // h
    r0 = A[0] % step
    return sorted(A) == sorted((r0 + j * step) % n for j in range(h))


def full_census(n: int, h: int, p: int) -> dict[str, int]:
    z = mu_n_generator(p, n)
    pw = [pow(z, a, p) for a in range(n)]
    buckets: dict[tuple[int, ...], list[tuple[tuple[int, ...], int]]] = {}
    for A in itertools.combinations(range(n), h):
        sig, eh = sig_general(A, pw, p, h)
        buckets.setdefault(sig, []).append((A, eh))
    unordered = toral = nontoral = 0
    anchored_cores = set()
    for lst in buckets.values():
        if len(lst) < 2:
            continue
        for i, (Ai, ea) in enumerate(lst):
            sAi = set(Ai)
            for Bj, eb in lst[i + 1:]:
                if sAi & set(Bj):
                    continue
                if ea == eb:
                    continue
                unordered += 1
                if is_coset(Ai, h, n) and is_coset(Bj, h, n):
                    toral += 1
                else:
                    nontoral += 1
                if 0 in Ai:
                    anchored_cores.add(Ai)
                if 0 in Bj:
                    anchored_cores.add(Bj)
    return {
        "unordered_trades": unordered,
        "toral": toral,
        "nontoral": nontoral,
        "anchored_cores": len(anchored_cores),
    }


def main() -> None:
    rows = [
        (16, 3, 17, {"unordered_trades": 352}),
        (16, 3, 97, {"unordered_trades": 16}),
        (16, 4, 17, {"nontoral": 120, "toral": 6, "unordered_trades": 126}),
    ]
    for n, h, p, expected in rows:
        got = full_census(n, h, p)
        for key, value in expected.items():
            assert got[key] == value, (n, h, p, key, got, expected)
        print(f"full_census({n},{h},{p}) = {got}")
    print("M720 n=16 small gate replay PASS")


if __name__ == "__main__":
    main()
