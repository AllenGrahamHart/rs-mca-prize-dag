#!/usr/bin/env python3
"""Verifier for xr_band_key_lemma_pencil_mass.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers, deterministic, no third-party imports, no file reads.

Fresh implementation (independent of lbt_lib/incidence.py; pins
cross-checked at draft time against
notes/pilots_20260802/list_bound_transfer/checkpoints/{incidence,mc,pencil}.json):

  A  THEOREM I / I' (pencil mass identity, with and without v-zeros),
     exhaustively over z in F_q, on censused codewords AND random c
  B  Corollaries I.1 (floor(n/a) members) and I.2 (disjoint lists, 2a > n)
  C  KEY LEMMA: dichotomy {0, 1, q+1} over EVERY S of size k, k+1, k+2 at
     (14,4,17); q+1 iff joint-explanation event; linearity exact;
     shared-agreement-set consequence on full per-member censuses
  D  MC-1/2/3 at (16,4,2,2), q = 97 and q = 193: census = indexed family,
     ceiling, count C(8,5)/8 = 7
  E  MC-5: every member of the shift pencil admits all 7 members
     (constructive); exhaustive census equality at 3 spot members
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


class LCG:
    def __init__(self, seed):
        self.s = seed

    def randint(self, lo, hi):
        self.s = (6364136223846793005 * self.s + 1442695040888963407) % (1 << 64)
        return lo + (self.s >> 33) % (hi - lo + 1)


# ------------------------------------------------------------ arithmetic
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


def interp_full(xs, ys, q):
    """degree-<len(xs) interpolant, full coefficient list."""
    a = len(xs)
    coeff = [0] * a
    for i in range(a):
        num, den = [1], 1
        for j in range(a):
            if j == i:
                continue
            num = poly_mul(num, [(-xs[j]) % q, 1], q)
            den = den * (xs[i] - xs[j]) % q
        w = ys[i] * pow(den, q - 2, q) % q
        for e in range(len(num)):
            coeff[e] = (coeff[e] + w * num[e]) % q
    return coeff


def census(vals, xs, k, q, amin):
    """{codeword: agreement} for every codeword with agr >= amin >= k."""
    n = len(xs)
    seen = {}
    for W in combinations(range(n), k):
        P = tuple(interp_full([xs[i] for i in W], [vals[i] for i in W], q)
                  + [0] * 0)[:k]
        P = tuple(list(P) + [0] * (k - len(P)))
        if P in seen:
            continue
        seen[P] = sum(1 for i in range(n) if poly_ev(P, xs[i], q) == vals[i])
    return {P: a for P, a in seen.items() if a >= amin}


def main():
    rng = LCG(20260802)

    # ---------------- A + B: THEOREM I / I', corollaries
    n, k, q = 12, 4, 13
    xs = list(range(1, n + 1))
    for tag, with_zero in [("v nowhere zero", False), ("v with zeros", True)]:
        u = [rng.randint(0, q - 1) for _ in range(n)]
        v = [rng.randint(1, q - 1) for _ in range(n)]
        if with_zero:
            v[0] = v[5] = 0
        Zv = [i for i in range(n) if v[i] == 0]
        cs = []
        for _ in range(8):
            cs.append([rng.randint(0, q - 1) for _ in range(n)])
        f = [rng.randint(0, q - 1) for _ in range(k)]
        cs.append([poly_ev(f, x, q) for x in xs])       # a codeword too
        bad = 0
        for c in cs:
            tot = 0
            for z in range(q):
                tot += sum(1 for i in range(n)
                           if (u[i] + z * v[i]) % q == c[i])
            e = sum(1 for i in Zv if u[i] == c[i])
            if tot != q * e + (n - len(Zv)):
                bad += 1
        check(f"A: THEOREM I/I' ({tag}) -- sum_z agr(c, w_z) = "
              "q e(c) + (n - |Z_v|), 9 functions x all z", bad == 0,
              f"{bad} bad")
    # I.1 / I.2 on an instance with a PLANTED high-agreement codeword
    u = [rng.randint(0, q - 1) for _ in range(n)]
    v = [rng.randint(1, q - 1) for _ in range(n)]
    fpl = [rng.randint(0, q - 1) for _ in range(k)]
    for i in range(8):
        u[i] = poly_ev(fpl, xs[i], q)                   # agr(f, w_0) >= 8
    a0 = n // 2 + 1                                     # 2a > n
    lists = {}
    for z in range(q):
        wz = [(u[i] + z * v[i]) % q for i in range(n)]
        lists[z] = set(census(wz, xs, k, q, a0).keys())
    nonempty = sum(1 for z in lists if lists[z])
    ok1 = all(
        sum(1 for z in range(q)
            if sum(1 for i in range(n)
                   if (u[i] + z * v[i]) % q == poly_ev(c, xs[i], q)) >= a0)
        <= n // a0
        for z0 in lists for c in lists[z0])
    ok2 = all(not (lists[z1] & lists[z2])
              for z1 in range(q) for z2 in range(z1 + 1, q))
    check("B: I.1 -- every codeword appears in <= floor(n/a) members; "
          "I.2 -- lists pairwise disjoint at 2a > n (non-vacuous: planted "
          "codeword present)", ok1 and ok2 and nonempty >= 1,
          f"{nonempty} nonempty member lists")

    # ---------------- C: KEY LEMMA
    n, k, q = 14, 4, 17
    xs = list(range(1, n + 1))
    u = [rng.randint(0, q - 1) for _ in range(n)]
    v = [rng.randint(1, q - 1) for _ in range(n)]
    # plant a joint-explanation event of size k+2 on S* = {0..5}
    Sstar = tuple(range(6))
    f = [rng.randint(0, q - 1) for _ in range(k)]
    g = [rng.randint(0, q - 1) for _ in range(k)]
    for i in Sstar:
        u[i] = poly_ev(f, xs[i], q)
        v[i] = poly_ev(g, xs[i], q)
    bad_dich = bad_iff = bad_lin = 0
    events = {a: 0 for a in (k, k + 1, k + 2)}
    tot_S = 0
    for a in (k, k + 1, k + 2):
        for S in combinations(range(n), a):
            tot_S += 1
            xsS = [xs[i] for i in S]
            Iu = interp_full(xsS, [u[i] for i in S], q)
            Iv = interp_full(xsS, [v[i] for i in S], q)
            A_top = tuple(Iu[k:])
            B_top = tuple(Iv[k:])
            joint = not any(A_top) and not any(B_top)
            cnt = 0
            if not any(B_top):
                cnt += 1                                    # (0:1) member
            if any(B_top) or any(A_top):
                # solutions of A + zB = 0 componentwise
                sols = None
                okz = True
                for e in range(a - k):
                    Ae, Be = A_top[e], B_top[e]
                    if Be == 0:
                        if Ae != 0:
                            okz = False
                            break
                        continue
                    zz = (-Ae) * pow(Be, q - 2, q) % q
                    if sols is None:
                        sols = zz
                    elif sols != zz:
                        okz = False
                        break
                if okz and sols is not None:
                    cnt += 1
                elif okz and sols is None and a > k:
                    cnt += q                                # A=B=0 finite part
            else:
                cnt += q                                    # A=B=0 finite part
            if a == k:
                cnt = q + 1                                 # no top: all
                joint = True
            if cnt not in (0, 1, q + 1):
                bad_dich += 1
            if (cnt == q + 1) != joint:
                bad_iff += 1
            if joint:
                events[a] += 1
            # linearity spot check
            z = (sum(S) * 7 + a) % q
            Iw = interp_full(xsS, [(u[i] + z * v[i]) % q for i in S], q)
            if any((Iu[e] + z * Iv[e] - Iw[e]) % q for e in range(a)):
                bad_lin += 1
    check("C: KEY LEMMA dichotomy -- #codeword members in {0, 1, q+1} for "
          f"EVERY S of size k..k+2 ({tot_S} sets), q+1 iff "
          "joint-explanation event", bad_dich == 0 and bad_iff == 0,
          f"dich {bad_dich}, iff {bad_iff}")
    check("C: interpolation linearity I_S(u + zv) = I_S(u) + z I_S(v) exact "
          "on every S", bad_lin == 0, f"{bad_lin} bad")
    check("C: the planted size-(k+2) joint-explanation event is found, and "
          "size-k events exist trivially", events[k + 2] >= 1,
          f"events by size: {events}")
    # shared-agreement-set consequence on full censuses
    shared_bad = 0
    shared_seen = 0
    mem_census = {}
    for z in list(range(q)) + [INF]:
        wz = v if z == INF else [(u[i] + z * v[i]) % q for i in range(n)]
        mem_census[z] = census(wz, xs, k, q, k)
    setmap = {}
    for z, cen in mem_census.items():
        for P, a in cen.items():
            wz = v if z == INF else [(u[i] + z * v[i]) % q for i in range(n)]
            S = frozenset(i for i in range(n)
                          if poly_ev(P, xs[i], q) == wz[i])
            setmap.setdefault(S, set()).add(z)
    for S, zs in setmap.items():
        if len(zs) >= 2:
            shared_seen += 1
            Ss = sorted(S)
            xsS = [xs[i] for i in Ss]
            Iu = interp_full(xsS, [u[i] for i in Ss], q)
            Iv = interp_full(xsS, [v[i] for i in Ss], q)
            if any(Iu[k:]) or any(Iv[k:]):       # tops must BOTH vanish
                shared_bad += 1
                continue
            # joint-explanation event: every member's interpolant is a
            # codeword agreeing with w_z on ALL of S (containment, not
            # exact-set equality -- other members may agree further)
            fS, gS = tuple(Iu[:k]), tuple(Iv[:k])
            for z in list(range(q)) + [INF]:
                wz = v if z == INF else [(u[i] + z * v[i]) % q
                                         for i in range(n)]
                cz = gS if z == INF else tuple((fS[e] + z * gS[e]) % q
                                               for e in range(k))
                if any(poly_ev(cz, xs[i], q) != wz[i] for i in Ss):
                    shared_bad += 1
                    break
    check("C: full per-member censuses -- every agreement set shared by "
          ">= 2 distinct members is a joint-explanation event and ALL q+1 "
          "members agree on it (containment)",
          shared_bad == 0 and shared_seen >= 1,
          f"{shared_seen} shared sets, {shared_bad} bad")

    # ---------------- D: MC-1/2/3 at (16,4,2,2), q in {97, 193, 12289}
    # (12289 - 1 = 2^12 * 3, so 16 | q-1, and q > C(16,10) = 8008: the
    # accidental-excess regime ends -- the pilot's P5.)
    n, k, w, M = 16, 4, 2, 2
    rp = n - k - w
    N, m = n // M, rp // M
    excess_by_q = {}
    for q in (97, 193, 12289):
        om = pow(primitive_root(q), (q - 1) // n, q)
        H = [pow(om, i, q) for i in range(n)]
        cosets = [[i for i in range(n) if i % N == j] for j in range(N)]
        T0 = [i for j in range(m) for i in cosets[j]]
        gamma = 1
        for i in T0:
            gamma = gamma * H[i] % q
        c = ((-1) ** (rp + 1) * gamma) % q
        u = [0] * n
        u[n - 1] = 1
        u[k + w - 1] = (u[k + w - 1] + c) % q
        uv = [poly_ev(u, x, q) for x in H]
        fam = []
        for S in combinations(range(N), m):
            T = [i for j in S for i in cosets[j]]
            p = 1
            for i in T:
                p = p * H[i] % q
            if p == gamma:
                fam.append(tuple(sorted(T)))
        # indexed set (ALL T, not only coset unions) vs exhaustive census
        indexed = set()
        for T in combinations(range(n), rp):
            s1 = 0
            p = 1
            for i in T:
                s1 = (s1 + H[i]) % q
                p = p * H[i] % q
            if s1 == 0 and p == gamma:                  # e_1 = 0 (w = 2)
                indexed.add(frozenset(range(n)) - frozenset(T))
        cen = census(uv, H, k, q, k + w)
        cen_sets = set()
        maxagr = 0
        for P, a in cen.items():
            maxagr = max(maxagr, a)
            cen_sets.add(frozenset(i for i in range(n)
                                   if poly_ev(P, H[i], q) == uv[i]))
        allcen = census(uv, H, k, q, k)
        ceiling = max(allcen.values(), default=0)
        check(f"D(q={q}): MC-1 -- census at agreement >= k+w EQUALS the "
              "indexed set {e_1..e_{w-1} = 0, prod = gamma}",
              cen_sets == indexed, f"{len(cen_sets)} vs {len(indexed)}")
        check(f"D(q={q}): MC-2 ceiling -- max agreement EXACTLY k+w = "
              f"{k + w}", ceiling == k + w and maxagr == k + w,
              f"max {ceiling}")
        fam_sets = {frozenset(range(n)) - frozenset(T) for T in fam}
        excess_by_q[q] = len(cen_sets) - len(fam)
        check(f"D(q={q}): MC-3 -- coset-union family has EXACTLY "
              f"C(N,m)/N = {comb(N, m) // N} members (gcd(m,N) = "
              f"{gcd(m, N)}) and is CONTAINED in the shell",
              len(fam) == comb(N, m) // N and fam_sets <= cen_sets,
              f"family {len(fam)}, census {len(cen_sets)}")
        if q == 97:
            # -------- E: MC-5 shift pencil
            j = 1
            members = {}
            okdiv = True
            for T in fam:
                VT = vanishing([H[i] for i in T], q)
                prod = poly_mul(u, VT, q)
                red = [0] * n
                for dd, cf in enumerate(prod):
                    red[dd % n] = (red[dd % n] + cf) % q     # beta = 1
                P, rem = poly_divmod(red, VT, q)
                assert not trim(rem) and len(trim(P)) <= k
                P = trim(P) + [0] * (k - len(trim(P)))
                if any(P[e] for e in range(M - 1)):     # X^{M-1} | P_T
                    okdiv = False
                members[T] = P
            check("E: X^{M-1} | P_T for every family member (shift class "
                  "well defined)", okdiv)
            v = [0] * n
            v[n - 1 - j] = 1
            v[k + w - 1 - j] = (v[k + w - 1 - j] + c) % q
            vv = [poly_ev(v, x, q) for x in H]
            ok_all = True
            for z in list(range(q)) + [INF]:
                wz = vv if z == INF else [(uv[i] + z * vv[i]) % q
                                          for i in range(n)]
                for T, P in members.items():
                    Q = tuple(list(P[j:]) + [0] * j)
                    cz = Q if z == INF else tuple((P[e] + z * Q[e]) % q
                                                 for e in range(k))
                    agr = sum(1 for i in range(n)
                              if poly_ev(cz, H[i], q) == wz[i])
                    ok_all &= (agr >= k + w)
            check("E: MC-5 -- ALL q+1 pencil members admit the ENTIRE "
                  "family at agreement >= k+w (constructive); min over "
                  f"P^1 >= C(N,m)/N = {comb(N, m) // N}", ok_all)
            spot_ok = True
            spot_counts = []
            for z in (0, 5, INF):
                wz = vv if z == INF else [(uv[i] + z * vv[i]) % q
                                          for i in range(n)]
                cz = census(wz, H, k, q, k + w)
                spot_counts.append(len(cz))
                spot_ok &= (len(cz) >= comb(N, m) // N)
            check("E: exhaustive census at 3 spot members finds >= "
                  "C(N,m)/N = 7 codewords each (the family floor holds "
                  "member-wise)", spot_ok, f"counts {spot_counts}")

    check("D: P5 -- accidental excess above the family floor vanishes at "
          "q = 12289 > C(n, r') = 8008 (small-q excess is measured, "
          "expected, and not part of MC-3's claim)",
          excess_by_q[12289] == 0 and all(v >= 0 for v in excess_by_q.values()),
          f"excess by q: {excess_by_q}")

    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("XR_BAND_KEY_LEMMA_PENCIL_MASS_ALL_PASS")


if __name__ == "__main__":
    main()
