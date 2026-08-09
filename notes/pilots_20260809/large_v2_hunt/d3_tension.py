#!/usr/bin/env python3
"""D3 - is there a TENSION between large v_2(Norm-1) and large LOGNORM?

A structural obstruction supporting option (c) would need large v_2 to cost
norm size (pushing witnesses out of the admissible window).  Measured here:
the conditional distribution of LOGNORM given v_2(Norm-1) >= g, for the
family (nodd = 3) that is NOT pinned by LAW 2."""
import random
import sys
from collections import defaultdict
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K  # noqa: E402

H = 64
rng = random.Random(20260809)
M = 60000
by = defaultdict(list)
for _ in range(M):
    w = K.fam_C(H, rng, 3)
    n = abs(K.tower_norm(w))
    if n == 0 or n % 2 == 0:
        continue
    g = ((n - 1) & -(n - 1)).bit_length() - 1
    by[g].append(n.bit_length())

allb = sorted(b for v in by.values() for b in v)
print("FAM-C3, %d odd norms.  unconditional LOGNORM: mean %.2f  median %d  "
      "max %d" % (len(allb), sum(allb) / len(allb), allb[len(allb) // 2], allb[-1]))
print("\n  g = v2(Norm-1)   count   mean LOGNORM   median   max   P(LOGNORM>=244)")
cum = []
for g in sorted(by):
    cum = [b for gg in sorted(by) if gg >= g for b in by[gg]]
    if len(cum) < 20:
        break
    print("   >= %-3d %12d   %10.2f %8d %5d   %.2e"
          % (g, len(cum), sum(cum) / len(cum), sorted(cum)[len(cum) // 2],
             max(cum), sum(1 for b in cum if b >= 244) / len(cum)))
print("\nIf the mean LOGNORM is flat in g, v_2(Norm-1) and LOGNORM are "
      "independent: large v_2 costs NOTHING in norm size, so there is no\n"
      "2-adic/archimedean tension to build a structural obstruction on.")
