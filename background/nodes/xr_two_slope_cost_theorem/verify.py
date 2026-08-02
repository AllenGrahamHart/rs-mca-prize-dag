#!/usr/bin/env python3
"""Verifier for xr_two_slope_cost_theorem.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers, deterministic, no third-party imports, no file reads.

Fresh implementation (independent of the pilot's tslib.py; cross-checked
against notes/pilots_20260802/xr_occupancy_v2/{cost.json pins, arith.json}
at draft time -- all pins inlined below):

  A  L1: dim C_S = |S|-k and dim(C_S ^ C_T) = max(0,|S^T|-k)
  B  dim R(P) = 2h for every sampled admissible datum, every band depth,
     slope pairs including 0 and (0:1) ("inf")
  C  core rows are IMPLIED by ray rows: rank(rays only) = rank(all) = 2h
  D  tiny shape (9,2,3,11): ALL slope pairs have rank 2h; distinct slope
     pairs have strictly larger joint rank (free-slope codim 2h-2 witness)
  E  family-rank law: spread family rank = 2hM; pairwise-core 3-ray family
     rank = 3h < 6h; sunflower cycle rank = mh vs per-datum 2hm (exact 2x)
  F  six-row exact integer ceiling table (fixed / free / per-ray / C(V*,2))
  G  end-to-end realisation at (16,4,4,97), d=1, fresh exhaustive scan
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


# ------------------------------------------------------------ field / rows
class LCG:
    def __init__(self, seed):
        self.s = seed

    def randint(self, lo, hi):
        self.s = (6364136223846793005 * self.s + 1442695040888963407) % (1 << 64)
        return lo + (self.s >> 33) % (hi - lo + 1)

    def sample(self, n, m):
        pool = list(range(n))
        out = []
        for _ in range(m):
            j = self.randint(0, len(pool) - 1)
            out.append(pool.pop(j))
        return out


INF = "inf"


class Row:
    def __init__(self, n, k, h, q):
        self.n, self.k, self.h, self.q = n, k, h, q
        self.A = k + h
        self.xs = [(i + 1) % q for i in range(n)]
        assert len(set(self.xs)) == n

    def interp(self, W, vals):
        """degree-<k interpolant coefficients of vals on index set W."""
        q, k = self.q, self.k
        coeff = [0] * k
        for idx, j in enumerate(W):
            num, den = [1], 1
            for m in W:
                if m == j:
                    continue
                new = [0] * (len(num) + 1)
                for e, ce in enumerate(num):
                    if ce:
                        new[e] = (new[e] - ce * self.xs[m]) % q
                        new[e + 1] = (new[e + 1] + ce) % q
                num = new
                den = den * (self.xs[j] - self.xs[m]) % q
            w = vals[idx] * pow(den, q - 2, q) % q
            for e in range(min(len(num), k)):
                coeff[e] = (coeff[e] + w * num[e]) % q
        return tuple(coeff)

    def ev(self, c, x):
        acc = 0
        for co in reversed(c):
            acc = (acc * x + co) % self.q
        return acc


def dual_basis(S, row):
    """basis of C_S = {c : supp(c) in S, c _|_ RS_k}: c^(t)_i = lam_i x_i^t."""
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


def ray_rows(row, S, z):
    n, q = row.n, row.q
    out = []
    for c in dual_basis(S, row):
        if z == INF:
            out.append([0] * n + list(c))
        else:
            out.append(list(c) + [z * x % q for x in c])
    return out


def core_rows(row, Z):
    n = row.n
    out = []
    for c in dual_basis(Z, row):
        out.append(list(c) + [0] * n)
        out.append([0] * n + list(c))
    return out


def datum_rows(row, Z, S1, z1, S2, z2, with_core=True):
    rows = ray_rows(row, S1, z1) + ray_rows(row, S2, z2)
    if with_core:
        rows = core_rows(row, Z) + rows
    return rows


def random_datum(row, d, rng):
    n, k, h = row.n, row.k, row.h
    need = k + d + 2 * (h - d)
    if need > n:
        return None
    pool = rng.sample(n, need)
    Z = tuple(sorted(pool[:k + d]))
    S1 = tuple(sorted(set(Z) | set(pool[k + d:k + d + h - d])))
    S2 = tuple(sorted(set(Z) | set(pool[k + d + h - d:])))
    return Z, S1, S2


def main():
    # ---------------- A: L1
    rng = LCG(20260802)
    bad = tot = 0
    for (n, k, h, q) in [(16, 4, 4, 97), (20, 5, 5, 241)]:
        row = Row(n, k, h, q)
        for _ in range(60):
            a = rng.randint(k + 1, min(n, k + h))
            b = rng.randint(k + 1, min(n, k + h))
            S = tuple(sorted(rng.sample(n, a)))
            T = tuple(sorted(rng.sample(n, b)))
            if S == T:
                continue
            tot += 1
            bS, bT = dual_basis(S, row), dual_basis(T, row)
            if len(bS) != a - k or len(bT) != b - k:
                bad += 1
                continue
            dim = len(bS) + len(bT) - rank_mod(bS + bT, q)
            if dim != max(0, len(set(S) & set(T)) - k):
                bad += 1
    check("A: L1 -- dim C_S = |S|-k and dim(C_S ^ C_T) = max(0,|S^T|-k) "
          "(120 sampled pairs, 2 shapes)", bad == 0, f"{tot} pairs, {bad} bad")

    # ---------------- B + C: datum rank = 2h; rays imply the core
    shapes = [(16, 4, 4, 97), (18, 4, 5, 101), (20, 5, 5, 241),
              (20, 4, 6, 101), (18, 3, 5, 73)]
    bad_b = bad_c = tot = 0
    for (n, k, h, q) in shapes:
        row = Row(n, k, h, q)
        for d in range(1, h - 1):
            for rep in range(2):
                dd = random_datum(row, d, rng)
                if dd is None:
                    continue
                Z, S1, S2 = dd
                zpairs = [(rng.randint(1, q - 1), rng.randint(1, q - 1)),
                          (0, rng.randint(1, q - 1)),
                          (INF, rng.randint(1, q - 1)), (INF, 0)]
                for (z1, z2) in zpairs:
                    if z1 == z2:
                        continue
                    tot += 1
                    full = rank_mod(datum_rows(row, Z, S1, z1, S2, z2), q)
                    rays = rank_mod(
                        datum_rows(row, Z, S1, z1, S2, z2, with_core=False), q)
                    if full != 2 * h:
                        bad_b += 1
                    if rays != full:
                        bad_c += 1
    check("B: dim R(P) = 2h at 5 shapes, every band depth, slope pairs "
          "incl. 0 and (0:1)", bad_b == 0, f"{tot} data, {bad_b} bad")
    check("C: core rows are implied by ray rows (rays-only rank = full "
          "rank) on every sampled datum", bad_c == 0, f"{bad_c} bad")

    # ---------------- D: tiny shape, all slope pairs + distinct kernels
    row = Row(9, 2, 3, 11)
    q, h = row.q, row.h
    Z, S1, S2 = (0, 1, 2), (0, 1, 2, 3, 4), (0, 1, 2, 5, 6)
    slopes = list(range(q)) + [INF]
    rks = set()
    systems = {}
    for i in range(len(slopes)):
        for j in range(i + 1, len(slopes)):
            rows = datum_rows(row, Z, S1, slopes[i], S2, slopes[j])
            rks.add(rank_mod(rows, q))
            systems[(slopes[i], slopes[j])] = rows
    check("D: tiny (9,2,3,11) -- ALL C(12,2) = 66 prescribed slope pairs "
          "have rank exactly 2h = 6", rks == {2 * h}, str(sorted(rks)))
    keys = list(systems)
    bad = 0
    for a in range(0, 12, 3):
        for b in range(a + 1, min(a + 5, len(keys))):
            if set(keys[a]) == set(keys[b]):
                continue
            if rank_mod(systems[keys[a]] + systems[keys[b]], q) <= 2 * h:
                bad += 1
    check("D: distinct slope pairs have distinct kernels (joint rank > 2h; "
          "free-slope codim = 2h-2 = 4 witness)", bad == 0, f"{bad} bad")

    # ---------------- E: family-rank law
    # (i) spread family: disjoint data -> rank = 2hM
    row = Row(24, 3, 3, 97)
    n, k, h, q = row.n, row.k, row.h, row.q
    fams = []
    for m0 in (0, 8, 16):
        Z = tuple(range(m0, m0 + 4))
        S1 = tuple(range(m0, m0 + 6))
        S2 = tuple(sorted(set(Z) | {m0 + 6, m0 + 7}))
        fams.append((Z, S1, S2))
    rows2 = []
    for i, (Z, S1, S2) in enumerate(fams[:2]):
        rows2 += datum_rows(row, Z, S1, 3 + i, S2, 5 + i)
    rows3 = rows2 + datum_rows(row, *fams[2][:1], fams[2][1], 9, fams[2][2], 11)
    check("E(i): spread family rank = 2hM exactly (M = 2, 3 disjoint data)",
          rank_mod(rows2, q) == 4 * h and rank_mod(rows3, q) == 6 * h,
          f"{rank_mod(rows2, q)}, {rank_mod(rows3, q)} vs {4*h}, {6*h}")
    # (ii) pairwise-core 3-ray family: rank = 3h although it carries 3 data
    row = Row(16, 3, 5, 97)
    n, k, h, q = row.n, row.k, row.h, row.q
    B12, B13, B23 = (0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11)
    Sa = tuple(sorted(B12 + B13))
    Sb = tuple(sorted(B12 + B23))
    Sc = tuple(sorted(B13 + B23))
    rows_pc = (ray_rows(row, Sa, 3) + ray_rows(row, Sb, 5)
               + ray_rows(row, Sc, 7))
    rk = rank_mod(rows_pc, q)
    per_datum_pred = 3 * 2 * h
    check("E(ii): pairwise-core 3-ray family (V = 3 rays, M = 3 data): "
          "rank = Vh = 15 < per-datum 2hM = 30 -- per-datum additivity FAILS",
          rk == 3 * h and rk < per_datum_pred, f"rank {rk}")
    # each constituent pair alone still costs 2h
    prs = [rank_mod(ray_rows(row, X, zx) + ray_rows(row, Y, zy), q)
           for (X, zx), (Y, zy) in
           [((Sa, 3), (Sb, 5)), ((Sa, 3), (Sc, 7)), ((Sb, 5), (Sc, 7))]]
    check("E(ii): each constituent datum alone has rank exactly 2h = 10",
          prs == [2 * h] * 3, str(prs))
    # (iii) sunflower cycle at (16,3,3,97), d = 1: m rays, m data, rank mh
    row = Row(16, 3, 3, 97)
    n, k, h, q = row.n, row.k, row.h, row.q
    d, m = 1, 5
    Y = tuple(range(k - 1))                      # common (k-1)-set
    petals = [tuple(range(k - 1 + i * (d + 1), k - 1 + (i + 1) * (d + 1)))
              for i in range(m)]
    cores = [tuple(sorted(Y + p)) for p in petals]
    edge_supports = [tuple(sorted(set(cores[i]) | set(cores[(i + 1) % m])))
                     for i in range(m)]          # size k+2d+1 = A = 6
    assert all(len(S) == row.A for S in edge_supports)
    zs = [2, 3, 5, 7, 11]
    rows_sf = []
    for S, z in zip(edge_supports, zs):
        rows_sf += ray_rows(row, S, z)
    rk = rank_mod(rows_sf, q)
    check("E(iii): sunflower cycle (m = 5 rays = data): family rank = mh = "
          f"{m*h}, exactly HALF the per-datum prediction 2hm = {2*h*m}",
          rk == m * h and 2 * rk == 2 * h * m, f"rank {rk}")

    # ---------------- F: six-row exact integer ceiling table
    ROWS = [("RowC 1/4", 1024, 256, 5), ("RowC 1/8", 1024, 128, 5),
            ("RowC 1/16", 1024, 64, 3),
            ("prize 1/4", 2**41, 2**39, 2**33 + 1),
            ("prize 1/8", 2**41, 2**38, 2**33 + 1),
            ("prize 1/16", 2**41, 2**37, 2**32 + 1)]
    # pins: notes/pilots_20260802/xr_occupancy_v2/arith.json (fixed/free,
    # per-ray = "ceiling_sunflower_cost") and
    # notes/pilots_20260802/adv_sublinear_rank/arith_repricing.json (V*, C(V*,2))
    PIN_FIXED = [153, 179, 319, 191, 223, 479]
    PIN_FREE = [191, 223, 479, 191, 223, 479]
    PIN_RAY = [307, 358, 639, 383, 447, 959]
    PIN_VSTAR = [192, 224, 480]          # prize rows only
    PIN_CV2 = [18336, 24976, 114960]
    got_f, got_fr, got_r, got_v, got_c = [], [], [], [], []
    for (name, n, k, h) in ROWS:
        R = n - k
        got_f.append((2 * R - 1) // (2 * h))
        got_fr.append((2 * R - 1) // (2 * h - 2))
        got_r.append((2 * R - 1) // h)
        if name.startswith("prize"):
            V = (R + 1) // (h - 1)
            got_v.append(V)
            got_c.append(V * (V - 1) // 2)
    check("F: per-datum prescribed ceiling floor((2R-1)/(2h)) matches the "
          "banked table", got_f == PIN_FIXED, str(got_f))
    check("F: free-slope ceiling floor((2R-1)/(2h-2)) matches the banked "
          "table", got_fr == PIN_FREE, str(got_fr))
    check("F: per-ray ceiling floor((2R-1)/h) matches the banked table",
          got_r == PIN_RAY, str(got_r))
    check("F: prize-row point-budget V* = floor((R+1)/(h-1)) = 192/224/480 "
          "and datum counts C(V*,2) = 18336/24976/114960 (the K_V "
          "re-pricing)", got_v == PIN_VSTAR and got_c == PIN_CV2,
          f"{got_v} {got_c}")

    # ---------------- G: end-to-end realisation + fresh exhaustive scan
    row = Row(16, 4, 4, 97)
    n, k, h, q, A = row.n, row.k, row.h, row.q, row.A
    d = 1
    Z = (0, 1, 2, 3, 4)
    S1 = tuple(sorted(set(Z) | {5, 6, 7}))
    S2 = tuple(sorted(set(Z) | {8, 9, 10}))
    z1, z2 = 3, 7
    rows_g = datum_rows(row, Z, S1, z1, S2, z2)
    ns = nullspace_mod(rows_g, 2 * n, q)
    check("G: kernel dimension = 2n - 2h "
          f"({2*n-2*h})", len(ns) == 2 * n - 2 * h, str(len(ns)))
    sol = None
    rng2 = LCG(7)
    for _ in range(300):
        w = [0] * (2 * n)
        for bvec in ns:
            cf = rng2.randint(0, q - 1)
            if cf:
                for i in range(2 * n):
                    w[i] = (w[i] + cf * bvec[i]) % q
        u, v = w[:n], w[n:]
        fu = row.interp(tuple(range(k)), u[:k])
        fv = row.interp(tuple(range(k)), v[:k])
        if all(row.ev(fu, row.xs[i]) == u[i] for i in range(n)) and \
           all(row.ev(fv, row.xs[i]) == v[i] for i in range(n)):
            continue                      # degenerate (u,v) in C x C
        sol = (u, v)
        break
    check("G: a non-degenerate realisation exists", sol is not None)
    if sol:
        u, v = sol
        # fresh exhaustive scan: every pair with joint agreement >= k
        pairs = {}
        for W in combinations(range(n), k):
            f = row.interp(W, [u[i] for i in W])
            g = row.interp(W, [v[i] for i in W])
            key = (f, g)
            if key in pairs:
                continue
            Zset = frozenset(i for i in range(n)
                             if row.ev(f, row.xs[i]) == u[i]
                             and row.ev(g, row.xs[i]) == v[i])
            pairs[key] = Zset
        byZ = {}
        for (f, g), Zset in pairs.items():
            if len(Zset) >= k:
                byZ.setdefault(Zset, (f, g))
        okZ = frozenset(Z) in byZ
        live_ok = False
        if okZ:
            f, g = byZ[frozenset(Z)]
            live = []
            for z in list(range(q)) + [INF]:
                if z == INF:
                    wz = v
                    cz = [g[i] for i in range(k)]
                else:
                    wz = [(u[i] + z * v[i]) % q for i in range(n)]
                    cz = [(f[i] + z * g[i]) % q for i in range(k)]
                agr = sum(1 for i in range(n)
                          if row.ev(cz, row.xs[i]) == wz[i])
                if agr >= A:
                    live.append(z)
            live_ok = z1 in live and z2 in live
        check("G: fresh exhaustive scan -- the intended core appears as a "
              "depth-1 joint-agreement set and BOTH prescribed slopes are "
              "live at agreement >= A (Lemma 0 semantics end-to-end)",
              okZ and live_ok)

    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("XR_TWO_SLOPE_COST_THEOREM_ALL_PASS")


if __name__ == "__main__":
    main()
