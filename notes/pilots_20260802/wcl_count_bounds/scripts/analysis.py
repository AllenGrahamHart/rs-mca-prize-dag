"""Consolidated analysis of the swept lattices: the minima law, how much the
AM-GM (norm) fence loses against the true first minimum, and the (h, det)
separation test that decides falsifier F3.

All statistics are exact integers / Fractions.
"""
import json, os, sys
from fractions import Fraction
from math import factorial
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lattice_core as lc

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(HERE, "results")

PI_LO = Fraction(31415926535897932384626433, 10 ** 25)
PI_HI = Fraction(31415926535897932384626434, 10 ** 25)


def gh_lambda1_sq_floor(h, det):
    """floor of the Gaussian-heuristic first minimum SQUARED,
       GH^2 = (det * (h/2)! / pi^{h/2})^{2/h},  computed by exact comparison."""
    m = h // 2
    # GH^2 = X^{1/m} with X = det * m! / pi^m
    # floor: largest integer g with g^m * pi^m <= det * m!
    lo, hi = 1, 1
    while hi ** m * PI_HI ** m <= det * factorial(m):
        hi *= 2
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** m * PI_HI ** m <= det * factorial(m):
            lo = mid
        else:
            hi = mid - 1
    return lo


def hist(xs):
    d = {}
    for x in xs:
        k = str(x)
        d[k] = d.get(k, 0) + 1
    return dict(sorted(d.items(), key=lambda kv: (len(kv[0]), kv[0])))


def analyse(rows, label, h, o, max_w):
    out = {"label": label, "h": h, "o": o, "n_rows": len(rows), "radius_sq": max_w}
    l1 = [r["lambda1_sq"] for r in rows]
    fence = [r["amgm_fence"] for r in rows]
    out["lambda1_sq_hist"] = hist(l1)
    out["amgm_fence_hist"] = hist(fence)
    out["amgm_slack_hist"] = hist([a - b for a, b in zip(l1, fence)])
    out["amgm_never_exceeds_lambda1"] = all(a >= b for a, b in zip(l1, fence))
    gh = [gh_lambda1_sq_floor(h, r["det"]) for r in rows]
    out["gh_floor_hist"] = hist(gh)
    out["lambda1_minus_gh_hist"] = hist([a - g for a, g in zip(l1, gh)])
    cen = [r for r in rows if r["min_ternary_weight"] is not None]
    out["n_census"] = len(cen)
    out["census_min_weight_hist"] = hist([r["min_ternary_weight"] for r in cen])
    out["census_lambda1_eq_minweight"] = sum(
        1 for r in cen if r["lambda1_sq"] == r["min_ternary_weight"])
    out["census_lambda1_lt_minweight"] = sum(
        1 for r in cen if r["lambda1_sq"] < r["min_ternary_weight"])
    out["minweight_ge_lambda1_always"] = all(
        r["min_ternary_weight"] >= r["lambda1_sq"] for r in cen)
    # ternary-relation counts are multiples of the free orbit 2h
    mult = []
    for r in cen:
        n = 2 * sum(r["ternary_pairs_by_weight"].values())
        mult.append(n % (2 * h) == 0)
    out["ternary_counts_multiple_of_2h"] = all(mult)
    out["n_census_checked_for_orbit"] = len(mult)

    # --- the (h, det) separation test  (falsifier F3) ---------------------
    bands = {}
    for r in rows:
        b = r["q"].bit_length()
        d = bands.setdefault(str(b), {"n": 0, "census": 0, "census_q": [], "clean_q": []})
        d["n"] += 1
        if r["min_ternary_weight"] is not None:
            d["census"] += 1
            if len(d["census_q"]) < 3:
                d["census_q"].append(r["q"])
        else:
            if len(d["clean_q"]) < 3:
                d["clean_q"].append(r["q"])
    mixed = [b for b, d in bands.items() if 0 < d["census"] < d["n"]]
    out["bit_bands"] = bands
    out["n_mixed_bands"] = len(mixed)
    out["mixed_bands"] = sorted(mixed, key=int)
    out["separation_witness"] = [
        {"bits": b, "q_with_relation": bands[b]["census_q"][0],
         "q_without_relation": bands[b]["clean_q"][0],
         "v2_with": lc.v2(bands[b]["census_q"][0] - 1),
         "v2_without": lc.v2(bands[b]["clean_q"][0] - 1)}
        for b in sorted(mixed, key=int)[:8]]
    # v_2 profile
    out["v2_hist_all"] = hist([lc.v2(r["q"] - 1) for r in rows])
    out["v2_hist_census"] = hist([lc.v2(r["q"] - 1) for r in cen])
    out["max_v2_census"] = max([lc.v2(r["q"] - 1) for r in cen], default=None)
    out["max_v2_all"] = max(lc.v2(r["q"] - 1) for r in rows)
    return out


def main():
    with open(os.path.join(RES, "census_validate.json")) as f:
        cv = json.load(f)
    out = {}
    out["A_2N32_ell1"] = analyse(cv["A_2N32_ell1"]["rows"], "2N=32, ell=1", 16, 1, 5)
    out["C_2N32_ell2"] = analyse(cv["C_2N32_ell2"]["rows"], "2N=32, ell=2", 16, 2, 8)
    out["B_2N16_ell1"] = analyse(cv["B_2N16_ell1"]["rows"], "2N=16, ell=1", 8, 1, 8)

    for k in ("A_2N32_ell1", "C_2N32_ell2", "B_2N16_ell1"):
        a = out[k]
        print("== %s  (n=%d, census=%d)" % (a["label"], a["n_rows"], a["n_census"]))
        print("   lambda1^2 hist      :", a["lambda1_sq_hist"])
        print("   AM-GM fence hist    :", a["amgm_fence_hist"])
        print("   AM-GM slack hist    :", a["amgm_slack_hist"],
              " (fence <= lambda1^2 always:", a["amgm_never_exceeds_lambda1"], ")")
        print("   lambda1^2 - GH hist :", a["lambda1_minus_gh_hist"])
        print("   census minweight    :", a["census_min_weight_hist"])
        print("   minweight >= l1^2   :", a["minweight_ge_lambda1_always"],
              "; equal in %d of %d, strict in %d"
              % (a["census_lambda1_eq_minweight"], a["n_census"],
                 a["census_lambda1_lt_minweight"]))
        print("   ternary counts mult of 2h:", a["ternary_counts_multiple_of_2h"])
        print("   mixed bit-bands     : %d of %d  -> (h,det) cannot decide"
              % (a["n_mixed_bands"], len(a["bit_bands"])))
        print("   v2 census hist      :", a["v2_hist_census"],
              " max v2 census", a["max_v2_census"], " max v2 all", a["max_v2_all"])
        print()

    with open(os.path.join(RES, "analysis.json"), "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
