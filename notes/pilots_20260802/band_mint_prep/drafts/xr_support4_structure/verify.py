#!/usr/bin/env python3
r"""Verifier for xr_support4_structure.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers, deterministic, no third-party imports, no file reads.

Fresh implementation (independent of s4lib/advlib; pins cross-checked at
draft time against notes/pilots_20260802/support4_relation/
{stage1_structure,stage3_construct,stage5_escape,stage6_repricing,
stage8_floor}.json):

  A  U-mechanism build (3,5,1,4): gates (pairwise k+d, triples EXACTLY
     k-1), dim Rel = 1, rank = Vh - 1 = 19
  B  S4-1 localisation (pointwise 0-or->=3), S4-3 rank-2 rigidity
     (dim L = 2, no proportional pair, supp(c_a) = U \ {y_a}, weight k+1)
  C  S4-4 Mobius criterion: CR match on the build; 24-value z_4 sweep --
     dim Rel = 1 EXACTLY at cross-ratio matches, else 0
  D  S4-2' K_V no-relation THEOREM at (3,7,1,5): triple locus = Y,
     dim Rel = 0, rank = Vh = 35 exactly
  E  S4-14: MDS sum lemma; dim pi_1 = m; m <= rank <= 2m; V <= m/2 =>
     charge >= 2 on both fixtures
  F  peeling/escape floor: rank >= sum min(h, escape); dim Rel <= cap;
     U-mech floor 16 / cap 4, K_V floor 35 (uncapped 40 shown FALSE)
  G  zero-escape clique (3,5,3,5): rank = 2m = 14 across 60 slope
     tuples -- MEASURED (not a theorem; labeled)
  H  re-pricing consistency pins (510 = 51 x 10; 510/384 = 85/64;
     margin 512 - 510 = 2; prize C(V*,2) unchanged)
"""
from __future__ import annotations

import sys
from itertools import combinations

sys.dont_write_bytecode = True

FAILURES = []
INF = "inf"


def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    if not ok:
        FAILURES.append(label)


class Row:
    def __init__(self, n, k, h, q):
        self.n, self.k, self.h, self.q = n, k, h, q
        self.A = k + h
        self.xs = [(i + 1) % q for i in range(n)]
        assert len(set(self.xs)) == n


def dual_basis(S, row):
    q, n, k = row.q, row.n, row.k
    S = tuple(sorted(S))
    lam = []
    for i in S:
        p = 1
        for j in S:
            if j != i:
                p = p * (row.xs[i] - row.xs[j]) % q
        lam.append(pow(p, q - 2, q))
    rows = []
    for t in range(len(S) - k):
        c = [0] * n
        for e, i in enumerate(S):
            c[i] = lam[e] * pow(row.xs[i], t, q) % q
        rows.append(c)
    return rows


def rref(rows, q):
    rows = [list(r) for r in rows]
    if not rows:
        return [], []
    ncol = len(rows[0])
    piv, pivcol = 0, []
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
                rows[i] = [(rows[i][c] - f * rows[piv][c]) % q for c in range(ncol)]
        pivcol.append(col)
        piv += 1
        if piv == len(rows):
            break
    return rows[:piv], pivcol


def rank_mod(rows, q):
    return len(rref(rows, q)[0])


def nullspace_mod(rows, ncol, q):
    red, pivcol = rref(rows, q)
    free = [c for c in range(ncol) if c not in pivcol]
    basis = []
    for fc in free:
        vv = [0] * ncol
        vv[fc] = 1
        for r, pc in enumerate(pivcol):
            vv[pc] = (-red[r][fc]) % q
        basis.append(vv)
    return basis


def relation_space(row, supports, slopes):
    """(dim Rel, relations as lists of V component vectors, rank)."""
    q, n = row.q, row.n
    blocks = [dual_basis(S, row) for S in supports]
    cols = []
    for B, z in zip(blocks, slopes):
        for c in B:
            if z == INF:
                cols.append([0] * n + list(c))
            else:
                cols.append([x % q for x in c] + [z * x % q for x in c])
    tot = len(cols)
    Mrows = [[cols[j][i] for j in range(tot)] for i in range(2 * n)]
    ker = nullspace_mod(Mrows, tot, q)
    rels = []
    for kv in ker:
        cs, off = [], 0
        for B in blocks:
            c = [0] * n
            for j in range(len(B)):
                t = kv[off + j]
                if t:
                    for i in range(n):
                        if B[j][i]:
                            c[i] = (c[i] + t * B[j][i]) % q
            off += len(B)
            cs.append(c)
        rels.append(cs)
    return len(ker), rels, rank_mod(cols, q)


def cross_ratio(a, b, c, d, q):
    num = (a - c) * (b - d) % q
    den = (a - d) * (b - c) % q
    if den == 0:
        return None
    return num * pow(den, q - 2, q) % q


def gates(supports, k, A):
    Ss = [set(S) for S in supports]
    V = len(Ss)
    pair = [len(Ss[a] & Ss[b]) for a in range(V) for b in range(a + 1, V)]
    trip = [len(Ss[a] & Ss[b] & Ss[c]) for a in range(V)
            for b in range(a + 1, V) for c in range(b + 1, V)]
    return pair, trip, all(len(S) == A for S in Ss)


def triple_locus(supports, n):
    mult = [0] * n
    for S in supports:
        for i in S:
            mult[i] += 1
    return frozenset(i for i in range(n) if mult[i] >= 3)


def peel(supports, n, max_it=20):
    cur = [frozenset(S) for S in supports]
    for _ in range(max_it):
        W = triple_locus([tuple(s) for s in cur], n)
        nxt = [s & W for s in cur]
        if nxt == cur:
            break
        cur = nxt
    return cur


def main():
    # ---------------- A + B + C: the U-mechanism at (3,5,1,4), n=16, q=97
    row = Row(16, 3, 5, 97)
    n, k, h, q, A = row.n, row.k, row.h, row.q, row.A
    V, d = 4, 1
    U = tuple(range(k + 2))                       # (0..4)
    ys = U[:V]
    B = {}
    cur = k + 2
    for a in range(V):
        for b in range(a + 1, V):
            B[(a, b)] = (cur,)
            cur += d
    priv = {}
    for a in range(V):
        priv[a] = (cur,)
        cur += 1
    supports = []
    for a in range(V):
        S = set(U) - {ys[a]}
        for b in range(V):
            if b != a:
                S |= set(B[(min(a, b), max(a, b))])
        S |= set(priv[a])
        supports.append(tuple(sorted(S)))
    pair, trip, size_ok = gates(supports, k, A)
    check("A: U-mechanism gates -- |S_a| = A, pairwise = k+d = 4, triples "
          "EXACTLY k-1 = 2 (gate SATURATED, not violated)",
          size_ok and all(p == k + d for p in pair)
          and all(t == k - 1 for t in trip),
          f"pair {sorted(set(pair))}, trip {sorted(set(trip))}")
    # Mobius-matched slopes: z_a = nu(x_{y_a}), nu = (w + 2)/(w + 5)
    ws = [row.xs[y] for y in ys]
    nu = None
    for (p_, r_, s_, t_) in [(1, 2, 1, 5), (2, 3, 1, 7), (1, 0, 1, 9),
                             (3, 1, 2, 11)]:
        if (p_ * t_ - r_ * s_) % q == 0:
            continue
        zs = []
        ok = True
        for w in ws:
            den = (s_ * w + t_) % q
            if den == 0:
                ok = False
                break
            zs.append((p_ * w + r_) % q * pow(den, q - 2, q) % q)
        if ok and len(set(zs)) == V and 0 not in zs:
            nu = (p_, r_, s_, t_)
            break
    check("A: a Mobius map with distinct nonzero matched slopes exists",
          nu is not None)
    dim, rels, rank = relation_space(row, supports, zs)
    check("A: dim Rel = 1 and rank = Vh - 1 = 19 (pilot stage1/stage3 "
          "pins)", dim == 1 and rank == V * h - 1,
          f"dim {dim}, rank {rank}")
    # B: S4-1 + S4-3 on the relation
    cs = rels[0]
    ok_loc = True
    for i in range(n):
        nz = sum(1 for a in range(V) if cs[a][i])
        if nz in (1, 2):
            ok_loc = False
    tl = triple_locus(supports, n)
    ok_loc &= all(all(i in tl for i in range(n) if cs[a][i])
                  for a in range(V))
    check("B: S4-1 -- at every point the relation has 0 or >= 3 nonzero "
          "components; every supp(c_a) inside the triple locus", ok_loc)
    spanrk = rank_mod([cs[a] for a in range(V)], q)
    prop = False
    for a in range(V):
        for b in range(a + 1, V):
            if rank_mod([cs[a], cs[b]], q) <= 1:
                prop = True
    supp_ok = all(
        frozenset(i for i in range(n) if cs[a][i])
        == frozenset(set(U) - {ys[a]}) for a in range(V))
    check("B: S4-3 -- all four duals in ONE 2-dim L, no two proportional; "
          "supp(c_a) = U \\ {y_a}, weight exactly k+1 = 4",
          spanrk == 2 and not prop and supp_ok, f"span {spanrk}")
    # C: S4-4 cross-ratio
    cr_z = cross_ratio(zs[0], zs[1], zs[2], zs[3], q)
    cr_w = cross_ratio(ws[0], ws[1], ws[2], ws[3], q)
    check("C: S4-4 minimal case -- CR(z_1..z_4) = CR(x_{y_1}..x_{y_4}) on "
          "the matched build", cr_z is not None and cr_z == cr_w,
          f"CR = {cr_z}")
    sweep_bad = match_cnt = 0
    cand = sorted(set([zs[3]] + [7 * t + 2 for t in range(23)]))
    for z4 in cand:
        if z4 in (zs[0], zs[1], zs[2]) or z4 == 0 or z4 >= q:
            continue
        d4, _, _ = relation_space(row, supports, [zs[0], zs[1], zs[2], z4])
        cr = cross_ratio(zs[0], zs[1], zs[2], z4, q)
        want = 1 if cr == cr_w else 0
        if d4 != want:
            sweep_bad += 1
        if cr == cr_w:
            match_cnt += 1
    check("C: z_4 sweep -- dim Rel = 1 EXACTLY at cross-ratio matches, 0 "
          "otherwise (slope codimension 1)",
          sweep_bad == 0 and match_cnt >= 1,
          f"{match_cnt} matches in sweep, {sweep_bad} bad")

    # ---------------- D: K_V no-relation THEOREM at (3,7,1,5), n=22, q=97
    rowK = Row(22, 3, 7, 97)
    nK, kK, hK, qK, AK = rowK.n, rowK.k, rowK.h, rowK.q, rowK.A
    VK, dK = 5, 1
    Y = (0, 1)
    BK = {}
    cur = 2
    for a in range(VK):
        for b in range(a + 1, VK):
            BK[(a, b)] = (cur, cur + 1)
            cur += dK + 1
    supK = []
    for a in range(VK):
        S = set(Y)
        for b in range(VK):
            if b != a:
                S |= set(BK[(min(a, b), max(a, b))])
        supK.append(tuple(sorted(S)))
    pairK, tripK, sizeK = gates(supK, kK, AK)
    tlK = triple_locus(supK, nK)
    zK = [3, 5, 7, 11, 13]
    dimK, _, rankK = relation_space(rowK, supK, zK)
    check("D: K_V -- |S_a| = A = 10, pairwise = k+d = 4, triple locus "
          "EXACTLY Y (|Y| = k-1 = 2)",
          sizeK and all(p == kK + dK for p in pairK)
          and tlK == frozenset(Y), f"tl {sorted(tlK)}")
    check("D: S4-2' K_V no-relation THEOREM -- dim Rel = 0, rank = Vh = "
          f"{VK * hK} EXACTLY (the banked measurement upgraded)",
          dimK == 0 and rankK == VK * hK, f"dim {dimK}, rank {rankK}")

    # ---------------- E: S4-14
    class LCG:
        def __init__(self, seed):
            self.s = seed

        def randint(self, lo, hi):
            self.s = (6364136223846793005 * self.s
                      + 1442695040888963407) % (1 << 64)
            return lo + (self.s >> 33) % (hi - lo + 1)

        def sample(self, n_, m_):
            pool = list(range(n_))
            out = []
            for _ in range(m_):
                out.append(pool.pop(self.randint(0, len(pool) - 1)))
            return out

    rng = LCG(20260802)
    bad = tot = 0
    for _ in range(40):
        a = rng.randint(kK + 1, kK + hK)
        b = rng.randint(kK + 1, kK + hK)
        X = set(rng.sample(nK, a))
        S = set(rng.sample(nK, b))
        if len(X & S) < kK:
            continue
        tot += 1
        bX, bS = dual_basis(tuple(X), rowK), dual_basis(tuple(S), rowK)
        if rank_mod(bX + bS, qK) != len(X | S) - kK:
            bad += 1
    check("E: MDS sum lemma -- |X ^ S| >= k gives C_X + C_S = C_{X u S} "
          f"({tot} samples)", tot >= 10 and bad == 0, f"{bad} bad")
    for (name, rw, sup, rk, Vv) in [("U-mech", row, supports, rank, V),
                                    ("K_V", rowK, supK, rankK, VK)]:
        un = set()
        for S in sup:
            un |= set(S)
        m = len(un) - rw.k
        pi1 = []
        for S in sup:
            pi1 += dual_basis(S, rw)
        d1 = rank_mod(pi1, rw.q)
        chg2 = (Vv <= m // 2)
        check(f"E: S4-14 on {name} -- dim pi_1 = m = {m}; m <= rank <= 2m; "
              "V <= m/2 holds and charge/ray >= 2",
              d1 == m and m <= rk <= 2 * m and chg2 and rk >= 2 * Vv,
              f"pi1 {d1}, rank {rk}, V {Vv}, m {m}")

    # ---------------- F: peeling / escape floor
    for (name, rw, sup, zz, pin_floor, pin_cap, pin_sinf) in [
            ("U-mech", row, supports, zs, 16, 4, 4),
            ("K_V", rowK, supK, zK, 35, 0, 2)]:
        inf_sets = peel(sup, rw.n)
        floor = sum(min(rw.h, len(set(S)) - len(I))
                    for S, I in zip(sup, inf_sets))
        cap = sum(max(0, len(I) - rw.k) for I in inf_sets)
        dimx, _, rkx = relation_space(rw, sup, zz)
        check(f"F: {name} peeling -- |S^inf| = {pin_sinf} per ray, escape "
              f"floor {pin_floor} <= rank, dim Rel <= cap {pin_cap}",
              all(len(I) == pin_sinf for I in inf_sets)
              and floor == pin_floor and rkx >= floor and dimx <= cap,
              f"floor {floor}, rank {rkx}, dim {dimx}")
    uncapped = sum(len(set(S)) - len(I)
                   for S, I in zip(supK, peel(supK, nK)))
    check("F: the min(h, .) cap is LOAD-BEARING -- the uncapped sum on "
          f"K_V is {uncapped} > rank {rankK} (the mis-coded first version "
          "the pilot caught)", uncapped == 40 and uncapped > rankK)

    # ---------------- G: zero-escape clique -- MEASURED collapse
    rowZ = Row(10, 3, 5, 97)
    uZ = tuple(range(10))
    g0 = rowZ.h - 3                                   # h - d, d = 3
    supZ = [tuple(sorted(set(uZ) - set(uZ[i * g0:(i + 1) * g0])))
            for i in range(5)]
    mZ = 10 - rowZ.k
    infZ = peel(supZ, rowZ.n)
    ranks = set()
    for t in range(60):
        zt = [(3 + 7 * t + 11 * a) % 97 for a in range(5)]
        if len(set(zt)) < 5 or 0 in zt:
            continue
        _, _, rz = relation_space(rowZ, supZ, zt)
        ranks.add(rz)
    check("G: zero-escape clique (3,5,3,5) -- zero escape confirmed "
          "(S^inf = S), and rank = 2m = 14 on EVERY sampled slope tuple: "
          "the COLLAPSE, a MEASUREMENT (never 2m-1; NOT a theorem -- "
          "claim 7's named open sub-item)",
          all(len(I) == len(set(S)) for S, I in zip(supZ, infZ))
          and ranks == {2 * mZ}, f"ranks {sorted(ranks)}")

    # ---------------- H: re-pricing consistency pins
    ok_h = (510 == 51 * 10)
    ok_h &= (510 * 64 == 85 * 384)                    # ratio = 85/64 = 1.328125
    ok_h &= (512 - 510 == 2)
    prize = []
    for (n_, k_, h_) in [(2**41, 2**39, 2**33 + 1), (2**41, 2**38, 2**33 + 1),
                         (2**41, 2**37, 2**32 + 1)]:
        Vst = (n_ - k_ + 1) // (h_ - 1)
        prize.append(Vst * (Vst - 1) // 2)
    ok_h &= (prize == [18336, 24976, 114960])
    check("H: re-pricing consistency -- RowC 1/4 U_N = 510 = 51 x C(5,2), "
          "ratio over K_V = 85/64 = 1.328125, margin to n/2 = 512 is "
          "EXACTLY 2; prize N_1 = C(V*,2) UNCHANGED (18336/24976/114960). "
          "(Cluster budget formula consistency-checked, NOT re-derived -- "
          "flagged.)", ok_h, str(prize))

    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("XR_SUPPORT4_STRUCTURE_ALL_PASS")


if __name__ == "__main__":
    main()
