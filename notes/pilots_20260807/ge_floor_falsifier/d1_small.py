#!/usr/bin/env python3
"""D1 FALSIFIER SEARCH -- the ESCAPE-RATE curve L_k(N').

L_k(N') = max |F|, F subset of C(N'), such that every nonzero pairwise
difference has its ideal supported on {lambda} u T for ONE fixed set T of at
most k ODD prime ideals.  L_0 = round-21's FLOOR-GE / MAXPOW2.
k >= 1 is exactly ESCAPE-GE's named class (the only class that can beat the
floor), so this IS the pre-registered falsifier search.

At N' = 8 the search is EXHAUSTIVE in centers AND in ideal subsets.
"""
import itertools
import json
import sys

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from gelib import centers, max_clique


def main():
    h = int(sys.argv[1])
    kmax = int(sys.argv[2])
    topn = int(sys.argv[3]) if len(sys.argv) > 3 else 0   # 0 = all ideals
    N = 2 * h
    data = json.load(open(__file__.rsplit('/', 1)[0] + "/sweep_h%d.json" % h))

    A0 = []
    groups = {}
    for d, c, sig in data["keep"]:
        d = tuple(d)
        if c == 0:
            A0.append(d)
        elif c == 1:
            (p, s), = sig.items()
            groups.setdefault((int(p), tuple(s)), []).append(d)
    ideals = sorted(groups, key=lambda k: (-len(groups[k]), k[0]))
    if topn:
        ideals = ideals[:topn]
    C = centers(h)
    cidx = {c: i for i, c in enumerate(C)}
    n = len(C)

    def adj_from(conn):
        adj = [set() for _ in range(n)]
        for i, c in enumerate(C):
            for dd in conn:
                q = tuple(c[j] + dd[j] for j in range(h))
                j2 = cidx.get(q)
                if j2 is not None and j2 != i:
                    adj[i].add(j2)
        return adj

    print("== D1 ESCAPE-RATE, N' = %d (h = %d) ==" % (N, h))
    print("|C(N')| = %d   |A_0| = %d   single odd ideals used: %d%s"
          % (n, len(A0), len(ideals),
             "  (TOP-%d subset -> SEARCHED, not exhaustive)" % topn if topn
             else "  (ALL -> exhaustive in T)"))

    adj0 = adj_from(A0)
    adjt = {}
    for t in ideals:
        adjt[t] = adj_from(groups[t])

    results = {}
    for k in range(0, kmax + 1):
        best = 0
        bestT = None
        bestwit = None
        nsub = 0
        for T in itertools.combinations(ideals, k):
            nsub += 1
            adj = [set(adj0[i]) for i in range(n)]
            for t in T:
                at = adjt[t]
                for i in range(n):
                    if at[i]:
                        adj[i] |= at[i]
            size, wit, complete = max_clique(adj, range(n))
            assert complete
            if size > best:
                best = size
                bestT = T
                bestwit = wit
        results[k] = best
        print("L_%d = %-4d  [%d ideal subsets, exhaustive-in-T]   "
              "N'+1 = %d   registered bound (k+1)(N'+1) = %d   %s"
              % (k, best, nsub, N + 1, (k + 1) * (N + 1),
                 "OK" if best <= (k + 1) * (N + 1) else "*** H2 FALSIFIED ***"))
        if bestT:
            print("     T = %s" % ([(t[0], t[1]) for t in bestT],))
        if bestwit and k <= 2:
            print("     witness: %s" % ([C[i] for i in bestwit],))

    print("\n-- ESCAPE-RATE curve, N' = %d --" % N)
    print("   %-4s %-7s %-10s %-12s" % ("k", "L_k", "GAIN(k)", "centers/ideal"))
    for k in range(0, kmax + 1):
        g = results[k] - results[0]
        print("   %-4d %-7d %-10d %-12s" %
              (k, results[k], g, ("%.3f" % (g / k)) if k else "-"))


if __name__ == "__main__":
    main()
