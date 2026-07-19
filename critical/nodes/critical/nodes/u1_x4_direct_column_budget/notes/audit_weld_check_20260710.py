#!/usr/bin/env python3
"""Independent recount of the f3_shiftpair_weld gate rows.

Counts unordered pairs of DISJOINT h-subsets of mu_n <= F_p^* with equal
e_1..e_{h-1}, plus the toral (mu_h-coset pair) split, from scratch.
Pinned expectations (F3_IDENTIFICATION.md):
  (16,3,17): unordered 352 (ordered 704)
  (16,3,97): unordered 16
  (16,4,17): unordered 126 = 120 nontoral + 6 toral
  (16,4,97): unordered 6
  (32,4,97): unordered 396
"""
import itertools
from collections import defaultdict


def mu_gen(p, n):
    e = (p - 1) // n
    a = 2
    while True:
        z = pow(a, e, p)
        if pow(z, n, p) == 1 and pow(z, n // 2, p) != 1:
            return z
        a += 1


def sig(subset_roots, p, h):
    # elementary symmetric e_1..e_{h-1} mod p
    coeffs = [1] + [0] * h
    for r in subset_roots:
        for j in range(h, 0, -1):
            coeffs[j] = (coeffs[j] - r * coeffs[j - 1]) % p
    return tuple(((-coeffs[j]) % p if j % 2 == 1 else coeffs[j]) for j in range(1, h))


def is_coset(exps, h, n):
    if n % h:
        return False
    step = n // h
    return any(sorted(exps) == sorted((r + j * step) % n for j in range(h))
               for r in range(step))


def census(n, h, p):
    assert (p - 1) % n == 0
    z = mu_gen(p, n)
    pw = [pow(z, a, p) for a in range(n)]
    assert len(set(pw)) == n
    buckets = defaultdict(list)
    for exps in itertools.combinations(range(n), h):
        buckets[sig([pw[a] for a in exps], p, h)].append(exps)
    unordered = toral = 0
    for _, members in buckets.items():
        for A, B in itertools.combinations(members, 2):
            if set(A) & set(B):
                continue
            unordered += 1
            if is_coset(A, h, n) and is_coset(B, h, n):
                toral += 1
    return unordered, toral


for (n, h, p, exp_u, exp_t) in [(16, 3, 17, 352, None), (16, 3, 97, 16, None),
                                (16, 4, 17, 126, 6), (16, 4, 97, 6, None),
                                (32, 4, 97, 396, None)]:
    u, t = census(n, h, p)
    ok = (u == exp_u) and (exp_t is None or t == exp_t)
    print(f"(n={n},h={h},p={p}): unordered={u} toral={t} expected_u={exp_u} "
          f"expected_t={exp_t} -> {'MATCH' if ok else 'MISMATCH'}")
