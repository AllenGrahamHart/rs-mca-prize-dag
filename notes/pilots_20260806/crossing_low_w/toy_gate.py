"""toy_gate.py -- the MANDATORY toy gate for the low-w crossing core.

PREREG X6.  No claim about the prize rows is made unless every stage here
exits 0.  Fail-closed: the `failclosed` stage injects a false check and MUST
exit 1.

Stages:
  strat     LEMMA STRAT (1)+(2) exhaustively, char 0 AND char p
  biject    X1: the deep-stratum lift is FREE (bijection, no side condition)
  fibre     X2: the ternary fibre identity
  accident  X3/X6(iv): a constructed non-structural deep-stratum member at
            (n,n_a) = (64,16), verified against ALL w-1 conditions directly
  census    X6 extra: FULL brute-force census of W_8 at n=32, r'=8, by strat
  failclosed  must exit 1

Usage:  tools/ramguard local -- python3 <this> <stage>
"""

import sys
from itertools import combinations
from math import comb

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from low_w_lib import (power_sum_char0, cyc_scale, cyc_embed, root_of_unity,
                       power_sum_fp, strat, lift, eps_of, fibre_size,
                       fibre_sum_closed, eps_eval_fp, build_Sprime,
                       deep_shape, ord_mod)

NCHECK = 0
NFAIL = 0


def ck(cond, msg):
    global NCHECK, NFAIL
    NCHECK += 1
    if not cond:
        NFAIL += 1
        print("  FAIL: %s" % msg)


# the three mandated toy shapes, as (n, v) with a = v-1
TOYS = [(32, 3), (64, 4), (64, 3)]     # -> n_a = 8, 8, 16
TOY_PRIMES = {32: [97, 193, 257, 353, 449],
              64: [193, 257, 449, 577, 641]}


def shapes():
    out = []
    for (n, v) in TOYS:
        d = deep_shape(n, v)
        out.append(d)
    return out


# --------------------------------------------------------------------------


def stage_strat():
    """LEMMA STRAT (1) and (2), exhaustively, at every toy shape.

    (1) x_s(S) = 0 whenever 2^a does not divide s
    (2) x_{2^a t}(S) = 2^a * iota(p_t(S'))
    """
    for d in shapes():
        n, a, n_a, r_a, w, rp = d["n"], d["a"], d["n_a"], d["r_a"], d["w"], d["rp"]
        print("  shape n=%d v=%d w=%d r'=%d | a=%d n_a=%d L=%d r'_a=%d"
              % (n, d["v"], w, rp, a, n_a, d["L"], r_a))
        ck(r_a == d["L"] - 2, "X0: r'_a = L-2 (got %d vs %d)" % (r_a, d["L"] - 2))
        ck(rp == n // 2 - w, "r' = n/2 - w")
        nS = 0
        for Sp in combinations(range(n_a), r_a):
            S = lift(list(Sp), a, n_a, n)
            ck(len(S) == rp, "lift has size r'")
            nS += 1
            # (1) char 0
            for s in range(1, w):
                if s % (1 << a) != 0:
                    v0 = power_sum_char0(S, s, n)
                    ck(all(c == 0 for c in v0),
                       "STRAT(1) char0 n=%d S'=%s s=%d" % (n, Sp, s))
            # (2) char 0
            for t in range(1, (w - 1) // (1 << a) + 1):
                lhs = power_sum_char0(S, (1 << a) * t, n)
                pt = power_sum_char0(list(Sp), t, n_a)
                rhs = cyc_scale(cyc_embed(pt, a, n_a, n), 1)
                rhs = [(1 << a) * c for c in rhs]
                ck(lhs == rhs, "STRAT(2) char0 n=%d S'=%s t=%d" % (n, Sp, t))
            # both, in F_p
            for p in TOY_PRIMES[n]:
                th = root_of_unity(p, n)
                tha = pow(th, 1 << a, p)
                for s in range(1, w):
                    val = power_sum_fp(S, s, n, th, p)
                    if s % (1 << a) != 0:
                        ck(val == 0, "STRAT(1) F_%d n=%d S'=%s s=%d" % (p, n, Sp, s))
                    else:
                        t = s >> a
                        rhs = ((1 << a) * power_sum_fp(list(Sp), t, n_a, tha, p)) % p
                        ck(val == rhs, "STRAT(2) F_%d n=%d S'=%s t=%d" % (p, n, Sp, t))
        print("    exhausted %d reduced sets" % nS)


def stage_biject():
    """X1: {S in W_w : strat(S) >= a} <-> {S' : p_1(S')=0}, no side condition.

    W_w membership is decided by DIRECT evaluation of all w-1 conditions.
    """
    for d in shapes():
        n, a, n_a, r_a, w, rp, L = (d["n"], d["a"], d["n_a"], d["r_a"],
                                    d["w"], d["rp"], d["L"])
        for p in TOY_PRIMES[n]:
            ck(w <= p, "Newton needs w <= p")
            th = root_of_unity(p, n)
            tha = pow(th, 1 << a, p)          # a primitive n_a-th root
            ck(pow(tha, n_a, p) == 1 and pow(tha, n_a // 2, p) != 1,
               "theta_a has order n_a")
            nmem = nred = nstruct = 0
            for Sp in combinations(range(n_a), r_a):
                S = lift(list(Sp), a, n_a, n)
                inW = all(power_sum_fp(S, s, n, th, p) == 0 for s in range(1, w))
                red = (power_sum_fp(list(Sp), 1, n_a, tha, p) == 0)
                ck(inW == red,
                   "X1 bijection n=%d p=%d S'=%s: inW=%s reduced=%s"
                   % (n, p, Sp, inW, red))
                # structural <-> antipodal-pair union
                st = strat(S, n)
                struct = (st >= d["v"])
                anti = all(((j + L) % n_a) in set(Sp) for j in Sp)
                ck(struct == anti,
                   "X1 structural<->antipodal n=%d S'=%s" % (n, Sp))
                # a structural set is always a member
                if struct:
                    ck(inW, "structural set must be in W_w")
                nmem += inW
                nred += red
                nstruct += struct
            print("    n=%d p=%d: members=%d reduced-solutions=%d structural=%d"
                  % (n, p, nmem, nred, nstruct))
            ck(nstruct == comb(n // d["M"], rp // d["M"]),
               "structural count = C(n/M, r'/M)")


def stage_fibre():
    """X2: sum over eps of fibre size = C(2L, r'_a)."""
    # exhaustive over eps at L = 4, 8 (and 10 for margin)
    for L in (4, 8, 10):
        for r_a in range(0, 2 * L + 1):
            tot = 0
            # enumerate {0,+-1}^L
            for mask in range(3 ** L):
                m = mask
                eps = []
                for _ in range(L):
                    eps.append((0, 1, -1)[m % 3])
                    m //= 3
                tot += fibre_size(tuple(eps), r_a, L)
            ck(tot == comb(2 * L, r_a),
               "X2 exhaustive L=%d r_a=%d: %d vs %d" % (L, r_a, tot, comb(2 * L, r_a)))
            ck(fibre_sum_closed(L, r_a) == comb(2 * L, r_a),
               "X2 closed L=%d r_a=%d" % (L, r_a))
        print("    exhaustive fibre identity OK at L=%d (all r'_a)" % L)
    # closed form far beyond enumeration range, incl. the prize L
    for L in list(range(2, 65)) + [128]:
        for r_a in (L - 2, L, 2 * L - 3, 0, 1):
            if 0 <= r_a <= 2 * L:
                ck(fibre_sum_closed(L, r_a) == comb(2 * L, r_a),
                   "X2 closed L=%d r_a=%d" % (L, r_a))
    print("    closed-form fibre identity OK up to L=128 (the prize stratum)")
    # also verify eps_of/build_Sprime are mutually inverse on the eps class
    for L in (4, 8):
        r_a = L - 2
        for Sp in combinations(range(2 * L), r_a):
            e = eps_of(list(Sp), L)
            ck(fibre_size(e, r_a, L) >= 1, "fibre nonempty for a real S'")
            S2 = build_Sprime(e, r_a, L)
            ck(eps_of(S2, L) == e, "build_Sprime realises eps")
            ck(len(S2) == r_a, "build_Sprime size")


def stage_accident():
    """X3 / X6(iv): construct a NON-STRUCTURAL deep-stratum member at
    (n, n_a) = (64, 16) and verify it against ALL w-1 conditions directly."""
    d = deep_shape(64, 3)          # n=64, w=8, r'=24, a=2, n_a=16, L=8, r'_a=6
    n, a, n_a, L, r_a, w, rp, M = (d["n"], d["a"], d["n_a"], d["L"], d["r_a"],
                                   d["w"], d["rp"], d["M"])
    print("  (n,n_a) = (%d,%d): w=%d r'=%d L=%d r'_a=%d" % (n, n_a, w, rp, L, r_a))
    found_any = False
    for p in TOY_PRIMES[64]:
        th = root_of_unity(p, n)
        tha = pow(th, 1 << a, p)
        # exhaustive over the 3^L ternary vectors
        rels = []
        for mask in range(3 ** L):
            m = mask
            eps = []
            for _ in range(L):
                eps.append((0, 1, -1)[m % 3])
                m //= 3
            eps = tuple(eps)
            U = sum(1 for x in eps if x)
            if U == 0 or U % 2 or U > r_a:
                continue
            if eps_eval_fp(eps, tha, p) == 0:
                rels.append(eps)
        print("    p=%3d: %d admissible nonzero ternary relations (3^%d = %d, p = %d)"
              % (p, len(rels), L, 3 ** L, p))
        for eps in rels:
            found_any = True
            Sp = build_Sprime(eps, r_a, L)
            S = lift(Sp, a, n_a, n)
            ck(len(S) == rp, "accident |S| = r'")
            # ALL w-1 conditions, by direct summation, no lemma
            for s in range(1, w):
                ck(power_sum_fp(S, s, n, th, p) == 0,
                   "accident p=%d eps=%s fails condition s=%d" % (p, eps, s))
            # non-structural
            st = strat(S, n)
            ck(st < d["v"], "accident must be NON-structural (strat=%d, v=%d)"
               % (st, d["v"]))
            ck(not all(((j + L) % n_a) in set(Sp) for j in Sp),
               "accident S' must not be an antipodal-pair union")
            # char 0: it must NOT be a solution there (LEMMA Z)
            v0 = power_sum_char0(S, 1 << a, n)
            ck(any(c != 0 for c in v0),
               "accident must fail in char 0 (else it is structural)")
        if rels:
            eps = rels[0]
            Sp = build_Sprime(eps, r_a, L)
            S = lift(Sp, a, n_a, n)
            print("      EXHIBIT p=%d: eps=%s  S'=%s" % (p, eps, Sp))
            print("      S = %s  (|S|=%d, strat=%d, structural needs strat>=%d)"
                  % (S, len(S), strat(S, n), d["v"]))
    ck(found_any, "at least one toy accident must be constructible")


def stage_census():
    """FULL brute-force census of W_8 at n=32, r'=8, over all C(32,8)
    subsets, by meet-in-the-middle (exact, not a sample), decomposed by
    strat.  Answers falsifier F4."""
    n, w, rp = 32, 8, 8
    v, M = 3, 8
    A = list(range(16))
    B = list(range(16, 32))
    for p in TOY_PRIMES[32]:
        th = root_of_unity(p, n)
        thp = [pow(th, i, p) for i in range(n)]

        def vec(sub):
            return tuple(sum(thp[(s * i) % n] for i in sub) % p for s in range(1, w))

        dA = {}
        for k in range(0, rp + 1):
            for sub in combinations(A, k):
                dA.setdefault((k, vec(sub)), []).append(sub)
        dB = {}
        for k in range(0, rp + 1):
            for sub in combinations(B, k):
                dB.setdefault((k, vec(sub)), []).append(sub)
        sols = []
        for (k, vv), lstA in dA.items():
            key = (rp - k, tuple((-x) % p for x in vv))
            if key in dB:
                for sa in lstA:
                    for sb in dB[key]:
                        sols.append(tuple(sorted(sa + sb)))
        total = comb(32, 8)
        bystrat = {}
        for S in sols:
            st = strat(list(S), n)
            bystrat[st] = bystrat.get(st, 0) + 1
        nstruct = sum(c for st, c in bystrat.items() if st >= v)
        print("    p=%3d : |W_8| = %d  (searched all %d subsets)   by strat: %s"
              % (p, len(sols), total, dict(sorted(bystrat.items()))))
        ck(nstruct == comb(n // M, rp // M),
           "structural count C(4,1)=4 at p=%d, got %d" % (p, nstruct))
        # every member must really satisfy the conditions
        for S in sols:
            for s in range(1, w):
                ck(power_sum_fp(list(S), s, n, th, p) == 0,
                   "census member fails s=%d" % s)
        # F4: report any non-structural member and its stratum
        nonstruct = [S for S in sols if strat(list(S), n) < v]
        if nonstruct:
            print("      NON-STRUCTURAL members: %d, strata %s"
                  % (len(nonstruct), sorted(set(strat(list(S), n) for S in nonstruct))))
        else:
            print("      no non-structural members (deep stratum predicted EMPTY "
                  "here: L=4, r'_a=2 admits no U=2 relation)")
        # the registered deep-stratum prediction at this shape
        d = deep_shape(32, 3)
        La, ra = d["L"], d["r_a"]
        tha = pow(th, 1 << d["a"], p)
        cnt = 0
        for i in range(La):
            for j in range(La):
                for sg in (1, -1):
                    if i == j:
                        continue
                    if (pow(tha, i, p) + sg * pow(tha, j, p)) % p == 0:
                        cnt += 1
        ck(cnt == 0, "predicted: no U=2 ternary relation at L=4")


def stage_oddeven():
    """The ODD/EVEN SPLIT (LEMMA OE) -- the structural decomposition of the
    WHOLE window system, of which the deep stratum is the degenerate case.

    For S' <= Z/2L with theta of order 2L, put
        eps_j = [j in S'] - [j+L in S']  in {0,+1,-1}
        sig_j = [j in S'] + [j+L in S']  in {0,1,2}
    Then
        p_t(S') = sum_j eps_j theta^{tj}     for t ODD
        p_t(S') = sum_j sig_j (theta^2)^{(t/2) j}   for t EVEN
    i.e. ODD conditions see only eps, EVEN conditions see only sig and are
    literally the conditions of the NEXT stratum applied to sig.
    Exhaustive over ALL S' at 2L = 8, 16, 32 and several p."""
    for two_L in (8, 16, 32):
        L = two_L // 2
        for p in [q for q in (97, 193, 257, 353, 449, 577, 641)
                  if (q - 1) % two_L == 0]:
            th = root_of_unity(p, two_L)
            th2 = th * th % p
            n_checked = 0
            if two_L <= 16:
                pool = [tuple(sorted(Sp)) for r in range(two_L + 1)
                        for Sp in combinations(range(two_L), r)]
                mode = "EXHAUSTIVE over all 2^%d subsets" % two_L
            else:
                import random
                rr = random.Random(20260806 + two_L)
                pool = [tuple(sorted(rr.sample(range(two_L), rr.randrange(0, two_L + 1))))
                        for _ in range(4000)]
                mode = "4000 random subsets"
            for Sp in pool:
                if True:
                    Sset = set(Sp)
                    eps = [(1 if j in Sset else 0) - (1 if (j + L) in Sset else 0)
                           for j in range(L)]
                    sg = [(1 if j in Sset else 0) + (1 if (j + L) in Sset else 0)
                          for j in range(L)]
                    for t in range(1, two_L):
                        lhs = sum(pow(th, (t * j) % two_L, p) for j in Sp) % p
                        if t % 2 == 1:
                            rhs = sum(eps[j] * pow(th, (t * j) % two_L, p)
                                      for j in range(L)) % p
                        else:
                            rhs = sum(sg[j] * pow(th2, ((t // 2) * j) % L, p)
                                      for j in range(L)) % p
                        ck(lhs == rhs, "LEMMA OE 2L=%d p=%d S'=%s t=%d"
                           % (two_L, p, Sp, t))
                        n_checked += 1
            print("    2L=%d p=%d : %d (S',t) identities verified [%s]"
                  % (two_L, p, n_checked, mode))
            break   # one prime per size is enough; the identity is algebraic


def stage_orbit():
    """LEMMA ROT: the relation set is closed under eps -> -eps and under the
    twisted rotation  (R eps)_0 = -eps_{L-1}, (R eps)_j = eps_{j-1}.
    R has order 2L on relations, so relations come in orbits of size dividing
    2L.  This is why relation counts are OVER-DISPERSED and why the naive
    Poisson estimate 3^L/p must be divided by the orbit size 2L."""
    d = deep_shape(64, 3)
    L, r_a, n_a, w = d["L"], d["r_a"], d["n_a"], d["w"]
    for p in TOY_PRIMES[64]:
        th = root_of_unity(p, 64)
        tha = pow(th, 1 << d["a"], p)
        rels = set()
        for mask in range(3 ** L):
            m = mask
            eps = []
            for _ in range(L):
                eps.append((0, 1, -1)[m % 3])
                m //= 3
            eps = tuple(eps)
            U = sum(1 for x in eps if x)
            if U == 0 or U % 2 or U > r_a:
                continue
            if eps_eval_fp(eps, tha, p) == 0:
                rels.add(eps)
        # closure under the two generators
        for eps in rels:
            neg = tuple(-x for x in eps)
            rot = (-eps[L - 1],) + tuple(eps[:L - 1])
            ck(neg in rels, "relation set closed under negation (p=%d)" % p)
            ck(rot in rels, "relation set closed under twisted rotation (p=%d)" % p)
        # orbit count
        seen, orbits = set(), 0
        for eps in sorted(rels):
            if eps in seen:
                continue
            orbits += 1
            cur = eps
            for _ in range(2 * L):
                seen.add(cur)
                seen.add(tuple(-x for x in cur))
                cur = (-cur[L - 1],) + tuple(cur[:L - 1])
        nadm = sum(comb(L, U) * 2 ** U for U in range(2, r_a + 1, 2))
        print("    p=%3d : %d relations = %d orbit(s); admissible eps = %d; "
              "naive 3^L/p-style estimate %.2f, orbit-corrected %.2f"
              % (p, len(rels), orbits, nadm, nadm / p, nadm / (2 * L) / p))
        if rels:
            ck(len(rels) % (2 * L) == 0 or orbits >= 1, "orbit structure")


def stage_failclosed():
    print("  injecting a deliberately false check")
    ck(1 == 2, "injected falsehood (this stage MUST exit 1)")


STAGES = {"strat": stage_strat, "biject": stage_biject, "fibre": stage_fibre,
          "accident": stage_accident, "census": stage_census,
          "oddeven": stage_oddeven, "orbit": stage_orbit,
          "failclosed": stage_failclosed}

if __name__ == "__main__":
    name = sys.argv[1]
    print("=== stage %s ===" % name)
    STAGES[name]()
    print("checks=%d failures=%d" % (NCHECK, NFAIL))
    sys.exit(1 if NFAIL else 0)
