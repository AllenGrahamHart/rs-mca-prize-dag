#!/usr/bin/env python3
"""Verifier for pb_design_ceiling.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers, deterministic, no third-party imports, no file reads.
All pins inlined; provenance paths appear in comments only.

Fresh implementation of the shortened dual / condition rows (independent of
the pilots' core.py and of the banked node's verify.py).

  A  banked L1 replayed fresh: dim C_S = |S|-K and
     dim(C_S ^ C_T) = max(0,|S^T|-K)          [cited, not re-derived: the
     PROOF lives at background/nodes/xr_two_slope_cost_theorem/proof.md:7-23]
  B  Lemma 0: spread <=> pairwise-transverse condition spaces
  C  the rank law rank = min(Mh, 2r) on random spread prescribed-slope
     families, and the attainment pattern of EXPC_rank.json
     (M = 10 leaves a non-codeword solution, M = 11 does not)
  D  the six-row ceiling table, exact integers -- the PROVED
     floor((2r-1)/h) and, LABELLED NOT-PROVED, floor((2r-1)/(h-1)) and
     the banked per-datum floor((2r-1)/(2h-2)); plus 2*191 != 383
  E  the forcedness arithmetic: 8n^3, the <= 960 cap, the six bit margins
  F  THEOREM 3 (the refutation) rebuilt from scratch: the monomial pencil
     at n=20,q=41,K=4,h=3 -- all 77,520 supports scanned, orbit
     decomposition, spreadness, distinct slopes, rank 31 of 60 vs 2r = 32
"""
from __future__ import annotations

import sys
from itertools import combinations

sys.dont_write_bytecode = True

FAILURES = []


def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    if not ok:
        FAILURES.append(label)


class LCG:
    def __init__(self, seed):
        self.s = seed

    def randint(self, lo, hi):
        self.s = (6364136223846793005 * self.s + 1442695040888963407) % (1 << 64)
        return lo + (self.s >> 33) % (hi - lo + 1)

    def sample(self, n, k):
        out = []
        while len(out) < k:
            x = self.randint(0, n - 1)
            if x not in out:
                out.append(x)
        return sorted(out)


# --------------------------------------------------------- linear algebra --

def rank_mod(rows, q):
    rows = [list(r) for r in rows]
    if not rows:
        return 0
    ncol = len(rows[0])
    piv = 0
    for col in range(ncol):
        sel = None
        for i in range(piv, len(rows)):
            if rows[i][col] % q:
                sel = i
                break
        if sel is None:
            continue
        rows[piv], rows[sel] = rows[sel], rows[piv]
        inv = pow(rows[piv][col], q - 2, q)
        rows[piv] = [x * inv % q for x in rows[piv]]
        for i in range(len(rows)):
            if i != piv and rows[i][col] % q:
                f = rows[i][col]
                rows[i] = [(rows[i][c] - f * rows[piv][c]) % q
                           for c in range(ncol)]
        piv += 1
        if piv == len(rows):
            break
    return piv


# ------------------------------------------------------------ RS machinery --

def root_of_unity(q, n):
    def factors(m):
        out, d = set(), 2
        while d * d <= m:
            if m % d == 0:
                out.add(d)
                while m % d == 0:
                    m //= d
            d += 1
        if m > 1:
            out.add(m)
        return sorted(out)

    fs = factors(q - 1)
    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // f, q) != 1 for f in fs))
    w = pow(g, (q - 1) // n, q)
    assert pow(w, n, q) == 1 and all(pow(w, d, q) != 1
                                     for d in range(1, n) if n % d == 0)
    return w


def lam(S, D, q):
    out = []
    for i in S:
        p = 1
        for j in S:
            if j != i:
                p = p * (D[i] - D[j]) % q
        out.append(pow(p, q - 2, q))
    return out


def dual_basis(S, D, K, q):
    """basis of C_S = {c : supp inside S, c _|_ RS_K}; dim |S|-K."""
    n = len(D)
    L = lam(S, D, q)
    rows = []
    for t in range(len(S) - K):
        c = [0] * n
        for e, i in enumerate(S):
            c[i] = L[e] * pow(D[i], t, q) % q
        rows.append(c)
    return rows


def cond_rows(fam, D, K, q):
    """rows (c, z c) for c in C_S, over the family [(S, z), ...]."""
    n = len(D)
    rows = []
    for S, z in fam:
        for c in dual_basis(S, D, K, q):
            rows.append(list(c) + [z * x % q for x in c])
    return rows


# ------------------------------------------------------------ the rows -----
# pins: xr_lowcore_spread_heart row block (RowC n=1024 / prize n=2^41,
# rates 1/4, 1/8, 1/16; h = n/scale + 1 with deciding scales 256/256/512)
ROWS = [
    ("RowC 1/4", 1024, 256, 5),
    ("RowC 1/8", 1024, 128, 5),
    ("RowC 1/16", 1024, 64, 3),
    ("prize 1/4", 1 << 41, 1 << 39, (1 << 33) + 1),
    ("prize 1/8", 1 << 41, 1 << 38, (1 << 33) + 1),
    ("prize 1/16", 1 << 41, 1 << 37, (1 << 32) + 1),
]


def lg_floor_frac(num, den):
    """floor and 2 decimals of log2(num/den) via integer scaling."""
    # returns log2(num/den) to 2 dp, using integer arithmetic on 2^20 scale
    lo, hi = -400.0, 400.0
    for _ in range(80):
        mid = (lo + hi) / 2
        # compare num/den vs 2^mid  <=>  num * 2^-mid vs den
        e = int(mid * 4096)
        # 2^(e/4096) approximated by exact powers only at integer e/4096;
        # fall back to float only for the PRINTED value
        break
    import math
    return math.log2(num) - math.log2(den)


# --------------------------------------------------------------- checks ----

def stage_A_B():
    cfgs = [(16, 97, 4, 3), (20, 241, 4, 3), (16, 97, 8, 3), (24, 73, 6, 3)]
    bad_a, bad_b, tot = [], [], 0
    witness_gap = []
    rnd = LCG(20260803)
    for (n, q, K, h) in cfgs:
        A = K + h
        w = root_of_unity(q, n)
        D = [pow(w, i, q) for i in range(n)]
        assert len(set(D)) == n
        for _ in range(100):
            S = tuple(rnd.sample(n, A))
            T = tuple(rnd.sample(n, A))
            bs, bt = dual_basis(S, D, K, q), dual_basis(T, D, K, q)
            if len(bs) != A - K or rank_mod(bs, q) != A - K:
                bad_a.append((n, q, K, "dim C_S"))
            inter = len(bs) + len(bt) - rank_mod(bs + bt, q)
            want = max(0, len(set(S) & set(T)) - K)
            tot += 1
            if inter != want:
                bad_a.append((n, q, K, S, T, inter, want))
            # B: CORRECTED Lemma 0 -- transverse iff |S^T| <= K (NOT <= K-1);
            # spread => transverse, converse FAILS exactly at core = K.
            core = len(set(S) & set(T))
            if (inter == 0) != (core <= K):
                bad_b.append((n, q, K, S, T, core, inter))
            if core <= K - 1 and inter != 0:
                bad_b.append((n, q, K, "spread but not transverse"))
            if core == K:
                witness_gap.append((n, q, K, S, T))
    check("A: banked L1 replayed FRESH -- dim C_S = |S|-K and "
          "dim(C_S ^ C_T) = max(0,|S^T|-K) (the PROOF is banked at "
          "xr_two_slope_cost_theorem/proof.md:7-23; consumed, not "
          "re-derived)", not bad_a,
          f"{tot} pairs over 4 shapes (pilot EXPC_lemma.json: 1599/1599); "
          f"bad={bad_a[:2]}")
    check("B: Lemma 0 CORRECTED -- C_S ^ C_T = 0 iff |S^T| <= K (NOT iff "
          "|S^T| <= K-1). Spread IMPLIES pairwise transversality; the "
          "CONVERSE FAILS exactly at core = K, and such pairs are "
          "exhibited. The pilot's 'spread <=> pairwise-transverse' "
          "(pb_h4_hunt/REPORT.md:29) is one-directional as stated",
          not bad_b and len(witness_gap) > 0,
          f"{len(witness_gap)} core-exactly-K pairs that ARE transverse but "
          f"NOT spread, e.g. {witness_gap[:1]}; bad={bad_b[:2]}")


def stage_C():
    """rank = min(Mh, 2r) on spread prescribed-slope families; EXPC_rank."""
    n, q, K, h = 20, 241, 4, 3
    A, r = K + h, n - K
    w = root_of_unity(q, n)
    D = [pow(w, i, q) for i in range(n)]
    rnd = LCG(777)
    # a spread pool
    fam, masks = [], []
    for _ in range(200000):
        S = tuple(rnd.sample(n, A))
        m = 0
        for i in S:
            m |= 1 << i
        if all(bin(m & o).count("1") <= K - 1 for o in masks):
            fam.append(S)
            masks.append(m)
            if len(fam) == 24:
                break
    rows_out, bad = [], []
    for M in (1, 2, 3, 5, 8, 10, 11, 12, 16, 20, 24):
        if M > len(fam):
            continue
        sub = [(fam[a], (a * 7 + 3) % q) for a in range(M)]
        rr = cond_rows(sub, D, K, q)
        rk = rank_mod(rr, q)
        want = min(M * h, 2 * r)
        beyond = 2 * n - rk - 2 * K      # kernel dim beyond RS_K x RS_K
        rows_out.append((M, len(rr), rk, beyond))
        if rk != want:
            bad.append((M, rk, want))
    ceil_fixed = (2 * r - 1) // h
    ok10 = any(M == 10 and b > 0 for (M, _, _, b) in rows_out)
    ok11 = any(M == 11 and b == 0 for (M, _, _, b) in rows_out)
    check("C: rank = min(Mh, 2r) on spread prescribed-slope families "
          "(n=20,q=241,K=4,h=3; 2r=32) and the EXPC_rank.json attainment "
          "pattern: ceiling floor((2r-1)/h) = 10 leaves a NON-codeword "
          "solution, M = 11 does not",
          not bad and ceil_fixed == 10 and ok10 and ok11,
          f"(M, rows, rank, kernel beyond codewords) = {rows_out}")


def stage_D_E():
    import math
    bad, tbl = [], []
    for (name, n, K, h) in ROWS:
        r = n - K
        cf = (2 * r - 1) // h
        cfree = (2 * r - 1) // (h - 1)
        cdatum = (2 * r - 1) // (2 * h - 2)
        tbl.append((name, cf, cfree, cdatum))
    want_fixed = [307, 358, 639, 383, 447, 959]
    want_free = [383, 447, 959, 383, 447, 959]
    want_datum = [191, 223, 479, 191, 223, 479]
    got_fixed = [t[1] for t in tbl]
    got_free = [t[2] for t in tbl]
    got_datum = [t[3] for t in tbl]
    check("D1: PROVED ceiling floor((2(n-K)-1)/h) = 307/358/639 (RowC) and "
          "383/447/959 (prize), exact integers at the pinned rows "
          "(identical to the banked per-RAY column, "
          "xr_two_slope_cost_theorem/proof.md:133)",
          got_fixed == want_fixed, f"{got_fixed}")
    check("D2: NOT-PROVED free-slope form floor((2(n-K)-1)/(h-1)) = "
          "383/447/959 on BOTH triples (the pilot's headline number, "
          "recorded as a determinantal count -- see statement THEOREM 2)",
          got_free == want_free, f"{got_free}")
    check("D3: the banked per-DATUM free form floor((2(n-K)-1)/(2h-2)) = "
          "191/223/479 on both triples, and 2*191 = 382 != 383 -- the "
          "per-support and per-datum free numbers are NOT the same integer",
          got_datum == want_datum and 2 * 191 != 383, f"{got_datum}")
    # E: forcedness.  The CLAIM is checked with exact integers; the bit
    # figures are a printed float DIAGNOSTIC only.
    margins, cap, exact_ok = [], 0, True
    for (name, n, K, h) in ROWS:
        r = n - K
        cf = (2 * r - 1) // h
        cap = max(cap, cf)
        budget = 8 * n ** 3
        # exact: margin > 23 bits  <=>  budget > ceiling * 2^23
        if not budget > cf * (1 << 23):
            exact_ok = False
        margins.append((name, cf, round(math.log2(budget) - math.log2(cf), 2)))
    # exact: RowC 1/16 is the worst row and its margin is < 24 bits
    worst_row = ROWS[2]
    wr = worst_row[1] - worst_row[2]
    wc = (2 * wr - 1) // worst_row[3]
    tight = (8 * worst_row[1] ** 3) < wc * (1 << 24)
    check("E: forcedness -- at most floor((2r-1)/h) <= 960 members of any "
          "realised family carry independent condition blocks, against "
          "budgets 8n^3 = 2^33 (RowC) / 2^126 (prize). EXACT INTEGER "
          "checks: cap = 959; every row has 8n^3 > ceiling * 2^23 (so "
          "margin > 23 bits, i.e. >= 1 - 2^-23 FORCED); and RowC 1/16 has "
          "8n^3 < ceiling * 2^24 (so 23 bits is the honest headline, not "
          "24). Bit figures below are a printed float DIAGNOSTIC",
          cap == 959 and exact_ok and tight,
          f"cap={cap}; (row, ceiling, bits below 8n^3) = {margins}")


def stage_F():
    """THEOREM 3: the mu_20-orbit refutation, rebuilt from scratch."""
    n, q, K, h = 20, 41, 4, 3
    A, r = K + h, n - K
    w = root_of_unity(q, n)
    D = [pow(w, i, q) for i in range(n)]
    u = [pow(x, A, q) for x in D]
    v = [(-pow(x, A - 1, q)) % q for x in D]
    xp = [[pow(D[i], t, q) for t in range(h)] for i in range(n)]
    wit = {}
    total = 0
    for S in combinations(range(n), A):
        total += 1
        L = lam(S, D, q)
        su = [0] * h
        sv = [0] * h
        for e, i in enumerate(S):
            a, b = L[e] * u[i] % q, L[e] * v[i] % q
            for t in range(h):
                su[t] = (su[t] + a * xp[i][t]) % q
                sv[t] = (sv[t] + b * xp[i][t]) % q
        if all(x == 0 for x in sv):
            continue
        t0 = next(t for t in range(h) if sv[t])
        z = (-su[t0]) * pow(sv[t0], q - 2, q) % q
        if all((su[t] + z * sv[t]) % q == 0 for t in range(h)):
            m = 0
            for i in S:
                m |= 1 << i
            wit[m] = (z, S)
    # orbit decomposition under the index shift i -> i+1 (mod n)
    def shift(mask):
        return ((mask << 1) | (mask >> (n - 1))) & ((1 << n) - 1)
    closed = all(shift(m) in wit for m in wit)
    seen, orbits = set(), []
    for m in wit:
        if m in seen:
            continue
        orb, cur = [], m
        while cur not in seen and cur in wit:
            seen.add(cur)
            orb.append(cur)
            cur = shift(cur)
        orbits.append(orb)
    full = [o for o in orbits if len(o) == n]
    spread_orbits = []
    for o in full:
        mx = 0
        for i in range(len(o)):
            for j in range(i + 1, len(o)):
                t = bin(o[i] & o[j]).count("1")
                mx = max(mx, t)
        if mx <= K - 1:
            spread_orbits.append((o, mx))
    ok_shape = (total == 77520 and len(wit) == 40 and closed
                and len(full) == 2 and len(spread_orbits) == 1)
    orb, maxcore = spread_orbits[0] if spread_orbits else ([], -1)
    fam = [(wit[m][1], wit[m][0]) for m in orb]
    slopes = {z for (_, z) in fam}
    rr = cond_rows(fam, D, K, q)
    rk = rank_mod(rr, q)
    beyond = 2 * n - rk - 2 * K
    ceil_fixed, ceil_free = (2 * r - 1) // h, (2 * r - 1) // (h - 1)
    ok = (ok_shape and len(orb) == 20 and maxcore == K - 1
          and len(slopes) == 20 and len(rr) == 60 and rk == 31
          and 2 * r == 32 and beyond > 0
          and ceil_fixed == 10 and ceil_free == 15)
    check("F: THEOREM 3 -- the monomial pencil U=X^7, V=-X^6 on mu_20 over "
          "F_41: all 77,520 supports scanned, 40 witnesses in 2 full "
          "mu_20-orbits, ONE of them SPREAD (max core 3 = K-1, zero "
          "self-collision) with 20 DISTINCT slopes, condition rank 31 of "
          "60 rows against 2r = 32 (kernel strictly beyond RS_K x RS_K). "
          "M = 20 exceeds BOTH ceilings (10 prescribed, 15 free): the "
          "independence hypothesis is load-bearing and 'rank deficit "
          "forces self-collision' is FALSE", ok,
          f"scanned={total} witnesses={len(wit)} full_orbits={len(full)} "
          f"spread_full={len(spread_orbits)} maxcore={maxcore} "
          f"slopes={len(slopes)} rank={rk}/{len(rr)} 2r={2*r} "
          f"kernel_beyond={beyond} ceilings=({ceil_fixed},{ceil_free})")
    # deficit without excess: 40 witnesses vs mean supply C(n,A)/q^{h-1}
    mean_num, mean_den = 77520, q ** (h - 1)
    check("F2: DEFICIT WITHOUT EXCESS (recorded, not claimed) -- 40 "
          "witnesses against mean supply C(20,7)/q^{h-1} = 77520/1681 "
          "= 46.11...: symmetry buys rank deficit, not over-supply",
          len(wit) == 40 and mean_num * 100 // mean_den == 4611,
          f"witnesses=40 mean_supply={mean_num}/{mean_den}")


def main():
    stage_A_B()
    stage_C()
    stage_D_E()
    stage_F()
    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("PB_DESIGN_CEILING_ALL_PASS")


if __name__ == "__main__":
    main()
