#!/usr/bin/env python3
"""z_n32_band -- round 25.  ALG-2 = UMITM (unbalanced meet-in-the-middle).

Registered in PREREG.md section Z1.2 BEFORE implementation.  The INDEPENDENT
verifier for ALG-1 (bbm.py): different split point (18/14, not 16/16), NO
bucketing, a single flat dict, the opposite join direction (the SMALL side is
tabulated and the BIG side is streamed), and a different association order of
the partial sums.  Shares only the column construction and Python integers.

  tools/ramguard local -- python3 notes/pilots_20260809/z_n32_band/umitm.py \
      FAM N KAPPA P [SMALL]
"""
import os
import sys
import time
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
Z24 = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   "..", "..", "pilots_20260808", "z_ceiling_assault"))
sys.path.insert(0, Z24)
from zcore import rows_M2, rows_M4, assert_2power_grid       # noqa: E402

CB = 1 << 40
CM = CB - 1


def _grow(cur, cols, p, kappa, W, G, K):
    for c in cols:
        nxt = []
        ap = nxt.append
        if kappa == 1:
            cn = (p - c) % p
            for kv, m in cur:
                ap((kv, 2 * m))
                a = kv + c
                if a >= p:
                    a -= p
                ap((a, m))
                b = kv + cn
                if b >= p:
                    b -= p
                ap((b, m))
        else:
            cp = 0
            cq = 0
            for i in range(kappa):
                cp |= c[i] << (W * (kappa - 1 - i))
                cq |= ((-c[i]) % p) << (W * (kappa - 1 - i))
            for kv, m in cur:
                ap((kv, 2 * m))
                s = kv + cp
                s -= (((s + K) & G) >> (W - 1)) * p
                ap((s, m))
                s = kv + cq
                s -= (((s + K) & G) >> (W - 1)) * p
                ap((s, m))
        cur = nxt
    return cur


def umitm(rows, p, small=14, verbose=False):
    """EXACT (TNUM, NKER).  Small side tabulated, big side streamed."""
    from bbm import swar_params
    kappa = len(rows)
    N = len(rows[0])
    big = N - small
    W, G, K = swar_params(p, kappa)
    Wm1 = W - 1

    def cols_of(idxs, neg):
        out = []
        for j in idxs:
            v = [rows[i][j] % p for i in range(kappa)]
            if neg:
                v = [(-x) % p for x in v]
            out.append(v[0] if kappa == 1 else v)
        return out

    # small side: columns NEGATED so the streamed big-side residue is the key
    sc = cols_of(range(big, N), True)
    sa, sb = sc[:small // 2], sc[small // 2:]
    A = _grow([(0, 1)], sa, p, kappa, W, G, K)
    B = _grow([(0, 1)], sb, p, kappa, W, G, K)
    D = {}
    Dg = D.get
    for av, am in A:
        ams = am << 40
        if kappa == 1:
            for bv, bm in B:
                r = av + bv
                if r >= p:
                    r -= p
                D[r] = Dg(r, 0) + ams * bm + 1
        else:
            for bv, bm in B:
                r = av + bv
                r -= (((r + K) & G) >> Wm1) * p
                D[r] = Dg(r, 0) + ams * bm + 1
    del A, B
    if verbose:
        print("   small side %d cols -> %d distinct residues" % (small, len(D)),
              flush=True)

    bc = cols_of(range(0, big), False)
    ba, bb = bc[:big // 2], bc[big // 2:]
    P = _grow([(0, 1)], ba, p, kappa, W, G, K)
    Q = _grow([(0, 1)], bb, p, kappa, W, G, K)
    tn = 0
    nk = 0
    t0 = time.time()
    for i, (pv, pm) in enumerate(P):
        if kappa == 1:
            for qv, qm in Q:
                r = pv + qv
                if r >= p:
                    r -= p
                v = Dg(r)
                if v is not None:
                    tn += pm * qm * (v >> 40)
                    nk += v & CM
        else:
            for qv, qm in Q:
                r = pv + qv
                r -= (((r + K) & G) >> Wm1) * p
                v = Dg(r)
                if v is not None:
                    tn += pm * qm * (v >> 40)
                    nk += v & CM
        if verbose and i % 4096 == 0:
            print("   stream %d/%d  %.1fs" % (i, len(P), time.time() - t0), flush=True)
    return tn, nk, len(D)


if __name__ == "__main__":
    fam, N, k, p = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    small = int(sys.argv[5]) if len(sys.argv) > 5 else 14
    assert_2power_grid(N)
    rows = rows_M4(N, p) if fam == "M4" else rows_M2(N, k, p)
    t0 = time.time()
    tn, nk, ns = umitm(rows, p, small=small, verbose=True)
    print("UMITM %s N=%d k=%d p=%d small=%d  TNUM=%d NKER=%d states=%d  %.1fs"
          % (fam, N, k, p, small, tn, nk, ns, time.time() - t0), flush=True)
    print("      TMASS=%s  = %.12f" % (Fraction(tn, 1 << N), tn / float(1 << N)))
