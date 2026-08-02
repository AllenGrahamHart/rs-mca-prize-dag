#!/usr/bin/env python3
"""Final consolidated table: the doubling law's exact status at every tested
(2N, w), plus the delta = Norm / w^(N/2) diagnostic that predicts the break.

THE LAW forces delta(N,w) = delta(N/2,w)^2 (both sides are divided by the same
ceiling w^(N/2) = (w^(N/4))^2).  So the law is equivalent to: no ternary weight-w
f at level N sustains a delta above the SQUARE of the best delta at level N/2.
Since delta(N/2,w) < 1 whenever w is non-saturating, the law's delta collapses
doubly-exponentially in log N while a fresh primitive construction at level N
need not -- which is exactly how the law dies.
"""
import glob, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)

EXH = {  # exhaustive maxnorm(N, w)
 4:  {1:1,2:4,3:9,4:8},
 8:  {1:1,2:16,3:81,4:196,5:529,6:1154,7:2401,8:2176},
 16: {1:1,2:256,3:6561,4:38416,5:279841,6:1331716,7:5764801,8:14760962,9:38950081,
      10:84580802,11:184497889,12:342386306,13:777684769,14:1040410946,
      15:1612931233,16:2311094272},
 32: {1:1,2:65536,3:43046721,4:1475789056,5:78310985281,6:1773467504656,
      7:33232930569601,8:217885999165444,9:1517108809906561,10:7153912066963204,
      11:34921634364102721},
 64: {2:4294967296,3:1853020188851841,4:2177953337809371136,
      5:6132610415680998648961,6:3145186990070779381678336},
}
SRC = {(32,8):"this pilot, exhaustive", (32,9):"this pilot, exhaustive", (32,11):"this pilot, exhaustive",
       (32,10):"this pilot, exhaustive", (32,7):"prior pilot, sandwich-proved",
       (64,2):"this pilot, exhaustive", (64,3):"this pilot, exhaustive",
       (64,4):"this pilot, exhaustive", (64,5):"this pilot, exhaustive",
       (64,6):"this pilot, exhaustive"}

def hunts():
    out = {}
    for p in glob.glob(os.path.join(ROOT, "results", "hunt_N*_w*.json")):
        r = json.load(open(p))
        k = (r["N"], r["w"])
        v = int(r["best_found_norm_exact"])
        if k not in out or v > out[k][0]:
            out[k] = (v, r["REFUTES_CONJECTURE"], r["best_is_primitive"],
                      int(r["target_law_prediction"]), r["n_strict_beats"],
                      r["restarts_done"], os.path.basename(p))
    return out

if __name__ == "__main__":
    H = hunts()
    rows = []
    for N in (8, 16, 32, 64):
        M = N // 2
        for w in range(1, N + 1):
            law = EXH.get(M, {}).get(w)
            if law is None:
                continue
            law = law * law
            exact = EXH.get(N, {}).get(w)
            hv = H.get((N, w))
            if exact is None and hv is None:
                continue
            best = exact if exact is not None else hv[0]
            status = ("LAW HOLDS (exhaustive)" if exact is not None and exact == law
                      else "LAW FAILS (exhaustive)" if exact is not None
                      else "LAW FAILS (witness)" if hv and hv[0] > law
                      else "consistent (hunt, not exhaustive)")
            rows.append({
                "2N": 2*N, "N": N, "w": w, "w_vs_N/2": "%d vs %d" % (w, N//2),
                "law_prediction": str(law), "best_known": str(best),
                "ratio": round(best/law, 6), "status": status,
                "delta_best = best/w^(N/2)": round(best / w**(N//2), 6),
                "delta_law  = (delta at N/2)^2": round(law / w**(N//2), 6),
                "witness_primitive": (hv[2] if hv and hv[0] > law else None),
                "hunt_beats": (hv[4] if hv else None),
                "source": SRC.get((N, w), "prior pilot / hunt"),
            })
    brk = {}
    for N in (8, 16, 32):
        f = [r["w"] for r in rows if r["N"] == N and r["status"].startswith("LAW FAILS")]
        h = [r["w"] for r in rows if r["N"] == N and r["status"].startswith("LAW HOLDS")]
        brk["N=%d" % N] = {"law_holds_w": h, "law_fails_w": f,
                           "smallest_failing_w": min(f) if f else None,
                           "N/2": N//2,
                           "conjectured_range_was": "w <= %d" % (N//2 - 1)}
    json.dump({"table": rows, "break_summary": brk},
              open(os.path.join(ROOT, "results", "final.json"), "w"), indent=1)
    print("%-6s %-4s %-9s %-26s %-26s %-8s %-26s" % ("2N","w","w vs N/2","law prediction","best known","ratio","status"))
    for r in rows:
        print("%-6d %-4d %-9s %-26s %-26s %-8.4f %-26s" %
              (r["2N"], r["w"], r["w_vs_N/2"], r["law_prediction"], r["best_known"],
               r["ratio"], r["status"]))
    print(json.dumps(brk, indent=1))
