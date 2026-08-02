"""first_moment.py -- what a UNIFORMLY RANDOM word/pair does at the six rows.

Three elementary quantities, all exact up to the entropy/Stirling evaluation
of log2 C(n,a) (which is used only where n is astronomically large):

  E[L(W,a)]      = q^k * P(one codeword agrees in >= a places)
                 ~ C(n,a) * q^(k-a)                          (dominant term)
  a_max(W)       = largest a with C(n,a) q^(k-a) >= 1
                   -- the first moment's max-agreement threshold for a
                   uniformly random word (= Justesen-Hoholdt's g-hat).
  s_max(u,v)     = largest s with C(n,s) q^(2(k-s)) >= 1
                   -- the same for a random PAIR's JOINT codeword-pair
                   explanation (the "cascade" object).

Route T's standing hypotheses on the pencil are
  (H3) tangent gate      : max_{z,c} agr(c,w_z) <= A = k+h
  (H2) below cascade     : max joint codeword-pair agreement <= A-2
so a uniformly random pencil is ADMISSIBLE exactly when
  a_max < A   and   s_max <= A-2,
and it then carries E[L(w_z,tau)] codewords at tau for every member.

If E[L(w_z,tau)] >> 0.7 n^2 while a_max < A and s_max <= A-2, the reduced
statement of the band-occupancy reduction is false for the GENERIC pencil,
not merely for a bespoke construction.
"""

import json
import os
import sys
from math import comb, lgamma, log, log2

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)

ROWS = [
    ("RowC 1/4",   1024,          256,           5,          34.84816753926702),
    ("RowC 1/8",   1024,          128,           5,          29.847533632286996),
    ("RowC 1/16",  1024,          64,            3,          None),
    ("prize 1/4",  2199023255552, 549755813888,  8589934593, 0.800767298932776),
    ("prize 1/8",  2199023255552, 274877906944,  8589934593, 0.6858649121282252),
    ("prize 1/16", 2199023255552, 137438953472,  4294967297, 0.6596448038293138),
]


def lg2comb(n, r):
    if r < 0 or r > n:
        return float("-inf")
    if n <= 5000:
        return log2(comb(n, r))
    return (lgamma(n + 1) - lgamma(r + 1) - lgamma(n - r + 1)) / log(2.0)


def largest_a(n, k, lq, mult):
    """largest a with lg2comb(n,a) + mult*(k-a)*lq >= 0, by bisection."""
    lo, hi = k, n
    if lg2comb(n, k) + mult * 0 < 0:
        return k
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if lg2comb(n, mid) + mult * (k - mid) * lq >= 0:
            lo = mid
        else:
            hi = mid - 1
    return lo


res = {"rows": []}
print("%-12s %-6s %14s %14s %14s %14s %10s %10s %9s" %
      ("row", "log2q", "tau-k", "h(=A-k)", "E[L@tau] bits", "req bits",
       "amax-k", "smax-k", "admiss?"))
for name, n, k, h, req in ROWS:
    tau = k + -(-h // 2)
    A = k + h
    for lq in (128.0, 256.0):
        EL = lg2comb(n, tau) - (tau - k) * lq
        amax = largest_a(n, k, lq, 1)
        smax = largest_a(n, k, lq, 2)
        gate_ok = amax < A
        casc_ok = smax <= A - 2
        reqbits = log2(req * n * n) if req else None
        e = {"row": name, "n": n, "k": k, "h": h, "tau": tau, "A": A,
             "log2q": lq, "E_L_at_tau_bits": EL,
             "required_bits": reqbits,
             "a_max_excess": amax - k, "s_max_excess": smax - k,
             "gate_ok(a_max<A)": gate_ok, "below_cascade_ok(s_max<=A-2)": casc_ok,
             "random_pencil_admissible": gate_ok and casc_ok,
             "refutes": (reqbits is not None and EL > reqbits and gate_ok and casc_ok)}
        res["rows"].append(e)
        print("%-12s %-6.0f %14d %14d %14.4g %14s %10d %10d %9s"
              % (name, lq, tau - k, h, EL,
                 ("%.2f" % reqbits) if reqbits else "-",
                 amax - k, smax - k,
                 "YES" if (gate_ok and casc_ok) else
                 ("gate!" if not gate_ok else "cascade!")))

print()
print("Reading: 'E[L@tau] bits' is log2 of the expected number of codewords at")
print("agreement >= tau for a uniformly random word; 'req bits' is log2 of the")
print("band-occupancy reduction's requirement (~0.7 n^2).  'amax-k'/'smax-k' are")
print("the first-moment max single agreement and max joint pair agreement,")
print("to be compared with h = A-k (gate) and h-2 (below cascade).")

with open(os.path.join(CHK, "first_moment.json"), "w") as f:
    json.dump(res, f, indent=1)
print("\nwrote checkpoints/first_moment.json")
