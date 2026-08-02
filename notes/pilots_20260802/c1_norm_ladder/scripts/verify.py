#!/usr/bin/env python3
"""Third independent code path: sympy.resultant(f(x), x^N+1) on every claimed
argmax and on a sample of census witnesses.  Nothing here shares code with the
field-norm descent or with the Bareiss determinant.
"""

from __future__ import annotations

import argparse
import json
import random

from sympy import Poly, Symbol, resultant

x = Symbol("x")


def res(d):
    N = len(d)
    f = Poly(sum(int(c) * x ** i for i, c in enumerate(d)), x)
    return int(resultant(f, Poly(x ** N + 1, x)))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--sample", type=int, default=60)
    args = ap.parse_args()
    R = args.root
    lad = json.load(open(R + "/ladder.json"))
    rep = {"argmax_checks": [], "witness_checks": []}
    bad = 0

    for twoN, tab in lad["argmax"].items():
        for w, f in tab.items():
            if f is None:
                continue
            claimed = int(lad["ladder"][twoN][w])
            got = res(f)
            ok = got == claimed
            bad += (not ok)
            rep["argmax_checks"].append(
                {"twoN": int(twoN), "w": int(w), "claimed": str(claimed),
                 "sympy_resultant": str(got), "ok": ok, "f": f})

    for cert in json.load(open(R + "/probe_2N64_w8.json"))["sandwich_certificates_2N64"]:
        got = res(cert["witness_f"])
        ok = str(got) == cert["Norm_f"]
        bad += (not ok)
        rep["argmax_checks"].append(
            {"twoN": 64, "w": cert["w"], "claimed": cert["Norm_f"],
             "sympy_resultant": str(got), "ok": ok, "source": "sandwich certificate"})

    rng = random.Random(31337)
    for name in ("table_2N16.json", "census_2N32.json", "census_2N64_w1to6.json"):
        blob = json.load(open(R + "/" + name))
        cens = blob["census"]
        pick = cens if len(cens) <= args.sample else rng.sample(cens, args.sample)
        for r in pick:
            f = r["witness_f"]
            got = res(f)
            claimed = int(r["Norm_f"] if "Norm_f" in r else r["witness_norm"])
            ok = got == claimed and got % r["q"] == 0
            bad += (not ok)
            rep["witness_checks"].append(
                {"file": name, "q": r["q"], "min_weight": r["min_weight"],
                 "claimed_norm": str(claimed), "sympy_resultant": str(got),
                 "q_divides": got % r["q"] == 0, "ok": ok})

    rep["n_argmax_checked"] = len(rep["argmax_checks"])
    rep["n_witness_checked"] = len(rep["witness_checks"])
    rep["failures"] = bad
    with open(args.out, "w") as fh:
        json.dump(rep, fh, indent=1)
    print(json.dumps({k: v for k, v in rep.items()
                      if k not in ("argmax_checks", "witness_checks")}))
    if bad:
        for c in rep["argmax_checks"] + rep["witness_checks"]:
            if not c["ok"]:
                print("FAIL", json.dumps(c))
    else:
        print("ALL SYMPY RESULTANT CHECKS PASS")


if __name__ == "__main__":
    main()
