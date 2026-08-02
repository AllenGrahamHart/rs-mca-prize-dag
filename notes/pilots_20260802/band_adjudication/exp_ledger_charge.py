"""exp_ledger_charge.py -- what does an MC received pair actually COST?

The ledger charges SLOPES, not pairs.  For each MC shift pencil this
measures, exhaustively:

    |Gamma|            live slopes (agreement exactly A over P^1(F_q))
    |Gamma_band|       live slopes sharing a band/cascade core with another
                       live slope (the exact object the Route-T column pays)
    sum_P L_P          over pairs with L_P >= 2   (the ledger's own sum)
    N_d                occupancy, selected-support reading (banked semantics)
    N_d^any            occupancy, "any exact-A ray" reading (NOT banked)
    n - A + 1          the printed B_tan slot
    |MC|               the raw band-pair population at depth h-1

PRE-REGISTERED (before any run):
 Q1  |Gamma| = n exactly (every point of -H is forced by some member).
 Q2  |Gamma_band| = |Gamma| (every live slope of an MC pencil is on a
     cascade line).
 Q3  |Gamma| > n - A + 1 by the factor n/(n-A+1) > 1 -- so a single MC
     received pair OVERFLOWS the printed tangent column.
 Q4  sum_{L_P>=2} L_P <= |Gamma| (exclusivity: the Lambda_P are disjoint).
 Q5  N_{h-1}(selected) <= |Gamma|/2 <= n/2  <<  |MC|.
 Q6  N_{h-1}(any) = |MC| -- the reading matters, and the banked reading is
     the selected one.

FIRST RUN OUTCOME: Q1, Q3, Q6 FAILED and are CORRECTED here (the original
forms are kept above verbatim; the corrected forms are what is now checked).
 Q1' Gamma = {-x_i : i in UNION of the family}, so |Gamma| = |union|,
     which is n when the family covers every coordinate and exactly
     n-A+1 = |T| when the family is a single member.  (The single-member
     case reproduces the payment audit's B_tan saturation ratio 1.0000
     CONSTRUCTIVELY.)
 Q3' |Gamma| > n-A+1 exactly when the family's union exceeds n-A+1
     coordinates, i.e. as soon as the family has two members with
     distinct supports.  Overflow factor = |union| / (n-A+1).
 Q6' N_{h-1}(any) >= |MC|: the structured members are a SUBSET of the
     depth-(h-1) pairs; char-p accidental (non-coset) solutions can add
     more (MC-4's completeness is char-0 and needs n a 2-power -- n = 18
     satisfies neither, and there the extras appear).
"""

import json
import os
import sys
from math import comb, gcd

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from mclib import (INF, Scan, make_domain, mc_c_from_gamma, mc_family,
                   poly_eval)

CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)

out = {"predictions": __doc__, "fixtures": [], "checks": 0, "fails": []}


def chk(cond, label, extra=None):
    out["checks"] += 1
    if not cond:
        out["fails"].append({"label": label, "extra": str(extra)})
        print("    FAIL", label, extra)
    return cond


def run(n, k, w, M, q):
    rp = n - k - w
    N, m = n // M, rp // M
    H, beta, omega = make_domain(q, n, beta_exp=0)
    c = mc_c_from_gamma(H, q, n, k, w, M)
    u = [0] * n
    u[n - 1] = 1
    u[k + w - 1] = (u[k + w - 1] + c) % q
    v = [0] * n
    v[n - 2] = 1
    v[k + w - 2] = (v[k + w - 2] + c) % q
    h, A = w + 1, k + w + 1
    uv = [poly_eval(u, x, q) for x in H]
    vv = [poly_eval(v, x, q) for x in H]
    fam = mc_family(H, q, n, k, w, M, c)
    pred = comb(N, m) // N if gcd(m, N) == 1 else None

    sc = Scan(H, q, k, uv, vv, A)
    live = sc.live()
    sel = sc.selected()
    Nd, Nd_any, detail = sc.occupancy()

    # Gamma_band: live slopes whose selected support carries a core shared
    # with another live slope's selected support (|S_z ^ S_z'| >= k).
    gb = set()
    ls = list(sel.items())
    for a in range(len(ls)):
        for b in range(a + 1, len(ls)):
            if len(ls[a][1] & ls[b][1]) >= k:
                gb.add(ls[a][0])
                gb.add(ls[b][0])
    sumL = sum(l for (_, l, _) in detail.values() if l >= 2)

    def Ld(d):
        return (n - k - d) // (h - d)

    rec = {"n": n, "k": k, "w": w, "M": M, "q": q, "h": h, "A": A,
           "mc_family": len(fam), "mc_formula": pred,
           "n_minus_A_plus_1": n - A + 1,
           "gamma": len(live), "gamma_band": len(gb),
           "sum_L_P_over_counted": sumL,
           "N_d_selected": {str(d): x for d, x in sorted(Nd.items())},
           "N_d_any": {str(d): x for d, x in sorted(Nd_any.items())},
           "ledger_column_selected": sum(Nd.get(d, 0) * Ld(d)
                                         for d in range(1, h)),
           "ledger_column_any": sum(Nd_any.get(d, 0) * Ld(d)
                                    for d in range(1, h)),
           "L_of_h_minus_1": Ld(h - 1),
           "gate_ok": sc.gate_ok(),
           "joint_explanation_max": sc.joint_max(),
           "pencil_max_agreement": max(sc.max_agr.values())}
    rec["gamma_over_slot"] = len(live) / float(n - A + 1)
    union = set()
    for T in fam:
        union |= set(T)
    rec["family_union"] = len(union)

    chk(rec["gate_ok"], "gate (no agreement > A)", (n, k, w, q))
    chk(sc.joint_max() == A - 1, "globally generic: joint max = A-1",
        (n, k, w, q, sc.joint_max(), A - 1))
    chk(len(live) == len(union), "Q1' |Gamma| = |union of the family|",
        (n, k, w, q, len(live), len(union)))
    chk(len(gb) == len(live), "Q2 Gamma_band = Gamma",
        (n, k, w, q, len(gb), len(live)))
    chk((len(live) > n - A + 1) == (len(union) > n - A + 1),
        "Q3' overflow iff union exceeds the slot",
        (n, k, w, q, len(live), len(union), n - A + 1))
    chk(len(fam) > 1 or len(live) == n - A + 1,
        "Q3' single-member family saturates the slot exactly",
        (n, k, w, q, len(fam), len(live), n - A + 1))
    chk(sumL <= len(live), "Q4 sum L_P <= |Gamma| (exclusivity)",
        (n, k, w, q, sumL, len(live)))
    chk(Nd.get(w, 0) <= len(live) // 2 or len(live) < 4,
        "Q5 N_{h-1} <= |Gamma|/2",
        (n, k, w, q, Nd.get(w, 0), len(live)))
    chk(Nd_any.get(w, 0) >= len(fam), "Q6' N_{h-1}(any) >= |MC|",
        (n, k, w, q, Nd_any.get(w, 0), len(fam)))
    chk(Ld(h - 1) == n - A + 1, "L(h-1) = n-A+1", (n, k, w, q))

    print("  n=%-3d k=%-3d w=%d q=%-4d | MC=%-4d  |Gamma|=%-3d "
          "Gamma_band=%-3d  n-A+1=%-3d (ratio %.4f) | sumL=%-3d "
          "N_{h-1}sel=%-3d N_{h-1}any=%-4d | col_sel=%-4d col_any=%-6d"
          % (n, k, w, q, len(fam), len(live), len(gb), n - A + 1,
             rec["gamma_over_slot"], sumL, Nd.get(w, 0), Nd_any.get(w, 0),
             rec["ledger_column_selected"], rec["ledger_column_any"]))
    return rec


JOBS = [
    (16, 4, 2, 2, 17), (16, 4, 2, 2, 97), (16, 4, 2, 2, 113),
    (16, 4, 2, 2, 193), (16, 4, 2, 2, 241),
    (18, 6, 2, 2, 19), (18, 6, 2, 2, 37), (18, 6, 2, 2, 73),
    (18, 6, 2, 2, 109), (18, 6, 2, 2, 181),
    (20, 4, 4, 4, 41), (20, 4, 4, 4, 101), (20, 4, 4, 4, 181),
    (16, 8, 4, 4, 17), (16, 8, 4, 4, 97), (16, 8, 4, 4, 193),
]
print("=== MC shift pencils: what the ledger actually pays ===")
for j in JOBS:
    out["fixtures"].append(run(*j))

out["verdict"] = "PASS" if not out["fails"] else "FAIL"
with open(os.path.join(CHK, "ledger_charge.json"), "w") as f:
    json.dump(out, f, indent=1)
print("\nchecks=%d fails=%d -> %s" % (out["checks"], len(out["fails"]),
                                      out["verdict"]))
