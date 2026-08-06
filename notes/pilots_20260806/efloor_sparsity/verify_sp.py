#!/usr/bin/env python3
"""Round 18 -- E_floor SPARSITY pilot: fail-closed verifier.

Stages:   self  cover  floor  dense  n64  prize  failclosed
Exit code is nonzero on ANY failed check (fail-closed, proven by the
permanent `failclosed` stage which injects a false check).

Run under the COMPUTE LAW only:
    tools/ramguard tiny  -- python3 .../verify_sp.py self
    tools/ramguard local -- python3 .../verify_sp.py cover
"""

import math
import sys
import itertools

sys.dont_write_bytecode = True

import sp_lib as SP
import cop_lib

NCHK = [0]
NFAIL = [0]
NPRED = [0]
PREDFAIL = []


def check(name, ok, detail=""):
    """CORRECTNESS invariant: any failure is a real failure (fail-closed)."""
    NCHK[0] += 1
    if not ok:
        NFAIL[0] += 1
        print("  FAIL  %s  %s" % (name, detail))
    return ok


def predict(name, ok, detail=""):
    """A PRE-REGISTERED PREDICTION.  A miss is reported, not buried, and is
    NOT a machine failure -- registered predictions are allowed to be wrong;
    that is what registering them is for."""
    NPRED[0] += 1
    if not ok:
        PREDFAIL.append("%s  [%s]" % (name, detail))
        print("  PREDICTION-MISS  %s  %s" % (name, detail))
    return ok


def hdr(t):
    print("-" * 74)
    print(t)


# ==========================================================================
def stage_self():
    """Machinery validation against the banked round-17 oracles."""
    hdr("[SELF] packer / factorisation / syndrome vs cop_lib.ideal_norm")
    import random
    rng = random.Random(11)

    # --- Packer ---------------------------------------------------------
    for p in (3, 5, 7, 17, 47):
        pk = SP.Packer(p, 9)
        for _ in range(200):
            a = [rng.randrange(p) for _ in range(9)]
            b = [rng.randrange(p) for _ in range(9)]
            va, vb = pk.pack(a), pk.pack(b)
            check("packer add p=%d" % p,
                  pk.unpack(pk.add(va, vb)) == [(x + y) % p for x, y in zip(a, b)])
            check("packer neg p=%d" % p,
                  pk.unpack(pk.neg(va)) == [(-x) % p for x in a])

    # --- Phi_n factorisation --------------------------------------------
    for n in (8, 16, 32, 64):
        for p in (3, 5, 7, 17):
            d = cop_lib.mult_order(p, n)
            fs = SP.phi_factors(n, p)
            check("factor count n=%d p=%d" % (n, p), len(fs) == (n // 2) // d,
                  "got %d want %d" % (len(fs), (n // 2) // d))
            prod = [1]
            for g in fs:
                check("factor degree n=%d p=%d" % (n, p), len(g) - 1 == d)
                prod = SP.pmul(prod, g, p)
            check("factors multiply to Phi_n n=%d p=%d" % (n, p),
                  prod == SP.pnorm(cop_lib.phi_n_poly(n), p),
                  "prod=%s" % prod[:6])
            # distinctness
            check("factors distinct n=%d p=%d" % (n, p),
                  len(set(map(tuple, fs))) == len(fs))

    # --- syndrome route  vs  exact HNF ideal norm  vs  banked gcd census --
    for n, rlist in ((16, (4, 5)), (32, (5,))):
        for p in (3, 5, 7, 17):
            fs = SP.phi_factors(n, p)
            for w in (3, 4, 6):
                packs = [SP.syndrome_columns(n, p, w, [g]) for g in fs]
                pool = []
                for rp in rlist:
                    allsets = list(itertools.combinations(range(n), rp))
                    if len(allsets) > 700:
                        allsets = [allsets[rng.randrange(len(allsets))]
                                   for _ in range(700)]
                    pool.extend(allsets)
                for S in pool:
                    N = cop_lib.ideal_norm(list(S), n, w)
                    oracle = (N == 0) or (N % p == 0)
                    mine = any(SP.is_bad_for_factor(S, pk, cols)
                               for pk, cols, _, _ in packs)
                    check("syndrome==HNF n=%d p=%d w=%d" % (n, p, w),
                          oracle == mine,
                          "S=%s N=%s mine=%s" % (S, N, mine))
                    if N != 0:
                        gcdroute = p in cop_lib.census_bad(list(S), n, w, [p])
                        check("syndrome==gcd-census n=%d p=%d w=%d" % (n, p, w),
                              gcdroute == mine, "S=%s" % (S,))

    # --- MITM census vs brute force at n = 16 ---------------------------
    n = 16
    for p in (3, 7):
        fs = SP.phi_factors(n, p)
        for w in (3, 5):
            g = fs[0]
            pk, cols, _, _ = SP.syndrome_columns(n, p, w, [g])
            brute = [0] * (n + 1)
            for m in range(1 << n):
                S = [i for i in range(n) if (m >> i) & 1]
                if SP.syndrome_of(S, pk, cols) == 0:
                    brute[len(S)] += 1
            got, L, reps = SP.census_by_weight(n, p, w, [g])
            check("MITM==brute n=16 p=%d w=%d" % (p, w), got == brute,
                  "mitm=%s brute=%s" % (got[:8], brute[:8]))
            # periodic sub-count
            per = SP.periodic_census_by_weight(n, p, w, [g])
            bper = [0] * (n + 1)
            for m in range(1 << (n // 2)):
                T = [i for i in range(n // 2) if (m >> i) & 1]
                S = sorted(T + [t + n // 2 for t in T])
                if SP.syndrome_of(S, pk, cols) == 0:
                    bper[len(S)] += 1
            check("MITM-periodic==brute n=16 p=%d w=%d" % (p, w), per == bper,
                  "%s vs %s" % (per[:8], bper[:8]))

    print("  [SELF] %d checks" % NCHK[0])


# ==========================================================================
def stage_cover():
    """(S1) THEOREM SP-COVER: thresholds, n-uniformity, exact census."""
    hdr("[COVER] w_cov(p,n) table and its 2^{v_2(p^2-1)} bound")
    print("  %-6s %-6s %-4s %s" % ("p", "j_p=v2", "2^j", "w_cov(p,2^m) for m=4..12"))
    plist = (3, 5, 7, 11, 13, 17, 19, 23, 31, 47, 97, 193, 257, 353, 449)
    for p in plist:
        j = 0
        t = p * p - 1
        while t % 2 == 0:
            t //= 2
            j += 1
        row = []
        for m in range(4, 13):
            n = 1 << m
            wc = SP.w_cover(n, p)
            row.append(wc)
            check("w_cov <= 2^{v2(p^2-1)} p=%d n=%d" % (p, n), wc <= (1 << j),
                  "wc=%d bound=%d" % (wc, 1 << j))
            if n >= (1 << j):
                check("w_cov n-uniform p=%d n=%d" % (p, n),
                      wc == SP.w_cover(1 << max(4, j), p),
                      "wc=%d ref=%d" % (wc, SP.w_cover(1 << max(4, j), p)))
        print("  %-6d %-6d %-4d %s" % (p, j, 1 << j, row))

    # --- EXACT census over ALL subsets, by weight ------------------------
    for n in (16, 32):
        hdr("[COVER] EXACT per-prime census at n=%d over ALL 2^%d subsets"
            % (n, n))
        print("  %-3s %-3s %-4s %-4s %-5s %-9s %-9s %-9s %s"
              % ("p", "w", "dlt", "e", "|Zw|", "bad(all)", "bad(per)",
                 "bad(a=0)", "verdict"))
        for p in (3, 5, 7, 17):
            fs = SP.phi_factors(n, p)
            d = cop_lib.mult_order(p, n)
            wc = SP.w_cover(n, p)
            for w in range(2, 13):
                tot, L, reps = SP.census_by_weight(n, p, w, [fs[0]])
                per = SP.periodic_census_by_weight(n, p, w, [fs[0]])
                zw = len(cop_lib.cyclotomic_closure(w, n, p))
                allb = sum(tot)
                allp = sum(per)
                a0 = allb - allp
                for k in range(n + 1):
                    check("periodic <= total n=%d p=%d w=%d k=%d" % (n, p, w, k),
                          per[k] <= tot[k])
                # cross-factor invariance (multiplier equivalence)
                if len(fs) > 1:
                    tot2, _, _ = SP.census_by_weight(n, p, w, [fs[1]])
                    check("factor-invariance n=%d p=%d w=%d" % (n, p, w),
                          tot2 == tot, "%s vs %s" % (tot2[:6], tot[:6]))
                verdict = ""
                if w >= wc:
                    ok = check("SP-COVER a=0 empty n=%d p=%d w=%d (w_cov=%d)"
                               % (n, p, w, wc), a0 == 0, "a0=%d" % a0)
                    verdict = "SP-COVER: a=0 EMPTY" if ok else "*** REFUTED ***"
                elif w == wc - 1:
                    ok = predict("(P2) SP-COVER sharp at w=w_cov-1 n=%d p=%d"
                                 % (n, p), a0 > 0, "a0=%d" % a0)
                    verdict = "sharp witness a=0" if ok else "NOT SHARP (P2 miss)"
                print("  %-3d %-3d %-4d %-4d %-5d %-9d %-9d %-9d %s"
                      % (p, w, d, len(fs), zw, allb, allp, a0, verdict))
        # weight profile of the surviving a=0 bad sets, p=3
        hdr("[COVER] n=%d p=3 a=0 bad counts by weight r' (the E_floor mass)"
            % n)
        fs = SP.phi_factors(n, 3)
        for w in (2, 3, 4, 5, 6, 7):
            tot, _, _ = SP.census_by_weight(n, 3, w, [fs[0]])
            per = SP.periodic_census_by_weight(n, 3, w, [fs[0]])
            prof = [(k, tot[k] - per[k]) for k in range(n + 1)
                    if tot[k] - per[k]]
            print("  w=%-2d a=0 profile (r',count): %s" % (w, prof[:12]))
    print("  [COVER] %d checks" % NCHK[0])


# ==========================================================================
def _orbit_reps(n, rp):
    """round-17 orbit convention: S ~ cS + b, c odd (verify_cop.py:373-377)."""
    binom = [[math.comb(x, y) for y in range(rp + 2)] for x in range(n + 1)]

    def rank(c):
        return sum(binom[x][j + 1] for j, x in enumerate(c))

    seen = bytearray(math.comb(n, rp))
    reps = []
    for comb in itertools.combinations(range(n), rp):
        pos = rank(sorted(comb))
        if seen[pos]:
            continue
        sz = 0
        for c in range(1, n, 2):
            base = tuple(sorted((c * i) % n for i in comb))
            for b in range(n):
                r = rank(tuple(sorted((i + b) % n for i in base)))
                if not seen[r]:
                    sz += 1
                seen[r] = 1
        reps.append((comb, sz))
    return reps


def stage_floor():
    """(E3) Is E_floor a tautology?  E_floor == {N_odd > 1} on strat=0?"""
    hdr("[FLOOR] E3: does THEOREM CS make the E_floor predicate automatic?")
    print("  %-3s %-3s %-7s %-9s %-9s %-9s %s"
          % ("r'", "w", "orbits", "a=0 sets", "N_odd>1", "in E_floor", "equal?"))
    n = 32
    for rp in (5, 6):
        reps = _orbit_reps(n, rp)
        for w in (3, 4, 5):
            tot0 = nbig = nfloor = 0
            for S, sz in reps:
                if cop_lib.strat(list(S), n) != 0:
                    continue
                tot0 += sz
                N, Nod = SP.odd_norm(S, n, w)
                if N == 0:
                    continue
                if Nod > 1:
                    nbig += sz
                    ps = sorted(cop_lib.factorize(Nod))
                    infl = False
                    for p in ps:
                        ok, zo, base = cop_lib.cs_floor_ok(n, rp, w, p, list(S))
                        # THEOREM CS says the floor predicate must hold for
                        # EVERY odd p dividing N_odd, not just one.
                        check("CS floor holds for every p|N_odd r'=%d w=%d p=%d"
                              % (rp, w, p), ok,
                              "S=%s N_odd=%d zo=%d base=%d" % (S, Nod, zo, base))
                        if ok:
                            infl = True
                    if infl:
                        nfloor += sz
            check("E_floor == {N_odd>1} on a=0  r'=%d w=%d" % (rp, w),
                  nbig == nfloor, "%d vs %d" % (nbig, nfloor))
            print("  %-3d %-3d %-7d %-9d %-9d %-9d %s"
                  % (rp, w, len(reps), tot0, nbig, nfloor,
                     "YES" if nbig == nfloor else "NO"))
    print("  [FLOOR] %d checks" % NCHK[0])


# ==========================================================================
def stage_dense():
    """(S2) adversarial: the densest floor families we can construct."""
    n, rp = 32, 6
    hdr("[DENSE] S2 -- floor density of constructed families, n=%d r'=%d"
        % (n, rp))
    total_sets = math.comb(n, rp)

    CAP = 6000

    def measure(name, fam, w):
        fam = [S for S in fam if len(S) == rp]
        if not fam:
            return None
        full = len(fam)
        sub = ""
        if full > CAP:
            stride = full // CAP + 1
            fam = fam[::stride]
            sub = " [SUBSAMPLE %d/%d stride=%d]" % (len(fam), full, stride)
        a0 = [S for S in fam if cop_lib.strat(list(S), n) == 0]
        nb = nz = 0
        kill = 0
        for S in a0:
            N, Nod = SP.odd_norm(S, n, w)
            if N == 0:
                nz += 1
                continue
            if Nod > 1:
                nb += 1
            kill += SP.vanishing_conditions(S, n, w)
        den = len(a0) - nz
        dens = (float(nb) / den) if den else float('nan')
        contrib = float(nb) * (full / float(len(fam))) / total_sets
        avgkill = (float(kill) / len(a0)) if a0 else 0.0
        print("  %-22s w=%d |F|=%-7d a0=%-7d N=0:%-5d floor=%-6d "
              "internal=%.5f contrib=%.3e kill=%.2f%s"
              % (name, w, full, len(a0), nz, nb, dens, contrib, avgkill, sub))
        return dens, contrib, full

    for w in (3, 4):
        # global baseline over ALL C(32,6) sets, exact via orbit weights
        reps = _orbit_reps(n, rp)
        tot = bad = zero = 0
        for S, sz in reps:
            if cop_lib.strat(list(S), n) != 0:
                continue
            N, Nod = SP.odd_norm(S, n, w)
            if N == 0:
                zero += sz
                continue
            tot += sz
            if Nod > 1:
                bad += sz
        base = float(bad) / tot if tot else 0.0
        print("  %-22s w=%d |F|=%-7d a0=%-7d N=0:%-5d floor=%-6d "
              "internal=%.5f contrib=%.3e"
              % ("BASELINE(all sets)", w, total_sets, tot + zero, zero, bad,
                 base, float(bad) / total_sets))
        measure("F1 quarter-shift j=2", SP.fam_shift(n, rp, 2), w)
        measure("F2 shift j=3", SP.fam_shift(n, rp, 3), w)
        measure("F2 shift j=4", SP.fam_shift(n, rp, 4), w)
        measure("F3 symmetric S=-S", SP.fam_symmetric(n, rp), w)
        measure("F4 mult-inv u=17", SP.fam_mult_invariant(n, rp, 17), w)
        measure("F4 mult-inv u=15", SP.fam_mult_invariant(n, rp, 15), w)
        measure("F5 AP supports", SP.fam_ap(n, rp, 0), w)
        measure("F6 coset-near M=2", SP.fam_coset_near(n, rp, 2, 1), w)
        measure("F6 coset-near M=4", SP.fam_coset_near(n, rp, 4, 1), w)
        for ap in (1, 2, 3):
            measure("F7 antipodal x%d" % ap, SP.fam_antipodal(n, rp, ap), w)
        check("baseline floor density is small w=%d" % w, base < 0.2,
              "base=%.5f" % base)
    print("  [DENSE] %d checks" % NCHK[0])


# ==========================================================================
def stage_n64(argv):
    """(S3) the n = 64 asymptotic: exact per-prime census, r' <= kmax."""
    n = int(argv[0]) if argv else 64
    kmax = int(argv[1]) if len(argv) > 1 else 6
    plist = [int(x) for x in argv[2].split(",")] if len(argv) > 2 else [3]
    wmax = int(argv[3]) if len(argv) > 3 else 10
    hdr("[N64] EXACT per-prime census at n=%d, r' <= %d (meet in the middle)"
        % (n, kmax))
    print("  %-3s %-3s %-4s %-4s %-6s %-6s %-11s %-11s %s"
          % ("p", "w", "dlt", "e", "|Zw|", "w_cov", "bad(all)", "bad(a=0)",
             "profile (r',a=0 count)"))
    for p in plist:
        fs = SP.phi_factors(n, p)
        d = cop_lib.mult_order(p, n)
        wc = SP.w_cover(n, p)
        for w in range(2, wmax + 1):
            tot, L, reps = SP.census_by_weight(n, p, w, [fs[0]], kmax=kmax)
            per = SP.periodic_census_by_weight(n, p, w, [fs[0]], kmax=kmax)
            zw = len(cop_lib.cyclotomic_closure(w, n, p))
            a0 = [tot[k] - per[k] for k in range(kmax + 1)]
            for k in range(kmax + 1):
                check("n=%d periodic<=total p=%d w=%d k=%d" % (n, p, w, k),
                      per[k] <= tot[k])
            if w >= wc:
                check("SP-COVER a=0 empty n=%d p=%d w=%d" % (n, p, w),
                      sum(a0) == 0, "a0=%s" % a0)
            prof = [(k, a0[k]) for k in range(kmax + 1) if a0[k]]
            print("  %-3d %-3d %-4d %-4d %-6d %-6d %-11d %-11d %s"
                  % (p, w, d, len(fs), zw, wc, sum(tot), sum(a0), prof[:8]))
    print("  [N64] %d checks" % NCHK[0])


# ==========================================================================
def stage_prize():
    """(E4/S4) does SP-COVER reach the official crossing rows?"""
    hdr("[PRIZE] SP-COVER vs the official crossing bracket")
    print("  crossing row constants quoted verbatim at")
    print("  es_coprimality/PROOFS.md:341 -- n = 2^41, r' = 2^40 - w,")
    print("  w in [2^34, 2^39], log2 p = 256, v_2(q-1) >= 41 (official gate)")
    n_log = 41
    for v2 in (41, 42, 45, 50):
        j = v2 + 1                    # v_2(q^2-1) = v_2(q-1) + v_2(q+1) = v2+1
        need = j                      # w >= 2^j
        print("  v_2(q-1)=%-3d  ->  j_q = v_2(q^2-1) = %-3d  ->  SP-COVER needs "
              "w >= 2^%d ; bracket caps at w = 2^39  ->  %s"
              % (v2, j, need, "BITES" if need <= 39 else "VACUOUS"))
        check("SP-COVER vacuous at official rows v2=%d" % v2, need > 39,
              "need 2^%d" % need)
    # CS-EXCL threshold, recomputed independently (round-17 w* = 2^37.3131)
    lo, hi = 2 ** 34, 2 ** 39
    n = 2 ** n_log

    def bites(w):
        rp = 2 ** 40 - w
        return math.ceil((w - 1) / 2) * 256.0 > (n / 4.0) * math.log2(rp)

    a, b = lo, hi
    if bites(hi) and not bites(lo):
        while b - a > 1:
            m = (a + b) // 2
            if bites(m):
                b = m
            else:
                a = m
    print("  CS-EXCL threshold w* = %d = 2^%.4f  (round 17: 2^37.3131)"
          % (b, math.log2(b)))
    check("CS-EXCL threshold reproduces round 17", abs(math.log2(b) - 37.3131) < 1e-3,
          "got 2^%.4f" % math.log2(b))
    print("  UNCOVERED bracket segment: w in [2^34, 2^%.4f]; SP-COVER would "
          "need w >= 2^42.  GAP = 2^%.4f in w." % (math.log2(b), 42 - math.log2(b)))
    # small-prime side: p > sqrt(w+1) for any a=0 bad prime
    print("  SP-UNIFORM contrapositive at the bracket ends:")
    for w in (2 ** 34, 2 ** 37, 2 ** 39):
        print("    w=2^%-3d  ->  every a=0 bad prime has p > sqrt(w+1) = 2^%.2f"
              % (math.log2(w), 0.5 * math.log2(w + 1)))
    print("  [PRIZE] %d checks" % NCHK[0])


# ==========================================================================
def stage_tern():
    """LEMMA AB + THEOREM SP-TERNARY: the odd-condition count, exactly.

    f_S = A + X^{n/2} B  =>  f_S = A - B  mod Phi_n, and v := A - B ranges
    over {0,+-1}^{n/2}, with exactly 2^{z(v)} sets S per v, and
    v = 0 <=> strat(S) >= 1.  For ODD s, xi^s is a root of Phi_n, so
    f_S(xi^s) = v(xi^s): the odd conditions are conditions on v alone.
    Hence
        #{S : odd conditions hold} = sum over ternary v in C of 2^{z(v)},
    C = {v : v(xi^s) = 0 for the odd window}.  So NO nonzero ternary
    codeword  =>  p is excluded on the WHOLE a=0 stratum (SP-TERNARY);
    SP-COVER is the special case C = {0}.
    """
    hdr("[TERN] LEMMA AB / SP-TERNARY: exact ternary-codeword counts")
    print("  %-3s %-3s %-3s %-6s %-6s %-12s %-14s %s"
          % ("n", "p", "w", "deg G", "w_cov", "tern v!=0", "sum 2^z(v)",
             "a=0 excluded by odd conditions alone?"))
    for n in (16, 32):
        h = n // 2
        for p in (3, 5, 7, 17):
            fs = SP.phi_factors(n, p)
            wc = SP.w_cover(n, p)
            for w in range(2, 9):
                reps = SP.odd_reps(n, w, p)
                if not reps:
                    continue
                pk, cols, _, L = SP.syndrome_columns(n, p, w, [fs[0]], reps)
                # v lives on coordinates 0..h-1 (v = A - B)
                half = h // 2
                tabs = []
                for rr in (range(half), range(half, h)):
                    d = {0: [1, 1]}          # syn -> [#v, sum of 2^{z(v)}]
                    for i in rr:
                        nd = {}
                        c0, cp, cm = 0, cols[i], pk.neg(cols[i])
                        for syn, (cnt, wt) in d.items():
                            for dcol, fac in ((c0, 2), (cp, 1), (cm, 1)):
                                s2 = pk.add(syn, dcol)
                                e0 = nd.get(s2)
                                if e0 is None:
                                    nd[s2] = [cnt, wt * fac]
                                else:
                                    e0[0] += cnt
                                    e0[1] += wt * fac
                        d = nd
                    tabs.append(d)
                lo, hi2 = tabs
                ntern = s2z = 0
                for syn, (cnt, wt) in lo.items():
                    o = hi2.get(pk.neg(syn))
                    if o:
                        ntern += cnt * o[0]
                        s2z += wt * o[1]
                ntern -= 1                   # drop v = 0
                s2z -= 2 ** h                # v = 0 contributes 2^{n/2}
                # independent cross-check: MITM census with the ODD window
                tot2, _, _ = SP.census_by_weight(n, p, w, [fs[0]], slist=reps)
                per2 = SP.periodic_census_by_weight(n, p, w, [fs[0]],
                                                    slist=reps)
                got = sum(tot2) - sum(per2)
                check("LEMMA AB: sum 2^z(v) == MITM odd-only n=%d p=%d w=%d"
                      % (n, p, w), got == s2z,
                      "mitm=%d ternary=%d" % (got, s2z))
                check("LEMMA AB: v=0 count == periodic count n=%d p=%d w=%d"
                      % (n, p, w), sum(per2) == 2 ** h if L == 0 else True)
                print("  %-3d %-3d %-3d %-6d %-6d %-12d %-14d %s"
                      % (n, p, w, L, wc, ntern, s2z,
                         "YES (proved, no nonzero ternary codeword)"
                         if ntern == 0 else "no"))
    print("  [TERN] %d checks" % NCHK[0])


def _scal(col, dig, pk):
    """digit-wise scalar multiple of a packed vector (dig in {0,1,p-1})."""
    if dig == 0:
        return 0
    if dig == 1:
        return col
    return pk.neg(col)


def stage_n64all(argv):
    """(S3-G3) ALL-CHARACTERISTIC exact census at n = 64 over affine orbits.

    This is the round-16 flag: 'n=64 was registered in my grid and never
    executed' (es_boundary_adversary/REPORT.md:106).  Exact ideal norms by
    the banked integer HNF, factored, so the bad-prime set is complete over
    EVERY characteristic at once -- no prime list, no sampling.
    """
    n = int(argv[0]) if argv else 64
    rmax = int(argv[1]) if len(argv) > 1 else 4
    wmax = int(argv[2]) if len(argv) > 2 else 5
    hdr("[N64ALL] all-characteristic exact census at n=%d, r' <= %d" % (n, rmax))
    print("  %-3s %-3s %-7s %-9s %-8s %-8s %-9s %s"
          % ("r'", "w", "orbits", "a=0 sets", "N=0", "E_floor", "density",
             "bad primes at a=0"))
    for rp in range(3, rmax + 1):
        reps = _orbit_reps(n, rp)
        for w in range(2, wmax + 1):
            tot = bad = zero = 0
            badp = set()
            for S, sz in reps:
                if cop_lib.strat(list(S), n) != 0:
                    continue
                N, Nod = SP.odd_norm(S, n, w)
                if N == 0:
                    zero += sz
                    continue
                tot += sz
                if Nod > 1:
                    bad += sz
                    try:
                        for q in cop_lib.factorize(Nod):
                            badp.add(q)
                    except Exception:
                        badp.add(-1)
                    # every bad prime must satisfy the CS floor (E3 again)
                    for q in sorted(cop_lib.factorize(Nod)):
                        ok, zo, base = cop_lib.cs_floor_ok(n, rp, w, q, list(S))
                        check("CS floor n=%d r'=%d w=%d p=%d" % (n, rp, w, q),
                              ok, "S=%s" % (S,))
                    # SP-UNIFORM: every a=0 bad prime has 2^{v2(p^2-1)} > w
                    for q in sorted(cop_lib.factorize(Nod)):
                        j = 0
                        tt = q * q - 1
                        while tt % 2 == 0:
                            tt //= 2
                            j += 1
                        check("SP-UNIFORM p>sqrt(w+1) n=%d w=%d p=%d" % (n, w, q),
                              (1 << j) > w, "j=%d w=%d" % (j, w))
            dens = (float(bad) / tot) if tot else 0.0
            print("  %-3d %-3d %-7d %-9d %-8d %-8d %-9.6f %s"
                  % (rp, w, len(reps), tot + zero, zero, bad, dens,
                     sorted(badp)[:10]))
    print("  [N64ALL] %d checks" % NCHK[0])


def stage_failclosed():
    hdr("[FAILCLOSED] permanent injected failure -- this stage MUST exit 1")
    check("injected false check (fail-closed proof)", False, "by construction")
    print("  [FAILCLOSED] %d checks, %d failures" % (NCHK[0], NFAIL[0]))


# ==========================================================================
def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "self"
    rest = sys.argv[2:]
    print("=" * 74)
    print("ROUND 18 -- E_floor SPARSITY PILOT   stage=%s" % stage)
    print("=" * 74)
    table = {"self": stage_self, "cover": stage_cover, "floor": stage_floor,
             "dense": stage_dense, "prize": stage_prize, "tern": stage_tern,
             "failclosed": stage_failclosed}
    if stage == "n64":
        stage_n64(rest)
    elif stage == "n64all":
        stage_n64all(rest)
    elif stage in table:
        table[stage]()
    else:
        print("unknown stage %r" % stage)
        sys.exit(64)
    print("=" * 74)
    print("TOTAL %d checks, %d FAILURES; %d registered predictions, %d misses"
          % (NCHK[0], NFAIL[0], NPRED[0], len(PREDFAIL)))
    for m in PREDFAIL:
        print("  registered-prediction MISS: %s" % m)
    print("=" * 74)
    sys.exit(1 if NFAIL[0] else 0)


if __name__ == "__main__":
    main()
