#!/usr/bin/env python3
"""D1 at N' = 16.  Edges are bucketed by ideal label in ONE pass over center
pairs, so each ideal subset T costs only a set union + a clique search.

Symmetry: the unit group <+-x> (order 2h) acts on C(N') and preserves every
ideal support, so a maximum clique may be assumed to contain an ORBIT
REPRESENTATIVE.  We therefore compute  max over reps v of 1 + omega(N(v)),
which is exact and 2h times cheaper at the root.
"""
import itertools
import json
import sys
import time
import functools
print = functools.partial(print, flush=True)

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from gelib import centers, max_clique


def main():
    h = int(sys.argv[1])
    kmax = int(sys.argv[2])
    topn = int(sys.argv[3]) if len(sys.argv) > 3 else 24
    budget = int(sys.argv[4]) if len(sys.argv) > 4 else 300000
    N = 2 * h
    data = json.load(open(__file__.rsplit('/', 1)[0] + "/sweep_h%d.json" % h))

    label = {}
    groups = {}
    for d, c, sig in data["keep"]:
        d = tuple(d)
        if c == 0:
            label[d] = 0
        elif c == 1:
            (p, s), = sig.items()
            groups.setdefault((int(p), tuple(s)), []).append(d)
    ideals = sorted(groups, key=lambda k: (-len(groups[k]), k[0]))[:topn]
    for gi, t in enumerate(ideals):
        for d in groups[t]:
            label[d] = gi + 1

    C = centers(h)
    n = len(C)
    cidx = {c: i for i, c in enumerate(C)}
    print("== D1 at N' = %d ==  |C| = %d, |A_0| = %d, ideals carried = %d"
          % (N, n, sum(1 for v in label.values() if v == 0), len(ideals)))
    for t in ideals[:8]:
        print("   ideal p=%-6d |Delta| = %d" % (t[0], len(groups[t])))

    t0 = time.time()
    buckets = [[] for _ in range(len(ideals) + 1)]
    for i in range(n):
        ci = C[i]
        for j in range(i + 1, n):
            cj = C[j]
            d = tuple(ci[t] - cj[t] for t in range(h))
            g = label.get(d)
            if g is not None:
                buckets[g].append((i, j))
    print("edge bucketing done in %.1fs: |E_0| = %d, sum |E_ideal| = %d"
          % (time.time() - t0, len(buckets[0]), sum(len(b) for b in buckets[1:])))

    # unit-group orbit representatives
    def shift(v):
        return tuple([-v[h - 1]] + list(v[:h - 1]))
    reps = []
    seen = set()
    for i, c in enumerate(C):
        if i in seen:
            continue
        reps.append(i)
        cur = c
        for _ in range(h):
            seen.add(cidx[cur])
            seen.add(cidx[tuple(-t for t in cur)])
            cur = shift(cur)
    print("unit-orbit representatives: %d (of %d centers)" % (len(reps), n))

    def build(T):
        adj = [set() for _ in range(n)]
        for g in (0,) + tuple(gi + 1 for gi in T):
            for (i, j) in buckets[g]:
                adj[i].add(j)
                adj[j].add(i)
        return adj

    def omega(T, lb=0):
        adj = build(T)
        best = lb
        wit = []
        complete = True
        for v in reps:
            P = adj[v]
            if len(P) + 1 <= best:
                continue
            sub = {u: (adj[u] & P) for u in P}
            size, w, comp = max_clique(sub, P, node_budget=budget, lb=best - 1)
            complete = complete and comp
            if size + 1 > best:
                best = size + 1
                wit = [v] + w
        return best, wit, complete

    t0 = time.time()
    b0, w0, c0 = omega(())
    print("\nL_0(%d) = %d  [%s]  N'+1 = %d   (%.1fs)"
          % (N, b0, "EXHAUSTIVE" if c0 else "budget-truncated LOWER bound",
             N + 1, time.time() - t0))
    print("   witness: %s" % ([C[i] for i in w0],))

    # RATIONAL-PRIME mode: T = ALL ideals above one small rational prime p.
    # This is the exact analogue of the N' = 8 winner (T = both primes over 3).
    byp = {}
    for gi, t in enumerate(ideals):
        byp.setdefault(t[0], []).append(gi)
    print("\n-- T = ALL carried ideals above ONE rational prime p --")
    for p in sorted(byp, key=lambda q: -sum(len(groups[ideals[g]])
                                            for g in byp[q]))[:10]:
        T = tuple(byp[p])
        s, w, comp = omega(T, lb=b0)
        nd = sum(len(groups[ideals[g]]) for g in T)
        print("   p = %-6d k = %-3d ideals, %-6d differences -> L = %-4d %s"
              % (p, len(T), nd, s, "EXHAUSTIVE" if comp else "(truncated)"))
        if s > b0:
            print("      *** BEATS THE FLOOR *** witness: %s" %
                  ([C[i] for i in w],))

    for k in range(1, kmax + 1):
        t0 = time.time()
        best, bestT, bestw, allc = b0, None, None, True
        cnt = 0
        for T in itertools.combinations(range(len(ideals)), k):
            cnt += 1
            s, w, comp = omega(T, lb=best)
            allc = allc and comp
            if s > best:
                best, bestT, bestw = s, T, w
        print("L_%d(%d) = %d  [%d subsets over the top-%d ideals -> SEARCHED"
              "%s]  registered bound (k+1)(N'+1) = %d  %s  (%.1fs)"
              % (k, N, best, cnt, len(ideals),
                 "" if allc else ", budget-truncated", (k + 1) * (N + 1),
                 "OK" if best <= (k + 1) * (N + 1) else "*** H2 FALSIFIED ***",
                 time.time() - t0))
        if bestT is not None:
            print("   T = %s" % ([ideals[i] for i in bestT],))
            print("   witness: %s" % ([C[i] for i in bestw],))


if __name__ == "__main__":
    main()
