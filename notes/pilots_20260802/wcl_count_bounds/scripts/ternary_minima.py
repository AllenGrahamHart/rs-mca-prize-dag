"""Is the FIRST MINIMUM of the relation lattice attained by a ternary vector?

If yes, the ternary (reduced signed) restriction costs nothing: the WCL slot
question "is there a ternary weight-w relation" coincides with the pure lattice
question "is lambda_1^2 <= w", i.e. with ideal-SVP.  The census rows already
answer yes wherever lambda_1^2 <= radius; this script tests the NON-census rows,
where lambda_1^2 exceeds the census radius and ternariness was never checked.
"""
import json, os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lattice_core as lc

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(HERE, "results")


def scan(rows, M, U, sample, label):
    idx = list(range(len(rows)))
    step = max(1, len(idx) // sample)
    sel = idx[::step][:sample]
    out = []
    for i in sel:
        r = rows[i]
        q = r["q"]
        B, om = lc.relation_lattice_basis(q, M, U)
        R = lc.fast_lll(B)
        assert lc.certify_basis(R, q, M, U, om)
        l1 = r["lambda1_sq"]
        mins = [v for v in lc.enumerate_short(R, l1) if lc.sq_norm(v) == l1]
        assert mins, (q, l1)
        tern = [v for v in mins if lc.is_ternary(v)]
        out.append({"q": q, "lambda1_sq": l1, "n_minimal_pairs": len(mins),
                    "n_ternary_minimal_pairs": len(tern),
                    "minimum_is_ternary": len(tern) > 0,
                    "all_minimal_ternary": len(tern) == len(mins),
                    "was_census": r["min_ternary_weight"] is not None})
    n = len(out)
    res = {"label": label, "n_sampled": n,
           "n_minimum_is_ternary": sum(1 for r in out if r["minimum_is_ternary"]),
           "n_all_minimal_ternary": sum(1 for r in out if r["all_minimal_ternary"]),
           "n_census_in_sample": sum(1 for r in out if r["was_census"]),
           "non_census_minimum_is_ternary": sum(
               1 for r in out if r["minimum_is_ternary"] and not r["was_census"]),
           "non_census_sampled": sum(1 for r in out if not r["was_census"]),
           "lambda1_hist_of_failures": {},
           "rows": out}
    for r in out:
        if not r["minimum_is_ternary"]:
            k = str(r["lambda1_sq"])
            res["lambda1_hist_of_failures"][k] = \
                res["lambda1_hist_of_failures"].get(k, 0) + 1
    return res


def main():
    with open(os.path.join(RES, "census_validate.json")) as f:
        cv = json.load(f)
    out = {}
    out["A_2N32_ell1"] = scan(cv["A_2N32_ell1"]["rows"], 32, (1,), 320,
                              "2N=32 ell=1 (sampled)")
    out["C_2N32_ell2"] = scan(cv["C_2N32_ell2"]["rows"], 32, (1, 3), 32,
                              "2N=32 ell=2 (all)")
    out["B_2N16_ell1"] = scan(cv["B_2N16_ell1"]["rows"], 16, (1,), 39,
                              "2N=16 ell=1 (all)")
    with open(os.path.join(RES, "ternary_minima.json"), "w") as f:
        json.dump(out, f, indent=1)
    for k, a in out.items():
        print("%-14s sampled %4d : minimum is ternary in %d  (all minimal vectors "
              "ternary in %d);  non-census %d/%d ; failures by lambda1^2: %s"
              % (k, a["n_sampled"], a["n_minimum_is_ternary"],
                 a["n_all_minimal_ternary"], a["non_census_minimum_is_ternary"],
                 a["non_census_sampled"], a["lambda1_hist_of_failures"]))


if __name__ == "__main__":
    main()
