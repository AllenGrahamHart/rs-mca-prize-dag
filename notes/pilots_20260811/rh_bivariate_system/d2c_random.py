"""D2(c) -- random ADMISSIBLE incidence data at the banked evaluation point
a = w* = a* = 7m-1, T = rho+2 = 4m+1, plus a direct test of the type-1
REDUCTION derived in D1/D3.

CANONICAL admissible shape at a = 7m-1 (this is round 32's W = minimising pair
union, rh_fr_algebraic/REPORT.md:95-104):
  S_g, S_h  type-1, both inside W, |S_g| = |S_h| = rho = 4m-1,
  S_g u S_h = W  (so |S_g ^ S_h| = 2rho - a = m-1),  hence T_1 = 2
  (banked: floor(a/(a-rho)) = 2 is the (AO1) first term at a >= 6m-1).
  Every x in W therefore already carries 1 or 2 type-1 slopes, and needs
  m - |A_x ^ {g,h}| further type-2 slopes; every type-2 slope obeys the banked
  (C2) cap X_gamma <= a - n_gamma - (R-r+1) <= 3m-3.

REDUCTION (derived, tested here).  X_g = X_h = rho = 4m-1 > 3m-3 = deg_x H, so
h_g = H(g,.) and h_h = H(h,.) vanish identically:  H = (Z-g)(Z-h) G  with

        deg_x G <= 3m-3,   deg_Z G <= m-1,
        G(.,x) = c_x prod_{gamma in A_x \\ {g,h}} (Z-gamma)   for x in S_g D S_h
        G(.,x) = c_x prod_{A_x\\{g,h}} (Z-gamma)(Z-mu(x))     for x in S_g ^ S_h

so the system is EXACTLY: 7m^2-9m+2 vanishing conditions on the 3m^2-2m
coefficients of G.  Deficit 4m^2-7m+2.  Predicted: nullity(S2) == nullity(G).
"""

import random
import sys

sys.path.insert(0, "notes/pilots_20260811/rh_bivariate_system")
from biv_core import PackedRank, build_S2, mu_N, primes_one_mod

out = []
P = out.append
P("=" * 78)
P("D2(c) -- RANDOM ADMISSIBLE INCIDENCE AT a = 7m-1, AND THE TYPE-1 REDUCTION")
P("=" * 78)


def canonical_incidence(m, rnd, unsat=0):
    """abstract admissible data; returns (Wab, Sg, Sh, A2 (type-2 slopes per x))"""
    a = 7 * m - 1
    inter = list(range(m - 1))
    gonly = list(range(m - 1, 4 * m - 1))          # S_g \ S_h , 3m points
    honly = list(range(4 * m - 1, 7 * m - 1))      # S_h \ S_g , 3m points
    Sg, Sh = set(inter) | set(gonly), set(inter) | set(honly)
    assert len(Sg) == len(Sh) == 4 * m - 1 and len(Sg | Sh) == a
    T2 = list(range(4 * m - 1))                    # type-2 slope labels
    cap = {t: 3 * m - 3 for t in T2}
    need = {}
    for x in range(a):
        k = 2 if x in inter else 1                 # |A_x ^ {g,h}|
        need[x] = m - k
    # take `unsat` points of W down by one incidence (d_x = m-1)
    order = list(range(a))
    rnd.shuffle(order)
    lowered = set()
    for x in order:
        if len(lowered) >= unsat:
            break
        if need[x] > 0:
            need[x] -= 1
            lowered.add(x)
    A2 = {}
    for x in sorted(range(a), key=lambda z: -need[z]):
        avail = [t for t in T2 if cap[t] > 0]
        if len(avail) < need[x]:
            return None
        pick = rnd.sample(avail, need[x])
        for t in pick:
            cap[t] -= 1
        A2[x] = pick
    return Wab_pack(m, Sg, Sh, A2, lowered)


def Wab_pack(m, Sg, Sh, A2, lowered):
    return {"m": m, "a": 7 * m - 1, "Sg": Sg, "Sh": Sh, "A2": A2, "low": lowered}


def build_G_system(dat, q, Wv, slope_val):
    """the reduced system on G: bidegree (3m-3, m-1)."""
    m = dat["m"]
    dz, dx = m - 1, 3 * m - 3
    cols = [(i, j) for i in range(dx + 1) for j in range(dz + 1)]
    nc = len(cols)
    pr = PackedRank(nc, q)
    rows = []
    for xi, x in enumerate(Wv):
        for t in dat["A2"][xi]:
            g = slope_val["t%d" % t]
            xp = [1] * (dx + 1)
            for i in range(1, dx + 1):
                xp[i] = xp[i - 1] * x % q
            gp = [1] * (dz + 1)
            for j in range(1, dz + 1):
                gp[j] = gp[j - 1] * g % q
            rows.append([xp[i] * gp[j] % q for (i, j) in cols])
    random.Random(5).shuffle(rows)
    for r in rows:
        if pr.rank == nc:
            break
        pr.add_row(r)
    return pr.rank, nc, len(rows)


P("")
P("      predicted counts:  G-unknowns 3m^2-2m ; G-conditions 7m^2-9m+2 ;"
  " deficit 4m^2-7m+2")
P("")
P("   m    q    a   T  S2-unknowns  S2-eqns  S2-rank  S2-null | G-unk  G-cond  G-rank  G-null")
for m in (2, 3, 4):
    N = 16 * m
    for q in primes_one_mod(N, count=2, limit=4000)[:2]:
        D = mu_N(q, N)
        s2n, gn = [], []
        for trial in range(20):
            rnd = random.Random(4000 + 91 * trial + q + m)
            dat = canonical_incidence(m, rnd)
            if dat is None:
                continue
            a = dat["a"]
            Wv = rnd.sample(D, a)
            sv = rnd.sample(range(1, q), 4 * m + 1)
            slope_val = {"g": sv[0], "h": sv[1]}
            for t in range(4 * m - 1):
                slope_val["t%d" % t] = sv[2 + t]
            Amap = {}
            for xi, x in enumerate(Wv):
                A = []
                if xi in dat["Sg"]:
                    A.append(slope_val["g"])
                if xi in dat["Sh"]:
                    A.append(slope_val["h"])
                A += [slope_val["t%d" % t] for t in dat["A2"][xi]]
                Amap[x] = A
            pr, cols, nc, nrows, T, _ = build_S2(m, q, Wv, Amap)
            s2n.append((nc, nrows, pr.rank, nc - pr.rank))
            rk, gnc, gcond = build_G_system(dat, q, Wv, slope_val)
            gn.append((gnc, gcond, rk, gnc - rk))
        agree = sum(1 for s, g in zip(s2n, gn) if s[3] == g[3])
        s = s2n[0]
        g = gn[0]
        P("  %2d  %4d  %3d  %2d  %11d  %7d  %7d  %7d | %5d  %6d  %6d  %6d"
          % (m, q, 7 * m - 1, 4 * m + 1, s[0], (m + 2) * (4 * m + 1), s[2], s[3],
             g[0], g[1], g[2], g[3]))
        hs = {}
        for x in s2n:
            hs[x[3]] = hs.get(x[3], 0) + 1
        hg = {}
        for x in gn:
            hg[x[3]] = hg.get(x[3], 0) + 1
        P("        20 embeddings: S2 nullity hist %s ; G nullity hist %s ;"
          " S2-null == G-null in %d/%d"
          % (dict(sorted(hs.items())), dict(sorted(hg.items())), agree, len(s2n)))
        P("        predicted G-unknowns %d, G-conditions %d, deficit %d"
          % (3 * m * m - 2 * m, 7 * m * m - 9 * m + 2, 4 * m * m - 7 * m + 2))

P("")
P("[B] the UNSATURATED exception: give k points of W degree d_x = m-1 and one")
P("    extra free root each (1+O <= m of them are allowed)")
P("")
P("   m    q   unsat k   S2-unknowns   nullity histogram over 12 embeddings")
for m in (2, 3, 4):
    N = 16 * m
    q = primes_one_mod(N, count=1, limit=4000)[0]
    D = mu_N(q, N)
    for k in range(0, m + 1):
        nn = []
        for trial in range(12):
            rnd = random.Random(6000 + 71 * trial + q + m + 3 * k)
            dat = canonical_incidence(m, rnd, unsat=k)
            if dat is None:
                continue
            a = dat["a"]
            Wv = rnd.sample(D, a)
            sv = rnd.sample(range(1, q), 4 * m + 1)
            slope_val = {"g": sv[0], "h": sv[1]}
            for t in range(4 * m - 1):
                slope_val["t%d" % t] = sv[2 + t]
            Amap, extra = {}, {}
            for xi, x in enumerate(Wv):
                A = []
                if xi in dat["Sg"]:
                    A.append(slope_val["g"])
                if xi in dat["Sh"]:
                    A.append(slope_val["h"])
                A += [slope_val["t%d" % t] for t in dat["A2"][xi]]
                Amap[x] = A
                if xi in dat["low"]:
                    extra[x] = 1
            pr, cols, nc, nrows, T, _ = build_S2(m, q, Wv, Amap, extra=extra)
            nn.append(nc - pr.rank)
        h = {}
        for v in nn:
            h[v] = h.get(v, 0) + 1
        P("  %2d  %4d   %3d      %8d   %s" % (m, q, k, nc, dict(sorted(h.items()))))

P("")
P("[C] FULLY random (non-admissible) A_x of size m, for contrast")
P("   m    q   nullity histogram over 20 embeddings")
for m in (2, 3, 4):
    N = 16 * m
    q = primes_one_mod(N, count=1, limit=4000)[0]
    D = mu_N(q, N)
    nn = []
    for trial in range(20):
        rnd = random.Random(8000 + 53 * trial + q + m)
        a = 7 * m - 1
        Wv = rnd.sample(D, a)
        sv = rnd.sample(range(1, q), 4 * m + 1)
        Amap = {x: rnd.sample(sv, m) for x in Wv}
        pr, cols, nc, nrows, T, _ = build_S2(m, q, Wv, Amap)
        nn.append(nc - pr.rank)
    h = {}
    for v in nn:
        h[v] = h.get(v, 0) + 1
    P("  %2d  %4d   %s" % (m, q, dict(sorted(h.items()))))

P("")
P("=" * 78)
print("\n".join(out))
with open("notes/pilots_20260811/rh_bivariate_system/d2c_random_results.txt", "w") as f:
    f.write("\n".join(out) + "\n")
