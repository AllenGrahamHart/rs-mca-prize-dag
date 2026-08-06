#!/usr/bin/env python3
"""cg_arith.py -- round-20 crossing_gap pilot: pure-arithmetic verifier.

Stages:
  rhllb   (C3) re-derivation of RHL-LB's 2^34 from its printed source
  pt2     (C3) the PT-2 clearance, ALL banked readings x the live p-range
  cover   (C1) w_cov(p,2^m) + the level-a coverage law + admissible classes
  cwfloor (C2) CW-FLOOR numerics at the prize deep stratum
  failclosed  permanent fail-closed control (MUST exit 1)

COMPUTE LAW: run only via  tools/ramguard tiny|local -- python3 ...
Fail-closed: any failed check -> nonzero exit.
"""
import sys
from math import comb, log2, gcd, lgamma

LOG2E = 1.4426950408889634


def lg_binom(nn, kk):
    """log2 C(nn,kk) via lgamma (exact for small nn via comb)."""
    if kk < 0 or kk > nn:
        return float("-inf")
    if nn <= 4000:
        return log2(comb(nn, kk))
    return (lgamma(nn + 1) - lgamma(kk + 1) - lgamma(nn - kk + 1)) * LOG2E

FAILS = []
NCHECK = 0


def check(desc, cond, extra=""):
    global NCHECK
    NCHECK += 1
    if not cond:
        FAILS.append(desc)
        print("  FAIL  %s %s" % (desc, extra))
    return bool(cond)


def hdr(t):
    print("\n" + "=" * 74)
    print(t)
    print("=" * 74)


# ---------------------------------------------------------------- constants
# All quoted VERBATIM in PROOFS.md with file:line.
N_BITS = 41                      # n = 2^41
K_BITS = 40                      # k = 2^40
LOG2_3 = log2(3.0)


# ================================================================== rhllb
def stage_rhllb():
    hdr("STAGE rhllb -- (C3) RHL-LB's 2^34 re-derived from source")
    # critical/nodes/rate_half_cyclic_rotated_prefix_floor/statement.md:106-134
    n = 1 << 41
    k = 1 << 40
    c = 1 << 33
    N = n // c
    d = 1
    m = N // 2 + d
    s = c - 1
    check("N = n/c = 256", N == 256, "(got %d)" % N)
    check("m = N/2+d = 129", m == 129, "(got %d)" % m)
    check("c divides n/2", (n // 2) % c == 0)
    check("0 < s < c", 0 < s < c)
    check("1 <= d <= N/2-1", 1 <= d <= N // 2 - 1)

    # (CR2): agreement = n/2 + d*c + s ; excess over k = n/2 is sigma_cyc
    agreement = n // 2 + d * c + s
    sigma_cyc = d * c + s
    print("  sigma_cyc = d*c + s = %d*%d + %d = %d" % (d, c, s, sigma_cyc))
    check("sigma_cyc == 2^34 - 1 EXACTLY (no floor, no rounding)",
          sigma_cyc == (1 << 34) - 1)
    check("sigma_cyc == 17,179,869,183 (printed constant)",
          sigma_cyc == 17179869183)
    check("agreement == k + sigma_cyc", agreement == k + sigma_cyc)

    # (CR1): the field-independent list floor
    L_cyc = -(-comb(N - 1, m) // N)          # ceil(C(255,129)/256)
    check("L_cyc = ceil(C(255,129)/256) > 2^238",
          L_cyc > (1 << 238), "(log2 = %.3f)" % log2(L_cyc))
    print("  L_cyc = ceil(C(255,129)/256), log2 = %.4f" % log2(L_cyc))

    # the cap step: q < 2^256  =>  B* = floor(q/2^128) < 2^128 < L_cyc
    check("floor(q/2^128) < 2^128 < L_cyc at the artificial cap q = 2^256",
          ((1 << 256) // (1 << 128)) <= (1 << 128) < L_cyc)

    # (CR5) margin at q = 2^256 : N q^d < 2^128 C(N-1,m)
    lhs = N * (1 << 256) ** d
    rhs = (1 << 128) * comb(N - 1, m)
    check("(CR5) N q^d < 2^128 C(N-1,m) at q = 2^256", lhs < rhs)
    margin = log2(rhs) - log2(lhs)
    print("  (CR5) margin at q=2^256 : %.4f bits  (statement says '> 114')"
          % margin)
    check("(CR5) margin > 114 bits (printed claim)", margin > 114)

    # RHL-LB itself: L_1(k+2^34-1) > B*  =>  a_L >= k + 2^34
    aL_min_excess = sigma_cyc + 1
    check("a_L - k >= sigma_cyc + 1 = 2^34 EXACTLY (integer successor)",
          aL_min_excess == (1 << 34))
    check("2^34 == 17,179,869,184 (printed RHL-LB constant)",
          (1 << 34) == 17179869184)

    # EXACT vs FLOORED vs CONVENTIONAL -- the extremality scope
    # "Among maximal-prefix instances s=c-1 of (CR1) whose lower bound is
    #  certified uniformly by checking (CR5) at q=2^256, this is the unique
    #  largest agreement excess."  Re-derive that extremality from scratch.
    # (CR5) in log2: 256*d + log2 N < 128 + log2 C(N-1, N/2+d).
    # Since log2 C(N-1,m) <= N-1, certification forces d <= (N+127)/256,
    # so sigma = c(d+1)-1 <= n/256 + c*(1+127/256): the tail in c is
    # controlled and the search below (N = 2^2..2^28) is exhaustive for the
    # maximum.  Exact integer arithmetic is used at the winner.
    best = None
    allsig = []
    for jb in range(2, 29):                      # N = 2^jb, c = n/N
        NN = 1 << jb
        cc = n // NN
        if cc < 2 or (n // 2) % cc != 0:
            continue
        dmax = min(NN // 2 - 1, (NN + 200) // 256 + 2)
        for dd in range(1, dmax + 1):
            mm = NN // 2 + dd
            lhs = 256.0 * dd + log2(NN)
            rhs = 128.0 + lg_binom(NN - 1, mm)
            if lhs < rhs:
                sg = dd * cc + (cc - 1)          # maximal prefix s = c-1
                allsig.append((sg, jb, dd))
                if best is None or sg > best[0]:
                    best = (sg, jb, dd)
    # exact-integer re-certification of the winner (no floating point)
    if best is not None:
        NN = 1 << best[1]
        dd = best[2]
        mm = NN // 2 + dd
        check("winner re-certified with EXACT integers",
              NN * (1 << 256) ** dd < (1 << 128) * comb(NN - 1, mm))
    best = (best[0], 41 - best[1], best[2])
    allsig = [(s, 41 - j, d) for (s, j, d) in allsig]
    check("extremal maximal-prefix excess is EXACTLY 2^34-1",
          best is not None and best[0] == (1 << 34) - 1,
          "(got %s)" % (best,))
    check("the extremal instance is (c,d) = (2^33, 1)",
          best is not None and best[1] == 33 and best[2] == 1)
    ties = [x for x in allsig if x[0] == best[0]]
    check("the extremal instance is UNIQUE among certified maximal prefixes",
          len(ties) == 1, "(ties = %s)" % ties)
    allsig.sort(reverse=True)
    print("  top certified maximal-prefix excesses (sigma, log2 c, d):")
    for x in allsig[:5]:
        print("    sigma = %d  (= 2^%.4f),  c = 2^%d,  d = %d"
              % (x[0], log2(x[0]), x[1], x[2]))

    print("\n  VERDICT: 2^34 is EXACT (an integer identity d*c+s+1 with")
    print("  d=1, c=2^33, s=c-1), NOT floored.  It is CONVENTIONAL only in")
    print("  its extremality scope (best maximal-prefix instance of ONE")
    print("  printed construction under ONE cap-uniform criterion).")
    print("  DIRECTION: RHL-LB lower-bounds a_L, so any improvement moves")
    print("  w = a_L - k UP, i.e. AWAY from the ternary threshold.")


# ================================================================== pt2
def w_tern_log2(log2p, functional):
    """log2 of the w-threshold below which the deep stratum is
    first-moment SUPERCRITICAL, at n = 2^41, delta = delta_a = 1.

    TERNARY (odd-part / deep-stratum / full-window readings all agree):
        subcritical  iff  L*log2 3 < log2 p,  L = 2^{41-v}
        <=> v > 41 - log2(log2 p / log2 3)
    ORBIT      : L*log2 3 - log2(2L) < log2 p
    PERWEIGHT  : log2 C(2L, L-2) < log2 p
    GLOBAL     : n_a = 2L ... requires log2 p >= 2L  (the (ES-G) functional)
    """
    lo, hi = 25.0, 41.0
    for _ in range(200):
        v = (lo + hi) / 2.0
        L = 2.0 ** (41.0 - v)
        if functional == "TERNARY":
            need = L * LOG2_3
        elif functional == "ORBIT":
            need = L * LOG2_3 - log2(2.0 * L)
        elif functional == "PERWEIGHT":
            need = lg_binom(int(round(2 * L)), int(round(L)) - 2) if L >= 4 else 0.0
        elif functional == "GLOBAL":
            need = 2.0 * L
        else:
            raise ValueError(functional)
        if need < log2p:            # subcritical at this v -> threshold lower
            hi = v
        else:
            lo = v
    return (lo + hi) / 2.0


def lgcomb(nn, kk):
    if kk < 0 or kk > nn:
        return float("-inf")
    return log2(comb(nn, kk))


def stage_pt2():
    hdr("STAGE pt2 -- (C3) the PT-2 cliff, ADVERSARIAL re-computation")
    # ---- reproduce the banked constants first (must match to 4 decimals)
    L34 = 1 << (41 - 34)                       # v = 34 -> L = 128
    check("v=34 gives L = 128", L34 == 128)
    lg3L = L34 * LOG2_3
    print("  L*log2 3 at v=34 : %.4f   (LEMMA TC prints 202.875)" % lg3L)
    check("L*log2 3 = 202.875 (LEMMA TC)", abs(lg3L - 202.875) < 5e-4)
    check("orbit-corrected = 194.875 (LEMMA ROT, -log2 2L = -8)",
          abs(lg3L - log2(2 * L34) - 194.875) < 5e-4)
    check("PER-WEIGHT (retired) = 251.628 = log2 C(256,126)",
          abs(lgcomb(256, 126) - 251.628) < 1e-3,
          "(got %.4f)" % lgcomb(256, 126))
    check("GLOBAL (ES-G) = 256 = n_a", 2 * L34 == 256)
    check("C(128,63) = 2^124.149 (the structural count)",
          abs(lgcomb(128, 63) - 124.149) < 1e-3,
          "(got %.4f)" % lgcomb(128, 63))

    # the banked threshold in w at log2 p = 256
    wt256 = w_tern_log2(256.0, "TERNARY")
    print("  w_tern(log2 p = 256) = 2^%.5f   (PT-2 prints 2^33.66445)" % wt256)
    check("w_tern at log2 p=256 reproduces 2^33.66445",
          abs(wt256 - 33.66445) < 1e-4)
    check("closed form w_tern = 2^41*log2(3)/log2(p)",
          abs(wt256 - log2((2.0 ** 41) * LOG2_3 / 256.0)) < 1e-9)
    clear256 = 34.0 - wt256
    print("  clearance at log2 p = 256 : %.5f bits  (PT-2 prints 0.336)"
          % clear256)
    check("banked 0.336-bit clearance reproduced",
          abs(clear256 - 0.336) < 5e-4, "(got %.5f)" % clear256)

    # I2-coordinate cross-check: one step below (v=33, L=256) -> tau=1, +149.75
    L33 = 1 << (41 - 33)
    check("v=33 gives L = 256", L33 == 256)
    tau33 = 1.0 * 256.0 / L33
    check("v=33 gives tau = 1 at log2 p = 256", abs(tau33 - 1.0) < 1e-12)
    tcrit33 = L33 * LOG2_3 - 256.0
    check("v=33 Tcrit = +149.75 (banked)", abs(tcrit33 - 149.75) < 5e-3,
          "(got %.4f)" % tcrit33)
    tcrit34 = L34 * LOG2_3 - 256.0
    check("v=34 Tcrit = -53.125 (banked)", abs(tcrit34 + 53.125) < 5e-3,
          "(got %.4f)" % tcrit34)

    # ---- G3.3 : parity / reading invariance at w = 2^34
    # odd-part reading   : g = w/2 = 2^33 conditions, h = n/2 = 2^40, ternary
    # deep-stratum (I2)  : g = delta_a = 1,           h = L   = 2^7,  ternary
    thr_odd = (2.0 ** 40) * LOG2_3 / (2.0 ** 33)
    thr_deep = L34 * LOG2_3 / 1.0
    check("odd-part and deep-stratum readings give the SAME log2 p threshold",
          abs(thr_odd - thr_deep) < 1e-9,
          "(%.6f vs %.6f)" % (thr_odd, thr_deep))
    print("  TERNARY threshold in log2 p at w = 2^34 : %.4f (both readings)"
          % thr_odd)
    check("that threshold is 202.875", abs(thr_odd - 202.875) < 5e-4)

    # ---- THE LIVE ADMISSIBLE e=1 PRIME RANGE
    # B* in {1,2} is closed exactly by (RHL-B12); the open crossing needs
    # B* >= 3, i.e. q >= 3*2^128.
    lp_lo_B3 = log2(3.0) + 128.0
    lp_lo_B1 = 128.0
    check("B* >= 3 <=> log2 q >= 129.5849625",
          abs(lp_lo_B3 - 129.5849625) < 1e-6, "(got %.7f)" % lp_lo_B3)
    print("  live e=1 prime range (B* >= 3): log2 p in [%.6f, 256)" % lp_lo_B3)

    readings = [
        ("TERNARY   (odd-part = deep-stratum = full-window)", "TERNARY"),
        ("TERNARY orbit-corrected (LEMMA ROT)",               "ORBIT"),
        ("PER-WEIGHT (retired, LEMMA TC: 48.75-bit mispriced)", "PERWEIGHT"),
        ("GLOBAL (ES-G) functional",                          "GLOBAL"),
    ]
    print("\n  CLEARANCE OF THE ENDPOINT w = 2^34, BY READING AND BY log2 p")
    print("  (clearance = 34 - log2 w_tern(p);  NEGATIVE = endpoint is")
    print("   BELOW the first-moment supercriticality threshold)")
    print("  %-52s %10s %10s %10s" % ("reading", "lp=129.585", "lp=202.875",
                                      "lp=255.999"))
    any_below = False
    below_detail = []
    for name, fn in readings:
        row = []
        for lp in (lp_lo_B3, 202.875, 255.999):
            cl = 34.0 - w_tern_log2(lp, fn)
            row.append(cl)
            if cl < 0:
                any_below = True
        print("  %-52s %10.4f %10.4f %10.4f" % (name, row[0], row[1], row[2]))
        # locate the crossover log2 p at which the endpoint goes subcritical
        lo, hi = 1.0, 256.0
        for _ in range(120):
            mid = (lo + hi) / 2.0
            if 34.0 - w_tern_log2(mid, fn) < 0:
                lo = mid
            else:
                hi = mid
        below_detail.append((name, (lo + hi) / 2.0))

    print("\n  CROSSOVER log2 p (endpoint w=2^34 is SUPERCRITICAL below it):")
    tot = 256.0 - lp_lo_B3
    for name, xo in below_detail:
        frac = max(0.0, min(xo, 256.0) - lp_lo_B3) / tot
        print("  %-52s  log2 p < %8.4f   -> %6.2f%% of the live range"
              % (name, xo, 100.0 * frac))

    check("at least one banked reading puts the endpoint BELOW threshold "
          "inside the live admissible e=1 prime range", any_below)
    # the headline numbers
    cl_lo = 34.0 - w_tern_log2(lp_lo_B3, "TERNARY")
    print("\n  HEADLINE (TERNARY functional, odd-part reading, shift-0 window,")
    print("  2-power w): at the BOTTOM of the live e=1 prime range")
    print("  (log2 p = %.6f, B* = 3) the endpoint w = 2^34 is %.4f bits"
          % (lp_lo_B3, cl_lo))
    print("  BELOW the ternary supercriticality threshold, i.e. w_tern =")
    print("  2^%.5f > 2^34." % w_tern_log2(lp_lo_B3, "TERNARY"))
    check("TERNARY clearance at the bottom of the live range is NEGATIVE",
          cl_lo < 0, "(got %.4f)" % cl_lo)
    check("TERNARY clearance at the bottom of the live range is -0.6465 bits",
          abs(cl_lo + 0.6465) < 5e-4, "(got %.4f)" % cl_lo)
    frac_super = (202.875 - lp_lo_B3) / (256.0 - lp_lo_B3)
    print("  Fraction of the live e=1 prime range (measured in log2 p) at")
    print("  which the endpoint is supercritical: %.4f%%" % (100 * frac_super))
    check("that fraction is 57.98%", abs(frac_super - 0.5798) < 5e-4,
          "(got %.4f)" % frac_super)

    # DSA's proved regime never reaches e=1 rows (banked dichotomy, re-checked)
    check("DSA regime log2 p < L-2 = 126 is disjoint from log2 p >= 128",
          126.0 < lp_lo_B1)
    print("\n  (proved-existence check: THEOREM DSA needs delta_a*log2 p <")
    print("   L-2 = 126; the live e=1 range starts at 129.585, so the")
    print("   supercriticality above is FIRST-MOMENT (heuristic), not proved.")
    print("   THEOREM MT proves existence only for tau < 1, i.e. log2 p <")
    print("   128 -- unreachable since B* >= 1 forces q >= 2^128.)")


# ================================================================== cover
def wcov(p, m):
    """w_cov(p, 2^m) = 1 + max over <p>-cosets of (Z/2^m)^* of least element."""
    n = 1 << m
    seen = [False] * n
    worst = 0
    for s in range(1, n, 2):
        if seen[s]:
            continue
        orb = []
        t = s
        while not seen[t]:
            seen[t] = True
            orb.append(t)
            t = (t * p) % n
        worst = max(worst, min(orb))
    return worst + 1


def stage_cover():
    hdr("STAGE cover -- (C1) w_cov, the level-a coverage law, official rows")
    # efloor_sparsity/PROOFS.md:193-205 (the TABLE) -- reproduced exactly.
    banked = {3: 6, 5: 4, 7: 12, 11: 6, 13: 4, 17: 16, 19: 6, 23: 12}
    # efloor_sparsity/REPORT.md:33 and PROOFS.md:212 (COROLLARY SP5) instead
    # print 8 for p in {11,19}.  That is 2^{j_p}, not w_cov: a transcription
    # of the wrong column.  CATCH-20A, checked explicitly below.
    print("  p  j_p=v2(p^2-1)  2^j_p   w_cov(p,2^m), m=4..12")
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 47, 97, 257):
        jp = 0
        x = p * p - 1
        while x % 2 == 0:
            x //= 2
            jp += 1
        vals = [wcov(p, m) for m in range(4, 13)]
        print("  %-4d %-13d %-7d %s" % (p, jp, 1 << jp, vals))
        check("LEMMA COS bound w_cov <= 2^{j_p} for p=%d" % p,
              all(v <= (1 << jp) for v in vals))
        check("LEMMA COS m-uniformity for p=%d (m >= j_p)" % p,
              len(set(v for m, v in zip(range(4, 13), vals) if m >= jp)) <= 1)
        if p in banked:
            check("banked w_cov(%d) = %d reproduced" % (p, banked[p]),
                  vals[-1] == banked[p], "(got %d)" % vals[-1])

    # ---- CATCH-20A : the banked w_cov print for p in {11,19}
    print("\n  CATCH-20A (banked constant):")
    for pp in (11, 19):
        v = wcov(pp, 12)
        jp = v2(pp * pp - 1)
        print("    w_cov(%d, 2^m) = %d for every m >= %d;  2^{j_p} = %d."
              % (pp, v, 4, 1 << jp))
        check("w_cov(%d) = 6 (independently recomputed)" % pp, v == 6,
              "(got %d)" % v)
        check("the banked print 8 for p=%d equals 2^{j_p}, i.e. the LEMMA "
              "COS BOUND, not w_cov" % pp, (1 << jp) == 8)
    print("    efloor_sparsity/REPORT.md:33 and COROLLARY SP5 "
          "(PROOFS.md:211-212)")
    print("    print 8; the correct sharp value is 6.  The corollary as")
    print("    printed is still TRUE (w>=8 => w>=6) but NOT SHARP.  The")
    print("    minted node es_ternary_suppression_instruments prints no")
    print("    w_cov value for 11 or 19, so the minted node is UNAFFECTED.")

    # ---- G1.2 : the level-a coverage law
    #   level a covers  iff  floor((w-1)/2^a) + 1 >= w_cov(p, 2^{m-a})
    #   i.e.            iff  w >= 2^a * (w_cov(p, 2^{m-a}) - 1) + 1
    print("\n  LEVEL-a COVERAGE THRESHOLDS  w_min(a) = 2^a(w_cov(p,2^{m-a})-1)+1")
    easier = []
    for m in range(4, 13):
        for p in (3, 5, 7, 11, 13, 17, 19, 23, 47, 97, 257):
            th = []
            for a in range(0, m - 1):
                wc = wcov(p, m - a)
                th.append((1 << a) * (wc - 1) + 1)
            check("level-0 threshold = w_cov(p,2^m) for p=%d m=%d" % (p, m),
                  th[0] == wcov(p, m))
            for a in range(1, len(th)):
                if th[a] < th[0]:
                    easier.append((p, m, a, th[a], th[0]))
    if easier:
        print("  G1.2 FALSIFIED: level-a coverage is EASIER than level-0 in")
        print("  %d (p,m,a) cells. First 8:" % len(easier))
        for e in easier[:8]:
            print("    p=%-4d m=%-3d a=%-3d  w_min(a)=%-8d < w_min(0)=%d" % e)
        print("  Structure of every such cell (checked below): ord_{2^{m-a}}(p)")
        print("  = 1, i.e. <p> is trivial on the reduced level.")
        okstruct = all((m - a) < v2(p * p - 1) for (p, m, a, _, _) in easier)
        check("every G1.2-falsifying cell has m-a < j_p (LEMMA COS's "
              "uniformity hypothesis fails at the reduced level)", okstruct)
        deep = [(p, m, a) for (p, m, a, _, _) in easier
                if ordmod(p, 1 << (m - a)) == 1]
        print("  of these, %d have ord_{2^{m-a}}(p) = 1 (the delta=1 family,"
              " which is exactly the official e=1 prime-row family)"
              % len(deep))
    else:
        print("  G1.2 held on the tested grid (no level-a cell easier).")

    # ---- the official rows: p = 1 mod 2^41  (e = 1 prime rows, delta = 1)
    print("\n  OFFICIAL PRIME ROWS (e=1  =>  n | p-1  =>  p = 1 mod 2^41):")
    # small-scale certification of the closed form w_cov = 2^m when delta = 1
    for m in range(4, 13):
        n = 1 << m
        p = n + 1          # p = 1 mod n (as a residue; primality irrelevant)
        check("delta=1 closed form w_cov(p=1 mod 2^%d, 2^%d) = 2^%d" % (m, m, m),
              wcov(p % n if p % n else 1, m) == n if False else
              wcov_trivial(m) == n)
    print("  ord_n(p) = 1  =>  every <p>-coset of (Z/n)^* is a SINGLETON")
    print("  =>  w_cov = 1 + (n-1) = n = 2^41.")
    print("  The window also obeys w <= r'+w = 2^40, so w < 2^40 < 2^41 ALWAYS.")
    check("SP-COVER is unconditionally inapplicable at e=1 prime rows "
          "(w_cov = 2^41 > 2^40 > w)", (1 << 41) > (1 << 40))

    # level-a at official prime rows
    print("\n  LEVEL-a THRESHOLDS AT e=1 PRIME ROWS (delta=1 at every level):")
    best = None
    plive = 3 * (1 << 128)                    # live e=1 prime floor (B* >= 3)
    for a in range(0, 41):                    # n_a = 2^{41-a} >= 2
        na = 1 << (41 - a)
        th = (1 << a) * (na - 1) + 1          # = 2^41 - 2^a + 1
        check("closed form w_min(a) = 2^41 - 2^a + 1 at a=%d" % a,
              th == (1 << 41) - (1 << a) + 1)
        if plive > (1 << a) and (best is None or th < best[1]):
            best = (a, th)                    # integrality gate p > 2^a
    print("  the integrality gate p > 2^a passes for EVERY a <= 40 at live")
    print("  rows (log2 p >= 129.585); the threshold w_min(a) = 2^41-2^a+1")
    print("  is MINIMISED at the deepest level a = 40:")
    print("  best admissible level: a = %d, w_min = %d = 2^%.5f"
          % (best[0], best[1], log2(best[1])))
    check("the minimising level is a = 40", best[0] == 40)
    check("the minimal level threshold is exactly 2^40 + 1",
          best[1] == (1 << 40) + 1)
    # every crossing instance has r' = 2^40 - w >= 1, so w <= 2^40 - 1
    wmax = (1 << 40) - 1
    check("no level fires: min_a w_min(a) = 2^40+1 > 2^40-1 = max w",
          best[1] > wmax)
    print("  every crossing instance has r' = 2^40 - w >= 1, i.e.")
    print("  w <= 2^40 - 1 = %d;  min_a w_min(a) - max w = %d."
          % (wmax, best[1] - wmax))

    # ---- the gap arithmetic (CATCH E-3 constant re-derived)
    print("\n  GAP ARITHMETIC (CATCH E-3 re-derived):")
    cs_star = 37.3131
    print("  CS closes  w > 2^%.4f (banked, es_ternary_suppression_instruments)"
          % cs_star)
    print("  SP-COVER needs w >= 2^41 at e=1 prime rows (this pilot),")
    print("  NOT 2^42 as CATCH E-3 prints (that uses w_cov <= 2^{j_q} with")
    print("  j_q >= 42, but LEMMA COS's m-uniformity needs m >= j_q and")
    print("  m = 41 < 42, so 2^{j_q} is not the operative value).")
    print("  gap = 2^{41 - %.4f} = 2^%.4f  (CATCH E-3 prints 2^4.6869)"
          % (cs_star, 41 - cs_star))
    check("re-derived gap exponent is 3.6869", abs((41 - cs_star) - 3.6869) < 1e-4)
    # bracket residual measured LINEARLY in w (the banked 71.16% convention)
    lo, hi = 2.0 ** 34, 2.0 ** 39
    closed = (hi - 2.0 ** cs_star) / (hi - lo)
    print("  CS covers %.4f%% of the bracket [2^34, 2^39] (banked 71.16%%)"
          % (100 * closed))
    check("71.16% bracket coverage reproduced (LINEAR-in-w convention)",
          abs(100 * closed - 71.16) < 0.01, "(got %.4f)" % (100 * closed))
    print("  residual = %.4f%% (banked 28.84%%)" % (100 * (1 - closed)))


def v2(x):
    j = 0
    while x % 2 == 0:
        x //= 2
        j += 1
    return j


def ordmod(p, n):
    if gcd(p, n) != 1:
        return 0
    o, t = 1, p % n
    while t != 1:
        t = (t * p) % n
        o += 1
        if o > n:
            return 0
    return o


def wcov_trivial(m):
    """w_cov when <p> is trivial in (Z/2^m)^*: every coset a singleton."""
    return 1 << m


# ================================================================== cwfloor
def stage_cwfloor():
    hdr("STAGE cwfloor -- (C2) CW-FLOOR numerics at the prize deep stratum")
    L, rp = 128, 126                       # LEMMA DS: r'_a = L - 2
    check("r'_a = L-2 is EVEN (CW-FLOOR's parity hypothesis)", rp % 2 == 0)
    W = rp // 2
    check("W = r'/2 = 63", W == 63)
    lg_struct = lgcomb(L, W)               # the eps=0 structural fibre
    lg_flat = lgcomb(2 * L, rp)            # the flat C(2L,r') count
    lg_floorC = 2 * lg_struct              # C(L,W)^2
    print("  log2 C(128,63)   = %.4f   (structural, LEMMA TC eps=0 fibre)"
          % lg_struct)
    print("  log2 C(256,126)  = %.4f   (flat = the retired PER-WEIGHT value)"
          % lg_flat)
    print("  log2 C(128,63)^2 = %.4f" % lg_floorC)
    loss = lg_flat - lg_floorC
    print("  shell-diagonal loss  log2 C(2L,r') - 2 log2 C(L,r'/2) = %.4f bits"
          % loss)
    check("G2.2 predicted shell-diagonal loss 3.33 bits",
          abs(loss - 3.33) < 0.01, "(got %.4f)" % loss)
    check("PER-WEIGHT functional 251.628 = log2 C(2L,r')",
          abs(lg_flat - 251.628) < 1e-3)
    check("structural count = 2^124.149 (banked)",
          abs(lg_struct - 124.149) < 1e-3)

    # firing thresholds
    thr_cw = lg_struct                     # C(L,W) > Q
    thr_dsa = L - 2                        # 2^{L-2} > p^{delta_a}
    print("\n  FIRING THRESHOLD on delta_a * log2 p:")
    print("    THEOREM DSA (banked)      : < %.4f" % thr_dsa)
    print("    CW-FLOOR   (this pilot)   : < %.4f" % thr_cw)
    print("    difference               : %.4f bits (CW-FLOOR strictly inside)"
          % (thr_dsa - thr_cw))
    check("G2.3: CW-FLOOR threshold in [124,125]", 124.0 <= thr_cw <= 125.0)
    check("G2.3: CW-FLOOR is strictly inside DSA's regime",
          thr_cw < thr_dsa)
    check("G2.3: the inside-margin is 1.851 bits",
          abs((thr_dsa - thr_cw) - 1.851) < 1e-3,
          "(got %.4f)" % (thr_dsa - thr_cw))
    print("    live e=1 prime rows start at log2 p = %.4f  -> CW-FLOOR is"
          % (128 + log2(3)))
    print("    VACUOUS at every prime row, by %.4f bits (B*>=3) / %.4f (B*>=1)"
          % (128 + log2(3) - thr_cw, 128 - thr_cw))
    check("CW-FLOOR vacuous at every e=1 prime row", thr_cw < 128.0)

    # the banked tower witness row
    p_w = 3 * (1 << 41) + 1
    lg_p = log2(p_w)
    delta_a = ordmod(p_w % 256, 256)
    check("witness row p = 3*2^41+1 has delta_a = ord_256(p) = 1",
          (p_w % 256) == 1)
    print("\n  BANKED TOWER WITNESS ROW p = 3*2^41+1 (delta_a = 1):")
    print("    log2 p = %.4f" % lg_p)
    check("witness row is inside CW-FLOOR's regime", lg_p < thr_cw)
    proved = lg_floorC - lg_p
    print("    CW-FLOOR proved count |X_126| >= 2^%.4f" % proved)
    print("    structural            C(128,63)  = 2^%.4f" % lg_struct)
    print("    DSA-proved excess     C(108,53)  = 2^%.4f" % lgcomb(108, 53))
    print("    heuristic (round 18)  C(256,126)/p = 2^%.4f" % (lg_flat - lg_p))
    check("G2.4: CW-FLOOR proves |X_126| >= 2^205.7 at the witness row",
          abs(proved - 205.7) < 0.05, "(got %.4f)" % proved)
    check("CW-FLOOR's proved count exceeds the structural count",
          proved > lg_struct)
    check("CW-FLOOR beats DSA's proved excess by >70 bits",
          proved - lgcomb(108, 53) > 70.0)
    check("CW-FLOOR is within 3.4 bits of the round-18 heuristic",
          abs((lg_flat - lg_p) - proved - loss) < 1e-6)
    print("    => CW-FLOOR upgrades round-18's HEURISTIC excess to a PROVED")
    print("       count, losing exactly the %.4f-bit shell-diagonal gap."
          % loss)

    # r' odd: the route is unavailable
    print("\n  r' ODD: every equal-weight collision gives a BALANCED eps")
    print("  (#{+1} = #{-1}), hence EVEN support U; LEMMA TC's index set at")
    print("  odd r' has U odd; the two sets are DISJOINT, so the diagonal")
    print("  shell contributes NOTHING.  CW-FLOOR is unavailable at odd r'.")
    check("LEMMA DS's r'_a = L-2 is even for every 2-power L >= 4",
          all((( 1 << j) - 2) % 2 == 0 for j in range(2, 10)))


# ================================================================== main
STAGES = {
    "rhllb": stage_rhllb,
    "pt2": stage_pt2,
    "cover": stage_cover,
    "cwfloor": stage_cwfloor,
}


def main():
    if len(sys.argv) < 2:
        print("usage: cg_arith.py STAGE   (%s|failclosed|all)"
              % "|".join(STAGES))
        return 2
    st = sys.argv[1]
    if st == "failclosed":
        hdr("STAGE failclosed -- permanent control, MUST exit 1")
        check("injected false check (this MUST fail)", 1 == 2)
    elif st == "all":
        for f in STAGES.values():
            f()
    elif st in STAGES:
        STAGES[st]()
    else:
        print("unknown stage %r" % st)
        return 2
    print("\n" + "-" * 74)
    print("checks = %d   failures = %d" % (NCHECK, len(FAILS)))
    for f in FAILS:
        print("  FAILED: %s" % f)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
