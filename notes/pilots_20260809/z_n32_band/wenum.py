#!/usr/bin/env python3
"""Low-weight ternary kernel enumerator at N=32 -- UMIN and AU[U] for U <= WCAP.

Same bucket-bisect skeleton as bbm.py, but each dict value is a PACKED COUNT
VECTOR sum_w count_w * 2^(32w) instead of a mass, and half-vectors of weight
> WCAP are dropped.  AU[U] is then EXACT for every U <= WCAP.

Gives P-Z5 (UMIN) and the RC(i) check UMIN >= p^{2/N} at N = 32.

  tools/ramguard local -- python3 wenum.py FAM N KAPPA P [WCAP] [RBUCK]
"""
import os
import sys
import time
from bisect import bisect_left

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bbm import swar_params, _ranges                          # noqa: E402
from zcore import rows_M2, rows_M4, assert_2power_grid        # noqa: E402

FB = 32
FM = (1 << FB) - 1


def table_w(cols, p, kappa, W, G, K, wcap):
    """(key, weight) for every ternary vector on `cols` of weight <= wcap."""
    cur = [(0, 0)]
    n = len(cols)
    for t, c in enumerate(cols):
        left = n - t - 1
        nxt = []
        ap = nxt.append
        if kappa == 1:
            cn = (p - c) % p
            for kv, w in cur:
                ap((kv, w))
                if w + 1 <= wcap:
                    a = kv + c
                    if a >= p:
                        a -= p
                    ap((a, w + 1))
                    b = kv + cn
                    if b >= p:
                        b -= p
                    ap((b, w + 1))
            cur = nxt
        else:
            cp = cq = 0
            for i in range(kappa):
                cp |= c[i] << (W * (kappa - 1 - i))
                cq |= ((-c[i]) % p) << (W * (kappa - 1 - i))
            for kv, w in cur:
                ap((kv, w))
                if w + 1 <= wcap:
                    s = kv + cp
                    s -= (((s + K) & G) >> (W - 1)) * p
                    ap((s, w + 1))
                    s = kv + cq
                    s -= (((s + K) & G) >> (W - 1)) * p
                    ap((s, w + 1))
            cur = nxt
    return cur


def wenum(rows, p, wcap=12, rbuck=256, verbose=False):
    kappa = len(rows)
    N = len(rows[0])
    h = N // 2
    q = h // 2
    W, G, K = swar_params(p, kappa)
    shift = W * (kappa - 1)
    Wm1 = W - 1
    POW = [1 << (FB * w) for w in range(2 * wcap + 2)]

    def cols_of(idxs, neg):
        out = []
        for j in idxs:
            v = [rows[i][j] % p for i in range(kappa)]
            if neg:
                v = [(-x) % p for x in v]
            out.append(v[0] if kappa == 1 else v)
        return out

    P1 = table_w(cols_of(range(0, q), False), p, kappa, W, G, K, wcap)
    Q1 = sorted(table_w(cols_of(range(q, h), False), p, kappa, W, G, K, wcap))
    Q1k = [t[0] for t in Q1]
    P2 = table_w(cols_of(range(h, h + q), True), p, kappa, W, G, K, wcap)
    Q2 = sorted(table_w(cols_of(range(h + q, N), True), p, kappa, W, G, K, wcap))
    Q2k = [t[0] for t in Q2]
    acc = 0
    for b in range(rbuck):
        lo = (b * p) // rbuck
        hi = ((b + 1) * p) // rbuck
        if lo == hi:
            continue
        D = {}
        Dg = D.get
        for pv, pw in P1:
            pv1 = pv >> shift
            for (s, e) in _ranges(lo, hi, pv1, p):
                i0 = bisect_left(Q1k, s << shift)
                i1 = bisect_left(Q1k, e << shift)
                for kv, kw in Q1[i0:i1]:
                    w = pw + kw
                    if w > wcap:
                        continue
                    r = pv + kv
                    if kappa == 1:
                        if r >= p:
                            r -= p
                    else:
                        r -= (((r + K) & G) >> Wm1) * p
                    D[r] = Dg(r, 0) + POW[w]
        for pv, pw in P2:
            pv1 = pv >> shift
            for (s, e) in _ranges(lo, hi, pv1, p):
                i0 = bisect_left(Q2k, s << shift)
                i1 = bisect_left(Q2k, e << shift)
                for kv, kw in Q2[i0:i1]:
                    w = pw + kw
                    if w > wcap:
                        continue
                    r = pv + kv
                    if kappa == 1:
                        if r >= p:
                            r -= p
                    else:
                        r -= (((r + K) & G) >> Wm1) * p
                    v = Dg(r)
                    if v is not None:
                        acc += v << (FB * w)
        del D
        if verbose and b % 64 == 0:
            print("   bucket %d/%d" % (b, rbuck), flush=True)
    AU = []
    for u in range(2 * wcap + 1):
        AU.append((acc >> (FB * u)) & FM)
    return AU


if __name__ == "__main__":
    fam, N, k, p = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    wcap = int(sys.argv[5]) if len(sys.argv) > 5 else 12
    rb = int(sys.argv[6]) if len(sys.argv) > 6 else 256
    assert_2power_grid(N)
    rows = rows_M4(N, p) if fam == "M4" else rows_M2(N, k, p)
    t0 = time.time()
    AU = wenum(rows, p, wcap=wcap, rbuck=rb, verbose=True)
    umin = next((u for u in range(1, wcap + 1) if AU[u]), None)
    lb = p ** (2.0 / N)
    print("WENUM %s N=%d k=%d p=%d WCAP=%d   %.1fs" % (fam, N, k, p, wcap,
                                                       time.time() - t0))
    print("  AU[U] EXACT for U <= %d :  %s" % (wcap,
          ", ".join("%d:%d" % (u, AU[u]) for u in range(wcap + 1) if AU[u])))
    print("  UMIN = %s ;  RC(i) lower bound p^{2/N} = %.4f ;  RC(i) %s" %
          (umin, lb, "HOLDS" if (umin is None or umin >= lb) else "VIOLATED"))
    print("  partial (splits capped at %d each) for U in [%d, %d]: %s" %
          (wcap, wcap + 1, 2 * wcap,
           ", ".join("%d:%d" % (u, AU[u]) for u in range(wcap + 1, 2 * wcap + 1))))
