#!/usr/bin/env python3
"""Exact WSL-safe complete-cell zero certificates for M720 h=7..20."""

from __future__ import annotations

import itertools
from math import comb

SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
COUNT_CEILING = 6_000_000


def is_prime(m: int) -> bool:
    if m < 2:
        return False
    for q in SMALL_PRIMES:
        if m % q == 0:
            return m == q
    d = m - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in SMALL_PRIMES:
        x = pow(a, d, m)
        if x == 1 or x == m - 1:
            continue
        for _ in range(r - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def next_prime_1mod(n: int, start: int) -> int:
    t = (start - 1) // n
    if t < 1:
        t = 1
    while True:
        p = 1 + n * t
        if p >= start and is_prime(p):
            return p
        t += 1


def mu_n_generator(p: int, n: int) -> int:
    assert (p - 1) % n == 0
    e = (p - 1) // n
    a = 2
    while True:
        z = pow(a, e, p)
        if pow(z, n // 2, p) != 1:
            return z
        a += 1


def sig_general(exps: tuple[int, ...], powers: list[int], p: int, h: int) -> tuple[tuple[int, ...], int]:
    coef = [1] + [0] * h
    for a in exps:
        r = powers[a]
        for j in range(h, 0, -1):
            coef[j] = (coef[j] - r * coef[j - 1]) % p
    e = tuple(((-coef[j]) % p if (j & 1) else coef[j]) for j in range(1, h))
    e_h = (-coef[h]) % p if (h & 1) else coef[h]
    return e, e_h


def is_coset(exps: tuple[int, ...], h: int, n: int) -> bool:
    if n % h:
        return False
    step = n // h
    r0 = exps[0] % step
    return sorted(exps) == sorted((r0 + j * step) % n for j in range(h))


def pack(exps: tuple[int, ...]) -> int:
    out = 0
    for a in exps:
        out = (out << 11) | a
    return out


def unpack(value: int, k: int) -> tuple[int, ...]:
    out = []
    for _ in range(k):
        out.append(value & 0x7FF)
        value >>= 11
    return tuple(reversed(out))


def mitm_complete(n: int, h: int, p: int) -> dict[str, int | bool]:
    z = mu_n_generator(p, n)
    powers = [pow(z, a, p) for a in range(n)]

    table: dict[tuple[int, ...], int | list[int]] = {}
    n_hash = 0
    for tri in itertools.combinations(range(1, n), h - 1):
        exps = (0,) + tri
        sig, _ = sig_general(exps, powers, p, h)
        packed = pack(tri)
        cur = table.get(sig)
        if cur is None:
            table[sig] = packed
        elif isinstance(cur, int):
            table[sig] = [cur, packed]
        else:
            cur.append(packed)
        n_hash += 1

    anchored_toral = 0
    anchored_nontoral = 0
    n_probe = 0
    for q_exps in itertools.combinations(range(1, n), h):
        sig, e_h = sig_general(q_exps, powers, p, h)
        n_probe += 1
        packed = table.get(sig)
        if packed is None:
            continue
        candidates = packed if isinstance(packed, list) else [packed]
        for cand in candidates:
            p_tail = unpack(cand, h - 1)
            p_exps = (0,) + p_tail
            p_sig, p_e_h = sig_general(p_exps, powers, p, h)
            if p_sig != sig:
                continue
            if set(p_exps) & set(q_exps):
                continue
            if p_e_h == e_h:
                continue
            if is_coset(p_exps, h, n) and is_coset(q_exps, h, n):
                anchored_toral += 1
            else:
                anchored_nontoral += 1

    return {
        "complete": True,
        "n_hash": n_hash,
        "n_probe": n_probe,
        "anchored_nontoral": anchored_nontoral,
        "anchored_toral": anchored_toral,
    }


def safe_complete_configs() -> list[tuple[int, int, int, int, int]]:
    configs = []
    for h in range(7, 21):
        for n in (16, 32, 64, 128, 256):
            if n < 2 * h:
                continue
            cost = comb(n - 1, h - 1) + comb(n, h)
            if cost <= COUNT_CEILING:
                for exp in (2, 3):
                    configs.append((n, h, exp, next_prime_1mod(n, n ** exp), cost))
    return configs


def main() -> None:
    expected = {
        (16, 7, 2, 257): (0, 0),
        (16, 7, 3, 4129): (0, 0),
        (32, 7, 2, 1153): (0, 0),
        (32, 7, 3, 32801): (0, 0),
        (16, 8, 2, 257): (0, 1),
        (16, 8, 3, 4129): (0, 1),
    }
    configs = safe_complete_configs()
    assert {(n, h, exp, p) for n, h, exp, p, _ in configs} == set(expected), configs
    for n, h, exp, p, cost in configs:
        got = mitm_complete(n, h, p)
        want_nontoral, want_toral = expected[(n, h, exp, p)]
        assert got["complete"] is True
        assert got["anchored_nontoral"] == want_nontoral, (n, h, exp, p, got)
        assert got["anchored_toral"] == want_toral, (n, h, exp, p, got)
        print(f"n={n} h={h} p={p} q_exp={exp} cost={cost} -> {got}")
    print("M720 WSL-safe complete zero subcertificates PASS")


if __name__ == "__main__":
    main()
