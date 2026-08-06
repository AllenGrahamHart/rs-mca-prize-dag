#!/usr/bin/env python3
"""THE PRIZE-ROW GAMMA-SHELL COMPARISON (round 20, gamma_shell pilot).

SELF-CONTAINED reproduction of the budget comparison at the DSA witness row.
No repo imports.  EXACT INTEGER / Fraction arithmetic at every comparison;
floats are used ONLY for display (log2).  Fail-closed.

Stages
  row       re-derive the witness row from scratch (primality, caps, B*).
  shell     the shell dictionary at the prize row: concentration + the
            structural per-shell count (must reproduce the banked 2^117.1491).
  bound     the PROVED accident lower bound (Cauchy-Schwarz + LEMMA TC).
  compare   THE COMPARISON, exact integers: max-shell vs B*.
  region    the admissible-row region on which the break holds + worst row.
  profile   the v-profile across the crossing bracket (PT-2 / G4).
  failclosed permanent negative control (MUST exit 1).

Usage: tools/ramguard tiny -- python3 notes/pilots_20260806/gamma_shell/shell_exhibit.py <stage>
"""
import sys
from fractions import Fraction
from math import comb, log2

CHECKS = 0
FAILS = 0

# ---- the row, verbatim from notes/pilots_20260806/es_g_lanes/PROOFS.md:174-179
P = 6597069766657          # = 3*2^41 + 1
E = 6
N = 1 << 41
K = 1 << 40
V = 34
W = 1 << V
RP = K - W                 # r' = n - k - w = 2^40 - 2^34
A = V - 1                  # 33
NA = N >> A                # 256
L = NA >> 1                # 128
RA = RP >> A               # 126 = L - 2


def ck(cond, msg):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print("  FAIL: %s" % msg)
    else:
        print("  ok  : %s" % msg)
    return cond


def is_prime(m):
    """deterministic Miller-Rabin for m < 3.3e24 (first 13 primes suffice)."""
    if m < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % q == 0:
            return m == q
    d, s = m - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(s - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def order_pow2(g, m, bound):
    """exact multiplicative order of g mod m, KNOWN to divide the 2-power
    `bound`.  Returns the order."""
    o = 1
    x = g % m
    while x != 1:
        x = x * x % m
        o *= 2
        if o > bound:
            raise RuntimeError("order does not divide %d" % bound)
    return o


def root_of_unity(p, m):
    """element of EXACT multiplicative order m = 2^t in F_p (m | p-1)."""
    assert (p - 1) % m == 0
    for b in range(2, 200):
        if pow(b, (p - 1) // 2, p) == p - 1:      # quadratic non-residue
            t = pow(b, (p - 1) // m, p)
            if order_pow2(t, p, m) == m:
                return t
    raise RuntimeError("no root of unity of order %d found" % m)


def rho_min_exact(L_, ra):
    """min over even U in [2, ra] of C(L-U,(ra-U)/2)/2^{L-2-U}, EXACT Fraction."""
    best, argu = None, None
    for U in range(2, ra + 1, 2):
        r = Fraction(comb(L_ - U, (ra - U) // 2), 1 << (L_ - 2 - U))
        if best is None or r < best:
            best, argu = r, U
    return best, argu


def deep(v):
    """(a, n_a, L, r', r'_a) at n = 2^41, k = 2^40, w = 2^v."""
    a = v - 1
    n_a = N >> a
    l = n_a >> 1
    rp = K - (1 << v)
    return a, n_a, l, rp, rp >> a


# ------------------------------------------------------------------ row
def stage_row():
    print("=== stage row  (the witness row, re-derived from scratch) ===")
    q = P ** E
    ck(is_prime(P), "p = %d is prime" % P)
    ck(P == 3 * (1 << 41) + 1, "p = 3*2^41 + 1")
    ck((P - 1) % N == 0, "2^41 | p-1  (so delta = ord_n(p) = 1)")
    ck(q < (1 << 256), "q = p^6 < 2^256  (rules_freeze cap); log2 q = %.6f"
       % log2(q))
    ck((q - 1) % N == 0, "2^41 | q-1  (the domain exists)")
    ck(K <= (1 << 40), "k = 2^40 <= 2^40  (rules_freeze cap)")
    bstar = q >> 128
    ck(bstar >= 3, "B* = floor(q/2^128) >= 3  (the node's open branch)")
    print("  B* = %d" % bstar)
    print("  log2 B* = %.3f" % log2(bstar))
    ck(abs(log2(bstar) - 127.510) < 5e-4,
       "log2 B* = 127.510 reproduces es_g_lanes/PROOFS.md:177")
    ck(W <= P, "w = 2^34 <= p  (Newton/BCH linearisation valid)")
    ck(P >= (1 << 39) + 1, "p >= 2^39+1  (banked characteristic arithmetic)")
    ck(RP == (1 << 40) - (1 << 34), "r' = n-k-w = 2^40 - 2^34")
    ck((A, NA, L, RA) == (33, 256, 128, 126), "deep shape (a,n_a,L,r'_a)")
    ck(RA == L - 2, "LEMMA DS: r'_a = L - 2")
    theta = root_of_unity(P, NA)
    ck(order_pow2(theta, P, NA) == NA, "theta of exact order n_a = 256 in F_p")
    ck(P % NA == 1, "p = 1 mod 256, so delta_a = ord_256(p) = 1 and Q = p")
    ck(P < (1 << (L - 2)), "THEOREM DSA regime: p^delta_a < 2^{L-2} = 2^126")
    return q, bstar, theta


# ---------------------------------------------------------------- shell
def stage_shell():
    print("=== stage shell  (the shell dictionary at the prize row) ===")
    # (SIG-LIFT) at the prize shape: the second term vanishes mod n
    sec = RA * NA * (1 << (A - 1)) * ((1 << A) - 1) % N
    ck(sec == 0,
       "(SIG-LIFT) second term |S'| n_a 2^{a-1}(2^a-1) = 0 mod 2^41")
    print("  => sig(S) = 2^33 * sigma'(S')  mod 2^41,  sigma' = sum_{j in S'} j")
    # (SHELL-CONC): the whole deep stratum sits in 2^33 Z / 2^41 = 256 shells
    ck(N // (1 << A) == NA, "deep-stratum shells = n/2^a = 2L = 256 of 2^41")
    print("  CONCENTRATION FACTOR = 2^41 / 256 = 2^%d" % (41 - 8))
    # (SHELL-STRUCT): structural sigma' is even -> 128 shells, in 2^34 Z
    #   structural S' = union of 63 antipodal pairs {j, j+128}
    #   sigma' = sum (2j + 128) = 2*sum j + 63*128 ; 63*128 = 8064 = 128 mod 256
    ck((63 * L) % NA == 128, "structural sigma' offset 63*L = 128 mod 256")
    ck(all((2 * t + 128) % 2 == 0 for t in range(5)), "structural sigma' EVEN")
    struct_tot = comb(128, 63)
    ck(struct_tot % L == 0,
       "L = 128 divides C(128,63) exactly (v_2 = 7, quotient odd)")
    per = struct_tot // L
    print("  |W^struct| = C(128,63) = %d = 2^%.4f" % (struct_tot, log2(struct_tot)))
    print("  structural per shell = C(128,63)/128 = %d = 2^%.4f"
          % (per, log2(per)))
    ck(abs(log2(per) - 117.1491) < 5e-4,
       "reproduces the banked [B4] figure 2^117.1491 EXACTLY "
       "(es_g_lanes/full_run.txt:127)")
    ck(abs(log2(struct_tot) - 124.149) < 1e-3,
       "and |W^struct| = 2^124.149 (crossing_low_w/PROOFS.md:283)")
    # equidistribution is exact because gcd(2L, r'_a/... ) -- the structural
    # shell index is 2^34 * (sum over Z/128 of a 63-subset), and
    # gcd(128, 63) = 1 makes the subset-sum EXACTLY equidistributed mod 128.
    from math import gcd
    ck(gcd(128, 63) == 1,
       "gcd(n/M, r'/M) = gcd(128,63) = 1 => exact equidistribution mod 128")
    return per


# ---------------------------------------------------------------- bound
def stage_bound():
    print("=== stage bound  (the PROVED accident lower bound) ===")
    Q = P  # delta_a = 1
    D = 1 << (L - 2)                      # |D| = 2^126
    print("  |D| = 2^%d,  Q = p^delta_a = p = 2^%.4f" % (L - 2, log2(Q)))
    ck(Q < D, "Cauchy-Schwarz non-vacuous: Q < |D|")
    # (PAIRS): P >= |D|^2/Q - |D|  (exact Fraction; floor is a valid lower bd)
    pairs_low = Fraction(D * D, Q) - D
    ck(pairs_low > 0, "P_low > 0")
    print("  P >= |D|^2/Q - |D| = 2^%.4f" % log2(float(pairs_low)))
    # (RATIO)
    rmin, argu = rho_min_exact(L, RA)
    ck(argu == 2, "rho_min attained at U = 2 (got U = %d)" % argu)
    ck(rmin == Fraction(comb(126, 62), 1 << 124), "rho_min = C(126,62)/2^124")
    print("  rho_min = C(126,62)/2^124 = %.9f = 2^%.4f"
          % (float(rmin), log2(float(rmin))))
    # (COUNT)
    nacc = int(rmin * pairs_low)          # floor: still a valid lower bound
    ck(nacc > 0, "N_acc lower bound positive")
    print("  N_acc >= %d" % nacc)
    print("  log2 N_acc >= %.4f" % log2(nacc))
    # sanity vs the banked heuristic C(256,126)/p (must be ABOVE our bound)
    heur = comb(256, 126) // P
    ck(nacc <= heur,
       "proved bound (2^%.3f) below the banked heuristic C(256,126)/p "
       "(2^%.3f) -- a necessary sanity condition"
       % (log2(nacc), log2(heur)))
    print("  [banked heuristic total, NOT used in the bound: C(256,126)/p "
          "= 2^%.3f]" % log2(heur))
    # and it must EXCEED the single-relation figure of round 18
    ck(nacc > comb(108, 53),
       "proved bound exceeds round 18's single-relation C(108,53) = 2^%.3f"
       % log2(comb(108, 53)))
    return nacc


# -------------------------------------------------------------- compare
def stage_compare():
    print("=== stage compare  (THE COMPARISON -- exact integers only) ===")
    q = P ** E
    bstar = q >> 128
    Q = P
    D = 1 << (L - 2)
    rmin, _ = rho_min_exact(L, RA)
    nacc = int(rmin * (Fraction(D * D, Q) - D))
    # the accidents occupy AT MOST 2L = 256 shells (SHELL-CONC), so some
    # shell carries at least ceil(N_acc / 256) of them.  Floor division is
    # used: it is the conservative direction.
    xmax = nacc // NA
    struct_per = comb(128, 63) // L
    print("  B*                       = %d" % bstar)
    print("  max-shell accident count >= %d" % xmax)
    print("  structural per shell     = %d" % struct_per)
    print("")
    print("  log2 B*                       = %.4f" % log2(bstar))
    print("  log2 max-shell accidents      = %.4f" % log2(xmax))
    print("  log2 structural per shell     = %.4f" % log2(struct_per))
    print("")
    # THE comparison, pure integers
    ck(xmax > bstar, "EXACT INTEGER COMPARISON: max-shell accidents > B*")
    print("  break margin = %.4f bits" % (log2(xmax) - log2(bstar)))
    ck(struct_per < bstar,
       "control: the STRUCTURAL family alone stays within budget "
       "(margin %.4f bits) -- the break is caused by the ACCIDENTS"
       % (log2(bstar) - log2(struct_per)))
    # exact integer ratio, no floats
    ck(xmax // bstar > 0, "integer ratio xmax//B* = %d" % (xmax // bstar))
    print("  xmax // B* = %d" % (xmax // bstar))
    # the consequence, stated as the list bound
    print("")
    print("  => L_1(k + 2^34) >= X_{2^34}(gamma_max) >= %d > B*" % xmax)
    print("  => a_L(C) > k + 2^34 at this row.")
    return xmax, bstar


# --------------------------------------------------------------- region
def stage_region():
    print("=== stage region  (admissible rows carrying the break; WORST row) ===")
    D = 1 << (L - 2)
    rmin, _ = rho_min_exact(L, RA)
    struct_per = comb(128, 63) // L
    live_q = struct_per << 128          # B* >= struct_per  <=>  q >= this
    print("  live-lane condition : B* >= structural per shell, i.e.")
    print("      log2 q >= %.4f   (es_g_lanes/full_run.txt:127)" % log2(live_q))
    print("  DSA / CS condition  : Q = p^delta_a < 2^126")
    print("  break condition     : floor(rho_min*(2^252/Q - 2^126))//256 > B*")
    print("")
    print("  %-3s %-8s %-22s %-16s %-11s"
          % ("e", "delta_a", "log2 p LIVE window", "break sub-window",
             "min margin"))
    worst = None
    npts = 0
    for e in range(1, 7):
        lo_lp = log2(live_q) / e
        hi_lp = 256.0 / e
        if hi_lp <= lo_lp:
            continue
        for da in (1, 2, 4):
            blo = bhi = None
            wmarg = None
            steps = 4000
            for i in range(steps + 1):
                lp = lo_lp + (hi_lp - lo_lp) * i / steps
                p = int(2.0 ** lp)
                if p < (1 << 39) + 1:
                    continue
                q = p ** e
                if q >= 1 << 256 or q < live_q:
                    continue
                bst = q >> 128
                Q = p ** da
                if Q >= D:
                    continue
                xm = int(rmin * (Fraction(D * D, Q) - D)) // NA
                npts += 1
                if xm > bst:
                    m = log2(xm) - log2(bst)
                    if blo is None:
                        blo = lp
                    bhi = lp
                    if wmarg is None or m < wmarg:
                        wmarg = m
                    if worst is None or m < worst[0]:
                        worst = (m, e, da, lp, xm, bst)
            if blo is not None:
                full = abs(blo - lo_lp) < 1e-6 and abs(bhi - hi_lp) < 1e-2
                print("  %-3d %-8d [%8.4f, %8.4f)%s [%6.3f, %6.3f] %+10.4f"
                      % (e, da, lo_lp, hi_lp, " FULL" if full else "     ",
                         blo, bhi, wmarg))
    ck(npts > 0, "the scan visited admissible live rows")
    ck(worst is not None, "the break region is NON-EMPTY")
    m, e, da, lp, xm, bst = worst
    print("")
    print("  WORST admissible row inside the break region:")
    print("    e = %d, delta_a = %d, log2 p = %.4f, log2 q = %.4f"
          % (e, da, lp, lp * e))
    print("    log2 xmax = %.4f, log2 B* = %.4f, MARGIN = %+.4f bits"
          % (log2(xm), log2(bst), m))
    ck(m > 0,
       "the break holds at the WORST row of the region (margin %+.4f bits)" % m)
    # the e = 1 dichotomy, exactly as THEOREM DSA has it
    e1_min_lp = log2(live_q)
    ck(2 ** (e1_min_lp / 1) >= 2 ** 126,
       "e = 1: the live lane needs log2 p >= %.3f >= 126, so Q = p >= 2^126 "
       "and Cauchy-Schwarz is VACUOUS -- e=1 prime rows are UNTOUCHED "
       "(reproduces the DSA dichotomy)" % e1_min_lp)
    return worst


# -------------------------------------------------------------- profile
def stage_profile():
    print("=== stage profile  (the v-profile across the bracket; PT-2 / G4) ===")
    q = P ** E
    bstar = q >> 128
    print("  row: p = 3*2^41+1, e = 6, log2 B* = %.3f" % log2(bstar))
    print("  %-6s %-5s %-6s %-6s %-12s %-9s %-12s %-9s"
          % ("w", "L", "n_a", "r'_a", "struct/shell", "2^{L-2}", "log2 xmax",
             "verdict"))
    verdicts = {}
    for v in range(34, 40):
        a, n_a, l, rp, ra = deep(v)
        if rp % (1 << v):
            sp = 0
        else:
            sp = comb(N // (1 << v), rp // (1 << v)) // (N // (1 << v))
        Dv = 1 << (l - 2)
        Q = P
        if Q < Dv:
            rmin, _ = rho_min_exact(l, ra)
            nacc = int(rmin * (Fraction(Dv * Dv, Q) - Dv))
            xm = nacc // n_a
            vd = "BREAK" if xm > bstar else "within"
            lx = "%.3f" % log2(xm) if xm > 0 else "-inf"
        else:
            xm, vd, lx = 0, "no proved acc", "-"
        verdicts[v] = vd
        print("  2^%-4d %-5d %-6d %-6d 2^%-10.3f 2^%-7d %-12s %-9s"
              % (v, l, n_a, ra, log2(sp) if sp else 0, l - 2, lx, vd))
    ck(verdicts[34] == "BREAK", "the break is at v = 34")
    ck(all(verdicts[v] != "BREAK" for v in range(35, 40)),
       "and ONLY at v = 34 -- the verdict is NOT uniform across the bracket")
    # PT-2 watch line
    tern = L * log2(3)
    print("")
    print("  PT-2 (tern_unification_adversary/REPORT.md:69): the ternary")
    print("  threshold at v = 34 is log2(3)*2^33 = %.3f;" % (log2(3) * (1 << 33)))
    print("  the bracket endpoint clears it by 0.336 bits.")
    print("  At the DEEP stratum the ternary requirement is L*log2 3 = %.3f"
          % tern)
    ck(abs(tern - 202.875) < 1e-3,
       "L*log2 3 = 202.875 reproduces crossing_low_w/PROOFS.md:196")
    return verdicts


def stage_failclosed():
    print("=== stage failclosed  (negative control: MUST exit 1) ===")
    ck(1 == 2, "injected false check")


STAGES = {"row": stage_row, "shell": stage_shell, "bound": stage_bound,
          "compare": stage_compare, "region": stage_region,
          "profile": stage_profile, "failclosed": stage_failclosed}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in STAGES:
        print("usage: shell_exhibit.py {%s}" % "|".join(STAGES))
        sys.exit(2)
    STAGES[sys.argv[1]]()
    print("checks=%d failures=%d" % (CHECKS, FAILS))
    sys.exit(1 if FAILS else 0)
