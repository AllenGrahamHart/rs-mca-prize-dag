#!/usr/bin/env python3
"""F2 campaign: the EXTRAS-CONTRACTION FALSIFIER instrument, final form
(per EXTRAS_CONTRACTION_TARGET.md — measurement + falsifier evaluation).

Per row (q, n, J), mid-band b = n/2, exact integers throughout:
  N^(j)      : j-null census by DP over F_q^j (gate: totals = C(n,b)).
  struct^(j) : #{unions of pairwise-disjoint FULL cosets c*mu_M
               (M | n, M >= 3) of total size b that are ACTUALLY
               j-null} — computed by direct power-sum evaluation of
               each union (captures cross-part cancellation patterns;
               no divisibility shortcut).
  extras^(j) = N^(j) - struct^(j)  (gate: >= 0).
  L_x(j) = extras^(j) * q / extras^(j-1)   where defined.

PRE-REGISTERED FALSIFIER (from the target brief, immutable): a row and
level j where the extras contract by strictly less than q / 2^15 —
i.e. L_x(j) > 2^15 — sustained at >= 3 field scales at matched
(n, b, j). At toy q < 2^15 the operative proxy read (also
pre-registered): L_x > 32 sustained at 3 scales = WARNING;
L_x <= 32 everywhere = the lemma's premise supported in extras form.
"""
import json
from itertools import combinations
from math import comb

import modal

app = modal.App("rs-mca-f2-extras-falsifier")
image = modal.Image.debian_slim()

ROWS = [(17, 16, 5), (31, 30, 4), (61, 30, 3), (97, 32, 3),
        (193, 32, 2), (113, 16, 3), (257, 16, 3)]


@app.function(image=image, cpu=2, memory=3072, timeout=280)
def row(job):
    q, n, J = job
    def pf(x):
        out, d = [], 2
        while d * d <= x:
            while x % d == 0:
                out.append(d); x //= d
            d += 1
        if x > 1:
            out.append(x)
        return out
    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // r, q) != 1 for r in set(pf(q - 1))))
    h = pow(g, (q - 1) // n, q)
    D = sorted(pow(h, i, q) for i in range(n))
    b = n // 2

    # all full cosets c*mu_M, M | n, 3 <= M <= b, as frozensets
    all_cosets = []
    for M in (M for M in range(3, b + 1) if n % M == 0):
        hM = pow(h, n // M, q)
        base = [pow(hM, i, q) for i in range(M)]
        seen = set()
        for c0 in D:
            cs = frozenset(c0 * x % q for x in base)
            if cs not in seen:
                seen.add(cs)
                all_cosets.append(cs)

    # enumerate disjoint unions of total size b; test j-null directly
    unions = []
    def rec(idx, used, parts):
        if len(used) == b:
            unions.append(frozenset(used))
            return
        if len(used) > b or idx == len(all_cosets):
            return
        rec(idx + 1, used, parts)
        cs = all_cosets[idx]
        if not (cs & used) and len(used) + len(cs) <= b:
            rec(idx + 1, used | cs, parts + 1)
    rec(0, frozenset(), 0)
    unions = set(unions)
    struct = []
    for j in range(1, J + 1):
        sj = 0
        for U in unions:
            if all(sum(pow(x, i, q) for x in U) % q == 0
                   for i in range(1, j + 1)):
                sj += 1
        struct.append(sj)

    # exact census ladder by DP
    counts = [comb(n, b)]
    for j in range(1, J + 1):
        dp = {(0,) * j: [1] + [0] * b}
        for x in D:
            pw = [pow(x, e, q) for e in range(1, j + 1)]
            new = {}
            for st, vec in dp.items():
                t = new.setdefault(st, [0] * (b + 1))
                for w in range(b + 1):
                    t[w] += vec[w]
                st2 = tuple((st[e] + pw[e]) % q for e in range(j))
                t2 = new.setdefault(st2, [0] * (b + 1))
                for w in range(b):
                    if vec[w]:
                        t2[w + 1] += vec[w]
            dp = new
        assert sum(v[b] for v in dp.values()) == comb(n, b)
        counts.append(dp.get((0,) * j, [0] * (b + 1))[b])

    extras = [counts[0]] + [counts[j] - struct[j - 1]
                            for j in range(1, J + 1)]
    for e in extras:
        assert e >= 0, ("negative extras — struct definition broken", e)
    Lx = []
    for j in range(1, J + 1):
        Lx.append(round(extras[j] * q / extras[j - 1], 3)
                  if extras[j - 1] > 0 else None)
    return {"q": q, "n": n, "b": b, "N": counts[1:], "struct": struct,
            "extras": extras[1:], "L_x": Lx}


@app.local_entrypoint()
def main():
    res = list(row.map(ROWS, return_exceptions=True))
    fails = 0
    warn = 0
    print(f"{'row':>10} {'b':>3}  N / struct / extras per level -> L_x")
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:200])
            continue
        print(f" ({r['q']},{r['n']})".rjust(10) + f" {r['b']:>3}  "
              f"N={r['N']} struct={r['struct']} extras={r['extras']} "
              f"-> L_x={r['L_x']}")
        for L in r["L_x"]:
            if L is not None and L > 32:
                warn += 1
    if fails:
        raise SystemExit(f"F2_EXTRAS_FALSIFIER_FAIL ({fails})")
    print(f"\nL_x > 32 events: {warn} "
          f"(falsifier needs sustained >= 3 matched scales)")
    print("F2_EXTRAS_FALSIFIER_PASS")
