#!/usr/bin/env python3
"""D3 -- THE PRE-SATURATION ANALYTIC ATTEMPT, and the official-row estimate.

1. THE EXCESS FIT on the exact level censuses banked by escalate.py phase C:
   Zlev(q) = Zinf + kappa * 2^n * q^-alpha .  Registered prediction alpha = T.
2. THE OFFICIAL ANCHOR: rebuild official_scale.json:78-83 from the toy law.
3. THE OFFICIAL-ROW JUNCTION SUM under the fitted law, over log2 q in
   [41, 256]: the first estimate of the C2''-r3 sum.  Labelled [law].
4. The saturated closed form R3inf across tower shapes (the GB-5 shape).
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from c2lib import (Zinf, Binf, LamStar, R3inf_full, R3inf_window, blocks,   # noqa: E402
                   log2_int, c_k, S_m, sigma, log2_sigma)

N_OFF, T_OFF, E_OFF, RESERVE = 2 ** 41, 2 ** 33, 128, 21


def fit(xs, ys):
    k = len(xs)
    sx, sy = sum(xs), sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    sl = (k * sxy - sx * sy) / (k * sxx - sx * sx)
    ic = (sy - sl * sx) / k
    res = max(abs(y - (ic + sl * x)) for x, y in zip(xs, ys))
    return sl, ic, res


def main():
    st = json.load(open(os.path.join(HERE, "ckpt.json")))

    print("=" * 78)
    print("D3.1 -- THE EXCESS FIT on EXACT censuses   (registered PR-D: alpha = T)")
    print("=" * 78)
    print(f"{'n':>5} {'t':>4} {'lev':>3} {'T':>3} {'e':>3} {'pts':>4} "
          f"{'alpha':>9} {'alpha/T':>8} {'aLO/T':>8} {'kap_bits':>9} {'resid':>7} "
          f"{'freeze':>7} {'LamStar':>8}")
    rows = []
    for key, cur in sorted(st.get("C", {}).items()):
        n, t, lev = (int(v) for v in key.split("|"))
        T = t // 2 ** lev
        zi = Zinf(n, t, lev)
        lzi = log2_int(zi)
        xs, ys, frz = [], [], []
        for qs, zs in sorted(cur.items(), key=lambda kv: int(kv[0])):
            q, z = int(qs), int(zs)
            d = z - zi
            if d > 0 and log2_int(z) - lzi >= 1.0:
                xs.append(math.log2(q))
                ys.append(log2_int(d))
            elif d == 0:
                frz.append(math.log2(q))
        if len(xs) < 2:
            print(f"{n:>5} {t:>4} {lev:>3} {T:>3} {n // (2 * t):>3} "
                  f"{len(xs):>4}   -- too few points in the fit window --")
            continue
        sl, ic, res = fit(xs, ys)
        alpha = -sl
        # SECOND ESTIMATOR (declared post hoc, after seeing the transition
        # tail): the local slope over the THREE DEEPEST pre-saturation
        # points, which is the least contaminated by the freeze cutoff.
        alo = float("nan")
        if len(xs) >= 3:
            alo = -fit(xs[:3], ys[:3])[0]
        elif len(xs) == 2:
            alo = -(ys[1] - ys[0]) / (xs[1] - xs[0])
        rows.append({"n": n, "t": t, "lev": lev, "T": T, "alpha": alpha,
                     "rel": alpha / T, "alo": alo, "alo_rel": alo / T,
                     "kap": ic - n, "resid": res,
                     "freeze": min(frz) if frz else float("nan"),
                     "npts": len(xs)})
        print(f"{n:>5} {t:>4} {lev:>3} {T:>3} {n // (2 * t):>3} {len(xs):>4} "
              f"{alpha:>9.4f} {alpha / T:>8.4f} {alo / T:>8.4f} "
              f"{ic - n:>9.3f} {res:>7.3f} "
              f"{(min(frz) if frz else float('nan')):>7.2f} "
              f"{LamStar(n, t, lev):>8.3f}")
    if rows:
        hot = [r for r in rows if r["rel"] >= 1.10]
        law = all(abs(r["rel"] - 1) < 0.10 and abs(r["kap"]) < 2.0
                  and r["resid"] < 0.25 for r in rows)
        fires = len(hot) >= 3 and len({r["T"] for r in hot}) >= 2
        print(f"\n  cells fitted: {len(rows)}   distinct T: "
              f"{sorted({r['T'] for r in rows})}")
        print(f"  mean alpha/T = {sum(r['rel'] for r in rows) / len(rows):.4f}"
              f"   max |alpha/T - 1| = "
              f"{max(abs(r['rel'] - 1) for r in rows):.4f}"
              f"   max resid = {max(r['resid'] for r in rows):.3f} bits")
        lo_ok = [r for r in rows if r["alo_rel"] == r["alo_rel"]]
        if lo_ok:
            print(f"  DEEP-BAND estimator alpha_LO/T: mean "
                  f"{sum(r['alo_rel'] for r in lo_ok) / len(lo_ok):.4f}, "
                  f"range [{min(r['alo_rel'] for r in lo_ok):.4f}, "
                  f"{max(r['alo_rel'] for r in lo_ok):.4f}]")
        hot_lo = [r for r in lo_ok if r["alo_rel"] >= 1.10]
        print(f"  cells with alpha/T >= 1.10 : {len(hot_lo)} (deep-band), "
              f"{len(hot)} (full-window); distinct T among them: "
              f"{sorted({r['T'] for r in hot})}")
        print(f"  G-c VERDICT: "
              f"{'FIRES' if fires else ('LAW HOLDS' if law else 'ANOMALY')}")

    print("\n" + "=" * 78)
    print("D3.2 -- THE OFFICIAL ANCHOR: rebuild official_scale.json:78-83")
    print("=" * 78)
    e = N_OFF // (2 * T_OFF)
    print(f"  support_to_constraint_ratio  n/t          = {N_OFF // T_OFF}"
          f"   [json: 256]  {N_OFF // T_OFF == 256}")
    print(f"  coset_stratum_cells          e = n/(2t)   = {e}"
          f"   [json: 128]  {e == 128}")
    print(f"  coset_stratum_size           Zinf(lev=0)  = 2^{e}"
          f"   [json: 2^128]  {e == 128}")
    print(f"  coset_stratum_probability    2^(e-n)      = 2^-{N_OFF - e}"
          f"   [json: 2^-2199023255424]  {N_OFF - e == 2199023255424}")
    print(f"  coset_term_log2_formula      e - n + t*Lam"
          f"  =  2^33*(log2 q - 256) + 128  "
          f"{E_OFF - N_OFF + T_OFF * 256 == 128}")
    lam_break = (RESERVE + N_OFF - e) / T_OFF
    print(f"  exceeds_2^21_iff  256 - log2 q < (e-21)/t = "
          f"{(e - RESERVE) / T_OFF:.6e}   [json says 107/2^33]  "
          f"{e - RESERVE == 107}")
    print(f"    -> CATCH: 107/2^33 = {107 / 2 ** 33:.6e}, but the json prints "
          f"'= 1.24556e-05', which is 10^3 too large.")
    print(f"  reserve-break scale log2 q  = {lam_break:.12f}")

    print("\n" + "=" * 78)
    print("D3.3 -- THE OFFICIAL-ROW JUNCTION SUM under the law  [law]")
    print("=" * 78)
    m = 33

    def lzinf(lev):
        """log2 Zinf at the official schedule, level lev  [law, C-1]."""
        return E_OFF * log2_sigma(2 ** lev, 2 * (T_OFF // 2 ** lev))

    def lamstar(lev):
        return (N_OFF - lzinf(lev)) / (T_OFF // 2 ** lev)

    R3inf_off = E_OFF * (1.0 - (2 ** 34 - c_k(34))) + N_OFF * S_m(m)
    print(f"  saturated ceiling R3inf(official) = {R3inf_off:.6e} bits "
          f"(vs the 21-bit reserve: factor {R3inf_off / 21:.3e})")
    print(f"  S_33 = {S_m(33):.10f}   S_200 = {S_m(200):.10f}   "
          f"1/ln2 = {1 / math.log(2):.10f}")
    print(f"\n  per-level crossovers LamStar(lev) [law]:")
    print("   " + "  ".join(f"{lev}:{lamstar(lev):.2f}"
                            for lev in [0, 1, 2, 3, 5, 10, 20, 33]))
    print(f"\n  {'log2 q':>14} {'lev-0 coset term':>18} "
          f"{'R3_full [law]':>16} {'<= 21?':>8}")
    LS = [lamstar(lev) for lev in range(m + 1)]
    LB = [N_OFF - (N_OFF / 2 ** (j + 1)) * c_k(j + 1) for j in range(m)]

    def lg1p(r):
        return math.log2(1 + 2.0 ** r) if -60 < r < 40 else (r if r >= 40 else 0.0)

    for lam in [41, 64, 128, 192, 224, 248, 254, 255, 255.9,
                256 - (E_OFF - RESERVE) / T_OFF, 256]:
        # R3_full = R3inf + log2(1+rho_0) - log2(1+rho_m) - sum_j log2(1+beta_j)
        tot = R3inf_off
        tot += lg1p((T_OFF) * (LS[0] - lam))
        tot -= lg1p((T_OFF // 2 ** m) * (LS[m] - lam))
        for j in range(m):
            Lj = T_OFF // 2 ** (j + 1)
            tot -= lg1p(N_OFF - Lj * lam - LB[j])
        lev0 = E_OFF - N_OFF + T_OFF * lam
        print(f"  {lam:>14.6f} {lev0:>18.4f} {tot:>16.6e} "
              f"{'YES' if tot <= 21 else 'NO':>8}")

    print("\n" + "=" * 78)
    print("D3.4 -- THE GB-5 SHAPE: saturated closed form across tower shapes")
    print("=" * 78)
    print(f"  {'n':>10} {'t':>10} {'e':>5} {'J':>3} {'R3inf':>16} "
          f"{'21J/33':>9} {'RATIO':>10} {'peak j':>7} {'term_0':>9}")
    for (n, t) in [(16, 8), (32, 16), (64, 32), (128, 64), (256, 128),
                   (512, 256), (1024, 512), (2 ** 20, 2 ** 19),
                   (32, 8), (32, 4), (64, 16), (64, 8), (128, 32),
                   (256, 32), (2 ** 41, 2 ** 33)]:
        mm = t.bit_length() - 1
        J = mm
        ee = n // (2 * t)
        if n <= 4096:
            W = list(range(J))
            r3 = R3inf_full(n, t)
            terms = []
            for j in W:
                terms.append(log2_int(Zinf(n, t, j)) - log2_int(Zinf(n, t, j + 1))
                             + n - log2_int(Binf(n, t, j)))
            peak = max(range(J), key=lambda i: terms[i])
            t0 = terms[0]
        else:
            r3 = ee * (1.0 - (2.0 ** (mm + 1) - c_k(mm + 1))) + n * S_m(mm)
            peak, t0 = -1, float("nan")
        print(f"  {n:>10} {t:>10} {ee:>5} {J:>3} {r3:>16.4f} "
              f"{21 * J / 33:>9.4f} {r3 / (21 * J / 33):>10.4f} "
              f"{peak:>7} {t0:>9.4f}")


if __name__ == "__main__":
    main()
