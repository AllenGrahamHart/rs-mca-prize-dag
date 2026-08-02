#!/usr/bin/env python3
"""dli_norm_gate -- THE RESERVE TEST.

Ground truth: the C2'' pilot's junction-0 rho spread (results/junction0_rho.json),
rho(G) = q^o * skewcount(G) / 2^{|G|} over every support G in Z/(n/2).

The NORM ACCOUNT to be tested:
  hit(G)  = #{eps : H_U(alpha_eps) != empty}  (= "q | Norm" for o=1; for o>1,
             "alpha carries at least one Galois translate of the exponent block")
  MODEL   : skewcount(G) ~ Binomial(hit(G), 1/phi(n)).
  R1 (exact, predicted): sum_G skewcount(G) = (1/phi) sum_G sum_eps |H_U|.
  R3      : does the q-independent multiset {Norm(alpha_eps)} determine rho?
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product as iproduct
from pathlib import Path

sys.dont_write_bytecode = True

import numpy as np

from core import get_zeta
from bridge import norms_batch
from splitting import root_powers, u_masks

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def support_batches(h, w, target_rows=1 << 18):
    signs = np.array(list(iproduct((1, -1), repeat=w)), dtype=np.int8)
    ns = len(signs)
    per = max(1, target_rows // ns)
    buf = []
    for S in combinations(range(h), w):
        buf.append(S)
        if len(buf) == per:
            yield buf, _build(buf, signs, h, ns), ns
            buf = []
    if buf:
        yield buf, _build(buf, signs, h, ns), ns


def _build(supports, signs, h, ns):
    A = np.zeros((len(supports) * ns, h), dtype=np.int8)
    for a, S in enumerate(supports):
        A[a * ns:(a + 1) * ns][:, list(S)] = signs
    return A


def junction0_full(n, q, U, wmax=None, with_norms=False):
    """exact per-support skewcount / hit / sum|H| for every support in Z/(n/2)."""
    h = n // 2
    o = len(U)
    P = root_powers(q, n)
    UM = u_masks(n, U)
    bits = np.array([np.uint64(1) << np.uint64(k) for k in range(h)],
                    dtype=np.uint64)
    per_support = {}                       # mask -> (k, skewcount, hit, sumH)
    normclass = defaultdict(set)           # norm-multiset -> set of rho
    W = h if wmax is None else wmax
    for w in range(0, W + 1):
        if w == 0:
            per_support[0] = (0, 1, 1, h)   # empty support: alpha = 0, all roots
            continue
        for supports, A, ns in support_batches(h, w):
            V = (A.astype(np.int64) @ P) % q
            Zb = (V == 0)
            Zm = (Zb.astype(np.uint64) * bits).sum(axis=1, dtype=np.uint64)
            Hc = np.zeros(len(A), dtype=np.int64)
            for k in range(h):
                mk = UM[k]
                Hc += ((Zm & mk) == mk)
            sol = ((Zm & UM[0]) == UM[0]).astype(np.int64)
            ns_ = ns
            nS = len(supports)
            sc_v = sol.reshape(nS, ns_).sum(axis=1)
            hit_v = (Hc > 0).reshape(nS, ns_).sum(axis=1)
            sH_v = Hc.reshape(nS, ns_).sum(axis=1)
            Nz = norms_batch(A).reshape(nS, ns_) if with_norms else None
            for a, S in enumerate(supports):
                mask = sum(1 << i for i in S)
                per_support[mask] = (w, int(sc_v[a]), int(hit_v[a]),
                                     int(sH_v[a]))
                if with_norms:
                    key = tuple(sorted(int(v) for v in Nz[a]))
                    normclass[key].add(Fraction(int(sc_v[a]) * q**o, 2**w))
    return per_support, normclass


def analyse(n, q, U, ground_truth=None, with_norms=False, wmax=None):
    h = n // 2
    o = len(U)
    per, normclass = junction0_full(n, q, U, wmax=wmax, with_norms=with_norms)
    rhos = {}
    for mask, (w, sc, hit, sH) in per.items():
        if mask == 0:
            continue
        rhos[mask] = Fraction(sc * q**o, 2**w)
    vals = list(rhos.values())
    tot_sc = sum(v[1] for k, v in per.items() if k)
    tot_sH = sum(v[3] for k, v in per.items() if k)
    tot_hit = sum(v[2] for k, v in per.items() if k)
    out = {"n": n, "q": q, "U": list(U), "o": o,
           "n_supports_nonempty": len(rhos),
           "rho_min": str(min(vals)), "rho_max": str(max(vals)),
           "rho_mean": str(sum(vals) / len(vals)),
           "rho_max_over_pred_float": float(max(vals)),
           "R1_sum_skewcount": tot_sc,
           "R1_sum_H_over_phi": Fraction(tot_sH, h),
           "R1_exact": Fraction(tot_sH, h) == tot_sc,
           "total_hit": tot_hit,
           "global_hit_ratio_times_phi":
               float(h * tot_sc / tot_hit) if tot_hit else None}
    if ground_truth:
        out["ground_truth"] = ground_truth
        out["matches_ground_truth"] = (
            str(min(vals)) == ground_truth["min_rho"]
            and str(max(vals)) == ground_truth["max_rho"]
            and str(sum(vals) / len(vals)) == ground_truth["mean_rho"])
    # BINOMIAL MODEL comparison, exactly (expected counts under Bin(hit,1/phi))
    p = Fraction(1, h)
    exp_mean = sum(Fraction(per[m][2], 1) * p * Fraction(q**o, 2**per[m][0])
                   for m in rhos) / len(rhos)
    # exact model distribution of rho over supports: E[rho], Var[rho]
    var_model = sum((Fraction(q**o, 2**per[m][0]) ** 2) *
                    per[m][2] * p * (1 - p) for m in rhos) / len(rhos)
    obs_mean = sum(vals) / len(vals)
    obs_var = sum((v - obs_mean) ** 2 for v in vals) / len(vals)
    # model's max attainable rho (all hits are solutions)
    max_model = max(Fraction(per[m][2] * q**o, 2**per[m][0]) for m in rhos)
    out["model"] = {"E_rho_model": str(exp_mean), "E_rho_observed": str(obs_mean),
                    "E_ratio": float(obs_mean / exp_mean) if exp_mean else None,
                    "Var_rho_model_meanpart": str(var_model),
                    "Var_rho_observed": str(obs_var),
                    "model_rho_ceiling(all hits solve)": str(max_model),
                    "observed_rho_max": str(max(vals)),
                    "ceiling_is_valid_bound": max(vals) <= max_model}
    # worst support
    wm = max(rhos, key=lambda m: rhos[m])
    out["worst_support"] = {"mask": wm,
                            "indices": [i for i in range(h) if (wm >> i) & 1],
                            "size": per[wm][0], "skewcount": per[wm][1],
                            "hit": per[wm][2], "sumH": per[wm][3],
                            "rho": str(rhos[wm])}
    if with_norms:
        multi = {k: v for k, v in normclass.items() if len(v) > 1}
        out["R3_norm_multiset"] = {
            "n_classes": len(normclass), "n_ambiguous": len(multi),
            "law_survives": len(multi) == 0,
            "largest_spread": str(max((max(v) - min(v) for v in multi.values()),
                                      default=0)),
            "compare_L12_difference_multiset": "547 ambiguous of 1064 classes"}
    return out


ALL_JOBS = {
    "a": (32, 97, [1], (32, 2, 97), False),
    "b": (32, 193, [1], (32, 2, 193), False),
    "c": (32, 8353, [1], (32, 2, 8353), False),
    "d": (32, 32801, [1], (32, 2, 32801), False),
    "e": (32, 97, [1, 3], (32, 3, 97), False),
    "f": (16, 97, [1], (16, 2, 97), True),
    "g": (16, 17, [1], (16, 2, 17), True),
}


def main():
    gt = json.loads((ROOT.parent / "c2pp_nullity_structure" / "results"
                     / "junction0_rho.json").read_text())
    gtmap = {(g["n"], g["t"], g["q"]): g["strata"]["0"] for g in gt}
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    out = []
    jobs = ([ALL_JOBS[k] for k in sorted(ALL_JOBS)] if stage == "all"
            else [ALL_JOBS[k] for k in stage.split(",") if k in ALL_JOBS])
    for (n, q, U, key, wn) in jobs:
        r = analyse(n, q, U, ground_truth=gtmap.get(key), with_norms=wn)
        out.append(r)
        print(f"n={n} q={q} U={U}: rho in [{r['rho_min']}, {r['rho_max']}] "
              f"mean {float(Fraction(r['rho_mean'])):.6g} | GT match "
              f"{r.get('matches_ground_truth')} | R1 exact {r['R1_exact']} | "
              f"model E ratio {r['model']['E_ratio']} | "
              f"ceiling valid {r['model']['ceiling_is_valid_bound']}")
        if "R3_norm_multiset" in r:
            print("    R3:", json.dumps(r["R3_norm_multiset"]))
    if stage in ("all", "h"):
        # the (32,q=97) norm-multiset test restricted to |G| <= 8, like L12
        r = analyse(32, 97, [1], with_norms=True, wmax=8)
        r["restricted"] = "supports of size <= 8 only (L12-comparable)"
        out.append(r)
        print("n=32 q=97 |G|<=8 R3:", json.dumps(r["R3_norm_multiset"]))
    tag = stage.replace(",", "")
    (ROOT / "results" / f"reserve_{tag}.json").write_text(
        json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
