# csp_findings — PROOF PACKET worker for petal_chart_carrying_descent (SUCCESSOR-A)
# 2026-07-13. Catch ledger continues from #132.

Mission: airtight general-parameter proof packet for the two search-yielded
claims (#132 structure theorem, #128 P3 uniqueness) + the K_2-invariance
composition, with verifier. Deliverables csp_statement.md / csp_proof.md /
csp_verify.py / csp_claim_contract.md, all csp_-prefixed in this scratchpad.

## TURN 1 — reading pass (verbatim sources)

Read: ccd_findings.md (the search ledger, all of it), dag.json nodes
petal_chart_carrying_descent (SUCCESSOR-A statement incl. #128-#132 pins),
petal_g2_support_forcing (stabilizer partition, PROVED), petal_g1_layer_maps,
petal_k4_primitive_bound, petal_small_scale_staircase_census;
critical/nodes/{petal_top_band_tail_collapse, petal_full_touched_set_injection,
petal_retained_zero_effective_degree}/{statement,proof}.md;
background/nodes/cyclic_fiber_interleaving_descent/{statement,proof}.md;
v13 tex def:capf-concrete-sunflower + prop:capf-concrete-sunflower +
def:capf-sunflower-layer + thm:stabilizer-partition (~4474);
ccd_struct_check.py / ccd_stage2.py / ccd_stage3.py / ccd_mutation_control.py;
banked tables ccd_out_n16/n32a/n32b/n32c.txt (in this scratchpad);
PRIZE_RESOLUTION_ROADMAP.md section 5.1 (claim contract form).

## TURN 1 — derivation audit (all sketch steps re-derived by hand, PASS)

All of the search's C1-C4/P1-P3 sketch steps re-derived independently; every
step closes at general parameters (n = 2^s, k even, n | q-1, c_i in F_q^*).
Key checks worth recording:

1. Fiberwise 2x2 Vandermonde [[1,x],[1,-x]] has det -2x != 0 (q odd since
   2 | n | q-1) — the fiberwise agreement bijection is unconditional.
2. P1 degree count: f_0 + x_nf f_1 has deg <= k'-1 and >= k'+1 roots on S'
   — one root of slack, not zero; the argument survives |S'| = k'+1 exactly.
3. The split fiber forces the K_2-invariance <=> g(y_nf) = 0 equivalence:
   x_nf ALWAYS agrees (both sides 0), so an aperiodic lift contributor has
   ODD agreement size 2|S'|+1; scale->=2 <=> -x_nf in S <=> g(y_nf)=0.
4. d' >= 1 automatically for members: z = k' would force g = 0 (deg <= k'-1
   with k' roots), and g = 0 has exactly k' agreements < k'+1 — the d' = 0
   descended chart is EMPTY. Boundary case handled explicitly in the packet.
5. m' = m exactly at M = 2: squaring is exponent-doubling mod n, injective on
   fiber indices 0..n/2-1; petal points never merge and never hit core''.
6. P3's load-bearing inequality is 2a' - m' > deg-bound: with a' = d'+1,
   m' <= d'+2, deg <= d'-1 it reads d' > d'-1 — margin EXACTLY 1.
   The deg <= d'-1 bound comes from deg g <= k'-1 MINUS |W| = z zeros
   (reading A: core'' of size k'), i.e. reading A buys the one degree that
   makes uniqueness true. Generic def:capf-sunflower-layer images (deg <= d')
   would NOT be unique — mutation M3 exhibits two members at deg d'.
7. Normalization pin found (catch #133 candidate, confirmed by algebra):
   "u1 carries the SAME scalars" is true in the concrete-word presentation
   (labels c_i relative to L_{Z'}, i.e. Y' = Z', R0' = {y_nf}); under
   reading A's LAYER bookkeeping (core'' = Z' u {y_nf}) the induced
   def:capf-sunflower-layer auxiliary labels are c_i/(y_i - y_nf), NOT c_i:
   L_{Z'}(y_i)/L_W(y_i) = L_{D0'}(y_i)/(y_i - y_nf) since
   L_{core''} = L_{Z'} (Y - y_nf) = L_W L_{D0'}.
8. Top-band pin translation: per-member exact-assignment band d >= 2(m-2)
   with m = |I| is EQUIVALENT to |S'| <= k'+2 <=> official |S| <= k+4
   (and 2 | |S| forces |S| in {k+2, k+4}: the official odd agreement sizes
   are automatically aperiodic — parity halves the band for this class).

## PLAN

- csp_statement.md: setting + Claim 1 (S1-S6) + Claim 2 (abstract uniqueness
  + instantiation) + Claim 3 (L0 K_2-invariance + composition + residuals).
- csp_proof.md: complete proofs, no evidence-substituted steps at M = 2;
  gaps live only in Claim 3's named residuals (G1) + sigma > 1 scope-out.
- csp_verify.py: independent quotient-side brute (new method direction) vs
  official-side fiber-subset census; pinned banked counts at overlap cells
  ((16,8,97,consec)=3, (16,8,257,wtauy)=1, (32,16,97,geom5)=63,
  (32,12,193,consec)=43, (32,8,97,geom5)=14); NEW cells (32,20,97,*) —
  a row shape the search never touched — and (16,8,577), (32,16,353) new
  primes; mutations M1 (word corrupt), M2 (fake scale->=2), M3 (P3 degree
  slack: two members at deg d').

## TURN 2 — packet written, verifier ALL PASS first run

csp_statement.md (Claims 1/2/3, every hypothesis explicit incl. reading A,
normalization pin, scope-outs), csp_proof.md (complete proofs; the
"where evidence substitutes for argument" section says: NOWHERE at M = 2),
csp_claim_contract.md (roadmap 5.1 form) written.

csp_verify.py executed under `tools/ramguard tiny -- python3` — ALL PASS:

- STAGE A (structure identities S1/S2/S4): 15 cells PASS, including NEW
  cells the search never touched: the (32,20) ROW SHAPE (rate 5/8 — a rate
  class outside all banked evidence), (16,8,p=577), (32,16,p=353).
- STAGE B (dual complete censuses: official fiber-subset vs quotient
  point-subset, matched through the S3/S4 lift bijection; full per-member
  battery incl. the S5 image factorization f = L_{ZnS}·[(Y-y_nf)h](X^2),
  exact-division deg h <= d'-1, d = 2d', r = 1, thresholds, band
  equivalence, full-petal, pattern; P3 pairwise band-chart uniqueness):
  13 cells, 332 members, ZERO violations. All NINE pinned member counts
  match the banked ccd tables exactly ((16,8,97,consec)=3 with the exact
  per-chart table, (16,8,257,wtauy)=1, (16,8,337,consec)=3,
  (32,16,97,geom5)=63, (32,16,193,consec)=56, (32,12,97,geom5)=47,
  (32,12,193,consec)=43, (32,8,97,geom5)=14, (32,8,193,rand1)=7).
  NEW-cell measurements: (32,20,97,geom5) 30 members/28 charts,
  (32,20,97,consec) 42/38, (16,8,577,consec) 3/3, (32,16,353,geom5) 20/19
  — max 1 member per band chart everywhere.
- STAGE C (mutation controls): 4/4 TRIP — M1 corrupted word kills S2;
  M2 coefficient-flipped fake member caught by both the support-semantics
  and the K_2-invariance checks; M3 two distinct DEGREE-d' pseudo-members
  DO occupy one band chart (the reading-A degree bound d'-1 is
  load-bearing; uniqueness margin exactly 1); M4 corrupted pin caught.

## STATUS

- CLAIM 1 (#132 structure theorem): PROVED. General parameters (all
  n = 2^s, s >= 2; all even k in [2, n-2]; all q with n | q-1; all labels
  c_i in F_q^*). sigma > 1: scoped out explicitly. Odd k: scoped out
  explicitly (no hidden gap — nothing claimed).
- CLAIM 2 (#128 P3 uniqueness): PROVED (abstract lemma U0 + instantiation
  U1 + boundary cases U2). Margin exactly 1; sharpness exhibited (M3).
- CLAIM 3: L0 (K_2-invariance of scale-M supports) PROVED, one line,
  self-contained. Composition C PROVED as stated — conditional on exactly
  ONE hypothesis: G1 coverage of the descended top band at the quotient
  row. Residual list (statement R): G1 coverage+budget; band scope
  |S| <= k+4 only; sigma > 1; layout pin; aperiodic bucket not touched.
- Overall packet verdict: PROVED (Claims 1, 2, L0) + PROVED-CONDITIONAL
  (C, single named hypothesis = G1's open content). No PARTIAL gaps at
  M = 2; no step in csp_proof.md rests on search evidence.

## CATCHES #133-#135

- #133 (NORMALIZATION PIN, scalars): "u1 carries the SAME scalars" is true
  in the concrete-WORD presentation (labels c_i against L_{Z'}, i.e.
  Y' = Z', R0' = {y_nf}); under reading A's LAYER bookkeeping
  (core'' = Z' u {y_nf}) the induced def:capf-sunflower-layer auxiliary
  labels are c_i/(y_i - y_nf), NOT c_i (algebra:
  L_{core''} = L_{Z'}(Y - y_nf) = L_W L_{D0'}). A successor consuming
  "same scalars" in the auxiliary-label normalization consumes a false
  premise. Statement + proof both carry the pin.
- #134 (READING A BUYS EXACTLY ONE DEGREE, and P3 spends it): descended
  images satisfy deg(g/L_W) <= d'-1 — one better than the generic
  def:capf-sunflower-layer bound d' — BECAUSE core'' has size k' (reading
  A) and deg g < k' (the code). P3's inequality 2a' - m' > deg closes as
  d' > d'-1: margin exactly 1. At degree d' (generic layer images, or any
  reading-B-style bookkeeping) uniqueness is FALSE: mutation M3
  constructs two distinct deg-d' pseudo-members occupying one band chart
  at (32,16,97). Consumers must not swap the descended concrete charts
  for generic auxiliary layers if they want the per-chart-1 line (the
  m'+1 line survives the swap).
- #135 (PARITY HALVES THE BAND for the periodic class): scale->=2
  contributors have EVEN agreement size, so official top-band sizes are
  exactly |S| in {k+2, k+4}, and the per-member exact-assignment band pin
  d >= 2(m-2) is EQUIVALENT to |S'| <= k'+2 <=> |S| <= k+4. Official
  odd-size agreement sets are automatically aperiodic. Useful pin for the
  census gate's band arithmetic (and it makes the "top band" scope of
  SUCCESSOR-A exact rather than approximate for this class).

## ARTIFACTS (all csp_-prefixed, this scratchpad)

- csp_statement.md   (three claims, general parameters, all pins)
- csp_proof.md       (complete proofs: L0/L1/L2, S1-S6, U0-U2, C)
- csp_verify.py      (dual-census verifier + pins + new cells + 4 mutations;
                      exit 0 = ALL PASS; replay:
                      tools/ramguard tiny -- python3 csp_verify.py)
- csp_claim_contract.md (roadmap 5.1 form)
- csp_findings.md    (this file)
