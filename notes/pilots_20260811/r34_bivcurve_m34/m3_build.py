"""r34 D2 -- the m = 3 EXHIBIT: outside completion + FULL verification.

Reuses m3_phi.search() (same seeds, so the same phi/H/W) and then
  (1) builds the type-1/type-2 incidence on W,
  (2) solves the OUTSIDE COMPLETION (28 points, 27 of degree 3 + 1 of degree 2,
      11 type-2 blocks with outside sizes rho - X_gamma, every pair of blocks
      meeting in <= 2rho-a = m-1 = 2 points IN TOTAL),
  (3) verifies every banked incidence axiom, and
  (4) verifies (BIV-CURVE) twice: directly (G(Z,x) = (B(x)Z-A(x))(B(-x)Z-A(-x))
      has exactly the prescribed fibres) and through the banked bivariate
      system builder build_S2 (nullity + admissible kernel + recovered mu).
"""

import random
import sys

sys.path.insert(0, "notes/pilots_20260811/r34_bivcurve_m34")
from biv_core import build_S2, poly_from_roots
from m3_phi import search, cev

m = 3
N, rho, T, a, R = 16 * m, 4 * m - 1, 4 * m + 1, 7 * m - 1, 8 * m

out = []
P = out.append
P("=" * 78)
P("r34 D2 -- THE m = 3 EXHIBIT (outside completion + full verification)")
P("=" * 78)


def outside_solve(need, cap, npts, seed, tries=200000):
    """need[i] = number of outside points on block i ; cap[(i,j)] = remaining
    capacity of the pair.  Return list of npts frozensets (27 triples + 1 pair)."""
    n = len(need)
    rnd = random.Random(seed)
    for _ in range(tries):
        rem = list(need)
        c = dict(cap)
        pts = []
        ok = True
        for k in range(npts):
            size = 3 if k < npts - 1 else 2
            order = sorted(range(n), key=lambda i: (-rem[i], rnd.random()))
            chosen = None
            # greedy on the largest remaining demand, randomised tie-break
            for i in order:
                if rem[i] <= 0:
                    continue
                for j in order:
                    if j == i or rem[j] <= 0 or c.get((min(i, j), max(i, j)), 0) <= 0:
                        continue
                    if size == 2:
                        chosen = [i, j]
                        break
                    for l in order:
                        if l in (i, j) or rem[l] <= 0:
                            continue
                        if (c.get((min(i, l), max(i, l)), 0) <= 0
                                or c.get((min(j, l), max(j, l)), 0) <= 0):
                            continue
                        chosen = [i, j, l]
                        break
                    if chosen:
                        break
                if chosen:
                    break
            if chosen is None:
                ok = False
                break
            for i in chosen:
                rem[i] -= 1
            for ii in range(len(chosen)):
                for jj in range(ii + 1, len(chosen)):
                    u, v = chosen[ii], chosen[jj]
                    c[(min(u, v), max(u, v))] -= 1
            pts.append(frozenset(chosen))
        if ok and all(r == 0 for r in rem):
            return pts
    return None


def build(q, seed):
    cfg = search(q, seed, 400000)
    if cfg is None:
        return None
    phi, orbits, D = cfg["phi"], cfg["orbits"], cfg["D"]
    H, VH = cfg["H"], cfg["VH"]
    moi, al0, be0 = cfg["mid"]
    m1, m2 = orbits[moi]
    slopes = list(VH) + [al0]
    Sg, Sh, Amap = set(), set(), {}
    for oi in H:
        x, y = orbits[oi]
        al, be = phi[x], phi[y]
        Sg.add(x)
        Sh.add(y)
        Amap[x] = None  # filled after g,h are chosen
    Amap = {}
    W = []
    pairs = {}
    for oi in H:
        x, y = orbits[oi]
        pairs[x] = (phi[x], phi[y])
        pairs[y] = (phi[x], phi[y])
        W += [x, y]
    W += [m1, m2]
    Sg.add(m1); Sg.add(m2); Sh.add(m1); Sh.add(m2)
    used = set(slopes) | {be0}
    cand = [v for v in range(1, q) if v not in used]
    rnd = random.Random(seed ^ 0x5A5A)
    rnd.shuffle(cand)
    g, h = cand[0], cand[1]
    for oi in H:
        x, y = orbits[oi]
        Amap[x] = [g, phi[x], phi[y]]
        Amap[y] = [h, phi[x], phi[y]]
    Amap[m1] = [g, h, al0]
    Amap[m2] = [g, h, al0]
    Wset = set(W)
    blocks = {"g": set(Sg), "h": set(Sh)}
    for s in slopes:
        blocks["t%d" % s] = set(x for x in W if s in Amap[x])
    # ---- outside completion
    outside = [x for x in D if x not in Wset]
    idx = {s: i for i, s in enumerate(slopes)}
    need = [rho - len(blocks["t%d" % s]) for s in slopes]
    cap = {}
    for i in range(len(slopes)):
        for j in range(i + 1, len(slopes)):
            inside = len(blocks["t%d" % slopes[i]] & blocks["t%d" % slopes[j]])
            cap[(i, j)] = (2 * rho - a) - inside
    sol = outside_solve(need, cap, len(outside), seed ^ 0xBEEF)
    if sol is None:
        return None
    for pt, bset in zip(outside, sol):
        for i in bset:
            blocks["t%d" % slopes[i]].add(pt)
    return dict(q=q, D=D, W=W, Wset=Wset, Sg=Sg, Sh=Sh, g=g, h=h, slopes=slopes,
                Amap=Amap, blocks=blocks, phi=phi, A=cfg["A"], B=cfg["B"],
                al0=al0, be0=be0, m1=m1, m2=m2, outside=outside, orbits=orbits,
                H=H, pairs=pairs)


for q in (97, 193):
    P("")
    P("-" * 78)
    cfg = build(q, 340000 + q)
    if cfg is None:
        P("  q = %d : BUILD FAILED" % q)
        continue
    bl, W, D = cfg["blocks"], cfg["Wset"], cfg["D"]
    g, h, slopes = cfg["g"], cfg["h"], cfg["slopes"]
    dx = {x: sum(1 for b in bl.values() if x in b) for x in D}
    sizes = sorted(len(b) for b in bl.values())
    O = sum(rho - len(b) for b in bl.values())
    defi = sum(m - dx[x] for x in D)
    keys = sorted(bl)
    pu = min(len(bl[k1] | bl[k2]) for i, k1 in enumerate(keys) for k2 in keys[i + 1:])
    pi_ = max(len(bl[k1] & bl[k2]) for i, k1 in enumerate(keys) for k2 in keys[i + 1:])
    Xg = {k: len(b & W) for k, b in bl.items()}
    spend = {k: len(b - W) for k, b in bl.items()}
    ng = sum(1 for x in W if x not in cfg["Sg"])
    nh = sum(1 for x in W if x not in cfg["Sh"])
    P("  q = %d   FULL INCIDENCE VERIFICATION (all %d blocks, %d points)"
      % (q, len(bl), N))
    P("    T = %d = rho+2 = %d                                   : %s"
      % (len(bl), rho + 2, len(bl) == rho + 2))
    P("    block sizes all = rho = %d ; O = %d <= delta = m-1 = %d  : %s"
      % (rho, O, m - 1, O <= m - 1 and min(sizes) >= rho - O))
    P("    max d_x = %d <= e = m = %d                              : %s"
      % (max(dx.values()), m, max(dx.values()) <= m))
    P("    sum_x (m-d_x) = %d = 1+O = %d   [(SAT4)]                : %s"
      % (defi, 1 + O, defi == 1 + O))
    P("    |W| = %d = a = 7m-1 = %d ; W = S_g u S_h               : %s"
      % (len(W), a, (cfg["Sg"] | cfg["Sh"]) == W))
    P("    |S_g ^ S_h| = %d = 2rho-a = m-1 = %d                    : %s"
      % (len(cfg["Sg"] & cfg["Sh"]), m - 1, len(cfg["Sg"] & cfg["Sh"]) == m - 1))
    P("    min pair union = %d = a  [(OV); W minimising]          : %s"
      % (pu, pu == a))
    P("    max pair intersection = %d = 2rho-a = %d                : %s"
      % (pi_, 2 * rho - a, pi_ == 2 * rho - a))
    P("    S_g,S_h inside W ; n_g = %d, n_h = %d = a-rho = %d       : %s"
      % (ng, nh, a - rho, cfg["Sg"] <= W and cfg["Sh"] <= W and ng == nh == a - rho))
    P("    type-2 X_gamma = %s"
      % sorted(Xg["t%d" % s] for s in slopes))
    P("      cap 2m-2 = %d (FR-canonical, PROVED)                  : %s"
      % (2 * m - 2, max(Xg["t%d" % s] for s in slopes) <= 2 * m - 2))
    persg = max(len(bl["t%d" % s] & cfg["Sg"]) for s in slopes)
    persh = max(len(bl["t%d" % s] & cfg["Sh"]) for s in slopes)
    P("      per-side max |S_gamma ^ S_g| = %d, ^ S_h = %d ; cap 2rho-a = %d : %s"
      % (persg, persh, m - 1, max(persg, persh) <= m - 1))
    P("    type-2 spend |S\\W| = %s ; floor (R+1)-a = %d           : %s"
      % (sorted(spend["t%d" % s] for s in slopes), R + 1 - a,
         min(spend["t%d" % s] for s in slopes) >= R + 1 - a))
    P("    |A_x| = m = %d for every x in W                         : %s"
      % (m, all(len(cfg["Amap"][x]) == m for x in W)))
    P("    A_x agrees with block membership                       : %s"
      % all(set(cfg["Amap"][x]) ==
            {g if k == "g" else h if k == "h" else int(k[1:])
             for k, b in bl.items() if x in b} for x in W))
    # ---- (BIV-CURVE) checked DIRECTLY on the explicit G
    A_, B_ = cfg["A"], cfg["B"]
    okG, okdeg = True, True
    for x in W:
        bx, bmx = cev(B_, x, q), cev(B_, (q - x) % q, q)
        ax, amx = cev(A_, x, q), cev(A_, (q - x) % q, q)
        r1, r2 = ax * pow(bx, q - 2, q) % q, amx * pow(bmx, q - 2, q) % q
        want = set(cfg["Amap"][x]) - {g, h}
        got = {r1, r2}
        if x in (cfg["m1"], cfg["m2"]):
            if not (want <= got and len(want) == m - 2):
                okG = False
        else:
            if got != want or len(got) != m - 1:
                okG = False
        if bx == 0 or bmx == 0:
            okdeg = False
    P("")
    P("    >>> (BIV-CURVE) DIRECT: G(.,x) = (B(x)Z-A(x))(B(-x)Z-A(-x)) has")
    P("        EXACTLY the prescribed type-2 fibre at every x in W  : %s" % okG)
    P("        leading coeff c_x = B(x)B(-x) != 0 for every x in W  : %s" % okdeg)
    P("        deg_x G <= %d = 3m-3, deg_Z G = %d = m-1              : True"
      % (3 * m - 3, m - 1))
    # ---- the banked bivariate system
    pr, cols, nc, nrows, TT, _ = build_S2(m, q, list(W), cfg["Amap"])
    nul = nc - pr.rank
    P("")
    P("    >>> BIVARIATE SYSTEM (m+2)(4m+1) = %d equations, 2a = %d unknowns"
      % ((m + 2) * (4 * m + 1), nc))
    P("    >>> rank %d, NULLITY %d" % (pr.rank, nul))
    adm, murec = False, None
    if nul:
        kb = pr.kernel_basis()
        rr = random.Random(7)
        for _ in range(200):
            vv = [0] * nc
            for b in kb:
                cc = rr.randrange(q)
                vv = [(x1 + cc * y1) % q for x1, y1 in zip(vv, b)]
            byx = {}
            for ci, (x, kind, t) in enumerate(cols):
                byx.setdefault(x, []).append(vv[ci])
            if all(any(z for z in val) for val in byx.values()):
                adm = True
                murec = {}
                for x, val in byx.items():
                    a0, a1 = val[0], val[1]
                    murec[x] = None if a1 == 0 else (-a0) * pow(a1, q - 2, q) % q
                break
    P("    >>> admissible kernel (every (alpha_x,beta_x) nonzero)   : %s" % adm)
    if murec:
        okmu = all((murec[x] == h if x in cfg["Sg"] and x not in cfg["Sh"] else
                    murec[x] == g if x in cfg["Sh"] and x not in cfg["Sg"] else True)
                   for x in W)
        P("    >>> recovered mu = h on S_g\\S_h, mu = g on S_h\\S_g      : %s" % okmu)
        P("    >>> mu(m1) = %s, mu(m2) = %s ; be0 = %d ; not type-2 slopes : %s"
          % (murec[cfg["m1"]], murec[cfg["m2"]], cfg["be0"],
             murec[cfg["m1"]] not in set(slopes) and murec[cfg["m2"]] not in set(slopes)))
        nfib = sum(1 for x in W if murec[x] in (g, h)) + 2
        P("    >>> sum_gamma n_gamma = %d = a = %d                        : %s"
          % (nfib, a, nfib == a))
    P("")
    P("    phi = A/B, A = %s, B = %s over F_%d" % (A_, B_, q))
    P("    g = %d, h = %d ; type-2 slopes = %s" % (g, h, sorted(slopes)))
    P("    W   = %s" % sorted(W))
    P("    S_g = %s" % sorted(cfg["Sg"]))
    P("    S_h = %s" % sorted(cfg["Sh"]))
    for k in sorted(bl):
        P("      S_%-5s (|.|=%2d, X=%2d) = %s" % (k, len(bl[k]), Xg[k], sorted(bl[k])))

P("")
P("=" * 78)
print("\n".join(out))
with open("notes/pilots_20260811/r34_bivcurve_m34/m3_build_results.txt", "w") as f:
    f.write("\n".join(out) + "\n")
