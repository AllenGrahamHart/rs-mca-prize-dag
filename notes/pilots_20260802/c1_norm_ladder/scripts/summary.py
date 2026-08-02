#!/usr/bin/env python3
"""Derived exact quantities for the report: router thresholds, F2 density, ladder c_w.

All arithmetic exact (ints / Fractions).  No floats in any certificate field;
the two ppm fields are exact Fractions rendered as "num/den" strings.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction

import numpy as np
from sympy import factorint


def primes_up_to(n: int) -> np.ndarray:
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p:: p] = False
    return np.flatnonzero(s)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    R = args.root
    lad = json.load(open(R + "/ladder.json"))
    c32 = json.load(open(R + "/census_2N32.json"))
    c64 = json.load(open(R + "/census_2N64_w1to6.json"))
    t16 = json.load(open(R + "/table_2N16.json"))
    t8 = json.load(open(R + "/table_2N8.json"))
    orb = json.load(open(R + "/orbit_counts.json"))

    out: dict = {}

    # ---------------- router thresholds ---------------------------------------
    thr = {}
    for twoN in ("8", "16", "32", "64"):
        row = lad["ladder"].get(twoN, {})
        run = 0
        d = {}
        for w in sorted(int(x) for x in row):
            run = max(run, int(row[str(w)]))
            d[w] = str(run)
        thr[twoN] = d
    out["router_threshold_T"] = {
        "meaning": "if q is admissible and q > T(2N,w) then q carries NO ternary "
                   "relation of weight <= w (q-independent, exact)",
        "T": thr,
    }

    # ---------------- F2: exact density of exceptional primes -----------------
    SIEVE = 10 ** 7
    ps = primes_up_to(SIEVE)
    adm32 = ps[ps % 32 == 1]
    dens = []
    minw = {r["q"]: r["min_weight"] for r in c32["census"]}
    for w in range(1, 17):
        T = int(thr["32"][w])
        exc = sum(1 for q, m in minw.items() if m <= w)
        rec = {"w": w, "threshold_T": str(T),
               "n_exceptional_primes_min_weight_le_w": exc}
        if T <= SIEVE:
            tot = int(np.searchsorted(adm32, T, side="right"))
            rec["n_admissible_primes_le_T"] = tot
            rec["exceptional_fraction"] = str(Fraction(exc, tot)) if tot else None
            rec["exceptional_fraction_ppm_floor"] = (exc * 1000000) // tot if tot else None
        dens.append(rec)
    out["F2_density_2N32"] = {
        "sieve_limit": SIEVE,
        "note": "fraction = (# admissible q <= T that carry a weight-<=w relation) "
                "/ (# admissible q <= T)",
        "rows": dens,
    }

    # ---------------- census growth across the ladder -------------------------
    out["census_growth"] = {
        "2N=8": {"weights": "1-4 (complete)", "n_primes": 0, "largest": None},
        "2N=16": {"weights": "1-8 (complete)",
                  "n_primes": t16["n_admissible_primes_in_census"],
                  "largest": max(r["q"] for r in t16["census"]),
                  "primes": [r["q"] for r in t16["census"]]},
        "2N=32": {"weights": "1-16 (complete)",
                  "n_primes": c32["n_admissible_primes_total"],
                  "largest": c32["largest_admissible_prime"],
                  "smallest": c32["smallest_admissible_prime"]},
        "2N=64": {"weights": "1-6 (partial)",
                  "n_primes": c64["n_admissible_primes_total"],
                  "largest": c64["largest_admissible_prime"],
                  "smallest": c64["smallest_admissible_prime"]},
    }

    # ---------------- c_w in the stable range ---------------------------------
    cw = []
    for e in lad["scaling_by_weight"]:
        w = e["w"]
        pts = {p["N"]: int(p["max_norm"]) for p in e["points"]}
        stable = None
        for N in sorted(pts):
            if 2 * N in pts and pts[2 * N] == pts[N] ** 2:
                stable = N
                break
        rec = {"w": w,
               "saturates_amgm_from": next((p["N"] for p in e["points"]
                                            if p["saturates"]), None),
               "stable_from_N": stable,
               "c_w_exact_when_integer": next(
                   (p["c_w_as_integer_Nover4_root"] for p in e["points"]
                    if p["c_w_as_integer_Nover4_root"] is not None
                    and (stable is None or p["N"] >= stable)), None),
               "law_maxnorm_N_w": ("%s^(N/%d)" % (pts[stable], stable))
               if stable else None,
               "points": {str(p["N"]): p["max_norm"] for p in e["points"]}}
        cw.append(rec)
    out["c_w_table"] = cw

    # ---------------- full-weight (w = N) anomaly -----------------------------
    fw = []
    for twoN, N in (("8", 4), ("16", 8), ("32", 16)):
        v = int(lad["ladder"][twoN][str(N)])
        f = factorint(v)
        odd = v
        e2 = 0
        while odd % 2 == 0:
            odd //= 2
            e2 += 1
        fw.append({"twoN": int(twoN), "N": N, "w": N, "max_norm": str(v),
                   "factorisation": {str(k): int(e) for k, e in f.items()},
                   "equals_2_pow_N_minus_1_times_P": e2 == N - 1,
                   "P": str(odd), "P_is_admissible": odd % (2 * N) == 1,
                   "amgm_ceiling": str(N ** (N // 2)),
                   "ratio_to_ceiling": str(Fraction(v, N ** (N // 2)))})
    out["full_weight_anomaly"] = {
        "note": "the maximum over ALL nonzero ternary f at weight w = N",
        "rows": fw,
    }

    # ---------------- orbit table --------------------------------------------
    out["orbit_counts"] = {k: {"|U|": v["|U|"], "|G|": v["|G|"],
                               "rows": v["rows"]} for k, v in orb.items()}

    # ---------------- q = 70529 ------------------------------------------------
    q = 70529
    rec = next(r for r in c32["census"] if r["q"] == q)
    out["q_70529"] = {
        "found_at_2N32": True, "min_weight": rec["min_weight"],
        "witness_f": rec["witness_f"], "Norm_f": rec["Norm_f"],
        "cofactor": rec["cofactor"],
        "n_weights_at_which_it_appears": sum(
            1 for pw in c32["per_weight"] if q in pw["primes_at_this_weight"]),
        "weights_at_which_it_appears": [pw["w"] for pw in c32["per_weight"]
                                        if q in pw["primes_at_this_weight"]],
        "prior_pilot_min_weight": 7,
        "agrees_with_prior_pilot": rec["min_weight"] == 7,
        "appears_in_2N16_census": q in [r["q"] for r in t16["census"]],
        "appears_in_2N64_w_le_6_census": q in [r["q"] for r in c64["census"]],
        "note": "70529 = 2311094272 / 2^15 is exactly the odd part of the GLOBAL "
                "maximum norm at 2N=32 (weight 16)",
    }

    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)

    print("== router thresholds T(2N=32, w) ==")
    for w in range(1, 17):
        print("  w<=%2d  T=%-12s" % (w, thr["32"][w]))
    print("\n== F2 density at 2N=32 ==")
    for r in dens:
        print("  w<=%2d T=%-12s exceptional=%-6d admissible<=T=%-9s frac=%s"
              % (r["w"], r["threshold_T"], r["n_exceptional_primes_min_weight_le_w"],
                 r.get("n_admissible_primes_le_T", "(>1e7)"),
                 r.get("exceptional_fraction", "-")))
    print("\n== c_w ==")
    for r in cw:
        print("  w=%2d stable_from_N=%s c_w=%s law=%s"
              % (r["w"], r["stable_from_N"], r["c_w_exact_when_integer"],
                 r["law_maxnorm_N_w"]))
    print("\n== full weight w=N ==")
    for r in fw:
        print("  2N=%-3d max=%-12s = 2^%d * %s (P admissible: %s) ratio_to_ceiling=%s"
              % (r["twoN"], r["max_norm"], r["N"] - 1, r["P"], r["P_is_admissible"],
                 r["ratio_to_ceiling"]))
    print("\n== q=70529 ==", json.dumps(
        {k: v for k, v in out["q_70529"].items() if k != "witness_f"}))


if __name__ == "__main__":
    main()
