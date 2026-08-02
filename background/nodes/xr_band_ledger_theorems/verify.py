#!/usr/bin/env python3
"""Verifier for xr_band_ledger_theorems.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers, deterministic, no third-party imports, no file reads.
NOTE: the prize-row divisor-block sums make this the slowest verifier of
the wave (a few seconds), still far inside the tiny profile.

  A  T3 line cap: planted single-core fixtures, L = cap TIGHT at
     d = 1, 2, 3; cap + 1 unrealisable by point count
  B  T4 ray rigidity on every witnessed common ray (interpolation
     forcing c = f + zg; at most one common ray per pair of pairs)
  C  T5 + corollary: planted overlap-(k-1) pair -- proportionality
     automatic, forced ray agreement = A + 1 (the gate fires)
  D  T7 two-column determinacy: exact 2x2 reconstruction
  E  FULL sunflower (m = 7 at (16,3,3)): N_1 = 7, |Gamma_band| = 21,
     master-ledger slack EXACTLY 2.000
  F  Theorem-6 WARNING bijection counted on one ray
  G  six-row pricing pins: band-proper SUM L(d), L(h-1) = n-A+1,
     printed-column kill on 5 of 6 rows
"""
from __future__ import annotations

import sys
from itertools import combinations
from math import isqrt

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


def scan(row, u, v):
    n, k, q, A = row.n, row.k, row.q, row.A
    pairs, rays = {}, {}
    for W in combinations(range(n), k):
        f = row.interp(W, [u[i] for i in W])
        g = row.interp(W, [v[i] for i in W])
        if (f, g) not in pairs:
            pairs[(f, g)] = frozenset(
                i for i in range(n)
                if row.ev(f, row.xs[i]) == u[i]
                and row.ev(g, row.xs[i]) == v[i])
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
                        i for i in range(n) if (pu[i] + z * qv[i]) % q == 0)
        if sum(1 for i in range(n) if qv[i] == 0) >= A and (INF, g) not in rays:
            rays[(INF, g)] = frozenset(i for i in range(n) if qv[i] == 0)
    return pairs, rays


def vanish_coeffs(pts, row):
    q = row.q
    m = [1]
    for i in pts:
        a = row.xs[i]
        new = [0] * (len(m) + 1)
        for e, ce in enumerate(m):
            new[e] = (new[e] - ce * a) % q
            new[e + 1] = (new[e + 1] + ce) % q
        m = new
    return m


def t4_battery(row, pairs, rays):
    """(witnessed, bad_ident, bad_multi): every pair of distinct pairs
    subordinate to a common ray -> c = f + zg forced for both, and at
    most one common ray."""
    q, k = row.q, row.k
    plist = [(p, Z) for p, Z in pairs.items() if len(Z) >= k]
    rlist = list(rays.items())
    sub = {}
    for pi, (p, Z) in enumerate(plist):
        for ri, ((z, c), S) in enumerate(rlist):
            if Z <= S:
                sub.setdefault(pi, []).append(ri)
    wit = bad_ident = bad_multi = 0
    common = {}
    for pi, ris in sub.items():
        (f, g), Z = plist[pi]
        for ri in ris:
            (z, c), S = rlist[ri]
            if z == INF:
                if g != c:
                    bad_ident += 1
            else:
                if any((f[e] + z * g[e] - c[e]) % q for e in range(k)):
                    bad_ident += 1
    ray_members = {}
    for pi, ris in sub.items():
        for ri in ris:
            ray_members.setdefault(ri, []).append(pi)
    for ri, ms in ray_members.items():
        for a in range(len(ms)):
            for b in range(a + 1, len(ms)):
                key = (ms[a], ms[b])
                common[key] = common.get(key, 0) + 1
                wit += 1
    bad_multi = sum(1 for v in common.values() if v > 1)
    return wit, bad_ident, bad_multi


def sum_floor_div(C, G):
    """sum_{g=2}^{G} floor(C/g), exact, O(sqrt(C)) via two regimes."""
    if G <= 1:
        return 0
    s = isqrt(C)
    total = 0
    g_hi = min(s, G)
    total += sum(C // g for g in range(2, g_hi + 1))
    if G > s:
        vmax = C // (s + 1)
        for v in range(1, vmax + 1):
            lo = max(C // (v + 1) + 1, s + 1)
            hi = min(C // v, G)
            if hi >= lo:
                total += v * (hi - lo + 1)
    return total


def main():
    rng = LCG(20260802)

    # ---------------- A: T3 planted single-core fixtures at (16,4,5,97)
    row = Row(16, 4, 5, 97)
    n, k, h, q, A = row.n, row.k, row.h, row.q, row.A
    fixA = None
    for d in (1, 2, 3):
        J = k + d
        cap = (n - J) // (A - J)
        check(f"A: cap arithmetic d={d}: floor((n-J)/(A-J)) = {cap}; "
              "cap+1 blocks need (cap+1)(A-J) > n-J points",
              (cap + 1) * (A - J) > n - J)
        f = tuple(rng.randint(0, q - 1) for _ in range(k))
        g = tuple(rng.randint(0, q - 1) for _ in range(k))
        Z = tuple(range(J))
        u, v = [None] * n, [None] * n
        for i in Z:
            u[i], v[i] = row.ev(f, row.xs[i]), row.ev(g, row.xs[i])
        cur = J
        zs = []
        for t in range(cap):
            zt = 3 + 5 * t
            zs.append(zt)
            for i in range(cur, cur + A - J):
                ep = rng.randint(1, q - 1)
                v[i] = (row.ev(g, row.xs[i]) + ep) % q
                u[i] = (row.ev(f, row.xs[i]) - zt * ep) % q
            cur += A - J
        for i in range(cur, n):
            u[i], v[i] = rng.randint(0, q - 1), rng.randint(0, q - 1)
        pairs, rays = scan(row, u, v)
        Zf = frozenset(Z)
        L = sum(1 for (zc, S) in rays.items() if Zf <= S)
        allcap = all(
            sum(1 for (zc, S) in rays.items() if Zp <= S)
            <= (n - len(Zp)) // (A - len(Zp))
            for p, Zp in pairs.items() if k <= len(Zp) < A)
        check(f"A: planted fixture d={d}: L = cap = {cap} TIGHT, and NO "
              "scanned pair exceeds its cap", L == cap and allcap,
              f"L = {L}")
        if d == 1:
            fixA = (pairs, rays, (f, g), Zf, zs, list(u), list(v))

    # ---------------- B: T4 on the d=1 fixture
    pairs, rays, fg, Zf, zsA, uA, vA = fixA
    wit, bad_i, bad_m = t4_battery(row, pairs, rays)
    check("B: T4 on every witnessed common ray -- interpolation forces "
          "c = f + zg for every subordinate pair (rigidity identity), and "
          "no two pairs share two rays", wit >= 1 and bad_i == 0
          and bad_m == 0, f"{wit} witnessed, ident {bad_i}, multi {bad_m}")

    # ---------------- C: T5 planted overlap-(k-1) at (16,5,4,97)
    row5 = Row(16, 5, 4, 97)
    n5, k5, h5, q5, A5 = row5.n, row5.k, row5.h, row5.q, row5.A
    d5 = 2
    Y = tuple(range(k5 - 1))
    Z1 = Y + tuple(range(4, 4 + d5 + 1))
    Z2 = Y + tuple(range(7, 7 + d5 + 1))
    assert len(Z1) == len(Z2) == k5 + d5
    VY = vanish_coeffs(Y, row5)
    f1 = tuple(rng.randint(0, q5 - 1) for _ in range(k5))
    g1 = tuple(rng.randint(0, q5 - 1) for _ in range(k5))
    al, be = 3, 7
    f2 = tuple((f1[e] + al * (VY[e] if e < len(VY) else 0)) % q5
               for e in range(k5))
    g2 = tuple((g1[e] + be * (VY[e] if e < len(VY) else 0)) % q5
               for e in range(k5))
    u, v = [None] * n5, [None] * n5
    for i in Z1:
        u[i], v[i] = row5.ev(f1, row5.xs[i]), row5.ev(g1, row5.xs[i])
    for i in Z2:
        u[i], v[i] = row5.ev(f2, row5.xs[i]), row5.ev(g2, row5.xs[i])
    for i in range(n5):
        if u[i] is None:
            u[i], v[i] = rng.randint(0, q5 - 1), rng.randint(0, q5 - 1)
    df = [(f1[e] - f2[e]) % q5 for e in range(k5)]
    dg = [(g1[e] - g2[e]) % q5 for e in range(k5)]
    e0 = next(e for e in range(k5) if dg[e])
    zst = (-df[e0]) * pow(dg[e0], q5 - 2, q5) % q5
    prop = all((df[e] + zst * dg[e]) % q5 == 0 for e in range(k5))
    c = tuple((f1[e] + zst * g1[e]) % q5 for e in range(k5))
    wz = [(u[i] + zst * v[i]) % q5 for i in range(n5)]
    agr = sum(1 for i in range(n5) if row5.ev(c, row5.xs[i]) == wz[i])
    check("C: T5 overlap-(k-1) fixture -- proportionality AUTOMATIC "
          "(differences are multiples of V_Y), and the forced ray agrees "
          f"on >= |Z1 u Z2| = A + 1 = {A5 + 1} points: d1 + d2 >= h "
          "forces the tangent event", prop and agr >= A5 + 1,
          f"z* = {zst}, agr = {agr}")

    # ---------------- D + E: FULL sunflower at (16,3,3,97)
    row3 = Row(16, 3, 3, 97)
    n3, k3, h3, q3, A3 = row3.n, row3.k, row3.h, row3.q, row3.A
    m = 7
    Y3 = tuple(range(k3 - 1))
    petals = [tuple(range(2 + 2 * i, 4 + 2 * i)) for i in range(m)]
    VY3 = vanish_coeffs(Y3, row3)
    L1 = (n3 - k3 - 1) // (h3 - 1)
    good = None
    for seed in range(1, 60):
        r2 = LCG(seed)
        f0 = tuple(r2.randint(0, q3 - 1) for _ in range(k3))
        g0 = tuple(r2.randint(0, q3 - 1) for _ in range(k3))
        ab = [(r2.randint(0, q3 - 1), r2.randint(1, q3 - 1))
              for _ in range(m)]
        zset = set()
        okz = True
        for a in range(m):
            for b in range(a + 1, m):
                da = (ab[a][0] - ab[b][0]) % q3
                db = (ab[a][1] - ab[b][1]) % q3
                if db == 0:
                    okz = False
                    break
                zz = (-da) * pow(db, q3 - 2, q3) % q3
                if zz in zset:
                    okz = False
                    break
                zset.add(zz)
            if not okz:
                break
        if not okz:
            continue
        u3, v3 = [None] * n3, [None] * n3
        prs = []
        for i in range(m):
            fi = tuple((f0[e] + ab[i][0] * (VY3[e] if e < len(VY3) else 0))
                       % q3 for e in range(k3))
            gi = tuple((g0[e] + ab[i][1] * (VY3[e] if e < len(VY3) else 0))
                       % q3 for e in range(k3))
            prs.append((fi, gi))
            for j in petals[i]:
                u3[j], v3[j] = row3.ev(fi, row3.xs[j]), row3.ev(gi, row3.xs[j])
        for j in Y3:
            u3[j], v3[j] = row3.ev(f0, row3.xs[j]), row3.ev(g0, row3.xs[j])
        pairs3, rays3 = scan(row3, u3, v3)
        # gate + intended structure
        if max((len(S) for S in rays3.values()), default=0) > A3:
            continue
        band = {p: Z for p, Z in pairs3.items()
                if len(Z) == k3 + 1}
        if len(band) != m:
            continue
        Ls = {p: sum(1 for (zc, S) in rays3.items() if Z <= S)
              for p, Z in band.items()}
        if any(Ls[p] != m - 1 for p in band):
            continue
        good = (pairs3, rays3, band, Ls, u3, v3)
        break
    check("E: FULL sunflower fixture realized inside the gate "
          f"(m = {m} cores, all C(m,2) slopes distinct)", good is not None)
    if good:
        pairs3, rays3, band, Ls, u3, v3 = good
        # Gamma_band = live slopes sharing a band core with another live
        gamma = set()
        for (zc, S) in rays3.items():
            for p, Z in band.items():
                if Z <= S and Ls[p] >= 2:
                    gamma.add(zc)
        N1 = sum(1 for p in band if Ls[p] >= 2)
        ledger = N1 * L1
        check(f"E: N_1 = {m}, |Gamma_band| = C(m,2) = {m*(m-1)//2}, and "
              "master-ledger slack = SUM N_d L(d) / |Gamma_band| EXACTLY "
              "2.000", N1 == m and len(gamma) == m * (m - 1) // 2
              and ledger * 1 == 2 * len(gamma) * 1
              and ledger == N1 * ((n3 - k3 - 1) // (h3 - 1)),
              f"ledger {ledger} vs 2x{len(gamma)}")
        wit3, bad_i3, bad_m3 = t4_battery(row3, pairs3, rays3)
        check("B: T4 on the sunflower fixture (21 shared rays): rigidity "
              "identity everywhere, no double rays",
              wit3 >= 1 and bad_i3 == 0 and bad_m3 == 0,
              f"{wit3} witnessed")
        # D: T7 determinacy
        bad7 = tot7 = 0
        plist = list(band.items())
        for a in range(len(plist)):
            for b in range(a + 1, len(plist)):
                (fa, ga), Za = plist[a]
                (fb, gb), Zb = plist[b]
                for i in range(n3):
                    if i in Za or i in Zb:
                        continue
                    ea = (u3[i] - row3.ev(fa, row3.xs[i])) % q3
                    epa = (v3[i] - row3.ev(ga, row3.xs[i])) % q3
                    eb = (u3[i] - row3.ev(fb, row3.xs[i])) % q3
                    epb = (v3[i] - row3.ev(gb, row3.xs[i])) % q3
                    if epa == 0 or epb == 0:
                        continue
                    za = (-ea) * pow(epa, q3 - 2, q3) % q3
                    zb = (-eb) * pow(epb, q3 - 2, q3) % q3
                    if za == zb:
                        continue
                    tot7 += 1
                    det = (zb - za) % q3
                    ca = (row3.ev(fa, row3.xs[i]) + za
                          * row3.ev(ga, row3.xs[i])) % q3
                    cb = (row3.ev(fb, row3.xs[i]) + zb
                          * row3.ev(gb, row3.xs[i])) % q3
                    vi = (cb - ca) * pow(det, q3 - 2, q3) % q3
                    ui = (ca - za * vi) % q3
                    if ui != u3[i] or vi != v3[i]:
                        bad7 += 1
        check("D: T7 two-column determinacy -- the ordered direction pair "
              "at a coordinate reconstructs (u_i, v_i) exactly",
              tot7 >= 50 and bad7 == 0, f"{tot7} reconstructions, {bad7} bad")

    # ---------------- F: Theorem-6 WARNING bijection on one ray
    (zc0, S0) = next(((zc, S) for (zc, S) in rays.items()
                      if zc[0] not in (0, INF) and len(S) == A),
                     (None, None))
    check("F: a finite-slope exact-A ray exists on the T3 fixture",
          zc0 is not None)
    if zc0:
        z0, c0 = zc0
        Ss = sorted(S0)
        # punctured-code census: codewords g' of C|_{S0} with
        # #{i in S0 : g'(x_i) = v_i} >= k
        punct = set()
        for W in combinations(Ss, k):
            gg = row.interp(W, [vA[i] for i in W])
            if sum(1 for i in Ss if row.ev(gg, row.xs[i]) == vA[i]) >= k:
                punct.add(gg)
        # scanned pairs on the ray side: f = c0 - z0 g and
        # #{i in S0 : g(x_i) = v_i} >= k
        side = set()
        bad_f = 0
        for (f_, g_), Z in pairs.items():
            agrS = sum(1 for i in Ss if row.ev(g_, row.xs[i]) == vA[i])
            if agrS >= k and all(
                    (c0[e] - z0 * g_[e] - f_[e]) % q == 0 for e in range(k)):
                side.add(g_)
                # Z ^ S0 must be exactly the g-agreement inside S0
                if frozenset(i for i in Ss
                             if row.ev(g_, row.xs[i]) == vA[i]) != (Z & S0):
                    bad_f += 1
        check("F: Theorem-6 WARNING bijection -- pairs on the ray "
              "(f = c - zg) correspond EXACTLY to punctured-MDS-list "
              "codewords g' at agreement >= k, with Z_P ^ S = the "
              "g-agreement set", punct == side and bad_f == 0
              and len(punct) >= 1,
              f"{len(punct)} punctured codewords = {len(side)} ray pairs")

    # ---------------- G: six-row pricing pins
    ROWS = [("RowC 1/4", 1024, 256, 5, 828, 764),
            ("RowC 1/8", 1024, 128, 5, 967, 892),
            ("RowC 1/16", 1024, 64, 3, 479, 958),
            ("prize 1/4", 2**41, 2**39, 2**33 + 1, 36839268578566,
             1640677507072),
            ("prize 1/8", 2**41, 2**38, 2**33 + 1, 43010571891409,
             1915555414016),
            ("prize 1/16", 2**41, 2**37, 2**32 + 1, 44764496190275,
             2057289334784)]
    ok_sum = ok_cas = True
    kills = []
    for (name, n_, k_, h_, pin_sum, pin_tan) in ROWS:
        R_ = n_ - k_
        A_ = k_ + h_
        # SUM_{d=1}^{h-2} floor((R-d)/(h-d)) = (h-2) + SUM_{g=2}^{h-1} fl((R-h)/g)
        got = (h_ - 2) + sum_floor_div(R_ - h_, h_ - 1)
        if h_ <= 7:      # brute-force cross-check at RowC scale
            brute = sum((R_ - d) // (h_ - d) for d in range(1, h_ - 1))
            ok_sum &= (brute == got)
        ok_sum &= (got == pin_sum)
        ok_cas &= (R_ - h_ + 1 == n_ - A_ + 1 == pin_tan)
        kills.append(got > pin_tan)
    check("G: band-proper SUM_d L(d) matches the banked pins at ALL SIX "
          "rows (divisor blocks; brute-forced at RowC)", ok_sum)
    check("G: L(h-1) = n - A + 1 EXACTLY on all six rows (cascade "
          "separability -- the printed tangent column is one cascade pair)",
          ok_cas)
    check("G: the printed n-A+1 column is exceeded by SUM L(d) on exactly "
          "5 of 6 rows (all but RowC 1/16) even at N_d = 1 -- the band "
          "column must be a THIRD generic column",
          kills == [True, True, False, True, True, True], str(kills))

    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("XR_BAND_LEDGER_THEOREMS_ALL_PASS")


if __name__ == "__main__":
    main()
