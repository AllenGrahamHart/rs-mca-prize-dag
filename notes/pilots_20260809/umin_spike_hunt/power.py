#!/usr/bin/env python3
"""POWER CONTROL on the instrument itself (the brief's second escape test).

Targets: the two banked UMIN=9 kappa=1 cells (the round-25 record 4683696257
and 12148002497) -- the sieve MUST fire at U=9 and stay silent at U<=8; and
the two banked UMIN=11 cells (4294967681, 6074003393) -- the sieve MUST stay
silent at every U <= 9.  Ground truth is wenum.py's exact AU (round 25).

  U=9 SHARD=0 NSHARD=6 tools/ramguard local -- python3 power.py
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rs                                                      # noqa: E402

TARGETS = [4683696257, 12148002497, 4294967681, 6074003393]
U = int(os.environ["U"])
SH = int(os.environ.get("SHARD", "0"))
NS = int(os.environ.get("NSHARD", "1"))
OUT = os.path.join(HERE, "POWER.U%d.s%d.tsv" % (U, SH))

q = rs.find_q(61, 64)
w = rs.find_w(q, 64)
W, Wn = rs.build_roots(32, q, w)
t0 = time.time()
with open(OUT, "w") as fh:
    found, nleaf = rs.sieve_targets(32, U, TARGETS, q, W, Wn, shard=SH,
                                    nshard=NS, out=fh, progress=100000)
print("POWER U=%d shard %d/%d: %d leaves, %d target hits  %.1fs"
      % (U, SH, NS, nleaf, len(found), time.time() - t0), flush=True)
for p in TARGETS:
    n = sum(1 for f in found if f[0] == p)
    print("   p=%-12d hits=%d" % (p, n), flush=True)
