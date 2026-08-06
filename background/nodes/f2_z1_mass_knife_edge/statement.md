# f2_z1_mass_knife_edge

- **status:** PROVED (the instruments; the open mass bound is a
  stated residual, NOT a claim)
- **minted:** 2026-08-06 (mint-4, round 18), coordinator-audited.
- **provenance:** notes/pilots_20260806/z1_ternary_mass/ (81/81) +
  notes/pilots_20260806/o1_generating_adversary/ (the blind-
  convergent D1), coordinator-replayed.

## Statement

THE F2 TERMINAL OF RECORD (SL-1b' pinned to the MASS form) AND ITS
PROVED CONSTRAINTS, on the admissible object (the [S, S-R, R+1]_p
negacyclic GRS code on the half-system of mu_{2^{e_p}},
S = 2^40/e, R/S = 1/log2 p, p >= 2^39; Z(L) = Z_1^C, C <= 4).

**THEOREM Z-FLOOR (pointwise first-moment floor).** For EVERY
F_p-subspace, Z(L) = sum_{eps in L^perp cap T} 2^{-wt(eps)} >=
2^m / p^{dim L}. One Cauchy-Schwarz from the banked collision
identity sum_s |F_s|^2 = 2^m Z(L)
(dli_c1_l1_block_owner_ledger:15,18) — the identity was banked, the
inequality never drawn. Tight within a factor 2 of the ensemble
mean (no subspace beats random by more than 2x). 696 configurations,
exact rationals, 0 violations.

**THEOREM Z-1 (the DLI transport; = the adversary's THEOREM D1,
blind convergence).** dli_wcl_newton_short_window_exclusion's
hypothesis char > w HOLDS on every admissible row (p > m always, by
the e_p case split — the tower verdict is REVERSED by the field
cap), so the min ternary weight is >= 2R+1 = 8,589,934,681, double
SL-1's characteristic-free R+1. SCOPE: shift-0 windows only — 43
shifted counterexamples exist; the transport is legitimate because
the official window starts at l = 1.

**THEOREM Z-2 (gift back to DLI).** The Newton short-window
exclusion holds for ALL integer coefficients with w read as the l1
weight — the {+1,-1} restriction is unnecessary. Licenses l1
sphere-packing between ternary codewords.

**THEOREM Z-NOGO.** Saturation pins R/S = 1/log2 p, so the entire
distance+counting family (M3 and all sharpenings: 39.2x -> 28.3x
with Z-1 -> 21.3x with l1 packing) discharges only if p <= 8 —
against an admissible floor of log2 p >= 39. NO bound in that
family can ever close the terminal.

**THE KNIFE EDGE.** At k = e the Z-FLOOR is silent by 46.02 bits
out of 2.75e11 under the banked R = ceil(t/2) reading — ONE Lambda
condition, worth log2 p = 64 bits — and FIRES at +17.98 bits under
the exact-balance reading (in which case ternary kernel vectors
provably exist at the witness row: Z_1 >= 2^{17.98}, the EXACT-ZERO
form of the terminal is dead, yet Z = 2^{o(n)} so the MASS form
survives). The two defensible t-readings straddle zero; the reading
belongs to the t-naming/ensemble maintainer stack.

**THE OPEN TERMINAL (residual, not claimed):** prove
Z_1 <= 2^{o(m)} at k = e. ROUTE (b) SIZING REFUTED (round-19
tern_route_b, forced correction 2026-08-06): the "factor-2 headroom"
dropped the degree factor — restored, Weil is VACUOUS by exactly
26.000 bits (deg·sqrt p = 2^65 vs |H| = 2^39), and the executable
substitute (AM-GM + Z-2 moments, THEOREM 7: Z_1 <= 2^{0.8908·S}
unconditional) closes only at p <= 8.30 — Z-NOGO's own threshold.
NO NAMED ROUTE REMAINS. What survives of (b): the exact 1+cos
character form (the object is a sum of p^R NON-NEGATIVE terms — no
cancellation exists in principle; the true criterion is the
TAIL-COUNT |{u : P(u) >= 2^{cS}}| <= 2^{(1-c)S+46+o(S)} for all c);
two favourable reductions (oddness => COMPLETE subgroup sums, no
partial-sum loss; AM-GM => first moment in V_1 only, no L2->Linf
loss). THE PROP-10 LEAD IS RETIRED (round-20 tail_count CATCH-T1,
third forced correction 2026-08-06): the doubling/log-sine
functional TELESCOPES to the elementary cost form log2 P(u) = S -
sum_s d(c_s(u)) — no Dedekind content, nothing to bound. THE OPEN
FORM OF RECORD (normalized): Pr_u[P(u) >= 2^{cS}] <= 2^{-cS+o(S)}
(the +46.02 was exactly the saturation constant Delta; the knife
edge = the c = 1 slack, re-identified from the tail side); the tail
IS a small-values/box count for the MDS value code (structure
theorem); THE BINDING LAYER is c* = 1/ln 2 - 1 = 0.4427, where the
flat model saturates with ZERO margin — no per-coordinate-loss
argument can survive there. Proved: U_c = {0} for
c > 1 - 2^{-124.19} (an endpoint, honestly, not bulk progress).
Both standard supplies killed with computed thresholds (Z-2
moments: p <= 8.30 = Corollary 8; interpolation: no p at all,
position entropy H(1/L) > 1/L); the common cause: every supplied
input is R-LOCAL, short by the factor log2 p / log2(e log2 p) =
8.60; the Fourier escape is circular. The measured genuine tail
obeys the criterion at every reachable row with the binding layer
measured at 0.45 (= c* to grid resolution). Remaining leads: a
non-R-local instrument (nothing named), and the constant-weight
Z-FLOOR cell (crossing-side). Route (a)
(norm sandwich) is DEAD quantified (yields w >= 4.0000 — constant corrected per round-19 CATCH-T3, the sharp ceiling being w^{n/4} — dominated
by 4.3e9); route (c) (class structure) localises but cannot narrow.

**Calibration (honest):** on all valid miniatures (2-power 2N ONLY —
composite 2N carries p-independent cyclotomic ternary relations the
official object structurally cannot have, CATCH-Z6; a standing grid
rule) the deployed code sits at or below the random-ensemble median;
the deficit is exactly the excluded low-weight mass; "better than
random" is NOT established. No toy is evidence about Z_1 at the
official row.

## Falsifier

A subspace violating Z-FLOOR; an admissible row violating Z-1's
transported floor; a distance+counting discharge at p > 8
(contradicting Z-NOGO); an exact-balance-reading row where the floor
fails to fire as computed.

## NOT claimed

Z_1 <= 2^{o(m)} at k = e (THE open terminal); the t-reading; a
shifted 2R+1 law at 2-power 2N (open, thin sample); the route-(b)
sizing as a theorem.
