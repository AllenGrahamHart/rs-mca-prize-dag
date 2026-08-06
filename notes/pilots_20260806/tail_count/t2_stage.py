#!/usr/bin/env python3
"""Round 20 -- T2 stage: identify the p=7, w=4 CREATION mechanism."""

import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import t2_lib as L                                            # noqa: E402


def run(CHK, head):
    # ------------------------------------------------------------------
    head("T2/CTRL -- independent replication of the banked I3 censuses")
    # tern_small_scale_laws/PROOFS.md:114 -- n=32, w=2 row
    banked_w2 = {3: 6560, 5: 0, 7: 16640, 17: 148224, 23: 288}
    for p, want in sorted(banked_w2.items()):
        N = 16
        T = L.p_closure([s for s in range(1, 2) if s % 2 == 1], 2 * N, p)
        gf, om = L.primitive_root_of_unity(p, 2 * N)
        cols = L.condition_columns(N, p, T, gf, om)
        W, _ = L.census(N, p, cols)
        tot = sum(W.values())
        CHK("T2/CTRL n=32 w=2 p=%d count = %d" % (p, want), tot == want,
            "got %d" % tot)

    # ------------------------------------------------------------------
    head("T2/CELL -- the p=7, w=4 cell: 288 codewords, weights {7,14}")
    p, N, w = 7, 16, 4
    M = 2 * N
    T = L.p_closure([s for s in range(1, w) if s % 2 == 1], M, p)
    gf, om = L.primitive_root_of_unity(p, M)
    cols = L.condition_columns(N, p, T, gf, om)
    W, vecs = L.census(N, p, cols, want_vectors=True)
    tot = sum(W.values())
    CHK("T2/CELL count = 288", tot == 288, "got %d" % tot)
    CHK("T2/CELL weights = {7,14}", sorted(W) == [7, 14],
        "spectrum %s" % sorted(W.items()))
    CHK("T2/CELL T = <7>-closure of {1,3} mod 32", sorted(T) ==
        [1, 3, 5, 7, 17, 19, 21, 23], "T=%s" % sorted(T))
    print("      |T| = %d, ord_32(7) = %d, F_7-rank of the system = %d"
          % (len(T), gf.k, dim_rank(cols, p)))

    # ------------------------------------------------------------------
    head("T2/H1 -- GENERATOR-COEFFICIENT hypothesis")
    # h(X) = prod_{s in T}(X - omega^s), degree |T| = 8, coefficients in F_7
    h = [gf.one]
    for s in sorted(T):
        r = gf.pw(om, s)
        nh = [gf.zero] * (len(h) + 1)
        for i, a in enumerate(h):
            nh[i + 1] = tuple((x + y) % p for x, y in zip(nh[i + 1], a))
            mr = gf.mul(a, r)
            nh[i] = tuple((x - y) % p for x, y in zip(nh[i], mr))
        h = nh
    in_fp = all(all(c == 0 for c in a[1:]) for a in h)
    hco = [a[0] for a in h]
    CHK("T2/H1a h = prod_{s in T}(X - omega^s) has coefficients in F_7",
        in_fp, "h = %s" % hco)
    print("      h(X) coefficients (const first): %s" % hco)
    sym = [c if c <= p // 2 else c - p for c in hco]
    print("      h(X) in symmetric residues [-3,3]: %s" % sym)
    # PREREG P6/H1 predicted a TERNARY generator.  It is not.  The checks
    # below assert the REFUTATION (fail-closed on the true state).
    CHK("T2/H1b [P6/H1 REFUTED] h is NOT ternary -- my prediction missed",
        not all(abs(c) <= 1 for c in sym), "symmetric coeffs %s" % sym)
    CHK("T2/H1c [P6/H1 REFUTED] wt(h) = 5, not the observed minimum 7",
        sum(1 for c in sym if c) == 5,
        "wt(h) = %d" % sum(1 for c in sym if c))
    CHK("T2/H1e h is a polynomial in X^2 (a CONSEQUENCE of decimation)",
        all(hco[i] == 0 for i in range(1, len(hco), 2)), "h = %s" % hco)

    # every codeword must be a multiple of h in F_7[X]/(X^N+1)  (control)
    def polymulmod(a, b):
        out = [0] * (2 * N)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    out[i + j] = (out[i + j] + x * y) % p
        res = [0] * N
        for i in range(2 * N):
            if i < N:
                res[i] = (res[i] + out[i]) % p
            else:
                res[i - N] = (res[i - N] - out[i]) % p       # negacyclic
        return res

    quotients = []
    okdiv = True
    for v in vecs:
        # divide v by h in F_7[X]/(X^16+1): h is invertible? no -- do long
        # division of v(X) by h(X) as ordinary polynomials (deg v < 16,
        # deg h = 8), then check remainder 0.
        a = [x % p for x in v]
        q = [0] * (N - len(hco) + 1)
        aa = list(a)
        for k in range(len(aa) - 1, len(hco) - 2, -1):
            c = aa[k] * pow(hco[-1], p - 2, p) % p
            q[k - (len(hco) - 1)] = c
            if c:
                for i, y in enumerate(hco):
                    aa[k - (len(hco) - 1) + i] = (
                        aa[k - (len(hco) - 1) + i] - c * y) % p
        if any(aa):
            okdiv = False
        quotients.append(tuple(q))
    CHK("T2/H1d all 288 codewords are ordinary-polynomial multiples of h",
        okdiv, "(definitional control)")
    qsym = set()
    for q in quotients:
        qsym.add(tuple(c if c <= p // 2 else c - p for c in q))
    tern_q = sum(1 for q in qsym if all(abs(c) <= 1 for c in q))
    print("      distinct quotients q = v/h: %d; of these ternary: %d"
          % (len(qsym), tern_q))
    wq = {}
    for q in qsym:
        k = sum(1 for c in q if c)
        wq[k] = wq.get(k, 0) + 1
    print("      quotient weight profile: %s" % sorted(wq.items()))
    print("      sample quotients: %s" % sorted(qsym)[:6])

    # ------------------------------------------------------------------
    head("T2/H4 -- MULTIPLIER hypothesis and the orbit structure")
    orbs = L.orbits(vecs, [L.rot_neg, lambda v: tuple(-x for x in v)])
    CHK("T2/H4a the 288 are closed under negacyclic rotation and negation",
        orbs is not None, "")
    if orbs:
        sizes = sorted(set(len(o) for o in orbs))
        CHK("T2/H4b 9 orbits of size 32 (banked: 9 orbits)",
            len(orbs) == 9 and sizes == [32],
            "orbits=%d sizes=%s" % (len(orbs), sizes))
    stab = [uu for uu in range(1, M, 2)
            if set((uu * s) % M for s in T) == set(T)]
    print("      multiplier stabiliser of T in (Z/32)^*: %s" % stab)

    def mult(uu):
        def f(v):
            out = [0] * N
            for i, x in enumerate(v):
                if x:
                    j = (uu * i) % M
                    if j < N:
                        out[j] = (out[j] + x)
                    else:
                        out[j - N] = (out[j - N] - x)
            return tuple(out)
        return f

    big = L.orbits(vecs, [L.rot_neg, lambda v: tuple(-x for x in v)]
                   + [mult(uu) for uu in stab if uu != 1])
    if big is None:
        CHK("T2/H4c the 288 are closed under the T-stabiliser multipliers",
            False, "NOT closed")
    else:
        CHK("T2/H4c the 288 are closed under the T-stabiliser multipliers",
            True, "orbits under the full group: %d, sizes %s"
            % (len(big), sorted(set(len(o) for o in big))))

    # ------------------------------------------------------------------
    head("T2/H5 -- THE MECHANISM: decimation + composition (THEOREM 13)")
    w7 = [v for v in vecs if sum(1 for x in v if x) == 7]
    w14 = [v for v in vecs if sum(1 for x in v if x) == 14]
    ev = [v for v in w7 if all(v[i] == 0 for i in range(1, N, 2))]
    od = [v for v in w7 if all(v[i] == 0 for i in range(0, N, 2))]
    CHK("T2/H5a every weight-7 codeword is DECIMATED (even- or odd-only)",
        len(ev) + len(od) == len(w7) == 32,
        "even %d, odd %d, mixed %d" % (len(ev), len(od),
                                       len(w7) - len(ev) - len(od)))
    Tm = sorted(set(s % N for s in T))
    CHK("T2/H5b T mod 16 collapses 8 -> 4 (the rank-collapse cause)",
        len(Tm) == 4 and Tm == [1, 3, 5, 7], "T mod 16 = %s" % Tm)
    colsE = [cols[i] for i in range(0, N, 2)]
    rkE = dim_rank(colsE, p)
    CHK("T2/H5c even-sublattice system has rank 4 (not 8): dim 4",
        rkE == 4 and len(colsE) - rkE == 4,
        "length %d rank %d dim %d" % (len(colsE), rkE, len(colsE) - rkE))
    sums = set()
    for a in ev:
        for b in od:
            sums.add(tuple(x + y for x, y in zip(a, b)))
    CHK("T2/H5d the weight-14 stratum IS exactly {even + odd} (16x16=256)",
        sums == set(w14) and len(sums) == 256,
        "|sums| = %d, |w14| = %d, equal = %s"
        % (len(sums), len(w14), sums == set(w14)))
    CHK("T2/H5e 288 = 16 + 16 + 16*16 exactly",
        len(ev) + len(od) + len(ev) * len(od) == 288, "")
    from math import comb
    print("      LEDGER: flat+TWT whole cell = %.4f" %
          ((comb(16, 7) * 2 ** 7 + comb(16, 14) * 2 ** 14) / 7 ** 8))
    print("        even-w7: flat %.6g -> after decimation %.4f -> per"
          " 16-orbit %.4f orbits -> MEASURED %d words (1 orbit)"
          % (comb(8, 7) * 2 ** 7 / 7 ** 8, comb(8, 7) * 2 ** 7 / 7 ** 4,
             comb(8, 7) * 2 ** 7 / 7 ** 4 / 16, len(ev)))
    print("        w14:     flat %.4f -> FORCED by composition = %d"
          % (comb(8, 7) ** 2 * 2 ** 14 / 7 ** 8, len(ev) * len(od)))

    head("T2/H6 -- why p=7 and nothing else: cross-p scan of the"
         " DECIMATED cell CT(8,p,{1,3,5,7} mod 16)")
    rows = []
    for q in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47):
        Tq = L.p_closure([1, 3, 5, 7], 16, q)
        gq, oq = L.primitive_root_of_unity(q, 16)
        cq = L.condition_columns(8, q, Tq, gq, oq)
        Wq, _v = L.census(8, q, cq)
        rk = dim_rank(cq, q)
        rows.append((q, len(Tq), rk, sum(Wq.values()), sorted(Wq)))
        print("      p=%-3d |T mod16|=%d rank=%-2d dim=%d ternary=%-5d"
              " weights=%s" % (q, len(Tq), rk, 8 - rk, sum(Wq.values()),
                               sorted(Wq)))
    collapse = [r for r in rows if r[2] < 8]
    CHK("T2/H6a the rank collapse happens only for ord_16(p) = 2",
        sorted(r[0] for r in collapse) == [7, 17, 23],
        "collapsed at p = %s" % [r[0] for r in collapse])
    CHK("T2/H6b among those, only p=7 admits a ternary word (TWT: p<=8)",
        [r[0] for r in collapse if r[3] > 0] == [7],
        "nonzero counts at p = %s" % [r[0] for r in collapse if r[3] > 0])

    # ------------------------------------------------------------------
    head("T2/H3 -- support structure of the weight-7 codewords")
    sup = sorted(set(tuple(i for i, x in enumerate(v) if x) for v in w7))
    print("      %d weight-7 codewords, %d distinct supports" % (len(w7), len(sup)))
    print("      first supports: %s" % sup[:4])
    diffs = []
    for s0 in sup[:1]:
        dd = {}
        for a in s0:
            for b in s0:
                if a != b:
                    k = (a - b) % N
                    dd[k] = dd.get(k, 0) + 1
        diffs.append(sorted(dd.items()))
    print("      difference multiset of the first support (mod 16): %s"
          % diffs[0])
    # supports as cosets of a subgroup of Z/16?
    cosetish = any(len(set((a - sup[0][0]) % N for a in sup[0])) == 7
                   for _ in [0])
    print("      (a (16,7,lambda) difference set would give a flat"
          " difference multiset; it is %sflat)"
          % ("" if len(set(v for _, v in diffs[0])) == 1 else "NOT "))
    _ = cosetish

    return {"h": hco, "hsym": sym, "quotients": qsym, "T": sorted(T),
            "stab": stab}


def dim_rank(cols, p):
    """rank over F_p of the matrix whose COLUMNS are cols."""
    rows = [[cols[i][j] for i in range(len(cols))]
            for j in range(len(cols[0]))]
    r = 0
    ncol = len(rows[0])
    for c in range(ncol):
        sel = None
        for i in range(r, len(rows)):
            if rows[i][c] % p:
                sel = i
                break
        if sel is None:
            continue
        rows[r], rows[sel] = rows[sel], rows[r]
        inv = pow(rows[r][c], p - 2, p)
        rows[r] = [x * inv % p for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] % p:
                f = rows[i][c]
                rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[r])]
        r += 1
    return r
