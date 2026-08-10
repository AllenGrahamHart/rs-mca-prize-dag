#!/usr/bin/env python3
"""D2 -- THE FALSIFIER HUNT at the M >= 5 large-source charts.

Registered at notes/pilots_20260809/m7_falsifier_hunt/PREREG.md R0-R7.

Hunts the round-25 registered falsifier: an FPC5 large-source cell,
inside its node's OWN admissibility, whose GUARDED split members have
kappa >= 1 or |U| < 2d -- i.e. sit on the winning side of sigma < 2a.

REUSES, unchanged (imported, not rewritten):
  notes/pilots_20260807/fpc5_diag/rh_m4t2_census.py  (exact F_q poly
      arithmetic: locator/pmul/prem/pgcd/pinvmod/peval/pdegree/domain)
  notes/pilots_20260807/mf_wall_adversary/rh_bucket.py (rref_kernel,
      monic_chart, enumerate_split, maxpack)
  notes/pilots_20260809/m7_complement_repose/d2_arm_a.py (anticode,
      annulus, pencil_stats)

The chart model (PREREG R0, H-CHART) generalises rh_m4t2_census.build_flat
by  background block -> canonical background pick R (|R|=u),
    2 touched petals -> t,   4 petals -> M.

Registered functionals (CATCH-19C): NSPLIT_S, NSPLIT_G, KCORE, UNION,
ANN_SIGMA, ANN_A, ANN_ACO, OVL_HIST (per config), OVL_MAX, OVL_MEAN,
PENCIL_MAX, AC_DIRECT, AC_COMP, MAXPACK_2D1, FIRE_SIGMA, FIRE_KCORE,
FIRE_UNION, SUBFIRE_MAX, FIRE3_COUNT.

Stdlib only.  Run via tools/ramguard local -- python3 ... from repo root.
"""
from __future__ import annotations

import json
import random
import sys
import time
from itertools import combinations

ROOT = "/home/u2470931/smooth-read-solomin/prize"
sys.path.insert(0, ROOT + "/notes/pilots_20260807/fpc5_diag")
sys.path.insert(0, ROOT + "/notes/pilots_20260807/mf_wall_adversary")
sys.path.insert(0, ROOT + "/notes/pilots_20260809/m7_complement_repose")
from rh_m4t2_census import (locator, pmul, prem, pgcd, pinvmod,   # noqa: E402
                            peval, pdegree, domain)
from rh_bucket import (rref_kernel, monic_chart,                  # noqa: E402
                       enumerate_split, maxpack)
from d2_arm_a import anticode, pencil_stats                       # noqa: E402


# ---------------------------------------------------- the generalised chart
def build_flat_general(R, petals, labels, touched, q, d):
    """Syndrome matrix T of the cell (R, touched petals, degree d).

    Conditions on F (monic, deg d): W = rem_P(F*G) has deg <= d, where
    P = L_R * prod_{i in touched} L_{T_i} and G = sum_i c_i e_i with e_i
    the CRT idempotents (so G == 0 mod L_R, == c_i mod L_{T_i}).
    Returns (T, P, G, rows).
    """
    facs = [locator(R, q)] + [locator(petals[i], q) for i in touched]
    P = [1]
    for f in facs:
        P = pmul(P, f, q)
    degP = pdegree(P)
    G = [0]
    for j, i in enumerate(touched):
        Li = facs[j + 1]
        Ni = [1]
        for jj, f in enumerate(facs):
            if jj != j + 1:
                Ni = pmul(Ni, f, q)
        ei = pmul(Ni, pinvmod(Ni, Li, q), q)
        c = labels[i]
        if len(ei) > len(G):
            G = G + [0] * (len(ei) - len(G))
        for m, cc in enumerate(ei):
            G[m] = (G[m] + c * cc) % q
    G = prem(G, P, q)
    rows = degP - (d + 1)
    T = [[0] * (d + 1) for _ in range(rows)]
    cur = G[:] + [0] * max(0, degP - len(G))
    for m in range(d + 1):
        for r in range(rows):
            idx = d + 1 + r
            T[r][m] = cur[idx] if idx < len(cur) else 0
        nxt = [0] + cur[:-1]
        top = cur[degP - 1]
        if top:
            f = top * pow(P[degP], q - 2, q) % q
            for i2 in range(degP + 1):
                if i2 < len(nxt):
                    nxt[i2] = (nxt[i2] - f * P[i2]) % q
        cur = nxt[:degP]
    return T, P, G, rows


def hist(vals):
    h = {}
    for v in vals:
        h[v] = h.get(v, 0) + 1
    return h


def annulus_of(sets, d):
    """(sigma, a, kappa, union, delta) + the two (PC3') orientations."""
    K = set.intersection(*sets)
    U = set.union(*sets)
    kappa, un = len(K), len(U)
    sig = un - kappa
    a = d - kappa
    ov = max(len(sets[i] & sets[j]) for i in range(len(sets))
             for j in range(i + 1, len(sets)))
    delta = d - ov
    return {"KCORE": kappa, "UNION": un, "ANN_SIGMA": sig, "ANN_A": a,
            "ANN_ACO": sig - a, "OVL_MAX": ov, "DELTA": delta,
            "FIRE_SIGMA": sig < 2 * a, "FIRE_KCORE": kappa >= 1,
            "FIRE_UNION": un < 2 * d,
            "AC_DIRECT": anticode(sig, a, delta),
            "AC_COMP": anticode(sig, sig - a, delta)}


def subfire(sets, d, exhaustive_cap=16, triple_cap=200):
    """FIRE3_COUNT (# firing triples) and SUBFIRE_MAX (largest subfamily
    of size >= 3 with its own sigma < 2a).  Exhaustive for m <= cap."""
    m = len(sets)
    if m < 3:
        return {"FIRE3_COUNT": 0, "SUBFIRE_MAX": 0, "SUBFIRE_EXHAUSTIVE": True,
                "SUBFIRE_WITNESS": None}
    fires = []
    if m <= triple_cap:
        for c in combinations(range(m), 3):
            K = sets[c[0]] & sets[c[1]] & sets[c[2]]
            U = sets[c[0]] | sets[c[1]] | sets[c[2]]
            if len(U) - len(K) < 2 * (d - len(K)):
                fires.append(c)
        n3 = len(fires)
        tri_exh = True
    else:
        n3, tri_exh = None, False
        for c in combinations(range(min(m, 60)), 3):
            K = sets[c[0]] & sets[c[1]] & sets[c[2]]
            U = sets[c[0]] | sets[c[1]] | sets[c[2]]
            if len(U) - len(K) < 2 * (d - len(K)):
                fires.append(c)
    best, wit, exh = 0, None, False
    if m <= exhaustive_cap:
        exh = True
        for size in range(m, 2, -1):
            if size <= best:
                break
            for c in combinations(range(m), size):
                K = set.intersection(*[sets[i] for i in c])
                U = set.union(*[sets[i] for i in c])
                if len(U) - len(K) < 2 * (d - len(K)):
                    if size > best:
                        best, wit = size, [sorted(sets[i]) for i in c]
                    break
    else:
        for c in fires[:2000]:
            cur = list(c)
            improved = True
            while improved:
                improved = False
                for j in range(m):
                    if j in cur:
                        continue
                    cand = cur + [j]
                    K = set.intersection(*[sets[i] for i in cand])
                    U = set.union(*[sets[i] for i in cand])
                    if len(U) - len(K) < 2 * (d - len(K)):
                        cur = cand
                        improved = True
                        break
            if len(cur) > best:
                best, wit = len(cur), [sorted(sets[i]) for i in cur]
    return {"FIRE3_COUNT": n3, "SUBFIRE_MAX": best,
            "SUBFIRE_EXHAUSTIVE": exh and tri_exh, "SUBFIRE_WITNESS": wit}


# ----------------------------------------------------------------- one config
def run_config(rng, spec, q, want_random_arm=True):
    rate, M, t, ell, b, u, d, N, n = (spec["rate"], spec["M"], spec["t"],
                                      spec["ell"], spec["b"], spec["u"],
                                      spec["d"], spec["N"], spec["n"])
    pts, cyc = domain(n, q)
    pool_all = pts[:]
    rng.shuffle(pool_all)
    core = sorted(pool_all[:N])
    bg = pool_all[N:N + b]
    petals = [pool_all[N + b + i * ell: N + b + (i + 1) * ell]
              for i in range(M)]
    labels = rng.sample(range(1, q), M)
    touched = tuple(range(t))
    untouched = [i for i in range(M) if i not in touched]

    found_split = {}           # rootset -> (R, coefs)
    found_full = {}
    per_R = []
    ranks_ok = True
    chart_pts = 0
    flat_gcd_deg = 0
    for R in combinations(bg, u):
        T, P, G, rows = build_flat_general(list(R), petals, labels,
                                           touched, q, d)
        if rows != ell - 1:
            ranks_ok = False
        basis = rref_kernel(T, d + 1, q)
        if len(basis) != d + 1 - rows:
            per_R.append({"R": list(R), "rank_deficient": True})
            continue
        v0, dirs = monic_chart(basis, d, q)
        if v0 is None:
            per_R.append({"R": list(R), "no_monic": True})
            continue
        g = v0[:]
        for dv in dirs:
            g = pgcd(g, dv, q)
        flat_gcd_deg = max(flat_gcd_deg, max(pdegree(g), 0))
        fnd, swept = enumerate_split(v0, dirs, core, d, q)
        chart_pts += swept
        ns_R, nf_R = 0, 0
        for rs, coefs in fnd.items():
            ns_R += 1
            found_split.setdefault(rs, (list(R), coefs))
            F = v0[:]
            for i2, c in enumerate(coefs):
                if c:
                    F = [(x + c * y) % q for x, y in zip(F, dirs[i2])]
            W = prem(pmul(F, G, q), P, q)
            if any(peval(W, x, q) == 0 for x in rs):
                continue                                   # gcd(F,W) != 1
            bad = False
            for iu in untouched:
                cu = labels[iu]
                for x in petals[iu]:
                    if (peval(W, x, q) - cu * peval(F, x, q)) % q == 0:
                        bad = True
                        break
                if bad:
                    break
            if bad:
                continue
            nf_R += 1
            found_full.setdefault(rs, (list(R), coefs))
        per_R.append({"R": list(R), "NSPLIT_S": ns_R, "NSPLIT_G": nf_R})

    rec = {"NSPLIT_S": len(found_split), "NSPLIT_G": len(found_full),
           "rows_is_ell_minus_1": ranks_ok, "chart_points_swept": chart_pts,
           "flat_common_gcd_deg": flat_gcd_deg,
           "per_R": per_R if len(per_R) > 1 else None,
           "mu_n_domain": cyc}

    for tag, fnd in (("S", found_split), ("G", found_full)):
        sets = [set(z) for z in fnd]
        rec["OVL_HIST_" + tag] = None
        if len(sets) >= 2:
            ov = [len(sets[i] & sets[j]) for i in range(len(sets))
                  for j in range(i + 1, len(sets))]
            rec["OVL_HIST_" + tag] = {str(k): v
                                      for k, v in sorted(hist(ov).items())}
            rec["OVL_MEAN_" + tag] = round(sum(ov) / len(ov), 4)
            rec["OVL_MAX_" + tag] = max(ov)
            an = annulus_of(sets, d)
            for k2, v in an.items():
                rec[k2 + "_" + tag] = v
            if tag == "G":
                rec.update(subfire(sets, d))
                rec["PENCIL_MAX"] = pencil_stats(list(fnd), d)["PENCIL_MAX"]
                mp, wit, exh = maxpack(list(fnd), 2 * d - 1)
                rec["MAXPACK_2D1"] = mp
                rec["MAXPACK_2D1_exhaustive"] = exh

    if want_random_arm:
        dimV = d + 1 - (ell - 1)
        while True:
            rows_r = [[rng.randrange(q) for _ in range(d + 1)]
                      for _ in range(dimV)]
            v0, dirs = monic_chart(rows_r, d, q)
            if v0 is not None and len(dirs) == dimV - 1:
                break
        fnd, _ = enumerate_split(v0, dirs, core, d, q)
        sets = [set(z) for z in fnd]
        rec["RAND_NSPLIT"] = len(sets)
        if len(sets) >= 2:
            an = annulus_of(sets, d)
            rec["RAND_FIRE_SIGMA"] = an["FIRE_SIGMA"]
            rec["RAND_FIRE_KCORE"] = an["FIRE_KCORE"]
            rec["RAND_KCORE"] = an["KCORE"]
            rec["RAND_OVL_MEAN"] = round(
                sum(len(sets[i] & sets[j]) for i in range(len(sets))
                    for j in range(i + 1, len(sets)))
                / (len(sets) * (len(sets) - 1) / 2), 4)
            rec["RAND_OVL_MAX"] = max(
                len(sets[i] & sets[j]) for i in range(len(sets))
                for j in range(i + 1, len(sets)))
            rec.update({"RAND_" + k2: v for k2, v in
                        subfire(sets, d).items() if k2 != "SUBFIRE_WITNESS"})
    return rec


# --------------------------------------------------------------- aggregation
def summarise(spec, q, recs, seed, elapsed):
    def frac(pred, cond=lambda r: True):
        den = [r for r in recs if cond(r)]
        if not den:
            return None
        return round(sum(1 for r in den if pred(r)) / len(den), 4)

    ge2 = lambda r: r.get("NSPLIT_G", 0) >= 2          # noqa: E731
    ge3 = lambda r: r.get("NSPLIT_G", 0) >= 3          # noqa: E731
    r2 = lambda r: r.get("RAND_NSPLIT", 0) >= 2        # noqa: E731
    r3 = lambda r: r.get("RAND_NSPLIT", 0) >= 3        # noqa: E731
    merged_g, merged_s = {}, {}
    for r in recs:
        for k, v in (r.get("OVL_HIST_G") or {}).items():
            merged_g[k] = merged_g.get(k, 0) + v
        for k, v in (r.get("OVL_HIST_S") or {}).items():
            merged_s[k] = merged_s.get(k, 0) + v
    ns_g = [r["NSPLIT_G"] for r in recs]
    ns_s = [r["NSPLIT_S"] for r in recs]
    out = {
        "cell": spec, "q": q, "seed": seed, "configs": len(recs),
        "rows_is_ell_minus_1_all": all(r["rows_is_ell_minus_1"]
                                       for r in recs),
        "flat_gcd_nontrivial_configs": sum(
            1 for r in recs if r["flat_common_gcd_deg"] > 0),
        "NSPLIT_S_mean": round(sum(ns_s) / len(recs), 4) if recs else 0,
        "NSPLIT_G_mean": round(sum(ns_g) / len(recs), 4) if recs else 0,
        "NSPLIT_G_max": max(ns_g, default=0),
        "NSPLIT_G_hist": {str(k): v for k, v in sorted(hist(ns_g).items())},
        "guard_survival_G_over_S": (round(sum(ns_g) / sum(ns_s), 4)
                                    if sum(ns_s) else None),
        "configs_NSPLIT_G_ge2": sum(1 for r in recs if ge2(r)),
        "configs_NSPLIT_G_ge3": sum(1 for r in recs if ge3(r)),
        "OVL_HIST_G_MERGED": dict(sorted(merged_g.items(),
                                         key=lambda x: int(x[0]))),
        "OVL_HIST_S_MERGED": dict(sorted(merged_s.items(),
                                         key=lambda x: int(x[0]))),
        "OVL_MEAN_G_over_configs": (
            round(sum(r["OVL_MEAN_G"] for r in recs if ge2(r))
                  / max(1, sum(1 for r in recs if ge2(r))), 4)),
        "OVL_MAX_G_observed": max((r.get("OVL_MAX_G", 0) for r in recs),
                                  default=0),
        "OVL_MAX_G_eq_rJ_configs": sum(
            1 for r in recs if r.get("OVL_MAX_G") == spec["r_J"]),
        "FIRE_KCORE_frac_ge2": frac(lambda r: r.get("FIRE_KCORE_G"), ge2),
        "FIRE_KCORE_frac_ge3": frac(lambda r: r.get("FIRE_KCORE_G"), ge3),
        "FIRE_UNION_frac_ge2": frac(lambda r: r.get("FIRE_UNION_G"), ge2),
        "FIRE_SIGMA_frac_ge3": frac(lambda r: r.get("FIRE_SIGMA_G"), ge3),
        "FIRE_SIGMA_count_ge3": sum(1 for r in recs
                                    if ge3(r) and r.get("FIRE_SIGMA_G")),
        "SUBFIRE_MAX_hist": {str(k): v for k, v in sorted(hist(
            [r.get("SUBFIRE_MAX", 0) for r in recs if ge3(r)]).items())},
        "SUBFIRE_all_exhaustive": all(r.get("SUBFIRE_EXHAUSTIVE", True)
                                      for r in recs if ge3(r)),
        "KCORE_G_max": max((r.get("KCORE_G", 0) for r in recs), default=0),
        "PENCIL_MAX_hist": {str(k): v for k, v in sorted(hist(
            [r.get("PENCIL_MAX", 0) for r in recs if ge2(r)]).items())},
        "MAXPACK_2D1_hist": {str(k): v for k, v in sorted(hist(
            [r.get("MAXPACK_2D1", 0) for r in recs if ge2(r)]).items())},
        "MAXPACK_2D1_all_exhaustive": all(r.get("MAXPACK_2D1_exhaustive",
                                                True) for r in recs if ge2(r)),
        "AC_DIRECT_G_vals": sorted({r.get("AC_DIRECT_G") for r in recs
                                    if ge2(r)} - {None}),
        "AC_COMP_G_vals": sorted({r.get("AC_COMP_G") for r in recs
                                  if ge2(r)} - {None}),
        # ---- matched random-flat power control (PREREG R3)
        "RAND_NSPLIT_mean": round(sum(r.get("RAND_NSPLIT", 0) for r in recs)
                                  / max(1, len(recs)), 4),
        "RAND_configs_ge2": sum(1 for r in recs if r2(r)),
        "RAND_configs_ge3": sum(1 for r in recs if r3(r)),
        "RAND_FIRE_KCORE_frac_ge2": frac(lambda r: r.get("RAND_FIRE_KCORE"),
                                         r2),
        "RAND_FIRE_KCORE_frac_ge3": frac(lambda r: r.get("RAND_FIRE_KCORE"),
                                         r3),
        "RAND_FIRE_SIGMA_frac_ge3": frac(lambda r: r.get("RAND_FIRE_SIGMA"),
                                         r3),
        "RAND_FIRE_SIGMA_count_ge3": sum(1 for r in recs if r3(r)
                                         and r.get("RAND_FIRE_SIGMA")),
        "RAND_OVL_MEAN": (round(sum(r["RAND_OVL_MEAN"] for r in recs if r2(r))
                                / max(1, sum(1 for r in recs if r2(r))), 4)),
        "RAND_OVL_MAX_observed": max((r.get("RAND_OVL_MAX", 0)
                                      for r in recs), default=0),
        "elapsed_s": round(elapsed, 1),
    }
    return out


SPECS = {}


def add_spec(cid, rate, M, t, ell, b, u, q=None):
    S = M * ell + b
    k = (S - 1) if rate == 2 else (S - 1) // (rate - 1)
    n, N = rate * k, k - 1
    d = (t - 1) * ell + u
    SPECS[cid] = {"id": cid, "rate": rate, "M": M, "t": t, "ell": ell,
                  "b": b, "u": u, "d": d, "h": t * ell,
                  "e": 2 * d + 1 - t * ell, "r_J": 2 * d - t * ell,
                  "N": N, "n": n, "k": k, "q": q}


for args in [("C1", 2, 5, 2, 2, 1, 1, 23), ("C2", 2, 8, 2, 2, 1, 1, 37),
             ("C3", 2, 16, 2, 2, 1, 1, 67), ("C4", 2, 5, 2, 3, 2, 2, 37),
             ("C5", 2, 8, 2, 3, 2, 2, 53), ("C6", 2, 5, 2, 4, 3, 3, 47),
             ("C7", 2, 6, 2, 4, 3, 3, 53), ("C8", 2, 5, 3, 2, 1, 1, 23),
             ("C9", 2, 8, 3, 2, 1, 1, 37), ("C10", 4, 18, 2, 2, 1, 1, 53),
             ("C11", 4, 24, 2, 2, 1, 1, 67), ("C12", 8, 42, 2, 2, 1, 1, 97),
             ("C13", 16, 120, 2, 2, 1, 1, 257),
             ("C1b", 2, 5, 2, 2, 1, 1, 47), ("C2b", 2, 8, 2, 2, 1, 1, 67),
             ("T1", 2, 8, 2, 4, 3, 1, 71), ("T2", 2, 8, 2, 4, 3, 2, 71),
             ("T3", 2, 8, 2, 4, 3, 3, 71),
             ("F1", 4, 15, 3, 2, 1, 1, 41), ("F2", 8, 35, 3, 2, 1, 1, 83),
             ("S1", 4, 7, 2, 3, 1, 1, 29),
             ("K1", 2, 5, 2, 3, 1, 1, 31), ("K2", 4, 12, 2, 2, 1, 1, 37),
             ("K3", 8, 28, 2, 2, 1, 1, 67), ("K4", 4, 12, 3, 2, 1, 1, 37)]:
    add_spec(*args)


def main():
    cid = sys.argv[1]
    nconfig = int(sys.argv[2])
    seed = int(sys.argv[3])
    outfile = sys.argv[4] if len(sys.argv) > 4 else ""
    tlimit = float(sys.argv[5]) if len(sys.argv) > 5 else 1e9
    spec = SPECS[cid]
    q = spec["q"]
    rng = random.Random(seed)
    recs = []
    t0 = time.time()
    for _ in range(nconfig):
        if time.time() - t0 > tlimit:
            break
        recs.append(run_config(rng, spec, q))
    out = summarise(spec, q, recs, seed, time.time() - t0)
    if outfile:
        with open(outfile, "w") as fh:
            json.dump({"summary": out, "recs": recs}, fh, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
