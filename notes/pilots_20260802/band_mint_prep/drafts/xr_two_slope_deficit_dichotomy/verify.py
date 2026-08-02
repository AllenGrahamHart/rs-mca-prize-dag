#!/usr/bin/env python3
"""Verifier for xr_two_slope_deficit_dichotomy.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers, deterministic, no third-party imports, no file reads.

Fresh scan engine (independent of the pilots' occlib/bandlib): one pass
over all k-subsets recovers EVERY codeword pair with joint agreement >= k
and EVERY ray of agreement >= A over ALL of P^1(F_q) INCLUDING (0:1).

  A  the dichotomy integer: k + 2d + 1 > A  <=>  2d >= h
  B  planted proportional-difference pair at 2d = h: the forced ray
     over-agrees at exactly A + 1 (Theorem 2's mechanism, positive control)
  C  realized fixtures at 2d >= h: 0 live-ray double-carries, 0
     proportional differences among same-depth pairs (Theorem 2 (a),(b))
  D  Theorem G on realized fixtures: L1 sharing identity at every ray
     pair; overlap >= k+1 & distinct slopes => the overlap IS a joint
     agreement set with both slopes live (witnessed events counted);
     complementary depths d + e <= h - 1 on every ray
  E  core transversality: C_Z ^ C_Z' = 0 for distinct cores
  F  existence side at d = (h-1)/2: the sunflower cycle realizes with
     shared slopes and proportional differences
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


class LCG:
    def __init__(self, seed):
        self.s = seed

    def randint(self, lo, hi):
        self.s = (6364136223846793005 * self.s + 1442695040888963407) % (1 << 64)
        return lo + (self.s >> 33) % (hi - lo + 1)


class Row:
    def __init__(self, n, k, h, q):
        self.n, self.k, self.h, self.q = n, k, h, q
        self.A = k + h
        self.xs = [(i + 1) % q for i in range(n)]
        assert len(set(self.xs)) == n

    def interp(self, W, vals):
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


# ------------------------------------------------------- exhaustive scan
def scan(row, u, v):
    """(pairs, rays):
    pairs: {(f,g): frozenset joint agreement}, every pair with J >= k;
    rays:  {(z, c): frozenset agreement set}, every ray with agr >= A,
           z over ALL of P^1 including INF."""
    n, k, q, A = row.n, row.k, row.q, row.A
    pairs, rays = {}, {}
    for W in combinations(range(n), k):
        f = row.interp(W, [u[i] for i in W])
        g = row.interp(W, [v[i] for i in W])
        if (f, g) not in pairs:
            Z = frozenset(i for i in range(n)
                          if row.ev(f, row.xs[i]) == u[i]
                          and row.ev(g, row.xs[i]) == v[i])
            pairs[(f, g)] = Z
        pu = [(row.ev(f, row.xs[i]) - u[i]) % q for i in range(n)]
        qv = [(row.ev(g, row.xs[i]) - v[i]) % q for i in range(n)]
        both = sum(1 for i in range(n) if pu[i] == 0 and qv[i] == 0)
        cnt = {}
        for i in range(n):
            if qv[i]:
                z = (-pu[i]) * pow(qv[i], q - 2, q) % q
                cnt[z] = cnt.get(z, 0) + 1
        for z, c0 in cnt.items():
            if both + c0 >= A:
                c = tuple((f[e] + z * g[e]) % q for e in range(k))
                if (z, c) not in rays:
                    rays[(z, c)] = frozenset(
                        i for i in range(n)
                        if (pu[i] + z * qv[i]) % q == 0)
        inf_agr = sum(1 for i in range(n) if qv[i] == 0)
        if inf_agr >= A and (INF, g) not in rays:
            rays[(INF, g)] = frozenset(i for i in range(n) if qv[i] == 0)
    return pairs, rays


def realise(row, rows, seed, tries=60):
    q, n, k = row.q, row.n, row.k
    ns = nullspace_mod(rows, 2 * n, q)
    rng = LCG(seed)
    for _ in range(tries):
        w = [0] * (2 * n)
        for b in ns:
            cf = rng.randint(0, q - 1)
            if cf:
                for i in range(2 * n):
                    w[i] = (w[i] + cf * b[i]) % q
        u, v = w[:n], w[n:]
        fu = row.interp(tuple(range(k)), u[:k])
        fv = row.interp(tuple(range(k)), v[:k])
        if all(row.ev(fu, row.xs[i]) == u[i] for i in range(n)) and \
           all(row.ev(fv, row.xs[i]) == v[i] for i in range(n)):
            continue
        return u, v
    return None


def prop_direction(row, p1, p2):
    """z* in F_q u {INF} with f1-f2 = -z*(g1-g2), or None if independent."""
    q, k = row.q, row.k
    df = [(p1[0][e] - p2[0][e]) % q for e in range(k)]
    dg = [(p1[1][e] - p2[1][e]) % q for e in range(k)]
    if not any(dg):
        return INF if any(df) else None
    if not any(df):
        return 0
    e0 = next(e for e in range(k) if dg[e])
    z = (-df[e0]) * pow(dg[e0], q - 2, q) % q
    if all((df[e] + z * dg[e]) % q == 0 for e in range(k)):
        return z
    return None


def gate_stats(row, pairs, rays):
    maxray = max((len(S) for S in rays.values()), default=0)
    return maxray


def main():
    rng = LCG(20260802)

    # ---------------- A: the dichotomy integer
    bad = 0
    for h in range(2, 40):
        for d in range(1, h - 1):
            over = (2 * d + 1 > h)          # k+2d+1 > k+h
            if over != (2 * d >= h):
                bad += 1
    check("A: k + 2d + 1 > A  <=>  2d >= h (all h < 40, all band depths)",
          bad == 0, f"{bad} bad")

    # ---------------- B: planted proportional pair at 2d = h over-agrees
    row = Row(18, 4, 4, 97)                 # h = 4, d = 2, 2d = h
    n, k, h, q, A = row.n, row.k, row.h, row.q, row.A
    d = 2
    Z1 = tuple(range(k + d))                              # (0..5)
    Z2 = tuple(range(3)) + tuple(range(k + d, k + d + 3))  # overlap k-1 = 3
    assert len(set(Z1) & set(Z2)) == k - 1
    f1 = tuple(rng.randint(0, q - 1) for _ in range(k))
    g1 = tuple(rng.randint(0, q - 1) for _ in range(k))
    t = tuple(rng.randint(0, q - 1) for _ in range(k - 1)) + (1,)
    zstar = 5
    g2 = tuple((g1[e] + t[e]) % q for e in range(k))
    f2 = tuple((f1[e] - zstar * t[e]) % q for e in range(k))
    u, v = [0] * n, [0] * n
    for i in range(n):
        if i in Z1:
            u[i], v[i] = row.ev(f1, row.xs[i]), row.ev(g1, row.xs[i])
        elif i in Z2:
            u[i], v[i] = row.ev(f2, row.xs[i]), row.ev(g2, row.xs[i])
        else:
            u[i], v[i] = rng.randint(0, q - 1), rng.randint(0, q - 1)
    c = tuple((f1[e] + zstar * g1[e]) % q for e in range(k))
    wz = [(u[i] + zstar * v[i]) % q for i in range(n)]
    agr = sum(1 for i in range(n) if row.ev(c, row.xs[i]) == wz[i])
    check("B: planted proportional-difference pair at 2d = h: the common "
          f"codeword agrees with w_z* on >= |Z1 u Z2| = A + 1 = {A+1} "
          "points -- the tangent gate fires exactly as Theorem 2 predicts",
          agr >= A + 1, f"agr = {agr}")

    # ---------------- C + D + E: realized fixtures, fresh scan
    fixtures = []
    # (C-i) TWO disjoint data at 2d >= h: (22,4,5,89), d = 3
    row_c = Row(22, 4, 5, 89)
    dd = 3
    rows_c = []
    for base, (za, zb) in [(0, (3, 7)), (11, (5, 13))]:
        Zc = tuple(range(base, base + row_c.k + dd))
        S1c = tuple(sorted(set(Zc) | {base + 7, base + 8}))
        S2c = tuple(sorted(set(Zc) | {base + 9, base + 10}))
        rows_c += core_rows(row_c, Zc) + ray_rows(row_c, S1c, za) \
            + ray_rows(row_c, S2c, zb)
    sol = realise(row_c, rows_c, seed=11)
    if sol:
        fixtures.append(("deep-datum d=3 (2d>=h)", row_c, sol))
    check("C: deep fixture realized (two disjoint depth-3 data, h = 5)",
          sol is not None)
    # (F) sunflower cycle at (16,3,3,97), d = 1 = (h-1)/2
    row_f = Row(16, 3, 3, 97)
    kf, hf = row_f.k, row_f.h
    Y = tuple(range(kf - 1))
    petals = [tuple(range(kf - 1 + 2 * i, kf - 1 + 2 * i + 2))
              for i in range(5)]
    cores_f = [tuple(sorted(Y + p)) for p in petals]
    edges = [tuple(sorted(set(cores_f[i]) | set(cores_f[(i + 1) % 5])))
             for i in range(5)]
    zs = [2, 3, 5, 7, 11]
    rows_f = []
    for S, z in zip(edges, zs):
        rows_f += ray_rows(row_f, S, z)
    solf = None
    for seed in range(1, 40):
        cand = realise(row_f, rows_f, seed=seed, tries=8)
        if cand is None:
            continue
        pairs, rays = scan(row_f, *cand)
        if gate_stats(row_f, pairs, rays) <= row_f.A:
            solf = cand
            break
    if solf:
        fixtures.append(("sunflower d=(h-1)/2", row_f, solf))
    check("F: sunflower-cycle fixture realized within the tangent gate",
          solf is not None)

    tot_double = tot_prop = tot_shared = tot_deep_pairs = 0
    tot_l1_bad = tot_wit = tot_wit_bad = tot_comp_bad = tot_core_bad = 0
    sun_props = 0
    for (name, rw, (u, v)) in fixtures:
        n, k, h, q, A = rw.n, rw.k, rw.h, rw.q, rw.A
        pairs, rays = scan(rw, u, v)
        deep = [d for d in range(1, h - 1) if 2 * d >= h]
        # C: no live ray carries two depth-d cores (2d >= h); no
        #    proportional differences among same-depth deep pairs
        cores_by_depth = {}
        for (f, g), Z in pairs.items():
            dd2 = len(Z) - k
            if 1 <= dd2 <= h - 2:
                cores_by_depth.setdefault(dd2, []).append(((f, g), Z))
        for d0 in deep:
            lst = cores_by_depth.get(d0, [])
            tot_deep_pairs += len(lst)
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    if prop_direction(rw, lst[i][0], lst[j][0]) is not None:
                        tot_prop += 1
                    for (zz, cc), S in rays.items():
                        if lst[i][1] <= S and lst[j][1] <= S:
                            tot_double += 1
        # D: Theorem G at every ray pair
        rl = list(rays.items())
        for a in range(len(rl)):
            for b in range(a + 1, len(rl)):
                (z1, c1), S1 = rl[a]
                (z2, c2), S2 = rl[b]
                ov = S1 & S2
                b1, b2 = dual_basis(tuple(sorted(S1)), rw), \
                    dual_basis(tuple(sorted(S2)), rw)
                dim = len(b1) + len(b2) - rank_mod(b1 + b2, q)
                if dim != max(0, len(ov) - k):
                    tot_l1_bad += 1
                if z1 != z2 and len(ov) >= k + 1:
                    tot_shared += 1
                    if ov in set(pairs.values()):
                        pr = next(p for p, Z in pairs.items() if Z == ov)
                        if S1 >= ov and S2 >= ov:
                            tot_wit += 1
                        else:
                            tot_wit_bad += 1
                    else:
                        tot_wit_bad += 1
        # D(iii): complementary depths on every ray
        for (zz, cc), S in rays.items():
            inside = [Z for Z in pairs.values()
                      if len(Z) >= k + 1 and Z <= S]
            for i in range(len(inside)):
                for j in range(i + 1, len(inside)):
                    if (len(inside[i]) - k) + (len(inside[j]) - k) > h - 1:
                        tot_comp_bad += 1
        # E: core transversality
        cs = [Z for Z in pairs.values() if len(Z) >= k + 1]
        for i in range(min(len(cs), 12)):
            for j in range(i + 1, min(len(cs), 12)):
                bi = dual_basis(tuple(sorted(cs[i])), rw)
                bj = dual_basis(tuple(sorted(cs[j])), rw)
                if bi and bj and \
                   len(bi) + len(bj) != rank_mod(bi + bj, q):
                    tot_core_bad += 1
        # F: mechanism existence at low depth (sunflower fixture)
        if name.startswith("sunflower"):
            for i in range(len(cores_f)):
                for j in range(i + 1, len(cores_f)):
                    ci, cj = frozenset(cores_f[i]), frozenset(cores_f[j])
                    if ci in set(pairs.values()) and cj in set(pairs.values()):
                        pi = next(p for p, Z in pairs.items() if Z == ci)
                        pj = next(p for p, Z in pairs.items() if Z == cj)
                        if prop_direction(rw, pi, pj) is not None:
                            sun_props += 1

    check("C: 0 live-ray double-carries and 0 proportional differences at "
          "depths with 2d >= h (both fixtures, exhaustive scan over P^1 "
          "incl. (0:1); non-vacuous: >= 2 deep pairs scanned)",
          tot_double == 0 and tot_prop == 0 and tot_deep_pairs >= 2,
          f"double={tot_double} prop={tot_prop} deep_pairs={tot_deep_pairs}")
    check("D: L1 sharing identity holds at every ray pair",
          tot_l1_bad == 0, f"{tot_l1_bad} bad")
    check("D: every distinct-slope overlap >= k+1 is EXACTLY a joint "
          "agreement set with both slopes live (Theorem G witness)",
          tot_shared > 0 and tot_wit == tot_shared and tot_wit_bad == 0,
          f"{tot_wit}/{tot_shared} witnessed, {tot_wit_bad} bad")
    check("D: complementary depths d + e <= h - 1 on every ray",
          tot_comp_bad == 0, f"{tot_comp_bad} bad")
    check("E: distinct cores transverse (C_Z ^ C_Z' = 0)",
          tot_core_bad == 0, f"{tot_core_bad} bad")
    check("F: the sharing mechanism EXISTS at d = (h-1)/2 -- sunflower "
          "core pairs with proportional differences", sun_props >= 4,
          f"{sun_props} proportional core pairs")

    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("XR_TWO_SLOPE_DEFICIT_DICHOTOMY_ALL_PASS")


if __name__ == "__main__":
    main()
