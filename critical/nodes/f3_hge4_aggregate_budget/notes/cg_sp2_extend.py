#!/usr/bin/env python3
"""cg_sp2_extend: SHALLOW-reading (SP-CENSUS split-pair, t=3 contact) census
extension for f3_hge4_aggregate_budget.

Pipeline: cg_trades (C, tdepth=3) dumps every anchored split pair; this
script applies an INDEPENDENT implementation of the X-9 charged classifier
(cyclic/dihedral fiber-union partitions, m in [t+1, h_max]) and reports
A_h^nt per cell + aggregates vs 14n^3.

CROSS-CHECK: the F1153/mu32 cell must reproduce the banked certificate
exactly: totals {4:7, 6:42, 7:224, 8:1225}, charged {4:7, 6:6, 8:249},
nontoral {6:36, 7:224, 8:976}.

Extension grid (all in-range q > n^2):
  n=32, h=4..8: p = 1153 (anchor), 1217, 1249, 1409, 2081+4289 (the rows
       SP-CENSUS-2 explicitly SKIPPED after its first falsifier), 32801 (far).
  n=64, h=4..5: p = 4289, 4481, 4673, 4801 (state cap blocks h >= 6).
  n=16, h=4..8: p = 257, 641, 1153 (continuity; certificate says 0).
"""
from __future__ import annotations

import json
import math
import subprocess
from collections import Counter, defaultdict

SCRATCH = ("/tmp/claude-1000/-home-u2470931-smooth-read-solomin/"
           "d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad")
T = 3


def h_max(n: int) -> int:
    return min(int(math.log2(n)) ** 2, n // 2)


def quotient_classes(n, m):
    g = math.gcd(n, m)
    if g <= 1:
        return []
    step = n // g
    return [frozenset((r + j * step) % n for j in range(g))
            for r in range(step)]


def dihedral_classes(n, m, offset):
    g = math.gcd(n, m)
    if g <= 1:
        return []
    step = n // g
    out, seen = [], set()
    for r in range(step):
        if r in seen:
            continue
        residues = {r % step, (offset - r) % step}
        seen.update(residues)
        cls = set()
        for a in residues:
            for j in range(g):
                cls.add((a + j * step) % n)
        out.append(frozenset(cls))
    return out


def charged_partitions(n, t):
    out = []
    for m in range(t + 1, h_max(n) + 1):
        q = quotient_classes(n, m)
        if q:
            out.append((f"cyclic:m={m}", q))
        step = n // math.gcd(n, m)
        for offset in range(step):
            d = dihedral_classes(n, m, offset)
            if d:
                out.append((f"dihedral:m={m}:offset={offset}", d))
    return out


def is_union(S, classes):
    for cls in classes:
        hit = S & cls
        if hit and hit != cls:
            return False
    return True


def charged_reason(Q, P, partitions):
    for reason, classes in partitions:
        if is_union(Q, classes) and is_union(P, classes):
            return reason
    return None


def run_shallow(n, p, h):
    """Run C in shallow mode over full window, return list of (P,Q)."""
    from math import comb
    # shard plan (probe side by min exponent), state cap 10^7
    hashed = comb(n - 1, h - 1)
    budget = 10**7 - hashed
    assert budget > 0
    shards_list = []
    lo = 1
    while lo <= n - h:
        acc, hi = 0, lo
        while hi <= n - h:
            nxt = comb(n - 1 - hi, h - 1)
            if acc + nxt > budget and hi > lo:
                break
            acc += nxt
            hi += 1
        shards_list.append((lo, hi - 1))
        lo = hi
    pairs = []
    for lo, hi in shards_list:
        r = subprocess.run([f"{SCRATCH}/cg_trades", str(n), str(p), str(h),
                            str(lo), str(hi), "3000000", str(T)],
                           capture_output=True, text=True, check=True)
        assert "dumpcap=ok" in r.stderr, r.stderr
        for ln in r.stdout.splitlines():
            if ln.startswith("T "):
                a, b = ln[2:].split()
                pairs.append((tuple(map(int, a.split(","))),
                              tuple(map(int, b.split(",")))))
    return pairs


def main():
    grid = []
    for p in (257, 641, 1153):
        grid += [(16, p, h) for h in range(T + 1, 9)]
    for p in (1153, 1217, 1249, 1409, 2081, 4289, 32801):
        grid += [(32, p, h) for h in range(T + 1, 9)]
    for p in (4289, 4481, 4673, 4801):
        grid += [(64, p, h) for h in (4, 5)]

    partitions_cache = {}
    rows = []
    for n, p, h in grid:
        if n not in partitions_cache:
            partitions_cache[n] = charged_partitions(n, T)
        partitions = partitions_cache[n]
        pairs = run_shallow(n, p, h)
        charged = Counter()
        nontoral = []
        for Pex, Qex in pairs:
            reason = charged_reason(frozenset(Qex), frozenset(Pex), partitions)
            if reason:
                charged[reason] += 1
            else:
                nontoral.append((Pex, Qex))
        rows.append({"n": n, "p": p, "h": h, "total": len(pairs),
                     "charged": sum(charged.values()),
                     "charged_reasons": dict(charged),
                     "A_h_nt": len(nontoral),
                     "nontoral_pairs": [[list(a), list(b)]
                                        for a, b in nontoral[:1500]]})
        print(f"n={n} p={p} h={h}: total={len(pairs)} "
              f"charged={sum(charged.values())} A_h_nt={len(nontoral)}",
              flush=True)

    with open(f"{SCRATCH}/cg_sp2_extend.json", "w") as f:
        json.dump(rows, f)

    # anchor cross-check vs banked certificate
    want_tot = {4: 7, 5: 0, 6: 42, 7: 224, 8: 1225}
    want_nt = {4: 0, 5: 0, 6: 36, 7: 224, 8: 976}
    ok = True
    for r in rows:
        if r["n"] == 32 and r["p"] == 1153:
            if r["total"] != want_tot[r["h"]] or r["A_h_nt"] != want_nt[r["h"]]:
                ok = False
                print(f"ANCHOR MISMATCH at h={r['h']}: {r['total']}/{r['A_h_nt']}")
    print("ANCHOR F1153/mu32 vs banked certificate:", "PASS" if ok else "FAIL")

    # aggregates vs 14 n^3 (shallow reading; scanned band only)
    agg = defaultdict(int)
    for r in rows:
        agg[(r["n"], r["p"])] += r["A_h_nt"]
    print("\n=== SHALLOW-reading aggregates (scanned band) vs 14n^3 ===")
    for (n, p) in sorted(agg):
        b = 14 * n**3
        print(f"n={n} p={p}: Sigma A_h_nt = {agg[(n,p)]} vs 14n^3 = {b} "
              f"({100.0*agg[(n,p)]/b:.4f}%) "
              f"{'EXCESS' if agg[(n,p)] > b else ''}")


if __name__ == "__main__":
    main()
