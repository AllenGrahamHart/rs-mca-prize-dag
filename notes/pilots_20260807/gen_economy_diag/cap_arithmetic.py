#!/usr/bin/env python3
"""MYSTERY-5 diagnosis, round 21: the quantitative ledger.

Named functionals (PREREG R4, R5, R6):
  GAP(N')      = log2(required centers) - log2(achieved certified centers)
  SEMICOUNT    = log2 |U| * C(g+d-1, d)   -- the general-base counting cap
  TAU          = c * log2 p / M           -- the round-19 criticality coordinate
  NORMTHRESH   = the log2 p at which the AM-GM norm ceiling becomes non-vacuous
  MITM(w)      = log2 C(N', w/2) + w/2    -- per-row certification cost
Everything printed here is arithmetic on constants quoted with file:line in the
report; nothing is fitted.
"""
import math


def lg(x):
    return math.log2(x)


def line(t):
    print("\n== %s ==" % t)


def main():
    # ---------------------------------------------------------- the contract
    line("D1  THE CONSUMER CONTRACT (arithmetic)")
    # cluster_certificates/statement.md:9  -> free clique ~2^33 at N'=128
    # census_window_arithmetic/statement.md:9 -> B* = floor(q/2^128)
    # pro_brief_gap128.md:5 -> B* = 2^122, required B*/2^33 = 2^89
    Bstar_bits = 122.0
    clique_bits = 33.0
    need_bits = Bstar_bits - clique_bits
    q_bits = Bstar_bits + 128.0
    print("  B* = 2^%.0f   free clique = 2^%.0f   required centers = 2^%.0f"
          % (Bstar_bits, clique_bits, need_bits))
    print("  row size q = B* * 2^128 = 2^%.0f  (matches p ~ 2^250)" % q_bits)
    print("  identity: B*/2^33 = q/2^161 -> required = 2^(%.0f-161) = 2^%.0f"
          % (q_bits, q_bits - 161))
    print("  DECIDED-WINDOW map: a certified family of size 2^m decides every")
    print("  prize row with q < 2^(m+161); the rest of [2^(m+161), 2^256) stays open.")

    # ------------------------------------------------ what is actually achieved
    line("D2  THE EARLY CAP MADE QUANTITATIVE")
    Np = 128
    subsets_bits = lg(Np) + lg(math.comb(Np // 2 - 2, Np // 4 - 1))
    print("  Pro-Brief-F |F| (SUBSET count)      = 2^%.3f   [pro_construction.md:5]"
          % subsets_bits)
    print("  Pro-Brief-F distinct e_1 centers    = N' = 2^%.4f   [measured R1]"
          % lg(Np))
    print("  claimed deficit  (subset count)     = %.1f bits  [pro_brief_gap128.md:4]"
          % (need_bits - subsets_bits))
    print("  TRUE deficit     (center count)     = %.2f bits" % (need_bits - lg(Np)))
    print("  overstatement of the banked family  = %.2f bits" % subsets_bits_gap(Np))
    for N2 in (256,):
        sb = lg(N2) + lg(math.comb(N2 // 2 - 2, N2 // 4 - 1))
        print("  at N'=%d: |F| = 2^%.3f subsets but 2^%.4f centers "
              "(the '+41 bits PASSES' claim inherits the same error)"
              % (N2, sb, lg(N2)))
    # cyclotomic-class ceiling measured in toy_cap.py: MAXPOW2(N) = N+1
    print("  MAXPOW2 measured: N=8 -> 9, N=16 -> 17  (= N+1, exhaustive)")
    print("  cyclotomic-class ceiling at N'=128 (extrapolated) = 129 = 2^%.4f"
          % lg(129))
    print("  => GAP(128) = %.2f bits against the required 2^%.0f"
          % (need_bits - lg(129), need_bits))
    print("  => decided window from the cyclotomic class: q < 2^%.2f "
          "(prize rows sit at 2^250)" % (lg(129) + 161))

    # ------------------------------- is the cap structural for GENERAL bases?
    line("D2b SEMIGROUP-COUNT: general poly(N') bases (the registered R4 bar)")
    # height budget: a difference of two e_1's has L1 height <= 2*N'... its norm
    # is at most (L2^2)^{h/2} with h = N'/2 (AM-GM); every non-unit base has
    # |Norm| >= 2, so the multiplicative degree d obeys 2^d <= |Norm|.
    h = Np // 2
    l2sq = 4 * h                     # ternary-folded coeffs in {-2..2}, length h
    dmax = (h / 2.0) * lg(l2sq)
    print("  folded length h = %d, ||v||_2^2 <= %d -> |Norm| <= 2^%.2f"
          % (h, l2sq, dmax))
    print("  every non-unit base has |Norm| >= 2, so multiplicative degree d <= %d"
          % int(dmax))
    for g in (Np + 1, Np ** 2, Np ** 3):
        d = int(dmax)
        bits = lg(math.comb(g + d - 1, d))
        print("  g = %-8d  d <= %d  ->  log2 |semigroup| <= %.1f bits   %s"
              % (g, d, bits, "EXCEEDS 2^89" if bits > need_bits else "below 2^89"))
    print("  VERDICT: the counting bound is VACUOUS for general poly(N') bases")
    print("  (thousands of bits of head-room). The cap is NOT structural from")
    print("  counting alone; it is structural for the CYCLOTOMIC base class.")

    # ----------------------------------------------------- the ternary bridge
    line("D3  TERNARY BRIDGE: the criticality coordinate")
    # Adversary convention (tern_unification_adversary/PROOFS.md:181-190):
    #   tau := c * log2 p / M   on the NATIVE cube of M coordinates.
    # generator_economy's collision cube is the UNFOLDED ternary
    #   v in {-1,0,1}^{N'},  sum_x v_x zeta^x = 0 mod p   [kernel_lattice_reframing]
    # so M = N' = 128 and c = g = |<p>Lambda| = 1 (p = 1 mod N' => delta = 1).
    M = Np
    c = 1
    for p_bits in (250.0, 255.4558, 256.0):
        tau = c * p_bits / M
        Tcrit = M * lg(3) - c * p_bits
        print("  log2 p = %8.4f  ->  TAU = %.4f   Tcrit = %+.2f bits  (%s)"
              % (p_bits, tau, Tcrit,
                 "subcritical" if tau > lg(3) else "supercritical"))
    print("  ANTI-NUMEROLOGY: the node banks '~2^-50 expected hits at N'=128'")
    print("  [kernel_lattice_reframing/statement.md:9]; the coordinate returns")
    print("  Tcrit = %+.2f at the row of record -- reproduced, not fitted."
          % (M * lg(3) - 250.0))
    print("  banked comparanda: I1 tau = 1 (SUPERcritical, mass target);")
    print("                     I2/I3 tau = 2 (subcritical, emptiness target).")
    print("  generator_economy sits at tau = %.4f -- the SAME criticality cell"
          % (250.0 / M))
    print("  as I2/I3: subcritical, emptiness is the meaningful target.")
    print("  Z-FLOOR (informative iff tau < 1) is therefore VACUOUS here.")
    print("  FOLDED cross-check: distinct differences live in {-2..2}^%d, so the"
          % h)
    print("  distinct-difference first moment is 5^%d/p = 2^%+.2f (the node's"
          % (h, h * lg(5) - 250.0))
    print("  -50 is the unfolded PAIR count; both say the same thing).")

    line("D3b THE NORM INSTRUMENT'S NON-VACUITY THRESHOLD")
    # AM-GM ceiling: |Norm(v)| <= (||v||_2^2)^{h/2}; p | Norm(v) is impossible
    # once p exceeds that ceiling.
    my_thresh = (h / 2.0) * lg(l2sq)
    banked = 32 * lg(253)
    print("  my re-derivation:  |Norm| <= (%d)^(%d/2) = 2^%.4f" % (l2sq, h, my_thresh))
    print("  banked constant:   253^32 = 2^%.4f  "
          "[integer_code_distance_high_field_folded_box_exclusion]" % banked)
    print("  agreement to %.2f bits -> the banked exclusion IS this instrument."
          % abs(my_thresh - banked))
    print("  non-vacuous iff log2 p > %.4f, i.e. TAU > %.4f"
          % (banked, banked / Np))
    print("  prize row: log2 p = 250 -> TAU = %.4f" % (250.0 / Np))
    print("  SHORTFALL: %.4f bits of log2 p  =  %.4f in TAU"
          % (banked - 250.0, banked / Np - 250.0 / Np))
    print("  i.e. the CRITICALITY-COMPATIBILITY gate is passed in SIDE but the")
    print("  norm instrument's non-vacuous tau-interval starts %.4f above the row."
          % (banked / Np - 250.0 / Np))

    # --------------------------------------------------------------- pricing
    line("D4  LATTICE-CONE / MITM PRICING")
    print("  cost model MITM(w) = log2 C(N', w/2) + w/2   [weight_graded_mitm:9]")
    for w in (12, 14, 16, 20, 24, 30, 40, 64, 128):
        if w // 2 > Np:
            continue
        bits = lg(math.comb(Np, w // 2)) + w / 2.0
        core_h = 2 ** (bits - 30) / 3600.0            # ~2^30 ops/core-second
        tag = ""
        if w in (12, 14, 16):
            tag = {12: " (banked 2^38.3)", 14: " (banked 2^43.5)",
                   16: " (banked 2^48.4)"}[w]
        print("  w = %-4d MITM = 2^%-7.2f ~ %-12s core-hours%s"
              % (w, bits, ("%.3g" % core_h), tag))
    print("  registered Modal-scale bar: <= 1e4 core-hours AND <= 1.5 GB/row.")
    print("  full radius needs w = 2l' = %d -> 2^%.1f: infeasible by ~%d orders."
          % (Np, lg(math.comb(Np, 64)) + 64,
             int((lg(math.comb(Np, 64)) + 64 - 48.4) / 3.32)))
    print("  MEMORY is the binding constraint, not time: a plain MITM table at")
    print("  w=16 holds 2^48.4 entries, ~2^18 x over the 1.5 GB ceiling.")


def subsets_bits_gap(Np):
    return lg(math.comb(Np // 2 - 2, Np // 4 - 1))


if __name__ == "__main__":
    main()
