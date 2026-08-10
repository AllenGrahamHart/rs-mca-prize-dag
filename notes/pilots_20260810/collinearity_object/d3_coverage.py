"""D3/D4: the coverage arithmetic and the payoff map, RE-DERIVED.

(1) apolar's (AO1) closure band, re-derived from the printed formula and
    checked against their banked table;
(2) my rigid band  a >= ceil((16m+3)/3)  (RIG = a-1-2s >= 0, s = R+1-a);
(3) the residual GAP, exactly, for m in [1,40] and for m = 2^j;
(4) D4: the payoff arithmetic from the profile constants, re-derived.

Profile (primary text, background/nodes/rate_half_ca_hankel_
endpoint_saturation_rigidity/statement.md and .../half_distance_a3_
slope_slack_ledger/statement.md):
    rho = 4m-1,  N = 16m,  R = 8m,  A = R+1-2rho = 3,  e = m,
    target T <= rho+1 = 4m,  failure size T = rho+2 = 4m+1  (SAT3),
    d_x <= m  and  sum_x (m-d_x) = 1+O <= m  (SAT4).
Official row: n = 2^41 = N  =>  m = 2^37, rho+1 = 2^39, rho+2 = 2^39+1.

Stdlib only.  Run under tools/ramguard.
"""


def say(s=""):
    print(str(s), flush=True)


def AO1(m, a, O):
    """apolar's (AO1) cap, re-derived from their printed formula."""
    rho, N, R1, e = 4 * m - 1, 16 * m, 8 * m + 1, m
    if a <= rho or a >= R1:
        return None
    t1 = min(e + 1, a // (a - rho), (a * e + O) // rho)
    t2 = (N - a) * e // (R1 - a)
    return t1 + t2


def apolar_band(m, O=0):
    """the band is contiguous from a=4m (verified exhaustively for m<=40);
    for large m find its top by binary search."""
    rho = 4 * m - 1
    ok = lambda a: (AO1(m, a, O) is not None and AO1(m, a, O) <= rho + 1)
    if m <= 64:
        good = [a for a in range(rho + 1, 8 * m + 1) if ok(a)]
        return (min(good), max(good)) if good else None
    lo = 4 * m
    if not ok(lo):
        return None
    hi = 8 * m - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if ok(mid):
            lo = mid
        else:
            hi = mid - 1
    return (4 * m, lo)


def rigid_threshold(m):
    """smallest a with RIG = a-1-2s >= 0, s = R+1-a = 8m+1-a."""
    return -(-(16 * m + 3) // 3)


say("=== 1. (AO1) re-derivation vs apolar's banked table (O=0) ===")
say("   m   band [a_min..a_max]   rho+1   4m+2   banked")
banked = {1: (4, 5), 2: (8, 10), 3: (12, 15), 4: (16, 19), 5: (20, 24),
          6: (24, 31), 7: (28, 35), 36: (144, 191), 37: (148, 195),
          38: (152, 202), 39: (156, 207), 40: (160, 211)}
agree = 0
for m in sorted(banked):
    b = apolar_band(m)
    ok = (b == banked[m])
    agree += ok
    say("  %3d  [%d..%d]  %8d %6d   %s %s"
        % (m, b[0], b[1], 4 * m, 4 * m + 2, banked[m],
           "AGREE" if ok else "*** DISAGREE ***"))
say("  %d/%d rows reproduced" % (agree, len(banked)))
say()

say("=== 2. THE TILING: apolar's band + my rigid band vs the w* window ===")
say("   w* window = [4m+2, 8m-2]  (apolar's proved joint-support window)")
say("   m    window        apolar [4m+2..a_max]   mine [thr..8m-2]     GAP")
gapsizes = {}
for m in list(range(1, 21)) + [24, 30, 32, 36, 39, 40]:
    lo, hi = 4 * m + 2, 8 * m - 2
    if hi < lo:
        say("  %3d   EMPTY WINDOW" % m)
        continue
    b = apolar_band(m)
    amax = min(b[1], hi) if b else lo - 1
    thr = max(rigid_threshold(m), lo)
    gap = [a for a in range(lo, hi + 1) if a > amax and a < thr]
    gapsizes[m] = len(gap)
    say("  %3d  [%d..%d]  [%d..%d]%s  [%d..%d]%s   %s"
        % (m, lo, hi, lo, amax, "" if amax >= lo else " (EMPTY)",
           thr, hi, "" if thr <= hi else " (EMPTY)",
           gap if gap else "NONE"))
say("  gap sizes over m in [1,20]: %s"
    % sorted({g for k, g in gapsizes.items() if k <= 20}))
say("  m mod 3 -> gap size: %s"
    % sorted({(k % 3, g) for k, g in gapsizes.items() if k > 1}))
say()

say("=== 3. asymptotic share of the w* window ===")
for j in (10, 20, 30, 37):
    m = 2 ** j
    lo, hi = 4 * m + 2, 8 * m - 2
    b = apolar_band(m)
    amax = min(b[1], hi)
    thr = max(rigid_threshold(m), lo)
    tot = hi - lo + 1
    ap = amax - lo + 1
    mine = hi - thr + 1
    gap = tot - ap - mine
    say("  m=2^%-3d window=%-14d apolar=%-14d (%.4f)  mine=%-14d (%.4f)"
        "  GAP=%d" % (j, tot, ap, ap / tot, mine, mine / tot, gap))
say()

say("=== 4. D4 THE PAYOFF MAP, re-derived (not cited) ===")
m = 2 ** 37
rho, N, R = 4 * m - 1, 16 * m, 8 * m
say("  m = 2^37 => N = 16m = %d = 2^%d = n ; rho = 4m-1 = 2^39-1 ;"
    % (N, N.bit_length() - 1))
say("  rho+1 = %d = 2^39 (budget 1) ; rho+2 = %d = 2^39+1 (budget 2)"
    % (rho + 1, rho + 2))
say("  R = 8m = 2^40 ; A = R+1-2rho = %d ; e = m ; SAT3 failure size "
    "= rho+2, deficit exactly 1 slope" % (R + 1 - 2 * rho))
say()
B128 = 2 ** 128
say("  B*(q) = floor(q / 2^128).  A budget b is met on the rows where"
    " B* >= b, i.e. q >= 2^128 * b.")
for b, name in ((2 ** 39, "rho+1 = 2^39"), (2 ** 39 + 1, "rho+2 = 2^39+1")):
    q0 = B128 * b
    say("    budget %-14s : q >= 2^128*%d = %d = 2^167%s"
        % (name, b, q0, "" if b == 2 ** 39 else " + 2^128"))
say("  bracket top before  : q >= 2^169 = 2^128 * n = 2^128 * 2^41 = %d"
    % (B128 * 2 ** 41))
say("  bracket top after closing 2^39+1 : q >= 2^167 + 2^128 = %d"
    % (B128 * (2 ** 39 + 1)))
num, den = 2 ** 169, B128 * (2 ** 39 + 1)
say("  extension factor 2^169/(2^167+2^128) = 2^41/(2^39+1) = %.6f"
    % (num / den))
say("      exact: 4 - 4/(2^39+1) = 4 - %.6e   -> '4.000000' to 6 dp,"
    " NOT exactly 4" % (4 / (2 ** 39 + 1)))
say("  the SLIVER (2^167, 2^167+2^128): floor(q/2^128) there = %d = 2^39"
    % ((2 ** 167 + 1) // B128))
say("      so budget 2^39 alone owns the sliver; 'all q > 2^167' needs"
    " the PAIR.  Sliver relative width = 2^128/2^167 = 2^-39.")
say("  low end: rho <= R - r = 2^34 (the quotient-floor cap).")
say()

say("=== 5. what T4 closes, and what it does NOT (honest ledger) ===")
say("  T4 (this pilot): for RIG >= 0, every collinear family of the")
say("  reciprocal-locator set is a PENCIL; sporadic (non-pencil)")
say("  collinearities are IMPOSSIBLE, not merely rare; and the counting")
say("  layer d_x <= e caps every pencil family at M <= e+1 = m+1.")
say("  Hence, on that band, #(weight-extremal type-2 slopes) <= m+1 and")
say("  T_1 <= e+1 = m+1, so T <= 2m+2 <= 4m = rho+1 for every m >= 1.")
for m in (1, 2, 3, 2 ** 37):
    say("     m=%-14d : 2m+2 = %-16d vs rho+1 = %-16d  %s"
        % (m, 2 * m + 2, 4 * m, "OK" if 2 * m + 2 <= 4 * m else "FAILS"))
say("  NOT closed by T4: (i) the gap values of w*; (ii) type-2 slopes")
say("  whose difference codeword is NOT of minimum weight R+1 (the")
say("  reciprocal-locator normal form does not apply to them); (iii) m=1.")
say("  Counting-layer arithmetic for the residual (ii), re-derived:")
for m in (2, 8, 2 ** 37):
    for a in (4 * m + 2, 6 * m, 8 * m - 2):
        s = 8 * m + 1 - a
        if s <= 0:
            continue
        say("     m=%-12d a=%-14d s=R+1-a=%-14d  counting cap "
            "(N-a)e/s = %-18d  target rho+1 = %d"
            % (m, a, s, (16 * m - a) * m // s, 4 * m))
say()
say("=== END d3_coverage ===")
