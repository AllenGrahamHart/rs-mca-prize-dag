#!/usr/bin/env python3
"""Exact CRATIO at promoted cells -- REUSES round-25 bbm.py verbatim.

MODE=main  : BBM identity split, RBUCK=256  (checkpoints into z_n32_band/ckpt)
MODE=alt   : BBM-ALT even/odd permutation, RBUCK=181 (D4 two-way verification)

  LIST=file SHARD=0 NSHARD=8 MODE=main tools/ramguard local -- python3 run32.py
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
Z25 = os.path.abspath(os.path.join(HERE, "..", "z_n32_band"))
sys.path.insert(0, HERE)
sys.path.insert(0, Z25)
from bbm import bbm, record, tsv_line, HDR                     # noqa: E402
from zcore import rows_M4, rows_M2                             # noqa: E402

CKDIR = os.path.join(Z25, "ckpt")
MODE = os.environ.get("MODE", "main")
SH = int(os.environ.get("SHARD", "0"))
NS = int(os.environ.get("NSHARD", "1"))
LIST = os.environ["LIST"]
OUT = os.path.join(HERE, "CELLS26.%s.s%d.tsv" % (MODE, SH))

jobs = []
for ln in open(os.path.join(HERE, LIST)):
    ln = ln.strip()
    if not ln or ln.startswith("#"):
        continue
    f = ln.split()
    jobs.append((f[0], int(f[1]), int(f[2]), f[3] if len(f) > 3 else ""))

done = set()
if os.path.exists(OUT):
    for ln in open(OUT):
        g = ln.split("\t")
        if len(g) > 3:
            done.add((g[0], int(g[2]), int(g[3])))

for idx, (fam, kappa, p, tag) in enumerate(jobs):
    if idx % NS != SH:
        continue
    if (fam, kappa, p) in done:
        continue
    rows = rows_M4(32, p) if fam == "M4" else rows_M2(32, kappa, p)
    t0 = time.time()
    if MODE == "main":
        ck = os.path.join(CKDIR, "%s_32_%d_%d.ck" % (fam, kappa, p))
        tn, nk, dp = bbm(rows, p, rbuck=256, ckpt=ck)
    elif MODE == "alt":
        perm = list(range(0, 32, 2)) + list(range(1, 32, 2))
        prows = [[r[j] for j in perm] for r in rows]
        tn, nk, dp = bbm(prows, p, rbuck=181)
    else:                       # MODE=alt2: THIRD variant, reversed + RBUCK=101
        prows = [list(reversed(r)) for r in rows]
        tn, nk, dp = bbm(prows, p, rbuck=101)
    d = record(rows, p, tn, nk, fam, tag)
    with open(OUT, "a") as fh:
        fh.write(tsv_line(d) + "\n")
    print("%s k=%d p=%-13d TNUM=%d NKER=%d CRATIO=%.10f ZFLOOR=%s  %.1fs"
          % (fam, kappa, p, tn, nk, d["CRATIO"], d["ZFLOOR_OK"],
             time.time() - t0), flush=True)
