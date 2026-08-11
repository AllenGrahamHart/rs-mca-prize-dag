"""D2(a) -- the K_7-star incidence system (round 32's residual-(i) fence).

The set system (rh_residuals_close/REPORT.md:285-301), m = 2, rho = 7, N = 32,
T = rho+2 = 9, a* = 11:

  W          = {0..10}
  type-1 (2) : S_g = {4,5,6,7,8,9,10},  S_h = {0,1,2,3,8,9,10}     (both in W)
  type-2 (7) : vertex stars of K_7 on the 21 outside points, star_j
               additionally containing the W-point j, j = 0..6.

DERIVED PREDICTION (registered in this file BEFORE running it).

At a = a* = 11 the shortened apolarity code K'|_W has deg_x H <= a-(4m+2) = 1,
so H(Z,x) = H_0(Z) + x H_1(Z) with deg_Z <= m+1 = 3.

  * x in {8,9,10} have A_x = {g,h}: (Z-g)(Z-h) | H_0 + x H_1 at three distinct
    x; the map x |-> (H_0 + xH_1 mod (Z-g)(Z-h)) is AFFINE in x, so it vanishes
    identically:  H = (Z-g)(Z-h) G(Z,x),  G of bidegree (1,1).
  * x in {0,1,2,3} have A_x = {h, s_x}; x in {4,5,6} have A_x = {g, s_x}.  In
    both cases s_x is distinct from g and h, so (Z - s_x) | G(Z,x).
  * x = 7 has A_7 = {g} (the UNSATURATED point, d_7 = 1 < m): no condition.

So the whole system collapses to  G(s_x, x) = 0 for x = 0..6, with
G(Z,x) = A + BZ + Cx + DZx.  That is exactly:

  *** the K_7-star is bivariately consistent IFF the 7 (W-point, private-slope)
      pairs (w_x, s_x) lie on a (1,1)-curve, i.e. IFF x |-> s_x is the
      restriction of a MOBIUS transformation. ***

and then mu(x) = g on {0,1,2,3}, mu(x) = h on {4,5,6,7}, mu(x) = Mobius image
on {8,9,10}.  Predictions tested below:
  (P-a) random embedding  -> nullity 0 (killed)
  (P-b) Mobius embedding  -> nullity >= 1, with a kernel vector all of whose
        (alpha_x, beta_x) are nonzero, and the mu-pattern above.
"""

import random
import sys

sys.path.insert(0, "notes/pilots_20260811/rh_bivariate_system")
from biv_core import build_S1, build_S2, mu_N, primes_one_mod

out = []
P = out.append
P("=" * 74)
P("D2(a) -- K_7-STAR INCIDENCE SYSTEM, BIVARIATE REALIZABILITY (m=2, a*=11)")
P("=" * 74)

m = 2
rho, N, T, a = 4 * m - 1, 16 * m, 4 * m + 1, 11
Wab = list(range(11))
Sg = {4, 5, 6, 7, 8, 9, 10}
Sh = {0, 1, 2, 3, 8, 9, 10}
stars = [
    {0, 11, 12, 13, 14, 15, 16},
    {1, 11, 17, 18, 19, 20, 21},
    {2, 12, 17, 22, 23, 24, 25},
    {3, 13, 18, 22, 26, 27, 28},
    {4, 14, 19, 23, 26, 29, 30},
    {5, 15, 20, 24, 27, 29, 31},
    {6, 16, 21, 25, 28, 30, 31},
]
blocks = [Sg, Sh] + stars

# ------------------------------------------------- independent axiom re-check
P("")
P("[A] independent re-check of the fence's own axioms (my code, not theirs)")
sizes = sorted(len(b) for b in blocks)
dx = {x: sum(1 for b in blocks if x in b) for x in range(N)}
pair_un = min(len(b1 | b2) for i, b1 in enumerate(blocks) for b2 in blocks[i + 1:])
pair_int = max(len(b1 & b2) for i, b1 in enumerate(blocks) for b2 in blocks[i + 1:])
spend = {i: len(b - set(Wab)) for i, b in enumerate(blocks)}
P("    T = %d blocks (rho+2 = %d)         : %s" % (len(blocks), T, len(blocks) == T))
P("    all |S| = rho = %d                : %s" % (rho, sizes[0] == sizes[-1] == rho))
P("    max d_x = %d (= e = m = %d)        : %s" % (max(dx.values()), m, max(dx.values()) == m))
P("    sum_x (e - d_x) = %d  (= 1+O, O=0) : %s" % (sum(m - dx[x] for x in range(N)),
                                                   sum(m - dx[x] for x in range(N)) == 1))
P("    min pair union = %d (= a*)         : %s" % (pair_un, pair_un == a))
P("    max pair overlap = %d (= 2rho-a)   : %s" % (pair_int, pair_int == 2 * rho - a))
P("    min type-2 spend = %d (= s = rho-a+... ), all type-2 spends: %s"
  % (min(spend[i] for i in range(2, 9)), sorted(spend[i] for i in range(2, 9))))
P("    type-1 blocks inside W            : %s" % (Sg <= set(Wab) and Sh <= set(Wab)))
Amap_ab = {x: [i for i, b in enumerate(blocks) if x in b] for x in Wab}
P("    A_x (abstract, 0=g 1=h 2..8=stars): %s"
  % {x: Amap_ab[x] for x in Wab})
P("    the UNSATURATED point of W is x=7 with d_7 = %d < m = %d" % (dx[7], m))
P("    X_gamma = |S_gamma ^ W| : %s" % [len(b & set(Wab)) for b in blocks])

# ---------------------------------------------------------------- experiments
def run(q, seed, mode, use_extra):
    """mode: 'random' or 'mobius'.  returns (nullity, ncols, kernel_ok, mu_ok)"""
    D = mu_N(q, N)
    rnd = random.Random(seed)
    while True:
        Wv = rnd.sample(D, 11)
        if mode == "random":
            sl = rnd.sample([v for v in range(q)], 9)
            g, h = sl[0], sl[1]
            svals = sl[2:]
        else:
            # Mobius mu(x) = (p x + r) / (s x + t), pt - rs != 0
            for _ in range(200):
                p, r, s, t = [rnd.randrange(q) for _ in range(4)]
                if (p * t - r * s) % q == 0:
                    continue
                den = [(s * w + t) % q for w in Wv]
                if 0 in den:
                    continue
                img = [(p * w + r) * pow((s * w + t) % q, q - 2, q) % q for w in Wv]
                if len(set(img)) != 11:
                    continue
                break
            else:
                return None
            svals = img[:7]
            cand = [v for v in range(q) if v not in set(img)]
            if len(cand) < 2:
                return None
            g, h = rnd.sample(cand, 2)
        slope_of = {0: g, 1: h}
        for j in range(7):
            slope_of[2 + j] = svals[j]
        if len(set(slope_of.values())) != 9:
            continue
        break
    Amap = {Wv[x]: [slope_of[i] for i in Amap_ab[x]] for x in Wab}
    extra = {Wv[7]: 1} if use_extra else None
    pr, cols, ncols, nrows, _, _ = build_S2(m, q, Wv, Amap, extra=extra)
    nul = ncols - pr.rank
    kernel_ok, mu_pat = None, None
    if nul > 0:
        kb = pr.kernel_basis()
        # look for a kernel vector with (alpha_x,beta_x) != (0,0) for every x
        best = None
        for _ in range(60):
            v = [0] * ncols
            for b in kb:
                c = rnd.randrange(q)
                v = [(vi + c * bi) % q for vi, bi in zip(v, b)]
            byx = {}
            for ci, (x, kind, tt) in enumerate(cols):
                byx.setdefault(x, []).append(v[ci])
            if all(any(z for z in vals) for vals in byx.values()):
                best = (v, byx)
                break
        kernel_ok = best is not None
        if best:
            v, byx = best
            mu_pat = {}
            for x in Wv:
                cc = [v[ci] for ci, (xx, kd, tt) in enumerate(cols) if xx == x]
                if len(cc) == 2:
                    a0, a1 = cc[0], cc[1]   # a1*Z*pi + a0*pi = (a1 Z + a0) pi
                    mu_pat[x] = "inf" if a1 == 0 else (-a0) * pow(a1, q - 2, q) % q
                else:
                    mu_pat[x] = "unsat:" + ",".join(str(z) for z in cc)
    return nul, ncols, kernel_ok, mu_pat, {"g": g, "h": h, "W": Wv, "s": svals}


P("")
P("[B] RANDOM embeddings: W -> mu_32, slopes -> F_q uniformly")
P("    (each row: nullity of S2 over 60 independent embeddings)")
for q in (97, 193):
    for use_extra in (False, True):
        nuls = []
        for k in range(60):
            r = run(q, 700000 + 137 * k + q + (5 if use_extra else 0), "random", use_extra)
            nuls.append(r[0])
        ncols = r[1]
        hist = {}
        for n in nuls:
            hist[n] = hist.get(n, 0) + 1
        adm = sum(1 for k in range(60)
                  if run(q, 700000 + 137 * k + q + (5 if use_extra else 0),
                         "random", use_extra)[2])
        P("    q=%-4d unsat-slack-at-x=7 %-5s unknowns=%2d  nullity histogram %s"
          "   admissible (all-coords-nonzero) kernel: %d/60"
          % (q, str(use_extra), ncols, dict(sorted(hist.items())), adm))

P("")
P("[C] MOBIUS embeddings: s_x = M(w_x) for a random Mobius M")
for q in (97, 193):
    for use_extra in (False, True):
        nuls, kok = [], []
        for k in range(40):
            r = run(q, 900000 + 211 * k + q + (5 if use_extra else 0), "mobius", use_extra)
            if r is None:
                continue
            nuls.append(r[0])
            kok.append(r[2])
        hist = {}
        for n in nuls:
            hist[n] = hist.get(n, 0) + 1
        P("    q=%-4d unsat-slack-at-x=7 %-5s nullity histogram %s   all-coords-nonzero kernel: %d/%d"
          % (q, str(use_extra), dict(sorted(hist.items())),
             sum(1 for z in kok if z), len(kok)))

P("")
P("[D] one MOBIUS solution in full: the recovered fibre map mu")
r = run(97, 4242, "mobius", True)
nul, ncols, kok, mupat, dat = r
P("    q=97  nullity=%d  unknowns=%d  all-nonzero kernel: %s" % (nul, ncols, kok))
Wv = dat["W"]
P("    g=%d h=%d   s_0..s_6 = %s" % (dat["g"], dat["h"], dat["s"]))
if mupat:
    lab = {}
    for idx, x in enumerate(Wv):
        v = mupat[x]
        if v == dat["g"]:
            v = "g"
        elif v == dat["h"]:
            v = "h"
        lab[idx] = v
    P("    recovered mu(x) by ABSTRACT W-index: %s" % lab)
    P("    PREDICTED                          : "
      "{0:'g',1:'g',2:'g',3:'g',4:'h',5:'h',6:'h',7:'h',8:M,9:M,10:M}")
    ok = all(lab[i] == "g" for i in (0, 1, 2, 3)) and all(
        lab[i] == "h" for i in (4, 5, 6))
    P("    mu = g on F_g = W\\S_g = {0,1,2,3} and mu = h on {4,5,6}: %s" % ok)

P("")
P("[E] MANDATE FORM S1 (mu given as data, a unknowns) at the Mobius embedding")
for q in (97, 193):
    D = mu_N(q, N)
    rnd = random.Random(5150 + q)
    r = run(q, 5150 + q, "mobius", True)
    if r is None:
        continue
    dat = r[4]
    Wv, g, h, sv = dat["W"], dat["g"], dat["h"], dat["s"]
    slope_of = {0: g, 1: h}
    for j in range(7):
        slope_of[2 + j] = sv[j]
    Amap = {Wv[x]: [slope_of[i] for i in Amap_ab[x]] for x in Wab}
    mumap = {}
    for x in Wab:
        if x in (0, 1, 2, 3):
            mumap[Wv[x]] = g
        elif x in (4, 5, 6, 7):
            mumap[Wv[x]] = h
        else:
            mumap[Wv[x]] = None  # unknown; try infinity and a sweep below
    # sweep the three free mu values over F_q for x in {8,9,10}: use the S2
    # kernel instead -- here just report S1 with mu = predicted Mobius image
    best = None
    for trial in range(1):
        mm = dict(mumap)
        for x in (8, 9, 10):
            mm[Wv[x]] = None
        pr, cols, aa, nrows = build_S1(m, q, Wv, Amap, mm)
        best = aa - pr.rank
    P("    q=%-4d S1 unknowns=%d  nullity with mu=(g,g,g,g,h,h,h,h,inf,inf,inf) = %d"
      % (q, aa, best))

P("")
P("=" * 74)
print("\n".join(out))
with open("notes/pilots_20260811/rh_bivariate_system/d2a_k7star_results.txt", "w") as f:
    f.write("\n".join(out) + "\n")
