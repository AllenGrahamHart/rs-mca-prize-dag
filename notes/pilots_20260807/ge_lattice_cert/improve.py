#!/usr/bin/env python3
"""Basis-quality experiment: does deep-insertion LLL cut FPEST enough to be
worth restarting an enumeration?  Writes state/CELL.deep.json (a candidate
basis) and prints FPEST before/after.  Never touches CELL.lll.json.

Deep insertion only PERMUTES basis rows, so the result is still a basis of
the same lattice -- DETCHECK/MEMBERCHECK are re-run regardless.
"""
import json
import math
import os
import sys
import time
from fractions import Fraction

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import latlib as LL                                       # noqa: E402
from estimate import est                                  # noqa: E402

STATE = os.path.join(HERE, "state")
SOFT = float(os.environ.get("GEL_SOFT", "225"))


def gso_from(B, d, lam, start):
    """Recompute the integral GSO for rows >= start, keeping d[0..start] and
    lam[i][*] for i < start."""
    n = len(B)
    for k in range(start, n):
        for j in range(k + 1):
            u = LL.dot(B[k], B[j])
            for i in range(j):
                u = (d[i + 1] * u - lam[k][i] * lam[j][i]) // d[i]
            if j < k:
                lam[k][j] = u
            else:
                d[k + 1] = u
    return d, lam


def profile(B):
    d, lam = LL.integral_gso(B)
    return [math.log2(d[i + 1]) - math.log2(d[i]) for i in range(len(B))]


def deep_lll(B, delta=Fraction(99, 100), deadline=None, k0=1, log=print):
    n = len(B)
    d, lam = LL.integral_gso(B)
    k = k0
    ins = 0
    while k < n:
        if deadline and time.time() > deadline:
            return B, k, ins, 'RUNNING'
        for l in range(k - 1, -1, -1):
            if 2 * abs(lam[k][l]) > d[l + 1]:
                q = LL.nint(lam[k][l], d[l + 1])
                Bl = B[l]
                B[k] = [B[k][t] - q * Bl[t] for t in range(n)]
                lam[k][l] -= q * d[l + 1]
                for i in range(l):
                    lam[k][i] -= q * lam[l][i]
        c = Fraction(LL.dot(B[k], B[k]))
        i = 0
        while i < k:
            bi = Fraction(d[i + 1], d[i])
            if c >= delta * bi:
                mu = Fraction(lam[k][i], d[i + 1])
                c -= mu * mu * bi
                i += 1
            else:
                break
        if i < k:
            row = B.pop(k)
            B.insert(i, row)
            gso_from(B, d, lam, i)
            ins += 1
            k = max(i, 1)
        else:
            k += 1
    return B, k, ins, 'DONE'


def main():
    cid = sys.argv[1]
    src = os.path.join(STATE, "%s.lll.json" % cid)
    dst = os.path.join(STATE, "%s.deep.json" % cid)
    if os.path.exists(dst):
        st = json.load(open(dst))
        B, k0, ins = st["B"], st["k"], st["ins"]
    else:
        B = json.load(open(src))["B"]
        k0, ins = 1, 0
    n = len(B)
    R = math.sqrt(4 * n)
    base = profile(json.load(open(src))["B"])
    t0, pk0, _ = est(base, R)
    t_start = time.time()
    B, k, ni, status = deep_lll(B, deadline=time.time() + SOFT, k0=k0,
                                log=print)
    ins += ni
    json.dump({"B": B, "k": k, "ins": ins}, open(dst, "w"))
    prof = profile(B)
    t1, pk1, _ = est(prof, R)
    d, lam = LL.integral_gso(B)
    det = LL.isqrt(d[n])
    b0 = min(LL.dot(r, r) for r in B)
    print("%s  deep-LLL %s: k=%d insertions=%d (%.0f s)"
          % (cid, status, k, ins, time.time() - t_start))
    print("   FPEST before = 2^%.2f (peak k=%d)   after = 2^%.2f (peak k=%d)"
          "   GAIN = %.2f bits (%.1fx)"
          % (t0, pk0[0], t1, pk1[0], t0 - t1, 2 ** (t0 - t1)))
    print("   det^2 == p^2 : %s ; shortest basis vector^2 = %d"
          % (det * det == d[n] and det == json_p(cid), b0))
    print("   GSPROFILE: " + " ".join("%.2f" % t for t in prof))
    print("STATUS: %s" % status)


def json_p(cid):
    import cells as C
    if cid == "E1-128":
        return C.P250
    if cid == "CORRIDOR-128":
        return C.QCORR
    if cid.startswith("PROTH"):
        return C.ALLCELLS[cid]["p"]
    if cid == "PLANT-64":
        return C.P250
    return None


if __name__ == "__main__":
    main()
