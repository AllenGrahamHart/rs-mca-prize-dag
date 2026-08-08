#!/usr/bin/env python3
"""Full fail-closed verification (PREREG P5) of every recorded hit."""
import glob
import json
import sys
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K
from hunt import verify_hit

MINBITS = int(sys.argv[1]) if len(sys.argv) > 1 else 244
ORDER = int(sys.argv[2]) if len(sys.argv) > 2 else 128
PAT = sys.argv[3] if len(sys.argv) > 3 else "probe64_*.json"

recs = []
for f in sorted(glob.glob("notes/pilots_20260808/kernel_window_hunt/state/" + PAT)):
    st = json.load(open(f))
    for r in st.get("hits", []):
        if r["pbits"] >= MINBITS:
            recs.append(r)
print("records with pbits >= %d: %d" % (MINBITS, len(recs)))

best = None
allok = True
for i, r in enumerate(recs):
    p = int(r["p"])
    rep = verify_hit(r["w"], p, ORDER)
    allok = allok and rep["ok"]
    if best is None or p > int(best[0]["p"]):
        best = (r, rep)
    print("[%02d] pbits=%d ok=%s l1=%d S=%d v2(p-1)=%d cof=%d km=%s"
          % (i, rep["p_bits"], rep["ok"], rep["l1"], rep["S"],
             rep["v2_p_minus_1"], rep["cofactor"],
             "yes(s=%d)" % rep["kernel_membership"][1] if rep["kernel_membership"] else "NO"))
print("ALL VERIFIED:", allok)

r, rep = best
print("\n=== LARGEST WITNESS ===")
print("w =", r["w"])
print("p =", r["p"])
print("p bits =", rep["p_bits"], " p mod 128 =", rep["p_mod_order"],
      " v2(p-1) =", rep["v2_p_minus_1"])
print("Norm bits =", rep["norm_bits"], " cofactor =", rep["cofactor"])
print("||w||_1 =", rep["l1"], " S =", rep["S"])
print("rho, s =", rep["kernel_membership"])
print("log2(253^32) = %.4f ; p <= 253^32 : %s" %
      (K.CEIL253.bit_length() - 1 + 0.4519, rep["p_le_253_32"]))
json.dump({"w": r["w"], "p": r["p"], "rep": {k: str(v) for k, v in rep.items()}},
          open("notes/pilots_20260808/kernel_window_hunt/state/best_witness.json", "w"))
