#!/usr/bin/env python3
"""Score the frozen PREDICTIONS.json against MEASURE_S*.json, and fit the
CORRECTED |Gamma| law.

Corrected law (post-hoc, stated here for the record and cross-checked on
every ladder point):

    witnesses(q)  =  C(F-g, a)            [planted split-fibre family]
                   + C(n,A) / q^(h-1)     [random supply]
    |Gamma|(q)    =  N_split(F,g,a)       [distinct planted slopes]
                   + random live slopes,        both capped by q
    |Gamma_lo|(q) =  random live slopes ONLY
                     (the planted part is entirely high-core; see
                      construction.py, the self-collision identity)
"""

from __future__ import annotations

import json
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from construction import n_slopes                        # noqa: E402

SHAPES = ["S1", "S2", "S3", "S4"]
OUT = os.path.join(HERE, "SCORE.json")


def main() -> None:
    with open(os.path.join(HERE, "PREDICTIONS.json")) as fh:
        PRED = json.load(fh)
    res = {"claims": {}, "corrected_law": []}

    c1 = {"pass": 0, "fail": 0, "worst": None}
    c2 = {"pass": 0, "fail": 0}
    c3 = {"pass": 0, "fail": 0, "vacuous": 0}
    c4 = {"pass": 0, "fail": 0}
    c5lo = {"pass": 0, "fail": 0, "vals": []}
    c5hi = {"pass": 0, "fail": 0, "vals": []}
    corr_w = []
    corr_g = []

    for sh in SHAPES:
        p = os.path.join(HERE, f"MEASURE_{sh}.json")
        if not os.path.exists(p):
            continue
        md = json.load(open(p))
        sd = PRED["shapes"][sh]
        prm = sd["params"]
        F = prm["n"] // prm["m"]
        Bpool = F - prm["g"]
        planted_w = math.comb(Bpool, prm["a"])
        planted_g = n_slopes(F, prm["g"], prm["a"])
        M_inf = sd["M_inf_greedy_lowcore"]
        for pt in md["points"]:
            q, lam = pt["q"], pt["mean_Wz_pred"]
            # C1 naive witness law
            if pt["witnesses_pred"] >= 100:
                r = pt["witnesses_meas"] / pt["witnesses_pred"]
                if 0.5 <= r <= 2.0:
                    c1["pass"] += 1
                else:
                    c1["fail"] += 1
                    if c1["worst"] is None or abs(math.log(r)) > abs(
                            math.log(c1["worst"][2])):
                        c1["worst"] = (sh, q, r)
            # C2 planted floor
            (c2["pass"] if pt["gamma_meas"] >= pt["M_lowcore_meas"]
             else c2["fail"]).__iadd__ if False else None
            if pt["gamma_meas"] >= pt["M_lowcore_meas"]:
                c2["pass"] += 1
            else:
                c2["fail"] += 1
            # C3 Poisson regime
            gp = pt["gamma_poisson_pred"]
            if gp >= 4 * M_inf:
                r = pt["gamma_meas"] / gp if gp else float("inf")
                (c3.__setitem__("pass", c3["pass"] + 1) if 0.5 <= r <= 2.0
                 else c3.__setitem__("fail", c3["fail"] + 1))
            else:
                c3["vacuous"] += 1
            # C5 retention
            if pt["retention"] is not None:
                if lam <= 0.1:
                    c5lo["vals"].append((sh, q, pt["retention"]))
                    if pt["retention"] >= 0.90:
                        c5lo["pass"] += 1
                    else:
                        c5lo["fail"] += 1
                if lam >= 100:
                    c5hi["vals"].append((sh, q, pt["retention"]))
                    if pt["retention"] <= 0.10:
                        c5hi["pass"] += 1
                    else:
                        c5hi["fail"] += 1
            # corrected law
            wc = planted_w + pt["witnesses_pred"]
            gc = min(q, planted_g + pt["gamma_poisson_pred"])
            corr_w.append(pt["witnesses_meas"] / wc)
            corr_g.append(pt["gamma_meas"] / gc)
            res["corrected_law"].append(dict(
                shape=sh, q=q, lam=lam,
                wit_meas=pt["witnesses_meas"], wit_corr=wc,
                wit_ratio=pt["witnesses_meas"] / wc,
                gam_meas=pt["gamma_meas"], gam_corr=gc,
                gam_ratio=pt["gamma_meas"] / gc,
                retention=pt["retention"]))
        top = md["points"][-1]
        if top["gamma_meas"] == M_inf:
            c4["pass"] += 1
        else:
            c4["fail"] += 1
        print(f"{sh}: top-of-ladder |Gamma| = {top['gamma_meas']}, "
              f"M_inf(greedy low-core) = {M_inf}, "
              f"N_split(F={F},g={prm['g']},a={prm['a']}) = {planted_g}, "
              f"C(B,a) = {planted_w}, witnesses measured "
              f"{top['witnesses_meas']}")

    print()
    print("PRE-REGISTERED CLAIMS")
    print(f"  C1 naive witness law in [0.5,2]      : "
          f"{c1['pass']} PASS / {c1['fail']} FAIL   worst {c1['worst']}")
    print(f"  C2 |Gamma| >= planted low-core floor : "
          f"{c2['pass']} PASS / {c2['fail']} FAIL")
    print(f"  C3 Poisson |Gamma| in [0.5,2]        : "
          f"{c3['pass']} PASS / {c3['fail']} FAIL / {c3['vacuous']} vacuous")
    print(f"  C4 |Gamma| -> M_inf at top of ladder : "
          f"{c4['pass']} PASS / {c4['fail']} FAIL")
    print(f"  C5a retention >= 0.90 at lam <= 0.1  : "
          f"{c5lo['pass']} PASS / {c5lo['fail']} FAIL "
          f"(measured range "
          f"{min(v[2] for v in c5lo['vals']):.4f}"
          f"-{max(v[2] for v in c5lo['vals']):.4f})")
    print(f"  C5b retention <= 0.10 at lam >= 100  : "
          f"{c5hi['pass']} PASS / {c5hi['fail']} FAIL "
          f"(measured range "
          f"{min(v[2] for v in c5hi['vals']):.4f}"
          f"-{max(v[2] for v in c5hi['vals']):.4f})")
    print()
    print("CORRECTED LAW, ratio measured/corrected over all ladder points")
    print(f"  witnesses : {min(corr_w):.4f} - {max(corr_w):.4f}  "
          f"(n={len(corr_w)})")
    print(f"  |Gamma|   : {min(corr_g):.4f} - {max(corr_g):.4f}")

    res["claims"] = dict(C1=c1, C2=c2, C3=c3, C4=c4, C5a=c5lo, C5b=c5hi,
                         corrected_witness_ratio=[min(corr_w), max(corr_w)],
                         corrected_gamma_ratio=[min(corr_g), max(corr_g)])
    with open(OUT, "w") as fh:
        json.dump(res, fh, indent=1, sort_keys=True, default=str)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
