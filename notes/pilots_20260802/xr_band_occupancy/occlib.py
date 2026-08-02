#!/usr/bin/env python3
"""Band-occupancy engine: exhaustive toy scan + occupancy measurements.

Extends the banked xr_graded_band_ledger/bandlib.py engine with

  * the (0:1) pencil direction  (max agreement of a codeword with v alone)
    -- the banked gate tracks only the finite slopes z (u + z v);
  * the occupancy quantities  N_d, X_d = sum_P C(L_P,2), |Gamma_band|,
    sum_P L_P, and the ledger bound sum_d N_d L(d);
  * checks of the new structural theorems (unified fibre strip, per-component
    multiplicity, per-slope high-depth uniqueness, spread-coset form).

Row/interp are imported read-only from the banked bandlib.
Run under tools/ramguard.
"""
import itertools
import sys
from collections import defaultdict

sys.dont_write_bytecode = True
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/"
                   "pilots_20260802/xr_graded_band_ledger")
from bandlib import Row  # noqa: E402  (read-only import)


# ---------------------------------------------------------------- scan
def scan(row, u, v):
    """Exhaustive pass over all k-subsets.

    Returns (pairs, rays, vmax) where
      pairs: Z(frozenset) -> dict(J, coeffs=(f,g), slopes={z: agr},
                                  supports={z: frozenset}, vagr=int)
      rays : (z, S) -> agreement size
      vmax : max over codewords g of |{i : g(x_i) = v_i}|   [(0:1) direction]
    """
    n, k, q, A = row.n, row.k, row.q, row.A
    INV, DIFF, INVDIFF = row.INV, row.DIFF, row.INVDIFF
    pairs, rays = {}, {}
    vmax = 0
    for W in itertools.combinations(range(n), k):
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
        vert = 0
        for i in range(n):
            if i in Wset:
                continue
            di = DIFF[i]
            PI = 1
            for m in W:
                PI = PI * di[m] % q
            gi = INVDIFF[i]
            su = sv = 0
            for e, j in enumerate(W):
                g_ = gi[j]
                su += cu[e] * g_
                sv += cv[e] * g_
            a = (PI * su - u[i]) % q
            b = (PI * sv - v[i]) % q
            if a == 0 and b == 0:
                Z.append(i)
            elif b:
                buckets[(-a) * INV[b] % q].append(i)
            else:
                vert += 1
        Zf = frozenset(Z)
        J = len(Zf)
        if J + vert > vmax:
            vmax = J + vert
        if Zf not in pairs:
            pairs[Zf] = dict(J=J, coeffs=None, slopes={}, supports={},
                             vagr=J + vert)
        pr = pairs[Zf]
        for z, extra in buckets.items():
            s = J + len(extra)
            if s >= A:
                S = Zf | frozenset(extra)
                pr["slopes"][z] = s
                pr["supports"][z] = S
                key = (z, S)
                if key not in rays or rays[key] < s:
                    rays[key] = s
    for Zf, pr in pairs.items():
        Zl = sorted(Zf)[:row.k]
        pr["coeffs"] = (row.interp(tuple(Zl), [u[i] for i in Zl]),
                        row.interp(tuple(Zl), [v[i] for i in Zl]))
    return pairs, rays, vmax


# ------------------------------------------------------------ measurement
def prop_slope(row, P1, P2):
    """z in F_q u {inf} with pi_z(P1) = pi_z(P2), else None.

    pi_z(f,g) = f + z g   (z finite);  pi_inf(f,g) = g.
    Returns 'inf', an int z, or None.  (f1=f2 and g1=g2 impossible for
    distinct pairs.)
    """
    q = row.q
    (f1, g1), (f2, g2) = P1["coeffs"], P2["coeffs"]
    df = [(a - b) % q for a, b in zip(f1, f2)]
    dg = [(a - b) % q for a, b in zip(g1, g2)]
    if not any(dg):
        return "inf"                      # g1 = g2
    if not any(df):
        return 0                          # f1 = f2
    lead = max(i for i, c in enumerate(dg) if c)
    lam = df[lead] * row.INV[dg[lead]] % q
    if all((a - lam * b) % q == 0 for a, b in zip(df, dg)):
        return (-lam) % q                 # df = -z dg
    return None


def measure(row, u, v, name="", want_checks=True):
    n, k, A, h, q, R = row.n, row.k, row.A, row.h, row.q, row.R
    pairs, rays, vmax = scan(row, u, v)
    rec = dict(fixture=name, n=n, k=k, t=row.t, A=A, h=h, R=R, q=q,
               band=[k + 1, A - 2])

    # ---- gates -------------------------------------------------------
    maxJ = max(p["J"] for p in pairs.values())
    maxray = max(rays.values(), default=0)
    rec["max_joint_agreement"] = maxJ
    rec["max_ray_agreement"] = maxray
    rec["max_v_side_agreement"] = vmax          # the (0:1) direction
    rec["globally_generic"] = maxJ <= A - 1
    rec["below_cascade"] = maxJ <= A - 2
    rec["tangent_free_finite_slopes"] = maxray <= A
    rec["tangent_free_v_direction"] = vmax <= A
    rec["v_nonvanishing"] = all(x != 0 for x in v)
    rec["ADMISSIBLE"] = (rec["below_cascade"] and rec["tangent_free_finite_slopes"]
                         and rec["v_nonvanishing"])
    rec["ADMISSIBLE_with_v_gate"] = rec["ADMISSIBLE"] and rec["tangent_free_v_direction"]

    # ---- band pairs / lines -----------------------------------------
    band = []            # (Z, pair, d, sorted live slopes)
    for Zf, p in pairs.items():
        d = p["J"] - k
        if 1 <= d <= h - 2:
            band.append((Zf, p, d, sorted(p["slopes"])))
    byd = defaultdict(list)
    for Zf, p, d, sl in band:
        byd[d].append((Zf, p, sl))

    ledger, N_tot, X_tot, sumL_tot = {}, 0, 0, 0
    gamma_band = set()
    ledger_bound = 0
    for d in sorted(byd):
        Ls = [len(sl) for _, _, sl in byd[d]]
        ge2 = [L for L in Ls if L >= 2]
        cap = (R - d) // (h - d)
        Nd = len(ge2)
        Xd = sum(L * (L - 1) // 2 for L in ge2)
        ledger[str(d)] = dict(pairs_at_depth=len(Ls), N_d=Nd, X_d=Xd,
                              sumL_ge2=sum(ge2), maxL=max(Ls), cap=cap,
                              cap_ok=max(Ls) <= cap)
        N_tot += Nd
        X_tot += Xd
        sumL_tot += sum(ge2)
        ledger_bound += Nd * cap
        for _, _, sl in byd[d]:
            if len(sl) >= 2:
                gamma_band |= set(sl)
    rec["ledger_by_depth"] = ledger
    rec["N_total"] = N_tot
    rec["X_total"] = X_tot
    rec["sum_L_over_band_pairs"] = sumL_tot
    rec["Gamma_band_measured"] = len(gamma_band)
    rec["ledger_bound_sum_Nd_L"] = ledger_bound
    rec["ledger_slack_vs_measured"] = (ledger_bound / len(gamma_band)
                                       if gamma_band else None)
    rec["sumL_slack_vs_measured"] = (sumL_tot / len(gamma_band)
                                     if gamma_band else None)
    rec["printed_tangent_column"] = n - A + 1
    rec["column_beats_printed"] = sumL_tot > n - A + 1
    rec["N_over_n"] = N_tot / n
    rec["N_over_n2"] = N_tot / (n * n)

    if not want_checks:
        return rec, pairs, band

    # ---- k-packing ---------------------------------------------------
    deep = [Zf for Zf, p in pairs.items() if p["J"] >= k + 1]
    worst = 0
    for a in range(len(deep)):
        for b in range(a + 1, len(deep)):
            m = len(deep[a] & deep[b])
            if m > worst:
                worst = m
    rec["deep_pairs"] = len(deep)
    rec["kpacking_max_intersection"] = worst
    rec["kpacking_ok"] = worst <= k - 1

    # ---- T-1 unified fibre strip + T-2 per-component multiplicity ----
    dl = [(Zf, p, p["J"] - k) for Zf, p in pairs.items() if p["J"] >= k + 1]
    t1_bad, t1_hits = [], 0
    for a in range(len(dl)):
        for b in range(a + 1, len(dl)):
            z = prop_slope(row, dl[a][1], dl[b][1])
            if z is None:
                continue
            t1_hits += 1
            Zu = len(dl[a][0] | dl[b][0])
            dsum = dl[a][2] + dl[b][2]
            if Zu > A or dsum > h - 1:
                t1_bad.append(dict(z=str(z), union=Zu, dsum=dsum, A=A, h=h))
    rec["T1_shared_fibre_pairs"] = t1_hits
    rec["T1_violations"] = t1_bad[:5]
    rec["T1_ok"] = not t1_bad

    fmult, gmult = defaultdict(int), defaultdict(int)
    for Zf, p, d in dl:
        fmult[(p["coeffs"][0], d)] += 1
        gmult[(p["coeffs"][1], d)] += 1
    rec["max_pairs_sharing_f_at_a_depth"] = max(fmult.values(), default=0)
    rec["max_pairs_sharing_g_at_a_depth"] = max(gmult.values(), default=0)
    hi = [(key, m) for key, m in fmult.items() if key[1] >= (h + 1) // 2 and m > 1]
    rec["T2_high_depth_f_violations"] = [(str(a), b) for a, b in hi][:5]
    rec["T2_ok"] = not hi

    # ---- per-slope line structure (partial linear space) -------------
    lines_at = defaultdict(list)      # z -> [depths of lines through z]
    for Zf, p, d, sl in band:
        if len(sl) >= 2:
            for z in sl:
                lines_at[z].append(d)
    rec["max_lines_per_slope"] = max((len(x) for x in lines_at.values()),
                                     default=0)
    hib = [(z, ds) for z, ds in lines_at.items()
           if sum(1 for d in ds if d >= (h + 1) // 2) > 1]
    rec["T3_high_depth_slope_violations"] = [(str(a), b) for a, b in hib][:5]
    rec["T3_ok"] = not hib
    dsum_bad = [(z, ds) for z, ds in lines_at.items()
                if len(ds) >= 2 and max(ds) + sorted(ds)[-2] > h - 1]
    rec["T1_perslope_depthsum_violations"] = [(str(a), b) for a, b in dsum_bad][:5]

    # ---- spread-coset form: pairs sharing slope z differ by ker(pi_z) --
    byslope, byray = defaultdict(list), defaultdict(list)
    for Zf, p, d, sl in band:
        for z in sl:
            byslope[z].append(p)
            byray[(z, p["supports"][z])].append(p)
    coset_bad, slope_bad = [], []
    for tgt, key in ((coset_bad, byray), (slope_bad, byslope)):
        for kk, ps in key.items():
            z = kk[0] if isinstance(kk, tuple) else kk
            for a in range(len(ps)):
                for b in range(a + 1, len(ps)):
                    (f1, g1), (f2, g2) = ps[a]["coeffs"], ps[b]["coeffs"]
                    if any(((x - y) + z * (w - t)) % q
                           for x, y, w, t in zip(f1, f2, g1, g2)):
                        tgt.append(str(z))
    rec["spread_coset_violations_per_ray"] = coset_bad[:5]
    rec["spread_coset_ok"] = not coset_bad            # per-RAY (Theorem 4)
    rec["spread_coset_violations_per_slope"] = slope_bad[:5]
    rec["spread_coset_per_slope_ok"] = not slope_bad  # fails iff re-selection

    # ---- T2 fibre identity: core of two live supports == Z of the pair -
    rl = [(z, S) for (z, S) in rays]
    t2f_bad = []
    for a in range(len(rl)):
        for b in range(a + 1, len(rl)):
            if rl[a][0] == rl[b][0]:
                continue
            core = rl[a][1] & rl[b][1]
            if len(core) >= k:
                if core not in pairs or pairs[core]["J"] != len(core):
                    t2f_bad.append((str(rl[a][0]), str(rl[b][0]), len(core)))
    rec["fibre_identity_violations"] = t2f_bad[:5]
    rec["n_rays"] = len(rays)
    rec["live_slopes"] = len({z for z, _ in rays})
    cnt = defaultdict(int)
    for z, _ in rays:
        cnt[z] += 1
    rec["max_rays_per_slope"] = max(cnt.values(), default=0)
    rec["reselection_slopes"] = sum(1 for c in cnt.values() if c > 1)
    return rec, pairs, band


# ------------------------------------------------------------- builders
def plant_cores(row, cores, assign, seed, rnd_free=True):
    """cores: list of index lists.  assign: {i: [(core_idx, z), ...]} with
    1 or 2 constraints per point (2 need distinct slopes).  Same semantics
    as the banked plant_general; re-implemented here (own file)."""
    import random
    rnd = random.Random(seed)
    n, k, q = row.n, row.k, row.q
    u = [None] * n
    v = [None] * n
    built = []
    for Z in cores:
        fixed = [i for i in Z if u[i] is not None]
        free = [i for i in Z if u[i] is None]
        if len(fixed) > k:
            raise ValueError("core over-determined")
        base = fixed + free[:k - len(fixed)]
        if len(base) != k:
            raise ValueError("core smaller than k")
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
            elif (u[i], v[i]) != (row.ev(f, row.xs[i]), row.ev(g, row.xs[i])):
                raise ValueError("core inconsistent with earlier data")
        built.append((f, g, frozenset(Z)))
    for i, cons in sorted(assign.items()):
        if u[i] is not None:
            raise ValueError("assigned point already used")
        rhs = [(z, (row.ev(built[s][0], row.xs[i])
                    + z * row.ev(built[s][1], row.xs[i])) % q)
               for s, z in cons]
        if len(rhs) == 1:
            z, c = rhs[0]
            gi = row.ev(built[cons[0][0]][1], row.xs[i])
            vi = rnd.randrange(1, q)
            while vi == gi:
                vi = rnd.randrange(1, q)
            v[i] = vi
            u[i] = (c - z * vi) % q
        else:
            (z1, c1), (z2, c2) = rhs[0], rhs[1]
            if z1 == z2:
                raise ValueError("two constraints need distinct slopes")
            vi = (c1 - c2) * row.INV[(z1 - z2) % q] % q
            if vi == 0:
                raise ValueError("degenerate shared point (v=0)")
            for s, _z in cons:
                if vi == row.ev(built[s][1], row.xs[i]):
                    raise ValueError("shared point falls into a core")
            v[i] = vi
            u[i] = (c1 - z1 * vi) % q
    for i in range(n):
        if u[i] is None:
            u[i] = rnd.randrange(q) if rnd_free else 0
            v[i] = rnd.randrange(1, q)
    return u, v, built


def plant_rays(row, slopes, supports, codewords):
    """Ray-first builder: u,v forced on every doubly covered coordinate.

    slopes[j], supports[j] (index set), codewords[j] (coeff tuple).
    Returns (u, v) or raises ValueError on an inconsistency.
    Coordinates covered once get a free v; uncovered ones stay None.
    """
    n, q = row.n, row.q
    cov = defaultdict(list)
    for j, S in enumerate(supports):
        for i in S:
            cov[i].append(j)
    u = [None] * n
    v = [None] * n
    for i, js in cov.items():
        vals = [(slopes[j], row.ev(codewords[j], row.xs[i])) for j in js]
        if len(js) == 1:
            return None, None, "singly covered handled by caller"
        (z1, c1), (z2, c2) = vals[0], vals[1]
        if z1 == z2:
            raise ValueError("repeated slope at a coordinate")
        vi = (c1 - c2) * row.INV[(z1 - z2) % q] % q
        ui = (c1 - z1 * vi) % q
        for (z, c) in vals[2:]:
            if (ui + z * vi) % q != c:
                raise ValueError(f"inconsistent triple cover at {i}")
        u[i], v[i] = ui, vi
    return u, v, "ok"
