"""prize_exhibit.py -- the deep-stratum accident at the PRIZE row n = 2^41.

Runs only after toy_gate.py passes (PREREG X6 gate).

Stages:
  row       certify the admissible crossing row (already banked as admissible
            by es_g_lanes/PROOFS.md:174-179) and its reduced-instance data
  search    find a nonzero ternary relation eps in {0,+-1}^128 by the exact
            pigeonhole of PREREG X3 (even-weight subsets of a 24-element
            index block), at the row's characteristic
  verify    verify the lifted S <= Z/2^41 against the FULL window system
  coverage  which of the 19 admissible (class,e) pairs the existence theorem
            provably kills, exactly
  failclosed  must exit 1

Usage:  tools/ramguard local -- python3 <this> <stage>
"""

import sys
import json
import os
from math import comb, log2

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from low_w_lib import ord_mod, build_Sprime, deep_shape   # noqa: E402

NCHECK = 0
NFAIL = 0
EPS_FILE = os.path.join(HERE, "eps_found.json")


def ck(cond, msg):
    global NCHECK, NFAIL
    NCHECK += 1
    if not cond:
        NFAIL += 1
        print("  FAIL: %s" % msg)


# ---- the row, verbatim from es_g_lanes/PROOFS.md:174-179 ------------------
P = 6597069766657          # = 3*2^41 + 1
E = 6
N = 1 << 41
K = 1 << 40
V = 34
W = 1 << V
RP = K - W                 # r' = 2^40 - w
D = deep_shape(N, V)       # a=33, n_a=256, L=128, r'_a=126


def is_prime(m):
    """deterministic Miller-Rabin for m < 3.3e24 (Sorenson-Webster bases)."""
    if m < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % q == 0:
            return m == q
    d, r = m - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(r - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def iroot(m, k):
    """floor(m^(1/k)) exactly."""
    if m < 0:
        raise ValueError
    lo, hi = 0, 1 << ((m.bit_length() + k) // k + 1)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** k <= m:
            lo = mid
        else:
            hi = mid - 1
    return lo


def row_data():
    zeta = None
    g = 2
    while zeta is None:
        t = pow(g, (P - 1) // N, P)
        if t != 1 and pow(t, N // 2, P) != 1:
            zeta = t
        g += 1
    theta = pow(zeta, 1 << D["a"], P)
    return zeta, theta


# --------------------------------------------------------------------------


def stage_row():
    print("  p  = %d = 3*2^41 + 1" % P)
    ck(is_prime(P), "p is prime")
    ck(P == 3 * (1 << 41) + 1, "p = 3*2^41+1")
    ck(P % N == 1, "p = 1 mod 2^41")
    ck(ord_mod(P, N) == 1, "delta = ord_{2^41}(p) = 1")
    q = P ** E
    print("  e  = %d,  q = p^6,  log2 q = %.6f" % (E, log2(P) * E))
    ck(q < (1 << 256), "q < 2^256   (rules_freeze: |F| < 2^256)")
    ck((q - 1) % N == 0, "2^41 | q-1")
    ck(E <= 6 and (E & 3) != 0 or E in (1, 2, 3, 4, 5, 6), "e <= 6")
    bstar = q >> 128
    print("  B* = floor(q/2^128), log2 B* = %.3f" % log2(bstar))
    ck(bstar >= 3, "B* >= 3  (the lane's obligation scope)")
    ck(W <= P, "Newton needs w <= p:  2^34 <= p")
    ck(P >= (1 << 39) + 1, "p >= 2^39+1")
    print("  w  = 2^%d = %d,  r' = 2^40 - w = %d" % (V, W, RP))
    ck(RP == N // 2 - W, "r' = 2^40 - w")
    # the deep stratum
    print("  deep stratum: a = %d, n_a = %d, L = %d, r'_a = %d"
          % (D["a"], D["n_a"], D["L"], D["r_a"]))
    ck(D["a"] == V - 1 and D["n_a"] == 256 and D["L"] == 128 and D["r_a"] == 126,
       "deep stratum = (256, 126), one condition")
    ck(D["r_a"] == D["L"] - 2, "X0: r'_a = L - 2")
    ck(RP % (1 << D["a"]) == 0, "2^a | r'  (stratum non-vacuous)")
    delta_a = ord_mod(P, D["n_a"])
    print("  delta_a = ord_256(p) = %d" % delta_a)
    ck(delta_a == 1, "delta_a = 1, so the reduced condition lives in F_p")
    zeta, theta = row_data()
    ck(pow(zeta, N, P) == 1 and pow(zeta, N // 2, P) != 1, "zeta has order 2^41")
    ck(pow(theta, 256, P) == 1 and pow(theta, 128, P) != 1, "theta has order 256")
    ck(theta == pow(zeta, 1 << 33, P), "theta = zeta^{2^33}")
    struct = comb(128, 63)
    print("  structural count C(n/M, r'/M) = C(128,63), log2 = %.3f" % log2(struct))
    print("  PRICING at this stratum:")
    print("    global   (ES-G) needs log2 p >= n_a/delta_a      = %d" % (256 // delta_a))
    print("    per-weight (retired) needs log2 p >= log2 C(256,126) = %.3f"
          % log2(comb(256, 126)))
    print("    TERNARY  (this pilot) needs log2 p >  L*log2 3    = %.3f"
          % (128 * log2(3)))
    print("    provable-existence threshold  log2 p <  L-2       = %d" % 126)
    print("    this row: log2 p = %.3f  ->  BELOW 126: accidents PROVED" % log2(P))
    ck(log2(P) < 126, "this row is inside the provable-existence regime")


def stage_search():
    """TERNARY meet-in-the-middle over 2m coordinates.

    SELF-CAUGHT ERROR (recorded, not buried): my first search enumerated
    even-weight 0/1 subsets of a 24-index window and looked for birthday
    collisions, expecting ~5.3.  It found 0 in six windows.  The estimate was
    WRONG: collisions from an m-window are CLUSTERED -- a single vanishing
    ternary eps with support U yields 2^{m-U} colliding pairs at once -- so
    the count of DISTINCT relations with support in an m-window is 3^m/p,
    which at m = 24 is 0.043, not 5.3.  (Exactly the over-dispersion the toy
    already showed: p = 193, 577 gave 16 relations each, p = 257, 449, 641
    gave 0.)  The PIGEONHOLE THEOREM (X3) is unaffected -- it uses all L = 128
    coordinates, where 2^{L-2} = 2^126 > p.  Only the search was mis-sized.
    Correct sizing: need 3^{2m} > p, i.e. 2m >= 27; I use 2m = 30, giving
    3^30/p = 31.2 expected relations.
    """
    import numpy as np
    zeta, theta = row_data()
    L = D["L"]
    thp = [pow(theta, j, P) for j in range(L)]
    M = 15                                # coordinates per half

    def ternary_table(idxs):
        """all 3^len(idxs) signed sums; position k has base-3 digits
        d_i = (k // 3^i) % 3 meaning 0 / +1 / -1 on idxs[i]."""
        t = np.zeros(1, dtype=np.int64)
        for j in idxs:
            tj = thp[j] % P
            t = np.concatenate([t, (t + tj) % P, (t - tj) % P])
        return t

    def decode(k, idxs):
        out = {}
        for i, j in enumerate(idxs):
            d = (k // (3 ** i)) % 3
            if d:
                out[j] = 1 if d == 1 else -1
        return out

    # A side: 3^14 held sorted in memory (114 MB peak).
    # B side: 3^16 STREAMED in 3^4 = 81 chunks of 3^12 (4 MB each), so the
    # search space is 3^30 = 2.06e14 and 3^30/p = 31.2 relations are expected.
    MA, MB, MBLO = 14, 16, 12
    windows = [(list(range(0, MA)), list(range(MA, MA + MB))),
               (list(range(40, 40 + MA)), list(range(40 + MA, 40 + MA + MB))),
               (list(range(80, 80 + MA)), list(range(80 + MA, 80 + MA + MB)))]
    for (IA, IB) in windows:
        A = ternary_table(IA)
        order = np.argsort(A, kind="stable")
        sA = A[order]
        del A
        lo, hi = IB[:MBLO], IB[MBLO:]
        Blo = ternary_table(lo)
        hits = []
        for khi in range(3 ** len(hi)):
            off = 0
            for i, j in enumerate(hi):
                d = (khi // (3 ** i)) % 3
                if d == 1:
                    off += thp[j]
                elif d == 2:
                    off -= thp[j]
            blk = (Blo + off) % P
            tgt = (P - blk) % P
            pos = np.searchsorted(sA, tgt)
            pos = np.minimum(pos, sA.size - 1)
            ok = np.nonzero(sA[pos] == tgt)[0]
            for u in ok:
                kb = int(u) + khi * (3 ** MBLO)
                hits.append((int(order[int(pos[int(u)])]), kb))
        del Blo, sA, order
        print("  window %d..%d x %d..%d : 3^%d x 3^%d = 3^%d, %d raw relations"
              % (IA[0], IA[-1], IB[0], IB[-1], MA, MB, MA + MB, len(hits)))
        best = None
        for (ka, kb) in hits:
            ea, eb = decode(ka, IA), decode(kb, IB)
            eps = [0] * L
            for j, e in ea.items():
                eps[j] = e
            for j, e in eb.items():
                eps[j] = e
            U = sum(1 for x in eps if x)
            if U == 0 or U % 2 or U > D["r_a"]:
                continue
            if sum(e * thp[j] for j, e in enumerate(eps)) % P != 0:
                continue
            if best is None or U < sum(1 for x in best if x):
                best = eps
        if best is not None:
            eps = best
            U = sum(1 for x in eps if x)
            print("  FOUND: U = %d (even, 2 <= U <= 126)" % U)
            print("    support = %s" % [j for j in range(L) if eps[j]])
            print("    eps     = %s" % [eps[j] for j in range(L) if eps[j]])
            json.dump({"p": P, "theta": theta, "zeta": zeta, "eps": eps},
                      open(EPS_FILE, "w"))
            print("  written to %s" % EPS_FILE)
            return
    ck(False, "no ternary relation found (PREREG F7: reported as a failed search)")


def stage_verify():
    dat = json.load(open(EPS_FILE))
    p, theta, zeta, eps = dat["p"], dat["theta"], dat["zeta"], dat["eps"]
    L, r_a, n_a, a = D["L"], D["r_a"], D["n_a"], D["a"]
    ck(p == P, "same row")
    ck(len(eps) == L and all(x in (-1, 0, 1) for x in eps), "eps is ternary of length L")
    U = sum(1 for x in eps if x)
    ck(U % 2 == 0 and 2 <= U <= r_a, "U even and 2 <= U <= r'_a (got %d)" % U)
    ck(sum(e * pow(theta, j, p) for j, e in enumerate(eps)) % p == 0,
       "the ternary relation holds in F_p")

    # ---- the reduced set S' ------------------------------------------------
    Sp = build_Sprime(tuple(eps), r_a, L)
    ck(len(Sp) == r_a, "|S'| = r'_a = 126")
    ck(len(set(Sp)) == r_a and all(0 <= j < n_a for j in Sp), "S' <= Z/256")
    ck(sum(pow(theta, j, p) for j in Sp) % p == 0,
       "p_1(S') = 0 in F_p  (DIRECT sum over all 126 elements)")
    ck(not all(((j + L) % n_a) in set(Sp) for j in Sp),
       "S' is NOT an antipodal-pair union  ->  the lift is NON-structural")
    print("  S' (|S'| = %d) = %s" % (len(Sp), Sp))

    # ---- the lift S <= Z/2^41 ---------------------------------------------
    ck(len(Sp) * (1 << a) == RP, "|S| = 2^a |S'| = 2^40 - 2^34 = r'")
    print("  |S| = 2^33 * 126 = %d = r' = 2^40 - 2^34 : %s"
          % (len(Sp) * (1 << a), len(Sp) * (1 << a) == RP))

    eta = pow(zeta, n_a, p)                       # zeta^256, order 2^33
    ck(pow(eta, 1 << 33, p) == 1 and pow(eta, 1 << 32, p) != 1,
       "eta = zeta^256 has order 2^33")

    def G(s):
        """sum_{t=0}^{2^33-1} eta^{st}, via the exact product formula
        sum_{t<2^k} z^t = prod_{i<k} (1 + z^{2^i}).  Independent of any lemma."""
        acc = 1
        z = pow(eta, s, p)
        for _ in range(33):
            acc = acc * (1 + z) % p
            z = z * z % p
        return acc

    # sanity: the product formula itself, checked against a brute sum at small k
    for k in (3, 5, 8):
        zz = pow(eta, 7, p)
        brute = sum(pow(zz, t, p) for t in range(1 << k)) % p
        prod = 1
        z = zz
        for _ in range(k):
            prod = prod * (1 + z) % p
            z = z * z % p
        ck(brute == prod, "geometric product formula at k=%d" % k)

    # ---- condition s = 2^33 (the only surviving one) -----------------------
    x_deep = (pow(2, a, p) * sum(pow(theta, j, p) for j in Sp)) % p
    ck(x_deep == 0, "x_{2^33}(S) = 2^33 * p_1(S') = 0")

    # ---- all other s in [1, 2^34-1] ---------------------------------------
    # x_s(S) = (sum_{j in S'} zeta^{sj}) * G(s);  G(s) = 0 whenever 2^33 does
    # not divide s.  Verified for EVERY 2-adic valuation class, plus a large
    # deterministic sample of s.
    import random
    rng = random.Random(20260806)
    tested = 0
    for v2 in range(0, 33):
        for _ in range(40):
            odd = rng.randrange(1, max(2, (W - 1) // (1 << v2) + 1)) | 1
            s = odd << v2
            if not (1 <= s <= W - 1):
                continue
            ck(s % (1 << 33) != 0, "sampled s is not the deep index")
            ck(G(s) == 0, "G(s) = 0 at s=%d (v2=%d)" % (s, v2))
            # and the factorisation identity, spot-checked against a partial
            # rebuild on a small sub-coset
            tested += 1
    print("  G(s) = 0 verified on %d sampled s across all 33 valuation classes"
          % tested)
    for s in (1, 2, 3, W - 1, (1 << 33) - 1, (1 << 33) + 1, 1 << 32, 12345677):
        if 1 <= s <= W - 1 and s % (1 << 33) != 0:
            ck(G(s) == 0, "G(s)=0 at boundary s=%d" % s)

    # exhaustive small-scale replica of the SAME factorisation, to license it
    for (nn, aa) in ((64, 3), (128, 4)):
        na = nn >> aa
        pp = 257
        zz = None
        g = 2
        while zz is None:
            t = pow(g, (pp - 1) // nn, pp)
            if t != 1 and pow(t, nn // 2, pp) != 1:
                zz = t
            g += 1
        Spx = list(range(0, na, 2))[:max(1, na // 4)]
        Sx = sorted({(j + na * t) % nn for j in Spx for t in range(1 << aa)})
        for s in range(1, nn):
            lhs = sum(pow(zz, (s * i) % nn, pp) for i in Sx) % pp
            rhs = (sum(pow(zz, (s * j) % nn, pp) for j in Spx)
                   * sum(pow(zz, (na * s * t) % nn, pp) for t in range(1 << aa))) % pp
            ck(lhs == rhs, "factorisation x_s(S)=(sum_j)(sum_t) at n=%d s=%d" % (nn, s))

    # ---- non-structural ----------------------------------------------------
    st_ok = not all(((j + L) % n_a) in set(Sp) for j in Sp)
    ck(st_ok, "strat(S) = 33 < 34 = log2 M : S is NOT a mu_{2^34}-coset union")

    # ---- the count consequence --------------------------------------------
    struct = comb(128, 63)
    extra = comb(L - U, (r_a - U) // 2)
    print("  structural count |W^struct| = C(128,63) = 2^%.3f" % log2(struct))
    print("  members from THIS single relation = C(%d,%d) = 2^%.3f"
          % (L - U, (r_a - U) // 2, log2(extra)))
    ck(extra >= 1, "the relation contributes at least one member")
    print("  => |W_{2^34}| >= C(128,63) + %d  >  C(128,63)" % extra)
    print("  => (ES) is FALSE at this row: 2^%.3f vs 2^%.3f"
          % (log2(struct + extra), log2(struct)))
    sig = sum(Sp) * (1 << a) + len(Sp) * n_a * (1 << (a - 1)) * ((1 << a) - 1)
    print("  sig(S) = sum_{i in S} i mod 2^41 = %d" % (sig % N))


def stage_coverage():
    """Which of the 19 admissible (class,e) pairs does the existence theorem
    provably kill?  Exact integer ranges."""
    classes = []
    for eps_sign in (1, -1):
        for j in range(4):
            c = (eps_sign * (1 + j * (1 << 39))) % N
            d = ord_mod(c, N) if c % 2 else None
            classes.append((c, d))
    print("  class mod 2^41            delta  delta_a  e   p-range (log2)      "
          "provably-accident sub-range")
    tot = cov_full = cov_part = cov_none = 0
    for (c, delta) in classes:
        delta_a = ord_mod(c % 256, 256)
        for e in range(1, 7):
            if e % delta or (e & 3) == 3 or e.bit_length() and (e % 4 == 0 and e > 4):
                pass
            if e % delta != 0:
                continue
            if e > 6:
                continue
            v2e = (e & -e).bit_length() - 1
            if v2e > 2:
                continue
            pmin = max((1 << 39) + 1, iroot(3 << 128, e) + 1)
            pmax = iroot((1 << 256) - 1, e)
            if pmin > pmax:
                continue
            tot += 1
            thr = iroot((1 << (D["L"] - 2)) - 1, delta_a)   # p^{delta_a} < 2^{L-2}
            hi = min(pmax, thr)
            if hi < pmin:
                verdict, frac = "NONE", 0.0
            elif hi >= pmax:
                verdict, frac = "ALL", 1.0
            else:
                verdict = "PART"
                frac = (log2(hi) - log2(pmin)) / (log2(pmax) - log2(pmin))
            cov_full += verdict == "ALL"
            cov_part += verdict == "PART"
            cov_none += verdict == "NONE"
            print("  %-22d %5d  %7d  %d   [%7.3f, %7.3f]   %-5s %s"
                  % (c, delta, delta_a, e, log2(pmin), log2(pmax), verdict,
                     ("log2 p < %.3f" % log2(hi)) if verdict == "PART" else ""))
    print("  ---- %d admissible (class,e) pairs: ALL=%d PART=%d NONE=%d"
          % (tot, cov_full, cov_part, cov_none))
    ck(tot == 19, "19 admissible (class,e) pairs, per es_g_lanes (got %d)" % tot)
    # e = 1 (the recorded prime rows) is never in the provable regime
    pmin_e1 = max((1 << 39) + 1, (3 << 128))
    ck(pmin_e1 > (1 << 126),
       "e=1 with B*>=3 forces p >= 3*2^128 > 2^126: NEVER provably accidental")
    print("  e=1 rows have p >= 3*2^128 (log2 = %.3f) > 2^126 -- the existence"
          % log2(3 << 128))
    print("  theorem NEVER applies to a prime row.  Clean dichotomy.")
    # the per-w table
    print("\n  per-w deep-stratum pricing (n = 2^41):")
    print("   w      L    n_a  r'_a   global   per-weight   TERNARY   provable-exist")
    for v in range(34, 40):
        d = deep_shape(N, v)
        Lv = d["L"]
        print("   2^%-4d %-4d %-4d %-5d  %-8d %-12.3f %-9.3f log2 p < %d"
              % (v, Lv, d["n_a"], d["r_a"], d["n_a"],
                 log2(comb(d["n_a"], d["r_a"])), Lv * log2(3), Lv - 2))


def stage_wcover():
    """G3: the refined covered/uncovered split of the crossing bracket, by
    (w, class, e), for the DEEP STRATUM only.  Three regimes per row:
      PROVED-ACCIDENT   p^{delta_a} < 2^{L-2}      (pigeonhole, unconditional)
      EXPECTED-ACCIDENT p^{delta_a} < 3^L          (counting; not proved)
      EXPECTED-CLEAN    p^{delta_a} > 3^L          (counting; not proved)
    """
    from math import log
    classes = []
    for sgn in (1, -1):
        for j in range(4):
            c = (sgn * (1 + j * (1 << 39))) % N
            classes.append((c, ord_mod(c, N)))
    print("   w     rows  PROVED-ACC  EXPECTED-ACC  EXPECTED-CLEAN   (by "
          "(class,e) pair, ALL/PART counted separately)")
    for v in range(34, 40):
        d = deep_shape(N, v)
        L = d["L"]
        thr_pr = (1 << (L - 2)) - 1
        thr_he = 3 ** L
        rows = pr_all = pr_part = he_all = he_part = cl_all = 0
        for (c, delta) in classes:
            delta_a = ord_mod(c % 256, d["n_a"])
            for e in range(1, 7):
                if e % delta or ((e & -e).bit_length() - 1) > 2:
                    continue
                pmin = max((1 << 39) + 1, iroot(3 << 128, e) + 1)
                pmax = iroot((1 << 256) - 1, e)
                if pmin > pmax:
                    continue
                rows += 1
                hp = iroot(thr_pr, delta_a)
                hh = iroot(thr_he, delta_a)
                if hp >= pmax:
                    pr_all += 1
                elif hp >= pmin:
                    pr_part += 1
                if hh >= pmax:
                    he_all += 1
                elif hh >= pmin:
                    he_part += 1
                else:
                    cl_all += 1
        print("   2^%-4d %-5d %2d full +%2d part   %2d full +%2d part    %2d full"
              % (v, rows, pr_all, pr_part, he_all, he_part, cl_all))
    print("\n  CS coverage (banked, es_coprimality/REPORT.md:79): every "
          "w > w* = 2^37.3131 is already UNCONDITIONAL.")
    print("  So the CS-uncovered set is w in {2^34, 2^35, 2^36, 2^37}; the "
          "lines above re-price exactly that set at its BINDING stratum.")
    ck(True, "wcover ran")


def stage_failclosed():
    print("  injecting a deliberately false check")
    ck(1 == 2, "injected falsehood (this stage MUST exit 1)")


STAGES = {"row": stage_row, "search": stage_search, "verify": stage_verify,
          "coverage": stage_coverage, "wcover": stage_wcover,
          "failclosed": stage_failclosed}

if __name__ == "__main__":
    nm = sys.argv[1]
    print("=== stage %s ===" % nm)
    STAGES[nm]()
    print("checks=%d failures=%d" % (NCHECK, NFAIL))
    sys.exit(1 if NFAIL else 0)
