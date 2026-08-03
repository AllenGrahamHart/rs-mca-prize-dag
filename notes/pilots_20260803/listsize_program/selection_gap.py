#!/usr/bin/env python3
"""The SELECTION GAP: N_d (selected, L_P >= 2) vs what the list sees.

PROFILE: local.   Run:  tools/ramguard local -- python3 <this>

BAND_LANE_DEFINITIONS item 8 defines N_d = #{depth-d pairs with L_P >= 2}.
THEOREM 2 bounds that by min_z L(w_z, k+d).  This script measures both on
admissible toy fixtures and exhibits the gap: pairs with L_P <= 1 are
invisible to the occupancy ledger but are shadowed into EVERY member's
list (the SHADOW LEMMA).  Seed search keeps only fixtures passing the
pencil-wide tangent gate, k-packing, below-cascade and v-nonvanishing.
"""
import json
import sys
from collections import defaultdict

sys.dont_write_bytecode = True
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/"
                   "pilots_20260802/xr_graded_band_ledger")
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/"
                   "pilots_20260803/listsize_program")
from bandlib import Row, plant, scan  # noqa: E402
from census import profile            # noqa: E402


def admissible(r, u, v, joints, maxagr):
    maxJ = max(joints.values())
    ok = dict(v_nonvanishing=all(x != 0 for x in v),
              tangent_gate_P1=max(maxagr.values()) <= r.A,
              below_cascade=maxJ <= r.A - 2,
              kpack=True)
    big = [Z for Z, s in joints.items() if s >= r.k]
    for a in range(len(big)):
        for b in range(a + 1, len(big)):
            if len(big[a] & big[b]) > r.k - 1:
                ok["kpack"] = False
    return ok


def measure(r, u, v):
    joints, lists, maxagr = profile(r, u, v)
    gates = admissible(r, u, v, joints, maxagr)
    pairs, _ = scan(r, u, v)          # banked engine: slopes thresholded at A
    members = list(range(r.q)) + ['inf']
    L = {m: len(lists[m]) for m in members}
    hi = [(Z, s) for Z, s in joints.items() if s >= r.tau]
    N_sel = 0     # occupancy count: high-depth pairs with L_P >= 2
    N_one = 0     # high-depth pairs with exactly one live slope
    N_zero = 0    # high-depth pairs with NO live slope
    for Z, s in hi:
        LP = len(pairs.get(Z, {}).get("slopes", {})) if Z in pairs else 0
        if LP >= 2:
            N_sel += 1
        elif LP == 1:
            N_one += 1
        else:
            N_zero += 1
    return dict(gates=gates, admissible=all(gates.values()),
                raw_high=len(hi), N_selected=N_sel, N_LP1=N_one,
                N_LP0=N_zero, min_L=min(L.values()), max_L=max(L.values()))


def main():
    out = []
    r = Row(14, 5, 4, 101)
    r.tau = r.k + (r.h + 1) // 2          # A=9, tau=7, high band d>=2
    specs = {
        "core7_1slope": [dict(Z=list(range(7)), slopes=[3], blocks=[[7, 8]])],
        "core7_2slope": [dict(Z=list(range(7)), slopes=[1, 2],
                              blocks=[[7, 8], [9, 10]])],
        "sunflower3": [dict(Z=[0, 1, 2, 3, 4, 5, 6], slopes=[1],
                            blocks=[[10, 11]]),
                       dict(Z=[0, 1, 2, 3, 7, 8, 9], slopes=[2],
                            blocks=[[12, 13]])],
    }
    for name, spec in specs.items():
        found = 0
        for seed in range(1, 61):
            try:
                u, v, _ = plant(r, spec, seed=seed)
            except AssertionError:
                break
            m = measure(r, u, v)
            if not m["admissible"]:
                continue
            m.update(name=name, seed=seed)
            out.append(m)
            print(f"{name:14s} seed={seed:3d} RAW_high={m['raw_high']} "
                  f"N_selected={m['N_selected']} N_LP1={m['N_LP1']} "
                  f"N_LP0={m['N_LP0']} min_L={m['min_L']} max_L={m['max_L']}")
            found += 1
            if found >= 4:
                break
    gap = [o for o in out if o["min_L"] > o["N_selected"]]
    tight = [o for o in out if o["min_L"] == o["raw_high"]]
    summary = dict(fixtures=len(out), admissible=len(out),
                   with_selection_gap=len(gap),
                   min_L_equals_raw_high=len(tight),
                   min_L_below_raw_high=sum(1 for o in out
                                            if o["min_L"] < o["raw_high"]),
                   results=out)
    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(summary, fh, indent=1)
    print(f"\nadmissible fixtures: {len(out)}")
    print(f"  min_z L  >  N_selected (SELECTION GAP): {len(gap)}")
    print(f"  min_z L == RAW_high (shadow is exact) : {len(tight)}")
    print(f"  min_z L  <  RAW_high (P1 violation)   : "
          f"{summary['min_L_below_raw_high']}")


if __name__ == "__main__":
    main()
