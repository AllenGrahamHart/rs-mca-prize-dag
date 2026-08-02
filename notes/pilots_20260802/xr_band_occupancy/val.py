#!/usr/bin/env python3
"""Validation: reproduce the banked V1 planted-band fixture with the new
engine, and time the scan at several shapes."""
import json
import sys
import time

sys.dont_write_bytecode = True
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/"
                   "pilots_20260802/xr_band_occupancy")
from occlib import Row, measure, plant_cores  # noqa: E402

OUT = {}

# ---- banked V1: n=14 k=5 t=4 q=97, core J=7 with 3 live slopes ----------
row = Row(14, 5, 4, 97)
recs = []
for seed in (1, 2, 3):
    Z = list(range(7))
    blk = [[7, 8], [9, 10], [11, 12]]
    assign = {}
    for z, b in zip([3, 10, 17], blk):
        for i in b:
            assign[i] = [(0, z)]
    u, v, _ = plant_cores(row, [Z], assign, seed)
    rec, _, _ = measure(row, u, v, f"V1-seed{seed}")
    recs.append(rec)
    print(f"V1-seed{seed}: ADMISSIBLE={rec['ADMISSIBLE']} maxJ={rec['max_joint_agreement']} "
          f"maxray={rec['max_ray_agreement']} vmax={rec['max_v_side_agreement']} "
          f"ledger={rec['ledger_by_depth']} Gamma_band={rec['Gamma_band_measured']} "
          f"kpack={rec['kpacking_max_intersection']} T1={rec['T1_ok']} "
          f"spread={rec['spread_coset_ok']}")
OUT["V1"] = recs

# ---- timing --------------------------------------------------------------
import random  # noqa: E402
tm = []
for (n, k, t, q) in [(20, 3, 3, 101), (32, 3, 3, 101), (48, 3, 3, 101),
                     (64, 3, 3, 101), (20, 4, 4, 101), (24, 4, 4, 101)]:
    r = Row(n, k, t, q)
    rnd = random.Random(7)
    u = [rnd.randrange(q) for _ in range(n)]
    v = [rnd.randrange(1, q) for _ in range(n)]
    t0 = time.time()
    rec, _, _ = measure(r, u, v, "timing", want_checks=True)
    el = time.time() - t0
    tm.append(dict(n=n, k=k, t=t, q=q, seconds=el, adm=rec["ADMISSIBLE"],
                   N=rec["N_total"], deep=rec.get("deep_pairs")))
    print(f"timing n={n} k={k} t={t}: {el:.2f}s  admissible={rec['ADMISSIBLE']} "
          f"N_total={rec['N_total']} deep={rec.get('deep_pairs')} "
          f"maxJ={rec['max_joint_agreement']} A={r.A}")
OUT["timing"] = tm

p = ("/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/"
     "xr_band_occupancy/val.json")
json.dump(OUT, open(p, "w"), indent=1, default=str)
print("checkpoint:", p)
