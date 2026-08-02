"""(a) How tight is the lattice relaxation?   lambda_1^2 > w  =>  slot empty.
    The converse can fail (the shortest vector need not be ternary).  Measure
    the false-positive rate  #{lambda_1^2 <= w} - #{min ternary weight <= w}.

(b) The kappa requirement across the WHOLE official q range, not only its top.
    A slot statement is universally quantified over official q, and the
    SMALLEST official prime is the hardest case:
        q_min = 3*2^41 + 1 = 6597069766657      (banked in
        dli_wcl_weight5_first64_mitm_exclusion, the k=3 row)
    Requirement:  kappa >= w / q^{1/128}, worst at q = q_min.
"""
import json, os, sys
from fractions import Fraction
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lattice_core as lc

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(HERE, "results")

Q_MIN = 3 * (1 << 41) + 1
Q_MAX = 1 << 256
OPEN = [(1, 5), (1, 6), (1, 7), (1, 8), (2, 7), (2, 8), (2, 9),
        (4, 10), (4, 11)]


def kappa_needed_milli(w, q):
    """ceil(1000 * w / q^{1/128}) : smallest k/1000 with (k/1000)^128 * q >= w^128"""
    lo, hi = 1, 1
    while Fraction(hi, 1000) ** 128 * q < w ** 128:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if Fraction(mid, 1000) ** 128 * q >= w ** 128:
            hi = mid
        else:
            lo = mid + 1
    return lo


def main():
    with open(os.path.join(RES, "census_validate.json")) as f:
        cv = json.load(f)
    out = {}

    # ---- (a) tightness ---------------------------------------------------
    tight = {}
    for key, radius in (("A_2N32_ell1", 5), ("C_2N32_ell2", 8), ("B_2N16_ell1", 8)):
        rows = cv[key]["rows"]
        t = []
        for w in range(2, radius + 1):
            lat = sum(1 for r in rows if r["lambda1_sq"] <= w)
            cen = sum(1 for r in rows if r["min_ternary_weight"] is not None
                      and r["min_ternary_weight"] <= w)
            t.append({"w": w, "n_lambda1sq_le_w": lat, "n_true_census_le_w": cen,
                      "false_positives": lat - cen,
                      "false_positive_rate_num": lat - cen, "n_rows": len(rows)})
        tight[key] = {"radius": radius, "table": t}
    out["tightness"] = tight

    # ---- (b) kappa requirement over the whole official range -------------
    q_min_ok = lc.is_prime(Q_MIN) and lc.v2(Q_MIN - 1) >= 41
    req = []
    for (ell, w) in OPEN:
        req.append({
            "slot": [ell, w], "h": 256 * ell,
            "kappa_needed_at_qmin_milli": kappa_needed_milli(w, Q_MIN),
            "kappa_needed_at_qmax_milli": kappa_needed_milli(w, Q_MAX),
            "fence_deficit_bits_vs_qmin": (w ** 128).bit_length() - Q_MIN.bit_length(),
            "fence_deficit_bits_vs_qmax": (w ** 128).bit_length() - 257,
        })
    out["q_min"] = str(Q_MIN)
    out["q_min_bits"] = Q_MIN.bit_length()
    out["q_min_is_prime_and_official"] = q_min_ok
    out["kappa_requirements"] = req
    out["v2_blind_cap_from_engineered_witness_milli"] = 1507
    out["all_open_slots_beyond_cap_over_full_range"] = all(
        r["kappa_needed_at_qmin_milli"] > 1507 for r in req)

    with open(os.path.join(RES, "tightness_and_range.json"), "w") as f:
        json.dump(out, f, indent=1)

    print("(a) TIGHTNESS of the lattice relaxation  (lambda_1^2 > w => empty)")
    for k, v in tight.items():
        print("  %s" % k)
        for r in v["table"]:
            print("     w=%2d : lambda_1^2<=w in %5d rows, true census %5d, "
                  "false positives %5d  (of %d)"
                  % (r["w"], r["n_lambda1sq_le_w"], r["n_true_census_le_w"],
                     r["false_positives"], r["n_rows"]))
    print("\n(b) kappa REQUIRED over the official range   "
          "q_min = %d (%d bits, prime & v2>=41: %s)"
          % (Q_MIN, Q_MIN.bit_length(), q_min_ok))
    print("slot    kappa@q_min  kappa@2^256   fence deficit vs q_min (bits)  vs 2^256")
    for r in req:
        print("(%d,%2d)   %7.3f      %7.3f            %6d                     %4d"
              % (r["slot"][0], r["slot"][1],
                 r["kappa_needed_at_qmin_milli"] / 1000,
                 r["kappa_needed_at_qmax_milli"] / 1000,
                 r["fence_deficit_bits_vs_qmin"], r["fence_deficit_bits_vs_qmax"]))
    print("\nengineered-witness cap on any v_2-blind kappa bound at h=256: 1.507")
    print("every open slot needs more than that over the full range:",
          out["all_open_slots_beyond_cap_over_full_range"])


if __name__ == "__main__":
    main()
