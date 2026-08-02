#!/usr/bin/env python3
"""F2A.5b measurement stages -- the hypothesis boundary map.

Run (always chunked, one p per invocation for the heavy stages):

  tools/ramguard local -- python3 .../experiments.py ramp 23
  tools/ramguard local -- python3 .../experiments.py killers 23
  tools/ramguard local -- python3 .../experiments.py climb 23 32
  tools/ramguard local -- python3 .../experiments.py margin
  tools/ramguard local -- python3 .../experiments.py weight
  tools/ramguard local -- python3 .../experiments.py census

Every banked number in *_counts / *_floor fields is an EXACT integer or an
exact-integer-derived log2; Lambda / |R_k| / certified_bits are FLOAT
diagnostics and are named as such.
"""

from __future__ import annotations

import collections
import json
import math
import os
import random
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import boundary as B  # noqa: E402
from slicecore import abs_pairs, elem_sym, slice_coeffs_carrydp  # noqa: E402

CS = ((1, 1), (2, 3))


# ================================================================== ramp ====
def stage_ramp(p: int):
    """The parity ramp: j EVEN-Delta coordinates among n, j = 0..n/2."""
    rows = []
    print(f"[RAMP p={p}] exact integer proxy; worst slice over b in [n/4,3n/4]")
    print(f"{'c':>7} {'n':>4} {'j':>4} {'beta_min':>9} {'worst b':>7} "
          f"{'-log2 rho':>10} {'eta_n':>7} {'k=p floor':>10} "
          f"{'central':>8} {'cen k=p':>8} {'minLam*n':>9} {'k*':>4} "
          f"{'cert':>7} {'1-|R|max':>9}")
    for c in CS:
        c = (c[0] % p, c[1] % p)
        for n in (32, 48, 64, 96):
            js = sorted({0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, n // 2}
                        & set(range(0, n // 2 + 1)))
            for j in js:
                w = B.parity_ramp_window(p, c, n, j)
                if w is None:
                    continue
                dl, base, sel = w
                row, V = B.summarise(p, dl, base, tag=f"ramp_j{j}", grid=256)
                row["c"] = list(c)
                row["j_even"] = j
                rows.append(row)
                print(f"{str(c):>7} {n:4d} {j:4d} {row['beta_min']:9.4f} "
                      f"{row['worst_b']:7d} {row['worst_neglog2']:10.4f} "
                      f"{row['eta_n']:7.4f} "
                      f"{(row['kp_floor_bits'] or float('nan')):10.4f} "
                      f"{(row['central_neglog2'] or float('nan')):8.3f} "
                      f"{(row['central_kp_floor_bits'] or float('nan')):8.3f} "
                      f"{row['min_Lambda']*n:9.4f} {row['min_Lambda_k']:4d} "
                      f"{row['certified_bits']:7.2f} "
                      f"{1-row['flatness_max_absR']:9.4f}")
    B.dump(f"ramp_p{p}.json", {"p": p, "rows": rows})


# =============================================================== killers ====
def _families(p, c, n):
    """Named candidate killer classes, all realised INSIDE the model."""
    D, S, loc = B.model(p, c)
    ctr = collections.Counter(D)
    two_p = 2 * p
    out = {}
    out["generic"] = B.generic_window(p, c, n)
    out["all_odd"] = B.parity_ramp_window(p, c, n, 0)
    out["all_even"] = B.parity_ramp_window(p, c, n, n)
    out["balanced_parity"] = B.parity_ramp_window(p, c, n, n // 2)
    out["coset_trivial"] = B.subgroup_coset_window(p, c, n, "trivial")
    out["coset_order2"] = B.subgroup_coset_window(p, c, n, "order2")
    for wdt in (2, 3, 5, 9, 17):
        out[f"arc{wdt}"] = B.arc_window(p, c, n, wdt)
    # the adversarial one: an ADJACENT Delta pair (opposite parities, so the
    # window is parity-BALANCED) with the largest joint multiplicity.
    best, bv = -1, None
    for a in range(two_p):
        t = min(ctr.get(a, 0), ctr.get((a + 1) % two_p, 0))
        if t > best:
            best, bv = t, {a, (a + 1) % two_p}
    out["adjacent_pair"] = B.value_window(p, c, n, bv) if 2 * best >= n else None
    # three consecutive values, balanced
    best3, bv3 = -1, None
    for a in range(two_p):
        vs = [(a + t) % two_p for t in range(3)]
        t = min(ctr.get(v, 0) for v in vs)
        if t > best3:
            best3, bv3 = t, set(vs)
    out["adjacent_triple"] = B.value_window(p, c, n, bv3) if 3 * best3 >= n else None
    # few distinct values, spread out (high multiplicity, NOT concentrated)
    top = [v for v, _ in ctr.most_common(4)]
    out["fewvalue_top4"] = B.value_window(p, c, n, set(top))
    top2 = [v for v, _ in ctr.most_common(2)]
    out["fewvalue_top2"] = B.value_window(p, c, n, set(top2))
    # coordinates whose Delta is congruent to a fixed residue mod a small d
    for d in (3, 5):
        if (2 * p) % d:
            best_r, bc_ = 0, -1
            for rr in range(d):
                t = sum(m for v, m in ctr.items() if v % d == rr)
                if t > bc_:
                    best_r, bc_ = rr, t
            vs = {v for v in ctr if v % d == best_r}
            out[f"modclass{d}"] = B.value_window(p, c, n, vs)
    return out


def stage_killers(p: int):
    rows = []
    print(f"[KILLERS p={p}] named window classes; exact integer proxy")
    print(f"{'c':>7} {'n':>4} {'family':>16} {'beta_min':>9} {'#Dvals':>7} "
          f"{'worst b':>7} {'-log2 rho':>10} {'eta_n':>7} {'k=p floor':>10} "
          f"{'minLam*n':>9} {'k*':>4} {'cert':>7} {'1-|R|max':>9}")
    for c in CS:
        c = (c[0] % p, c[1] % p)
        for n in (32, 48, 64):
            fams = _families(p, c, n)
            for name, w in fams.items():
                if w is None:
                    continue
                dl, base, sel = w
                row, V = B.summarise(p, dl, base, tag=name, grid=256)
                row["c"] = list(c)
                row["family"] = name
                rows.append(row)
                print(f"{str(c):>7} {n:4d} {name:>16} {row['beta_min']:9.4f} "
                      f"{row['distinct_delta']:7d} "
                      f"{row['worst_b']:7d} {row['worst_neglog2']:10.4f} "
                      f"{row['eta_n']:7.4f} "
                      f"{(row['kp_floor_bits'] or float('nan')):10.4f} "
                      f"{row['min_Lambda']*n:9.4f} {row['min_Lambda_k']:4d} "
                      f"{row['certified_bits']:7.2f} "
                      f"{1-row['flatness_max_absR']:9.4f}")
    B.dump(f"killers_p{p}.json", {"p": p, "rows": rows})


# ================================================================= climb ====
def _objective(p, deltas, base, n, lo=0.25, hi=0.75):
    """EXACT: the worst (smallest) -log2 rho_b over the central band.

    Returned as an exact comparable pair (log via Fractions is overkill; we
    compare |V_b| * C_ref vs |V_ref| * C_b with integers).
    """
    V = B.V_exact(p, deltas, base)
    best = None
    for b in B.band(n, lo, hi):
        v = abs(V[b])
        C = math.comb(n, b)
        if v == 0:
            continue
        if best is None or v * best[1] > best[0] * C:  # v/C > best_v/best_C
            best = (v, C, b)
    return best


def stage_climb(p: int, n: int, iters: int = 25, cand: int = 12, seed: int = 7):
    """Hill-climb the window choice against the EXACT integer objective."""
    rng = random.Random(seed)
    out = []
    for c in CS:
        c = (c[0] % p, c[1] % p)
        D, S, loc = B.model(p, c)
        m = len(D)
        # calibration: the known all-odd killer must be found/kept
        for start in ("random", "generic", "all_odd", "adjacent_pair"):
            if start == "random":
                sel = rng.sample(range(m), n)
            elif start == "generic":
                sel = list(range(n))
            elif start == "all_odd":
                w = B.parity_ramp_window(p, c, n, 0)
                if w is None:
                    continue
                sel = w[2]
            else:
                w = _families(p, c, n).get("adjacent_pair")
                if w is None:
                    continue
                sel = w[2]
            sel = list(sel)
            cur = _objective(p, [D[i] for i in sel],
                             sum(S[i] for i in sel) % (2 * p), n)
            hist = [math.log2(cur[1]) - math.log2(cur[0])]
            for _ in range(iters):
                improved = False
                pool = [i for i in rng.sample(range(m), min(cand * 3, m))
                        if i not in set(sel)][:cand]
                for pos in rng.sample(range(n), min(4, n)):
                    for q in pool:
                        trial = list(sel)
                        trial[pos] = q
                        o = _objective(p, [D[i] for i in trial],
                                       sum(S[i] for i in trial) % (2 * p), n)
                        if o is None:
                            continue
                        if o[0] * cur[1] > cur[0] * o[1]:
                            sel, cur, improved = trial, o, True
                    if improved:
                        break
                hist.append(math.log2(cur[1]) - math.log2(cur[0]))
                if not improved:
                    break
            dl = [D[i] for i in sel]
            base = sum(S[i] for i in sel) % (2 * p)
            row, V = B.summarise(p, dl, base, tag=f"climb_{start}", grid=256)
            row["c"] = list(c)
            row["start"] = start
            row["hist"] = hist
            row["delta_multiset"] = sorted(collections.Counter(dl).items())
            out.append(row)
            print(f"p={p} c={c} n={n} start={start:8s} "
                  f"-log2 rho: {hist[0]:8.3f} -> {hist[-1]:8.3f} "
                  f"(eta {hist[-1]/n:.4f}) beta_min={row['beta_min']:.4f} "
                  f"#Dvals={row['distinct_delta']:3d} "
                  f"1-|R|max={1-row['flatness_max_absR']:.4f} "
                  f"minLam*n={row['min_Lambda']*n:.3f} k*={row['min_Lambda_k']}")
    B.dump(f"climb_p{p}_n{n}.json", {"p": p, "n": n, "rows": out})


# ============================================================== arcscale ====
def stage_arcscale():
    """How far in n does the ADJACENT-PAIR (arc-2) killer survive, and how
    large a window does the model actually realise?  Exact integers."""
    print("[A1] MODEL-REALISED adjacent-pair windows (Delta in {a, a+1}), "
          "exact integer proxy over the full available multiplicity")
    print(f"{'p':>5} {'c':>7} {'a':>4} {'n_avail':>8} {'n':>5} {'beta_min':>9} "
          f"{'worst b':>7} {'-log2 rho':>10} {'eta_n':>8} {'>1/43':>6}")
    rows = []
    for p in (23, 41, 67, 101, 151):
        for c in CS:
            c = (c[0] % p, c[1] % p)
            D, S, loc = B.model(p, c)
            ctr = collections.Counter(D)
            two_p = 2 * p
            best, ba = -1, None
            for a in range(two_p):
                t = min(ctr.get(a, 0), ctr.get((a + 1) % two_p, 0))
                if t > best:
                    best, ba = t, a
            avail = ctr.get(ba, 0) + ctr.get((ba + 1) % two_p, 0)
            for n in (16, 32, 48, 64, 96, 128, 160, 192):
                if n > avail:
                    continue
                w = B.value_window(p, c, n, {ba, (ba + 1) % two_p})
                if w is None:
                    continue
                dl, base, _ = w
                V = B.V_exact(p, dl, base)
                x, xb = B.worst_in_band(V, n)
                bm = B.beta_min(dl)
                rows.append({"p": p, "c": list(c), "a": ba, "n_avail": avail,
                             "n": n, "beta_min": bm, "worst_b": xb,
                             "worst_neglog2": x, "eta_n": (x / n) if x else 0.0,
                             "V_worst": V[xb] if xb is not None else None,
                             "C_worst": math.comb(n, xb) if xb is not None else None})
                print(f"{p:5d} {str(c):>7} {ba:4d} {avail:8d} {n:5d} {bm:9.4f} "
                      f"{xb:7d} {x:10.5f} {x/n:8.5f} "
                      f"{'Y' if x/n > 1/43 else 'n':>6}")
    B.dump("arcscale_model.json", {"rows": rows})

def stage_arcsynth():
    """[A2] SYNTHETIC balanced two-value windows Delta in {v, v+1}: how far in
    n does the total-death regime run?  Exact integers, O(n) per slice."""
    print("[A2] SYNTHETIC adjacent-pair window (n/2 coords with Delta=0, n/2 "
          "with Delta=1), beta_min = 1/2 exactly; exact integer V_b")
    print(f"{'p':>6} {'n':>8} {'n/p^2':>10} {'worst b':>9} {'-log2 rho':>11} "
          f"{'eta_n':>10} {'>1/43':>6} {'>1/3':>5}")
    rows2 = []
    for p in (23, 41, 101, 251, 1009, 65537):
        ns = [32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
        for n in ns:
            if n < 4 * p and p > 1000:
                continue
            if n > 40 * p * p:
                continue
            bs = sorted({max(1, n // 4), 3 * n // 8, n // 2, 5 * n // 8,
                         min(n - 1, 3 * n // 4)})
            V = B.V_two_value_at(p, n // 2, n // 2, 0, 1, 0, bs)
            best, bb = None, None
            for b in bs:
                x = B.neglog2_rho(V[b], n, b)
                if x is None:
                    continue
                if best is None or x < best:
                    best, bb = x, b
            if best is None:
                continue
            rows2.append({"p": p, "n": n, "worst_b": bb, "worst_neglog2": best,
                          "eta_n": best / n, "n_over_p2": n / (p * p),
                          "log2_absV": (math.log2(abs(V[bb]))
                                        if V[bb] else None),
                          "log2_C": math.log2(math.comb(n, bb))})
            print(f"{p:6d} {n:8d} {n/(p*p):10.5f} {bb:9d} {best:11.5f} "
                  f"{best/n:10.7f} {'Y' if best/n > 1/43 else 'n':>6} "
                  f"{'Y' if best/n > 1/3 else 'n':>5}")
    B.dump("arcscale_synth.json", {"rows": rows2})


# ============================================================== flatscan ====
def stage_flatscan(p: int, n: int = 48, seed: int = 11):
    """THE BOUNDARY MAP.  Sample many windows of the same size and ask which
    candidate dial actually predicts the exact exponent:

      beta_min          = min(#odd,#even)/n            (the parity clause)
      1 - max_k |R_k|   = Fourier flatness of Delta    (the proposed clause)
      n * min_k Lambda_k= the sharp Cauchy exponent    (the sharp clause)

    Reported as the LOWER ENVELOPE of the exact eta over bins of each dial:
    a dial is usable iff its lower envelope is bounded away from 0.
    """
    rng = random.Random(seed)
    rows = []
    for c in CS:
        c = (c[0] % p, c[1] % p)
        D, S, loc = B.model(p, c)
        m = len(D)
        vals = sorted(set(D))
        cand = []
        for _ in range(90):                    # uniformly random windows
            cand.append(("random", rng.sample(range(m), n)))
        for _ in range(70):                    # random Delta-value sets
            k = rng.randint(1, max(2, len(vals) // 2))
            vs = set(rng.sample(vals, k))
            pool = [i for i in range(m) if D[i] in vs]
            if len(pool) >= n:
                cand.append(("valueset", rng.sample(pool, n)))
        for j in range(0, n // 2 + 1, 2):      # the parity ramp
            w = B.parity_ramp_window(p, c, n, j)
            if w:
                cand.append((f"ramp{j}", w[2]))
        for wd in range(1, 2 * p, 2):          # arcs of every width
            w = B.arc_window(p, c, n, wd)
            if w:
                cand.append((f"arc{wd}", w[2]))
        for name, sel in cand:
            dl = [D[i] for i in sel]
            base = sum(S[i] for i in sel) % (2 * p)
            V = B.V_exact(p, dl, base)
            x, xb = B.worst_in_band(V, n)
            if x is None:
                continue
            fm, fk, _ = B.flatness(p, dl)
            mp_ = B.mode_profile(p, dl, xb, grid=256)
            rows.append({"p": p, "c": list(c), "n": n, "kind": name,
                         "worst_b": xb, "worst_neglog2": x, "eta_n": x / n,
                         "beta_min": B.beta_min(dl),
                         "flat": 1 - fm, "flat_argk": fk,
                         "minLam_n": mp_["min_Lambda"] * n,
                         "minLam_k": mp_["min_Lambda_k"],
                         "distinct": len(set(dl))})
    B.dump(f"flatscan_p{p}_n{n}.json", {"p": p, "n": n, "rows": rows})

    def envelope(key, edges, label):
        print(f"\n  lower envelope of eta_n over bins of {label} "
              f"(p={p}, n={n}, {len(rows)} exact windows)")
        print(f"    {'bin':>18} {'#win':>5} {'min eta_n':>10} "
              f"{'median eta':>11} {'max eta_n':>10}")
        for a, bnd in zip(edges, edges[1:]):
            sel = [r for r in rows if a <= r[key] < bnd]
            if not sel:
                continue
            es = sorted(r["eta_n"] for r in sel)
            print(f"    [{a:7.4f},{bnd:7.4f}) {len(sel):5d} {es[0]:10.5f} "
                  f"{es[len(es)//2]:11.5f} {es[-1]:10.5f}")

    print(f"\n[FLATSCAN p={p} n={n}] which dial has a usable lower envelope?")
    envelope("beta_min", [0, .001, .05, .1, .15, .2, .25, .3, .35, .4, .45, .51],
             "beta_min  (the PARITY clause)")
    envelope("flat", [0, .001, .01, .03, .06, .1, .2, .3, .45, .6, 1.01],
             "1 - max_k |R_k|  (FOURIER FLATNESS)")
    envelope("minLam_n", [0, .5, 1, 2, 4, 8, 12, 16, 20, 25, 30, 1e9],
             "n * min_k Lambda_k  (the SHARP Cauchy exponent)")

    # the headline pair: worst window that PASSES a parity hypothesis
    print(f"\n  worst exact eta_n among windows with beta_min >= 0.25:")
    sel = sorted((r for r in rows if r["beta_min"] >= 0.25),
                 key=lambda r: r["eta_n"])[:6]
    for r in sel:
        print(f"    kind={r['kind']:>10} beta_min={r['beta_min']:.4f} "
              f"eta_n={r['eta_n']:.6f} flat={r['flat']:.5f} "
              f"minLam*n={r['minLam_n']:.3f} k*={r['minLam_k']}")
    print(f"  worst exact eta_n among windows with 1-max|R_k| >= 0.30:")
    sel = sorted((r for r in rows if r["flat"] >= 0.30),
                 key=lambda r: r["eta_n"])[:6]
    for r in sel:
        print(f"    kind={r['kind']:>10} beta_min={r['beta_min']:.4f} "
              f"eta_n={r['eta_n']:.6f} flat={r['flat']:.5f} "
              f"minLam*n={r['minLam_n']:.3f} k*={r['minLam_k']}")


# ================================================================ margin ====
def stage_margin():
    """Model-free sharpness of the PARITY clause.

    The k=p mode's own slice ratio needs only (n_o, n_e, b) -- exact
    Krawtchouk integers -- so it extrapolates to the official prime p ~ 2^31
    with NO proxy, NO model and NO float algebra in the core quantity.

    lambda(beta_min, beta) := (1/n) * (-log2 |Kr| / C(n,b)) is measured at
    n = 2048 (exact) and shown to be n-stable; the k=p floor on the whole
    statistic is then  -log2 rho_b  <=  log2 p + n*lambda + o(n), so a budget
    eta survives only while  n <= log2(p) / (eta - lambda)  when lambda < eta.
    """
    print("[M1] the EXACT k=p exponent lambda(beta_min, beta) = "
          "(1/n)(log2 C(n,b) - log2|Kr|), exact integers, n-stability check")
    print(f"{'beta_min':>9} {'b/n':>6} {'n=256':>9} {'n=1024':>9} "
          f"{'n=2048':>9} {'Cauchy bd':>10}")
    lam = {}
    BMS = (0.0, 1 / 64, 1 / 32, 1 / 16, 1 / 8, 3 / 16, 1 / 4, 1 / 3, 7 / 16, 1 / 2)
    FRACS = (0.25, 0.375, 0.5)
    rows = []
    for bm in BMS:
        for frac in FRACS:
            vals = {}
            for n in (256, 1024, 2048):
                b = int(round(frac * n))
                m = int(round(bm * n))
                n_o, n_e = n - m, m
                x = B.kp_ratio_bits(n_o, n_e, b)
                vals[n] = (x / n) if x is not None else None
            lam[(bm, frac)] = vals[2048]
            cb = B.Lambda_p_closed(bm, frac)
            rows.append({"beta_min": bm, "b_over_n": frac,
                         "lambda_256": vals[256], "lambda_1024": vals[1024],
                         "lambda_2048": vals[2048], "cauchy_bound": cb})
            f = lambda v: ("%9.5f" % v) if v is not None else "     dead"
            print(f"{bm:9.5f} {frac:6.3f} {f(vals[256])} {f(vals[1024])} "
                  f"{f(vals[2048])} {cb:10.5f}")
    B.dump("margin_lambda_p.json", {"rows": rows})

    print("\n[M2] PARITY-CLAUSE SHARPNESS: max window size n at which the k=p "
          "floor alone still permits each budget.  n_max = log2 p/(eta-lambda);"
          " 'inf' = the parity floor never binds.")
    print(f"{'log2 p':>8} {'beta_min':>9} {'worst b/n':>10} {'lambda':>8} "
          f"{'n_max(1/3)':>12} {'n_max(1/43)':>13}")
    rows2 = []
    for lg2p in (4.5236, 6.6582, 31.0):
        for bm in BMS:
            # the ADVERSARIAL slice is the one in [n/4,3n/4] with the smallest
            # lambda; among our grid that is always b/n = 1/4 (or 3/4).
            frac = min(FRACS, key=lambda fr: (lam[(bm, fr)]
                                              if lam[(bm, fr)] is not None
                                              else 9e9))
            L = lam[(bm, frac)]
            out = {}
            for tgt, tn in ((1 / 3, "1/3"), (1 / 43, "1/43")):
                out[tn] = (float("inf") if L >= tgt
                           else lg2p / (tgt - L))
            rows2.append({"log2p": lg2p, "beta_min": bm, "b_over_n": frac,
                          "lambda": L, "n_max_third": out["1/3"],
                          "n_max_43": out["1/43"]})
            print(f"{lg2p:8.4f} {bm:9.5f} {frac:10.3f} {L:8.5f} "
                  f"{out['1/3']:12.1f} {out['1/43']:13.1f}")
    B.dump("margin_parity_sharpness.json", {"rows": rows2})

    print("\n[M3] ARC-w killer (synthetic, exact integer V_b): the exponent "
          "as a function of the concentration width w at fixed n")
    rows3 = []
    print(f"{'p':>5} {'w':>3} {'n':>4} {'beta_min':>9} {'#Dvals':>7} "
          f"{'worst b':>7} {'-log2 rho':>10} {'eta_n':>8} {'>1/3':>5} "
          f"{'>1/43':>6} {'1-|R|max':>9}")
    for p in (23, 41, 67, 101):
        for w in (1, 2, 3, 5, 9, 17, 33):
            for n in (48, 64):
                dl = [(i % w) for i in range(n)]
                row, V = B.summarise(p, dl, 0, tag=f"arc{w}", grid=256)
                row["p"], row["w"], row["synthetic"] = p, w, True
                rows3.append(row)
                if row["worst_neglog2"] is None:
                    continue
                print(f"{p:5d} {w:3d} {n:4d} {row['beta_min']:9.4f} "
                      f"{row['distinct_delta']:7d} "
                      f"{row['worst_b']:7d} {row['worst_neglog2']:10.4f} "
                      f"{row['eta_n']:8.5f} "
                      f"{'Y' if row['eta_n']>1/3 else 'n':>5} "
                      f"{'Y' if row['eta_n']>1/43 else 'n':>6} "
                      f"{1-row['flatness_max_absR']:9.5f}")
    B.dump("margin_arc.json", {"rows": rows3})


# ================================================================ weight ====
def stage_weight():
    """TRUE-weight (exact Z[zeta_p]) confirmation that the killers are real."""
    print("[W] TRUE weights 2cos(pi s/p), exact algebra; decimals are 60-digit "
          "renderings of exactly computed cyclotomic integers")
    print(f"{'p':>4} {'c':>7} {'n':>3} {'family':>16} {'b':>3} "
          f"{'true -log2 rho':>15} {'proxy -log2 rho':>16} {'beta_min':>9}")
    rows = []
    for p in (11, 13, 19, 23):
        for c in CS:
            c = (c[0] % p, c[1] % p)
            D, S, loc = B.model(p, c)
            for n in (8, 10, 12):
                fams = _families(p, c, n)
                for name, w in fams.items():
                    if w is None:
                        continue
                    dl, base, sel = w
                    sub = [loc[i] for i in sel]
                    A = slice_coeffs_carrydp(p, sub)
                    E = elem_sym(abs_pairs(p, sub))
                    Vp = B.V_exact(p, dl, base)
                    per = []
                    for b in range(n + 1):
                        av = abs(complex(A[b].tocomplex()))
                        ev = abs(complex(E[b].tocomplex()))
                        per.append({
                            "b": b,
                            "true": (math.log2(ev / av) if av > 0 else None),
                            "proxy": B.neglog2_rho(Vp[b], n, b)})
                    rows.append({"p": p, "c": list(c), "n": n, "family": name,
                                 "beta_min": B.beta_min(dl), "per_b": per})
                    for b in (n // 4, n // 2, 3 * n // 4):
                        e = per[b]
                        if e["true"] is None:
                            continue
                        print(f"{p:4d} {str(c):>7} {n:3d} {name:>16} {b:3d} "
                              f"{e['true']:15.4f} "
                              f"{(e['proxy'] if e['proxy'] is not None else float('nan')):16.4f} "
                              f"{B.beta_min(dl):9.4f}")
    B.dump("true_weight_killers.json", {"rows": rows})


# ================================================================ census ====
def stage_census():
    """Realisability: the Delta multiplicity law, and how large a killer
    window each class admits, as a function of p."""
    rows = []
    print("[C] Delta multiset law over the FULL pair set (exact)")
    print(f"{'p':>5} {'m pairs':>9} {'#values':>8} {'max mult':>9} "
          f"{'mult profile == 1..p-1':>23} {'arc2':>6} {'arc3':>6} "
          f"{'best adj-pair min':>18}")
    for p in (11, 13, 19, 23, 31, 41, 53, 67, 79, 101, 127, 151, 199):
        for c in CS:
            c = (c[0] % p, c[1] % p)
            D, S, loc = B.model(p, c)
            ctr = collections.Counter(D)
            two_p = 2 * p
            prof = sorted(ctr.values())
            law = (prof == list(range(1, p)))
            arc = {}
            for wdt in (2, 3):
                arc[wdt] = max(sum(ctr.get((a + t) % two_p, 0)
                                   for t in range(wdt)) for a in range(two_p))
            adj = max(min(ctr.get(a, 0), ctr.get((a + 1) % two_p, 0))
                      for a in range(two_p))
            rows.append({"p": p, "c": list(c), "m": len(D),
                         "n_values": len(ctr), "max_mult": max(ctr.values()),
                         "mult_law_1_to_pm1": law, "arc2": arc[2],
                         "arc3": arc[3], "best_adjacent_pair_min": adj})
            print(f"{p:5d} {len(D):9d} {len(ctr):8d} {max(ctr.values()):9d} "
                  f"{str(law):>23} {arc[2]:6d} {arc[3]:6d} {adj:18d}")
    B.dump("delta_multiplicity_law.json", {"rows": rows})


if __name__ == "__main__":
    os.makedirs(B.RESULTS, exist_ok=True)
    st = sys.argv[1]
    if st == "ramp":
        stage_ramp(int(sys.argv[2]))
    elif st == "killers":
        stage_killers(int(sys.argv[2]))
    elif st == "climb":
        stage_climb(int(sys.argv[2]), int(sys.argv[3]))
    elif st == "margin":
        stage_margin()
    elif st == "weight":
        stage_weight()
    elif st == "census":
        stage_census()
    elif st == "arcscale":
        stage_arcscale()
    elif st == "arcsynth":
        stage_arcsynth()
    elif st == "flatscan":
        stage_flatscan(int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 48)
    else:
        raise SystemExit(f"unknown stage {st}")
