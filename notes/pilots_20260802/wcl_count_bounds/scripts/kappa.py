"""The normalized first minimum kappa, and exactly how much of it each slot needs.

DEFINITION.  For a nonzero ideal I of Z[zeta_M] (M = 2h a power of two) put

    kappa(I) = lambda_1(I)^2 / N(I)^{2/h}          (scale-invariant, >= 1)

AM-GM (= the banked norm fence, LN4) is exactly the statement kappa(I) >= 1:
    N(I) <= |Norm(alpha)| <= (||alpha||^2)^{h/2}   for 0 != alpha in I.

At an official WCL row, h = 256 ell and N(I) = q^ell, so N(I)^{2/h} = q^{1/128}
INDEPENDENTLY of ell.  Slot (ell,w) is closed as soon as lambda_1^2 > w, i.e.

    kappa . q^{1/128} > w.

With q < 2^256 the strongest available q^{1/128} is 4, so the slot needs

    kappa > w/4          --  1.25 at w=5 ... 2.75 at w=11.

This file measures kappa, compares it with the Gaussian heuristic value
kappa_GH(h) = ((h/2)!)^{2/h}/pi, and tests whether kappa >= 1 is TIGHT (it is:
the banked flat weight-7 ternary polynomials generate ideals with kappa = 1
exactly, at every h).
"""
import json, os, sys
from fractions import Fraction
from math import factorial
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lattice_core as lc

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(HERE, "results")
PI_HI = Fraction(31415926535897932384626434, 10 ** 25)
PI_LO = Fraction(31415926535897932384626433, 10 ** 25)


def kappa_pow(l1sq, det, h):
    """kappa^{h/2} = (lambda_1^2)^{h/2} / N(I)   -- an exact Fraction, >= 1."""
    return Fraction(l1sq ** (h // 2), det)


def kappa_milli(l1sq, det, h):
    """floor(1000 * kappa), exactly: largest k with (k/1000)^{h/2} <= kappa^{h/2}."""
    m = h // 2
    lo, hi = 1000, 1000
    while Fraction(hi, 1000) ** m <= kappa_pow(l1sq, det, h):
        hi *= 2
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if Fraction(mid, 1000) ** m <= kappa_pow(l1sq, det, h):
            lo = mid
        else:
            hi = mid - 1
    return lo


def kappa_gh_milli(h):
    """floor(1000 * ((h/2)!)^{2/h} / pi)  -- exact, conservative (uses pi upper)."""
    m = h // 2
    lo, hi = 1, 1
    while Fraction(hi, 1000) ** m * PI_HI ** m <= factorial(m):
        hi *= 2
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if Fraction(mid, 1000) ** m * PI_HI ** m <= factorial(m):
            lo = mid
        else:
            hi = mid - 1
    return lo


def flat_ideal_test():
    """The banked AM-GM-saturating (flat) ternary polynomials generate ideals
    with kappa = 1 EXACTLY, so kappa >= 1 cannot be improved over all ideals."""
    cases = [
        (8, [1, 1, 1, -1, -1, 1, -1, 0], 7, 2401),          # 2N=16 w=7 argmax
        (16, [1, 0, 1, 0, -1, 0, 1, 0, 1, 0, 1, 0, -1, 0, 0, 0], 7, 5764801),
        (16, [1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0], 3, 6561),
        (16, [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 2, 256),
    ]
    out = []
    for (h, f, w, banked_norm) in cases:
        rows, s = [f[:]], f[:]
        for _ in range(h - 1):
            s = lc.negacyclic_shift(s)
            rows.append(s)
        det = abs(lc.det_int(rows))
        R = lc.fast_lll(rows)
        l1 = None
        b = 0
        while l1 is None and b < 30:
            b += 1
            vs = lc.enumerate_short(R, b)
            if vs:
                l1 = min(lc.sq_norm(v) for v in vs)
        out.append({
            "h": h, "weight": w, "f": f,
            "det_of_principal_ideal": det, "banked_norm": banked_norm,
            "det_matches_banked_norm": det == banked_norm,
            "flat_check_norm_eq_w_pow_h_over_2": det == w ** (h // 2),
            "lambda1_sq": l1,
            "kappa_milli": kappa_milli(l1, det, h),
            "kappa_is_exactly_1": l1 ** (h // 2) == det,
        })
    return out


def main():
    with open(os.path.join(RES, "census_validate.json")) as f:
        cv = json.load(f)
    out = {}

    for key, h, o in (("A_2N32_ell1", 16, 1), ("C_2N32_ell2", 16, 2),
                      ("B_2N16_ell1", 8, 1)):
        rows = cv[key]["rows"]
        km = [(kappa_milli(r["lambda1_sq"], r["det"], h), r["q"],
               r["min_ternary_weight"]) for r in rows]
        km.sort()
        n = len(km)
        cen = [t for t in km if t[2] is not None]
        out[key] = {
            "h": h, "o": o, "n": n,
            "kappa_gh_milli": kappa_gh_milli(h),
            "kappa_min_milli": km[0][0], "kappa_min_q": km[0][1],
            "kappa_max_milli": km[-1][0], "kappa_max_q": km[-1][1],
            "kappa_median_milli": km[n // 2][0],
            "kappa_deciles_milli": [km[(n - 1) * i // 10][0] for i in range(11)],
            "kappa_min_over_census_milli": (min(t[0] for t in cen) if cen else None),
            "kappa_lt_1100_count": sum(1 for t in km if t[0] < 1100),
            "kappa_lt_1250_count": sum(1 for t in km if t[0] < 1250),
            "kappa_ge_1_all": all(t[0] >= 1000 for t in km),
        }

    out["flat_ideals"] = flat_ideal_test()
    out["flat_kappa_one_attained"] = all(r["kappa_is_exactly_1"]
                                         for r in out["flat_ideals"])

    # what each slot needs, and what the heuristic offers
    need = {}
    for (ell, w) in [(1, 5), (1, 6), (1, 7), (1, 8), (2, 7), (2, 8), (2, 9),
                     (4, 9), (4, 10), (4, 11)]:
        h = 256 * ell
        need["(%d,%d)" % (ell, w)] = {
            "h": h,
            "kappa_needed_milli": (1000 * w + 3) // 4,   # ceil(1000 w / 4)
            "kappa_needed_exact": "%d/4" % w,
            "kappa_gh_milli": kappa_gh_milli(h),
            "gh_over_need": str(Fraction(kappa_gh_milli(h), 1000) / Fraction(w, 4)),
        }
    out["slot_kappa_requirement"] = need

    with open(os.path.join(RES, "kappa.json"), "w") as f:
        json.dump(out, f, indent=1)

    for key in ("A_2N32_ell1", "C_2N32_ell2", "B_2N16_ell1"):
        a = out[key]
        print("%s h=%d o=%d n=%d: kappa min %.3f  median %.3f  max %.3f  "
              "(GH %.3f)  #kappa<1.10: %d  #kappa<1.25: %d  kappa>=1 all: %s"
              % (key, a["h"], a["o"], a["n"], a["kappa_min_milli"] / 1000,
                 a["kappa_median_milli"] / 1000, a["kappa_max_milli"] / 1000,
                 a["kappa_gh_milli"] / 1000, a["kappa_lt_1100_count"],
                 a["kappa_lt_1250_count"], a["kappa_ge_1_all"]))
        print("    deciles:", [x / 1000 for x in a["kappa_deciles_milli"]])
    print("\nflat (AM-GM-saturating) ideals -> kappa exactly 1:",
          out["flat_kappa_one_attained"])
    for r in out["flat_ideals"]:
        print("   h=%d w=%d  N=%d  lambda1^2=%d  kappa=%.4f  norm==w^{h/2}: %s"
              % (r["h"], r["weight"], r["det_of_principal_ideal"], r["lambda1_sq"],
                 r["kappa_milli"] / 1000, r["flat_check_norm_eq_w_pow_h_over_2"]))
    print("\nslot   kappa needed   kappa_GH(h)   GH/need")
    for k, v in need.items():
        print("%-8s %6.2f        %8.2f     %s"
              % (k, v["kappa_needed_milli"] / 1000, v["kappa_gh_milli"] / 1000,
                 v["gh_over_need"]))


if __name__ == "__main__":
    main()
