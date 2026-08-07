#!/usr/bin/env python3
"""Collect every radius-graded certificate produced at the deployed rows."""
import glob
import json
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "state")
sys.path.insert(0, HERE)
import cells as C                                         # noqa: E402

print("== RADIUS-GRADED CERTIFICATES at the four LITERAL deployed Proth "
      "prize primes (h=64, N'=128) ==")
print("   free radius by the archimedean norm bound (L^64 < p) is L = 6 at "
      "ALL FOUR rows;")
print("   every line below with L > 6 is BEYOND what any norm bound gives.\n")
print("%-16s %-9s %-5s %-8s %-14s %-9s %-10s"
      % ("row", "log2 p", "L", "swaps", "FPNODES", "CPU-sec", "verdict"))
rows = {}
for f in sorted(glob.glob(os.path.join(STATE, "PROTH-*@*.cert.json"))):
    d = json.load(open(f))
    cid = os.path.basename(f).replace(".cert.json", "")
    base, L = cid.split("@")
    rows[(base, int(L))] = d
for (base, L) in sorted(rows, key=lambda t: (t[0], t[1])):
    d = rows[(base, L)]
    print("%-16s %-9.3f %-5d %-8d %-14d %-9.0f %-10s"
          % (base, math.log2(d["p"]), L, L // 2, d["nodes"], d["fpsec"],
             "EMPTY" if not d["found"] else "NONEMPTY(%d)" % len(d["found"])))
print("\n   'swaps' = L/2: a swap-distance-s collision has folded support "
      "||w||_1 <= 2s,")
print("   so L = 24 certifies 12 swaps -- the radius named verbatim in")
print("   critical/nodes/lattice_cone_certificate/statement.md:13:")
print("     \"weight-graded MITM (provable radius extension 7 -> ~12 swaps "
      "per row)\"")
