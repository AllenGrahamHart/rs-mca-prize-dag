#!/usr/bin/env python3
"""FM3 mechanism pilot -- score the pre-registered predictions against the
measured new points R1/R2/R3."""
from __future__ import annotations
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, _HERE)
from fm3_mine import analyse_case, SUPPORT_ORDERS, NULL_ORDERS  # noqa

pred = json.load(open(os.path.join(_HERE, "PREDICTIONS.json")))
meas = {}
for tag in ["R1", "R2", "R3"]:
    meas[tag] = analyse_case(os.path.join(_HERE, f"k1_{tag}.json"), {})

print("=" * 112)
print("PREDICTION vs MEASUREMENT  (predictions frozen in PREDICTIONS.json "
      "before any of R1/R2/R3 was run)")
print("=" * 112)
print(f"{'pt':3s} {'order':13s} {'|B|100 p/m':>11s} {'|B|90 p/m':>10s} "
      f"{'E[core] p':>9s} {'E[core] m':>9s} {'P>=K pred':>10s} "
      f"{'band':>19s} {'P>=K meas':>10s} {'in?':>4s} "
      f"{'ret pred':>9s} {'ret meas':>9s} {'<=cap?':>6s}")
rows = []
for tag in ["R1", "R2", "R3"]:
    p, m = pred["points"][tag], meas[tag]
    print(f"--- {tag}: n={p['parameters']['n']} q={p['parameters']['q']} "
          f"K={p['parameters']['K']} A={p['parameters']['A']} "
          f"|W_z|pred={p['mean_Wz']:.1f} |W_z|meas={m['mean_Wz']:.1f} "
          f"live pred={p['live_pred']} meas={m['live']}")
    for o in SUPPORT_ORDERS:
        pe, me = p["orders"][o], m["orders"][o]
        lo, hi = pe["pred_p_ge_K_band"]
        inb = lo <= me["p_ge_K_obs"] <= hi
        cap = pe["pred_retention_band"][1]
        rows.append(dict(pt=tag, order=o, band_ok=inb,
                         block_ok=abs(pe["pred_block100"]
                                      - len(me["block_100"])) <= 1,
                         ret_ok=me["retention_measured"] <= cap,
                         p_pred=pe["pred_p_ge_K"], p_meas=me["p_ge_K_obs"],
                         ret_meas=me["retention_measured"]))
        print(f"{tag:3s} {o[4:]:13s} "
              f"{pe['pred_block100']:5d}/{len(me['block_100']):<5d} "
              f"{pe['pred_block90']:4d}/{len(me['block_90']):<5d} "
              f"{pe['pred_mean_core']:9.3f} {me['mean_core']:9.3f} "
              f"{pe['pred_p_ge_K']:10.5f} "
              f"[{lo:.5f},{hi:.5f}] {me['p_ge_K_obs']:10.5f} "
              f"{('YES' if inb else 'no'):>4s} "
              f"{pe['pred_retention_point']:9.4f} "
              f"{me['retention_measured']:9.4f} "
              f"{('ok' if me['retention_measured'] <= cap else 'FAIL'):>6s}")
    for o in NULL_ORDERS:
        me = m["orders"][o]
        print(f"{tag:3s} {o[4:]:13s} {'':11s} {'':10s} "
              f"{m['null_uniform']['mean']:9.3f} {me['mean_core']:9.3f} "
              f"{m['null_uniform']['p_ge_K']:10.5f} {'':19s} "
              f"{me['p_ge_K_obs']:10.5f} {'':4s} "
              f"{m['null_uniform']['pred_retention']:9.4f} "
              f"{me['retention_measured']:9.4f}")

print()
print("=" * 112)
print("REGISTERED CLAIMS")
print("=" * 112)
verdicts = {}

c1 = all(meas[t]["orders"][o]["retention_measured"] <= 0.15
         for t in meas for o in SUPPORT_ORDERS)
worst = max((meas[t]["orders"][o]["retention_measured"], t, o)
            for t in meas for o in SUPPORT_ORDERS)
verdicts["C1"] = (c1, f"max support-keyed retention = {worst[0]:.4f} "
                      f"({worst[1]} {worst[2]}) vs cap 0.15")

c2 = all(meas["R3"]["orders"][o]["retention_measured"] >= 0.75
         for o in NULL_ORDERS)
verdicts["C2"] = (c2, "R3 null retentions = " + ", ".join(
    f"{meas['R3']['orders'][o]['retention_measured']:.3f}"
    for o in NULL_ORDERS))

c3ok, c3d = True, []
for t in ["R2", "R3"]:
    for o in ["ORD-LEX", "ORD-COLEX"]:
        lo, hi = pred["points"][t]["orders"][o]["pred_p_ge_K_band"]
        v = meas[t]["orders"][o]["p_ge_K_obs"]
        ok = lo <= v <= hi
        c3ok &= ok
        c3d.append(f"{t}/{o[4:]}: {v:.5f} in [{lo:.5f},{hi:.5f}] "
                   f"{'YES' if ok else 'NO'}")
verdicts["C3"] = (c3ok, "; ".join(c3d))

r1 = meas["R1"]["orders"]["ORD-LEX"]["p_ge_K_obs"]
r2 = meas["R2"]["orders"]["ORD-LEX"]["p_ge_K_obs"]
verdicts["C4"] = (r1 > 2 * r2,
                  f"P(R1,n=24,|W|={meas['R1']['mean_Wz']:.0f})={r1:.5f} vs "
                  f"P(R2,n=32,|W|={meas['R2']['mean_Wz']:.0f})={r2:.5f}  "
                  f"ratio={r1/r2:.2f} (model predicted 18.1)")

c5ok, c5d = True, []
for t in ["R1", "R2", "R3"]:
    pp = pred["points"][t]["orders"]["ORD-LEX"]["pred_block100"]
    mm = len(meas[t]["orders"]["ORD-LEX"]["block_100"])
    ok = abs(pp - mm) <= 1
    c5ok &= ok
    c5d.append(f"{t}: pred {pp} meas {mm} {'YES' if ok else 'NO'}")
verdicts["C5"] = (c5ok, "; ".join(c5d))

bank = json.load(open(os.path.join(_HERE, "MINE.json")))
q9 = bank["Q9"]["orders"]["ORD-LEX"]["p_ge_K_obs"]
r3 = meas["R3"]["orders"]["ORD-LEX"]["p_ge_K_obs"]
verdicts["C6"] = (r3 > 1.25 * q9,
                  f"R3 (rate 12/32, |W|=50105) P={r3:.5f} vs "
                  f"Q9 (rate 16/32, |W|=50105) P={q9:.5f}  "
                  f"ratio={r3/q9:.3f}; claim needed >1.25")

for k in sorted(verdicts):
    ok, det = verdicts[k]
    claim = [c for c in pred["registered_claims"] if c.startswith(k)][0]
    print(f"{k}: {'PASS' if ok else 'FAIL'}   {claim}")
    print(f"      {det}")

out = dict(measured={t: {o: dict(
    retention=meas[t]["orders"][o]["retention_measured"],
    p_ge_K=meas[t]["orders"][o]["p_ge_K_obs"],
    mean_core=meas[t]["orders"][o]["mean_core"],
    block100=len(meas[t]["orders"][o]["block_100"]),
    block90=len(meas[t]["orders"][o]["block_90"]),
    hist=meas[t]["orders"][o]["hist_counts"],
    null_greedy_p=meas[t]["orders"][o].get("null_greedy", {}).get("p_ge_K"),
    null_marg_p=meas[t]["orders"][o]["null_marginal_matched"]["p_ge_K"],
) for o in SUPPORT_ORDERS + NULL_ORDERS} for t in meas},
    claims={k: dict(pass_=v[0], detail=v[1]) for k, v in verdicts.items()})
with open(os.path.join(_HERE, "SCORE.json"), "w") as fh:
    json.dump(out, fh, indent=1, sort_keys=True)
print("\n->", os.path.join(_HERE, "SCORE.json"))
