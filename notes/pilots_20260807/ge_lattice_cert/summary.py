#!/usr/bin/env python3
"""Final ledger: every cell attempted, its exact measured state, and the
model's prediction at the REALISED basis quality."""
import glob
import json
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', 'ge_floor_falsifier')))
import latlib as LL                                       # noqa: E402
from estimate import est                                  # noqa: E402
from d4_price import fpcost                               # noqa: E402

STATE = os.path.join(HERE, "state")


def prof_of(cid):
    f = os.path.join(STATE, "%s.lll.json" % cid)
    B = json.load(open(f))["B"]
    d, lam = LL.integral_gso(B)
    n = len(B)
    return [math.log2(d[i + 1]) - math.log2(d[i]) for i in range(n)], B


def rhf_of(B, p):
    n = len(B)
    b0 = LL.dot(B[0], B[0])
    return 2 ** ((0.5 * math.log2(b0) - math.log2(p) / n) / (n - 1))


CELLS = [("E1-128", 12), ("CORRIDOR-128", 1), ("CORRIDOR-128-CONJ", 1),
         ("PLANT-64", 1), ("PROTH-1over2", 1)]

print("=" * 112)
print("FINAL LEDGER -- every dimension-64 cell attempted in this pilot")
print("=" * 112)
print("%-20s %-9s %-8s %-9s %-14s %-12s %-11s %-8s"
      % ("cell", "log2 p", "RHF", "FPEST", "FPNODES measured", "log2 nodes",
         "CPU-sec", "verdict"))
print("-" * 112)
for (cid, ns) in CELLS:
    lf = os.path.join(STATE, "%s.lll.json" % cid)
    if not os.path.exists(lf):
        continue
    prof, B = prof_of(cid)
    n = len(B)
    R = math.sqrt(4 * n)
    fe, pk, _ = est(prof, R)
    tot, secs, fnd, done, nsh = 0, 0.0, set(), 0, 0
    if ns > 1:
        fs = sorted(glob.glob(os.path.join(STATE,
                                           "%s.enum.s*of%d.json" % (cid, ns))))
    else:
        fs = [os.path.join(STATE, "%s.enum.json" % cid)]
    for f in fs:
        if not os.path.exists(f):
            continue
        d = json.load(open(f))
        tot += d["nodes"]
        secs += d["secs"]
        fnd |= set(tuple(w) for w in d["found"])
        done += (d["lev"] >= n)
        nsh += 1
    fin = (nsh == ns) and (done == ns)
    p = json.load(open(os.path.join(STATE, "%s.cert.json" % cid)))["p"] \
        if os.path.exists(os.path.join(STATE, "%s.cert.json" % cid)) else None
    if p is None:
        import cells as C
        p = (C.P250 if cid in ("E1-128", "PLANT-64") else
             C.QCORR if cid.startswith("CORRIDOR") else C.ALLCELLS[cid]["p"])
    verd = ("EMPTY" if (fin and not fnd) else
            "NONEMPTY(%d)" % len(fnd) if fin else "PARTIAL")
    print("%-20s %-9.3f %-8.5f 2^%-7.2f %-14d 2^%-10.3f %-11.0f %-8s"
          % (cid, math.log2(p), rhf_of(B, p), fe, tot,
             math.log2(max(tot, 1)), secs, verd))
print("-" * 112)

print("\n-- the round-22 GSA model at the REALISED root Hermite factor --")
print("   (round-22 priced 2^27.4 assuming delta = 1.0219 and log2 p = 250;")
print("    the pinned prime is 2^249.000 and my exact integer LLL realises")
print("    a worse delta, so the honest LLL-only price is higher.)")
for (cid, lp) in [("E1-128", 249.000), ("CORRIDOR-128", 255.900)]:
    prof, B = prof_of(cid)
    import cells as C
    p = C.P250 if cid == "E1-128" else C.QCORR
    r = rhf_of(B, p)
    m1 = fpcost(64, lp, 16.0, 1.0219)[0]
    m2 = fpcost(64, lp, 16.0, r)[0]
    fe, pk, _ = est(prof, 16.0)
    print("   %-16s GSA@1.0219 = 2^%-6.2f   GSA@realised %.5f = 2^%-6.2f   "
          "measured-profile FPEST = 2^%.2f" % (cid, m1, r, m2, fe))

print("\n-- ledger of what was NOT run, with its exact price --")
import cells as C                                        # noqa: E402
for c in C.EXTENSION:
    print("   %-16s h=64 log2 p=%-8.3f  FPPRICE(LLL) = 2^%-6.2f  "
          "FPPRICE(BKZ-90) = 2^%-6.2f  -> OUT OF REACH"
          % (c["cid"], math.log2(c["p"]),
             fpcost(64, math.log2(c["p"]), 16.0, 1.0219)[0],
             fpcost(64, math.log2(c["p"]), 16.0, 1.0060)[0]))
for c in C.ANCHOR:
    R2 = min(4 * c["h"], 2 * c["L"])
    R = math.sqrt(R2)
    bc = LL.boxcount(c["h"], c["L"])
    ch = math.log2(bc - 1) - math.log2(c["p"])
    print("   %-16s h=%-4d 2l'=%-4d FPPRICE(LLL) = 2^%-7.1f  CLASSHEUR = "
          "2^%-8.1f  -> %s"
          % (c["cid"], c["h"], c["L"],
             fpcost(c["h"], math.log2(c["p"]), R, 1.0219)[0], ch,
             "OUT OF REACH; witnesses EXPECTED" if ch > 0
             else "OUT OF REACH; emptiness expected"))
