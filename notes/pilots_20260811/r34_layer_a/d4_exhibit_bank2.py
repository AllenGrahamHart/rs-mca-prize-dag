"""D4 -- THE EXHIBIT.

An m = 2 configuration at the banked evaluation point a = w* = a* = 7m-1 = 13,
with T = rho+2 = 9 (the (SAT3) failure size), which satisfies

  (i)  EVERY banked incidence axiom (block sizes rho, d_x <= e, the exact
       saturation deficit sum_x(m-d_x) = 1+O with O <= m-1, pairwise unions
       >= a = w*, W = S_g u S_h a MINIMISING pair union, the (C2) spend floor,
       and the proved FR-canonical cap X_gamma <= 2m-2), and
  (ii) THE BIVARIATE REALIZABILITY SYSTEM of this pilot: the (m+2)(4m+1) = 36
       linear conditions have a nonzero solution whose every coordinate
       (alpha_x, beta_x) is nonzero, i.e. a legitimate Psi.

Structure (all forced by D3):
  * phi = -A/B a degree-3 rational map; the type-2 slope of x in W is phi(x).
  * 5 two-point fibres (one point in S_g\\S_h, one in S_h\\S_g) + 2 one-point
    fibres = 12 points; w13 = S_g ^ S_h carries no type-2 slope.
  * outside W: 19 points realise K_7 minus the matching {(2,3),(4,5),(6,7)}
    (18 edges = 18 points of degree 2) plus ONE point of degree 1 on block 7.
    Block outside-sizes 6,5,5,5,5,5,6 -> all 7 type-2 blocks have size rho = 7.
"""

import random
import sys

sys.path.insert(0, "notes/pilots_20260811/rh_bivariate_system")
from biv_core import build_S2, mu_N

out = []
P = out.append
P("=" * 78)
P("D4 -- EXHIBIT: an m=2, T=rho+2, a=7m-1 configuration that the bivariate")
P("      realizability system does NOT kill")
P("=" * 78)

m, N, rho, T, a, R = 2, 32, 7, 9, 13, 16


def cev(c, x, q):
    v = 0
    for co in reversed(c):
        v = (v * x + co) % q
    return v


def build(q, seed, trials=400000):
    D = mu_N(q, N)
    Dset = set(D)
    rnd = random.Random(seed)
    for _ in range(trials):
        A = [rnd.randrange(q) for _ in range(4)]
        B = [rnd.randrange(q) for _ in range(4)]
        phi, bad = {}, False
        for x in D:
            bx, ax = cev(B, x, q), cev(A, x, q)
            if bx == 0:
                if ax == 0:
                    bad = True
                    break
                continue
            phi[x] = (-ax) * pow(bx, q - 2, q) % q
        if bad or len(phi) < 14:
            continue
        fib = {}
        for x, s in phi.items():
            fib.setdefault(s, []).append(x)
        twos = [(s, v) for s, v in fib.items() if len(v) == 2]
        ones = [(s, v) for s, v in fib.items() if len(v) == 1]
        if len(twos) < 5 or len(ones) < 3:
            continue
        pairs = twos[:5]
        sing = ones[:2]
        w13 = ones[2][1][0]
        used = [x for _, v in pairs for x in v] + [v[0] for _, v in sing]
        W = used + [w13]
        if len(set(W)) != a:
            continue
        gam = [s for s, _ in pairs] + [s for s, _ in sing]      # 7 type-2 slopes
        if len(set(gam)) != 7:
            continue
        vals = set(phi[x] for x in W)
        cand = [v for v in range(1, q) if v not in vals]
        if len(cand) < 2:
            continue
        rnd.shuffle(cand)
        g, h = cand[0], cand[1]
        # sides: pairs give one S_g point and one S_h point; singletons alternate
        Sg, Sh = set(), set()
        Amap, side = {}, {}
        for s, v in pairs:
            Sg.add(v[0])
            Sh.add(v[1])
            Amap[v[0]] = [g, s]
            Amap[v[1]] = [h, s]
        for k, (s, v) in enumerate(sing):
            if k == 0:
                Sg.add(v[0])
                Amap[v[0]] = [g, s]
            else:
                Sh.add(v[0])
                Amap[v[0]] = [h, s]
        Sg.add(w13)
        Sh.add(w13)
        Amap[w13] = [g, h]
        if len(Sg) != rho or len(Sh) != rho:
            continue
        # outside completion
        outside = [x for x in D if x not in set(W)]
        if len(outside) != N - a:
            continue
        # vertices 0..6 : 0 and 6 are the X=1 blocks; 1..5 the X=2 blocks
        order = [gam[5], gam[0], gam[1], gam[2], gam[3], gam[4], gam[6]]
        removed = {(1, 2), (3, 4), (5, 6)}
        edges = [(i, j) for i in range(7) for j in range(i + 1, 7)
                 if (i, j) not in removed]
        if len(edges) != 18 or len(outside) != 19:
            continue
        blocks = {s: set() for s in gam}
        for s, v in pairs:
            blocks[s] |= set(v)
        for s, v in sing:
            blocks[s] |= set(v)
        for k, (i, j) in enumerate(edges):
            blocks[order[i]].add(outside[k])
            blocks[order[j]].add(outside[k])
        blocks[order[6]].add(outside[18])        # the half-edge (degree-1 point)
        allblocks = {"g": set(Sg), "h": set(Sh)}
        for s in gam:
            allblocks["t%d" % s] = blocks[s]
        return dict(A=A, B=B, q=q, D=D, W=W, Sg=Sg, Sh=Sh, w13=w13, g=g, h=h,
                    gam=gam, Amap=Amap, blocks=allblocks, phi=phi,
                    pairs=pairs, sing=sing, outside=outside)
    return None


for q in (97, 193):
    cfg = build(q, 20260811 + q)
    P("")
    P("-" * 78)
    if cfg is None:
        P("  q = %d : NO configuration found within the search budget (MISS)" % q)
        continue
    bl = cfg["blocks"]
    W, D = set(cfg["W"]), cfg["D"]
    dx = {x: sum(1 for b in bl.values() if x in b) for x in D}
    sizes = sorted(len(b) for b in bl.values())
    O = sum(rho - len(b) for b in bl.values())
    defi = sum(m - dx[x] for x in D)
    pu = min(len(b1 | b2) for k1, b1 in bl.items() for k2, b2 in bl.items() if k1 < k2)
    pi_ = max(len(b1 & b2) for k1, b1 in bl.items() for k2, b2 in bl.items() if k1 < k2)
    Xg = {k: len(b & W) for k, b in bl.items()}
    spend = {k: len(b - W) for k, b in bl.items()}
    nfib = {"g": sum(1 for x in W if x not in cfg["Sg"]),
            "h": sum(1 for x in W if x not in cfg["Sh"])}
    P("  q = %d   FULL INCIDENCE VERIFICATION (my code, all 9 blocks, 32 points)" % q)
    P("    T = %d = rho+2 = %d                                : %s"
      % (len(bl), rho + 2, len(bl) == rho + 2))
    P("    block sizes %s   all = rho = %d ; O = %d <= delta = m-1 = %d : %s"
      % (sizes, rho, O, m - 1, O <= m - 1))
    P("    max d_x = %d <= e = m = %d                          : %s"
      % (max(dx.values()), m, max(dx.values()) <= m))
    P("    sum_x (m - d_x) = %d = 1+O = %d   [(SAT4)]           : %s"
      % (defi, 1 + O, defi == 1 + O))
    P("    |W| = %d = a = 7m-1 = %d ; W = S_g u S_h            : %s"
      % (len(W), 7 * m - 1, (cfg["Sg"] | cfg["Sh"]) == W))
    P("    min pair union = %d = a  [(OV), w* = a* = a]        : %s"
      % (pu, pu == a))
    P("    max pair intersection = %d = 2rho-a = %d             : %s"
      % (pi_, 2 * rho - a, pi_ == 2 * rho - a))
    P("    S_g, S_h inside W (type-1) ; n_g = %d, n_h = %d = a-rho = %d : %s"
      % (nfib["g"], nfib["h"], a - rho,
         cfg["Sg"] <= W and cfg["Sh"] <= W and nfib["g"] == nfib["h"] == a - rho))
    P("    type-2 X_gamma = %s ; cap 2m-2 = %d (FR-canonical)  : %s"
      % (sorted(Xg["t%d" % s] for s in cfg["gam"]), 2 * m - 2,
         max(Xg["t%d" % s] for s in cfg["gam"]) <= 2 * m - 2))
    P("    type-2 spend |S\\W| = %s ; floor (R+1)-a+n = %d      : %s"
      % (sorted(spend["t%d" % s] for s in cfg["gam"]), R + 1 - a,
         min(spend["t%d" % s] for s in cfg["gam"]) >= R + 1 - a))
    P("    |A_x| = m = 2 for every x in W                     : %s"
      % all(len(cfg["Amap"][x]) == m for x in W))
    P("    A_x agrees with block membership                   : %s"
      % all(set(cfg["Amap"][x]) ==
            {cfg["g"] if k == "g" else cfg["h"] if k == "h" else int(k[1:])
             for k, b in bl.items() if x in b} for x in W))
    # the bivariate system
    pr, cols, nc, nrows, TT, _ = build_S2(m, q, cfg["W"], cfg["Amap"])
    nul = nc - pr.rank
    P("")
    P("    >>> BIVARIATE SYSTEM  (m+2)(4m+1) = %d equations, 2a = %d unknowns"
      % ((m + 2) * (4 * m + 1), nc))
    P("    >>> rank %d, NULLITY %d" % (pr.rank, nul))
    adm, murec = False, None
    if nul:
        kb = pr.kernel_basis()
        rr = random.Random(3)
        for _ in range(120):
            vv = [0] * nc
            for b in kb:
                c = rr.randrange(q)
                vv = [(x1 + c * y1) % q for x1, y1 in zip(vv, b)]
            byx = {}
            for ci, (x, kind, t) in enumerate(cols):
                byx.setdefault(x, []).append(vv[ci])
            if all(any(z for z in val) for val in byx.values()):
                adm = True
                murec = {}
                for x, val in byx.items():
                    a0, a1 = val[0], val[1]
                    murec[x] = "inf" if a1 == 0 else (-a0) * pow(a1, q - 2, q) % q
                break
    P("    >>> admissible kernel (every (alpha_x,beta_x) nonzero)   : %s" % adm)
    if murec:
        gg, hh = cfg["g"], cfg["h"]
        okmu = all(
            (murec[x] == hh if x in cfg["Sg"] and x not in cfg["Sh"] else
             murec[x] == gg if x in cfg["Sh"] and x not in cfg["Sg"] else True)
            for x in W)
        P("    >>> recovered mu: mu = h on S_g\\S_h and mu = g on S_h\\S_g  : %s" % okmu)
        P("    >>> mu(w13) = %s ; it is NOT a slope (so d_{w13} = m = 2)   : %s"
          % (murec[cfg["w13"]],
             murec[cfg["w13"]] not in set(cfg["gam"]) | {gg, hh}))
        P("    >>> sum_gamma n_gamma = %d = a = %d                          : %s"
          % (sum(1 for x in W if murec[x] in (gg, hh)) + 1, a,
             sum(1 for x in W if murec[x] in (gg, hh)) + 1 == a))
    P("")
    P("    phi = -A/B with A = %s, B = %s (ascending coefficients) over F_%d"
      % (cfg["A"], cfg["B"], q))
    P("    W  = %s" % sorted(W))
    P("    S_g= %s" % sorted(cfg["Sg"]))
    P("    S_h= %s" % sorted(cfg["Sh"]))
    P("    g = %d, h = %d, type-2 slopes = %s" % (cfg["g"], cfg["h"], sorted(cfg["gam"])))
    for k in sorted(bl):
        P("      S_%-5s = %s" % (k, sorted(bl[k])))

P("")
P("=" * 78)
print("\n".join(out))
with open("notes/pilots_20260811/rh_bivariate_system/d4_exhibit_results.txt", "w") as f:
    f.write("\n".join(out) + "\n")
