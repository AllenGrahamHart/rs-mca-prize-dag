#!/usr/bin/env python3
"""TOY GATE for the gamma-shell question (round 20, gamma_shell pilot).

Self-contained.  No repo imports.  Fail-closed: every stage counts checks
and any failure exits 1; the `failclosed` stage injects a false check and
MUST exit 1.

Stages
  siglift    (P1/F1, MANDATORY) exhaustive (SIG-LIFT) at the three DSA gate
             shapes (n,w) = (32,8), (64,8), (64,16).
  dsbiject   independent re-check of LEMMA DS/FREE (lift in W_w <=> p_1=0).
  shell      (P2/F2) the shell map: concentration, structural shells,
             accident parity, per-shell structural count.
  mult       (P3.1/F3) exhaustive check of the pair-multiplicity 2^{L-2-U}.
  count      (P3/F3) exhaustive check of the Cauchy-Schwarz accident bound.
  census     FULL W_w census (meet-in-the-middle) -> Lemma X and the
             X_w(gamma) dictionary, deep stratum located inside the whole set.
  failclosed permanent negative control.

Usage: tools/ramguard local -- python3 notes/pilots_20260806/gamma_shell/toy_shell.py <stage>
"""
import sys
from fractions import Fraction
from itertools import combinations
from math import comb, gcd

CHECKS = 0
FAILS = 0


def ck(cond, msg):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print("  FAIL: %s" % msg)
    return cond


def deep_shape(n, w):
    """(a, n_a, L, r', r'_a) for the crossing family k = n/2, r' = n/2 - w."""
    v = w.bit_length() - 1
    assert 1 << v == w
    a = v - 1
    n_a = n >> a
    L = n_a >> 1
    rp = (n >> 1) - w
    ra = rp >> a
    return a, n_a, L, rp, ra


# the three DSA gate shapes, verbatim from
# background/nodes/crossing_dsa_refutation/statement.md:21
SHAPES = [(32, 8), (64, 8), (64, 16)]
PRIMES = {32: [97, 193, 257, 353, 449], 64: [193, 257, 449, 577, 641]}


def unit_of_order(p, m):
    """some element of exact multiplicative order m in F_p (m | p-1)."""
    assert (p - 1) % m == 0
    for g in range(2, p):
        t = pow(g, (p - 1) // m, p)
        if all(pow(t, m // r, p) != 1 for r in set(prime_factors(m))):
            return t
    raise RuntimeError("no element of order %d mod %d" % (m, p))


def prime_factors(m):
    f, d = [], 2
    while d * d <= m:
        while m % d == 0:
            f.append(d)
            m //= d
        d += 1
    if m > 1:
        f.append(m)
    return f


def lift(Sp, n_a, a):
    """S = {j + n_a t : j in S', 0 <= t < 2^a}  <=  Z/n."""
    return [j + n_a * t for j in Sp for t in range(1 << a)]


# --------------------------------------------------------------- siglift
def stage_siglift():
    """(SIG-LIFT): sig(S) = 2^a sigma'(S') + |S'| n_a 2^{a-1} (2^a - 1)  mod n."""
    print("=== stage siglift  (P1 / falsifier F1 -- MANDATORY GATE) ===")
    for (n, w) in SHAPES:
        a, n_a, L, rp, ra = deep_shape(n, w)
        print("  shape (n,w)=(%d,%d): a=%d n_a=%d L=%d r'=%d r'_a=%d (L-2=%d)"
              % (n, w, a, n_a, L, rp, ra, L - 2))
        ck(ra == L - 2, "LEMMA DS shape r'_a = L-2 at (%d,%d)" % (n, w))
        # exhaustive over EVERY subset of Z/n_a of EVERY size (stronger than
        # needed: the registered formula is claimed for all S').
        tot = 0
        for msk in range(1 << n_a):
            Sp = [j for j in range(n_a) if (msk >> j) & 1]
            S = lift(Sp, n_a, a)
            direct = sum(S) % n
            formula = (( 1 << a) * sum(Sp)
                       + len(Sp) * n_a * (1 << (a - 1)) * ((1 << a) - 1)) % n
            if direct != formula:
                ck(False, "(SIG-LIFT) S'=%s at (%d,%d)" % (Sp, n, w))
            tot += 1
        ck(True, "(SIG-LIFT) exhaustive over all 2^%d subsets at (%d,%d)"
           % (n_a, n, w))
        print("    verified on %d subsets S' <= Z/%d" % (tot, n_a))
        # the prize-shape simplification: second term == 0 mod n when
        # |S'| * n_a * 2^{a-1} * (2^a - 1) == 0 mod n
        sec = ra * n_a * (1 << (a - 1)) * ((1 << a) - 1) % n
        print("    second term at |S'| = r'_a = %d : %d mod %d" % (ra, sec, n))
    return


# --------------------------------------------------------------- dsbiject
def window_ok(S, n, w, p, zeta):
    """direct evaluation of ALL w-1 power-sum conditions (no lemma used)."""
    for s in range(1, w):
        if sum(pow(zeta, (s * i) % n, p) for i in S) % p:
            return False
    return True


def reduced_solutions(n_a, ra, p, theta):
    out = []
    for Sp in combinations(range(n_a), ra):
        if sum(pow(theta, j, p) for j in Sp) % p == 0:
            out.append(Sp)
    return out


def stage_dsbiject():
    """LEMMA DS + LEMMA FREE, re-verified independently of round 18."""
    print("=== stage dsbiject  (independent re-check of the imported lemma) ===")
    for (n, w) in SHAPES:
        a, n_a, L, rp, ra = deep_shape(n, w)
        for p in PRIMES[n]:
            zeta = unit_of_order(p, n)
            theta = pow(zeta, 1 << a, p)
            ck(pow(theta, n_a, p) == 1 and pow(theta, n_a // 2, p) != 1,
               "theta has order n_a = %d (p=%d)" % (n_a, p))
            mem = struct = 0
            for Sp in combinations(range(n_a), ra):
                red = sum(pow(theta, j, p) for j in Sp) % p == 0
                S = lift(list(Sp), n_a, a)
                inW = window_ok(S, n, w, p, zeta)
                ck(red == inW, "DS bijection S'=%s (n,w)=(%d,%d) p=%d"
                   % (Sp, n, w, p))
                if inW:
                    mem += 1
                    if all(((j + L) % n_a) in Sp for j in Sp):
                        struct += 1
            exp_struct = comb(n // w, rp // w) if rp % w == 0 else 0
            ck(struct == exp_struct,
               "structural count = C(n/M, r'/M) = %d (got %d)"
               % (exp_struct, struct))
            print("    (n,w)=(%d,%d) p=%-4d members=%-4d structural=%-4d accidents=%d"
                  % (n, w, p, mem, struct, mem - struct))
    return


# --------------------------------------------------------------- shell
def stage_shell():
    """(SHELL-CONC) / (SHELL-STRUCT) / (SHELL-ACC) -- the danger case FIRST."""
    print("=== stage shell  (P2 / falsifier F2 -- the concentration danger case) ===")
    for (n, w) in SHAPES:
        a, n_a, L, rp, ra = deep_shape(n, w)
        for p in PRIMES[n]:
            zeta = unit_of_order(p, n)
            theta = pow(zeta, 1 << a, p)
            sols = reduced_solutions(n_a, ra, p, theta)
            sigs, ssig, asig = set(), set(), set()
            for Sp in sols:
                S = lift(list(Sp), n_a, a)
                sg = sum(S) % n
                sigs.add(sg)
                if all(((j + L) % n_a) in Sp for j in Sp):
                    ssig.add(sg)
                else:
                    asig.add(sg)
                # (SHELL-CONC): sig in 2^a Z/n
                ck(sg % (1 << a) == 0,
                   "(SHELL-CONC) sig=%d not in 2^%d Z (n,w)=(%d,%d)"
                   % (sg, a, n, w))
            ck(len(sigs) <= n_a,
               "(SHELL-CONC) deep stratum in <= 2L = %d shells (got %d)"
               % (n_a, len(sigs)))
            # (SHELL-STRUCT): structural sigs in 2^{a+1} Z/n
            for sg in ssig:
                ck(sg % (1 << (a + 1)) == 0,
                   "(SHELL-STRUCT) structural sig=%d not in 2^%d Z" % (sg, a + 1))
            # structural per-shell count is |W^struct| / L, EXACTLY equal on
            # every occupied structural shell
            prof = {}
            for Sp in sols:
                if all(((j + L) % n_a) in Sp for j in Sp):
                    S = lift(list(Sp), n_a, a)
                    prof[sum(S) % n] = prof.get(sum(S) % n, 0) + 1
            if prof:
                vals = set(prof.values())
                ck(len(vals) == 1,
                   "(SHELL-STRUCT) structural shells equidistributed %s" % vals)
                tot = sum(prof.values())
                ck(len(prof) * next(iter(vals)) == tot, "profile sums")
                ck(tot == comb(n // w, rp // w) if rp % w == 0 else True,
                   "structural total")
            # (SHELL-ACC) parity rule: sigma'(S') even <=> sig in 2^{a+1} Z
            for Sp in sols:
                S = lift(list(Sp), n_a, a)
                sg = sum(S) % n
                ck((sum(Sp) % 2 == 0) == (sg % (1 << (a + 1)) == 0),
                   "(SHELL-ACC) parity rule S'=%s" % (Sp,))
            print("    (n,w)=(%d,%d) p=%-4d shells: total=%-3d struct=%-3d acc=%-3d"
                  "  (2L=%d, L=%d)  struct/shell=%s"
                  % (n, w, p, len(sigs), len(ssig), len(asig), n_a, L,
                     sorted(set(prof.values())) if prof else "-"))
    return


# --------------------------------------------------------------- mult
def domain_D(L):
    """D = {x in {0,1}^L : x_{L-1} = 0, |x| even}, as bitmasks."""
    out = []
    for msk in range(1 << (L - 1)):
        if bin(msk).count("1") % 2 == 0:
            out.append(msk)
    return out


def stage_mult():
    """(MULT): #{(x,y) in D^2 : x - y = eps} = 2^{L-2-U}, EXACT, exhaustive."""
    print("=== stage mult  (P3.1 / falsifier F3) ===")
    for L in (4, 6, 8):
        D = domain_D(L)
        ck(len(D) == 1 << (L - 2), "|D| = 2^{L-2} at L=%d (got %d)" % (L, len(D)))
        pairs = {}
        for x in D:
            for y in D:
                if x == y:
                    continue
                eps = tuple((((x >> j) & 1) - ((y >> j) & 1)) for j in range(L))
                pairs[eps] = pairs.get(eps, 0) + 1
        for eps, m in pairs.items():
            U = sum(1 for e in eps if e)
            ck(U % 2 == 0, "U even for eps=%s (L=%d)" % (eps, L))
            ck(2 <= U <= L - 2, "2 <= U <= L-2 = r'_a for eps=%s (L=%d)"
               % (eps, L))
            ck(eps[L - 1] == 0, "eps_{L-1} = 0 for eps=%s" % (eps,))
            ck(m == 1 << (L - 2 - U),
               "(MULT) eps=%s U=%d mult=%d expected 2^%d"
               % (eps, U, m, L - 2 - U))
        print("    L=%d: |D|=%d, %d distinct difference vectors, all mult exact"
              % (L, len(D), len(pairs)))
    return


# --------------------------------------------------------------- count
def rho_min(L, ra):
    """min over even U in [2, ra] of C(L-U,(ra-U)/2) / 2^{L-2-U}, EXACT."""
    best = None
    argu = None
    for U in range(2, ra + 1, 2):
        r = Fraction(comb(L - U, (ra - U) // 2), 1 << (L - 2 - U))
        if best is None or r < best:
            best, argu = r, U
    return best, argu


def relations(L, p, theta):
    """all eps in {0,+-1}^L with eps_{L-1}=0, sum eps_j theta^j = 0 in F_p.

    meet-in-the-middle over the two ternary halves."""
    h = (L - 1) // 2
    lo, hi = h, (L - 1) - h
    tp = [pow(theta, j, p) for j in range(L)]

    def enum(idx):
        out = [(0, ())]
        for j in idx:
            nxt = []
            for val, vec in out:
                nxt.append((val, vec + (0,)))
                nxt.append(((val + tp[j]) % p, vec + (1,)))
                nxt.append(((val - tp[j]) % p, vec + (-1,)))
            out = nxt
        return out

    A = enum(range(lo))
    Bd = {}
    for val, vec in enum(range(lo, lo + hi)):
        Bd.setdefault((p - val) % p, []).append(vec)
    res = []
    for val, vec in A:
        for vec2 in Bd.get(val, ()):
            eps = vec + vec2 + (0,)
            if any(eps):
                res.append(eps)
    return res


def count_reduced_mitm(n_a, ra, p, theta):
    """#{S' <= Z/n_a : |S'| = ra, sum_{j in S'} theta^j = 0}, by MITM.

    No lemma used: a direct count over the two halves of Z/n_a."""
    h = n_a // 2
    tp = [pow(theta, j, p) for j in range(n_a)]

    def tab(idx):
        d = [dict() for _ in range(len(idx) + 1)]
        d[0][0] = 1
        for j in idx:
            for sz in range(len(idx) - 1, -1, -1):
                for v, c in list(d[sz].items()):
                    nv = (v + tp[j]) % p
                    d[sz + 1][nv] = d[sz + 1].get(nv, 0) + c
        return d

    A = tab(range(h))
    B = tab(range(h, n_a))
    tot = 0
    for j in range(max(0, ra - (n_a - h)), min(ra, h) + 1):
        for v, c in A[j].items():
            tot += c * B[ra - j].get((p - v) % p, 0)
    return tot


def stage_count():
    """(PAIRS)+(RATIO)+(COUNT): the proved accident lower bound, exhaustive."""
    print("=== stage count  (P3 / falsifier F3 -- the load-bearing new step) ===")
    CASES = [(8, 16, [17]), (16, 32, [97, 193, 257, 353, 449, 577, 641])]
    for (L, n_a, ps) in CASES:
        ra = L - 2
        rmin, argu = rho_min(L, ra)
        ck(argu == 2, "rho_min attained at U=2 (L=%d, got U=%d)" % (L, argu))
        for p in ps:
            if (p - 1) % n_a:
                continue
            theta = unit_of_order(p, n_a)
            D = domain_D(L)
            Q = p  # delta_a = 1 by construction (theta in F_p)
            # exact fibre profile of phi on D
            fib = {}
            for msk in D:
                val = sum(pow(theta, j, p) for j in range(L) if (msk >> j) & 1) % p
                fib[val] = fib.get(val, 0) + 1
            P_true = sum(m * m for m in fib.values()) - len(D)
            P_low = Fraction(len(D) ** 2, Q) - len(D)
            ck(P_true >= P_low, "(PAIRS) Cauchy-Schwarz P >= |D|^2/Q - |D| "
               "(L=%d p=%d): %d vs %s" % (L, p, P_true, float(P_low)))
            # P as the weighted relation sum
            rels = relations(L, p, theta)
            # CATCH: the relation set also contains ODD-support eps.  Those
            # arise from no difference of two D-elements (both have even
            # weight) AND have an EMPTY fibre by LEMMA TC (nonempty iff
            # U = r'_a mod 2, and r'_a = L-2 is even).  They contribute to
            # NEITHER side; restrict both sums to even U.
            rels_even = [e for e in rels if sum(1 for x in e if x) % 2 == 0]
            n_odd = len(rels) - len(rels_even)
            P_rel = sum(1 << (L - 2 - sum(1 for e in eps if e))
                        for eps in rels_even)
            ck(P_rel == P_true,
               "(PAIRS) P = sum_{eps even U} 2^{L-2-U} (L=%d p=%d): %d vs %d"
               % (L, p, P_rel, P_true))
            # exact accident count from the eps with eps_{L-1} = 0, U even
            N_restr = 0
            for eps in rels_even:
                U = sum(1 for e in eps if e)
                ck(2 <= U <= ra, "2 <= U <= r'_a (L=%d p=%d U=%d)" % (L, p, U))
                N_restr += comb(L - U, (ra - U) // 2)
            # the TRUE total accident count (all eps, no eps_{L-1} restriction).
            # Counted by meet-in-the-middle over the two halves of Z/2L, i.e.
            # WITHOUT using LEMMA TC -- an independent count.
            N_true = count_reduced_mitm(n_a, ra, p, theta) - comb(L, ra // 2)
            if L <= 8:  # cross-check the MITM counter by brute force
                brute = sum(1 for Sp in combinations(range(n_a), ra)
                            if sum(pow(theta, j, p) for j in Sp) % p == 0)
                ck(brute == N_true + comb(L, ra // 2),
                   "MITM reduced-solution counter == brute force (L=%d p=%d)"
                   % (L, p))
            ck(N_true >= N_restr,
               "restricted sum <= true accident count (L=%d p=%d): %d <= %d"
               % (L, p, N_restr, N_true))
            bound = rmin * P_low
            ck(N_restr >= bound,
               "(COUNT) N_restr >= rho_min*(|D|^2/Q-|D|) (L=%d p=%d): %d vs %s"
               % (L, p, N_restr, float(bound)))
            ck(N_true >= bound,
               "(COUNT) N_acc >= rho_min*(|D|^2/Q-|D|) (L=%d p=%d): %d vs %s"
               % (L, p, N_true, float(bound)))
            print("    L=%-3d p=%-4d |D|=%-6d rels=%-6d P=%-12d "
                  "N_restr=%-8d N_acc=%-8d bound=%.1f  slack=%.2fx (odd-U rels dropped)"
                  % (L, p, len(D), len(rels_even), P_true, N_restr, N_true,
                     float(bound), N_true / float(bound) if bound > 0 else 0))
        print("    rho_min(L=%d) = %s = %.6f  at U=%d"
              % (L, rmin, float(rmin), argu))
    return


# --------------------------------------------------------------- census
def stage_census():
    """FULL W_w census -> Lemma X, X_w(gamma), deep stratum inside the whole."""
    print("=== stage census  (X_w(gamma) dictionary + Lemma X, FULL census) ===")
    for (n, w, ps) in [(16, 4, [17, 97, 113, 193, 241, 257]),
                       (32, 8, [97, 193, 257, 353, 449])]:
        k = n // 2
        rp = n - k - w
        a, n_a, L, rp2, ra = deep_shape(n, w)
        ck(rp == rp2, "r' consistent at (%d,%d)" % (n, w))
        d = gcd(rp, n)
        for p in ps:
            zeta = unit_of_order(p, n)
            # meet-in-the-middle over the two halves of Z/n
            half = n // 2
            zp = [[pow(zeta, (s * i) % n, p) for i in range(n)]
                  for s in range(w)]

            def vecs(idx, size):
                out = {}
                for S in combinations(idx, size):
                    v = tuple(sum(zp[s][i] for i in S) % p for s in range(1, w))
                    out.setdefault(v, []).append(S)
                return out

            W = []
            for j in range(0, rp + 1):
                if j > half or rp - j > n - half:
                    continue
                A = vecs(range(half), j)
                B = vecs(range(half, n), rp - j)
                for v, SA in A.items():
                    nv = tuple((p - x) % p for x in v)
                    for SB in B.get(nv, ()):
                        for S1 in SA:
                            W.append(tuple(S1) + SB)
            # sig profile
            prof = [0] * n
            for S in W:
                prof[sum(S) % n] += 1
            ck(sum(prof) == len(W), "profile total")
            # Lemma X: fibres equal within each class mod d
            okx = True
            for j in range(d):
                vals = set(prof[t] for t in range(n) if t % d == j)
                if len(vals) != 1:
                    okx = False
            ck(okx, "LEMMA X: sig fibres equal within classes mod d=%d "
                    "(n,w)=(%d,%d) p=%d" % (d, n, w, p))
            # X_w(gamma) IS the sig fibre (x_0 = 1)
            for t in range(n):
                gam = pow(zeta, t, p)
                cnt = sum(1 for S in W if pow(zeta, sum(S) % n, p) == gam)
                ck(cnt == prof[t], "X_w(gamma) = sig fibre at t=%d" % t)
            # structural + deep stratum located inside the FULL census
            struct = [S for S in W if all(((i + n // w) % n) in S for i in S)]
            deep = [S for S in W if all(((i + n_a) % n) in S for i in S)]
            ck(len(struct) == (comb(n // w, rp // w) if rp % w == 0 else 0),
               "structural count inside full census")
            ck(set(struct) <= set(deep), "structural <= deep stratum")
            dsig = set(sum(S) % n for S in deep)
            ck(all(x % (1 << a) == 0 for x in dsig),
               "(SHELL-CONC) inside the FULL census")
            ck(len(dsig) <= n_a, "deep stratum in <= 2L shells (full census)")
            mx = max(prof)
            print("    (n,w)=(%d,%d) p=%-4d |W_w|=%-6d d=%-3d shells occupied=%-3d "
                  "max X_w=%-5d struct=%-4d deep=%-4d deep-shells=%d"
                  % (n, w, p, len(W), d, sum(1 for x in prof if x), mx,
                     len(struct), len(deep), len(dsig)))
    return



# --------------------------------------------------------------- pipeline
def stage_pipeline():
    """END-TO-END: the exact inequality chain used at the prize row, tested
    against the BRUTE-FORCE maximal shell at a toy where accidents are dense.

    chain:  N_acc >= rho_min*(|D|^2/Q - |D|)   [proved]
            max-shell >= N_acc / 2L            [pigeonhole, SHELL-CONC]
    tested against the TRUE per-shell accident profile."""
    print("=== stage pipeline  (end-to-end gate on the prize-row chain) ===")
    # (n,w) = (64,4): a=1, n_a=32, L=16, r'=28, r'_a=14 = L-2
    n, w = 64, 4
    a, n_a, L, rp, ra = deep_shape(n, w)
    ck((a, n_a, L, rp, ra) == (1, 32, 16, 28, 14), "shape (64,4) as expected")
    rmin, argu = rho_min(L, ra)
    for p in [193, 257, 449, 577, 641]:
        theta = unit_of_order(p, n_a)
        D = domain_D(L)
        Q = p
        ck(Q < len(D), "CS non-vacuous at p=%d" % p)
        # TRUE per-shell profile of the reduced solutions, by MITM over the
        # two halves of Z/32, keyed by (p_1 value, sigma' mod n_a).
        h = n_a // 2
        tp = [pow(theta, j, p) for j in range(n_a)]

        def tab(idx):
            d = [dict() for _ in range(len(idx) + 1)]
            d[0][(0, 0)] = 1
            for j in idx:
                for sz in range(len(idx) - 1, -1, -1):
                    for (v, sg), c in list(d[sz].items()):
                        key = ((v + tp[j]) % p, (sg + j) % n_a)
                        d[sz + 1][key] = d[sz + 1].get(key, 0) + c
            return d

        A, B = tab(range(h)), tab(range(h, n_a))
        prof = {}
        for j in range(max(0, ra - (n_a - h)), min(ra, h) + 1):
            for (v, sg), c in A[j].items():
                for sg2 in range(n_a):
                    c2 = B[ra - j].get(((p - v) % p, sg2), 0)
                    if c2:
                        t = (sg + sg2) % n_a
                        prof[t] = prof.get(t, 0) + c * c2
        total = sum(prof.values())
        # structural profile: unions of ra/2 antipodal pairs, exact
        sprof = {}
        for Sp in combinations(range(L), ra // 2):
            sg = sum((2 * j + L) for j in Sp) % n_a
            sprof[sg] = sprof.get(sg, 0) + 1
        stot = sum(sprof.values())
        ck(stot == comb(L, ra // 2), "structural total = C(L, r'_a/2)")
        # (SHELL-CONC) at this shape: sig(S) = 2^a sigma' mod n  (second term 0?)
        sec = ra * n_a * (1 << (a - 1)) * ((1 << a) - 1) % n
        # accident profile, per SIG SHELL of the lift
        aprof = {}
        for t, c in prof.items():
            sg = ((1 << a) * t + sec) % n
            aprof[sg] = aprof.get(sg, 0) + c - sprof.get(t, 0)
        N_acc_true = total - stot
        ck(N_acc_true == sum(aprof.values()), "accident profile sums to N_acc")
        maxshell_true = max(aprof.values())
        bound = rmin * (Fraction(len(D) ** 2, Q) - len(D))
        N_acc_low = int(bound)
        pig = N_acc_low // n_a
        ck(N_acc_true >= N_acc_low,
           "(COUNT) true N_acc %d >= proved lower bound %d (p=%d)"
           % (N_acc_true, N_acc_low, p))
        ck(maxshell_true >= pig,
           "(PIGEONHOLE) true max shell %d >= N_acc_low/2L = %d (p=%d)"
           % (maxshell_true, pig, p))
        ck(len(aprof) <= n_a, "accidents in <= 2L shells (p=%d)" % p)
        print("    p=%-4d shells=%-3d N_acc=%-8d bound=%-8d "
              "max-shell=%-7d pigeonhole=%-7d slack=%.2fx"
              % (p, len(aprof), N_acc_true, N_acc_low, maxshell_true, pig,
                 maxshell_true / pig if pig else 0))
    print("    rho_min(L=%d) = %s at U=%d" % (L, rmin, argu))
    return


def stage_failclosed():
    print("=== stage failclosed  (negative control: MUST exit 1) ===")
    ck(1 == 2, "injected false check")
    return


STAGES = {"siglift": stage_siglift, "dsbiject": stage_dsbiject,
          "shell": stage_shell, "mult": stage_mult, "count": stage_count,
          "census": stage_census, "pipeline": stage_pipeline,
          "failclosed": stage_failclosed}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in STAGES:
        print("usage: toy_shell.py {%s}" % "|".join(STAGES))
        sys.exit(2)
    STAGES[sys.argv[1]]()
    print("checks=%d failures=%d" % (CHECKS, FAILS))
    sys.exit(1 if FAILS else 0)
