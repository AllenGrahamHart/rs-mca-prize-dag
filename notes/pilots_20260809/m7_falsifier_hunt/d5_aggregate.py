#!/usr/bin/env python3
"""D5 -- the per-cell verdict table with MARGINS.

Reads every out_*.json produced by d2_hunt.py and reports, per cell:
the guarded family sizes, the overlap distribution vs the (JB3)/(CJ2)
cap r_J, the two falsifier flags, the decisive FIRE_SIGMA rate, the
MARGIN sigma/2a (the round-25 threshold quantity: < 1 means the
complement orientation wins), and the matched random-flat control.

Stdlib only.  Run via tools/ramguard tiny -- python3 from repo root.
"""
from __future__ import annotations

import glob
import json
import os

DIR = ("/home/u2470931/smooth-read-solomin/prize/notes/"
       "pilots_20260809/m7_falsifier_hunt")


def main():
    out = []
    for p in sorted(glob.glob(DIR + "/out_*.json")):
        cid = os.path.basename(p)[4:-5]
        try:
            d = json.load(open(p))
        except Exception:
            continue
        s, recs = d["summary"], d["recs"]
        c = s["cell"]
        m2 = [r for r in recs if r.get("NSPLIT_G", 0) >= 2]
        m3 = [r for r in recs if r.get("NSPLIT_G", 0) >= 3]
        marg = [r["ANN_SIGMA_G"] / (2 * r["ANN_A_G"]) for r in m2
                if r.get("ANN_A_G")]
        marg3 = [r["ANN_SIGMA_G"] / (2 * r["ANN_A_G"]) for r in m3
                 if r.get("ANN_A_G")]
        ovl_g = s.get("OVL_HIST_G_MERGED", {})
        ovl_s = s.get("OVL_HIST_S_MERGED", {})
        tot_g = sum(ovl_g.values()) or 1
        tot_s = sum(ovl_s.values()) or 1
        rj = c["r_J"]
        out.append({
            "cell": cid, "rate": "1/%d" % c["rate"], "M": c["M"],
            "t": c["t"], "ell": c["ell"], "b": c["b"], "u": c["u"],
            "d": c["d"], "e": c["e"], "r_J": rj, "N": c["N"], "n": c["n"],
            "q": s["q"], "configs": s["configs"],
            "2d_minus_N": 2 * c["d"] - c["N"],
            "NSPLIT_G_mean": s["NSPLIT_G_mean"],
            "NSPLIT_G_max": s["NSPLIT_G_max"],
            "guard_survival": s["guard_survival_G_over_S"],
            "cfg_m_ge3": len(m3),
            "OVL_MAX_G": s["OVL_MAX_G_observed"],
            "frac_pairs_at_cap_rJ_G": round(ovl_g.get(str(rj), 0) / tot_g, 5),
            "frac_pairs_at_cap_rJ_SPLITONLY":
                round(ovl_s.get(str(rj), 0) / tot_s, 5),
            "PENCIL_MAX_hist": s.get("PENCIL_MAX_hist"),
            "FIRE_KCORE_frac_ge3": s.get("FIRE_KCORE_frac_ge3"),
            "FIRE_UNION_frac_ge2": s.get("FIRE_UNION_frac_ge2"),
            "FIRE_SIGMA_frac_ge3": s.get("FIRE_SIGMA_frac_ge3"),
            "FIRE_SIGMA_count_ge3": s.get("FIRE_SIGMA_count_ge3"),
            "MARGIN_sigma_over_2a_mean_m2":
                round(sum(marg) / len(marg), 4) if marg else None,
            "MARGIN_sigma_over_2a_min_m2":
                round(min(marg), 4) if marg else None,
            "MARGIN_sigma_over_2a_mean_m3":
                round(sum(marg3) / len(marg3), 4) if marg3 else None,
            "RAND_FIRE_SIGMA_frac_ge3": s.get("RAND_FIRE_SIGMA_frac_ge3"),
            "RAND_OVL_MAX": s.get("RAND_OVL_MAX_observed"),
            "SUBFIRE_MAX_hist": s.get("SUBFIRE_MAX_hist"),
            "SUBFIRE_all_exhaustive": s.get("SUBFIRE_all_exhaustive"),
            "elapsed_s": s.get("elapsed_s"),
        })
    out.sort(key=lambda r: (r["cell"]))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
