# Floor-campaign survey: petal_growth, xr_smallcore_spread_count, rate_half_band_closure, worst_word_challenger_pricing
# (Explore agent, 2026-07-07; verbatim quotes from node folders + dag.json; consumer edges all confirmed kind=req)

## NODE — petal_growth -> imgfib
STATEMENT: "Full-petal extras at cofactor excess d-ell = c are poly(n) uniformly in c (equivalently: the
amplification bound closes the Thm 21/B11 escape route)." FALSIFIER (dag): "fixed-excess counts growing
super-poly in n at some c". statement.md falsifier richer: "below-top Lemma-13 failures, exact realizable
full-petal counts growing outside paid/top-band families, or an uncharged top-band family whose count cannot
be bounded by a polynomial with exponent independent of c". Status TARGET (demoted 2026-07-05,
RETRACTION_MANIFEST). Best-known structure: threat CONFINED to top-defect band d >= M(t-2) (verified);
off-band has induction route via top-coefficient forcing; the band needs a parameterized paid family.
CONSUMPTION (imgfib): "For ALL received words U: #ImgFib_U(k+sigma) <= n^B once sigma log2(q_D) >=
(1+eps) log2 C(n, k+sigma) and the quotient profile is budgeted." petal_growth enters as "close the petal
escape route (the only open branch of the Thm 21/B11 frontier); monomial instance already proved in
quasi-poly range". imgfib has NO reduction packet; notes/ empty.
MACHINERY: experiments/amber_stress/petal_excess_local_scan.py (16 coset-chart configs / 76 rows, no
below-top Lemma-13 violations, max exact count below top = 1, at/beyond top = 5005). petal_growth/notes/ empty.
QUANTIFIERS: universal in c; imgfib universal over words U. Exceptional structure: top-defect band split.

## NODE — xr_smallcore_spread_count -> xr_clean_residual_any_gate
STATEMENT (dag, LIVE — statement.md is stale poly(n) version): "For every pair (u,v): the number of aligned
aperiodic supports whose agreement sets pairwise share cores < k+t-1 (the post-cascade remainder, a spread
family in the face-3 sense) is bounded in the budget-compatible form needed by the consumer:
R_spread(u,v; A) <= 16 n^3 after the quotient, tangent, dihedral, and extension columns are stripped or
counted inside R_post." FALSIFIER: "a toy pair with super-poly many pairwise-small-core aligned supports
(searchable with E27's pencil machinery)". Status label CONDITIONAL but the routed predicates were CUT
(RETRACTION 2026-07-05: 30 nodes incl. xr_fresh_codim_dichotomy, xr_partial_tangent_band).
CONSUMPTION (xr_clean_residual_any_gate): "The proved xr_target_budget_audit reduces the clean-rate
obligation to the exact per-pair inequality R_post(u, v; A) <= 16 n^3 after the quotient and tangent strips,
with the dihedral and extension columns counted inside R_post." statement.md: "any polynomial up to ~n^3
fits inside the 2^122-2^127.9 allowance"; "Sufficiency is exact integer arithmetic at all six candidates."
MACHINERY: SOV_STABILITY_THEOREM_ADVISORY.md (Pro's Freiman-type stability: |V_h([1,m])| = h(m-h)+1;
Bajnok-Edwards C_h(Z_p) = floor((p-2)/h)+h). notes/ empty. E27 pencil machinery external.
QUANTIFIERS: for every pair (u,v); consumer sufficiency = exact integer arithmetic at all six candidates.
E27 toy data: remainder "exactly in the FM band... all classification tests at chance"; "no fifth mechanism".

## NODE — rate_half_band_closure -> adjacency_closing + list_adjacency_closing + mca_safe
STATEMENT: "Cover the 2,978,147-radius band at prize-max rate 1/2 (M_max = 2^33 vs sigma* = 8,592,912,738)
by a new mechanism (quotient windows and integrality both fall short) — or the rate-1/2 determination lands
bracket-grade there. Rates 1/4, 1/8, 1/16 need nothing (clean by margins < -121)." Band verbatim:
"2^33 < sigma <= 8,592,912,738". dag: "A bracket-grade obstruction for some band radius would be a
creditable partial result, but it does not satisfy this node as consumed by adjacency_closing,
list_adjacency_closing, or mca_safe." FALSIFIER: "a band radius provably uncoverable by any priced
mechanism". Routes AQB + dihedral/Chebyshev sibling both REFUTED. ATTACK queue: averaged conversion at
giant M; B2b-style balance; safe-side push through sigma*; q-threshold refinement.
CONSUMPTION (all three consume IDENTICALLY): the single premise covering the rate-1/2 residual band/top
slice so the "for each admissible row/C" universal has no exception. adjacency_closing: "if that strong
rate-half premise holds, the for-each-admissible-row quantifier has no remaining exception."
mca_safe: "The rate-1/2 safe-side top slice is... included only through the strong rate_half_band_closure
premise."
MACHINERY: notes/floor_depth.md — Modal verdict: max quotient-remainder floor depth = 2^33 EXACTLY on
plateau c = 2^22..2^33; "the band IS the floor's shadow". notes/pro_brief_razor.md — THE RAZOR: floor
covers sigma* for ALL log2 q <= 255.900; the band survives ONLY for q in the top 0.100 bits
(q in (2^255.9, 2^256)). notes/verify_floor_depth_modal.py + verify_q_threshold_modal.py (Modal apps).
P6_RATEHALF_SIBLING.md (Pro window; why AQB died: B_I(256) = 429,645,546.77; Q_crit = 255.90000002).
QUANTIFIERS: consumers need for-each-admissible-row at rate 1/2; band only exists for log2 q > 255.9;
rates 1/4, 1/8, 1/16 clean by < -121 margins.

## NODE — worst_word_challenger_pricing -> worst_word_planted + list_planted_arithmetic
STATEMENT: "Price or exhaust the structured low-slack NON-planted challenger class (the E15 counterexample's
family) so the revised worst_word_planted statement's sup-over-words claim is carried by planted + challenger
classes jointly." dag adds: "For downstream list arithmetic, a weaker rowwise deliverable is also sufficient:
a certified upper envelope for all non-planted low-slack contributions, together with explicit lower
witnesses where the unsafe side is invoked." RESOLVED 2026-07-06: EXHAUSTION half PROVED (Lemma A: bg <= 1
max-fill cells admit NO third class at any sigma >= 1, any q); PRICING half has verified law: challengers
are codim-sigma coincidences, count ~ K_cell/q^sigma. REMAINING KERNEL: "the per-official-row certified
envelope (count law at prize rows — certification-shaped, the accepted crux-2 pattern) + the K_cell
upper-bound lemma." FALSIFIER: "a third challenger class outside both".
CONSUMPTION: worst_word_planted (CONJECTURE status): "at the crossing radii the sup-over-words list is
attained by the planted sunflower family OR the E15 structured challenger class, and list_planted_arithmetic
must price BOTH classes exactly" — consumes exhaustion + priced challenger column. list_planted_arithmetic
(weakened 2026-07-06): "downstream use does not require a global claim that only the planted and
E15-successor families exist. It is enough to have, row by row, a certified upper envelope for every
non-extremal/non-planted contribution and explicit lower witnesses for unsafe rows."
MACHINERY: LEMMA_A_EXHAUSTION_PROOF.md (bg<=1 exhaustion + window law verified: E[#challengers] ~
K_cell/q^sigma; sigma=2 window opens q=17 closes by q=97). notes/e22_census_modal.py (pre-registered census
sigma=1..3, n=16..64), e22_core.py (E15 #197 byte-identical, md5 b3561a...), e22_gate_local.py. External:
e22_extended_local_census.py (77 cells, 1,920,836 subsets, UNCLASSIFIED=0), e22_random_layout_census.py
(219 cells, 1,427,408 subsets, UNCLASSIFIED=0).
QUANTIFIERS: sup-over-words (planted) / per-official-row + m-quantifier (list, weakened to rowwise).
Lemma A scope: bg <= 1 (official max-fill convention — "bg <= 1 always" for official cells).
