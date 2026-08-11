"""D3 -- THE CONSISTENCY RELATIONS, and the decisive constructive test.

CORRECTION TO D2(c) (reported as a miss).  At the CANONICAL W = S_g u S_h the
banked FR-canonical bound
    |S_gamma ^ W| <= 4rho - 2a - 2o_gamma - o_g - o_h = 2m-2
(rh_fr_algebraic/REPORT.md:95-104; node rate_half_fr_canonical_min_pair_union_bound)
is STRICTLY STRONGER than the (C2) cap 3m-3 used by d2c_random.py.  Worse, it
comes with a SIDE-SPLIT: (OV) forces |S_gamma ^ S_g| <= 2rho - a = m-1 and
|S_gamma ^ S_h| <= m-1 separately.  d2c's generator used the (C2) cap only, so
part of its data was NOT admissible.  Re-run with the correct caps below.

THE TIGHTNESS (new, and the reason the structure is nearly forced):
  g-side type-2 demand  = 3m(m-1) + (m-1)(m-2) = (m-1)(4m-2)
  g-side type-2 capacity= (4m-1)(m-1)
  slack                 = (m-1)  -- i.e. all but m-1 of the 4m-1 type-2 slopes
  carry EXACTLY m-1 points of S_g and EXACTLY m-1 points of S_h.

THE REDUCED SYSTEM (verified in d2c, 120/120):
  H = (Z-g)(Z-h) G,  deg_x G <= 3m-3, deg_Z G <= m-1, and for x in W
      G(.,x) = c_x prod_{gamma in A_x\\{g,h}} (Z-gamma) [ * (Z-mu(x)) if x in S_g^S_h ]

so the consistency relation is exactly:

  *** (BIV-CURVE)  the map  x |-> [ prod_{gamma in A_x^2} (Z-gamma) ]  in P^{m-1}
      must be the restriction to W of a rational curve of degree <= 3m-3. ***

At m = 2 that reads: x |-> s_x must be a degree-<= 3 rational map F -> P^1, i.e.
the type-2 slope classes on W must be FIBRES of a degree-3 rational map -- and
since (OV) caps each class at one S_g-point and one S_h-point, the classes are
2-element fibres, i.e. a PERFECT MATCHING between S_g\\S_h and S_h\\S_g
realised by a degree-3 map.  That is constructible: see [B].
"""

import random
import sys

sys.path.insert(0, "notes/pilots_20260811/rh_bivariate_system")
from biv_core import build_S2, mu_N, primes_one_mod

out = []
P = out.append
P("=" * 78)
P("D3 -- CONSISTENCY RELATIONS AND THE CONSTRUCTIVE TEST")
P("=" * 78)

P("")
P("[A] the corrected admissible generator (caps 2m-2 overall, m-1 per side)")
P("")
P("   m  type-2 demand  g-side demand  g-side capacity  slack   (predicted (m-1))")
for m in (2, 3, 4, 8, 64):
    dem = 7 * m * m - 9 * m + 2
    gdem = (m - 1) * (4 * m - 2)
    gcap = (4 * m - 1) * (m - 1)
    P("  %3d  %13d  %13d  %15d  %5d   %s"
      % (m, dem, gdem, gcap, gcap - gdem, "OK" if gcap - gdem == m - 1 else "MISMATCH"))


def admissible(m, rnd, tries=400):
    """canonical W = S_g u S_h with the CORRECT caps; returns A2 per abstract x."""
    inter = list(range(m - 1))
    gonly = list(range(m - 1, 4 * m - 1))
    honly = list(range(4 * m - 1, 7 * m - 1))
    T2 = list(range(4 * m - 1))
    for _ in range(tries):
        capg = {t: m - 1 for t in T2}
        caph = {t: m - 1 for t in T2}
        A2 = {}
        ok = True
        order = inter + gonly + honly
        rnd.shuffle(order)
        for x in order:
            need = m - (2 if x in inter else 1)
            ing = x in inter or x in gonly
            inh = x in inter or x in honly
            avail = [t for t in T2
                     if (not ing or capg[t] > 0) and (not inh or caph[t] > 0)]
            if len(avail) < need:
                ok = False
                break
            pick = rnd.sample(avail, need)
            for t in pick:
                if ing:
                    capg[t] -= 1
                if inh:
                    caph[t] -= 1
            A2[x] = pick
        if ok:
            return {"m": m, "inter": set(inter), "gonly": set(gonly),
                    "honly": set(honly), "A2": A2}
    return None


P("")
P("[A2] nullity of S2 on CORRECTLY admissible random data, random embeddings")
P("   m    q    unknowns  equations   nullity histogram (20 embeddings)   max X_gamma (cap 2m-2)")
for m in (2, 3, 4):
    N = 16 * m
    for q in primes_one_mod(N, count=2, limit=4000)[:2]:
        D = mu_N(q, N)
        nn, mx = [], 0
        for trial in range(20):
            rnd = random.Random(12000 + 37 * trial + q + m)
            dat = admissible(m, rnd)
            if dat is None:
                continue
            a = 7 * m - 1
            Wv = rnd.sample(D, a)
            sv = rnd.sample(range(1, q), 4 * m + 1)
            sg, sh = sv[0], sv[1]
            tv = sv[2:]
            Amap = {}
            cnt = {t: 0 for t in range(4 * m - 1)}
            for xi, x in enumerate(Wv):
                A = []
                if xi in dat["inter"] or xi in dat["gonly"]:
                    A.append(sg)
                if xi in dat["inter"] or xi in dat["honly"]:
                    A.append(sh)
                for t in dat["A2"][xi]:
                    A.append(tv[t])
                    cnt[t] += 1
                Amap[x] = A
            mx = max(mx, max(cnt.values()))
            pr, cols, nc, nrows, T, _ = build_S2(m, q, Wv, Amap)
            nn.append(nc - pr.rank)
        h = {}
        for v in nn:
            h[v] = h.get(v, 0) + 1
        P("  %2d  %4d  %8d  %9d   %-32s  %d (cap %d)"
          % (m, q, nc, (m + 2) * (4 * m + 1), str(dict(sorted(h.items()))), mx, 2 * m - 2))

# --------------------------------------------------------------- CONSTRUCTIVE
P("")
P("[B] CONSTRUCTIVE TEST at m = 2, a = 7m-1 = 13: search a degree-3 rational")
P("    map phi = -A/B on mu_32 with >= 6 disjoint 2-element fibres, build the")
P("    full admissible configuration from them, and test the bivariate system.")


def cubic_eval(c, x, q):
    v = 0
    for co in reversed(c):
        v = (v * x + co) % q
    return v


def search_config(q, seed, trials=250000):
    m = 2
    N = 32
    D = mu_N(q, N)
    rnd = random.Random(seed)
    best = None
    for _ in range(trials):
        A = [rnd.randrange(q) for _ in range(4)]
        B = [rnd.randrange(q) for _ in range(4)]
        fib = {}
        bad = False
        for x in D:
            bx = cubic_eval(B, x, q)
            ax = cubic_eval(A, x, q)
            if bx == 0:
                if ax == 0:
                    bad = True
                    break
                continue  # phi(x) = infinity, not a finite slope
            s = (-ax) * pow(bx, q - 2, q) % q
            fib.setdefault(s, []).append(x)
        if bad:
            continue
        pairs = [(s, v[:2]) for s, v in fib.items() if len(v) >= 2]
        if len(pairs) >= 6:
            best = (A, B, pairs[:6], D)
            break
    return best


for q in (97, 193):
    res = search_config(q, 424242 + q)
    if res is None:
        P("    q=%d : no configuration found in the budget (reported as a MISS)" % q)
        continue
    A, B, pairs, D = res
    used = [x for _, pr_ in pairs for x in pr_]
    gam = [s for s, _ in pairs]
    rest = [x for x in D if x not in used]
    w13 = rest[0]
    Wv = used + [w13]
    # the 7th type-2 slope, and the two type-1 slopes: any values not yet used
    forbid = set(gam)
    spare = [v for v in range(1, q) if v not in forbid]
    rnd = random.Random(99 + q)
    rnd.shuffle(spare)
    g7, sg, sh = spare[0], spare[1], spare[2]
    slopes = gam + [g7, sg, sh]
    Amap = {}
    Sg, Sh = set(), set()
    for i, (s, pr_) in enumerate(pairs):
        u, v = pr_
        Amap[u] = [sg, s]
        Amap[v] = [sh, s]
        Sg.add(u)
        Sh.add(v)
    Amap[w13] = [sg, sh]
    Sg.add(w13)
    Sh.add(w13)
    pr, cols, nc, nrows, T, _ = build_S2(2, q, Wv, Amap)
    nul = nc - pr.rank
    # admissibility of the W-side
    okX = all(sum(1 for x in Wv if s in Amap[x]) <= 2 for s in gam)
    P("")
    P("    q=%d  |Z|=%d distinct slopes: %s" % (q, len(set(slopes)), len(set(slopes)) == 9))
    P("    |W|=%d=7m-1  |S_g|=%d  |S_h|=%d  (rho=%d)  |S_g^S_h|=%d (=m-1)  S_g u S_h = W : %s"
      % (len(Wv), len(Sg), len(Sh), 4 * 2 - 1, len(Sg & Sh), (Sg | Sh) == set(Wv)))
    P("    every |A_x| = m = 2 : %s   X_gamma <= 2m-2 = 2 for all type-2 : %s"
      % (all(len(Amap[x]) == 2 for x in Wv), okX))
    P("    |S_gamma ^ S_g ^ W| <= m-1 = 1 : %s ; |S_gamma ^ S_h ^ W| <= 1 : %s"
      % (all(sum(1 for x in Sg if s in Amap[x]) <= 1 for s in gam),
         all(sum(1 for x in Sh if s in Amap[x]) <= 1 for s in gam)))
    P("    >>> BIVARIATE SYSTEM: unknowns %d, equations %d, rank %d, NULLITY %d"
      % (nc, (2 + 2) * (4 * 2 + 1), pr.rank, nul))
    if nul > 0:
        kb = pr.kernel_basis()
        adm = False
        rr = random.Random(7)
        for _ in range(80):
            vv = [0] * nc
            for b in kb:
                c = rr.randrange(q)
                vv = [(a1 + c * b1) % q for a1, b1 in zip(vv, b)]
            byx = {}
            for ci, (x, kind, t) in enumerate(cols):
                byx.setdefault(x, []).append(vv[ci])
            if all(any(z for z in val) for val in byx.values()):
                adm = True
                break
        P("    >>> kernel vector with (alpha_x,beta_x) != (0,0) for EVERY x in W : %s" % adm)
    P("    the 6 slope classes are the 2-element fibres of phi = -A/B,")
    P("    A = %s , B = %s (coefficients, ascending)" % (A, B))

# ------------------------------------------------------------ FIRST MOMENT
P("")
P("[C] FIRST-MOMENT count (HEURISTIC -- assumes the structured system behaves")
P("    like a random one; calibrated against the K_7-star, where it is EXACT)")
P("")
P("    #(embeddings x slope tuples x admissible incidences) x Pr[nonzero kernel]")
P("    log2 E ~ E_comb + (4m-1)log2 q + log2(N!/(N-a)!) - (4m^2-7m+3) log2 q")
P("")
P("      m      q       E_comb   slopeterm   Wterm    deficit+1    log2 E")
import math
for (m, q) in [(2, 97), (3, 97), (4, 193), (8, 129), (16, 257), (64, 1025),
               (64, 12289), (2 ** 37, 2 ** 167)]:
    N, a = 16 * m, 7 * m - 1
    # E_comb: 6m points choose m-1 of 4m-1 slopes, (m-1) points choose m-2
    def lc(n, k):
        if k < 0 or k > n:
            return 0.0
        return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)) / math.log(2)
    ecomb = 6 * m * lc(4 * m - 1, m - 1) + (m - 1) * lc(4 * m - 1, m - 2)
    lq = math.log2(q)
    wterm = min(a, N) * math.log2(N)
    defp = 4 * m * m - 7 * m + 3
    tot = ecomb + (4 * m - 1) * lq + wterm - defp * lq
    P("   %7s %8s  %11.1f  %10.1f  %7.1f  %11d  %12.1f  %s"
      % (m if m < 1000 else "2^37", q if q < 10 ** 6 else "2^167",
         ecomb, (4 * m - 1) * lq, wterm, defp, tot,
         "solutions EXPECTED" if tot > 0 else "NONE expected"))

P("")
P("=" * 78)
print("\n".join(out))
with open("notes/pilots_20260811/rh_bivariate_system/d3_consistency_results.txt", "w") as f:
    f.write("\n".join(out) + "\n")
