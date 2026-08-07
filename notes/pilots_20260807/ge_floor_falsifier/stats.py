#!/usr/bin/env python3
"""Ideal-group statistics at h, plus KMIN of explicit candidate families.

KMIN(F) := the exact number of distinct odd prime IDEALS needed to certify F
           (= |union over pairs of the odd ideal support of f - f'|).
This prices a NAMED family directly, with no clique search.
"""
import itertools
import json
import sys

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from gelib import (tower_norm, sigma, mult_order, spf_sieve, factor_with, plcm)


def kmin(F, h, spf, verbose=""):
    """Exact odd-ideal cost of a family F (list of integer vectors)."""
    N = 2 * h
    lcms = {}
    seen_d = set()
    maxnorm = 0
    for i in range(len(F)):
        for j in range(i + 1, len(F)):
            d = tuple(F[i][t] - F[j][t] for t in range(h))
            if d in seen_d:
                continue
            seen_d.add(d)
            nm = abs(tower_norm(list(d)))
            if nm > maxnorm:
                maxnorm = nm
            o = nm
            while o % 2 == 0:
                o //= 2
            if o == 1:
                continue
            for p in factor_with(spf, o):
                s = sigma(d, p, h)
                lcms[p] = plcm(lcms.get(p, ()), s, p) if p in lcms else s
    cost = 0
    for p, s in lcms.items():
        f = mult_order(p, N)
        cost += (len(s) - 1) // f
    if verbose:
        print("   %s: |F| = %d, distinct differences = %d, odd rational primes"
              " = %d, KMIN = %d odd ideals, max|Norm| = %d"
              % (verbose, len(F), len(seen_d), len(lcms), cost, maxnorm))
    return cost, len(lcms)


def main():
    h = int(sys.argv[1])
    N = 2 * h
    path = __file__.rsplit('/', 1)[0] + "/sweep_h%d.json" % h
    data = json.load(open(path))
    groups = {}
    n0 = 0
    for d, c, sig in data["keep"]:
        if c == 0:
            n0 += 1
        elif c == 1:
            (p, s), = sig.items()
            groups.setdefault((int(p), tuple(s)), []).append(tuple(d))
    sizes = sorted((len(v) for v in groups.values()), reverse=True)
    print("== IDEAL GROUPS, N' = %d ==" % N)
    print("|A_0| = %d ; distinct single-ideal groups = %d" % (n0, len(groups)))
    print("|Delta_pi| top 20: %s" % sizes[:20])
    print("|Delta_pi| >= 100: %d ideals ; >= 32: %d ; >= 8: %d ; total diffs "
          "with cost 1 = %d" %
          (sum(1 for s in sizes if s >= 100), sum(1 for s in sizes if s >= 32),
           sum(1 for s in sizes if s >= 8), sum(sizes)))
    byp = {}
    for (p, s), v in groups.items():
        byp[p] = byp.get(p, 0) + len(v)
    top = sorted(byp.items(), key=lambda t: -t[1])[:12]
    print("by rational prime (p, #cost-1 diffs): %s" % top)

    # ---- named families
    spf = spf_sieve(1 << 21)
    print("\n== KMIN of NAMED families (exact odd-ideal price) ==")
    zero = tuple([0] * h)

    # (i) round-21's extremal 2-adic family {0} u orbit(1+x)
    c = [0] * h
    c[0] = 1
    c[1] = 1
    orb = []
    cur = list(c)
    for _ in range(h):
        orb.append(tuple(cur))
        orb.append(tuple(-t for t in cur))
        cur = [-cur[h - 1]] + cur[:h - 1]
    F = [zero] + sorted(set(orb))
    kmin(F, h, spf, "FLOOR-GE extremal  {0} u orbit(1+x)")

    # (ii) the all-signs family {0} u {+-1}^h  -- size 2^h + 1
    F2 = [zero] + [v for v in itertools.product((-1, 1), repeat=h)]
    kmin(F2, h, spf, "ALL-SIGNS          {0} u {+-1}^h")

    # (iii) sub-cubes of the all-signs family: fix the last h-m coordinates
    for m in range(1, h + 1):
        F3 = [zero] + [tuple(list(v) + [1] * (h - m))
                       for v in itertools.product((-1, 1), repeat=m)]
        k, np = kmin(F3, h, spf)
        print("   SUBCUBE m=%-2d  |F| = %-6d  KMIN = %-5d odd ideals "
              "(%d rational primes)" % (m, len(F3), k, np))


if __name__ == "__main__":
    main()
