#!/usr/bin/env python3
"""z_n32_band -- round 25.  ALG-1 = BBM (Bucket-Bisect Meet-In-The-Middle).

Registered in PREREG.md section Z1.1 BEFORE implementation.

Reaches N = 32 at sigma ~ 0 (MSTATES = 3^16 = 43,046,721) inside the 1G
ceiling by cutting MITM *memory* by a factor RBUCK without paying RBUCK
enumerations: buckets are CONTIGUOUS residue intervals, so for a fixed
first-octet partial sum the second-octet partials that land in a bucket
form at most two CONTIGUOUS ranges of the sorted table, found by bisect.
Sum over buckets of the work is therefore one enumeration, not RBUCK.

Half 2's columns are NEGATED, so the join condition s1 + s2 = 0 becomes
s1 = s2' and no negation-symmetry theorem is used for correctness.

Run ONLY via  tools/ramguard local -- python3 ...  from repo root.
Stdlib only.
"""
import os
import sys
from bisect import bisect_left
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
Z24 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "pilots_20260808", "z_ceiling_assault")
sys.path.insert(0, os.path.abspath(Z24))
from zcore import (is_prime, elt_of_order, rows_M2, rows_M4,   # noqa: E402
                   assert_2power_grid, tmass_exact, primes_upto)

CNTBASE = 1 << 40
CNTMASK = CNTBASE - 1


# ------------------------------------------------------------------ packing
def swar_params(p, kappa):
    """field width W with 2^(W-1) > p, guard/carry constants for kappa fields."""
    W = 1
    while (1 << (W - 1)) <= p:
        W += 1
    G = 0
    K = 0
    for i in range(kappa):
        G |= (1 << (W - 1)) << (W * i)
        K |= ((1 << (W - 1)) - p) << (W * i)
    return W, G, K


def pack(vec, W, kappa):
    """coordinate 0 in the HIGHEST field, so packed order = lexicographic order."""
    v = 0
    for i in range(kappa):
        v |= vec[i] << (W * (kappa - 1 - i))
    return v


# ------------------------------------------------------------------ tables
def build_table(cols, p, kappa, W, G, K):
    """all 3^len(cols) partial sums as (packed_key, mass) with mass = 2^(n-wt)."""
    cur = [(0, 1)]
    for c in cols:
        if kappa == 1:
            nxt = []
            ap = nxt.append
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
            cur = nxt
        else:
            cpk = pack(c, W, kappa)
            cnk = pack([(-x) % p for x in c], W, kappa)
            nxt = []
            ap = nxt.append
            for kv, m in cur:
                ap((kv, 2 * m))
                s = kv + cpk
                s -= (((s + K) & G) >> (W - 1)) * p
                ap((s, m))
                s = kv + cnk
                s -= (((s + K) & G) >> (W - 1)) * p
                ap((s, m))
            cur = nxt
    return cur


def split_table(tab):
    tab.sort()
    return [t[0] for t in tab], tab


def _ranges(lo, hi, pv, mod):
    """{q : (pv + q) mod `mod` in [lo,hi)}  as 1-2 contiguous [s,e) ranges."""
    a = lo - pv
    b = hi - pv
    if a < 0:
        a += mod
        b += mod
    if b <= mod:
        return ((a, b),)
    return ((a, mod), (0, b - mod))


# ------------------------------------------------------------------ the cell
def bbm(rows, p, rbuck=256, ckpt=None, verbose=False, hi_hook=None):
    """EXACT (TNUM, NKER) for the cell with these parity-check rows.

    TNUM = 2^N * TMASS is an integer;  NKER = |ker cap ternary| (0 included).
    Memory: one dict of ~3^(N/4)^2 / rbuck entries.
    """
    kappa = len(rows)
    N = len(rows[0])
    assert N % 4 == 0
    h = N // 2
    q = h // 2
    W, G, K = swar_params(p, kappa)
    top = p << (W * (kappa - 1))          # bucket key-space = first coordinate

    def cols_of(idxs, neg):
        out = []
        for j in idxs:
            v = [rows[i][j] % p for i in range(kappa)]
            if neg:
                v = [(-x) % p for x in v]
            out.append(v[0] if kappa == 1 else v)
        return out

    c1a = cols_of(range(0, q), False)
    c1b = cols_of(range(q, h), False)
    c2a = cols_of(range(h, h + q), True)
    c2b = cols_of(range(h + q, N), True)

    P1 = build_table(c1a, p, kappa, W, G, K)
    Q1k, Q1 = split_table(build_table(c1b, p, kappa, W, G, K))
    P2 = build_table(c2a, p, kappa, W, G, K)
    Q2k, Q2 = split_table(build_table(c2b, p, kappa, W, G, K))

    done = {}
    if ckpt and os.path.exists(ckpt):
        for ln in open(ckpt):
            f = ln.split()
            if len(f) == 3:
                done[int(f[0])] = (int(f[1]), int(f[2]))

    tnum = 0
    nker = 0
    dpeak = 0
    shift = W * (kappa - 1)
    Wm1 = W - 1
    for b in range(rbuck):
        if b in done:
            tnum += done[b][0]
            nker += done[b][1]
            continue
        lo = (b * p) // rbuck
        hi = ((b + 1) * p) // rbuck
        if lo == hi:
            continue
        LO = lo << shift
        HI = hi << shift
        D = {}
        Dg = D.get
        # ---- fill: half-1 partial sums landing in bucket [lo,hi)
        for pv, pm in P1:
            pv1 = pv >> shift
            pms = pm << 40
            for (s, e) in _ranges(lo, hi, pv1, p):
                i0 = bisect_left(Q1k, s << shift)
                i1 = bisect_left(Q1k, e << shift)
                if i0 == i1:
                    continue
                if kappa == 1:
                    for kv, m in Q1[i0:i1]:
                        r = pv + kv
                        if r >= p:
                            r -= p
                        D[r] = Dg(r, 0) + pms * m + 1
                else:
                    for kv, m in Q1[i0:i1]:
                        r = pv + kv
                        r -= (((r + K) & G) >> Wm1) * p
                        D[r] = Dg(r, 0) + pms * m + 1
        if len(D) > dpeak:
            dpeak = len(D)
        # ---- probe: half-2 (negated) partial sums landing in the same bucket
        tb = 0
        nb = 0
        for pv, pm in P2:
            pv1 = pv >> shift
            for (s, e) in _ranges(lo, hi, pv1, p):
                i0 = bisect_left(Q2k, s << shift)
                i1 = bisect_left(Q2k, e << shift)
                if i0 == i1:
                    continue
                if kappa == 1:
                    for kv, m in Q2[i0:i1]:
                        r = pv + kv
                        if r >= p:
                            r -= p
                        v = Dg(r)
                        if v is not None:
                            tb += pm * m * (v >> 40)
                            nb += v & CNTMASK
                else:
                    for kv, m in Q2[i0:i1]:
                        r = pv + kv
                        r -= (((r + K) & G) >> Wm1) * p
                        v = Dg(r)
                        if v is not None:
                            tb += pm * m * (v >> 40)
                            nb += v & CNTMASK
        del D
        tnum += tb
        nker += nb
        if ckpt:
            with open(ckpt, "a") as fh:
                fh.write("%d %d %d\n" % (b, tb, nb))
        if verbose and (b % 32 == 0):
            print("   bucket %4d/%d  dpeak=%d  tnum=%d" % (b, rbuck, dpeak, tnum),
                  flush=True)
        if hi_hook:
            hi_hook(b, dpeak)
    return tnum, nker, dpeak


def record(rows, p, tnum, nker, family, tag=""):
    import math
    kappa = len(rows)
    N = len(rows[0])
    tm = Fraction(tnum, 1 << N)
    H = Fraction((1 << N) - 1, p ** kappa)
    d = dict(family=family, N=N, kappa=kappa, p=p, TNUM=tnum, NKER=nker,
             TMASS=tm, TMASSf=float(tm), H=float(H),
             CRATIO=float(tm / (1 + H)),
             EXCESS=float((tm - 1) / H) if H else 0.0,
             SIGMA=N - kappa * math.log2(p),
             ZFRATIO=float(tm * p ** kappa) / float(1 << N),
             ZFLOOR_OK=(tm >= Fraction(1 << N, p ** kappa)), tag=tag)
    return d


HDR = ("family N kappa p SIGMA TNUM NKER TMASSf CRATIO EXCESS ZFRATIO "
       "ZFLOOR_OK tag").split()


def tsv_line(d):
    return "\t".join(str(d[k]) for k in HDR)
