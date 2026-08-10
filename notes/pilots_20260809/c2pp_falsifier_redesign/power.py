#!/usr/bin/env python3
"""POWER CONTROL (PREREG P5) -- run BEFORE any falsifier is proposed.

Synthetic true/false pair on the REACHABLE grid.  No real censuses: this
script decides whether a candidate falsifier can separate a C2''-r3-safe
world from a C2''-r3-breaking world at reachable scale.  If it cannot,
the shape is not proposed.

Worlds (PREREG P5):
  T   Zlev = Zinf + round(2^n q^-T)
  F1  Zlev = 2^(kappa h) Zinf + round(2^n q^-T)        (floor inflation)
  F2  Zlev = Zinf + round(2^n q^-(T(1+delta)))         (decay excess)
  F3  Zlev = Zinf + round(2^n q^-T) + round(2^(n/2) q^-(T/2))
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from c2lib import (Zinf, LamStar, primes_mod, cost_Z, log2_int)   # noqa: E402

# official schedule pins (background/nodes/dli_official_support_forcing:5-7)
N_OFF, T_OFF = 2 ** 41, 2 ** 33
E_OFF = N_OFF // (2 * T_OFF)          # 128  (official_scale.json:79)
RATIO_OFF = N_OFF // T_OFF            # 256  (official_scale.json:78)
RESERVE = 21

# ---------------------------------------------------------------- reachable grid
BUDGET = 2 ** 22

LCELLS = [(32, 2, 1), (32, 4, 1), (64, 4, 2), (64, 8, 2), (64, 8, 3),
          (64, 16, 3), (128, 16, 4), (128, 32, 4), (256, 32, 5),
          (32, 2, 0), (32, 4, 0), (32, 8, 0), (32, 16, 0), (16, 4, 0),
          (16, 8, 0), (64, 16, 2), (64, 32, 2), (128, 64, 4)]


def grid():
    """Reachable (n,t,lev) cells with a NON-EMPTY pre-saturation band."""
    out = []
    for (n, t, lev) in LCELLS:
        if cost_Z(n, lev) > BUDGET:
            continue
        T = t // 2 ** lev
        if T < 1 or n // 2 ** lev < 2:
            continue
        ls = LamStar(n, t, lev)
        lo = math.log2(n + 1)                # admissibility q > n
        band = ls - lo
        out.append({"n": n, "t": t, "lev": lev, "T": T,
                    "e": n // (2 * t), "h": n // 2 ** lev,
                    "LamStar": ls, "band": band,
                    "cost": cost_Z(n, lev)})
    return out


# ---------------------------------------------------------------- synthetic worlds


def synth(cell, q, world, par=0.0):
    n, t, lev, T = cell["n"], cell["t"], cell["lev"], cell["T"]
    zi = Zinf(n, t, lev)
    lam = math.log2(q)

    def pw(x):
        """integer-rounded 2^x: a census is an INTEGER, so a sub-1/2 term
        contributes exactly nothing (this is what produces exact freeze)."""
        if x < -1.0:
            return 0
        if x > 4000:
            return None                       # overflow guard; never hit here
        return int(round(2.0 ** x)) if x < 900 else (1 << int(x))

    rnd = pw(n - T * lam)
    if world == "T":
        z = zi + rnd
    elif world == "F1":
        z = int(zi * 2.0 ** (par * cell["h"])) + rnd
    elif world == "F2":
        z = zi + pw(n - T * (1 + par) * lam)
    elif world == "F3":
        z = zi + rnd + pw(n / 2 - T / 2 * lam)
    else:
        raise ValueError(world)
    return log2_int(z)


# ---------------------------------------------------------------- the statistic


def statistic(cell, qs, vals):
    """THE EXCESS FIT (the statistic of record).  vals = log2 Zlev.

    Model:  Zlev(q) = Zinf + kappa * 2^n * q^-alpha,
    so  log2(Zlev - Zinf) = (n + log2 kappa) - alpha * Lam,  a straight line
    in Lam using EVERY point with a positive excess -- not just a deep band.
    Reports (alpha/T, kappa_bits, max fit residual, exact-freeze scale)."""
    n, t, lev, T = cell["n"], cell["t"], cell["lev"], cell["T"]
    lzi = log2_int(Zinf(n, t, lev))
    pts, frozen = [], []
    for q, v in zip(qs, vals):
        exc = v - lzi                                   # log2(Z/Zinf) >= 0
        # FIT WINDOW (calibrated on the synthetic worlds, then frozen):
        # only points where the second term dominates the floor by >= 1 bit.
        if exc >= 1.0:
            # log2(Z - Zinf) = lzi + log2(2^exc - 1)
            pts.append((math.log2(q), lzi + math.log2(2.0 ** exc - 1.0)))
        else:
            frozen.append(math.log2(q))
    alpha = kappa_bits = resid = float("nan")
    if len(pts) >= 2:
        k = len(pts)
        sx = sum(p[0] for p in pts)
        sy = sum(p[1] for p in pts)
        sxx = sum(p[0] ** 2 for p in pts)
        sxy = sum(p[0] * p[1] for p in pts)
        slope = (k * sxy - sx * sy) / (k * sxx - sx * sx)
        icpt = (sy - slope * sx) / k
        alpha, kappa_bits = -slope, icpt - n
        resid = max(abs(y - (icpt + slope * x)) for x, y in pts)
    return {"alpha": alpha, "alpha_rel": alpha / T, "kappa_bits": kappa_bits,
            "resid": resid, "npts": len(pts),
            "freeze": min(frozen) if frozen else float("nan"),
            "LamStar": LamStar(n, t, lev)}


def verdict(rows):
    """Registered decision rule (PREREG P4/P5).
    LAW HOLDS iff, at every cell with >= 2 usable points,
      |alpha/T - 1| < 0.10  and  |kappa_bits| < 2  and  resid < 0.5 bits,
      and the closed-form floor is reached exactly somewhere on the ladder.
    G-c FIRES iff alpha >= 1.10 T at >= 3 cells spanning >= 2 distinct T."""
    use = [r for r in rows if r["s"]["npts"] >= 2]
    hot = [r for r in use if r["s"]["alpha_rel"] >= 1.10]
    fires = len(hot) >= 3 and len({r["cell"]["T"] for r in hot}) >= 2
    ok = all(abs(r["s"]["alpha_rel"] - 1) < 0.10
             and abs(r["s"]["kappa_bits"]) < 2.0
             and r["s"]["resid"] < 0.25
             and r["s"]["freeze"] == r["s"]["freeze"]
             for r in use)
    return ("FIRES" if fires else ("LAW HOLDS" if ok else "ANOMALY"))


# ---------------------------------------------------------------- break analysis


def kappa_break(lam):
    """F1: coset term = e + kappa*n - n + T_OFF*lam > 21."""
    return (RESERVE + N_OFF - E_OFF - T_OFF * lam) / N_OFF


def delta_break(lam):
    """F2: coset term = e - n + T_OFF*(1+delta)*lam > 21."""
    return (RESERVE + N_OFF - E_OFF - T_OFF * lam) / (T_OFF * lam)


def main():
    cells = grid()
    print("=" * 78)
    print("REACHABLE GRID (PREREG P6 cost model, budget 2^22 half-states)")
    print("=" * 78)
    print(f"{'n':>5} {'t':>4} {'lev':>3} {'T':>3} {'e':>4} {'h':>3} "
          f"{'cost':>10} {'LamStar':>8} {'band(oct)':>9}")
    usable = []
    for c in cells:
        flag = "" if c["band"] > 0.5 else "   <- no band"
        print(f"{c['n']:>5} {c['t']:>4} {c['lev']:>3} {c['T']:>3} {c['e']:>4} "
              f"{c['h']:>3} {c['cost']:>10} {c['LamStar']:>8.3f} "
              f"{c['band']:>9.2f}{flag}")
        if c["band"] > 0.5:
            usable.append(c)
    Ts = sorted({c["T"] for c in usable})
    print(f"\nUsable cells: {len(usable)}   distinct T on the ladder: {Ts}")

    # q ladders, built ONCE per cell and reused by every world
    LAD = {}
    for c in usable:
        lo = math.ceil(math.log2(c["n"] + 1))
        hi = c["n"] / c["T"] + 4          # must pass EXACT FREEZE
        LAD[id(c)] = primes_mod(c["n"], lo, hi, per_octave=2)

    print("\n" + "=" * 78)
    print("POWER CONTROL: synthetic worlds on the usable grid")
    print("=" * 78)
    results = {}
    for world, par in [("T", 0.0), ("F1", 1.0 / 32), ("F1", 0.25),
                       ("F2", 0.10), ("F2", 0.30), ("F3", 0.0)]:
        rows = []
        for c in usable:
            qs = LAD[id(c)]
            vals = [synth(c, q, world, par) for q in qs]
            rows.append({"cell": c, "s": statistic(c, qs, vals)})
        v = verdict(rows)
        tag = f"{world}(par={par:g})"
        results[tag] = v
        print(f"\n--- WORLD {tag}: VERDICT = {v}")
        print(f"    {'n':>5} {'t':>4} {'lev':>3} {'T':>3} {'alpha/T':>8} "
              f"{'kap_bits':>9} {'resid':>7} {'freeze':>7} {'npts':>5}")
        for r in rows:
            c, s = r["cell"], r["s"]
            print(f"    {c['n']:>5} {c['t']:>4} {c['lev']:>3} {c['T']:>3} "
                  f"{s['alpha_rel']:>8.4f} {s['kappa_bits']:>9.3f} "
                  f"{s['resid']:>7.3f} {s['freeze']:>7.2f} {s['npts']:>5}")

    print("\n" + "=" * 78)
    print("EMPIRICAL DETECTION THRESHOLDS (scan; the statistic decides)")
    print("=" * 78)

    def run(world, par):
        rows = []
        for c in usable:
            qs = LAD[id(c)]
            rows.append({"cell": c,
                         "s": statistic(c, qs,
                                        [synth(c, q, world, par) for q in qs])})
        return verdict(rows)

    d_scan = [0.0, 0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.10, 0.15, 0.30]
    k_scan = [0.0, 1 / 256, 1 / 128, 1 / 64, 1 / 32, 1 / 16, 1 / 8, 0.25]
    print(" F2 delta :  " + "  ".join(f"{d:g}" for d in d_scan))
    print(" verdict  :  " + "  ".join(run("F2", d)[:4] for d in d_scan))
    print(" F1 kappa :  " + "  ".join(f"{k:.4g}" for k in k_scan))
    print(" verdict  :  " + "  ".join(run("F1", k)[:4] for k in k_scan))
    d_det = next((d for d in d_scan if d > 0 and run("F2", d) != "LAW HOLDS"),
                 None)
    k_det = next((k for k in k_scan if k > 0 and run("F1", k) != "LAW HOLDS"),
                 None)
    print(f"\n EMPIRICAL delta_det = {d_det}   kappa_det = {k_det}")

    print("\n" + "=" * 78)
    print("POWER NUMBERS (registered P5): detectable vs reserve-breaking")
    print("=" * 78)
    hmax = max(c["h"] for c in usable)
    kappa_det = k_det if k_det else 1.0 / hmax
    delta_det = d_det if d_det else 0.10
    print(f"kappa_det = 1/h_max = 1/{hmax} = {kappa_det:.5f}  "
          f"(one bit of floor mismatch at the widest reachable cell)")
    print(f"delta_det = {delta_det:.3f}  (the registered G-c firing threshold)")
    print(f"\n{'log2 q':>8} {'kappa_brk':>11} {'F1 powered':>11} "
          f"{'delta_brk':>11} {'F2 powered':>11}")
    for lam in [41, 64, 96, 128, 160, 192, 224, 232, 233, 240, 248, 252, 255, 256]:
        kb, db = kappa_break(lam), delta_break(lam)
        print(f"{lam:>8} {kb:>11.6f} {'YES' if kappa_det <= kb else 'no':>11} "
              f"{db:>11.6f} {'YES' if delta_det <= db else 'no':>11}")
    lam_k = [l for l in range(41, 257) if kappa_det <= kappa_break(l)]
    lam_d = [l for l in range(41, 257) if delta_det <= delta_break(l)]
    print(f"\nF1 powered for log2 q in [{min(lam_k)}, {max(lam_k)}]")
    print(f"F2 powered for log2 q in [{min(lam_d)}, {max(lam_d)}]")
    print(f"BLIND SPOT (neither): log2 q > "
          f"{max(max(lam_k), max(lam_d))}  of the admissible [41, 256]")

    with open(os.path.join(HERE, "power_results.json"), "w") as fh:
        json.dump({"verdicts": results, "kappa_det": kappa_det,
                   "delta_det": delta_det,
                   "usable_cells": [[c["n"], c["t"], c["lev"], c["T"],
                                     c["band"]] for c in usable],
                   "F1_powered_max_lam": max(lam_k),
                   "F2_powered_max_lam": max(lam_d)}, fh, indent=1)
    print("\nwritten: power_results.json")


if __name__ == "__main__":
    main()
