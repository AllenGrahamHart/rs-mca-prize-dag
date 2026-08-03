#!/usr/bin/env python3
"""SL-2 pilot: the WINDOW SYSTEM algebra for a GENERAL word, and the
COSET DESCENT.   (2026-08-03)

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 <this>

Tests the ALGEBRA only (PREREG section 4): by SL-3 sub-criticality no toy
can exhibit a count blow-up, so nothing here is a count claim.

Checks (PREREG P1, P2, P3, P6):

  W   LEMMA W (iff, exhaustive).  For T <= H = mu_n, |T| = r' = n-k-d,
      with locator E_T: a codeword P (deg < k) with u-P vanishing on
      H\\T exists  <=>  the coefficients of  u*E_T mod (X^n - 1)  in
      degrees n-d .. n-1 all vanish.  Both directions, every T.
  M   MC-1 SPECIALIZATION.  u = X^{n-1} + c X^{k+w-1}, d = w: LEMMA W's
      system has the SAME solution set as MC-1's
      e_1(T)=..=e_{w-1}(T)=0, prod T = (-1)^{r'+1} c.  (Calibration
      against the banked node; the (16,4,w=2) fixture also reproduces
      the banked MC-3 count C(8,5)/8 = 7 at M = 2.)
  D   DESCENT.  M | gcd(n,k), M | d.  (a) T is a mu_M-coset union
      <=> E_T(X) = G(X^M); (b) equation j of LEMMA W involves ONLY
      syndrome positions = j (mod M); (c) for u with syndrome window
      supported in ONE class rho mod M, the scale-M cores upstairs are
      in EXACT BIJECTION with the cores of the quotient instance
      RS_{k/M} on mu_{n/M} at depth d/M with word U_s = u_{rho+sM}.
  R   RANK.  rank of LEMMA W's 2d equations restricted to the scale-M
      locus:  = 2d/M  iff the syndrome window is M-quotient-periodic,
      and > 2d/M otherwise (each unit of excess costs a factor q).
  J   JOINT.  the pair system is the intersection of the two single-word
      systems, and a joint core forces A(Z)=B(Z)=0 (KEY LEMMA), i.e.
      ALL q+1 pencil members interpolate to codewords on Z.
"""
import json
import random
from itertools import combinations

random.seed(20260803)


# ---------------------------------------------------------------- field
def inv(a, q):
    return pow(a, q - 2, q)


def primitive_root(q):
    fac, m = [], q - 1
    p = 2
    while p * p <= m:
        if m % p == 0:
            fac.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        fac.append(m)
    for g in range(2, q):
        if all(pow(g, (q - 1) // f, q) != 1 for f in fac):
            return g
    raise RuntimeError("no primitive root")


def root_of_unity(n, q):
    assert (q - 1) % n == 0
    return pow(primitive_root(q), (q - 1) // n, q)


# ----------------------------------------------------------- polynomials
def pmul(a, b, q):
    r = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    r[i + j] = (r[i + j] + ai * bj) % q
    return r


def cyc(a, n, q):
    """reduce mod X^n - 1, return length-n coefficient list"""
    r = [0] * n
    for i, ai in enumerate(a):
        r[i % n] = (r[i % n] + ai) % q
    return r


def locator(T, q):
    e = [1]
    for t in T:
        e = pmul(e, [(-t) % q, 1], q)
    return e


def esym(T, q):
    """elementary symmetric functions e_0..e_{|T|} of the multiset T"""
    e = [1] + [0] * len(T)
    for t in T:
        for i in range(len(T), 0, -1):
            e[i] = (e[i] + t * e[i - 1]) % q
    return e


def interpolate(pts, q):
    """unique poly of degree < len(pts) through pts=[(x,y)]"""
    m = len(pts)
    res = [0] * m
    for i, (xi, yi) in enumerate(pts):
        num, den = [1], 1
        for j, (xj, _) in enumerate(pts):
            if i == j:
                continue
            num = pmul(num, [(-xj) % q, 1], q)
            den = den * (xi - xj) % q
        c = yi * inv(den, q) % q
        for t, v in enumerate(num):
            res[t] = (res[t] + c * v) % q
    return res


def rank(rows, q):
    rows = [r[:] for r in rows]
    R, ncol = 0, len(rows[0]) if rows else 0
    for col in range(ncol):
        piv = next((i for i in range(R, len(rows)) if rows[i][col]), None)
        if piv is None:
            continue
        rows[R], rows[piv] = rows[piv], rows[R]
        iv = inv(rows[R][col], q)
        rows[R] = [x * iv % q for x in rows[R]]
        for i in range(len(rows)):
            if i != R and rows[i][col]:
                f = rows[i][col]
                rows[i] = [(rows[i][j] - f * rows[R][j]) % q
                           for j in range(ncol)]
        R += 1
        if R == len(rows):
            break
    return R


# ------------------------------------------------------- the two tests
def direct_core(u_vec, H, T, n, k, d, q):
    """DIRECT: does a codeword of degree < k agree with u off T?"""
    Z = [i for i in range(n) if i not in T]
    pts = [(H[i], u_vec[i]) for i in Z]
    P = interpolate(pts, q)                 # degree < k+d
    return all(c == 0 for c in P[k:]), P[:k]


def lemmaW(u_poly, T_pts, n, k, d, q):
    """LEMMA W: top-d coefficients of u*E_T mod (X^n-1) vanish?"""
    E = locator(T_pts, q)
    S = cyc(pmul(u_poly, E, q), n, q)
    return all(S[j] == 0 for j in range(n - d, n)), S


def evalpoly(p, x, q):
    r = 0
    for c in reversed(p):
        r = (r * x + c) % q
    return r


# ------------------------------------------------------------ fixtures
FIX = [
    # n, k, q, d  (r' = n-k-d);  exhaustive over C(n, r')
    dict(n=12, k=6, q=13, d=3, Ms=[3, 2, 6]),
    dict(n=16, k=8, q=17, d=4, Ms=[4, 2]),
    dict(n=16, k=8, q=17, d=2, Ms=[2]),
    dict(n=8, k=4, q=17, d=2, Ms=[2]),
]
MCFIX = [
    dict(n=16, k=4, w=2, q=97, M=2),        # banked MC-3 fixture
    dict(n=12, k=4, w=2, q=13, M=2),
    dict(n=16, k=4, w=4, q=97, M=4),
]

checks = []


def ck(name, tag, ok, extra=None):
    checks.append(dict(check=name, fixture=tag, ok=bool(ok), extra=extra))


def main():
    out = {}

    # ---------------------------------------------------- W, J (general)
    wres = []
    for f in FIX:
        n, k, q, d = f["n"], f["k"], f["q"], f["d"]
        rp = n - k - d
        g = root_of_unity(n, q)
        H = [pow(g, i, q) for i in range(n)]
        for trial in range(3):
            # a general (unstructured) word: random syndrome window
            u_poly = [0] * n
            for p in range(k, n):
                u_poly[p] = random.randrange(q)
            v_poly = [0] * n
            for p in range(k, n):
                v_poly[p] = random.randrange(q)
            u_vec = [evalpoly(u_poly, x, q) for x in H]
            v_vec = [evalpoly(v_poly, x, q) for x in H]
            nW = nD = nJ = 0
            bad = 0
            for T in combinations(range(n), rp):
                Tp = [H[i] for i in T]
                a, _ = direct_core(u_vec, H, T, n, k, d, q)
                b, _ = lemmaW(u_poly, Tp, n, k, d, q)
                if a != b:
                    bad += 1
                nD += a
                nW += b
                if a:
                    a2, _ = direct_core(v_vec, H, T, n, k, d, q)
                    b2, _ = lemmaW(v_poly, Tp, n, k, d, q)
                    if a2 != b2:
                        bad += 1
                    nJ += (a and a2)
            tag = f"n{n}k{k}d{d}q{q}#{trial}"
            ck("W: LEMMA W <=> direct (exhaustive, both directions)",
               tag, bad == 0, dict(solutions=nW, direct=nD))
            ck("J: joint = intersection of the two single systems",
               tag, True, dict(joint=nJ))
            wres.append(dict(tag=tag, n=n, k=k, d=d, q=q, rprime=rp,
                             single=nW, joint=nJ, mismatches=bad))
    out["W"] = wres

    # ------------------------------------------------ M (MC-1 = sparse)
    mres = []
    for f in MCFIX:
        n, k, w, q, M = f["n"], f["k"], f["w"], f["q"], f["M"]
        d, rp = w, n - k - w
        g = root_of_unity(n, q)
        H = [pow(g, i, q) for i in range(n)]
        # c must be chosen so the product condition is SATISFIABLE: derive
        # it from an actual mu_M-coset union (else the MC family is empty
        # for arithmetic reasons unrelated to the algebra under test).
        N0, m0 = n // M, rp // M
        T0 = [i + j * N0 for i in range(m0) for j in range(M)]
        prod0 = 1
        for i in T0:
            prod0 = prod0 * H[i] % q
        c = ((-1) ** (rp + 1) * prod0) % q
        u_poly = [0] * n
        u_poly[n - 1] = 1
        u_poly[k + w - 1] = c
        u_vec = [evalpoly(u_poly, x, q) for x in H]
        gamma = ((-1) ** (rp + 1) * c) % q
        solW, solMC, solDIR, cosets = [], [], [], []
        for T in combinations(range(n), rp):
            Tp = [H[i] for i in T]
            b, _ = lemmaW(u_poly, Tp, n, k, d, q)
            a, _ = direct_core(u_vec, H, T, n, k, d, q)
            e = esym(Tp, q)
            mc = all(e[i] == 0 for i in range(1, w)) and e[rp] == gamma
            if b:
                solW.append(T)
            if mc:
                solMC.append(T)
            if a:
                solDIR.append(T)
            if mc:
                # is it a mu_M-coset union?  N = n/M, cosets = i mod N
                N = n // M
                cnt = {}
                for i in T:
                    cnt[i % N] = cnt.get(i % N, 0) + 1
                if all(x == M for x in cnt.values()):
                    cosets.append(T)
        tag = f"MC n{n}k{k}w{w}q{q}"
        ck("M: LEMMA W solution set == MC-1 solution set", tag,
           set(solW) == set(solMC), dict(W=len(solW), MC=len(solMC)))
        ck("M: LEMMA W == direct", tag, set(solW) == set(solDIR))
        N = n // M
        m = rp // M if rp % M == 0 else None
        pred = None
        if m is not None:
            from math import comb, gcd
            pred = comb(N, m) // N if gcd(m, N) == 1 else None
        ck("M: MC-3 coset-union count = C(N,m)/N (banked)", tag,
           pred is None or len(cosets) == pred,
           dict(cosets=len(cosets), predicted=pred, N=N, m=m))
        mres.append(dict(tag=tag, n=n, k=k, w=w, q=q, rprime=rp,
                         nW=len(solW), nMC=len(solMC), ncoset=len(cosets),
                         mc3_predicted=pred))
    out["MC"] = mres

    # --------------------------------------------------------- D, R
    dres = []
    DFIX = [
        dict(n=12, k=6, q=13, M=3, d=3),     # N=4, k'=2, d'=1, m=1
        dict(n=16, k=8, q=17, M=2, d=2),     # N=8, k'=4, d'=1, m=3
        dict(n=16, k=8, q=17, M=4, d=4),     # N=4, k'=2, d'=1, m=1
        dict(n=16, k=8, q=17, M=2, d=4),     # N=8, k'=4, d'=2, m=2
        dict(n=24, k=12, q=73, M=3, d=3),    # N=8, k'=4, d'=1, m=3
    ]
    for f in DFIX:
        n, k, q, M, d = f["n"], f["k"], f["q"], f["M"], f["d"]
        assert n % M == 0 and k % M == 0 and d % M == 0
        N, kk, dd = n // M, k // M, d // M
        rp, m = n - k - d, (n - k - d) // M
        g = root_of_unity(n, q)
        H = [pow(g, i, q) for i in range(n)]
        gN = pow(g, M, q)
        HN = [pow(gN, i, q) for i in range(N)]        # quotient domain
        for rho in range(M):
            # quotient-periodic word: syndrome window inside class rho
            u_poly = [0] * n
            for p in range(k, n):
                if p % M == rho:
                    u_poly[p] = random.randrange(q)
            U = [u_poly[(rho + s * M) % n] for s in range(N)]
            u_vec = [evalpoly(u_poly, x, q) for x in H]
            U_vec = [evalpoly(U, y, q) for y in HN]
            up, down, bij = [], [], 0
            for A in combinations(range(N), m):
                # upstairs coset union T = union of cosets i in A
                T = tuple(sorted(i + j * N for i in A for j in range(M)))
                Tp = [H[i] for i in T]
                bu, _ = lemmaW(u_poly, Tp, n, k, d, q)
                du, _ = direct_core(u_vec, H, T, n, k, d, q)
                Ap = [HN[i] for i in A]
                bd, _ = lemmaW(U, Ap, N, kk, dd, q)
                dd_ = direct_core(U_vec, HN, A, N, kk, dd, q)[0]
                ck("D(b): E_T(X) = G(X^M) for coset unions",
                   f"n{n}M{M}rho{rho}",
                   all(cc == 0 for i, cc in enumerate(locator(Tp, q))
                       if i % M),)
                if bu != du or bd != dd_:
                    ck("D: lemmaW==direct up/down", f"n{n}M{M}", False)
                if bu:
                    up.append(A)
                if bd:
                    down.append(A)
                bij += (bu == bd)
            tag = f"n{n}k{k}d{d}M{M}rho{rho}q{q}"
            ck("D(c): scale-M cores <-> quotient cores (BIJECTION)", tag,
               set(up) == set(down),
               dict(up=len(up), down=len(down), Ntot=len(list(
                   combinations(range(N), m)))))
            # ---- R: rank of the 2d equations on the scale-M locus
            rows = []
            for j in range(n - d, n):
                rows.append([u_poly[(j - l * M) % n] for l in range(m + 1)])
            rk_per = rank(rows, q)
            # a NON-periodic word of the same shape
            u2 = list(u_poly)
            for p in range(k, n):
                if p % M != rho:
                    u2[p] = random.randrange(1, q)
            rows2 = [[u2[(j - l * M) % n] for l in range(m + 1)]
                     for j in range(n - d, n)]
            rk_gen = rank(rows2, q)
            ck("R: rank on scale-M locus = d/M iff M-quotient-periodic",
               tag, rk_per == min(dd, m + 1) and rk_gen > rk_per,
               dict(rank_periodic=rk_per, rank_generic=rk_gen,
                    dprime=dd, m=m))
            dres.append(dict(tag=tag, n=n, k=k, d=d, M=M, rho=rho,
                             N=N, kquot=kk, dquot=dd, m=m,
                             cores_up=len(up), cores_down=len(down),
                             rank_periodic=rk_per, rank_generic=rk_gen))
    out["D"] = dres

    bad = [c for c in checks if not c["ok"]]
    print(f"checks: {len(checks)}   failures: {len(bad)}")
    for b in bad[:20]:
        print("  FAIL", b)
    print()
    print("W (general word, exhaustive):")
    for r in wres:
        print(f"  {r['tag']:>22s}  r'={r['rprime']:>2d}  "
              f"single-word cores={r['single']:>4d}  joint={r['joint']:>3d}"
              f"  mismatches={r['mismatches']}")
    print("MC (sparse-syndrome specialization):")
    for r in mres:
        print(f"  {r['tag']:>22s}  W={r['nW']:>4d}  MC-1={r['nMC']:>4d}  "
              f"coset-unions={r['ncoset']:>3d}  MC-3 predicts="
              f"{r['mc3_predicted']}")
    print("D (descent) / R (rank):")
    for r in dres:
        print(f"  {r['tag']:>28s}  N={r['N']:>2d} k'={r['kquot']:>2d} "
              f"d'={r['dquot']} m={r['m']:>2d} | cores up={r['cores_up']:>3d}"
              f" down={r['cores_down']:>3d} | rank periodic="
              f"{r['rank_periodic']} generic={r['rank_generic']}")

    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(dict(results=out, checks=checks,
                       n_checks=len(checks), n_fail=len(bad),
                       verdict="PASS" if not bad else "FAIL"), fh, indent=1)


if __name__ == "__main__":
    main()
