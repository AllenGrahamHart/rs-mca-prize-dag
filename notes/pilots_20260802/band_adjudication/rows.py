"""rows.py -- exact six-row arithmetic for the band/cascade adjudication.

Sections
  1. row pins, recomputed from scratch and cross-checked against the banked
     xr_graded_band_ledger/band_arith.json;
  2. the 2-adic census of structured (coset-union) depths;
  3. the MC population at d = h-1, exact integers, and what it costs;
  4. pricing of the two adjudication outcomes;
  5. the B_tan re-baseline trip test.

All integer arithmetic exact; log2 only for display.
"""

import json
import os
import sys
from math import comb, gcd, log2

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)

# ---------------------------------------------------------------- 1. rows
# n, k from the banked dag pins; A = k + n/scale + 1, h = A - k.
ROWS = [
    ("RowC 1/4", 1024, 256, 256),
    ("RowC 1/8", 1024, 128, 256),
    ("RowC 1/16", 1024, 64, 512),
    ("prize 1/4", 2199023255552, 549755813888, 256),
    ("prize 1/8", 2199023255552, 274877906944, 256),
    ("prize 1/16", 2199023255552, 137438953472, 512),
]

BANKED = json.load(open(os.path.join(
    HERE, os.pardir, "xr_graded_band_ledger", "band_arith.json")))

res = {"rows": [], "checks": 0, "fails": []}


def chk(cond, label, extra=None):
    res["checks"] += 1
    if not cond:
        res["fails"].append({"label": label, "extra": str(extra)})
        print("   FAIL", label, extra)
    return cond


def L(d, n, k, h):
    return (n - k - d) // (h - d)


def sumL(n, k, h, dmax):
    """sum_{d=1}^{dmax} floor((R-d)/(h-d)).

    Substituting e = h-d gives floor((R-h+e)/e) = floor(C/e) + 1 with
    C = R-h, so the sum is (#terms) + sum_{e=e0}^{h-1} floor(C/e), which is
    evaluated by exact divisor blocks.
    """
    R = n - k
    C = R - h
    e0, e1 = h - dmax, h - 1
    tot = e1 - e0 + 1
    e = e0
    while e <= e1:
        q = C // e
        hi = e1 if q == 0 else min(e1, C // q)
        tot += q * (hi - e + 1)
        e = hi + 1
    return tot


def v2(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


def ceil_pow2(x):
    p = 1
    while p < x:
        p *= 2
    return p


print("=== 1. row pins (recomputed; banked values cross-checked) ===")
for name, n, k, scale in ROWS:
    h = n // scale + 1
    A = k + h
    R = n - k
    n3 = n ** 3
    b = next(r for r in BANKED["rows"] if r["name"] == name)
    chk(b["h"] == h and b["A"] == A and b["R"] == R, "row pin", name)
    s_lo = int(b["Bstar"]) - int(b["B_quot_ub"]) if "B_quot_ub" in b else int(b["s_lo"])
    s_lo = int(b["s_lo"])
    headroom = s_lo - 16 * n3
    chk(headroom == int(b["headroom"]), "headroom", name)
    sl_band = sumL(n, k, h, h - 2)
    sl_ext = sumL(n, k, h, h - 1)
    chk(sl_band == b["sumL"], "sumL over [1,h-2] matches banked",
        (name, sl_band, b["sumL"]))
    chk(sl_ext == sl_band + L(h - 1, n, k, h), "extension adds exactly L(h-1)",
        name)
    chk(L(h - 1, n, k, h) == n - A + 1, "L(h-1) = n-A+1", name)
    e = {"name": name, "n": n, "k": k, "scale": scale, "h": h, "A": A, "R": R,
         "n_minus_A_plus_1": n - A + 1, "n2": n * n, "n3": n3,
         "s_lo": str(s_lo), "headroom_13n3": str(headroom),
         "headroom_over_n3": headroom / float(n3),
         "sumL_band_1_to_hminus2": sl_band,
         "sumL_ext_1_to_hminus1": sl_ext,
         "L_hminus1": L(h - 1, n, k, h)}
    # required uniform N_d
    e["req_Nd_band_over_n2"] = headroom / float(sl_band) / (n * n)
    e["req_Nd_ext_over_n2"] = headroom / float(sl_ext) / (n * n)
    e["req_N_hminus1_alone_over_n2"] = headroom / float(n - A + 1) / (n * n)
    res["rows"].append(e)
    print("%-11s n=2^%-5.2f k=2^%-5.2f h=%-11d A=%-13d n-A+1=%-13d "
          "sumL[1,h-2]=%-15d L(h-1)=%-13d headroom=%.3f n^3"
          % (name, log2(n), log2(k), h, A, n - A + 1, sl_band,
             L(h - 1, n, k, h), headroom / float(n3)))

print()
print("=== 2. 2-adic census of STRUCTURED (coset-union) depths ===")
print("    admissible d  <=>  M := 2^ceil(log2 d) divides n and n-k-d")
print("    (MC-3 window conditions + MC-4 structured-floor completeness)")
for e in res["rows"]:
    n, k, h, A = e["n"], e["k"], e["h"], e["A"]
    # M := 2^ceil(log2 d) satisfies M >= d, so M | n and M | (n-k-d) with
    # M | n, M | k (both 2-powers, M <= k) force M | d, hence M = d and d is
    # a power of two.  Enumerating powers of two is therefore EXHAUSTIVE;
    # the loop below re-tests the raw condition on every power of two AND on
    # a dense sample of non-powers to certify the reduction.
    adm = []
    p = 1
    while p <= h:
        M = ceil_pow2(p)
        if n % M == 0 and (n - k - p) % M == 0 and p <= M:
            adm.append(p)
        p *= 2
    sample = set()
    lim = min(h, 4000)
    sample |= set(range(1, lim + 1))
    for c in (h, h - 1, h - 2, h - 3, -(-h // 2), -(-h // 2) + 1, h // 2,
              h // 2 + 1, h - 5, 3 * h // 4):
        for dd in (c - 2, c - 1, c, c + 1, c + 2):
            if 1 <= dd <= h:
                sample.add(dd)
    extra = []
    for d in sorted(sample):
        M = ceil_pow2(d)
        if n % M == 0 and (n - k - d) % M == 0 and d <= M:
            if d & (d - 1) != 0:
                extra.append(d)
    chk(extra == [], "sampled non-powers-of-two are never structured",
        (e["name"], extra[:5]))
    hi = [d for d in adm if d >= -(-h // 2)]
    band = [d for d in adm if -(-h // 2) <= d <= h - 2]
    lo = [d for d in adm if d < -(-h // 2)]
    e["structured_depths_all"] = adm if len(adm) < 60 else \
        {"count": len(adm), "min": adm[0], "max": adm[-1],
         "all_powers_of_two": all(d & (d - 1) == 0 for d in adm)}
    e["structured_in_upper_window"] = hi
    e["structured_in_band_proper_upper"] = band
    e["structured_in_low_band_count"] = len(lo)
    # excess h (a live ray directly) -- structured?
    Mh = ceil_pow2(h)
    e["structured_at_excess_h"] = (n % Mh == 0 and (n - k - h) % Mh == 0
                                   and h <= Mh)
    chk(all(d & (d - 1) == 0 for d in adm),
        "every structured depth is a power of two", (e["name"], adm[:8]))
    chk(hi == [h - 1], "h-1 is the unique structured depth in [ceil(h/2),h]",
        (e["name"], hi))
    chk(band == [], "NO structured depth in the band proper [ceil(h/2),h-2]",
        (e["name"], band))
    chk(not e["structured_at_excess_h"],
        "no structured solution at excess h (no structured live ray)",
        e["name"])
    print("%-11s ceil(h/2)=%-11d structured depths: %s | in [ceil(h/2),h]: %s"
          " | in band proper [ceil(h/2),h-2]: %s | at excess h: %s"
          % (e["name"], -(-h // 2),
             (str(adm) if len(adm) < 12 else
              "%d powers of two, 1..%d" % (len(adm), adm[-1])),
             hi, band if band else "NONE", e["structured_at_excess_h"]))

print()
print("=== 3. the MC family at d = h-1: exact population and exact cost ===")
for e in res["rows"]:
    n, k, h, A = e["n"], e["k"], e["h"], e["A"]
    w = M = h - 1
    rp = n - k - w
    ok = (n % M == 0 and rp % M == 0 and w <= M)
    e["mc_admissible"] = ok
    if not ok:
        print("%-11s MC at w=h-1 NOT admissible" % e["name"])
        continue
    N, m = n // M, rp // M
    cnt = comb(N, m) // N if gcd(m, N) == 1 else None
    e.update({"mc_w": w, "mc_N": N, "mc_m": m, "mc_gcd": gcd(m, N),
              "mc_count_bits": None if cnt is None else cnt.bit_length(),
              "mc_count_log2": None if cnt is None else log2(cnt)})
    # what the LEDGER actually pays for this received pair
    e["mc_gamma"] = n                    # union of the family = all of H
    e["mc_gamma_over_slot"] = n / float(n - A + 1)
    e["mc_N_hminus1_ceiling_selected"] = n // 2
    e["mc_N_hminus1_typical"] = n // (n - A + 1) + 1
    e["mc_column_cost_slopes"] = n       # |Gamma_band| for this pair
    e["mc_refutation_margin_bits"] = (
        log2(cnt) - log2(e["req_N_hminus1_alone_over_n2"] * n * n)
        if cnt else None)
    e["mc_selected_margin_bits"] = (
        log2(n // 2) - log2(e["req_N_hminus1_alone_over_n2"] * n * n))
    print("%-11s w=M=%-11d N=%-6d m=%-6d MC=2^%-7.2f | required N_{h-1} "
          "<= %.3f n^2 = 2^%.2f | RAW-PAIR margin %+.1f bits ; "
          "SELECTED ceiling n/2 = 2^%.2f margin %+.1f bits"
          % (e["name"], w, N, m, log2(cnt),
             e["req_N_hminus1_alone_over_n2"],
             log2(e["req_N_hminus1_alone_over_n2"] * n * n),
             e["mc_refutation_margin_bits"], log2(n // 2),
             e["mc_selected_margin_bits"]))

print()
print("=== 4. pricing the two adjudication outcomes ===")
print("  (i)  d = h-1 = CASCADE TIER   -> band column pays [1,h-2];")
print("       the cascade tier needs its own charge of |Gamma_casc|")
print("  (ii) d = h-1 = BAND           -> band column pays [1,h-1]")
for e in res["rows"]:
    n, k, h, A = e["n"], e["k"], e["h"], e["A"]
    head = int(e["headroom_13n3"])
    slb, sle = e["sumL_band_1_to_hminus2"], e["sumL_ext_1_to_hminus1"]
    e["outcome_i_band_column_at_Nd_1"] = slb
    e["outcome_ii_band_column_at_Nd_1"] = sle
    e["outcome_i_extra_term_one_cascade_pair"] = n - A + 1
    e["cost_delta_ii_minus_i_at_Nd_1"] = sle - slb
    e["frac_of_column_that_is_the_cascade_tier"] = (sle - slb) / float(sle)
    print("%-11s (i) column@N=1 = %-15d  (ii) = %-15d  delta = %-13d "
          "(%.4f%% of the extended column) | req N_d: (i) %.4f n^2  "
          "(ii) %.4f n^2  (ratio %.6f)"
          % (e["name"], slb, sle, sle - slb,
             100.0 * e["frac_of_column_that_is_the_cascade_tier"],
             e["req_Nd_band_over_n2"], e["req_Nd_ext_over_n2"],
             e["req_Nd_ext_over_n2"] / e["req_Nd_band_over_n2"]))

print()
print("=== 5. B_tan re-baseline trip test ===")
print("  strip item 4:  B_quot_ub(A) + (n-A+1) + 16 n^3 <= B*")
print("  a re-baselined B_tan = (n-A+1) + X n^3 needs X <= floor(s_lo/n^3)-16")
for e in res["rows"]:
    n = e["n"]
    n3 = e["n3"]
    s_lo = int(e["s_lo"])
    max_extra = (s_lo - 16 * n3) // n3
    e["max_B_tan_enlargement_over_n3"] = max_extra
    e["retuning_headroom_bits_now"] = log2((s_lo // n3) / 16.0)
    e["retuning_headroom_bits_after_13n3"] = log2((s_lo // n3) / 29.0) \
        if s_lo // n3 >= 29 else None
    aft = e["retuning_headroom_bits_after_13n3"]
    print("%-11s floor(s_lo/n^3) = %-6d  max B_tan enlargement = %d n^3  "
          "| retuning headroom now = %.4f bits, after a 13 n^3 re-baseline "
          "= %s bits"
          % (e["name"], s_lo // n3, max_extra,
             e["retuning_headroom_bits_now"],
             ("%.4f" % aft) if aft is not None else "n/a"))

print()
print("=== 6. is the MC pair QUOTIENT-PERIODIC (T3/P3) at scale M = h-1? ===")
print("  P3 needs M > 1 with M | gcd(n,k) and the pencil folding "
      "through x -> x^M")
for e in res["rows"]:
    n, k, h, A, scale = e["n"], e["k"], e["h"], e["A"], e["scale"]
    M = h - 1
    g = gcd(n, k)
    e["P3_M"] = M
    e["gcd_n_k"] = g
    e["P3_M_gt_1"] = M > 1
    e["P3_M_divides_gcd_nk"] = (g % M == 0)
    e["P3_fires"] = (M > 1 and g % M == 0)
    chk(e["P3_fires"], "P3 admissibility M | gcd(n,k), M > 1",
        (e["name"], M, g))
    # the quotient row that the paid mass descends to (Q_M = Q_1, rate-preserved)
    nq, kq = n // M, k // M
    hq = nq // scale + 1 if nq % scale == 0 else None
    e["quotient_row"] = {"n": nq, "k": kq, "h": hq,
                         "band_proper_empty": (hq is not None and hq - 2 < 1)}
    # overflow of the printed B_tan slot by this single received pair
    e["MC_gamma_over_B_tan_slot"] = n / float(n - A + 1)
    print("%-11s M=h-1=%-11d gcd(n,k)=%-13d M|gcd: %-5s  P3 FIRES: %-5s | "
          "quotient row (n',k')=(%d,%d) h'=%s band proper %s | "
          "|Gamma|=n overflows n-A+1 by x%.4f"
          % (e["name"], M, g, e["P3_M_divides_gcd_nk"], e["P3_fires"],
             nq, kq, hq, "EMPTY" if e["quotient_row"]["band_proper_empty"]
             else "nonempty", e["MC_gamma_over_B_tan_slot"]))

res["verdict"] = "PASS" if not res["fails"] else "FAIL"
with open(os.path.join(CHK, "rows.json"), "w") as f:
    json.dump(res, f, indent=1)
print("\nchecks=%d fails=%d -> %s" % (res["checks"], len(res["fails"]),
                                      res["verdict"]))
