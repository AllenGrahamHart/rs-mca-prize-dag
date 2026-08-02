#!/usr/bin/env python3
"""Adversarial constructions for the band-occupancy lemma.

Groups (CLI):
  sun    the SUNFLOWER family: m cores of size k+d through a common
         lambda-set, lambda = k+2d-h, so that EVERY pair of cores forces a
         live slope of support exactly A (the interaction strip at equality
         d_1+d_2 = h-1).  Saturates the line cap L(d) by construction.
  multi  several sunflowers (disjoint / point-sharing) -- attempts to beat
         the one-sunflower law N_d ~ n/(h-d).
  climb  hill-climb on the received pair maximising N_total under the
         exhaustive admissibility gate.
  growth aggregation of the max admissible N over n for the growth law.

Run: tools/ramguard local -- python3 <this> <group>
"""
import json
import random
import sys
import time

sys.dont_write_bytecode = True
HERE = ("/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/"
        "xr_band_occupancy")
sys.path.insert(0, HERE)
from occlib import Row, measure, plant_cores  # noqa: E402

OUT = []


def sunflower_cores(k, h, d, m, offset=0):
    """m cores of size k+d pairwise meeting in exactly lam = k+2d-h.

    Returns (cores, lam, n_needed).  Y = [offset .. offset+lam-1];
    each core adds h-d fresh points.
    """
    lam = k + 2 * d - h
    if lam < 0 or lam > k - 1:
        return None, lam, None
    Y = list(range(offset, offset + lam))
    cores, nxt = [], offset + lam
    for _ in range(m):
        F = list(range(nxt, nxt + (h - d)))
        nxt += h - d
        cores.append(Y + F)
    return cores, lam, nxt


def run_sunflower(n, k, t, q, d, m, seed, tag=""):
    row = Row(n, k, t, q)
    h = row.h
    cores, lam, need = sunflower_cores(k, h, d, m)
    if cores is None or need > n:
        return None
    try:
        u, v, built = plant_cores(row, cores, {}, seed)
    except ValueError as e:
        return dict(fixture=f"SUN{tag}-n{n}-k{k}-t{t}-d{d}-m{m}-s{seed}",
                    error=str(e))
    rec, pairs, band = measure(row, u, v,
                               f"SUN{tag}-n{n}-k{k}-t{t}-d{d}-m{m}-s{seed}")
    rec["construction"] = dict(kind="sunflower", d=d, m=m, lam=lam,
                               points_used=need,
                               predicted_N_d=m,
                               predicted_L_P=m - 1,
                               line_cap=(row.R - d) // (h - d))
    return rec


def run_multi_sunflower(n, k, t, q, d, m, s, seed, share=0, tag=""):
    """s sunflowers, each with m cores; consecutive sunflowers overlap in
    `share` fresh points (share=0 -> fully disjoint)."""
    row = Row(n, k, t, q)
    h = row.h
    allcores, off = [], 0
    for _ in range(s):
        cores, lam, nxt = sunflower_cores(k, h, d, m, offset=off)
        if cores is None or nxt > n:
            return None
        allcores += cores
        off = nxt - share
    try:
        u, v, built = plant_cores(row, allcores, {}, seed)
    except ValueError as e:
        return dict(fixture=f"MULTI{tag}-n{n}-d{d}-m{m}-s{s}-sh{share}-{seed}",
                    error=str(e))
    rec, pairs, band = measure(
        row, u, v, f"MULTI{tag}-n{n}-k{k}-t{t}-d{d}-m{m}-s{s}-sh{share}-{seed}")
    rec["construction"] = dict(kind="multi-sunflower", d=d, m=m, sunflowers=s,
                               share=share, cores=len(allcores),
                               points_used=off + share,
                               predicted_N_d=s * m)
    return rec


def hill_climb(n, k, t, q, seed, iters, restarts=1):
    """maximise N_total subject to ADMISSIBLE; single-coordinate moves."""
    row = Row(n, k, t, q)
    rnd = random.Random(seed)
    best = None
    for _ in range(restarts):
        u = [rnd.randrange(q) for _ in range(n)]
        v = [rnd.randrange(1, q) for _ in range(n)]
        rec, _, _ = measure(row, u, v, "climb", want_checks=False)
        cur = rec["N_total"] if rec["ADMISSIBLE"] else -1
        for it in range(iters):
            i = rnd.randrange(n)
            ou, ov = u[i], v[i]
            u[i] = rnd.randrange(q)
            v[i] = rnd.randrange(1, q)
            r2, _, _ = measure(row, u, v, "climb", want_checks=False)
            sc = r2["N_total"] if r2["ADMISSIBLE"] else -1
            if sc >= cur:
                cur, rec = sc, r2
            else:
                u[i], v[i] = ou, ov
        if best is None or cur > best[0]:
            full, _, _ = measure(row, u, v, f"CLIMB-n{n}-k{k}-t{t}-s{seed}")
            best = (cur, full)
    return best[1] if best else None


def main():
    grp = sys.argv[1] if len(sys.argv) > 1 else "sun"
    t0 = time.time()

    if grp == "sun":
        # h=3 d=1 family (lam = k-1) across n; then h=4 d=1 (lam = k-2)
        for (n, k, t, q) in [(16, 3, 3, 4001), (20, 3, 3, 4001),
                             (24, 3, 3, 4001), (28, 3, 3, 4001),
                             (32, 3, 3, 4001), (40, 3, 3, 4001),
                             (48, 3, 3, 4001), (56, 3, 3, 4001),
                             (64, 3, 3, 4001)]:
            mmax = (n - (k - 1)) // 2
            for m in (mmax, mmax - 1):
                if m < 3:
                    continue
                for seed in (101, 102):
                    r = run_sunflower(n, k, t, q, 1, m, seed)
                    if r:
                        OUT.append(r)
                        report(r)
                if OUT and OUT[-1].get("ADMISSIBLE"):
                    break
        for (n, k, t, q) in [(20, 4, 4, 4001), (28, 4, 4, 4001),
                             (36, 4, 4, 4001), (44, 4, 4, 4001)]:
            mmax = (n - (k - 2)) // 3
            for m in (mmax, mmax - 1, mmax - 2):
                if m < 3:
                    continue
                done = False
                for seed in (201, 202):
                    r = run_sunflower(n, k, t, q, 1, m, seed, tag="h4")
                    if r:
                        OUT.append(r)
                        report(r)
                        done = done or r.get("ADMISSIBLE", False)
                if done:
                    break

    if grp == "odd5":
        # h=5, d=2: lam = k-1 again, union = k+2d+1 = A -> automatic live slope
        for (n, k, t, q) in [(16, 3, 5, 4001), (22, 3, 5, 4001),
                             (28, 3, 5, 4001), (34, 3, 5, 4001),
                             (40, 3, 5, 4001), (52, 3, 5, 4001)]:
            mmax = (n - (k - 1)) // 3
            for m in (mmax, mmax - 1):
                if m < 3:
                    continue
                hit = False
                for seed in (501, 502):
                    r = run_sunflower(n, k, t, q, 2, m, seed, tag="d2")
                    if r:
                        OUT.append(r)
                        report(r)
                        hit = hit or r.get("ADMISSIBLE", False)
                if hit:
                    break

    if grp == "multi":
        for (n, k, t, q) in [(24, 3, 3, 4001), (32, 3, 3, 4001),
                             (40, 3, 3, 4001), (48, 3, 3, 4001),
                             (64, 3, 3, 4001)]:
            for (m, s, share) in [(3, (n - 2) // 8, 0), (4, (n - 2) // 10, 0),
                                  (3, (n - 2) // 6, 2), (5, (n - 2) // 12, 0),
                                  (3, (n - 2) // 5, 3)]:
                if s < 2 or m < 3:
                    continue
                for seed in (301, 302):
                    r = run_multi_sunflower(n, k, t, q, 1, m, s, seed,
                                            share=share)
                    if r:
                        OUT.append(r)
                        report(r)

    if grp == "climb":
        for (n, k, t, q, it) in [(16, 3, 3, 401, 300), (20, 3, 3, 401, 300),
                                 (24, 3, 3, 401, 250), (28, 3, 3, 401, 200),
                                 (16, 3, 3, 101, 300), (20, 3, 4, 401, 250)]:
            for seed in (401, 402):
                r = hill_climb(n, k, t, q, seed, it)
                if r:
                    OUT.append(r)
                    report(r)

    path = f"{HERE}/battery_{grp}.json"
    json.dump(OUT, open(path, "w"), indent=1, default=str)
    print(f"\n[{time.time()-t0:.1f}s] checkpoint: {path}")


def report(r):
    if "error" in r:
        print(f"  {r['fixture']}: BUILD ERROR {r['error']}")
        return
    c = r.get("construction", {})
    print(f"\n### {r['fixture']}  n={r['n']} k={r['k']} t={r['t']} A={r['A']} "
          f"h={r['h']} band={r['band']} q={r['q']}")
    print(f"  ADMISSIBLE={r['ADMISSIBLE']} (generic {r['globally_generic']} "
          f"maxJ={r['max_joint_agreement']} / tangent-free "
          f"{r['tangent_free_finite_slopes']} maxray={r['max_ray_agreement']} / "
          f"v-dir gate {r['tangent_free_v_direction']} vmax="
          f"{r['max_v_side_agreement']})")
    if c:
        print(f"  construction: {c}")
    print(f"  ledger: {r['ledger_by_depth']}")
    print(f"  N_total={r['N_total']}  N/n={r['N_over_n']:.3f}  "
          f"N/n^2={r['N_over_n2']:.5f}  X_total={r['X_total']}  "
          f"sum_L={r['sum_L_over_band_pairs']}")
    print(f"  |Gamma_band| measured = {r['Gamma_band_measured']}   "
          f"ledger bound sum N_d L(d) = {r['ledger_bound_sum_Nd_L']}   "
          f"slack = {r['ledger_slack_vs_measured']}")
    if "kpacking_ok" in r:
        print(f"  checks: kpack={r['kpacking_ok']}({r['kpacking_max_intersection']}) "
              f"T1={r['T1_ok']}({r['T1_shared_fibre_pairs']} shared-fibre pairs) "
              f"T2={r['T2_ok']} T3={r['T3_ok']} spread={r['spread_coset_ok']} "
              f"fibre_id_viol={r['fibre_identity_violations']} "
              f"rays/slope={r['max_rays_per_slope']}(resel {r['reselection_slopes']}) "
              f"maxlines/slope={r['max_lines_per_slope']} "
              f"max f-mult={r['max_pairs_sharing_f_at_a_depth']} "
              f"g-mult={r['max_pairs_sharing_g_at_a_depth']}")


if __name__ == "__main__":
    main()
