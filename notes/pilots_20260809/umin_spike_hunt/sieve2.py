#!/usr/bin/env python3
"""kappa=2 arm (M2, Lambda={1,3}, N=32, sigma in [-2,2] -> p in [2^15,2^17]).
The whole in-band M2 line is only 266 primes; the RESSIEVE decides ALL of them
for every weight U <= UMAX at once, and each candidate is re-verified exactly.

  UMAX=7 tools/ramguard local -- python3 sieve2.py
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rs                                                      # noqa: E402
from zcore import is_prime                                     # noqa: E402

N = 32
UMAX = int(os.environ.get("UMAX", "7"))
PLO, PHI = 1 << 15, 1 << 17
q = rs.find_q(61, 64)
w = rs.find_w(q, 64)
W, Wn = rs.build_roots(N, q, w)

band = [p for p in range(PLO + 1, PHI + 1, 64) if is_prime(p)]
print("in-band M2 primes (p = 1 mod 64, 2^15 < p <= 2^17): %d" % len(band),
      flush=True)

reps = {}
t0 = time.time()
for U in range(1, UMAX + 1):
    hits, nleaf, nhit = rs.sieve_U_sq(N, U, PLO, PHI, q, W, Wn)
    ok = 0
    for (p, UU, S, t) in hits:
        v = rs.verify_hit(N, p, S, t, kappa=2)
        if v is None:
            continue          # p^2 | Res but not two DISTINCT vanishing factors
        ok += 1
        reps.setdefault(p, []).append((UU, v[1]))
    print("  U=%d: %d leaves, %d square-candidates, %d verified kernel vectors"
          % (U, nleaf, nhit, ok), flush=True)

with open(os.path.join(HERE, "CANDS.N32.k2.tsv"), "w") as fh:
    fh.write("p\tSIGMA\tUMIN\tH\tPREDCR\tBONUS\tAU\n")
    out = []
    import math
    for p, rl in reps.items():
        AU = rs.au_from_reps(N, rl)
        bonus = sum(a * 2.0 ** (-u) for u, a in AU.items())
        H = ((1 << 32) - 1) / float(p * p)
        out.append((1 + bonus / (1 + H), p, min(AU), H, bonus, AU))
    out.sort(reverse=True)
    for (pc, p, umin, H, bonus, AU) in out:
        fh.write("%d\t%.6f\t%d\t%.6f\t%.6f\t%.6f\t%s\n"
                 % (p, 32 - 2 * math.log2(p), umin, H, pc, bonus,
                    ";".join("%d:%d" % (u, AU[u]) for u in sorted(AU))))
    for r in out[:20]:
        print("   p=%-7d UMIN=%d PREDCR=%.4f AU=%s"
              % (r[1], r[2], r[0], ";".join("%d:%d" % (u, r[5][u])
                                            for u in sorted(r[5]))), flush=True)
print("kappa=2 arm: %d of %d in-band primes carry an orbit of weight <= %d"
      " (%.1fs)" % (len(reps), len(band), UMAX, time.time() - t0), flush=True)
