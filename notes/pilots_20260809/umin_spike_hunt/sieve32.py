#!/usr/bin/env python3
"""D2 THE HUNT -- exhaustive RESSIEVE census of the WHOLE N=32 band.

Decides, for EVERY admissible prime p in [2^30, 2^34] with 64 | p-1
(~2.1e7 of them), whether the M4/I2-RSET cell at p carries a ternary
kernel orbit of weight U -- exactly, by THEOREM RS.  Round 25 sampled
47 of those primes; this is a census.

  U=6 SHARD=0 NSHARD=1 tools/ramguard local -- python3 sieve32.py
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rs                                                      # noqa: E402

N = int(os.environ.get("N", "32"))
U = int(os.environ["U"])
SH = int(os.environ.get("SHARD", "0"))
NS = int(os.environ.get("NSHARD", "1"))
PLO = 1 << (N - 2)
PHI = 1 << (N + 2)
OUT = os.path.join(HERE, "HITS.N%d.U%d.s%d.tsv" % (N, U, SH))

q = rs.find_q(61, 2 * N)
w = rs.find_w(q, 2 * N)
W, Wn = rs.build_roots(N, q, w)
t0 = time.time()
with open(OUT, "w") as fh:
    hits, nleaf, ncand, nhit = rs.sieve_U(
        N, U, PLO, PHI, q, W, Wn, shard=SH, nshard=NS, out=fh,
        progress=20000, collect=False)
dt = time.time() - t0
print("SIEVE N=%d U=%d shard %d/%d : leaves=%d cand=%d hits=%d  %.1fs "
      "(%.2f us/leaf)" % (N, U, SH, NS, nleaf, ncand, nhit, dt,
                          1e6 * dt / max(nleaf, 1)), flush=True)
