#!/usr/bin/env python3
"""Verifier for xr_mc_depth_quantization.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers, deterministic, no third-party imports, no file reads.

Fresh implementation (independent of mclib/lbt_lib/occlib; pins
cross-checked at draft time against
notes/pilots_20260802/xr_occupancy_v2/mc_c1.json and
notes/pilots_20260802/band_adjudication/checkpoints/band_proper.json):

  A  coset-sharing integer |T ^ T'| <= r' - M (exhaustive)
  B  MC diagonal quantization at (16,4,2,2,q=97) and (20,4,4,4,q=41):
     member agreement EXACTLY k+w, cross pairs <= k, N_d = 0 at every
     band-proper depth, cascade count = C(N,m)/N, line cap saturated
  C  BP(1)/BP(3) exact 2-adic arithmetic at all six rows
  D  BP(2)/BP(3) fixture battery (h = 6 even control, h = 7 odd, h = 5
     cascade) -- productivity, slope confinement, |Gamma| <= n/(h-d)
  E  structured-floor completeness census at (16,8,2,2), q = 65537
"""
from __future__ import annotations

import sys
from itertools import combinations
from math import comb, gcd

sys.dont_write_bytecode = True

FAILURES = []
INF = "inf"


def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    if not ok:
        FAILURES.append(label)


# ------------------------------------------------------------------ field
def primitive_root(q):
    m, fac, t, d = q - 1, [], q - 1, 2
    while d * d <= t:
        if t % d == 0:
            fac.append(d)
            while t % d == 0:
                t //= d
        d += 1
    if t > 1:
        fac.append(t)
    for g in range(2, q):
        if all(pow(g, m // p, q) != 1 for p in fac):
            return g
    raise AssertionError


def make_domain(q, n):
    """H = mu_n inside F_q^* (x0 = 1, beta = 1)."""
    assert (q - 1) % n == 0
    om = pow(primitive_root(q), (q - 1) // n, q)
    H = [pow(om, i, q) for i in range(n)]
    assert len(set(H)) == n
    return H


# ------------------------------------------------------------ polynomials
def trim(c):
    c = list(c)
    while c and c[-1] == 0:
        c.pop()
    return c


def poly_ev(c, x, q):
    acc = 0
    for co in reversed(c):
        acc = (acc * x + co) % q
    return acc


def poly_mul(a, b, q):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    out[i + j] = (out[i + j] + ai * bj) % q
    return out


def vanishing(pts, q):
    m = [1]
    for a in pts:
        m = poly_mul(m, [(-a) % q, 1], q)
    return m


def poly_divmod(a, b, q):
    a, b = trim(a), trim(b)
    out = [0] * max(0, len(a) - len(b) + 1)
    inv = pow(b[-1], q - 2, q)
    while len(a) >= len(b):
        d = len(a) - len(b)
        f = a[-1] * inv % q
        out[d] = f
        for i, bb in enumerate(b):
            a[i + d] = (a[i + d] - f * bb) % q
        a = trim(a)
        if not a:
            break
    return out, a


def mod_xn_minus_1(c, n, q):
    red = [0] * n
    for d, cf in enumerate(c):
        red[d % n] = (red[d % n] + cf) % q
    return red


def interp(xs, ys, q, kcap):
    """degree-<kcap interpolant coefficients (len kcap)."""
    coeff = [0] * kcap
    for i in range(len(xs)):
        num, den = [1], 1
        for j in range(len(xs)):
            if j == i:
                continue
            num = poly_mul(num, [(-xs[j]) % q, 1], q)
            den = den * (xs[i] - xs[j]) % q
        w = ys[i] * pow(den, q - 2, q) % q
        for e in range(min(len(num), kcap)):
            coeff[e] = (coeff[e] + w * num[e]) % q
    return tuple(coeff)


# ------------------------------------------------------------- MC objects
def mc_word(n, k, w, c, q):
    u = [0] * n
    u[n - 1] = 1
    u[k + w - 1] = (u[k + w - 1] + c) % q
    return u


def mc_setup(H, q, n, k, w, M):
    """Return (c, gamma, family) with family = list of index tuples T."""
    rp = n - k - w
    N, m = n // M, rp // M
    cosets = [[i for i in range(n) if i % N == j] for j in range(N)]
    T0 = [i for j in range(m) for i in cosets[j]]
    gamma = 1
    for i in T0:
        gamma = gamma * H[i] % q
    c = ((-1) ** (rp + 1) * gamma) % q
    fam = []
    for S in combinations(range(N), m):
        T = [i for j in S for i in cosets[j]]
        p = 1
        for i in T:
            p = p * H[i] % q
        if p == gamma:
            fam.append(tuple(sorted(T)))
    return c, gamma, fam


def codeword_from_T(u, T, H, k, n, q):
    MT = vanishing([H[i] for i in T], q)
    prod = poly_mul(u, MT, q)
    red = mod_xn_minus_1(prod, n, q)
    P, rem = poly_divmod(red, MT, q)
    if trim(rem) or len(trim(P)) > k:
        return None
    P = trim(P) + [0] * (k - len(trim(P)))
    return tuple(P[:k])


# ------------------------------------------------------- exhaustive scan
def scan(H, u, v, k, A, q):
    """pairs {(f,g): frozenset}, rays {(z,c): frozenset}; z over P^1."""
    n = len(H)
    pairs, rays = {}, {}
    for W in combinations(range(n), k):
        f = interp([H[i] for i in W], [u[i] for i in W], q, k)
        g = interp([H[i] for i in W], [v[i] for i in W], q, k)
        if (f, g) not in pairs:
            pairs[(f, g)] = frozenset(
                i for i in range(n)
                if poly_ev(f, H[i], q) == u[i] and poly_ev(g, H[i], q) == v[i])
        pu = [(poly_ev(f, H[i], q) - u[i]) % q for i in range(n)]
        qv = [(poly_ev(g, H[i], q) - v[i]) % q for i in range(n)]
        both = sum(1 for i in range(n) if pu[i] == 0 and qv[i] == 0)
        cnt = {}
        for i in range(n):
            if qv[i]:
                z = (-pu[i]) * pow(qv[i], q - 2, q) % q
                cnt[z] = cnt.get(z, 0) + 1
        for z, c0 in cnt.items():
            if both + c0 >= A:
                c = tuple((f[e] + z * g[e]) % q for e in range(k))
                if (z, c) not in rays:
                    rays[(z, c)] = frozenset(
                        i for i in range(n) if (pu[i] + z * qv[i]) % q == 0)
        if sum(1 for i in range(n) if qv[i] == 0) >= A and (INF, g) not in rays:
            rays[(INF, g)] = frozenset(i for i in range(n) if qv[i] == 0)
    return pairs, rays


def occupancy(H, u, v, k, h, q):
    """N_d and per-depth pair counts from the fresh scan; A = k + h."""
    A = k + h
    pairs, rays = scan(H, u, v, k, A, q)
    raysets = list(rays.items())
    prof = {}
    for (f, g), Z in pairs.items():
        d = len(Z) - k
        if d < 1:
            continue
        L = sum(1 for (zc, S) in raysets if Z <= S)
        rec = prof.setdefault(d, [0, 0, 0])
        rec[0] += 1                      # pairs at this depth
        if L >= 2:
            rec[1] += 1                  # N_d
        rec[2] = max(rec[2], L)          # max L
    return prof, pairs, rays


def main():
    # ---------------- A: coset-sharing integer, exhaustive
    bad = tot = 0
    for (N, m, M) in [(8, 5, 2), (5, 3, 4), (8, 3, 2), (6, 2, 3)]:
        rp = m * M
        subs = list(combinations(range(N), m))
        for a in range(len(subs)):
            for b in range(a + 1, len(subs)):
                tot += 1
                sh = len(set(subs[a]) & set(subs[b])) * M
                if sh > rp - M:
                    bad += 1
    check("A: distinct coset unions share <= r' - M points (exhaustive, "
          "4 (N,m,M) shapes)", bad == 0, f"{tot} pairs, {bad} bad")

    # ---------------- B: MC diagonal quantization, two shapes
    for (n, k, w, M, h, q, pin_casc) in [(16, 4, 2, 2, 3, 97, 7),
                                         (20, 4, 4, 4, 5, 41, 2)]:
        rp = n - k - w
        N, m = n // M, rp // M
        A = k + h
        assert w == h - 1
        H = make_domain(q, n)
        c, gamma, fam = mc_setup(H, q, n, k, w, M)
        formula = comb(N, m) // N if gcd(m, N) == 1 else None
        check(f"B({n},{k},{w},{M}): MC family size = C(N,m)/N = {formula}",
              len(fam) == formula == pin_casc, f"{len(fam)}")
        u = mc_word(n, k, w, c, q)
        uv = [poly_ev(u, x, q) for x in H]
        members = {}
        okP = okEx = True
        for T in fam:
            P = codeword_from_T(u, T, H, k, n, q)
            if P is None:
                okP = False
                continue
            agr = frozenset(i for i in range(n)
                            if poly_ev(P, H[i], q) == uv[i])
            okEx &= (agr == frozenset(range(n)) - frozenset(T))
            members[T] = P
        check(f"B({n},{k},{w},{M}): every member P_T is a degree-<k "
              "codeword agreeing with u EXACTLY on H \\ T (agreement "
              "exactly k+w)", okP and okEx)
        # shift pencil j = 1
        j = 1
        okdiv = True
        Qs = {}
        for T, P in members.items():
            if any(P[e] for e in range(j)):        # X^{M-1} | P_T, j <= M-1
                okdiv = False
                continue
            Qs[T] = tuple(list(P[j:]) + [0] * j)
        check(f"B({n},{k},{w},{M}): X^j | P_T for j = 1 <= M-1 "
              "(the shift class is well defined)", okdiv)
        v = [0] * n
        v[n - 1 - j] = 1
        v[k + w - 1 - j] = (v[k + w - 1 - j] + c) % q
        vv = [poly_ev(v, x, q) for x in H]
        # diagonal exactly w, cross <= k
        okdiag = okcross = True
        fams = list(fam)
        for a in range(len(fams)):
            Ta = fams[a]
            Za = frozenset(i for i in range(n)
                           if poly_ev(members[Ta], H[i], q) == uv[i]
                           and poly_ev(Qs[Ta], H[i], q) == vv[i])
            okdiag &= (Za == frozenset(range(n)) - frozenset(Ta))
            for b in range(len(fams)):
                if a == b:
                    continue
                Tb = fams[b]
                Zx = sum(1 for i in range(n)
                         if poly_ev(members[Ta], H[i], q) == uv[i]
                         and poly_ev(Qs[Tb], H[i], q) == vv[i])
                okcross &= (Zx <= k)
        check(f"B({n},{k},{w},{M}): diagonal pairs (P_T, Q_T) at depth "
              "EXACTLY w; ALL cross pairs (P_T, Q_T') at joint agreement "
              "<= k+w-M <= k", okdiag and okcross)
        # full scan: N_d = 0 in the band proper, cascade count, line cap
        prof, pairs, rays = occupancy(H, uv, vv, k, h, q)
        band_bad = sum(prof.get(d, [0, 0, 0])[1] for d in range(1, h - 1))
        casc = prof.get(h - 1, [0, 0, 0])
        check(f"B({n},{k},{w},{M}): fresh exhaustive scan -- N_d = 0 at "
              "EVERY band-proper depth; cascade tier N_{h-1} = "
              f"{pin_casc} = C(N,m)/N", band_bad == 0 and casc[1] == pin_casc,
              f"profile {dict((d, tuple(x)) for d, x in sorted(prof.items()))}")
        check(f"B({n},{k},{w},{M}): line cap SATURATED at the cascade tier "
              f"(max L = n - A + 1 = {n - A + 1})", casc[2] == n - A + 1,
              f"maxL {casc[2]}")

    # ---------------- C: six-row 2-adic arithmetic
    ROWS = [("RowC 1/4", 1024, 256, 5), ("RowC 1/8", 1024, 128, 5),
            ("RowC 1/16", 1024, 64, 3),
            ("prize 1/4", 2**41, 2**39, 2**33 + 1),
            ("prize 1/8", 2**41, 2**38, 2**33 + 1),
            ("prize 1/16", 2**41, 2**37, 2**32 + 1)]
    ok_all = True
    det = []
    for (name, n, k, h) in ROWS:
        ok = (h % 2 == 1) and (h - 1) & (h - 2) == 0     # h odd, h-1 = 2^s
        # unique power of two in [ceil(h/2), h] is h-1
        lo, hi = (h + 1) // 2, h
        p = 1
        pows = []
        while p <= hi:
            if p >= lo:
                pows.append(p)
            p *= 2
        ok &= (pows == [h - 1])
        # no structured depth in the upper window [ceil(h/2), h-2]
        p = 1
        while p <= h - 2:
            ok &= not (lo <= p <= h - 2)
            p *= 2
        # parity: for every 2-power d in [2, h-2], h-d is odd > 1
        p = 2
        while p <= h - 2:
            ok &= ((h - p) % 2 == 1) and (h - p > 1)
            p *= 2
        # M = 2^ceil(log2 d) < 2d <= 2(h-2) < k across the band
        ok &= 2 * (h - 2) < k
        ok_all &= ok
        det.append(f"{name}:{'ok' if ok else 'BAD'}")
    check("C: BP(1)+BP(3) 2-adic/parity arithmetic at ALL SIX rows "
          "(h odd; unique 2-power in [ceil(h/2),h] = h-1; upper window "
          "structured-free; h-d odd for every structured d >= 2; "
          "2(h-2) < k)", ok_all, " ".join(det))

    # ---------------- D: BP(2)/BP(3) fixture battery (fresh replication)
    # pins: band_adjudication/checkpoints/band_proper.json (q = 41 rows)
    def bp_fixture(n, k, w, M, t, q, j):
        h, A = t, k + t
        H = make_domain(q, n)
        c, gamma, fam = mc_setup(H, q, n, k, w, M)
        u = mc_word(n, k, w, c, q)
        v = [0] * n
        v[n - 1 - j] = 1
        v[k + w - 1 - j] = (v[k + w - 1 - j] + c) % q
        uv = [poly_ev(u, x, q) for x in H]
        vv = [poly_ev(v, x, q) for x in H]
        prof, pairs, rays = occupancy(H, uv, vv, k, h, q)
        d = w
        Nd = prof.get(d, [0, 0, 0])[1]
        # slope confinement on depth-d family cores
        conf = True
        gam = set()
        allowed = {(-pow(x, j, q)) % q for x in H}
        for (zc, S) in rays.items():
            z = zc[0]
            for (f, g), Z in pairs.items():
                if len(Z) - k == d and Z <= S:
                    gam.add(z)
                    if z != INF and z not in allowed:
                        conf = False
        return Nd, conf, gam, prof

    n, k, w, M, q = 20, 4, 4, 4, 41
    # h = 6 (even) control: d = 4 in band proper [1,4]; productive iff j = 2
    res = {}
    for j in (1, 2, 3):
        res[j] = bp_fixture(n, k, w, M, 6, q, j)
    check("D: h = 6 EVEN control -- j = 2 (g = 2 = h-d) IS productive "
          "(N_4 = 2, pinned), j = 1 and j = 3 are NOT",
          res[2][0] == 2 and res[1][0] == 0 and res[3][0] == 0,
          f"N_4 by j: { {j: res[j][0] for j in res} }")
    check("D: h = 6 control -- live slopes on family cores confined to "
          "{-x^j : x in H}, |Gamma| <= n/(h-d) = 10",
          res[2][1] and len(res[2][2]) <= n // 2,
          f"|Gamma| = {len(res[2][2])}")
    # h = 7 (odd): no productive j -- the toy analogue of the six rows
    ok7 = True
    n7 = {}
    for j in (1, 2, 3):
        Nd, conf, gam, prof = bp_fixture(n, k, w, M, 7, q, j)
        n7[j] = Nd
        ok7 &= (Nd == 0)
    check("D: h = 7 ODD -- NO productive shift (N_4 = 0 for every "
          "j in [1, M-1]); official-row protection is PARITY", ok7,
          f"N_4 by j: {n7}")
    # h = 5: d = 4 = h-1 is the CASCADE tier; j = 1 productive (allowed)
    Nd5, conf5, gam5, prof5 = bp_fixture(n, k, w, M, 5, q, 1)
    check("D: h = 5 -- d = w = 4 = h-1 is the CASCADE tier, j = 1 "
          "productive there (g = 1 = h-d): the exclusion is of the band "
          "PROPER, not of the cascade tier", Nd5 == 2 and conf5,
          f"N_4 = {Nd5}")

    # ---------------- E: structured-floor completeness census
    n, k, w, M, q = 16, 8, 2, 2, 65537
    rp = n - k - w
    N, m = n // M, rp // M
    H = make_domain(q, n)
    c, gamma, fam = mc_setup(H, q, n, k, w, M)
    census = []
    for T in combinations(range(n), rp):
        s = 0
        p = 1
        for i in T:
            s = (s + H[i]) % q
            p = p * H[i] % q
        if s == 0 and p == gamma:
            census.append(tuple(sorted(T)))
    check("E: structured-floor completeness at (16,8,2,2), q = 65537 -- "
          "the FULL window census {|T| = r', e_1 = 0, prod = gamma} "
          "equals the mu_M-coset-union family exactly "
          f"({comb(N, m) // N} members)",
          sorted(census) == sorted(fam),
          f"census {len(census)} vs family {len(fam)}")

    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("XR_MC_DEPTH_QUANTIZATION_ALL_PASS")


if __name__ == "__main__":
    main()
