#!/usr/bin/env python3
"""Stages C1-C4 of the fixed-sector absorption pilot.  Exact where banked.

  c1  positivity + class inheritance census      (P1, P2, P3, P5, P7-lite)
  c2  the K2 pullback identity                   (P4)
  c3  annealed marginality of the parity classes (P6)
  c4  exact b-resolved two-sector composition    (P7, P9)
"""
from __future__ import annotations

import json
import math
import os
import sys

sys.dont_write_bytecode = True
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import numpy as np  # noqa: E402
import core as C  # noqa: E402


def instance(e: int):
    p = C.official_shaped_prime(e)
    F = C.Fp2(p)
    fixed, mreps, freps = C.sectors(F, e)
    return p, F, fixed, mreps, freps


def rand_coeffs(rng, p, ls):
    return {int(l): (int(rng.integers(p)), int(rng.integers(p))) for l in ls}


def sector_report(F, coeffs, n_ord, fixed, mreps, freps):
    """All exact per-sector data for one frequency."""
    p = F.p
    fv = C.chi_values(F, coeffs, fixed, n_ord)
    mv_all = C.chi_values(F, coeffs, [y for y in mreps]
                          + [F.neg(y) for y in mreps], n_ord)
    Ffix = C.census_term(p, fv)
    Fmov = C.census_term(p, mv_all)
    Ftot = C.census_term(p, fv + mv_all)
    okf, vf = C.cyc_is_rational_integer(Ffix)
    okm, vm = C.cyc_is_rational_integer(Fmov)
    okt, vt = C.cyc_is_rational_integer(Ftot)
    # windows (the lane's carry coordinates) for both sectors
    Dm, basem = C.window_of(F, coeffs, mreps, n_ord)
    Df, basef = C.window_of(F, coeffs, freps, n_ord)
    mr_m, k_m = C.maxR_float(p, Dm)
    mr_f, k_f = C.maxR_float(p, Df)
    return {
        "class": C.parity_class(coeffs),
        "fixed_int": okf, "fixed_val": vf if okf else None,
        "moving_int": okm, "moving_val": vm if okm else None,
        "total_int": okt, "total_val": vt if okt else None,
        "fixed_real": C.cyc_is_real(Ffix), "moving_real": C.cyc_is_real(Fmov),
        "total_real": C.cyc_is_real(Ftot),
        "fixed_shadow_trivial": all(s == 0 for s in fv),
        "fixed_all_delta_even": C.all_even(Df),
        "moving_all_delta_even": C.all_even(Dm),
        "fixed_all_delta_zero": all(d == 0 for d in Df),
        "moving_all_delta_zero": all(d == 0 for d in Dm),
        "fixed_flat_float": 1.0 - mr_f, "fixed_argmax_k": k_f,
        "moving_flat_float": 1.0 - mr_m, "moving_argmax_k": k_m,
        "n0": len(fixed), "n_move": 2 * len(mreps),
    }


# --------------------------------------------------------------------- c1 ----


def stage_c1(es=(4, 5, 6, 7), trials=60, seed=101, lin_cap=4000):
    rng = np.random.default_rng(seed)
    out = {"rows": [], "detail_counts": {}}
    for e in es:
        p, F, fixed, mreps, freps = instance(e)
        n_ord = 1 << (e + 1)
        # --- family A: the LINEAR character (l = 1): the banked pilots' model
        allc = [(a, b) for a in range(p) for b in range(p) if (a, b) != (0, 0)]
        exhaustive = len(allc) <= lin_cap
        if not exhaustive:
            idx = rng.choice(len(allc), size=lin_cap, replace=False)
            cs = [allc[i] for i in sorted(idx)]
        else:
            cs = allc
        fam = {"linear": [{1: c} for c in cs]}
        # --- family B: multi-condition, by parity class
        odd_ls = [l for l in range(1, n_ord) if l % 2 == 1]
        even_ls = [l for l in range(2, n_ord) if l % 2 == 0]
        for tag, pool in (("K1_multi", odd_ls), ("K2_multi", even_ls),
                          ("G_multi", list(range(1, n_ord)))):
            lst = []
            for _ in range(trials):
                L = int(rng.integers(1, 5))
                ls = list(rng.choice(pool, size=min(L, len(pool)),
                                     replace=False))
                co = rand_coeffs(rng, p, ls)
                if all(v == (0, 0) for v in co.values()):
                    continue
                if tag == "G_multi" and C.parity_class(co) != "G":
                    # force a mixed support
                    co[int(rng.choice(odd_ls))] = (1, 1)
                    co[int(rng.choice(even_ls))] = (1, 2)
                lst.append(co)
            fam[tag] = lst
        for tag, lst in fam.items():
            agg = []
            for co in lst:
                r = sector_report(F, co, n_ord, fixed, mreps, freps)
                agg.append(r)
            if not agg:
                continue
            byc = {}
            for r in agg:
                byc.setdefault(r["class"], []).append(r)
            for cls, rows in byc.items():
                nn = len(rows)
                row = {
                    "e": e, "p": p, "family": tag, "class": cls, "n": nn,
                    "n0": rows[0]["n0"], "n_move": rows[0]["n_move"],
                    "exhaustive_linear": exhaustive if tag == "linear" else None,
                    "rate_fixed_positive_int":
                        sum(1 for r in rows
                            if r["fixed_int"] and r["fixed_val"] > 0) / nn,
                    "rate_moving_positive_int":
                        sum(1 for r in rows
                            if r["moving_int"] and r["moving_val"] > 0) / nn,
                    "rate_total_positive_int":
                        sum(1 for r in rows
                            if r["total_int"] and r["total_val"] > 0) / nn,
                    "rate_total_negative_int":
                        sum(1 for r in rows
                            if r["total_int"] and r["total_val"] < 0) / nn,
                    "rate_total_nonint":
                        sum(1 for r in rows if not r["total_int"]) / nn,
                    "rate_total_real":
                        sum(1 for r in rows if r["total_real"]) / nn,
                    "rate_fixed_all_delta_even":
                        sum(1 for r in rows if r["fixed_all_delta_even"]) / nn,
                    "rate_moving_all_delta_even":
                        sum(1 for r in rows if r["moving_all_delta_even"]) / nn,
                    "rate_fixed_all_delta_zero":
                        sum(1 for r in rows if r["fixed_all_delta_zero"]) / nn,
                    "rate_moving_all_delta_zero":
                        sum(1 for r in rows if r["moving_all_delta_zero"]) / nn,
                    "rate_fixed_shadow_trivial":
                        sum(1 for r in rows if r["fixed_shadow_trivial"]) / nn,
                    "fixed_flat_max":
                        max(r["fixed_flat_float"] for r in rows),
                    "moving_flat_max":
                        max(r["moving_flat_float"] for r in rows),
                    "fixed_argmax_k_is_p":
                        sum(1 for r in rows if r["fixed_argmax_k"] == p) / nn,
                    "moving_argmax_k_is_p":
                        sum(1 for r in rows if r["moving_argmax_k"] == p) / nn,
                }
                # the trivial-shadow sub-class: is the fixed factor 2^{n0}?
                triv = [r for r in rows if r["fixed_shadow_trivial"]]
                if triv:
                    row["trivial_shadow_count"] = len(triv)
                    row["trivial_shadow_fixed_val_is_2^n0"] = all(
                        r["fixed_val"] == (1 << r["n0"]) for r in triv)
                out["rows"].append(row)
                print(f"e={e} p={p:4d} {tag:10s} class={cls:8s} n={nn:5d} "
                      f"fix+int={row['rate_fixed_positive_int']:.3f} "
                      f"mov+int={row['rate_moving_positive_int']:.3f} "
                      f"tot+int={row['rate_total_positive_int']:.3f} "
                      f"tot-int={row['rate_total_negative_int']:.3f} "
                      f"nonint={row['rate_total_nonint']:.3f} "
                      f"fixEven={row['rate_fixed_all_delta_even']:.3f} "
                      f"movEven={row['rate_moving_all_delta_even']:.3f} "
                      f"fixFlatMax={row['fixed_flat_max']:.4f} "
                      f"trivShadow={row['rate_fixed_shadow_trivial']:.4f}")
    C.dump("C1_positivity_census.json", out)


# --------------------------------------------------------------------- c2 ----


def stage_c2(es=(4, 5, 6), trials=25, seed=202):
    """P4: K2 is the pullback of a lower-rung frequency; exact identities."""
    rng = np.random.default_rng(seed)
    rows = []
    for e in es:
        p, F, fixed, mreps, freps = instance(e)
        n_ord = 1 << (e + 1)
        even_ls = [l for l in range(2, n_ord) if l % 2 == 0]
        ok_pull_move = ok_pull_fixed = ok_zero_delta = 0
        tot = 0
        for _ in range(trials):
            L = int(rng.integers(1, 4))
            ls = list(rng.choice(even_ls, size=min(L, len(even_ls)),
                                 replace=False))
            co = rand_coeffs(rng, p, ls)
            if all(v == (0, 0) for v in co.values()):
                continue
            tot += 1
            # moving sector product
            mv = C.chi_values(F, co, [y for y in mreps]
                              + [F.neg(y) for y in mreps], n_ord)
            Fmov = C.census_term(p, mv)
            # reduced frequency g with f(x) = g(x^2)
            g = {int(l // 2): c for l, c in co.items()}
            # x^2 for x of order 2^{e+1} runs 2:1 over the order-exactly-2^e set
            sq = sorted({F.pow(y, 2) for y in mreps})
            gv = C.chi_values(F, g, sq, 1 << e)
            base = C.census_term(p, gv)
            sq_base = C.canon(_cyc_square(base))
            ok_pull_move += (C.canon(Fmov) == sq_base)
            # fixed sector: x^2 runs 2:1 over mu_{2^{e-1}}
            fv = C.chi_values(F, co, fixed, n_ord)
            Ffix = C.census_term(p, fv)
            half = sorted({F.pow(x, 2) for x in fixed})
            gvf = C.chi_values(F, g, half, 1 << e)
            basef = C.census_term(p, gvf)
            ok_pull_fixed += (C.canon(Ffix) == C.canon(_cyc_square(basef)))
            Dm, _ = C.window_of(F, co, mreps, n_ord)
            ok_zero_delta += all(d == 0 for d in Dm)
        rows.append({"e": e, "p": p, "trials": tot,
                     "moving_is_square_of_reduced": ok_pull_move,
                     "fixed_is_square_of_reduced": ok_pull_fixed,
                     "moving_delta_all_zero": ok_zero_delta})
        print(f"e={e} p={p:4d} K2 trials={tot}: moving=sq {ok_pull_move}, "
              f"fixed=sq {ok_pull_fixed}, Delta==0 {ok_zero_delta}")
    C.dump("C2_k2_pullback.json", {"rows": rows})


def _cyc_square(u):
    p = len(u)
    out = [0] * p
    for i, a in enumerate(u):
        if not a:
            continue
        for j, b in enumerate(u):
            if b:
                out[(i + j) % p] += a * b
    return C.canon(out)


# --------------------------------------------------------------------- c3 ----


def stage_c3b(es=(4, 5, 6), seed=313, gtrials=40000):
    """P6 done properly: exact per-element constants + EXHAUSTIVE class means.

    The parity-pure classes pair up (chi(-x) = -chi(x)), so their annealed mass
    is a product of |1+psi|^2 terms with per-element mean EXACTLY 2; the generic
    class has per-element mean (1/p) sum_s |1+psi(s)| -> 4/pi.  The class mean of
    a PRODUCT is heavy-tailed, so only exhaustive class enumeration is banked.
    """
    rng = np.random.default_rng(seed)
    rows = []
    for e in es:
        p, F, fixed, mreps, freps = instance(e)
        n_ord = 1 << (e + 1)
        allx = fixed + [y for y in mreps] + [F.neg(y) for y in mreps]
        npairs = n_ord // 2
        # exact per-element constants
        A1 = sum(abs(2.0 * math.cos(math.pi * s / p)) for s in range(p)) / p
        A2 = sum(2.0 + 2.0 * math.cos(2.0 * math.pi * s / p)
                 for s in range(p)) / p
        # EXHAUSTIVE linear-character class (every linear frequency is K1)
        ux = np.array([x[0] for x in allx], dtype=np.int64)
        vx = np.array([x[1] for x in allx], dtype=np.int64)
        ab = [(a, b) for a in range(p) for b in range(p) if (a, b) != (0, 0)]
        tot, mx = 0.0, -1e18
        logs = []
        for a, b in ab:
            vals = (2 * (a * ux + F.N * b * vx)) % p
            lg = np.sum(np.log(np.abs(2.0 * np.cos(np.pi * vals / p))))
            logs.append(lg)
        logs = np.array(logs)
        m = logs.max()
        lin_mean_per_pair = math.exp(
            (m + math.log(np.mean(np.exp(logs - m)))) / npairs)
        # sampled generic class (2+ conditions, mixed parity)
        odd_ls = [l for l in range(1, n_ord) if l % 2 == 1]
        even_ls = [l for l in range(2, n_ord) if l % 2 == 0]
        glogs = []
        for _ in range(gtrials):
            co = {int(rng.choice(odd_ls)): (int(rng.integers(p)),
                                            int(rng.integers(p))),
                  int(rng.choice(even_ls)): (int(rng.integers(p)),
                                             int(rng.integers(p)))}
            vs = C.chi_values(F, co, allx, n_ord)
            glogs.append(sum(math.log(abs(2.0 * math.cos(math.pi * v / p)))
                             for v in vs))
        glogs = np.array(glogs)
        gm = glogs.max()
        g_mean_per_pair = math.exp(
            (gm + math.log(np.mean(np.exp(glogs - gm)))) / npairs)
        rows.append({"e": e, "p": p, "n": n_ord, "npairs": npairs,
                     "A1_per_element_float": A1, "A1_squared_float": A1 * A1,
                     "A2_per_pair_exact_float": A2,
                     "linear_class_exhaustive": len(ab),
                     "K1_linear_mean_per_pair_float": lin_mean_per_pair,
                     "G_sampled": gtrials,
                     "G_mean_per_pair_float": g_mean_per_pair,
                     "iid_benchmark_generic_per_pair_float": A1 * A1})
        print(f"e={e} p={p:4d} exact A1={A1:.5f} (4/pi={4/math.pi:.5f}) "
              f"A1^2={A1*A1:.5f}  A2(per pair, parity-pure)={A2:.5f}  | "
              f"EXHAUSTIVE K1-linear class mean per pair = "
              f"{lin_mean_per_pair:.4f}  | sampled G mean per pair = "
              f"{g_mean_per_pair:.4f}")
    C.dump("C3b_annealed_exact.json",
           {"rows": rows, "k1_target": 2.0,
            "generic_target": (4 / math.pi) ** 2})


def stage_c3(es=(4, 5, 6), trials=400, seed=303, lin_cap=20000):
    """P6: annealed mean of exp(S_c) per antipodal pair, by class."""
    rng = np.random.default_rng(seed)
    rows = []
    for e in es:
        p, F, fixed, mreps, freps = instance(e)
        n_ord = 1 << (e + 1)
        allx = fixed + [y for y in mreps] + [F.neg(y) for y in mreps]
        npairs = n_ord // 2

        def mass(co):
            vs = C.chi_values(F, co, allx, n_ord)
            s = 0.0
            for v in vs:
                s += math.log(abs(2.0 * math.cos(math.pi * v / p)))
            return s                                  # = S_c = log exp(S_c)

        def mean_per_pair(cos):
            ms = np.array([mass(co) for co in cos])
            mx = ms.max()
            mean = mx + math.log(np.mean(np.exp(ms - mx)))
            return math.exp(mean / npairs), float(np.exp((ms / npairs)).mean())

        # class K1 via the linear character (every linear frequency is K1)
        allc = [(a, b) for a in range(p) for b in range(p) if (a, b) != (0, 0)]
        if len(allc) > lin_cap:
            idx = rng.choice(len(allc), size=lin_cap, replace=False)
            allc = [allc[i] for i in sorted(idx)]
        k1_lin = [{1: c} for c in allc]
        odd_ls = [l for l in range(1, n_ord) if l % 2 == 1]
        even_ls = [l for l in range(2, n_ord) if l % 2 == 0]
        k1_multi, g_multi, k2_multi = [], [], []
        for _ in range(trials):
            L = int(rng.integers(2, 5))
            k1_multi.append(rand_coeffs(rng, p, rng.choice(
                odd_ls, size=min(L, len(odd_ls)), replace=False)))
            k2_multi.append(rand_coeffs(rng, p, rng.choice(
                even_ls, size=min(L, len(even_ls)), replace=False)))
            co = rand_coeffs(rng, p, rng.choice(
                range(1, n_ord), size=min(2 * L, n_ord - 1), replace=False))
            co[int(rng.choice(odd_ls))] = (1, 1)
            co[int(rng.choice(even_ls))] = (1, 2)
            g_multi.append(co)
        for tag, cos in (("K1_linear", k1_lin), ("K1_multi", k1_multi),
                         ("K2_multi", k2_multi), ("G_multi", g_multi)):
            mpp, _ = mean_per_pair(cos)
            rows.append({"e": e, "p": p, "n": n_ord, "npairs": npairs,
                         "family": tag, "count": len(cos),
                         "mean_expS_per_pair_float": mpp})
            print(f"e={e} p={p:4d} {tag:10s} count={len(cos):6d} "
                  f"mean(exp S)^(1/pairs) = {mpp:.4f}   "
                  f"[K1 target 2.0000, generic target {(4/math.pi)**2:.4f}]")
    C.dump("C3_annealed_mass.json",
           {"rows": rows, "generic_target": (4 / math.pi) ** 2,
            "k1_target": 2.0})


# --------------------------------------------------------------------- c4 ----


def stage_c4(es=(4, 5), seed=404):
    """Exact b-resolved two-sector composition and the bits ledger."""
    rng = np.random.default_rng(seed)
    rows = []
    for e in es:
        p, F, fixed, mreps, freps = instance(e)
        n_ord = 1 << (e + 1)
        n0, nm = len(fixed), 2 * len(mreps)
        odd_ls = [l for l in range(1, n_ord) if l % 2 == 1]
        even_ls = [l for l in range(2, n_ord) if l % 2 == 0]
        cases = {
            "K1_linear_generic": {1: (1, 1)},
            "K1_linear_trivialshadow": {1: (0, 1)},
            "K1_multi": {1: (2, 3), 3: (1, 5), 5: (4, 1)},
            "K2_multi": {2: (1, 1), 4: (2, 3)},
            "G_multi": {1: (1, 1), 2: (2, 3)},
        }
        for _ in range(2):
            ls = [int(x) for x in rng.choice(range(1, n_ord), size=4,
                                             replace=False)]
            co = rand_coeffs(rng, p, ls)
            co[int(rng.choice(odd_ls))] = (1, 1)
            co[int(rng.choice(even_ls))] = (3, 2)
            cases[f"G_rand{sorted(co)}"] = co
        for tag, co in cases.items():
            fv = C.chi_values(F, co, fixed, n_ord)
            mv = C.chi_values(F, co, [y for y in mreps]
                              + [F.neg(y) for y in mreps], n_ord)
            pf = C.census_poly(p, fv)
            pm = C.census_poly(p, mv)
            pt = C.census_poly(p, fv + mv)
            real_f = all(C.cyc_is_real(u) for u in pf)
            real_m = all(C.cyc_is_real(u) for u in pm)
            real_t = all(C.cyc_is_real(u) for u in pt)
            int_t = all(C.cyc_is_rational_integer(u)[0] for u in pt)

            def bits(poly, size):
                out = []
                for b in range(size + 1):
                    la = C.cyc_log2abs(poly[b])
                    out.append(math.log2(math.comb(size, b)) - la
                               if la != float("-inf") else float("inf"))
                return out

            bf, bm, bt = bits(pf, n0), bits(pm, nm), bits(pt, n_ord)

            def central_worst(bl, size):
                lo, hi = math.ceil(0.25 * size), math.floor(0.75 * size)
                vals = [v for v in bl[lo:hi + 1] if v != float("inf")]
                return min(vals) if vals else None

            def central_best(bl, size):
                lo, hi = math.ceil(0.25 * size), math.floor(0.75 * size)
                vals = [v for v in bl[lo:hi + 1] if v != float("inf")]
                return max(vals) if vals else None

            # the lane's carry currency for the two windows
            Dm, basem = C.window_of(F, co, mreps, n_ord)
            Df, basef = C.window_of(F, co, freps, n_ord)
            Vm = C.DP_V(p, Dm, basem)
            Vf = C.DP_V(p, Df, basef)

            def carry_bits(V, m):
                lo, hi = math.ceil(0.25 * m), math.floor(0.75 * m)
                vals = []
                for b in range(lo, hi + 1):
                    if V[b] == 0:
                        continue
                    vals.append(math.log2(math.comb(m, b))
                                - math.log2(abs(V[b])))
                return (min(vals) if vals else None,
                        max(vals) if vals else None)

            cm_lo, cm_hi = carry_bits(Vm, len(Dm))
            cf_lo, cf_hi = carry_bits(Vf, len(Df))
            row = {
                "e": e, "p": p, "case": tag, "class": C.parity_class(co),
                "n0": n0, "n_move": nm, "n": n_ord,
                "log2_p": math.log2(p),
                "fixed_all_real": real_f, "moving_all_real": real_m,
                "total_all_real": real_t, "total_all_rational_int": int_t,
                "fixed_shadow_trivial": all(s == 0 for s in fv),
                "bits_fixed_worst_central": central_worst(bf, n0),
                "bits_fixed_best_central": central_best(bf, n0),
                "bits_moving_worst_central": central_worst(bm, nm),
                "bits_moving_best_central": central_best(bm, nm),
                "bits_total_worst_central": central_worst(bt, n_ord),
                "bits_total_best_central": central_best(bt, n_ord),
                "carry_bits_moving_worst": cm_lo, "carry_bits_moving_best": cm_hi,
                "carry_bits_fixed_worst": cf_lo, "carry_bits_fixed_best": cf_hi,
            }
            for k in ("bits_fixed_worst_central", "bits_moving_worst_central",
                      "bits_total_worst_central"):
                sz = {"bits_fixed_worst_central": n0,
                      "bits_moving_worst_central": nm,
                      "bits_total_worst_central": n_ord}[k]
                row[k + "_per_element"] = (row[k] / sz) if row[k] else None
            rows.append(row)
            print(f"e={e} p={p:4d} {tag:28s} cls={row['class']:3s} "
                  f"bits fix/mov/tot (worst central) = "
                  f"{_f(row['bits_fixed_worst_central'])}/"
                  f"{_f(row['bits_moving_worst_central'])}/"
                  f"{_f(row['bits_total_worst_central'])}   "
                  f"carry mov={_f(cm_lo)} fix={_f(cf_lo)}  "
                  f"log2p={math.log2(p):.2f}  realF/M/T="
                  f"{int(real_f)}{int(real_m)}{int(real_t)}")
    C.dump("C4_bresolved_composition.json", {"rows": rows})


def _f(x):
    return "None" if x is None else f"{x:.3f}"


# -------------------------------------------------------------------- c1p ----


def stage_c1p(es=(4, 5, 6, 7), trials=40, seed=505, lin_cap=300):
    """P1/P2 restated correctly: the parity-pure sector factors are TOTALLY
    POSITIVE real cyclotomic integers (exact antipodal normal form), while the
    G class carries genuine sign."""
    rng = np.random.default_rng(seed)
    rows = []
    for e in es:
        p, F, fixed, mreps, freps = instance(e)
        n_ord = 1 << (e + 1)
        odd_ls = [l for l in range(1, n_ord) if l % 2 == 1]
        even_ls = [l for l in range(2, n_ord) if l % 2 == 0]
        allc = [(a, b) for a in range(p) for b in range(p) if (a, b) != (0, 0)]
        if len(allc) > lin_cap:
            idx = rng.choice(len(allc), size=lin_cap, replace=False)
            allc = [allc[i] for i in sorted(idx)]
        fam = {"K1_linear": [{1: c} for c in allc], "K1_multi": [], "K2_multi": [],
               "G_multi": []}
        for _ in range(trials):
            L = int(rng.integers(1, 4))
            fam["K1_multi"].append(rand_coeffs(rng, p, rng.choice(
                odd_ls, size=min(L, len(odd_ls)), replace=False)))
            fam["K2_multi"].append(rand_coeffs(rng, p, rng.choice(
                even_ls, size=min(L, len(even_ls)), replace=False)))
            co = rand_coeffs(rng, p, rng.choice(range(1, n_ord),
                                                size=2, replace=False))
            co[int(rng.choice(odd_ls))] = (1, 1)
            co[int(rng.choice(even_ls))] = (1, 2)
            fam["G_multi"].append(co)
        for tag, cos in fam.items():
            nn = 0
            id_fix = id_mov = pos_tot = neg_tot = tot_real = totpos = 0
            for co in cos:
                if C.parity_class(co) == "vacuous":
                    continue
                nn += 1
                fv = C.chi_values(F, co, fixed, n_ord)
                mv = C.chi_values(F, co, [y for y in mreps]
                                  + [F.neg(y) for y in mreps], n_ord)
                Ffix = C.census_term(p, fv)
                Fmov = C.census_term(p, mv)
                Ftot = C.census_term(p, fv + mv)
                tot_real += C.cyc_is_real(Ftot)
                # exact antipodal normal form (only meaningful for parity-pure)
                fp = C.chi_values(F, co, freps, n_ord)
                mp_ = C.chi_values(F, co, mreps, n_ord)
                id_fix += (C.canon(Ffix) == C.pair_product(p, fp))
                id_mov += (C.canon(Fmov) == C.pair_product(p, mp_))
                v = float(C.cyc_embed(Ftot, 1).real)
                pos_tot += (v > 0)
                neg_tot += (v < 0)
                # total positivity is CERTIFIED EXACTLY by the antipodal normal
                # form (every factor 2 + zeta^s + zeta^{-s} has all conjugates
                # 2 + 2cos(2 pi k s/p) > 0, p odd); the numerical all-conjugate
                # check is run only at the smallest prime as a cross-check.
                if p <= 97:
                    totpos += (C.cyc_min_conjugate(Ftot, dps=30) > 0)
            rows.append({"e": e, "p": p, "family": tag, "n": nn,
                         "rate_fixed_antipodal_normal_form": id_fix / nn,
                         "rate_moving_antipodal_normal_form": id_mov / nn,
                         "rate_total_real_exact": tot_real / nn,
                         "rate_total_positive": pos_tot / nn,
                         "rate_total_negative": neg_tot / nn,
                         "rate_total_totally_positive": totpos / nn})
            print(f"e={e} p={p:4d} {tag:10s} n={nn:4d}  "
                  f"fixNF={id_fix/nn:.3f} movNF={id_mov/nn:.3f} "
                  f"real={tot_real/nn:.3f} pos={pos_tot/nn:.3f} "
                  f"neg={neg_tot/nn:.3f} totpos={totpos/nn:.3f}")
    C.dump("C1p_sign_field.json", {"rows": rows})


def main():
    st = sys.argv[1] if len(sys.argv) > 1 else "c1"
    {"c1": stage_c1, "c1p": stage_c1p, "c2": stage_c2, "c3": stage_c3,
     "c3b": stage_c3b, "c4": stage_c4}[st]()


if __name__ == "__main__":
    main()
