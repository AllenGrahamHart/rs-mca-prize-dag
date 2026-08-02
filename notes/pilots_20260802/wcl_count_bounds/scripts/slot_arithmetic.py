"""Per-slot gap arithmetic for the ten WCL cells, all exact integers.

Slot (ell, w):  root order M = 512*ell, ring degree h = 256*ell,
o = ell simultaneous odd-index vanishings, relation lattice L = prod_u p_u
with det L = q^ell.  Official rows: q < 2^256 and v_2(q-1) >= 41.

Quantities computed (exact):

 F_unc(w)  = w^128            the unconditional norm fence  (q > F closes)
 F_con(w)  = maxnorm(16,w)^16 the C1-doubling-law fence      (q > F closes)
             (= c_w^64, since maxnorm(16,w) = c_w^4; exact even when c_w is
              irrational, e.g. c_6 = sqrt(1154) -> 1154^32)
 deficit   = the exact ratio F / 2^256 and its bit length

 |T_w|     = C(h,w) 2^w              the ternary weight-w search set
 heuristic = |T_w| / q^ell           expected number of solutions at q ~ 2^256
 orbit     = 2h = 512*ell            the free signed-shift orbit size: the count
                                     of weight-w relations is 0 or >= 2h, so a
                                     count bound < 2h already proves emptiness
 L2 gap    = sqrt(|T_w|) / 2h        shortfall of the trivial Cauchy-Schwarz
                                     character bound (see report section 5)
 Minkowski = the largest r^2 such that a ball of radius r is GUARANTEED to
             contain a nonzero point of L (existence, not exclusion)
"""
import json, os, sys
from fractions import Fraction
from math import comb, isqrt
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(HERE, "results")

OPEN_SLOTS = [(1, 5), (1, 6), (1, 7), (1, 8),
              (2, 7), (2, 8), (2, 9),
              (4, 9), (4, 10), (4, 11)]
CLOSED = {(4, 9)}          # closed by the quartic-divisor descent lineage
MAXNORM16 = {1: 1, 2: 256, 3: 6561, 4: 38416, 5: 279841, 6: 1331716,
             7: 5764801, 8: 14760962, 9: 38950081, 10: 84580802,
             11: 184497889}
# stable range of the repaired doubling law at h=16 is w <= h/2 - 1 = 7
STABLE_W = 7
# probed (not proved, not exhaustive) h=32 value at w=8, c1_norm_ladder probe
MAXNORM32_W8 = 217885999165444

CAP = 1 << 256            # official q < 2^256


def ilog2_floor(n):
    return n.bit_length() - 1


def frac_log2(n, digits=4):
    """floor(log2 n) plus an exact rational refinement: returns (floor, num, den)
    with log2(n) in [floor + num/den, floor + (num+1)/den]. No floats."""
    e = ilog2_floor(n)
    # binary search the fractional part by comparing n^den vs 2^(e*den + num)
    den = 1 << digits
    lo, hi = 0, den
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if n ** den >= (1 << (e * den + mid)):
            lo = mid
        else:
            hi = mid - 1
    return e, lo, den


def isqrt_frac(n):
    return isqrt(n)


def minkowski_radius_sq(h, det):
    """Largest integer r2 with vol(Ball(sqrt(r2))) <= 2^h det  (so r2+1 is a
    GUARANTEED nonzero-point radius squared).  Exact rational bound on pi.

    vol = pi^{h/2} r^h / (h/2)!   for even h.
    Condition: pi^{h/2} r2^{h/2} > 2^h det (h/2)!   ->  point exists.
    Uses a strict lower rational bound for pi to stay conservative in the
    direction that makes the EXISTENCE claim rigorous.
    """
    assert h % 2 == 0
    m = h // 2
    PI_LO = Fraction(31415926535897932384626433, 10 ** 25)   # < pi
    from math import factorial
    need = (1 << h) * det * factorial(m)
    # smallest r2 with PI_LO^m * r2^m > need
    lo, hi = 1, 1
    while (PI_LO ** m) * hi ** m <= need:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if (PI_LO ** m) * mid ** m > need:
            hi = mid
        else:
            lo = mid + 1
    return lo


def main():
    out = {"cap_bits": 256, "note": "official q < 2^256, v_2(q-1) >= 41"}
    rows = []
    for (ell, w) in OPEN_SLOTS:
        h = 256 * ell
        o = ell
        M = 512 * ell
        F_unc = w ** 128
        stable = (w <= STABLE_W)
        if w <= STABLE_W:
            F_con = MAXNORM16[w] ** 16
            con_src = "maxnorm(16,%d)^16 = c_%d^64 (stable doubling range w<=7)" % (w, w)
        elif w == 8:
            F_con = MAXNORM32_W8 ** 8          # = c_8^64 from the h=32 probe
            con_src = "maxnorm(32,8)^8 from the c1 hill-climb PROBE (not proved)"
        else:
            F_con = MAXNORM16[w] ** 16
            con_src = ("maxnorm(16,%d)^16 -- OUTSIDE the stable range (w >= h/2 at "
                       "h=16); extrapolation only" % w)
        T = comb(h, w) * (2 ** w)
        orbit = 2 * h
        e_unc = frac_log2(F_unc)
        e_con = frac_log2(F_con)
        e_T = frac_log2(T)
        # heuristic solution count at q = 2^256 - eps  ->  T / 2^{256 ell}
        heur_bits = e_T[0] + Fraction(e_T[1], e_T[2]) - 256 * ell
        # trivial Cauchy-Schwarz character error term sqrt(T) vs the orbit floor
        sqrtT = isqrt(T)
        l2_gap = Fraction(sqrtT, orbit)
        mink = minkowski_radius_sq(h, CAP ** ell)   # det = q^ell at the top of the range
        # AM-GM fence value at q = 2^256 (the strongest official case)
        # lambda_1^2 >= q^{2 ell / h} = q^{1/128}; at q = 2^256 that is exactly 4
        rows.append({
            "slot": [ell, w], "M": M, "h": h, "o": o,
            "closed": (ell, w) in CLOSED,
            "F_unconditional": str(F_unc),
            "F_unc_bits": F_unc.bit_length(),
            "F_unc_log2_floor_frac": [e_unc[0], e_unc[1], e_unc[2]],
            "unc_deficit_bits_over_cap": e_unc[0] - 256,
            "unc_reachable": F_unc < CAP,
            "F_conditional": str(F_con),
            "F_con_bits": F_con.bit_length(),
            "F_con_log2_floor_frac": [e_con[0], e_con[1], e_con[2]],
            "con_deficit_bits_over_cap": e_con[0] - 256,
            "con_reachable": F_con < CAP,
            "con_source": con_src,
            "con_stable": stable,
            "ternary_set_size": str(T),
            "ternary_set_log2": [e_T[0], e_T[1], e_T[2]],
            "orbit_size_2h": orbit,
            "heuristic_count_log2": str(heur_bits),
            "heuristic_margin_bits": str(-heur_bits),
            "heuristic_margin_bits_floor": int(-heur_bits),
            "sqrt_T": str(sqrtT),
            "L2_shortfall_ratio": str(l2_gap),
            "L2_shortfall_bits": frac_log2(max(sqrtT // orbit, 1))[0],
            "minkowski_guaranteed_r2_at_2p256": mink,
            "amgm_lambda1sq_lower_bound_at_2p256": 4,
        })
    out["slots"] = rows

    # --- the uniform official invariants -------------------------------------
    out["uniform"] = {
        "det_root_h": "q^{1/256} for every slot (det=q^ell, h=256 ell) -- < 2 for q < 2^256",
        "amgm_fence": "lambda_1^2 >= q^{1/128} < 4 for q < 2^256; = 4 iff q > 3^128",
        "3pow128_bits": (3 ** 128).bit_length(),
        "4pow128_eq_2pow256": 4 ** 128 == 1 << 256,
        "cheapest_open_slot_unc_deficit_bits": min(
            r["unc_deficit_bits_over_cap"] for r in rows if not r["closed"]),
        "cheapest_open_slot_con_deficit_bits": min(
            r["con_deficit_bits_over_cap"] for r in rows if not r["closed"]),
    }
    with open(os.path.join(RES, "slot_arithmetic.json"), "w") as f:
        json.dump(out, f, indent=1)

    hdr = ("slot   h    F_unc bits  gap  |  F_con bits  gap  | |T_w| log2 | "
           "heur margin | 2h  | L2 gap bits | Mink r^2")
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        e = r["ternary_set_log2"]
        print("(%d,%2d)%s %4d  %6d %5d  |  %6d %5d  |  %6.2f    | %9d  | %4d| %6d      | %d"
              % (r["slot"][0], r["slot"][1], "*" if r["closed"] else " ", r["h"],
                 r["F_unc_bits"], r["unc_deficit_bits_over_cap"],
                 r["F_con_bits"], r["con_deficit_bits_over_cap"],
                 e[0] + e[1] / e[2],
                 r["heuristic_margin_bits_floor"], r["orbit_size_2h"],
                 r["L2_shortfall_bits"], r["minkowski_guaranteed_r2_at_2p256"]))
    print("\n* = already closed (4,9). gap = floor(log2 F) - 256 (bits by which the")
    print("fence overshoots the official cap; > 0 means unreachable).")


if __name__ == "__main__":
    main()
