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

## Round-22 forced corrections (2026-08-07, coordinator-applied on replay: CATCH-RL1 + CATCH-RL2 of f2_rlocality; 47/0 verifier suite)

**CATCH-RL1 — the 8.60 is attached to the wrong layer.** The
constant log2 p / log2(e log2 p) = 8.5990 (lines 82-84) is correct
arithmetic, but it is the instrument deficit AT LAYER c = 1
(DEF_INSTR(1)), where in fact R-locality costs NOTHING (proved by
exact LP: OPT_k(1) = p^{-k} exactly, measured 17^{-2}, 17^{-3};
tail_count THEOREM 12 already proves the c = 1 layer purely
R-locally with the knife-edge constant as the entire margin). The
BINDING-LAYER deficit is DEF_INSTR(c*) = 6.3130 (the quoted
sentence's own two numbers 0.443/0.116 = 3.8068 mix the two layers:
0.116 = I_INSTR(1), while the requirement 0.443 is at c*; the true
I_INSTR(c*) = 0.070124). Four-factor decomposition at c*:
THETA 1.0000 (zero margin) x AMGM 2.2990 x GAUSS 1.0348 x
LOCALITY-CAP 2.6536 = 6.3130 — at the binding layer the lossiest
single step is the locality cap, and at c = 1 the dominant loss in
the 8.60 was Chebyshev-at-an-endpoint (GAUSS = 44.36), not
locality. Numbers of record: 6.3130 (binding layer), floors below.

**CATCH-RL2 — the position-entropy diagnosis is an artifact.** The
clause "interpolation: no p at all, position entropy H(1/L) > 1/L"
(lines 81-82; tail_count THEOREM 10) rests on the union bound
|U_c| <= C(S,R) m^R, which is not the right R-local instrument:
the exact binomial moment Pr[N_A >= m] <= E[C(N_A,R)]/C(m,R) =
C(S,R) rho^R / C(m,R) CANCELS the position entropy, turning the
exponent positive (-0.0947 -> +0.0017 at c*) with a threshold at
every log2 p >= 3.06. The route still dies NUMERICALLY (deficit
258.9) — the ledger is unchanged; the DIAGNOSIS changes: the wall
is locality, not position entropy. "Dies at every p / no threshold
in p" is withdrawn as a diagnosis.

**THE CONCLUSION SURVIVES AND IS NOW A FLOOR.** The deficit is
STRUCTURAL for the formalized class (k-LOCAL: valid against every
k-wise-uniform law): exact toy floor FLOOR_R(c*) = 1.5889 at G1
(full 12870-state LP; second row p = 41: 2.7651); lifted
official-row floors (asymptotic evidence) FLOOR_R = 6.2063,
FLOOR_2R = 3.4848. The banked instrument (6.3130) sits +1.7% above
the k = R floor — essentially OPTIMAL for what R-wise independence
allows; the at-most-1.81x remaining headroom requires turning
Z-2's 2R-order l1-restricted information into a genuine 2R-wise
tail bound, and the licensed-radius analysis shows that attempt
collapses back onto V_1. The k <= R moment cap is SHARP (N_{R+1}
fails on all three toy rows, banked G2 value reproduced).

**MYSTERY 2'S REQUIRED INPUT, named:** a NON-LOCAL statement — "no
codeword of the GRS value code C* is unusually smooth" (a
box/smoothness count at exponential scale, quantifying over
Theta(S) coordinates at once). Nearest banked object: the
constant-weight Z-FLOOR cell on the crossing side (the same
constant-weight population shape as the round-22 crossing crux —
a FOURTH lane convergence). Sharpening: under the finite target
Z(L) <= 1 + N^3 the window is 4.77 bits absolute, so the non-local
input must be essentially EXACT, not merely 2^{o(S)}.
Source: notes/pilots_20260807/f2_rlocality/ (PROOFS.md THEOREMS
RL-1..RL-5; four verifier logs, coordinator-replayed).
