#!/usr/bin/env python3
"""G6 (added gate): SHARD EQUIVALENCE.  For every validation cell, the
sharded enumeration must reproduce the single-process FPNODES EXACTLY
(sum over shards) and the single-process FPFOUND EXACTLY (union over
shards), for several shard counts and frontier depths.
"""
import os
import sys
import time

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', 'ge_floor_falsifier')))
import latlib as LL                                       # noqa: E402

STATE = os.path.join(HERE, "state")
os.makedirs(STATE, exist_ok=True)
FAIL = []

ROWS = [(4, 137, 8), (4, 401, 8), (8, 12289, 6), (8, 12289, 16),
        (8, 463249, 16), (8, 463457, 16)]

print("== G6: shard equivalence (exact node totals AND exact witness sets) ==")
print("%-4s %-9s %-5s %-4s %-4s %-10s %-10s %-8s %-8s"
      % ("h", "p", "2l'", "ns", "sd", "nodes(1)", "sum nodes", "nodes==",
         "found=="))
for (h, p, L) in ROWS:
    z = LL.zeta_of_order(2 * h, p)
    cv = [pow(z, j, p) for j in range(h)]
    B = LL.coeff_basis(h, p, cv)
    dl = time.time() + 1e9
    sp = os.path.join(STATE, "sh.lll.json")
    if os.path.exists(sp):
        os.remove(sp)
    st, info = LL.lll_resumable(sp, B, "sh", [(3, 4), (99, 100)], dl,
                                log=lambda *a: None)
    Br = info["B"]
    R2 = min(4 * h, 2 * L)
    ep = os.path.join(STATE, "sh.enum.json")
    if os.path.exists(ep):
        os.remove(ep)
    _, base = LL.enum_resumable(ep, Br, R2, L, "sh", dl, log=lambda *a: None)
    for (ns, sd) in [(2, 1), (3, 2), (5, 2), (7, 3), (13, 3)]:
        tot = 0
        fnd = set()
        for s in range(ns):
            f = os.path.join(STATE, "sh.enum.s%d.json" % s)
            if os.path.exists(f):
                os.remove(f)
            _, r = LL.enum_resumable(f, Br, R2, L, "sh", dl,
                                     log=lambda *a: None,
                                     shard=s, nshard=ns, sdepth=sd)
            tot += r["nodes"]
            fnd |= set(r["found"])
        a = tot == base["nodes"]
        b = fnd == set(base["found"])
        if not (a and b):
            FAIL.append((h, p, L, ns, sd, base["nodes"], tot))
        print("%-4d %-9d %-5d %-4d %-4d %-10d %-10d %-8s %-8s  %s"
              % (h, p, L, ns, sd, base["nodes"], tot, a, b,
                 "PASS" if (a and b) else "**FAIL**"))

print()
if FAIL:
    print("G6 **FAILED**: %s" % FAIL)
    sys.exit(1)
print("G6 PASS -- sharding is exactly equivalent to the single-process "
      "enumeration on all %d cells x 5 shard configurations." % len(ROWS))
