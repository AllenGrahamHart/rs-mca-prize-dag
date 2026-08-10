"""D4: re-derive the payoff chain from primary text (NOT from round-27).

Primary sources actually read:
  background/nodes/rate_half_half_distance_safe_bracket/statement.md  (HD1,HD2)
  background/nodes/rate_half_ca_hankel_exceptional_root_charge         (ERC2,ERC4)
  background/nodes/rate_half_ca_hankel_minimal_index_budget            (MI1,MI2)
  critical/nodes/rate_half_band_crossing_location/statement.md
  critical/nodes/rate_half_band_closure/statement.md  (line 164 residual)

Stdlib only.  Run under tools/ramguard.
"""


def say(s=""):
    print(str(s), flush=True)


n = 2 ** 41
k = 2 ** 40
R = n - k                      # = 2^40
say("official row: n = 2^41 = %d, k = 2^40 = %d, R = n-k = 2^40 = %d" % (n, k, R))
say("B*(q) = floor(q / 2^128).")
say()

say("=== 1. where the residual sits on the q-axis ===")
say("  wave-10 staircase proves the crossing for B* <= 2^39-1, i.e.")
say("    q < 2^128 * 2^39 = 2^167 = %d" % (2 ** 167))
say("  the two residual budgets are B* = 2^39 and B* = 2^39+1, i.e.")
say("    q in [2^128*2^39, 2^128*(2^39+2)) = [2^167, 2^167 + 2^129)")
say("    width = 2^129 = %d  (relative width 2^129/2^167 = 2^-38)" % (2 ** 129))
say()

say("=== 2. the two budgets, as radii ===")
for B in [2 ** 39, 2 ** 39 + 1]:
    r = B - 1
    say("  budget B* = %d : r = B*-1 = %d ; R-r = %d ; r+1 = %d ; r vs R/2 : %s"
        % (B, r, R - r, r + 1, "r = R/2-1" if r == R // 2 - 1 else
           ("r = R/2" if r == R // 2 else "?")))
say("  strict budget 2^39 -> r = R/2 - 1 (A = 3 possible)")
say("  half-distance budget 2^39+1 -> r = R/2 (A = 1 or 3)")
say()

say("=== 3. (ERC4) at the strict A=3 profile — the exact one-slope deficit ===")
m = 2 ** 37
rho = 4 * m - 1
say("  m = 2^37 = %d, rho = 4m-1 = 2^39-1 = %d, N = 16m = 2^41 = %d"
    % (m, rho, 16 * m))
say("  (ERC4): T <= 4e+1.  First live degree e = m = 2^37:")
cap = 4 * m + 1
say("    cap  = 4m+1 = %d" % cap)
say("    target rho+1 = %d" % (rho + 1))
say("    DEFICIT = cap - target = %d  (exactly one slope)" % (cap - rho - 1))
say()

say("=== 4. bracket ENDS: the far-CA caps, re-derived ===")
a_lo = k + 2 ** 34
r_lo = n - a_lo
say("  lower end a = k + 2^34 = %d ; r = n-a = %d ; R-r = %d" % (a_lo, r_lo, R - r_lo))
say("    generic Hankel rank rho <= min(R-r, r+1) = %d = 2^34" % min(R - r_lo, r_lo + 1))
say("    fixed-kernel / rank branch gives T <= rho <= 2^34 = %d" % (2 ** 34))
a_hi = 3 * n // 4
r_hi = n - a_hi
say("  upper end a = 3n/4 = %d ; r = n-a = %d = R/2 ; R-r = %d ; r+1 = %d"
    % (a_hi, r_hi, R - r_hi, r_hi + 1))
say("    (HD1) as PROVED gives B_mca(3n/4) <= n = %d" % n)
say("    the far-CA TARGET at this row is T <= r+1 = %d = 2^39+1" % (r_hi + 1))
say()

say("=== 5. the bracket-top field condition, exactly ===")
say("  (HD2) needs B*(q) >= cap(3n/4).")
say("  with cap = n = 2^41 : q >= 2^128 * 2^41 = 2^169 = %d" % (2 ** 169))
say("      -> reproduces the PROVED hypothesis q >= 2^169 EXACTLY.")
newcap = r_hi + 1
qmin = 2 ** 128 * newcap
say("  with cap = r+1 = 2^39+1 (i.e. budget 2^39+1 CLOSED) :")
say("      q >= 2^128 * (2^39+1) = 2^167 + 2^128 = %d" % qmin)
say("      = 2^167 * (1 + 2^-39).")
say("  EXTENSION FACTOR = 2^169 / (2^167+2^128) = %.6f  (= %.4f bits)"
    % (2 ** 169 / qmin, (169 * 1.0) - (qmin.bit_length() - 1)))
say("  PRECISION NOTE: the payoff is 'all q >= 2^167 + 2^128', NOT literally")
say("  'all q > 2^167'; the uncovered sliver (2^167, 2^167+2^128) has")
say("  B* = 2^39 exactly, where the needed cap 2^39+1 still exceeds B*.")
say("  Relative size of the sliver: 2^128 / 2^167 = 2^-39.")
say()

say("=== 6. the crossing-formula payoff ===")
say("  closing BOTH budgets makes a_RH = n - B*(q) + 1 exact for every")
say("  B* <= 2^39+1, i.e. every q < 2^167 + 2^129 = %d" % (2 ** 167 + 2 ** 129))
say("  the currently-proved reach is q < 2^167 = %d" % (2 ** 167))
say("  gain on the q-axis: a factor 1 + 2^-38 (relative 2^-38), i.e. the")
say("  whole residual-budget interval [2^167, 2^167+2^129).")
say("  NOTE the two payoffs are DIFFERENT and the bracket-top one is bigger:")
say("    crossing formula gain : relative 2^-38")
say("    bracket-top gain      : 2^169 -> 2^167+2^128, a ~2-bit window")
say()
say("=== END part 4 ===")
