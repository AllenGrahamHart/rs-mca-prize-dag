#!/usr/bin/env python3
"""Aggregate every fixture checkpoint: theorem violations, gate statistics,
maximum occupancy, ledger sharpness."""
import glob
import json

HERE = ("/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/"
        "xr_band_occupancy")
tot = adm = 0
viol = dict(kpacking=0, T1=0, T2=0, T3=0, spread_per_ray=0,
            spread_per_slope=0, line_cap=0, fibre_identity=0)
viol_nonadm = dict(viol)
resel = 0
resel_adm = 0
vgate_fail = 0
best = None
slacks = []
files = sorted(glob.glob(f"{HERE}/battery_*.json") + [f"{HERE}/val.json"])
for fn in files:
    data = json.load(open(fn))
    if isinstance(data, dict):
        data = data.get("V1", [])
    for r in data:
        if not isinstance(r, dict) or "error" in r or "N_total" not in r:
            continue
        tot += 1
        a = r.get("ADMISSIBLE", False)
        adm += bool(a)
        tgt = viol if a else viol_nonadm
        if not r.get("kpacking_ok", True):
            tgt["kpacking"] += 1
        if not r.get("T1_ok", True):
            tgt["T1"] += 1
        if not r.get("T2_ok", True):
            tgt["T2"] += 1
        if not r.get("T3_ok", True):
            tgt["T3"] += 1
        if not r.get("spread_coset_ok", True):
            tgt["spread_per_ray"] += 1
        if not r.get("spread_coset_per_slope_ok", True):
            tgt["spread_per_slope"] += 1
        if r.get("fibre_identity_violations"):
            tgt["fibre_identity"] += 1
        for d, e in r.get("ledger_by_depth", {}).items():
            if not e.get("cap_ok", True):
                tgt["line_cap"] += 1
        if r.get("reselection_slopes", 0):
            resel += 1
            resel_adm += bool(a)
        if a and not r.get("tangent_free_v_direction", True):
            vgate_fail += 1
        if a and (best is None or r["N_total"] > best["N_total"]):
            best = r
        if a and r.get("ledger_slack_vs_measured"):
            slacks.append((r["ledger_slack_vs_measured"], r["fixture"]))

print(f"fixtures measured: {tot}   admissible: {adm}")
print(f"violations on ADMISSIBLE fixtures : {viol}")
print(f"violations on INADMISSIBLE ones   : {viol_nonadm}")
print(f"fixtures with re-selection freedom (a slope with >1 exact-A ray): "
      f"{resel}  (of which admissible: {resel_adm})")
print(f"admissible fixtures failing the (0:1) v-direction gate: {vgate_fail}")
if best:
    print(f"max admissible occupancy: {best['fixture']}  N={best['N_total']} "
          f"n={best['n']} -> N/n={best['N_over_n']:.4f}  N/n^2={best['N_over_n2']:.5f}")
if slacks:
    slacks.sort()
    print(f"ledger slack (sum_d N_d L(d)) / |Gamma_band| over admissible "
          f"fixtures: min {slacks[0][0]:.3f} ({slacks[0][1]}), "
          f"max {slacks[-1][0]:.3f} ({slacks[-1][1]})")
    print(f"  fixtures with slack < 2.2: "
          f"{sum(1 for s, _ in slacks if s < 2.2)} / {len(slacks)}")
json.dump(dict(total=tot, admissible=adm, violations_admissible=viol,
               violations_inadmissible=viol_nonadm, reselection=resel,
               reselection_admissible=resel_adm, v_gate_failures=vgate_fail,
               best=best, slack_min=slacks[0] if slacks else None,
               slack_max=slacks[-1] if slacks else None),
          open(f"{HERE}/aggregate.json", "w"), indent=1, default=str)
print("checkpoint:", f"{HERE}/aggregate.json")
