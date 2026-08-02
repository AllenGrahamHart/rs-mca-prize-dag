#!/usr/bin/env python3
"""FM3 mechanism pilot -- PRE-REGISTRATION of predictions for three NEW
parameter points, from the greedy-depletion model fitted on nothing.

Written and committed to PREDICTIONS.json BEFORE the new points are run.
Run:  tools/ramguard local -- python3 .../fm3_predict.py
"""
from __future__ import annotations
import json
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, _HERE)
from fm3_mine import (greedy_pi, greedy_marginals, greedy_overlap,  # noqa
                      hypergeom_overlap, tail, GREEDY_SPEC)

# --- the three new points --------------------------------------------------
# R1 : n = 24  -- a NEW domain size at rate 1/4, density matched to R2.
#      separates "n-degradation" from "density" (the banked grid has one n).
# R2 : n = 32, rate 1/4, q = 641 -- same shape as Q4/Q5/Q6, lower density,
#      density-matched to R1.
# R3 : n = 32, q = 97, rate 3/8 -- density EXACTLY matched to Q9 (50105/slope)
#      with a different A/n and K.  separates "density" from "A/n, K".
NEW = {
    "R1": dict(n=24, q=73, m=2, K=6, h=2, g=2, a=3, b=10),
    "R2": dict(n=32, q=641, m=2, K=8, h=2, g=2, a=4, b=14),
    "R3": dict(n=32, q=97, m=2, K=12, h=2, g=2, a=6, b=14),
}


def predict(prm):
    n, q, K, h, m = prm["n"], prm["q"], prm["K"], prm["h"], prm["m"]
    A = K + h
    CnA = math.comb(n, A)
    Wz = CnA / q ** h
    live = q                      # every slope carries witnesses at |W_z|>>1
    out = dict(parameters=dict(prm, A=A), mean_Wz=Wz, live_pred=live,
               A_minus_m=A - m, total_witnesses_pred=CnA / q ** (h - 1),
               orders={})
    n0 = hypergeom_overlap(n, A)
    out["null_uniform"] = dict(mean=sum(t * n0[t] for t in range(A + 1)),
                               p_ge_K=tail(n0, K),
                               pred_retention=(1 - tail(n0, K)) ** (live - 1))
    for o, (seq, pref) in GREEDY_SPEC.items():
        pi = greedy_pi(n, A, q, h, pref)
        marg = greedy_marginals(pi, n, A)
        ov = greedy_overlap(pi, n, A)
        P = tail(ov, K)
        chi = sum(t * ov[t] for t in range(A + 1))
        var = sum(t * t * ov[t] for t in range(A + 1)) - chi * chi
        b100 = sum(1 for p in marg if p ** live >= 0.5)
        b90 = sum(1 for p in marg if p >= 0.90)
        r = (1 - P) ** (live - 1)
        out["orders"][o] = dict(
            model_marginals=marg,
            pred_block100=b100, pred_block90=b90,
            pred_mean_core=chi, pred_sd_core=math.sqrt(max(var, 0.0)),
            pred_p_ge_K=P,
            pred_p_ge_K_band=[P / 2.0, min(1.0, P * 2.0)],
            pred_retention_point=r,
            pred_retention_band=[0.0, min(1.0, 30 * max(r, 1.0 / live))],
        )
    return out


def main():
    pred = dict(
        generated="2026-08-02",
        model=("parameter-free greedy-depletion Markov chain: "
               "nu(i,a)=C(n-i,A-a)/q^h, inclusion prob "
               "(1-e^-nu_in)/(1-e^-(nu_in+nu_out)) for include-first orders "
               "(mirrored for exclude-first); two independent copies "
               "convolved by exact 3-index DP.  NO parameter is fitted to "
               "any measured selection."),
        validation=("on the 12 banked cases the model reproduces "
                    "P[core>=K] of the selected family to within a factor "
                    "0.78-1.35 at every n=32 point with >=1700 witnesses "
                    "per slope, and 1.5-2.2 down to ~300/slope."),
        registered_claims=[
            "C1  every support-keyed order at R1,R2,R3 has retention <= 0.15",
            "C2  every null-control (hash) order at R3 has retention >= 0.75",
            "C3  measured P[core>=K] lands inside the registered band "
                "[P/2, 2P] for ORD-LEX and ORD-COLEX at R2 and R3",
            "C4  N-DEGRADATION: at matched density (138 vs 157 witnesses per "
                "slope) the measured P[core>=K] for ORD-LEX at R1 (n=24) "
                "EXCEEDS that at R2 (n=32) by a factor > 2",
            "C5  measured global block |B|_100 for ORD-LEX equals the "
                "predicted value +/- 1 at all three points",
            "C6  DENSITY IS NOT THE CONTROLLING VARIABLE: R3 has EXACTLY the "
                "same witness density as Q9 (50105/slope) but a smaller "
                "K/n; measured P[core>=K] for ORD-LEX at R3 will DIFFER "
                "from Q9's 0.0533 by more than 25% -- specifically it will "
                "be LARGER (model: R3 > Q9)",
        ],
        points={},
    )
    for tag, prm in sorted(NEW.items()):
        pred["points"][tag] = predict(prm)
        p = pred["points"][tag]
        print(f"[{tag}] n={prm['n']} q={prm['q']} K={prm['K']} "
              f"A={prm['K']+prm['h']} h={prm['h']} "
              f"|W_z|={p['mean_Wz']:.1f} live={p['live_pred']}")
        print(f"      uniform null: E[core]={p['null_uniform']['mean']:.3f} "
              f"P>=K={p['null_uniform']['p_ge_K']:.3e} "
              f"ret={p['null_uniform']['pred_retention']:.3f}")
        for o, e in sorted(p["orders"].items()):
            print(f"      {o:14s} |B|100={e['pred_block100']:2d} "
                  f"|B|90={e['pred_block90']:2d} "
                  f"E[core]={e['pred_mean_core']:6.3f} "
                  f"sd={e['pred_sd_core']:5.3f} "
                  f"P>=K={e['pred_p_ge_K']:.5f} "
                  f"band=[{e['pred_p_ge_K_band'][0]:.5f},"
                  f"{e['pred_p_ge_K_band'][1]:.5f}] "
                  f"ret={e['pred_retention_point']:.4f} "
                  f"(<= {e['pred_retention_band'][1]:.3f})")
    path = os.path.join(_HERE, "PREDICTIONS.json")
    if os.path.exists(path):
        raise SystemExit("PREDICTIONS.json already exists -- refusing to "
                         "overwrite a pre-registration")
    with open(path, "w") as fh:
        json.dump(pred, fh, indent=1, sort_keys=True)
    print("\nPRE-REGISTERED ->", path)


if __name__ == "__main__":
    main()
