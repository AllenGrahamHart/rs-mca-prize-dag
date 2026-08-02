#!/usr/bin/env python3
"""Exhaustive band-structure engine for toy RS rows.

One pass over all k-subsets W of the evaluation domain yields, EXACTLY and
EXHAUSTIVELY:

  * every codeword pair (f,g) whose joint agreement Z(f,g) with (u,v) has
    size >= k        (any such pair is (P_W,Q_W) for any k-subset W of Z,
                      by linearity+uniqueness of interpolation);
  * every ray (z,c) with agr(u+zv, c) >= A >= k, together with its FULL
    agreement set   (any such c is P_W + z Q_W for any k-subset W of the
                     agreement set);
  * hence: global genericity (max |Z|), tangent-freeness (max ray agreement),
    all cross-pair cores, all band pairs and their live-slope counts.

Per W the work is O(n k) field operations using the barycentric identity
   l_j(x_i) = (prod_{m in W}(x_i-x_m)) * INV[x_i-x_j] * INV[prod_{m!=j}(x_j-x_m)].
"""
import itertools
from collections import defaultdict


class Row:
    def __init__(self, n, k, t, q):
        self.n, self.k, self.t, self.q = n, k, t, q
        self.A = k + t
        self.h = t
        self.R = n - k
        self.r = n - self.A
        self.xs = [(i + 1) % q for i in range(n)]
        assert len(set(self.xs)) == n and 0 not in self.xs
        self.INV = [0] * q
        for a in range(1, q):
            self.INV[a] = pow(a, q - 2, q)
        self.DIFF = [[(self.xs[i] - self.xs[m]) % q for m in range(n)]
                     for i in range(n)]
        self.INVDIFF = [[self.INV[self.DIFF[i][m]] if i != m else 0
                         for m in range(n)] for i in range(n)]

    def interp(self, W, vals):
        """coefficients of the deg<k interpolant of vals on W (tuple)."""
        q, k = self.q, self.k
        coeff = [0] * k
        for idx, j in enumerate(W):
            num = [1]
            den = 1
            for m in W:
                if m == j:
                    continue
                new = [0] * (len(num) + 1)
                for e, ce in enumerate(num):
                    if ce:
                        new[e] = (new[e] - ce * self.xs[m]) % q
                        new[e + 1] = (new[e + 1] + ce) % q
                num = new
                den = den * self.DIFF[j][m] % q
            w = vals[idx] * self.INV[den] % q
            for e in range(len(num)):
                coeff[e] = (coeff[e] + w * num[e]) % q
        return tuple(coeff)

    def ev(self, c, x):
        q = self.q
        acc = 0
        for co in reversed(c):
            acc = (acc * x + co) % q
        return acc


def scan(row, u, v):
    """The exhaustive pass.  Returns (pairs, rays).

    pairs: Z(frozenset) -> dict(J, coeffs=(f,g), slopes=set, agr=dict z->size)
    rays : (z, Z_ray frozenset) -> dict(z, support)
    """
    n, k, q, A = row.n, row.k, row.q, row.A
    xs, INV, DIFF, INVDIFF = row.xs, row.INV, row.DIFF, row.INVDIFF
    pairs = {}
    rays = {}
    allidx = range(n)
    for W in itertools.combinations(allidx, k):
        Wset = set(W)
        invden = []
        for j in W:
            d_ = 1
            dj = DIFF[j]
            for m in W:
                if m != j:
                    d_ = d_ * dj[m] % q
            invden.append(INV[d_])
        cu = [u[j] * invden[e] % q for e, j in enumerate(W)]
        cv = [v[j] * invden[e] % q for e, j in enumerate(W)]
        Z = list(W)
        buckets = defaultdict(list)
        for i in allidx:
            if i in Wset:
                continue
            di = DIFF[i]
            PI = 1
            for m in W:
                PI = PI * di[m] % q
            gi = INVDIFF[i]
            su = 0
            sv = 0
            for e, j in enumerate(W):
                g = gi[j]
                su += cu[e] * g
                sv += cv[e] * g
            a = (PI * su - u[i]) % q
            b = (PI * sv - v[i]) % q
            if a == 0 and b == 0:
                Z.append(i)
            elif b != 0:
                buckets[(-a) * INV[b] % q].append(i)
        Zf = frozenset(Z)
        J = len(Zf)
        if Zf not in pairs:
            pairs[Zf] = dict(J=J, coeffs=None, slopes={})
        pr = pairs[Zf]
        for z, extra in buckets.items():
            s = J + len(extra)
            if s >= A:
                pr["slopes"][z] = s
                key = (z, Zf | frozenset(extra))
                if key not in rays:
                    rays[key] = dict(z=z, supp=Zf | frozenset(extra), agr=s)
    for Zf, pr in pairs.items():
        Zl = sorted(Zf)[:row.k]
        pr["coeffs"] = (row.interp(tuple(Zl), [u[i] for i in Zl]),
                        row.interp(tuple(Zl), [v[i] for i in Zl]))
    return pairs, rays


def analyse(row, u, v, verbose=False):
    n, k, A, h, q = row.n, row.k, row.A, row.h, row.q
    pairs, rays = scan(row, u, v)
    res = dict(n=n, k=k, t=row.t, A=A, h=h, R=row.R, r=row.r, q=q,
               band=[k + 1, A - 2])

    # ---- strip / genericity gates (exhaustive) -------------------------
    maxJ = max(p["J"] for p in pairs.values())
    max_agr = max((rr["agr"] for rr in rays.values()), default=0)
    res["max_joint_agreement"] = maxJ
    res["globally_generic"] = maxJ <= A - 1
    res["below_cascade_threshold"] = maxJ <= A - 2
    res["max_ray_agreement"] = max_agr
    res["tangent_free"] = max_agr <= A
    res["v_nonvanishing"] = all(x != 0 for x in v)
    res["n_rays"] = len(rays)
    live = defaultdict(int)
    for rr in rays.values():
        live[rr["z"]] += 1
    res["live_slopes"] = len(live)
    res["max_rays_per_slope"] = max(live.values(), default=0)
    res["slopes_with_multiple_rays"] = sum(1 for c in live.values() if c > 1)

    # ---- the graded ledger objects ------------------------------------
    byd = defaultdict(list)
    for Zf, pr in pairs.items():
        d = pr["J"] - k
        if 0 <= d <= h - 1 and pr["slopes"]:
            byd[d].append((Zf, pr))
    ledger = {}
    capfail = []
    for d in sorted(byd):
        Ls = [len(pr["slopes"]) for _, pr in byd[d]]
        cap = (row.R - d) // (h - d) if h - d > 0 else None
        n2 = sum(1 for L in Ls if L >= 2)
        ledger[d] = dict(pairs_with_slopes=len(Ls), N_d=n2,
                         maxL=max(Ls), cap=cap,
                         sumL_over_Ldd2=sum(L for L in Ls if L >= 2),
                         cap_tight=(max(Ls) == cap))
        if cap is not None and max(Ls) > cap:
            capfail.append((d, max(Ls), cap))
    res["ledger"] = ledger
    res["LINE_CAP_violations"] = capfail

    # ---- k-packing (exhaustive over all pairs with J >= k) -------------
    big = [Zf for Zf, pr in pairs.items() if pr["J"] >= k]
    worst = 0
    for a in range(len(big)):
        for b in range(a + 1, len(big)):
            m = len(big[a] & big[b])
            if m > worst:
                worst = m
    res["kpacking_max_intersection"] = worst
    res["kpacking_ok"] = worst <= k - 1
    res["pairs_with_J_ge_k"] = len(big)

    # ---- T2 fibre identity: cross-pair core == Z of the forced pair ----
    rl = list(rays.values())
    t2_bad = []
    cores = defaultdict(int)
    band_slopes = set()
    eqk_slopes = set()
    for a in range(len(rl)):
        for b in range(a + 1, len(rl)):
            if rl[a]["z"] == rl[b]["z"]:
                continue
            core = rl[a]["supp"] & rl[b]["supp"]
            cores[len(core)] += 1
            if len(core) >= k:
                if core not in pairs or pairs[core]["J"] != len(core):
                    t2_bad.append((rl[a]["z"], rl[b]["z"], len(core)))
                if len(core) == k:
                    eqk_slopes |= {rl[a]["z"], rl[b]["z"]}
                if k + 1 <= len(core) <= A - 2:
                    band_slopes |= {rl[a]["z"], rl[b]["z"]}
    res["core_histogram"] = {str(a): b for a, b in sorted(cores.items())
                             if a >= k - 1}
    res["T2_violations"] = t2_bad
    res["band_slopes"] = len(band_slopes)
    res["exact_k_core_slopes"] = len(eqk_slopes)

    # ---- shared-slope rigidity ----------------------------------------
    withsl = [(Zf, pr) for Zf, pr in pairs.items()
              if pr["J"] >= k + 1 and pr["slopes"]]
    rig_bad = []
    prop_bad = []
    shared_hist = defaultdict(int)
    for a in range(len(withsl)):
        for b in range(a + 1, len(withsl)):
            sa = set(withsl[a][1]["slopes"])
            sb = set(withsl[b][1]["slopes"])
            sh = sa & sb
            shared_hist[len(sh)] += 1
            if len(sh) > 1:
                rig_bad.append((sorted(sh),))
            for z in sh:
                (f1, g1) = withsl[a][1]["coeffs"]
                (f2, g2) = withsl[b][1]["coeffs"]
                df = tuple((x - y) % q for x, y in zip(f1, f2))
                dg = tuple((x - y) % q for x, y in zip(g1, g2))
                ok = all((x + z * y) % q == 0 for x, y in zip(df, dg))
                if not ok:
                    prop_bad.append((z, df, dg))
    res["rigidity_shared_slope_hist"] = {str(a): b
                                         for a, b in sorted(shared_hist.items())}
    res["rigidity_violations"] = rig_bad
    res["rigidity_proportionality_violations"] = prop_bad

    # ---- ledger column measured ---------------------------------------
    col = sum(v_["sumL_over_Ldd2"] for d, v_ in ledger.items() if d >= 1)
    res["measured_band_column_sumL"] = col
    res["measured_band_slopes"] = len(band_slopes)
    res["printed_tangent_column_n_A_1"] = n - A + 1
    res["column_vs_printed"] = col - (n - A + 1)
    return res, pairs, rays


def plant(row, cores, seed, vfree_nonzero=True):
    """Build a received pair with planted band cores.

    cores: list of dict(Z=[idx...], slopes=[z...], blocks=[[idx...],...])
    Blocks must be pairwise disjoint and disjoint from every Z.
    """
    import random
    rnd = random.Random(seed)
    n, k, q, A = row.n, row.k, row.q, row.A
    u = [None] * n
    v = [None] * n
    built = []
    for spec in cores:
        Z = list(spec["Z"])
        fixed = [i for i in Z if u[i] is not None]
        assert len(fixed) <= k, "core over-determined by earlier cores"
        free = [i for i in Z if u[i] is None]
        base = fixed + free[:k - len(fixed)]
        assert len(base) == k, "core smaller than k"
        for i in base:
            if u[i] is None:
                u[i] = rnd.randrange(q)
                v[i] = rnd.randrange(1, q)
        f = row.interp(tuple(base), [u[i] for i in base])
        g = row.interp(tuple(base), [v[i] for i in base])
        for i in Z:
            if u[i] is None:
                u[i] = row.ev(f, row.xs[i])
                v[i] = row.ev(g, row.xs[i])
        built.append((f, g, frozenset(Z)))
    for spec, (f, g, Zf) in zip(cores, built):
        J = len(spec["Z"])
        for z, blk in zip(spec["slopes"], spec["blocks"]):
            assert len(blk) == A - J, f"block size must be A-J={A-J}"
            for i in blk:
                assert u[i] is None, "block point already used"
                gi = row.ev(g, row.xs[i])
                vi = rnd.randrange(1, q)
                while vi == gi:
                    vi = rnd.randrange(1, q)
                v[i] = vi
                u[i] = (row.ev(f, row.xs[i]) + z * (gi - vi)) % q
    for i in range(n):
        if u[i] is None:
            u[i] = rnd.randrange(q)
            v[i] = rnd.randrange(1, q) if vfree_nonzero else rnd.randrange(q)
    return u, v, built
