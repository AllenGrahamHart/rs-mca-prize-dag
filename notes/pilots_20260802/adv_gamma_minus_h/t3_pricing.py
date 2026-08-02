"""t3_pricing.py -- exact six-row pricing of the attack's outcome.

Three questions, priced:

 1. WHERE does the confinement come from?  THEOREM Y makes it a PRODUCT-
    COSET fact at j = 1 (no q-threshold at all).  For j >= 2 it is a
    COUNTING fact, governed by

        X(n,k,w,q) := C(n,A) / q^w ,   A = k+w+1, w = h-1,

    the same index that governs the existence of ANY non-structured
    exact-A codeword.  Sanity check to be verified here: log2(C(n,A))/w
    must reproduce the list-bound pilot's published "minimum log2 q for
    gate-admissibility" (209.26 / 141.93 / 176.58) -- i.e. the caveat-1
    threshold and the caveat-2 threshold are the SAME NUMBER.

 2. HOW MUCH ROOM is there at the official rows?  log2 X at the banked
    q >= 2^250 pin and at the 2^256 cap.

 3. WHAT WOULD BREAK if the confinement failed?  Price
    N_{h-1} <= |Gamma|/2 for |Gamma| = n (proved), |Gamma| = q+1 (total
    failure) against the tier requirement, and |Gamma_casc| against 13n^3.

All row pins are read from the banked band_arith.json; nothing is
recomputed by hand.  Binomial logs use the entropy formula with the
standard Stirling correction, whose error is < 25 bits against totals of
~10^12 bits (stated, not hidden).
"""

import json
import os
import sys
from decimal import Decimal, getcontext
from math import comb, log2

sys.dont_write_bytecode = True
getcontext().prec = 60
HERE = os.path.dirname(os.path.abspath(__file__))
CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)

BANKED = json.load(open(os.path.join(
    HERE, os.pardir, "xr_graded_band_ledger", "band_arith.json")))
LN2 = Decimal(2).ln()

out = {"doc": __doc__, "rows": [], "checks": 0, "fails": [], "law": {}}


def chk(cond, label, extra=None):
    out["checks"] += 1
    if not cond:
        out["fails"].append({"label": label, "extra": str(extra)})
        print("    FAIL", label, extra)
    return cond


def log2binom(n, a):
    """log2 C(n,a) via the entropy formula (exact for small n)."""
    if n <= 4000:
        return float(Decimal(comb(n, a)).ln() / LN2)
    N, A = Decimal(n), Decimal(a)
    B = N - A
    ent = (N * N.ln() - A * A.ln() - B * B.ln()) / LN2
    corr = (Decimal(2) * Decimal(3.141592653589793) * N * A * B / (N * N)).ln()
    return float(ent - corr / (2 * LN2))


PUBLISHED_GATE_THRESHOLD = {"prize 1/4": 209.26, "prize 1/8": 141.93,
                            "prize 1/16": 176.58}

print("=== 1. the criticality threshold, row by row ===")
print("    A = k+h ; w = M = h-1 ; X = C(n,A)/q^w ; q_crit = "
      "2^(log2 C(n,A) / w)")
for b in BANKED["rows"]:
    n, k, A, h = int(b["n"]), int(b["k"]), int(b["A"]), int(b["h"])
    w = h - 1
    lb = log2binom(n, A)
    qcrit = lb / w
    e = {"name": b["name"], "n": n, "k": k, "h": h, "A": A, "w": w,
         "log2_C_n_A": lb, "log2_q_critical": qcrit,
         "log2X_at_q_2^250": lb - 250.0 * w,
         "log2X_at_q_2^256": lb - 256.0 * w,
         "log2X_at_q_crit": 0.0}
    if b["name"] in PUBLISHED_GATE_THRESHOLD:
        pub = PUBLISHED_GATE_THRESHOLD[b["name"]]
        e["published_gate_threshold"] = pub
        chk(abs(qcrit - pub) < 0.5,
            "caveat-1 threshold == published caveat-2 gate threshold",
            (b["name"], qcrit, pub))
    out["rows"].append(e)
    print("  %-11s n=2^%-6.2f A=2^%-8.3f w=2^%-6.2f | log2 C(n,A)=%.6g  "
          "log2 q_crit=%.2f%s | log2 X at q=2^250: %+.4g"
          % (b["name"], log2(n), log2(A), log2(w), lb, qcrit,
             ("  (published %.2f)" % PUBLISHED_GATE_THRESHOLD[b["name"]])
             if b["name"] in PUBLISHED_GATE_THRESHOLD else "",
             e["log2X_at_q_2^250"]))

print()
print("=== 2. occupancy pricing at the cascade tier d = h-1 ===")
print("    tier charge L(h-1) = n-A+1 ; requirement  N_{h-1} <= "
      "headroom/(n-A+1)")
for e, b in zip(out["rows"], BANKED["rows"]):
    n, A = e["n"], e["A"]
    head = int(b["headroom"])
    slot = n - A + 1
    req = head // slot
    n3 = n ** 3
    e["tier_slot_n_minus_A_plus_1"] = slot
    e["required_N_hminus1"] = str(req)
    e["log2_required_N_hminus1"] = log2(req)
    e["log2_N_proved_bound_n_over_2"] = log2(n // 2)
    e["margin_bits_proved"] = log2(n // 2) - log2(req)
    e["log2_N_if_Gamma_is_q_2^250"] = 250.0 - 1
    e["margin_bits_if_confinement_failed"] = 249.0 - log2(req)
    e["log2_13n3"] = log2(13 * n3)
    e["log2_Gamma_casc_proved"] = log2(n)
    e["margin_bits_Gamma_casc_proved"] = log2(n) - log2(13 * n3)
    e["margin_bits_Gamma_casc_if_failed"] = 250.0 - log2(13 * n3)
    print("  %-11s required N_{h-1} <= 2^%-7.2f | PROVED n/2 = 2^%-6.2f "
          "(%+.1f bits) | if |Gamma| = q = 2^250: 2^249 (%+.1f bits) "
          "| Gamma_casc vs 13n^3: proved %+.1f, failed %+.1f"
          % (e["name"], log2(req), log2(n // 2), e["margin_bits_proved"],
             e["margin_bits_if_confinement_failed"],
             e["margin_bits_Gamma_casc_proved"],
             e["margin_bits_Gamma_casc_if_failed"]))
    chk(e["margin_bits_proved"] < 0,
        "proved bound clears the tier requirement", e["name"])
    chk(e["margin_bits_if_confinement_failed"] > 0,
        "a total confinement failure WOULD break the tier bound "
        "(the claim is load-bearing)", e["name"])

print()
print("=== 3. the measured extras law (from t1/t2 checkpoints) ===")
pts = []
for fn, key in (("t1_validate.json", "fixtures"), ("t2_hunt.json", "runs")):
    p = os.path.join(CHK, fn)
    if not os.path.exists(p):
        continue
    d = json.load(open(p))
    for r in d[key]:
        X = r["criticality_index"]
        ex = r.get("n_extra_rays_beyond_MC", r.get("n_extra_rays"))
        if ex is None or r.get("c_twist", 1) != 1:
            continue
        pts.append((r["n"], r["k"], r["w"], r["q"], r["j"], X, ex))
pts.sort(key=lambda t: t[5])
print("   n   k  w   q    j       X      extras   extras/X")
for (n, k, w, q, j, X, ex) in pts:
    print("  %3d %3d %2d %5d %2d %9.4g %8d   %s"
          % (n, k, w, q, j, X, ex, ("%.3f" % (ex / X)) if X else "-"))
sub = [(X, ex) for (_, _, _, _, _, X, ex) in pts if X < 1]
sup = [(X, ex) for (_, _, _, _, _, X, ex) in pts if X >= 2]
chk(all(ex == 0 for X, ex in sub),
    "no extra ray anywhere below the threshold (X < 1)", sub)
chk(any(ex > 0 for X, ex in sup),
    "extras DO appear above the threshold", sup[:5])
out["law"] = {"points": pts,
              "subcritical_all_zero": all(ex == 0 for X, ex in sub),
              "supercritical_max_ratio":
                  max([ex / X for X, ex in sup], default=None)}

out["verdict"] = "PASS" if not out["fails"] else "FAIL"
with open(os.path.join(CHK, "t3_pricing.json"), "w") as f:
    json.dump(out, f, indent=1)
print("\nchecks=%d fails=%d -> %s" % (out["checks"], len(out["fails"]),
                                      out["verdict"]))
