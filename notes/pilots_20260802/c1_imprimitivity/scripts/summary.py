#!/usr/bin/env python3
"""Assemble the ladder table, the seed/N0 reformulation check and the c_w table."""
import glob, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)

PRIOR = {   # prior pilot's exhaustive values (c1_norm_ladder/REPORT.md)
 4:  {1:1,2:4,3:9,4:8},
 8:  {1:1,2:16,3:81,4:196,5:529,6:1154,7:2401,8:2176},
 16: {1:1,2:256,3:6561,4:38416,5:279841,6:1331716,7:5764801,8:14760962,9:38950081,
      10:84580802,11:184497889,12:342386306,13:777684769,14:1040410946,
      15:1612931233,16:2311094272},
 32: {1:1,2:65536,3:43046721,4:1475789056,5:78310985281,6:1773467504656,
      7:33232930569601},          # w<=6 exhaustive, w=7 proved by the sandwich
}
NEW = {}    # filled from this pilot's scans

def load():
    for d in ("results/n32", "results/n32big", "results/n64"):
        for p in glob.glob(os.path.join(ROOT, d, "N*_w*.json")):
            r = json.load(open(p))
            N, w = r["N"], r["w"]
            v = int(r.get("max_norm", r.get("max_norm_exact")))
            key = (N, w)
            e = NEW.setdefault(key, {"max": -1, "parts": set(), "nparts": r["nparts"],
                                     "orbits_total": r["n_support_orbits_total"],
                                     "orbits": 0, "polys": 0, "arg": None})
            if r["part"] in e["parts"]:
                continue
            e["parts"].add(r["part"]); e["orbits"] += r["n_support_orbits_this_part"]
            e["polys"] += r["n_polynomials_scanned"]
            if v > e["max"]: e["max"] = v; e["arg"] = r["argmax_f"]

def n0(w):
    n = 4
    while n <= w: n *= 2
    return n

if __name__ == "__main__":
    load()
    rows = []
    for (N, w), e in sorted(NEW.items()):
        complete = len(e["parts"]) == e["nparts"] and e["orbits"] == e["orbits_total"]
        pred = PRIOR.get(N//2, {}).get(w)
        pred = pred**2 if pred else None
        if pred is None and (N//2, w) in NEW:
            pred = NEW[(N//2, w)]["max"]**2
        sup = [i for i, c in enumerate(e["arg"]) if c] if e["arg"] else []
        rows.append({
            "twoN": 2*N, "N": N, "w": w, "complete": complete,
            "parts": "%d/%d" % (len(e["parts"]), e["nparts"]),
            "orbits": "%d/%d" % (e["orbits"], e["orbits_total"]),
            "polynomials_scanned": e["polys"],
            "maxnorm": str(e["max"]),
            "law_prediction_maxnorm(N/2,w)^2": str(pred) if pred else None,
            "LAW_HOLDS": (pred is not None and e["max"] == pred),
            "argmax_support": sup,
            "argmax_imprimitive_all_even": bool(sup) and all(i % 2 == 0 for i in sup),
            "N0(w)": n0(w),
            "seed_form_maxnorm(N0,w)^(N/N0)":
                str(PRIOR.get(n0(w), {}).get(w, "?")) + "^" + str(N//n0(w)),
            "seed_form_matches":
                (PRIOR.get(n0(w), {}).get(w) is not None
                 and PRIOR[n0(w)][w] ** (N // n0(w)) == e["max"]),
        })
    cw = {}
    for w in range(1, 12):
        n = n0(w)
        v = PRIOR.get(n, {}).get(w)
        if v is None and (n, w) in NEW: v = NEW[(n, w)]["max"]
        if v is None: continue
        cw[str(w)] = {"N0": n, "maxnorm(N0,w)": str(v),
                      "c_w = maxnorm(N0,w)^(4/N0)": round(v ** (4.0/n), 6),
                      "rate = c_w^(1/4)": round(v ** (1.0/n), 6),
                      "amgm_rate_sqrt_w": round(w ** 0.5, 6),
                      "saturating": v == w ** (n//2)}
    json.dump({"ladder": rows, "c_w_table": cw}, open(os.path.join(ROOT, "results", "summary.json"), "w"), indent=1)
    for r in rows:
        print("2N=%-4d w=%-3d %-9s max=%-30s law=%-5s seed=%-5s imprimitive_argmax=%-5s scanned=%d"
              % (r["twoN"], r["w"], r["parts"], r["maxnorm"], r["LAW_HOLDS"],
                 r["seed_form_matches"], r["argmax_imprimitive_all_even"], r["polynomials_scanned"]))
    print(json.dumps(cw, indent=1))
