#!/usr/bin/env python3
"""Deployed-window experiments.

Stages
  classes  -- E1: the three frequency-support classes (odd-only / even-only /
              mixed) at official-shaped rung-1 instances.
  bandlim  -- E2: the official band-limited reading, f supported on l <= t_eff.
  slice    -- E3: exact-integer V_b and -log2 rho_b for each class.
  budget   -- E4: what each budget needs vs what each class delivers, per rung.
  scaling  -- E5: generic flatness vs p and vs rung index (window size).
"""
from __future__ import annotations

import collections
import json
import math
import os
import sys

sys.dont_write_bytecode = True
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import numpy as np  # noqa: E402
import deployed as DP  # noqa: E402
import tower as TW  # noqa: E402
import census as CS  # noqa: E402
import moment as MO  # noqa: E402
from slicecore import Fp2, pair_reps  # noqa: E402
from verify import DP_V  # noqa: E402


def instance(e: int):
    p = TW.official_shaped_prime(e)
    n1 = 1 << (e + 1)
    F, reps = MO.sector_reps(p, n1)
    return p, n1, F, reps


def rand_coeffs(rng, F, n_ord, ls):
    return {int(l): (int(rng.integers(F.p)), int(rng.integers(F.p)))
            for l in ls}


def stage_classes(es=(4, 5, 6, 7), trials=40, seed=7):
    rng = np.random.default_rng(seed)
    rows = []
    for e in es:
        p, n1, F, reps = instance(e)
        m = len(reps)
        odd_ls = [l for l in range(1, n1) if l % 2 == 1]
        even_ls = [l for l in range(2, n1) if l % 2 == 0]
        for cls, pool in (("odd_only", odd_ls), ("even_only", even_ls),
                          ("mixed", list(range(1, n1)))):
            agg = []
            for _ in range(trials):
                L = int(rng.integers(1, 6))
                ls = list(rng.choice(pool, size=min(L, len(pool)),
                                     replace=False))
                co = rand_coeffs(rng, F, n1, ls)
                if all(v == (0, 0) for v in co.values()):
                    continue
                D = MO.deltas_moment(F, reps, n1, co)
                st = MO.window_stats(p, D)
                st["class"] = cls
                st["support"] = sorted(int(x) for x in ls)
                agg.append(st)
            fl = [a["flat_float"] for a in agg]
            rows.append({
                "p": p, "e": e, "n_ord": n1, "m": m, "class": cls,
                "trials": len(agg),
                "flat_min": min(fl), "flat_med": float(np.median(fl)),
                "flat_max": max(fl),
                "frac_all_even": float(np.mean([a["all_delta_even"] for a in agg])),
                "frac_all_zero": float(np.mean([a["all_delta_zero"] for a in agg])),
                "beta_min_med": float(np.median([a["beta_min"] for a in agg])),
                "argmax_k_modes": collections.Counter(
                    ("k=p" if a["argmax_k"] == p else "k!=p")
                    for a in agg).most_common(),
            })
            print(f"p={p:5d} e={e} m={m:4d} class={cls:10s} "
                  f"flat min/med/max = {min(fl):.4f}/{np.median(fl):.4f}/"
                  f"{max(fl):.4f}  all_even={rows[-1]['frac_all_even']:.2f} "
                  f"all_zero={rows[-1]['frac_all_zero']:.2f}")
    DP.dump("E1_frequency_classes.json", {"rows": rows})


def stage_bandlim(es=(5, 6, 7), seed=11, trials=30):
    """The official reading: f = sum_{l=1..t_eff} c_l x^l, random coefficients."""
    rng = np.random.default_rng(seed)
    rows = []
    for e in es:
        p, n1, F, reps = instance(e)
        m = len(reps)
        for tfrac in (0.02, 0.05, 0.25, 1.0, 2.0):
            t_eff = max(1, int(tfrac * n1))
            fl, ae, az = [], 0, 0
            for _ in range(trials):
                ls = list(range(1, min(t_eff, n1) + 1))
                if len(ls) > 24:
                    ls = list(rng.choice(ls, size=24, replace=False))
                co = rand_coeffs(rng, F, n1, ls)
                D = MO.deltas_moment(F, reps, n1, co)
                st = MO.window_stats(p, D)
                fl.append(st["flat_float"])
                ae += st["all_delta_even"]
                az += st["all_delta_zero"]
            rows.append({"p": p, "e": e, "m": m, "t_eff": t_eff,
                         "t_over_n": tfrac, "trials": trials,
                         "flat_min": min(fl), "flat_med": float(np.median(fl)),
                         "flat_max": max(fl), "n_all_even": ae,
                         "n_all_zero": az})
            print(f"p={p:5d} m={m:4d} t_eff={t_eff:5d} (t/n={tfrac:g}) "
                  f"flat min/med/max = {min(fl):.4f}/{np.median(fl):.4f}/"
                  f"{max(fl):.4f}")
    DP.dump("E2_bandlimited.json", {"rows": rows})


def stage_slice(es=(4, 5, 6), seed=3):
    """EXACT integer V_b for one representative of each frequency class."""
    rng = np.random.default_rng(seed)
    rows = []
    for e in es:
        p, n1, F, reps = instance(e)
        m = len(reps)
        if m > 40:
            continue
        cases = {}
        cases["odd_only(l=1)"] = {1: (1, 1)}
        cases["odd_only(l=1,3)"] = {1: (1, 1), 3: (2, 3)}
        cases["even_only(l=2)"] = {2: (1, 1)}
        cases["mixed(l=1,2)"] = {1: (1, 1), 2: (2, 3)}
        for _ in range(3):
            ls = [int(x) for x in rng.choice(range(1, n1), size=4,
                                             replace=False)]
            cases[f"mixed_rand{sorted(ls)}"] = rand_coeffs(rng, F, n1, ls)
        for tag, co in cases.items():
            D = MO.deltas_moment(F, reps, n1, co)
            st = MO.window_stats(p, D)
            # base = sum_i sigma_i^-  (recomputed from the same evaluation)
            base = _base_of(F, reps, n1, co)
            V = DP_V(p, D, base)
            best, bb = None, None
            for b in range(1, m):
                if V[b] == 0:
                    continue
                x = math.log2(math.comb(m, b)) - math.log2(abs(V[b]))
                if best is None or x > best:
                    best, bb = x, b
            worst, wb = None, None
            lo, hi = math.ceil(0.25 * m), math.floor(0.75 * m)
            for b in range(lo, hi + 1):
                if V[b] == 0:
                    continue
                x = math.log2(math.comb(m, b)) - math.log2(abs(V[b]))
                if worst is None or x < worst:
                    worst, wb = x, b
            rows.append({"p": p, "e": e, "m": m, "case": tag,
                         "flat_float": st["flat_float"],
                         "beta_min": st["beta_min"],
                         "all_delta_even": st["all_delta_even"],
                         "all_delta_zero": st["all_delta_zero"],
                         "max_neglog2_rho": best, "argmax_b": bb,
                         "worst_band_neglog2_rho": worst, "worst_b": wb,
                         "log2_p": math.log2(p),
                         "eta_worst": (worst / m) if worst else 0.0})
            print(f"p={p:5d} m={m:3d} {tag:22s} flat={st['flat_float']:.4f} "
                  f"bmin={st['beta_min']:.3f} max(-log2 rho)={best if best is None else round(best,4)} "
                  f"worst-band={worst if worst is None else round(worst,4)} "
                  f"(log2 p={math.log2(p):.3f})  eta={rows[-1]['eta_worst']:.5f}")
    DP.dump("E3_slice_exact.json", {"rows": rows})


def _base_of(F, reps, n_ord, coeffs):
    p = F.p
    two_p = 2 * p
    tot = 0
    for y in reps:
        accM = (0, 0)
        for l, cl in coeffs.items():
            term = F.mul(cl, F.pow(y, l % n_ord))
            if l % 2 == 0:
                accM = ((accM[0] + term[0]) % p, (accM[1] + term[1]) % p)
            else:
                accM = ((accM[0] - term[0]) % p, (accM[1] - term[1]) % p)
        sm = F.trace(accM)
        tot += (sm + p * (1 if 2 * sm > p else 0)) % two_p
    return tot % two_p


def stage_budget():
    """Per-rung budget arithmetic at the official shape.  Exact where integral."""
    p_bits = 31
    p = TW.KOALABEAR
    rows = []
    for j in TW.OFFICIAL_RUNGS:
        rp = TW.rung_params(24, j)
        m = rp["m_pairs"]
        n_j = rp["n_ord"]
        # startup deficit: log2 M_p + log2 kappa(m, m/4)
        b = m // 4
        deficit = DP.startup_deficit(p, m, b)
        need_43 = m / 43.0
        need_3 = m / 3.0
        # (H-flat) thresholds at beta = 1/4 and 1/2
        rows.append({
            "rung": j, "n_ord": n_j, "m_pairs": m,
            "log2_m": math.log2(m),
            "startup_deficit_bits": deficit,
            "budget_1_43_bits": need_43,
            "budget_1_3_bits": need_3,
            "deployed_ceiling_bits_K1": p_bits,      # slice floor 1/p
            "deployed_ceiling_bits_K2": 0.0,         # rho_b = 1 exactly
            "shortfall_43_bits_K1": need_43 - p_bits,
            "shortfall_43_log2": math.log2(max(need_43 - p_bits, 1e-9)),
            "flat_needed_43_beta_quarter": (1 / 43) * math.log(2) / 0.1875,
            "flat_needed_3_beta_quarter": (1 / 3) * math.log(2) / 0.1875,
            "flat_needed_43_beta_half": (1 / 43) * math.log(2) / 0.25,
            "flat_needed_3_beta_half": (1 / 3) * math.log(2) / 0.25,
        })
    DP.dump("E4_budget_per_rung.json", {"rows": rows,
                                        "p": p, "log2_p": math.log2(p)})
    print(f"{'rung':>4} {'n_j':>12} {'m_j':>12} {'need 1/43':>14} "
          f"{'need 1/3':>14} {'startup':>8} {'K1 ceiling':>10}")
    for r in rows:
        print(f"{r['rung']:>4} 2^{math.log2(r['n_ord']):.0f}"
              f"{'':>8} 2^{math.log2(r['m_pairs']):.0f}{'':>8} "
              f"{r['budget_1_43_bits']:>14.3e} {r['budget_1_3_bits']:>14.3e} "
              f"{r['startup_deficit_bits']:>8.2f} {r['deployed_ceiling_bits_K1']:>10}")


def stage_scaling(es=(4, 5, 6, 7, 8, 9, 10, 11), trials=12, seed=5):
    """Generic (mixed-frequency) deployed flatness vs p and vs window size."""
    rng = np.random.default_rng(seed)
    rows = []
    for e in es:
        p, n1, F, reps = instance(e)
        m = len(reps)
        fl = []
        resid = []
        for _ in range(trials):
            ls = [int(x) for x in rng.choice(range(1, n1),
                                             size=min(6, n1 - 1), replace=False)]
            co = rand_coeffs(rng, F, n1, ls)
            D = MO.deltas_moment(F, reps, n1, co)
            cnt = MO.counts_of(p, D)
            mr, kk = CS.maxR(p, cnt, m)
            fl.append(1.0 - mr)
            mr2, _ = CS.maxR_excluding_p(p, cnt, m)
            resid.append(1.0 - mr2)
        # the pure-odd (pilots' j=1) deployed window, for contrast
        Dk1 = MO.deltas_moment(F, reps, n1, {1: (1, 1)})
        cntk1 = MO.counts_of(p, Dk1)
        k1_all, _ = CS.maxR(p, cntk1, m)
        k1_res, _ = CS.maxR_excluding_p(p, cntk1, m)
        rows.append({"p": p, "e": e, "m": m,
                     "generic_flat_min": min(fl),
                     "generic_flat_med": float(np.median(fl)),
                     "generic_resid_flat_med": float(np.median(resid)),
                     "K1_flat": 1.0 - k1_all,
                     "K1_resid_flat": 1.0 - k1_res,
                     "sqrt_p_over_m": math.sqrt(p) / m})
        print(f"e={e:2d} p={p:9d} m={m:6d} generic flat med={np.median(fl):.4f} "
              f"(min {min(fl):.4f})   K1 flat={rows[-1]['K1_flat']:.2e} "
              f"K1 residual flat={rows[-1]['K1_resid_flat']:.6f} "
              f"sqrt(p)/m={rows[-1]['sqrt_p_over_m']:.6f}")
    DP.dump("E5_scaling.json", {"rows": rows})




# ---------------------------------------------------------------- classes2 ---

def _zset(F, reps):
    """z_i in F_p^* with y_i = w z_i (deployed rung-1 elements are trace-zero)."""
    return [y[1] for y in reps]


def stage_classes2(es=(6, 7, 8, 9, 10), trials=60, seed=21):
    """The (A, B) normal form of the deployed rung-1 window.

    y = w z with z in a half-system S of a coset of the 2-Sylow H_2 <= F_p^*.
    For l EVEN, y^l lies in F_p; for l ODD, y^l lies in w F_p.  Hence

        s^+ = A(z) + B(z),   s^- = A(z) - B(z),
        A(z) = Tr(f_even(y))  (an EVEN polynomial in z),
        B(z) = Tr(f_odd(y))   (an ODD polynomial in z).

    A == 0  <=>  the pilots' j = 1 class (all Delta even, k = p dead).
    B == 0  <=>  coset-trivial (all Delta = 0, rho_b = 1 at every b).
    """
    rng = np.random.default_rng(seed)
    rows = []
    for e in es:
        p, n1, F, reps = instance(e)
        m = len(reps)
        z = np.array(_zset(F, reps), dtype=np.int64)
        for deg in (1, 2, 4, 8, 32):
            fl, fl_res, bmin, ndead = [], [], [], 0
            for _ in range(trials):
                # A: even poly of degree <= 2*deg ; B: odd poly, same budget
                A = np.zeros_like(z)
                B = np.zeros_like(z)
                for d in range(1, deg + 1):
                    A = (A + int(rng.integers(p)) * pow_mod(z, 2 * d, p)) % p
                    B = (B + int(rng.integers(p)) * pow_mod(z, 2 * d - 1, p)) % p
                A = (A + int(rng.integers(p))) % p          # constant term (even)
                sp = (A + B) % p
                sm = (A - B) % p
                sig_p = sp + p * (2 * sp > p)
                sig_m = sm + p * (2 * sm > p)
                Dl = (sig_p - sig_m) % (2 * p)
                cnt = np.bincount(Dl, minlength=2 * p)
                mr, kk = CS.maxR(p, cnt, m)
                mr2, _ = CS.maxR_excluding_p(p, cnt, m)
                fl.append(1.0 - mr)
                fl_res.append(1.0 - mr2)
                odd = int(cnt[1::2].sum())
                bmin.append(min(odd, m - odd) / m)
                ndead += (1.0 - mr) < 1e-9
            rows.append({"p": p, "e": e, "m": m, "deg": deg, "trials": trials,
                         "flat_min": min(fl), "flat_med": float(np.median(fl)),
                         "flat_max": max(fl),
                         "resid_flat_med": float(np.median(fl_res)),
                         "beta_min_med": float(np.median(bmin)),
                         "n_dead": int(ndead),
                         "frac_clear_43": float(np.mean([x >= 0.086 for x in fl])),
                         "sqrt_p_over_m": math.sqrt(p) / m})
            print(f"p={p:8d} e={e:2d} m={m:5d} deg={deg:3d}  flat min/med/max = "
                  f"{min(fl):.4f}/{np.median(fl):.4f}/{max(fl):.4f}  "
                  f"bmin_med={np.median(bmin):.4f} dead={ndead}/{trials} "
                  f"clear(1/43)={rows[-1]['frac_clear_43']:.2f}")
    DP.dump("E6_AB_normal_form.json", {"rows": rows})


def pow_mod(z, d, p):
    out = np.ones_like(z)
    base = z % p
    while d:
        if d & 1:
            out = (out * base) % p
        base = (base * base) % p
        d >>= 1
    return out


def stage_residual(es=(10, 11, 12, 13, 14), seed=31, trials=6):
    """A7b: residual flatness (k != p) at large m -- the Gauss-sum regime."""
    rng = np.random.default_rng(seed)
    rows = []
    for e in es:
        r = 8
        p = TW.official_shaped_prime(e, start_odd=(1 << r) | 1)
        n1 = 1 << (e + 1)
        if (p * p - 1) % n1:
            continue
        ra = CS.reps_arrays(p, n1)
        if ra is None:
            continue
        F, ay, by = ra
        m = len(ay)
        worst = 0.0
        for _ in range(trials):
            c = (int(rng.integers(p)), int(rng.integers(1, p)))
            cnt = CS.delta_counts(p, F, ay, by, c)
            mr2, _ = CS.maxR_excluding_p(p, cnt, m)
            worst = max(worst, mr2)
        rows.append({"p": p, "e": e, "m": m,
                     "log2_m_over_sqrt_p": math.log2(m / math.sqrt(p)),
                     "max_absR_k_ne_p": worst, "residual_flat": 1.0 - worst,
                     "sqrt_p_over_m": math.sqrt(p) / m,
                     "sqrt_p_lnp_over_m": math.sqrt(p) * math.log(p) / m})
        print(f"e={e:2d} p={p:10d} m={m:6d} m/sqrt(p)=2^{rows[-1]['log2_m_over_sqrt_p']:+.2f}"
              f"  max_{{k!=p}}|R_k|={worst:.6f}  residual flat={1-worst:.6f}"
              f"  sqrt(p)/m={math.sqrt(p)/m:.6f}"
              f"  sqrt(p)lnp/m={math.sqrt(p)*math.log(p)/m:.6f}")
    DP.dump("A7b_residual_large_m.json", {"rows": rows})


def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "classes"
    tab = {"classes": stage_classes, "bandlim": stage_bandlim,
           "slice": stage_slice, "budget": stage_budget,
           "scaling": stage_scaling, "classes2": stage_classes2,
           "residual": stage_residual}
    tab[stage]()


if __name__ == "__main__":
    main()
