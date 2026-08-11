"""D5 -- CROSS-LAYER CHECK on my own D4 exhibit (this is the SIBLING pilot's
lane -- the psi_gamma / full-domain degree count -- flagged, not appropriated).

My instrument (D1-D4) is the W-LAYER: Psi(Z) in K'[Z] constrains only x in W,
because c_0, c_1 are supported in W.  There is a SECOND, logically independent
necessary condition on the same data, on the WHOLE domain:

  (LAYER A)  Q(Z;x) is ONE bivariate polynomial, deg_x <= rho, deg_Z <= e = m,
             with Q(gamma, .) vanishing exactly on S_gamma
             (saturation_rigidity/proof.md:5-6,15; apolar_origin/PREREG.md:187-190).

With o_gamma = 0 this pins Q(gamma,x) = c_gamma * L_gamma(x),
L_gamma = prod_{y in S_gamma}(x-y) (degree rho, split, same roots), so LAYER A
says: there are c_gamma != 0 such that for EVERY coefficient index t,

      ( c_gamma * [x^t] L_gamma )_{gamma in Z}   lies in   RS(Z, m+1),

i.e. is the evaluation at the T slope values of a polynomial of degree <= m.
That is (rho+1) x (T - (m+1)) = 8 x 6 = 48 linear conditions on the T = 9
unknowns c_gamma, for m = 2.  Run it on the D4 exhibit.
"""

import random
import sys

sys.path.insert(0, "notes/pilots_20260811/rh_bivariate_system")
from biv_core import PackedRank, mu_N, poly_from_roots

out = []
P = out.append
P("=" * 78)
P("D5 -- LAYER A (full-domain bivariate Q(Z,x)) APPLIED TO THE D4 EXHIBIT")
P("=" * 78)

m, N, rho, T, a = 2, 32, 7, 9, 13


def cev(c, x, q):
    v = 0
    for co in reversed(c):
        v = (v * x + co) % q
    return v


def build_cfg(q, seed, trials=400000):
    """same constructor as d4_exhibit (kept local so d5 is self-contained)."""
    D = mu_N(q, N)
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
        pairs, sing = twos[:5], ones[:2]
        w13 = ones[2][1][0]
        used = [x for _, v in pairs for x in v] + [v[0] for _, v in sing]
        W = used + [w13]
        if len(set(W)) != a:
            continue
        gam = [s for s, _ in pairs] + [s for s, _ in sing]
        if len(set(gam)) != 7:
            continue
        vals = set(phi[x] for x in W)
        cand = [v for v in range(1, q) if v not in vals]
        if len(cand) < 2:
            continue
        rnd.shuffle(cand)
        g, h = cand[0], cand[1]
        Sg, Sh, Amap = set(), set(), {}
        for s, v in pairs:
            Sg.add(v[0]); Sh.add(v[1])
            Amap[v[0]] = [g, s]; Amap[v[1]] = [h, s]
        for k, (s, v) in enumerate(sing):
            if k == 0:
                Sg.add(v[0]); Amap[v[0]] = [g, s]
            else:
                Sh.add(v[0]); Amap[v[0]] = [h, s]
        Sg.add(w13); Sh.add(w13); Amap[w13] = [g, h]
        if len(Sg) != rho or len(Sh) != rho:
            continue
        outside = [x for x in D if x not in set(W)]
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
            blocks[order[i]].add(outside[k]); blocks[order[j]].add(outside[k])
        blocks[order[6]].add(outside[18])
        allb = {("g", g): set(Sg), ("h", h): set(Sh)}
        for s in gam:
            allb[("t", s)] = blocks[s]
        return dict(q=q, D=D, W=W, allb=allb, g=g, h=h, gam=gam, Amap=Amap)
    return None


def layerA_core(slopes, L, q):
    """L[i] = coefficient vector (length rho+1) of the i-th block's locator."""
    # parity check of RS(Z, m+1) on the T slope values: sum_gamma d_gamma v_gamma
    # for the (T - (m+1)) dual basis; use the dual GRS check
    #   v in RS(Z,m+1)  <=>  sum_gamma v_gamma * lam_gamma * gamma^j = 0,
    #   j = 0..T-m-2, with lam_gamma = 1/prod_{d != gamma}(gamma-d).
    lam = []
    for i, gi in enumerate(slopes):
        pr_ = 1
        for j, gj in enumerate(slopes):
            if i != j:
                pr_ = pr_ * (gi - gj) % q
        lam.append(pow(pr_, q - 2, q))
    rows = []
    for t in range(rho + 1):
        for j in range(T - m - 1):
            rows.append([lam[i] * pow(slopes[i], j, q) * L[i][t] % q
                         for i in range(T)])
    prk = PackedRank(T, q)
    for r in rows:
        prk.add_row(r)
    return prk, len(rows), slopes, L, lam


def layerA_rank(cfg):
    q = cfg["q"]
    items = sorted(cfg["allb"].items(), key=lambda kv: kv[0][1])
    slopes = [k[1] for k, _ in items]
    L = [poly_from_roots(sorted(b), q) for _, b in items]
    assert all(len(p) == rho + 1 for p in L)
    return layerA_core(slopes, L, q)


def admissible_kernel(prk, seed=1, tries=80):
    q = prk.q
    if prk.rank == prk.n:
        return False
    kb = prk.kernel_basis()
    rr = random.Random(seed)
    for _ in range(tries):
        v = [0] * prk.n
        for b in kb:
            c = rr.randrange(q)
            v = [(x1 + c * y1) % q for x1, y1 in zip(v, b)]
        if all(v):
            return True
    return False


P("")
for q in (97, 193):
    cfg = build_cfg(q, 20260811 + q)
    if cfg is None:
        P("  q=%d : exhibit not reproduced (MISS)" % q)
        continue
    prk, nrows, slopes, L, lam = layerA_rank(cfg)
    nul = T - prk.rank
    P("  q = %d   LAYER A on the D4 exhibit" % q)
    P("    unknowns c_gamma : %d (= T = rho+2)" % T)
    P("    conditions       : %d  ((rho+1) x (T-m-1) = %d x %d)"
      % (nrows, rho + 1, T - m - 1))
    P("    rank             : %d   ->  NULLITY %d" % (prk.rank, nul))
    ok = False
    if nul:
        kb = prk.kernel_basis()
        rr = random.Random(1)
        for _ in range(60):
            v = [0] * T
            for b in kb:
                c = rr.randrange(q)
                v = [(x1 + c * y1) % q for x1, y1 in zip(v, b)]
            if all(v):
                ok = True
                break
    P("    kernel with EVERY c_gamma != 0 : %s" % ok)
    P("    >>> LAYER A verdict for the exhibit: %s"
      % ("SURVIVES" if ok else "KILLED (no bivariate Q(Z,x) of bidegree (rho,m))"))

P("")
P("  CONTROLS on the layer-A linear algebra (the root-set -> coefficient step is")
P("  already controlled in d1_control.py [C1]).")
P("")
P("  CTRL-1 (POSITIVE): take L_gamma := d_gamma * Q(gamma,.) for a RANDOM")
P("    bidegree-(rho,m) Q and random nonzero d_gamma.  Then c_gamma = 1/d_gamma")
P("    is a solution, so the nullity MUST be >= 1 with an all-nonzero kernel.")
for q in (97, 193):
    rnd = random.Random(555 + q)
    qq = [[rnd.randrange(q) for _ in range(rho + 1)] for _ in range(m + 1)]
    sl = rnd.sample(range(1, q), T)
    d = [rnd.randrange(1, q) for _ in range(T)]
    L = [[d[i] * sum(qq[j][t] * pow(sl[i], j, q) for j in range(m + 1)) % q
          for t in range(rho + 1)] for i in range(T)]
    prk, nrows, _, _, _ = layerA_core(sl, L, q)
    nul = T - prk.rank
    adm = admissible_kernel(prk, seed=2)
    P("    q=%-4d nullity %d (predicted >= 1), all-nonzero kernel %s   %s"
      % (q, nul, adm, "PASS" if nul >= 1 and adm else "FAIL"))

P("")
P("  CTRL-2 (ANALYTIC): all T blocks EQUAL (L_gamma = L for every gamma).  Then")
P("    the condition is (c_gamma)_gamma in RS(Z,m+1), so nullity == m+1 = 3.")
for q in (97, 193):
    rnd = random.Random(777 + q)
    sl = rnd.sample(range(1, q), T)
    base = [rnd.randrange(1, q) for _ in range(rho + 1)]
    L = [base[:] for _ in range(T)]
    prk, nrows, _, _, _ = layerA_core(sl, L, q)
    nul = T - prk.rank
    P("    q=%-4d nullity %d (predicted %d)   %s"
      % (q, nul, m + 1, "PASS" if nul == m + 1 else "FAIL"))

P("")
P("  CTRL-3 (NEGATIVE): perturb CTRL-1's L at ONE coefficient of ONE slope;")
P("    the solution should be destroyed (nullity drops to 0).")
for q in (97, 193):
    rnd = random.Random(555 + q)
    qq = [[rnd.randrange(q) for _ in range(rho + 1)] for _ in range(m + 1)]
    sl = rnd.sample(range(1, q), T)
    d = [rnd.randrange(1, q) for _ in range(T)]
    L = [[d[i] * sum(qq[j][t] * pow(sl[i], j, q) for j in range(m + 1)) % q
          for t in range(rho + 1)] for i in range(T)]
    L[3][2] = (L[3][2] + 1) % q
    prk, nrows, _, _, _ = layerA_core(sl, L, q)
    P("    q=%-4d nullity %d (predicted 0)   %s"
      % (q, T - prk.rank, "PASS" if T - prk.rank == 0 else "FAIL"))

P("")
P("=" * 78)
print("\n".join(out))
with open("notes/pilots_20260811/rh_bivariate_system/d5_layerA_results.txt", "w") as f:
    f.write("\n".join(out) + "\n")
