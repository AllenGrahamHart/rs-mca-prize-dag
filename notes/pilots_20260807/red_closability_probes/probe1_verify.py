#!/usr/bin/env python3
"""PROBE 1 verifier: integer_code_distance_cert vs THEOREM Z-1 / THEOREM Z-2.

Round 21, notes/pilots_20260807/red_closability_probes/.
Stdlib only.  Run under:  tools/ramguard local -- python3 <this>  [stage]

Stages (registered in PREREG.md P4 as V1-V5):
  hyp        the hypothesis-match arithmetic (H1-H4), pinned constants
  rank1      verify multi_multiplier_reduction Lemma 1 (rank 1 for every k)
  fold       the fold lemma: min non-cyclotomic ternary SUPPORT == min folded l1
  box        V1/V2/V3 exact min folded l1 weight at 2-power cells
  tight      the ell=1 floor 2*1+1 = 3 is ATTAINED, hence unimprovable
  poscontrol V4: the genuine ell-condition system, and the shift scope
  catch      the Galois/Frobenius symmetry claim of weight_graded_mitm
  failclosed V5: a control that MUST exit 1
  all        everything except failclosed
"""
import sys

FAILURES = []
CHECKS = [0]


def check(name, cond, detail=""):
    CHECKS[0] += 1
    if not cond:
        FAILURES.append("%s  %s" % (name, detail))
        print("  FAIL  %s  %s" % (name, detail))
    return cond


# ----------------------------------------------------------------- helpers

def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def exact_order_element(order, p):
    """Return z in F_p of EXACT multiplicative order `order`, or None."""
    if (p - 1) % order:
        return None
    for g in range(2, p):
        z = pow(g, (p - 1) // order, p)
        # exact order check: z^order == 1 and z^(order/l) != 1 for every prime l | order
        if pow(z, order, p) != 1:
            continue
        ok = True
        m, ls = order, set()
        d = 2
        while d * d <= m:
            if m % d == 0:
                ls.add(d)
                while m % d == 0:
                    m //= d
            d += 1
        if m > 1:
            ls.add(m)
        for l in ls:
            if pow(z, order // l, p) == 1:
                ok = False
                break
        if ok:
            return z
    return None


def rank_mod_p(rows, p):
    rows = [list(r) for r in rows]
    ncol = len(rows[0])
    rank, prow = 0, 0
    for col in range(ncol):
        piv = None
        for i in range(prow, len(rows)):
            if rows[i][col] % p:
                piv = i
                break
        if piv is None:
            continue
        rows[prow], rows[piv] = rows[piv], rows[prow]
        inv = pow(rows[prow][col], p - 2, p)
        rows[prow] = [(x * inv) % p for x in rows[prow]]
        for i in range(len(rows)):
            if i != prow and rows[i][col] % p:
                f = rows[i][col]
                rows[i] = [(rows[i][j] - f * rows[prow][j]) % p for j in range(ncol)]
        rank += 1
        prow += 1
        if prow == len(rows):
            break
    return rank


INF = float("inf")


def min_folded_l1(Nprime, p, zeta):
    """Exact minimum l1 weight of a NONZERO w in {-2..2}^{N'/2} with
    sum_x w_x zeta^x == 0 (mod p).  Exhaustive by exact DP over residues."""
    n = Nprime // 2
    powers = [pow(zeta, x, p) for x in range(n)]
    # dp[flag][r]; flag = 1 once some coefficient is nonzero
    dp = [[INF] * p, [INF] * p]
    dp[0][0] = 0
    for i in range(n):
        pw = powers[i]
        nd = [[INF] * p, [INF] * p]
        contrib = [((c * pw) % p, abs(c), 1 if c else 0) for c in (-2, -1, 0, 1, 2)]
        for flag in (0, 1):
            row = dp[flag]
            for r in range(p):
                v = row[r]
                if v is INF:
                    continue
                for shift, cost, nz in contrib:
                    f2 = flag | nz
                    r2 = r + shift
                    if r2 >= p:
                        r2 -= p
                    if v + cost < nd[f2][r2]:
                        nd[f2][r2] = v + cost
        dp = nd
    return dp[1][0]


def brute_min_noncyclotomic_support(Nprime, p, zeta):
    """Brute force over ternary v in {0,+-1}^{N'}: minimum support of a
    NON-cyclotomic kernel vector (non-cyclotomic == folded vector nonzero)."""
    n = Nprime
    pw = [pow(zeta, x, p) for x in range(n)]
    best = INF
    for code in range(3 ** n):
        c, v = code, []
        for _ in range(n):
            v.append((c % 3) - 1)
            c //= 3
        s = 0
        for x in range(n):
            if v[x]:
                s += v[x] * pw[x]
        if s % p:
            continue
        half = n // 2
        folded_zero = all(v[x] == v[x + half] for x in range(half))
        if folded_zero:
            continue
        sup = sum(1 for a in v if a)
        if sup and sup < best:
            best = sup
    return best


def enum_int_vectors(N, budget):
    """All integer vectors of length N with l1 weight <= budget (yields lists)."""
    cur = [0] * N

    def rec(i, left):
        if i == N:
            yield list(cur)
            return
        for c in range(-left, left + 1):
            cur[i] = c
            for out in rec(i + 1, left - abs(c)):
                yield out
        cur[i] = 0

    return rec(0, budget)


# ----------------------------------------------------------------- stages

def stage_hyp():
    print("== hyp: hypothesis match, pinned arithmetic ==")
    # The node's threshold.  l' = rho N' + 1 (acl_count/statement.md:9;
    # qfloor_exact/statement.md:13); rate 1/2 prize cell N' = 128.
    for Nprime, rho in ((128, 0.5), (256, 0.25), (512, 0.0625)):
        lp = int(rho * Nprime) + 1
        print("   N'=%-4d rho=%-7s l'=rho N'+1=%-4d 2l'=%-4d  N'=%d  support bound vacuous? %s"
              % (Nprime, rho, lp, 2 * lp, Nprime, 2 * lp >= Nprime))
    lp_half = int(0.5 * 128) + 1
    check("hyp.rate-half-support-bound-covers-whole-box", 2 * lp_half > 128,
          "2l'=%d vs N'=128" % (2 * lp_half))
    # the alternative census convention l' = round((j/n) N')
    lp_alt = 64
    check("hyp.alt-convention-also-whole-box", 2 * lp_alt >= 128,
          "2l'=%d" % (2 * lp_alt))
    # Z-1/Z-2 floor as a function of ell.
    for ell in (1, 2, 8, 32, 64, 65):
        print("   ell=%-3d  Z-1/Z-2 floor 2*ell+1 = %-4d  reaches 2l'=%d ? %s"
              % (ell, 2 * ell + 1, 2 * lp_half, 2 * ell + 1 > 2 * lp_half))
    check("hyp.ell-1-floor-is-3", 2 * 1 + 1 == 3)
    check("hyp.ell-1-does-not-reach-threshold", not (2 * 1 + 1 > 2 * lp_half))
    check("hyp.required-ell-is-l-prime", 2 * lp_half + 1 > 2 * lp_half and
          2 * (lp_half - 1) + 1 <= 2 * lp_half)
    print("   DEFICIT at the rate-1/2 prize cell: ell needed = %d, ell available = 1, missing = %d"
          % (lp_half, lp_half - 1))
    print("   WEIGHT GAP: Z-2 gives >= 3, node needs > %d  (gap %d units of l1 weight)"
          % (2 * lp_half, 2 * lp_half + 1 - 3))


def stage_rank1():
    print("== rank1: multi_multiplier_reduction Lemma 1, rank 1 for every k ==")
    cells = [(8, 17), (8, 41), (16, 97), (16, 193), (32, 193), (16, 10177)]
    for Nprime, p in cells:
        z = exact_order_element(Nprime, p)
        if z is None:
            continue
        base = [pow(z, x, p) for x in range(Nprime)]
        for k in (1, 2, 3, 5, 10):
            mults = [(37 * i + 11) % p or 1 for i in range(1, k + 1)]
            rows = [[(m * b) % p for b in base] for m in mults]
            r = rank_mod_p(rows, p)
            check("rank1.N%d.p%d.k%d" % (Nprime, p, k), r == 1,
                  "rank=%d, expected 1" % r)
        print("   N'=%-4d p=%-7d  stacked k-multiplier matrix has rank 1 for k in 1,2,3,5,10"
              % (Nprime, p))
    print("   => stacking multipliers adds NO independent vanishing condition: ell stays 1.")


def stage_fold():
    print("== fold: min non-cyclotomic ternary SUPPORT == min nonzero folded l1 ==")
    for Nprime, p in ((8, 17), (8, 41), (8, 73), (8, 89), (8, 97), (8, 113)):
        z = exact_order_element(Nprime, p)
        if z is None:
            continue
        a = brute_min_noncyclotomic_support(Nprime, p, z)
        b = min_folded_l1(Nprime, p, z)
        check("fold.N%d.p%d" % (Nprime, p), a == b, "support=%s folded_l1=%s" % (a, b))
        print("   N'=%-3d p=%-5d  min non-cyclotomic support = %-4s  min folded l1 = %-4s"
              % (Nprime, p, a, b))


def stage_box():
    print("== box: V1/V2/V3 exact min folded l1 weight (the node's own question) ==")
    cells = [(8, 17), (8, 41), (8, 73), (8, 89), (8, 97), (8, 113), (8, 193), (8, 241),
             (16, 17), (16, 97), (16, 113), (16, 193), (16, 241), (16, 337),
             (16, 10177), (16, 12289), (16, 60161)]
    for Nprime, p in cells:
        if not is_prime(p) or (p - 1) % Nprime:
            continue
        z = exact_order_element(Nprime, p)
        if z is None:
            continue
        m = min_folded_l1(Nprime, p, z)
        lp = Nprime // 2 + 1                      # rho = 1/2
        # V2: Z-2 at ell = 1 says NO nonzero kernel vector of l1 weight <= 2.
        check("box.V2.Z2-ell1.N%d.p%d" % (Nprime, p), m >= 3,
              "min folded l1 = %s, Z-2(ell=1) floor is 3" % m)
        # V3: does the ell = 1 floor reach the node's threshold?
        reaches = (3 > 2 * lp)
        check("box.V3.ell1-cannot-reach.N%d.p%d" % (Nprime, p), not reaches)
        verdict = "CERTIFIED (no non-cyclotomic vector at all)" if m is INF else \
                  ("COLLISION at l1 weight %d" % m)
        print("   N'=%-3d p=%-6d  min folded l1 = %-5s  node needs > 2l' = %-4d  ->  %s"
              % (Nprime, p, m, 2 * lp, verdict))
    # replication of the two banked toy verdicts (folded_certificate.md:17-20)
    z = exact_order_element(16, 60161)
    m = min_folded_l1(16, 60161, z)
    check("box.replicate.N16.p60161.certified", m is INF,
          "banked: 0 non-cyclotomic collisions; got min l1 = %s" % m)
    z = exact_order_element(16, 10177)
    m = min_folded_l1(16, 10177, z)
    # CATCH-P1: folded_certificate.md:19-20 records "48 collisions, min support 5".
    # The count 48 replicates exactly; the "5" is the folded HAMMING weight.
    # The node's threshold is on the UNFOLDED ternary support, which is 7.
    check("box.replicate.N16.p10177.unfolded-support-is-7", m == 7,
          "corrected banked value: unfolded ternary support 7 (folded hamming 5); got %s" % m)
    print("   REPLICATED the banked toy verdicts of")
    print("   critical/nodes/integer_code_distance_cert/notes/folded_certificate.md:17-20,")
    print("   with CATCH-P1: the recorded 'min support 5' is a folded HAMMING weight;")
    print("   the node-relevant UNFOLDED ternary support at that cell is 7.")


def stage_banked():
    """CATCH-P1 in full: count, l1, folded hamming, and unfolded ternary support."""
    import itertools
    print("== banked: audit of folded_certificate.md:17-20 against exact enumeration ==")
    Np, p = 16, 10177
    half = Np // 2
    roots = []
    for g in range(2, p):
        z = pow(g, (p - 1) // Np, p)
        if pow(z, Np, p) == 1 and pow(z, Np // 2, p) != 1 and z not in roots:
            roots.append(z)
        if len(roots) >= 8:
            break
    roots = sorted(set(roots))
    check("banked.eight-primitive-roots", len(roots) == 8, str(roots))
    for z in roots:
        pw = [pow(z, x, p) for x in range(half)]
        cnt, best_l1, best_ham = 0, None, None
        for w in itertools.product((-2, -1, 0, 1, 2), repeat=half):
            if not any(w):
                continue
            s = 0
            for i in range(half):
                if w[i]:
                    s += w[i] * pw[i]
            if s % p:
                continue
            cnt += 1
            l1 = sum(abs(c) for c in w)
            ham = sum(1 for c in w if c)
            best_l1 = l1 if best_l1 is None or l1 < best_l1 else best_l1
            best_ham = ham if best_ham is None or ham < best_ham else best_ham
        check("banked.count48.zeta%d" % z, cnt == 48, "got %d" % cnt)
        check("banked.l1-is-7.zeta%d" % z, best_l1 == 7, "got %s" % best_l1)
        check("banked.hamming-is-5.zeta%d" % z, best_ham == 5, "got %s" % best_ham)
    print("   all 8 primitive 16th roots mod 10177: 48 folded kernel vectors,")
    print("   min folded l1 = 7, min folded HAMMING = 5  (root-independent here)")
    # exhaustive unfolded confirmation of the fold lemma at the real cell
    z = roots[0]
    pwf = [pow(z, x, p) for x in range(Np)]
    found = {}
    for s in range(1, 9):
        c = 0
        for pos in itertools.combinations(range(Np), s):
            for signs in itertools.product((1, -1), repeat=s):
                tot = 0
                for i in range(s):
                    tot += signs[i] * pwf[pos[i]]
                if tot % p:
                    continue
                v = [0] * Np
                for i in range(s):
                    v[pos[i]] = signs[i]
                if all(v[x] == v[x + half] for x in range(half)):
                    continue
                c += 1
        found[s] = c
        print("   unfolded ternary support %d: non-cyclotomic kernel vectors = %d" % (s, c))
    check("banked.no-collision-below-7", all(found[s] == 0 for s in range(1, 7)),
          str(found))
    check("banked.first-collision-at-7", found[7] == 128, "got %s" % found.get(7))
    print("   => MIN UNFOLDED TERNARY SUPPORT = 7, not 5.  Fold lemma confirmed at the")
    print("      real toy cell: min unfolded support == min folded l1 == 7.")


def stage_tight():
    print("== tight: the ell=1 floor 3 is ATTAINED, so Z-2 at ell=1 is unimprovable ==")
    hits = []
    Nprime = 8
    p = 3
    while len(hits) < 4 and p < 4000:
        p += 1
        if not is_prime(p) or (p - 1) % Nprime:
            continue
        z = exact_order_element(Nprime, p)
        if z is None:
            continue
        m = min_folded_l1(Nprime, p, z)
        if m == 3:
            hits.append((p, z, m))
    for (p, z, m) in hits:
        print("   N'=8 p=%-5d zeta=%-5d  min folded l1 = 3  (the Z-2 ell=1 floor, ATTAINED)" % (p, z))
    check("tight.floor-3-attained", len(hits) >= 1,
          "found %d cells attaining l1 = 3" % len(hits))
    print("   => no sharpening of Z-1/Z-2 at ell = 1 can exceed 3.  The node needs > 2l'.")


def stage_poscontrol():
    print("== poscontrol: V4, the GENUINE ell-condition system, and the shift scope ==")
    # Z-2 at shift 0 with ell conditions: no nonzero integer c of l1 weight <= 2ell
    # with sum_e c_e omega^{(2j-1)e} = 0, j = 1..ell.
    for (twoN, ell, p) in ((16, 2, 97), (16, 2, 193), (16, 3, 97), (16, 3, 193),
                           (12, 2, 13), (12, 2, 37), (20, 2, 41)):
        N = twoN // 2
        if (p - 1) % twoN:
            continue
        om = exact_order_element(twoN, p)
        if om is None:
            continue
        budget = 2 * ell
        if p <= budget:              # char > w is a hypothesis of Z-2
            continue
        bad = None
        for c in enum_int_vectors(N, budget):
            if not any(c):
                continue
            ok = True
            for j in range(1, ell + 1):
                e = (2 * j - 1)
                s = 0
                for idx in range(N):
                    if c[idx]:
                        s += c[idx] * pow(om, (e * idx) % twoN, p)
                if s % p:
                    ok = False
                    break
            if ok:
                bad = c
                break
        check("poscontrol.shift0.2N%d.ell%d.p%d" % (twoN, ell, p), bad is None,
              "counterexample %s" % (bad,))
        print("   2N=%-3d ell=%-2d p=%-5d  shift 0: no nonzero c with l1 <= %d  ->  Z-2 HOLDS"
              % (twoN, ell, p, budget))
    # The SHIFT scope: the banked smallest counterexample, 2N=12, p=13, R=1, a=1.
    twoN, p, ell, shift = 12, 13, 1, 1
    N = twoN // 2
    om = exact_order_element(twoN, p)
    found = None
    for c in enum_int_vectors(N, 2 * ell):
        if not any(c):
            continue
        ok = True
        for j in range(1, ell + 1):
            e = 2 * (j + shift) - 1
            s = sum(c[i] * pow(om, (e * i) % twoN, p) for i in range(N) if c[i])
            if s % p:
                ok = False
                break
        if ok:
            found = c
            break
    check("poscontrol.shifted-counterexample-exists", found is not None,
          "expected the banked 2N=12,p=13,R=1,a=1 counterexample")
    if found:
        w = sum(abs(x) for x in found)
        print("   SHIFTED (a=1) 2N=12 p=13 ell=1: c=%s has l1 weight %d < 2R+1 = 3  ->  Z-1 FAILS off shift 0"
              % (found, w))
        eff = pow(om, 2 * (1 + shift) - 1, p)
        order = 1
        t = eff
        while t != 1:
            t = t * eff % p
            order += 1
        print("   mechanism: the shifted generator omega^%d has exact order %d < 2N = %d,"
              % (2 * (1 + shift) - 1, order, twoN))
        print("              so hypothesis (H2) 'exact order 2N' is what the shift destroys.")
        check("poscontrol.shift-breaks-H2", order < twoN,
              "order %d vs 2N %d" % (order, twoN))
    print("   => Z-1/Z-2 are SOUND; it is the node's system (ell = 1) that is short.")


def stage_catch():
    print("== catch: the Galois/Frobenius reduction claimed by weight_graded_mitm ==")
    # weight_graded_mitm/proof.md:110-114 claims collisions are closed under
    # v -> v^{(p)} = index multiplication by (p mod N'), giving a factor ~N'.
    # But the node's own hypothesis is p = 1 mod N'.
    for Nprime, p in ((8, 17), (16, 97), (16, 10177), (32, 193)):
        check("catch.p-mod-Nprime-is-1.N%d.p%d" % (Nprime, p), p % Nprime == 1,
              "p mod N' = %d" % (p % Nprime))
    print("   p = 1 mod N' at every in-scope row  =>  p mod N' = 1  =>  v -> v^{(p)} is the IDENTITY;")
    print("   the claimed Frobenius orbit has size 1, not N'.")
    # Does index multiplication by a general unit a preserve K_p?  (Claim: NO.)
    bad_example = None
    for Nprime, p in ((8, 17), (8, 41), (16, 97), (16, 10177)):
        z = exact_order_element(Nprime, p)
        if z is None:
            continue
        pw = [pow(z, x, p) for x in range(Nprime)]
        # collect a few kernel vectors
        for code in range(1, 3 ** Nprime if Nprime == 8 else 3 ** 8):
            c, v = code, []
            for _ in range(Nprime if Nprime == 8 else 8):
                v.append((c % 3) - 1)
                c //= 3
            if Nprime != 8:
                v = v + [0] * (Nprime - 8)
            if sum(v[x] * pw[x] for x in range(Nprime)) % p:
                continue
            if not any(v):
                continue
            for a in range(3, Nprime, 2):
                vv = [0] * Nprime
                for x in range(Nprime):
                    vv[(a * x) % Nprime] = v[x]
                if sum(vv[x] * pw[x] for x in range(Nprime)) % p:
                    bad_example = (Nprime, p, a, v)
                    break
            if bad_example:
                break
        if bad_example:
            break
    check("catch.index-mult-not-a-symmetry", bad_example is not None,
          "expected a v in K_p with v-composed-with-a outside K_p")
    if bad_example:
        Nprime, p, a, v = bad_example
        print("   COUNTEREXAMPLE: N'=%d p=%d, v=%s in K_p but index-multiplication by a=%d leaves K_p."
              % (Nprime, p, v, a))
    # Cyclic shift IS a symmetry.
    okshift = True
    for Nprime, p in ((8, 17), (16, 97), (16, 10177)):
        z = exact_order_element(Nprime, p)
        pw = [pow(z, x, p) for x in range(Nprime)]
        for code in range(1, 3 ** min(Nprime, 8)):
            c, v = code, []
            for _ in range(min(Nprime, 8)):
                v.append((c % 3) - 1)
                c //= 3
            v = v + [0] * (Nprime - len(v))
            if sum(v[x] * pw[x] for x in range(Nprime)) % p:
                continue
            sh = [v[(x - 1) % Nprime] for x in range(Nprime)]
            if sum(sh[x] * pw[x] for x in range(Nprime)) % p:
                okshift = False
    check("catch.cyclic-shift-is-a-symmetry", okshift)
    print("   Cyclic shift v_x -> v_{x-1} IS a symmetry (multiplies the sum by zeta).")
    print("   => the factor-N' saving survives, but via cyclic shift, NOT via Frobenius:")
    print("      weight_graded_mitm/proof.md:110-114 states the wrong mechanism.")


def stage_failclosed():
    print("== failclosed: this control MUST exit 1 ==")
    z = exact_order_element(16, 97)
    m = min_folded_l1(16, 97, z)
    # deliberately false: assert the ell=1 floor reaches the node's threshold
    check("failclosed.deliberately-false", 3 > 2 * (16 // 2 + 1),
          "3 > 2l' is FALSE by construction; min folded l1 here = %s" % m)


def stage_hfb():
    """What integer_code_distance_high_field_folded_box_exclusion already pays,
    and the exact residual, on the rate-1/2 crossing lane's own log-window."""
    import math
    print("== hfb: the residual left by the PROVED high-field branch ==")
    # HFB1: p > 253^32  (background/nodes/
    #   integer_code_distance_high_field_folded_box_exclusion/statement.md:17)
    thr = 32 * math.log(253, 2)
    print("   HFB threshold: log2(253^32) = %.4f bits" % thr)
    check("hfb.threshold-under-256", thr < 256.0, "%.4f" % thr)
    # The crossing lane's live prime-row window (same constants as PROBE 2 region):
    lo, hi = 245.1491, 256.0
    covered = max(0.0, hi - max(lo, thr))
    total = hi - lo
    print("   crossing-lane e=1 live window: log2 p in [%.4f, %.4f), width %.4f bits" % (lo, hi, total))
    print("   HFB covers log2 p in (%.4f, %.4f), width %.4f bits = %.2f%% of the window"
          % (thr, hi, covered, 100.0 * covered / total))
    check("hfb.covers-a-strict-minority", covered < total / 2.0,
          "covered %.4f of %.4f" % (covered, total))
    print("   RESIDUAL on this lane alone: log2 p in [%.4f, %.4f], width %.4f bits (%.2f%%),"
          % (lo, thr, thr - lo, 100.0 * (thr - lo) / total))
    print("   plus every quotient order N' != 128, plus the cell-cardinality-vs-B* obligation.")
    # The four pinned Proth exhibits are 167-171 bits (status_ruling.md:19-21).
    for b in (167, 168, 170, 171):
        check("hfb.proth-exhibit-below-threshold.%d" % b, b < thr, "%d vs %.4f" % (b, thr))
    print("   the four pinned Proth prize exhibits (167-171 bits) all sit BELOW the threshold,")
    print("   by %.1f to %.1f bits." % (thr - 171, thr - 167))


STAGES = {
    "hyp": stage_hyp, "rank1": stage_rank1, "fold": stage_fold, "box": stage_box,
    "tight": stage_tight, "poscontrol": stage_poscontrol, "catch": stage_catch,
    "banked": stage_banked, "hfb": stage_hfb,
    "failclosed": stage_failclosed,
}

if __name__ == "__main__":
    want = sys.argv[1] if len(sys.argv) > 1 else "all"
    if want == "all":
        for nm in ("hyp", "rank1", "fold", "box", "banked", "tight", "poscontrol", "catch", "hfb"):
            STAGES[nm]()
            print("")
    else:
        STAGES[want]()
    print("---- %d checks, %d failures ----" % (CHECKS[0], len(FAILURES)))
    for f in FAILURES:
        print("   " + f)
    sys.exit(1 if FAILURES else 0)
