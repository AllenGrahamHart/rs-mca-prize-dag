#!/usr/bin/env python3
"""FM3 mechanism pilot -- falsifier hunt against my own mechanism claim.

The claim under attack:  the concentration of the SELECTED family depends
only on (n, A, q, h) through the greedy-depletion profile, and NOT on the
internal shape (g, a, b) of the split-fibre pencil -- i.e. an adversary
cannot keep Gamma_lo large at high density by re-shaping the pencil.

F1a-c : Q9's (n,q,K,h,m) with THREE different (g,a,b) shapes -- the core
        grows from 2 to 8 points and the fibre count shrinks from 8 to 5.
F2a-b : Q4's parameters, same idea.
F3a   : n = 32, rate 1/4, q = 4993 -- q/n = 156, an order of magnitude
        beyond the banked grid's q/n in [3,14] (the prior pilot's biggest
        flagged gap), at the cost of density.

Stage 'pred' freezes the model prediction; stage 'run' measures; stage
'score' compares.
"""
from __future__ import annotations
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.join(os.path.dirname(_HERE), "pb_selector_orders")
sys.dont_write_bytecode = True
sys.path.insert(0, _BANK)
sys.path.insert(0, _HERE)
import k1_orders as KO  # noqa: E402
from fm3_predict import NEW, predict  # noqa: E402
from fm3_mine import analyse_case, SUPPORT_ORDERS, NULL_ORDERS  # noqa: E402

FALS = {
    "F1a": dict(n=32, q=97, m=2, K=16, h=2, g=4, a=7, b=12),
    "F1b": dict(n=32, q=97, m=2, K=16, h=2, g=6, a=6, b=10),
    "F1c": dict(n=32, q=97, m=2, K=16, h=2, g=8, a=5, b=8),
    "F2a": dict(n=32, q=97, m=2, K=8, h=2, g=4, a=3, b=12),
    "F2b": dict(n=32, q=97, m=2, K=8, h=2, g=6, a=2, b=10),
    "F3a": dict(n=32, q=4993, m=2, K=8, h=2, g=2, a=4, b=14),
}
KO.CASES.update(NEW)
KO.CASES.update(FALS)


def main():
    stage = sys.argv[1]
    if stage == "pred":
        out = {t: predict(p) for t, p in FALS.items()}
        path = os.path.join(_HERE, "FALSIFY_PRED.json")
        if os.path.exists(path):
            raise SystemExit("refusing to overwrite a frozen prediction")
        with open(path, "w") as fh:
            json.dump(out, fh, indent=1, sort_keys=True)
        for t in sorted(out):
            e = out[t]["orders"]["ORD-LEX"]
            print(f"{t}: |W_z|={out[t]['mean_Wz']:.1f} "
                  f"|B|100={e['pred_block100']} "
                  f"E[core]={e['pred_mean_core']:.3f} "
                  f"P>=K={e['pred_p_ge_K']:.5f} "
                  f"ret={e['pred_retention_point']:.4f}")
        print("FROZEN ->", path)
    elif stage == "run":
        for t in sys.argv[2:]:
            KO.stage_select(t, 0, KO.CASES[t]["q"], _HERE)
            KO.stage_stats(t, _HERE)
    else:
        pred = json.load(open(os.path.join(_HERE, "FALSIFY_PRED.json")))
        print(f"{'case':5s} {'g':>2s} {'a':>2s} {'b':>3s} {'|W_z|':>8s} "
              f"{'order':11s} {'|B|p/m':>8s} {'E[c] pred':>9s} "
              f"{'E[c] meas':>9s} {'P pred':>8s} {'P meas':>8s} "
              f"{'ret meas':>8s}")
        for t in sorted(FALS):
            fn = os.path.join(_HERE, f"k1_{t}.json")
            if not os.path.exists(fn):
                continue
            m = analyse_case(fn, {})
            p = pred[t]
            prm = FALS[t]
            for o in SUPPORT_ORDERS + NULL_ORDERS:
                pe = p["orders"].get(o)
                me = m["orders"][o]
                if pe:
                    print(f"{t:5s} {prm['g']:2d} {prm['a']:2d} {prm['b']:3d} "
                          f"{m['mean_Wz']:8.1f} {o[4:]:11s} "
                          f"{pe['pred_block100']:3d}/{len(me['block_100']):<4d} "
                          f"{pe['pred_mean_core']:9.3f} {me['mean_core']:9.3f} "
                          f"{pe['pred_p_ge_K']:8.5f} {me['p_ge_K_obs']:8.5f} "
                          f"{me['retention_measured']:8.4f}")
                else:
                    print(f"{t:5s} {prm['g']:2d} {prm['a']:2d} {prm['b']:3d} "
                          f"{m['mean_Wz']:8.1f} {o[4:]:11s} {'':8s} "
                          f"{m['null_uniform']['mean']:9.3f} "
                          f"{me['mean_core']:9.3f} "
                          f"{m['null_uniform']['p_ge_K']:8.5f} "
                          f"{me['p_ge_K_obs']:8.5f} "
                          f"{me['retention_measured']:8.4f}")
            print("-" * 100)


if __name__ == "__main__":
    main()
