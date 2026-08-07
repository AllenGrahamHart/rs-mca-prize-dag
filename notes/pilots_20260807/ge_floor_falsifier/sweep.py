#!/usr/bin/env python3
"""EXHAUSTIVE sweep of the difference box {-2,..,2}^h.  Feeds D1 and D3.

For every nonzero box vector d it records, exactly:
  NORM(d)             Norm_{R/Q}(d)                       (tower recursion)
  ODDCOST(d)          # of distinct odd PRIME IDEALS dividing (d)
  ODDSIG(d)           the ideal set itself, as {p: gcd(d mod p, x^h+1)}
  L1(d) = ||d||_1     the folded support cost (D3's ell-condition)

Outputs (stdout + a JSON dump of the small filtered sets):
  D1  cost histogram; the sets A_k = {d : ODDCOST(d) <= k}
  D3  MAXNORM(L) = max |NORM| over ||d||_1 <= L
      TIGHTEMPTY(L) = max prime p = 1 mod N' with p | NORM(d), ||d||_1 <= L
"""
import json
import sys
import itertools

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from gelib import (tower_norm, sigma, mult_order, spf_sieve, factor_with)


def main():
    h = int(sys.argv[1])
    kmax = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    N = 2 * h
    amgm = (4 * h) ** (h // 2)          # AM-GM ceiling on the full box
    spf = spf_sieve(amgm if amgm <= (1 << 21) else (1 << 21))

    fcache = {}

    def fp(p):
        if p not in fcache:
            fcache[p] = mult_order(p, N)
        return fcache[p]

    cost_hist = {}
    maxnorm = [0] * (2 * h + 1)         # by ||d||_1 (max 2h)
    maxnorm_wit = [None] * (2 * h + 1)
    tight = [0] * (2 * h + 1)           # max p = 1 mod N dividing a norm
    tight_wit = [None] * (2 * h + 1)
    keep = []                           # (d, cost, sig) for cost <= kmax
    pool = {}                           # odd rational primes seen -> count
    nbox = 0

    for d in itertools.product((-2, -1, 0, 1, 2), repeat=h):
        if not any(d):
            continue
        nbox += 1
        nm = tower_norm(list(d))
        anm = abs(nm)
        l1 = sum(abs(t) for t in d)
        if anm > maxnorm[l1]:
            maxnorm[l1] = anm
            maxnorm_wit[l1] = d
        o = anm
        while o % 2 == 0:
            o //= 2
        if o == 1:
            cost = 0
            sig = {}
        else:
            fac = factor_with(spf, o)
            for p in fac:
                pool[p] = pool.get(p, 0) + 1
                if p % N == 1 and p > tight[l1]:
                    tight[l1] = p
                    tight_wit[l1] = d
            if len(fac) > kmax:
                cost = kmax + 1
                sig = None
            else:
                cost = 0
                sig = {}
                for p in fac:
                    s = sigma(d, p, h)
                    c = (len(s) - 1) // fp(p)
                    assert c >= 1 and (len(s) - 1) % fp(p) == 0, (d, p, s)
                    cost += c
                    sig[p] = s
                    if cost > kmax:
                        break
        cost_hist[min(cost, kmax + 1)] = cost_hist.get(min(cost, kmax + 1), 0) + 1
        if cost <= kmax:
            keep.append((d, cost, sig))

    # running maxima over ||d||_1 <= L
    for i in range(1, 2 * h + 1):
        if maxnorm[i] < maxnorm[i - 1]:
            maxnorm[i] = maxnorm[i - 1]
            maxnorm_wit[i] = maxnorm_wit[i - 1]
        if tight[i] < tight[i - 1]:
            tight[i] = tight[i - 1]
            tight_wit[i] = tight_wit[i - 1]

    print("== SWEEP h=%d (N'=%d)  box=%d nonzero vectors  kmax=%d ==" %
          (h, N, nbox, kmax))
    print("-- D1: ODDCOST histogram (# distinct odd prime IDEALS dividing (d))")
    for c in sorted(cost_hist):
        lbl = str(c) if c <= kmax else ">%d" % kmax
        print("   cost %-4s : %d" % (lbl, cost_hist[c]))
    print("-- odd rational primes occurring in box norms (PRIMEPOOL): %d" %
          len(pool))
    print("   %s" % sorted(pool))
    print("   residue degrees f_p = ord(p mod %d): %s" %
          (N, {p: fp(p) for p in sorted(pool)}))
    print("-- D3: MAXNORM and TIGHTEMPTY by ||w||_1 <= L  (2l' = L)")
    print("   %-4s %-14s %-10s %-14s %s" %
          ("L", "MAXNORM", "log2", "TIGHTEMPTY", "AMGM=min(2L,4h)^(h/2)"))
    for L in range(1, 2 * h + 1):
        import math
        a = min(2 * L, 4 * h) ** (h // 2)
        print("   %-4d %-14d %-10.3f %-14d %d  (log2 %.3f)" %
              (L, maxnorm[L], math.log2(maxnorm[L]) if maxnorm[L] else 0,
               tight[L], a, math.log2(a)))
    print("   MAXNORM witness at L=%d: %s" % (2 * h, maxnorm_wit[2 * h],))
    print("   TIGHTEMPTY witness at L=%d: %s  (p=%d)" %
          (2 * h, tight_wit[2 * h], tight[2 * h]))

    out = {
        "h": h, "N": N, "kmax": kmax,
        "cost_hist": {str(k): v for k, v in cost_hist.items()},
        "pool": sorted(pool),
        "fp": {str(p): fp(p) for p in sorted(pool)},
        "maxnorm": maxnorm, "tight": tight,
        "maxnorm_wit": maxnorm_wit[2 * h], "tight_wit": tight_wit[2 * h],
        "keep": [[list(d), c, {str(p): list(s) for p, s in sig.items()}]
                 for (d, c, sig) in keep],
    }
    path = __file__.rsplit('/', 1)[0] + "/sweep_h%d.json" % h
    with open(path, "w") as fh:
        json.dump(out, fh)
    print("wrote %s  (|A_%d| = %d)" % (path, kmax, len(keep)))


if __name__ == "__main__":
    main()
