#!/usr/bin/env python3
"""Escape tests for the RESSIEVE (round 26, umin_spike_hunt).

E1  necklace generator count == exact necklace formula (N=32 and N=16)
E2  modulus/root: w has exact order 2N, Res recoverable (cap < q)
E3  THEOREM RS on GROUND TRUTH at N=8: the sieve's census over the whole
    admissible band must equal the exhaustive round-23 weight enumerator
    (REF_wenum) cell by cell, for every U <= 7.  This is the IFF.
E4  same at N=16 on a sample (the full-band arm runs in n16.py)
E5  throughput measurement at N=32

  tools/ramguard local -- python3 escape.py
"""
import os
import sys
import time
from math import comb, gcd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rs                                                      # noqa: E402
from zcore import REF_wenum, rows_M4, is_prime                 # noqa: E402

PASS = FAIL = 0


def ck(name, cond, extra=""):
    global PASS, FAIL
    print("%-5s %-56s %s" % ("PASS" if cond else "FAIL", name, extra), flush=True)
    if cond:
        PASS += 1
    else:
        FAIL += 1


def neck_count(N, U):
    tot = 0
    for d in range(1, N + 1):
        if N % d == 0 and U % d == 0:
            # phi(d)
            ph, n, x = d, d, 2
            while x * x <= n:
                if n % x == 0:
                    ph -= ph // x
                    while n % x == 0:
                        n //= x
                x += 1
            if n > 1:
                ph -= ph // n
            tot += ph * comb(N // d, U // d)
    return tot // N


# ---------------------------------------------------------------- E1
def e1():
    for N, Us in ((32, range(1, 10)), (16, range(1, 13))):
        for U in Us:
            got = sum(1 for _ in rs.necklaces(N, U))
            want = neck_count(N, U)
            ck("E1 necklaces N=%d U=%d" % (N, U), got == want,
               "%d == %d" % (got, want))


# ---------------------------------------------------------------- E2
def e2():
    q = rs.find_q(61, 64)
    w = rs.find_w(q, 64)
    ck("E2 q prime, 64 | q-1", is_prime(q) and (q - 1) % 64 == 0, "q=%d" % q)
    ck("E2 ord(w) = 64", pow(w, 32, q) == q - 1 and pow(w, 64, q) == 1)
    ck("E2 cap(U=9,N=32) < q", 9 ** 16 < q, "9^16=%d q=%d" % (9 ** 16, q))
    ck("E2 cap(U=12,N=16) < q", 12 ** 8 < q)
    return q, w


# ------------------------------------------------- E3 / E4 ground-truth arm
def census(N, umax, plo, phi, q, w):
    """{p: {U: AU[U] vector count}} over the whole band, from the sieve."""
    W, Wn = rs.build_roots(N, q, w)
    reps = {}
    tot = 0
    for U in range(1, umax + 1):
        hits, nleaf, ncand, ngcd = rs.sieve_U(N, U, plo, phi, q, W, Wn)
        tot += nleaf
        for (p, UU, S, t) in hits:
            v = rs.verify_hit(N, p, S, t, kappa=1)
            assert v is not None, "hit failed arithmetic re-verification"
            reps.setdefault(p, []).append((UU, v[1]))
    out = {}
    for p, rl in reps.items():
        out[p] = rs.au_from_reps(N, rl)
    return out, tot


def truth(N, plo, phi, umax):
    """exhaustive AU from the round-23/24 reference enumerator, cell by cell."""
    M = 2 * N
    out = {}
    p = plo + (-(plo - 1)) % M
    while p <= phi:
        if is_prime(p):
            AU = REF_wenum(rows_M4(N, p), p) if False else REF_wenum(
                rows_M4(N, p)[0], p)
            d = {U: AU[U] for U in range(1, umax + 1) if AU[U]}
            if d:
                out[p] = d
        p += M
    return out


def e3():
    q, w = rs.find_q(61, 16), None
    q = rs.find_q(61, 16)
    w = rs.find_w(q, 16)
    N, umax = 8, 8          # U<=8 is the COMPLETE enumerator at N=8
    t0 = time.time()
    got, nleaf = census(N, umax, 1 << (N - 2), 1 << (N + 2), q, w)
    want = truth(N, 1 << (N - 2), 1 << (N + 2), umax)
    ck("E3 N=8 IFF: cells with a weight<=7 orbit agree",
       set(got) == set(want),
       "sieve %d cells, truth %d cells, %d leaves, %.1fs"
       % (len(got), len(want), nleaf, time.time() - t0))
    bad = [p for p in set(got) | set(want) if got.get(p) != want.get(p)]
    ck("E3 N=8 IFF: every AU[U] exact", not bad, "mismatches=%s" % bad[:4])


def e4():
    q = rs.find_q(61, 32)
    w = rs.find_w(q, 32)
    N, umax = 16, 12
    t0 = time.time()
    got, nleaf = census(N, umax, 1 << 14, 1 << 18, q, w)
    tg = time.time() - t0
    t0 = time.time()
    want = truth(N, 1 << 14, 1 << 18, umax)
    ck("E4 N=16 IFF over the WHOLE band: cell sets agree",
       set(got) == set(want),
       "sieve %d cells (%d leaves, %.1fs), truth %d cells (%.1fs)"
       % (len(got), nleaf, tg, len(want), time.time() - t0))
    bad = [p for p in set(got) | set(want) if got.get(p) != want.get(p)]
    ck("E4 N=16 IFF: every AU[U], U<=12, exact", not bad,
       "mismatches=%s" % bad[:4])
    import json
    with open(os.path.join(HERE, "N16_CENSUS.json"), "w") as fh:
        json.dump({str(k): {str(a): b for a, b in v.items()}
                   for k, v in got.items()}, fh)
    print("   wrote N16_CENSUS.json (%d cells)" % len(got), flush=True)


def e5():
    q = rs.find_q(61, 64)
    w = rs.find_w(q, 64)
    W, Wn = rs.build_roots(32, q, w)
    for U in (5, 6):
        t0 = time.time()
        hits, nleaf, ncand, ngcd = rs.sieve_U(32, U, 1 << 30, 1 << 34, q, w and W,
                                              Wn)
        dt = time.time() - t0
        print("E5  N=32 U=%d : %d leaves, %d cand, %d hits, %.1fs -> %.2f us/leaf"
              % (U, nleaf, ncand, len(hits), dt, 1e6 * dt / max(nleaf, 1)),
              flush=True)
    ck("E5 throughput measured", True)


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "e1"):
        e1()
    if which in ("all", "e2"):
        e2()
    if which in ("all", "e3"):
        e3()
    if which in ("all", "e4"):
        e4()
    if which in ("all", "e5"):
        e5()
    print("=" * 80)
    print("TOTAL %d PASS / %d FAIL" % (PASS, FAIL))
    sys.exit(1 if FAIL else 0)
