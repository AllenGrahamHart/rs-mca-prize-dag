"""priced_table.py -- the two adjudication outcomes, priced, six rows.

Reads checkpoints/rows.json (produced by rows.py) and prints the table the
Route T memo needs, plus the MC exposure figures under both readings of
L_P.
"""

import json
import os
import sys
from math import log2

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
CHK = os.path.join(HERE, "checkpoints")
R = json.load(open(os.path.join(CHK, "rows.json")))["rows"]

print("=== TABLE 1: the classification, priced (exact) ===")
print("%-11s %-16s %-16s %-9s %-9s %-8s" %
      ("row", "col[1,h-2] @N=1", "col[1,h-1] @N=1", "reqN(i)", "reqN(ii)",
       "tighten"))
for e in R:
    print("%-11s %-16d %-16d %-9s %-9s %-8s" %
          (e["name"], e["sumL_band_1_to_hminus2"], e["sumL_ext_1_to_hminus1"],
           ("%.4f n^2" % e["req_Nd_band_over_n2"])
           if e["req_Nd_band_over_n2"] < 1e6 else "vacuous",
           ("%.4f n^2" % e["req_Nd_ext_over_n2"])
           if e["req_Nd_ext_over_n2"] < 1e6 else "vacuous",
           "%.2f%%" % (100 * (1 - e["req_Nd_ext_over_n2"]
                              / e["req_Nd_band_over_n2"]))))

print()
print("=== TABLE 2: the cascade tier as a standalone charge ===")
print("%-11s %-16s %-14s %-14s %-14s" %
      ("row", "L(h-1)=n-A+1", "reqN_{h-1}", "|Gamma_casc| cap",
       "as %% of 16n^3"))
for e in R:
    n = e["n"]
    cap = e["req_N_hminus1_alone_over_n2"] * n * n * e["n_minus_A_plus_1"]
    vac = e["req_N_hminus1_alone_over_n2"] >= 1e6
    print("%-11s %-16d %-14s %-14s %-14s" %
          (e["name"], e["n_minus_A_plus_1"],
           "vacuous" if vac else ("%.3f n^2"
                                  % e["req_N_hminus1_alone_over_n2"]),
           "vacuous" if vac else "%.3f n^3" % (cap / float(e["n3"])),
           "vacuous" if vac else "%.2f%%" % (100.0 * cap
                                             / (16.0 * e["n3"]))))

print()
print("=== TABLE 3: the MC exposure under the two readings of L_P ===")
print("%-11s %-12s %-12s %-12s %-12s %-12s" %
      ("row", "MC pairs", "req N_{h-1}", "ANY reading", "SELECTED cap",
       "SELECTED"))
for e in R:
    if not e.get("mc_admissible"):
        continue
    n = e["n"]
    req = e["req_N_hminus1_alone_over_n2"] * n * n
    print("%-11s 2^%-10.2f 2^%-10.2f %-12s 2^%-10.2f %-12s" %
          (e["name"], e["mc_count_log2"], log2(req),
           "%+.1f bits" % (e["mc_count_log2"] - log2(req)),
           log2(n // 2),
           "%+.1f bits" % (log2(n // 2) - log2(req))))

print()
print("=== TABLE 4: what a single MC received pair actually costs ===")
print("%-11s %-14s %-16s %-10s %-22s" %
      ("row", "|Gamma| = n", "B_tan slot n-A+1", "overflow", "|Gamma| vs 13n^3"))
for e in R:
    n = e["n"]
    print("%-11s 2^%-12.2f %-16d x%-9.4f %-22s" %
          (e["name"], log2(n), e["n_minus_A_plus_1"],
           e["MC_gamma_over_B_tan_slot"],
           "%+.1f bits" % (log2(n) - log2(13.0 * e["n3"]))))

print()
print("=== TABLE 5: quotient-strip status of the MC pair (T3/P3) ===")
print("%-11s %-14s %-16s %-8s %-24s" %
      ("row", "M = h-1", "gcd(n,k)", "P3?", "quotient row (n',k',h')"))
for e in R:
    qr = e["quotient_row"]
    print("%-11s %-14d %-16d %-8s (%d, %d, %s)  band proper %s" %
          (e["name"], e["P3_M"], e["gcd_n_k"], e["P3_fires"], qr["n"], qr["k"], qr["h"],
           "EMPTY" if qr["band_proper_empty"] else "nonempty"))

print()
print("=== TABLE 6: structured (coset-union) depth census ===")
print("%-11s %-12s %-30s %-22s" %
      ("row", "ceil(h/2)", "structured depths", "in band proper"))
for e in R:
    sd = e["structured_depths_all"]
    txt = (str(sd) if isinstance(sd, list) else
           "%d powers of two, 1..%d" % (sd["count"], sd["max"]))
    print("%-11s %-12d %-30s %-22s" %
          (e["name"], -(-e["h"] // 2), txt,
           e["structured_in_band_proper_upper"] or "NONE (empty)"))
