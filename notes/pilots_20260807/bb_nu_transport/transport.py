#!/usr/bin/env python3
"""BB -> accident UPPER bound / nu(A) transport probe (round 22).

Stages:
  mfun      -- verify the closed form for M(N,m) = max_g #{S<=Z/N,|S|=m,sum==g}
  census    -- exhaustive per-shell deep-stratum profiles at the registered
               toy cells; test candidates U1, U2, U3
  dict      -- reproduce gamma_shell's banked toy observations (cross-check)
  prize     -- exact-integer evaluation at the DSA witness row, v = 34..39
  nu        -- exhaustive verification of THEOREM AT (occupancy anti-transport)
  failclosed-- negative control, must exit 1

stdlib only.  Run under tools/ramguard.
"""
import sys
from itertools import combinations
from math import comb, log2
from fractions import Fraction

CHECKS = 0
FAILS = 0


def ck(cond, label):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print("    FAIL: %s" % label)
    return cond


# ---------------------------------------------------------------- utilities
def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def elt_of_order(p, N):
    """theta in F_p^* of EXACT order N (requires N | p-1); verified."""
    assert (p - 1) % N == 0
    for g in range(2, p):
        th = pow(g, (p - 1) // N, p)
        # exact order check
        ok = pow(th, N, p) == 1
        if not ok:
            continue
        good = True
        for q in prime_factors(N):
            if pow(th, N // q, p) == 1:
                good = False
                break
        if good:
            return th
    raise RuntimeError("no element of order %d mod %d" % (N, p))


def prime_factors(n):
    fs, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            fs.add(d)
            n //= d
        d += 1
    if n > 1:
        fs.add(n)
    return fs


# ------------------------------------------------------- M(N,m) prescribed sum
def prescribed_sum_profile(N, m):
    """Exact vector c[g] = #{S<=Z/N : |S|=m, sum(S) == g mod N}, by DP."""
    # dp[j][g] after processing some elements: j chosen so far
    dp = [[0] * N for _ in range(m + 1)]
    dp[0][0] = 1
    for j in range(N):
        for c in range(min(j, m - 1), -1, -1):
            row = dp[c]
            tgt = dp[c + 1]
            for g in range(N):
                v = row[g]
                if v:
                    tgt[(g + j) % N] += v
    return dp[m]


def M_closed(N, m):
    """Ramanathan/Lehmer closed form, specialised to gcd(N,m) | 2 cases.

    #{S:|S|=m,sum==g} = (1/N) sum_{d | gcd(N,m)} (-1)^{m+m/d} C(N/d,m/d) c_d(g),
    c_d = Ramanujan sum.  For the crossing family N = 2L, m = L-2, gcd = 2
    (L even, L >= 4), c_1(g) = 1, c_2(g) = (-1)^g.
    """
    from math import gcd
    g = gcd(N, m)
    assert g in (1, 2), "closed form registered only for gcd in {1,2}"
    if g == 1:
        return comb(N, m) // N, comb(N, m) // N
    t1 = comb(N, m)
    t2 = comb(N // 2, m // 2)
    s = (-1) ** (m + m // 2)
    # even g: (t1 + s*t2*(+1))/N ; odd g: (t1 + s*t2*(-1))/N
    even = (t1 + s * t2) // N
    odd = (t1 - s * t2) // N
    assert (t1 + s * t2) % N == 0 and (t1 - s * t2) % N == 0
    return even, odd


def stage_mfun():
    print("== stage mfun: closed form for M(N,m), N = 2L, m = L-2 ==")
    for L in (4, 8, 16, 32, 64):
        N, m = 2 * L, L - 2
        prof = prescribed_sum_profile(N, m)
        ck(sum(prof) == comb(N, m), "L=%d total = C(%d,%d)" % (L, N, m))
        ev = set(prof[g] for g in range(0, N, 2))
        od = set(prof[g] for g in range(1, N, 2))
        ck(len(ev) == 1 and len(od) == 1,
           "L=%d profile constant on each parity class" % L)
        ce, co = M_closed(N, m)
        ck(prof[0] == ce, "L=%d even-shell closed form (%d vs %d)"
           % (L, prof[0], ce))
        ck(prof[1] == co, "L=%d odd-shell closed form (%d vs %d)"
           % (L, prof[1], co))
        Mv = max(prof)
        ck(Mv == max(ce, co), "L=%d max matches" % L)
        ck(co > ce, "L=%d maximum attained at ODD g (registered P3)" % L)
        print("   L=%3d N=%3d m=%3d  even/shell=%-22d odd/shell=%-22d "
              "M=2^%.4f  C(N,m)=2^%.4f"
              % (L, N, m, prof[0], prof[1], log2(Mv), log2(comb(N, m))))
    print()


# --------------------------------------------------------------- toy census
def deep_profile(L, p):
    """EXHAUSTIVE per-shell profile of the deep stratum at (2L, L-2, p).

    Returns (total_profile, struct_profile) as length-2L lists.
    total: S' <= Z/2L, |S'| = L-2, sum_{j in S'} theta^j == 0 in F_p,
           indexed by sigma'(S') mod 2L.
    struct: those with eps = 0 (unions of antipodal pairs).
    Meet in the middle over the halves [0,L) and [L,2L); uses no lemma.
    """
    N, m = 2 * L, L - 2
    th = elt_of_order(p, N)
    pw = [pow(th, j, p) for j in range(N)]

    def half(idxs):
        # d[size][value] = {shellsum: count}
        d = [dict() for _ in range(m + 1)]
        n = len(idxs)
        for mask in range(1 << n):
            c = bin(mask).count("1")
            if c > m:
                continue
            v = 0
            s = 0
            mm = mask
            while mm:
                b = (mm & -mm).bit_length() - 1
                j = idxs[b]
                v += pw[j]
                s += j
                mm &= mm - 1
            v %= p
            s %= N
            bucket = d[c].setdefault(v, {})
            bucket[s] = bucket.get(s, 0) + 1
        return d

    Ld = half(list(range(0, L)))
    Rd = half(list(range(L, N)))

    prof = [0] * N
    for c in range(m + 1):
        if c > L or (m - c) > L or (m - c) < 0:
            continue
        for v, sd in Ld[c].items():
            other = Rd[m - c].get((-v) % p)
            if not other:
                continue
            for s1, n1 in sd.items():
                for s2, n2 in other.items():
                    prof[(s1 + s2) % N] += n1 * n2

    # structural: choose (L-2)/2 antipodal pairs out of L
    sprof = [0] * N
    c = m // 2
    for ch in combinations(range(L), c):
        s = sum(2 * j + L for j in ch) % N
        sprof[s] += 1
    return prof, sprof


def brute_profile(L, p):
    """Independent brute force over all C(2L,L-2) subsets."""
    N, m = 2 * L, L - 2
    th = elt_of_order(p, N)
    pw = [pow(th, j, p) for j in range(N)]
    prof = [0] * N
    sprof = [0] * N
    for S in combinations(range(N), m):
        if sum(pw[j] for j in S) % p:
            continue
        g = sum(S) % N
        prof[g] += 1
        Sset = set(S)
        if all(((j + L) % N) in Sset for j in S):
            sprof[g] += 1
    return prof, sprof


CELLS = [
    ("CELL-A", 4, [17, 41, 73, 89, 97], "(n,w)=(32,8) m=5 v=3 a=2"),
    ("CELL-B", 8, [17, 97, 113, 193, 241], "(n,w)=(64,8) m=6 v=3 a=2"),
    ("CELL-C", 16, [97, 193, 257, 353, 449, 577, 641], "(n,w)=(64,4) m=6 v=2 a=1"),
]


def stage_census():
    print("== stage census: exhaustive deep-stratum shell profiles ==")
    print("   functionals: Xdeep(g), Sstruct(g), A_deep(g)=Xdeep-Sstruct,")
    print("   Amax, Xmax, N_acc, Occ, R2=Amax*2L/N_acc, R3=Amax*L/N_acc")
    worstR3 = Fraction(0)
    worstcell = None
    u3_fail = []
    for name, L, primes, shape in CELLS:
        N, m = 2 * L, L - 2
        Ccap = comb(N, m)
        ce, co = M_closed(N, m)
        Mcap = max(ce, co)
        structtot = comb(L, m // 2)
        print("\n  %s  L=%d  n_a=2L=%d  r'_a=%d   %s" % (name, L, N, m, shape))
        print("   C(2L,L-2)=%d   M(2L,L-2)=%d   |W^struct|=%d  struct/shell=%d"
              % (Ccap, Mcap, structtot, structtot // L))
        print("   %-6s %-10s %-8s %-8s %-6s %-8s %-8s %-7s %-7s %s"
              % ("p", "N_acc", "Amax", "Xmax", "Occ", "parities", "CS?",
                 "R2", "R3", "U3"))
        for p in primes:
            ck(is_prime(p), "%s p=%d prime" % (name, p))
            ck((p - 1) % N == 0, "%s p=%d == 1 mod 2L (delta_a=1)" % (name, p))
            prof, sprof = deep_profile(L, p)
            if L <= 8:
                bp, bs = brute_profile(L, p)
                ck(bp == prof, "%s p=%d MITM == brute force (total)" % (name, p))
                ck(bs == sprof, "%s p=%d MITM == brute force (struct)" % (name, p))
            # structural sanity: exactly the even shells, exactly equidistributed
            ck(sum(sprof) == structtot, "%s p=%d struct total" % (name, p))
            ck(all(sprof[g] == 0 for g in range(1, N, 2)),
               "%s p=%d struct on even shells only" % (name, p))
            sv = set(sprof[g] for g in range(0, N, 2))
            ck(len(sv) == 1, "%s p=%d struct EXACTLY equidistributed (BB-4)"
               % (name, p))
            # structural must satisfy the relation
            ck(all(prof[g] >= sprof[g] for g in range(N)),
               "%s p=%d struct subset of total" % (name, p))
            acc = [prof[g] - sprof[g] for g in range(N)]
            Nacc = sum(acc)
            Amax = max(acc)
            Xmax = max(prof)
            Occ = sum(1 for a in acc if a > 0)
            pe = sum(1 for g in range(0, N, 2) if acc[g] > 0)
            po = sum(1 for g in range(1, N, 2) if acc[g] > 0)
            # ---- candidate U1
            ck(Xmax <= Ccap, "%s p=%d (U1) Xmax<=C(2L,L-2)" % (name, p))
            # ---- candidate U2
            ck(Xmax <= Mcap, "%s p=%d (U2) Xmax<=M(2L,L-2)" % (name, p))
            ck(Amax <= Mcap, "%s p=%d (U2) Amax<=M(2L,L-2)" % (name, p))
            # ---- candidate U3 (naive transport)  Amax <= N_acc/L
            if Nacc:
                R2 = Fraction(Amax * N, Nacc)
                R3 = Fraction(Amax * L, Nacc)
                u3ok = Amax * L <= Nacc
                if not u3ok:
                    u3_fail.append((name, L, p, Amax, Nacc, float(R3)))
                if R3 > worstR3:
                    worstR3 = R3
                    worstcell = (name, L, p, Amax, Nacc)
                r2s, r3s = "%.4f" % float(R2), "%.4f" % float(R3)
            else:
                u3ok = True
                r2s = r3s = "  n/a "
            csv = "YES" if p < 2 ** (L - 2) else "vac"
            # how lossy is (U2)?  registered claim: lossy by ~ a factor Q = p
            slack = Fraction(Mcap, Xmax) if Xmax else None
            ss = ("%.2f" % float(slack)) if slack else " n/a"
            print("   %-6d %-10d %-8d %-8d %-6d e%-3d/o%-3d %-8s %-7s %-7s %-10s"
                  " U2slack=%s (p=%d)"
                  % (p, Nacc, Amax, Xmax, Occ, pe, po, csv, r2s, r3s,
                     "ok" if u3ok else "FALSIFIED", ss, p))
            if Xmax and Nacc:
                # the (U2) loss factor should track Q = p, not something else
                ck(Fraction(1, 4) * p <= slack <= 4 * p,
                   "%s p=%d (U2) loss factor tracks Q=p within 4x (slack=%.2f)"
                   % (name, p, float(slack)))
    print("\n  (U3) Amax <= N_acc/L :  %d falsifying cells" % len(u3_fail))
    for f in u3_fail:
        print("     FALSIFIER  %s L=%d p=%d : Amax=%d > N_acc/L=%s  (R3=%.4f)"
              % (f[0], f[1], f[2], f[3], Fraction(f[4], f[1]), f[5]))
    if worstcell:
        print("  worst R3 = %s = %.4f at %s L=%d p=%d (Amax=%d, N_acc=%d)"
              % (worstR3, float(worstR3), worstcell[0], worstcell[1],
                 worstcell[2], worstcell[3], worstcell[4]))
    print()
    return len(u3_fail), worstR3


def relation_weights(L, p):
    """Exact weight distribution of the relation set
       R = {eps in {0,+-1}^L : sum_j eps_j theta^j = 0 in F_p},
    theta of exact order 2L.  Meet-in-the-middle over 3^{L/2} halves.
    Returns Counter-like dict U -> #{eps in R with |supp(eps)| = U}."""
    N = 2 * L
    th = elt_of_order(p, N)
    pw = [pow(th, j, p) for j in range(N)]
    h = L // 2

    def half(idxs):
        d = {}
        n = len(idxs)
        for code in range(3 ** n):
            c, v, U = code, 0, 0
            for b in range(n):
                dgt = c % 3
                c //= 3
                if dgt == 1:
                    v += pw[idxs[b]]
                    U += 1
                elif dgt == 2:
                    v -= pw[idxs[b]]
                    U += 1
            v %= p
            dd = d.setdefault(v, {})
            dd[U] = dd.get(U, 0) + 1
        return d

    Ld = half(list(range(0, h)))
    Rd = half(list(range(h, L)))
    out = {}
    for v, du in Ld.items():
        other = Rd.get((-v) % p)
        if not other:
            continue
        for u1, c1 in du.items():
            for u2, c2 in other.items():
                out[u1 + u2] = out.get(u1 + u2, 0) + c1 * c2
    return out


def stage_relations():
    print("== stage relations: independent re-verification of LEMMA TC (BB-6) ==")
    print("   and the minimum ternary support U_min of the relation lattice")
    for name, L, primes, shape in CELLS:
        N, m = 2 * L, L - 2
        print("\n  %s  L=%d  2L=%d  r'_a=%d" % (name, L, N, m))
        print("   %-6s %-9s %-8s %-8s %-12s %-12s %s"
              % ("p", "#relns", "U_min", "3^L/p", "sum fibres", "N_acc(TC)",
                 "N_acc(census)"))
        for p in primes:
            R = relation_weights(L, p)
            tot = sum(R.values())
            ck(R.get(0, 0) == 1, "%s p=%d : eps=0 is the unique U=0 relation"
               % (name, p))
            nz = {u: c for u, c in R.items() if u > 0}
            Umin = min(nz) if nz else None

            def fib(U):
                if U > m or (U - m) % 2:
                    return 0
                return comb(L - U, (m - U) // 2)

            # banked identity (crossing_low_w/PROOFS.md:175), over ALL eps:
            allfib = sum(comb(L, U) * (2 ** U) * fib(U) for U in range(L + 1))
            ck(allfib == comb(N, m),
               "%s p=%d LEMMA TC total identity sum_eps C(L-U,(r'_a-U)/2)"
               " = C(2L,r'_a)" % (name, p))
            nacc_tc = sum(c * fib(u) for u, c in nz.items())
            prof, sprof = deep_profile(L, p)
            nacc_cen = sum(prof) - sum(sprof)
            ck(nacc_tc == nacc_cen,
               "%s p=%d LEMMA TC fibre sum == exhaustive census N_acc (%d vs %d)"
               % (name, p, nacc_tc, nacc_cen))
            ck(sum(sprof) == fib(0), "%s p=%d eps=0 fibre == structural total"
               % (name, p))
            print("   %-6d %-9d %-8s %-8.1f %-12d %-12d %d"
                  % (p, tot, str(Umin), 3.0 ** L / p, allfib, nacc_tc, nacc_cen))
    print("\n   NOTE: an UPPER bound on #relns by weight is precisely what an")
    print("   Acc_deep upper bound needs beyond (U2); U_min is the ternary")
    print("   minimum-distance quantity that would supply it.")
    print()


def stage_dict():
    """Dictionary cross-check against gamma_shell's BANKED toy observations.

    POST-REGISTRATION addition, disclosed: these primes were chosen to
    reproduce banked numbers, not to test a candidate.
    """
    print("== stage dict: cross-check vs gamma_shell banked toy claims ==")
    # gamma_shell/toy_shell.out `shell` stage, VERBATIM columns:
    #   (n,w)=(64,8) p=193  shells: total=8   struct=8   acc=8
    #   (n,w)=(64,8) p=577  shells: total=16  struct=8   acc=8
    #   (n,w)=(64,8) p in {257,449,641}: acc=0
    #   (n,w)=(32,8) p in {97,193,257,353,449}: acc=0   (L=4)
    # NB the columns are counts of SHELLS, not of accidents -- see CATCH-T1.
    for p, tot_sh, acc_sh in ((193, 8, 8), (257, 8, 0), (449, 8, 0),
                              (577, 16, 8), (641, 8, 0)):
        prof, sprof = deep_profile(8, p)
        acc = [prof[g] - sprof[g] for g in range(16)]
        ev = sum(1 for g in range(0, 16, 2) if acc[g] > 0)
        od = sum(1 for g in range(1, 16, 2) if acc[g] > 0)
        occ_tot = sum(1 for g in range(16) if prof[g] > 0)
        print("   L=8 p=%-4d  N_acc=%-4d  acc-shells=%d (even %d / odd %d)  "
              "total-shells=%d" % (p, sum(acc), ev + od, ev, od, occ_tot))
        ck(ev + od == acc_sh, "banked toy_shell.out: (64,8) p=%d acc shells = %d"
           % (p, acc_sh))
        ck(occ_tot == tot_sh, "banked toy_shell.out: (64,8) p=%d total shells = %d"
           % (p, tot_sh))
    ck(deep_profile(8, 193)[0] != deep_profile(8, 577)[0],
       "the two parity branches are genuinely different cells")
    for p in (97, 193, 257, 353, 449):
        prof, sprof = deep_profile(4, p)
        acc = [prof[g] - sprof[g] for g in range(8)]
        ck(sum(acc) == 0, "banked toy_shell.out: (32,8) p=%d acc=0 (L=4)" % p)
    # gamma_shell PROOFS:337-343 -- at (64,4) [L=16] accidents occupy exactly
    # 2L = 32 shells, five primes.
    for p in (97, 193, 257, 353, 449):
        prof, sprof = deep_profile(16, p)
        acc = [prof[g] - sprof[g] for g in range(32)]
        occ = sum(1 for a in acc if a > 0)
        ck(occ == 32, "banked: (64,4) p=%d accidents occupy exactly 2L=32 shells"
           % p)
        print("   L=16 p=%-4d N_acc=%-8d Occ=%d" % (p, sum(acc), occ))
    # dictionary: structural per shell reproduces S(v) form C(L,(L-2)/2)/L
    for L in (4, 8, 16):
        ck(comb(L, (L - 2) // 2) % L == 0,
           "L=%d: C(L,(L-2)/2) divisible by L (BB-4 exact equidistribution)" % L)
    print()


# ------------------------------------------------------------- the prize row
def stage_prize():
    print("== stage prize: DSA witness row, exact integers ==")
    p = 3 * (1 << 41) + 1
    ck(is_prime(p), "p = 3*2^41+1 is prime")
    ck(p == 6597069766657, "p value matches banked 6597069766657")
    e = 6
    q = p ** e
    Bstar = q >> 128
    ck(Bstar == 242251802232021244567343686397347233808,
       "B* reproduces banked 242251802232021244567343686397347233808")
    print("   p = %d   log2 p = %.4f" % (p, log2(p)))
    print("   q = p^6, log2 q = %.6f      B* = %d  (log2 = %.4f)"
          % (log2(q), Bstar, log2(Bstar)))
    n = 1 << 41
    print("\n   v    L     2L    r'_a   S(v)=struct/shell   C(2L,r'_a)   "
          "M(2L,r'_a)   U2 vs B*")
    rows = []
    for v in range(34, 40):
        L = 1 << (41 - v)
        N = 2 * L
        m = L - 2
        ck(N == 1 << (42 - v), "v=%d n_a = 2^{42-v}" % v)
        Sv = comb(L, m // 2) // L
        ck(comb(L, m // 2) % L == 0, "v=%d structural exactly equidistributed" % v)
        Ccap = comb(N, m)
        ce, co = M_closed(N, m)
        Mcap = max(ce, co)
        # independent DP check of M at the small v (N <= 64)
        if N <= 64:
            prof = prescribed_sum_profile(N, m)
            ck(max(prof) == Mcap, "v=%d M(2L,r'_a) DP == closed form" % v)
        rows.append((v, L, N, m, Sv, Ccap, Mcap))
        verdict = "BELOW B*" if Mcap <= Bstar else "above B*  (VACUOUS)"
        print("   %-4d %-5d %-5d %-6d 2^%-17.4f 2^%-10.4f 2^%-10.4f %s"
              % (v, L, N, m, log2(Sv) if Sv > 1 else 0.0,
                 log2(Ccap), log2(Mcap), verdict))
    # dictionary vs banked gamma_shell numbers
    Sv34 = rows[0][4]
    ck(abs(log2(Sv34) - 117.1491) < 5e-4, "S(34) reproduces banked 2^117.1491")
    ck(abs(log2(comb(128, 63)) - 124.1491) < 5e-4,
       "|W^struct| at v=34 reproduces banked 2^124.1491")
    ck(abs(log2(rows[1][4]) - 54.624) < 1e-3, "S(35) reproduces banked 2^54.624")
    ck(abs(log2(rows[2][4]) - 24.076) < 1e-3, "S(36) reproduces banked 2^24.076")
    ck(abs(log2(rows[3][4]) - 9.482) < 1e-3, "S(37) reproduces banked 2^9.482")
    ck(abs(log2(rows[4][4]) - 2.807) < 1e-3, "S(38) reproduces banked 2^2.807")
    ck(abs(log2(comb(256, 126)) - 251.6279) < 5e-4,
       "log2 C(256,126) reproduces banked 251.6279 (crossing_gap)")

    print("\n   -- the registered margins at v = 35 --")
    v, L, N, m, Sv, Ccap, Mcap = rows[1]
    print("      C(128,62)  = %d" % Ccap)
    print("      M(128,62)  = %d" % Mcap)
    print("      B*         = %d" % Bstar)
    print("      log2 C(128,62) = %.4f   margin vs B* = %+.4f bits"
          % (log2(Ccap), log2(Bstar) - log2(Ccap)))
    print("      log2 M(128,62) = %.4f   margin vs B* = %+.4f bits"
          % (log2(Mcap), log2(Bstar) - log2(Mcap)))
    ck(Ccap < Bstar, "(U1) at v=35: C(128,62) < B*  [exact integers]")
    ck(Mcap < Bstar, "(U2) at v=35: M(128,62) < B*  [exact integers]")
    ck(Ccap * 1 > Bstar // 100, "sanity: C(128,62) not absurdly small")
    # P6.6 bracket: M/Q should sit ABOVE the banked proved lower bound 2^73.061
    lb = log2(Mcap) - log2(p)
    print("      log2 M(128,62) - log2 p = %.4f   vs banked PROVED max-shell "
          "lower bound 73.061  (gap %+.4f)" % (lb, lb - 73.061))
    ck(lb > 73.061, "P6.6: heuristic M/Q sits ABOVE the banked proved floor")
    ck(lb - 73.061 < 3.0, "P6.6: bracket within 3 bits")

    print("\n   -- CATCH-T2: a dangerous 0.067-bit numerical collision --")
    S34 = rows[0][4]
    print("      banked  S(34)      = C(128,63)/128 = %d  (2^%.4f)"
          % (S34, log2(S34)))
    print("      new     M(128,62)  =                 %d  (2^%.4f)"
          % (Mcap, log2(Mcap)))
    print("      banked  |W^struct| = C(128,63)     = %d  (2^%.4f)"
          % (comb(128, 63), log2(comb(128, 63))))
    print("      new     C(128,62)  =                 %d  (2^%.4f)"
          % (Ccap, log2(Ccap)))
    ck(S34 != Mcap, "S(34) and M(128,62) are DIFFERENT integers")
    ck(comb(128, 63) != Ccap, "C(128,63) and C(128,62) are DIFFERENT integers")
    ck(comb(128, 63) * 63 == Ccap * 66, "C(128,63)/C(128,62) = 66/63 exactly")
    ck(abs(log2(S34) - log2(Mcap)) < 0.07,
       "the two collide to within 0.07 bits (why this must be flagged)")
    print("      C(128,63)/C(128,62) = 66/63 exactly -> 0.0671 bits apart.")
    print("      They are different objects at different v: S(34) is the")
    print("      STRUCTURAL per-shell count at v=34; M(128,62) is the")
    print("      UNCONDITIONED shell cap at v=35.  Do not conflate.")

    print("\n   -- row region of (U2): it is p-INDEPENDENT --")
    print("      (U2) certifies the deep stratum at w=2^v on every row with")
    print("      B* >= M(2L,r'_a), i.e. q >= 2^128 * M.  Prime rows e=1 have")
    print("      q = p and live range log2 p in [129.5849625, 256) (B* >= 3).")
    lo, hi = 128 + log2(3), 256.0
    print("      %-4s %-14s %-14s %s" % ("v", "log2 M", "min log2 q", "share of live prime window"))
    shares = []
    for (v, L, N, m, Sv, Ccap, Mcap) in rows:
        thr = 128 + log2(Mcap)
        cov = max(0.0, hi - max(lo, thr)) / (hi - lo)
        shares.append(cov)
        print("      %-4d %-14.4f %-14.4f %.2f%%" % (v, log2(Mcap), thr, 100 * cov))
    ck(shares == sorted(shares), "P6.5: prime-row coverage grows with v")
    ck(shares[0] == 0.0, "P6.5: v=34 covers none (the break row)")
    ck(0.0 < shares[1] < 0.10, "P6.5: v=35 covers <10%% of the live prime window")
    print()
    return Bstar, rows


# ------------------------------------------------------------------ nu(A)
def occupancy_vectors(Nn, Y):
    """All multisets of Y positive integers summing to Nn (partitions)."""
    def rec(rem, parts, mx):
        if parts == 0:
            if rem == 0:
                yield ()
            return
        for a in range(min(rem - parts + 1, mx), 0, -1):
            for tail in rec(rem - a, parts - 1, a):
                yield (a,) + tail
    return rec(Nn, Y, Nn)


def stage_nu():
    print("== stage nu: THEOREM AT -- the occupancy anti-transport ==")
    print("   functional: RHS(A) := N - (1/2) sum_z X_z(X_z-1), the exact")
    print("   right-hand side of averaged_slope_conversion (nu(A) = E[RHS]).")
    worst_ratio = None
    for Nn in range(1, 15):
        for Y in range(1, Nn + 1):
            for vec in occupancy_vectors(Nn, Y):
                assert sum(vec) == Nn and len(vec) == Y
                rhs = Fraction(Nn) - Fraction(sum(x * (x - 1) for x in vec), 2)
                # (i) the conversion inequality itself, pointwise
                ck(rhs <= Y, "conversion RHS <= Y at N=%d vec=%s" % (Nn, vec))
                # (ii) Cauchy-Schwarz form
                cs = Fraction(3 * Nn, 2) - Fraction(Nn * Nn, 2 * Y)
                ck(rhs <= cs, "RHS <= (3/2)N - N^2/(2Y) at N=%d vec=%s" % (Nn, vec))
                # (iii) the anti-transport threshold
                if 3 * Y <= Nn:
                    ck(rhs <= 0, "Y<=N/3 => RHS<=0 at N=%d vec=%s" % (Nn, vec))
                if rhs > 0:
                    r = Fraction(Nn, Y)
                    if worst_ratio is None or r > worst_ratio:
                        worst_ratio = r
    print("   exhaustive over all occupancy vectors with N <= 14")
    print("   largest concentration ratio N/Y admitting RHS > 0 : %s = %.4f"
          % (worst_ratio, float(worst_ratio)))
    ck(worst_ratio < 3, "P7.3/F5: the threshold constant is exactly 3")
    # the uniform-concentration identity  RHS = N(3-kappa)/2
    for Nn, kap in ((12, 2), (12, 3), (12, 4), (12, 6)):
        Y = Nn // kap
        vec = tuple([kap] * Y)
        rhs = Fraction(Nn) - Fraction(sum(x * (x - 1) for x in vec), 2)
        ck(rhs == Fraction(Nn * (3 - kap), 2),
           "uniform concentration factor %d: RHS = N(3-kappa)/2" % kap)
        print("   uniform kappa=%d  (N=%d, Y=%d): RHS = %s" % (kap, Nn, Y, rhs))
    # what BB's own concentration factor would do
    print("\n   BB's deep-stratum concentration factor is 2^33 (256 shells of")
    print("   2^41).  kappa = 2^33 gives RHS = N(3 - 2^33)/2 < 0 for every")
    print("   N >= 1: the M-route's occupancy functional is DESTROYED, not")
    print("   supplied, by shell concentration.")
    # first moment is structure-blind (quoted identity, checked symbolically)
    print("   E[N(A)] = |A|(1-q^{-t})q^{1-t} depends on A only through |A|;")
    print("   C_t(A) >= 0 enters nu with a MINUS sign.  Hence structure can")
    print("   only LOWER nu(A) below the |A|-only ceiling.")
    # CATCH-T3 (my own defect, found by this gate): q**(1-t) is a FLOAT in
    # Python for t>1, so the first version of this check silently compared a
    # binary-float Fraction against an exact one and FAILED.  Exact form only.
    for q_, t_, Asz in ((5, 2, 7), (11, 3, 40), (13, 2, 100)):
        en = Fraction(Asz) * (1 - Fraction(1, q_ ** t_)) * Fraction(1, q_ ** (t_ - 1))
        ck(en > 0, "E[N] positive at (q,t,|A|)=(%d,%d,%d)" % (q_, t_, Asz))
        ck(en == Fraction(Asz * (q_ ** t_ - 1), q_ ** (2 * t_ - 1)),
           "E[N] closed form at (q,t,|A|)=(%d,%d,%d)" % (q_, t_, Asz))
        # the decisive structural fact: E[N] is a function of |A| ALONE
        en2 = Fraction(Asz + 1) * (1 - Fraction(1, q_ ** t_)) * Fraction(1, q_ ** (t_ - 1))
        ck(en2 / (Asz + 1) == en / Asz,
           "E[N]/|A| independent of the family at (q,t)=(%d,%d)" % (q_, t_))
    print()


def stage_failclosed():
    print("== stage failclosed: negative control ==")
    ck(1 == 2, "deliberate false check")
    print()


STAGES = {
    "mfun": stage_mfun,
    "census": stage_census,
    "relations": stage_relations,
    "dict": stage_dict,
    "prize": stage_prize,
    "nu": stage_nu,
    "failclosed": stage_failclosed,
}

if __name__ == "__main__":
    which = sys.argv[1:] or ["mfun", "census", "relations", "dict", "prize", "nu"]
    for s in which:
        STAGES[s]()
    print("TOTAL CHECKS %d   FAILURES %d" % (CHECKS, FAILS))
    sys.exit(1 if FAILS else 0)
