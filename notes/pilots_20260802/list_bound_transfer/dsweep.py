"""dsweep.py -- how large can the STRUCTURED part be made as the excess
d = a - k grows, and how does it compare with plain volume counting?

(1) MC sweep.  For each row and each admissible M = w (M | n, M | n-k-w),
    the structured floor is C(N,m)/N, N = n/M, m = (n-k-M)/M.  Tabulated in
    bits against n^2 and against the band-occupancy requirement.

(2) Plain counting (Justesen-Hoholdt / Cheng-Wan restatement, evaluation-set
    AGNOSTIC): SOME Hamming ball of radius n-a contains at least
    C(n,a)/q^{a-k} codewords.  Computed in bits at tau for log2 q = 256.
    This bound needs no domain structure at all -- but it gives an
    EXISTENTIAL centre with NO control on the maximum agreement, so it
    cannot by itself meet the Route-T tangent gate (H3).  The MC family
    does, via the proved ceiling.

(3) Crossover: the largest excess d at which the MC floor still exceeds n^2.
"""

import json
import os
import sys
from math import comb, gcd, log2

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

LOG2Q = 256.0   # official cap q < 2^256


def log2comb(n, r):
    """log2 C(n,r) -- exact for small n, entropy+Stirling for huge n."""
    if n <= 4000:
        return log2(comb(n, r))
    from math import lgamma, log
    return (lgamma(n + 1) - lgamma(r + 1) - lgamma(n - r + 1)) / log(2.0)


res = {"mc_sweep": [], "plain_counting": [], "crossover": []}

print("=== (1) MC structured floor as a function of the excess d = w = M ===")
for name, n, k, h, req in ROWS:
    tau = k + -(-h // 2)
    G = gcd(n, k)
    divs = sorted({d for i in range(1, int(G ** 0.5) + 1) if G % i == 0
                   for d in (i, G // i)})
    print("%-12s n=%d k=%d h=%d tau-k=%d   [admissible w must divide gcd(n,k)=%d]"
          % (name, n, k, h, tau - k, G))
    rowout = {"row": name, "n": n, "k": k, "h": h, "tau_excess": tau - k,
              "sweep": []}
    for M in divs:
        rp = n - k - M
        if rp % M or n % M:
            continue
        N, m = n // M, rp // M
        if gcd(m, N) != 1:
            continue
        lb = log2comb(N, m) - log2(N)
        e = {"w": M, "N": N, "m": m, "log2_count": lb,
             "log2_n2": 2 * log2(n), "over_n2_bits": lb - 2 * log2(n),
             "in_route_T_window": (tau - k) <= M <= h}
        rowout["sweep"].append(e)
        mark = "  <== Route-T window" if e["in_route_T_window"] else ""
        if M in divs[:6] or e["in_route_T_window"] or M >= divs[-3]:
            print("    w=M=%-12d N=%-8d m=%-8d log2(count)=%8.2f  "
                  "(n^2 = 2^%.2f, excess %+8.2f bits)%s"
                  % (M, N, m, lb, 2 * log2(n), lb - 2 * log2(n), mark))
    res["mc_sweep"].append(rowout)
    print()

print("=== (2) plain volume counting at tau (Justesen-Hoholdt), log2 q = 256 ===")
print("    NOTE: existential centre, NO ceiling -> cannot meet the tangent gate.")
for name, n, k, h, req in ROWS:
    tau = k + -(-h // 2)
    lb = log2comb(n, tau) - (tau - k) * LOG2Q
    e = {"row": name, "tau": tau, "log2_JH_bound": lb,
         "log2_n2": 2 * log2(n),
         "nontrivial": lb > 0, "beats_n2": lb > 2 * log2(n)}
    res["plain_counting"].append(e)
    print("    %-12s log2[C(n,tau)/q^(tau-k)] = %14.4g   (n^2 = 2^%.2f)  "
          "nontrivial=%s beats_n2=%s"
          % (name, lb, 2 * log2(n), e["nontrivial"], e["beats_n2"]))

print()
print("=== (3) crossover: largest excess d with MC floor > n^2, rate 1/4 ===")
for n in [256, 1024, 4096, 65536, 2199023255552]:
    k = n // 4
    best = None
    G = gcd(n, k)
    divs = sorted({d for i in range(1, int(G ** 0.5) + 1) if G % i == 0
                   for d in (i, G // i)})
    for M in divs:
        rp = n - k - M
        if rp % M or gcd(rp // M, n // M) != 1:
            continue
        lb = log2comb(n // M, rp // M) - log2(n // M)
        if lb > 2 * log2(n):
            best = (M, lb)
    e = {"n": n, "k": k, "largest_d_above_n2": best[0] if best else None,
         "log2_count_there": best[1] if best else None,
         "d_over_n": best[0] / n if best else None}
    res["crossover"].append(e)
    print("    n=%-16d k=%-14d largest d with floor > n^2: %-14s (d/n = %.4g)"
          % (n, k, best[0] if best else "none", best[0] / n if best else 0))

with open(os.path.join(CHK, "dsweep.json"), "w") as f:
    json.dump(res, f, indent=1)
print("\nwrote checkpoints/dsweep.json")
