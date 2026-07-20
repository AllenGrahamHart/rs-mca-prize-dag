# WAVE-15 SUB-AUDIT L1 — Codex v7 replay audit (PIN 5661ba51)

READ-ONLY. Pinned tree: scratchpad/w15_tree. Repo dag: /home/u2470931/smooth-read-solomin/prize/dag.json

## Node set confirmed
31 new l1_ nodes (matches w15_added_nodes.txt). Extra folder l1_coset_chart_residue_bridge is PRE-EXISTING (not in added set).
Ladder-1 (17 nodes, c9f2c78e..7400e1ba): mixed_residual_intersection_pin, two_petal_small_support_anchor_closure, polarized_petal_entropy_ledger, polarized_b11_box_closure, bounded_polarity_marked_full_pencil_reduction, marked_constant_shift_{subtwoell,multistrip}_exclusion, marked_constant_shift_extremal_kernel_normal_form, marked_constant_shift_forney_window_normal_form, marked_common_pencil_crt_fiber_bound, marked_common_pencil_quotient_boundary_router, quotient_chart_bounded_core_boundary_closure, marked_common_pencil_next_strip_boundary_fiber_bound, quotient_chart_bipolar_entropy_closure, core_bipolar_signed_quotient_normal_form, intrinsic_quotient_source_chart_census, intrinsic_partial_core_triple_polarity_closure
Ladder-2 (14 nodes, 45b75960..18383409): bounded_mark_affine_split_pencil_compiler, affine_split_pencil_cross_determinant_uniqueness, fixed_support_cross_determinant_fiber_bound, fixed_support_defect_johnson_bound, bounded_retained_core_payment, cross_quotient_split_descent_obstruction, fixed_support_codeword_quotient_bound, background_overlap_singleton_payment, background_quotient_johnson_bound, joint_core_background_johnson_bound, joint_johnson_source_scale_gate, joint_plotkin_boundary_payment, bounded_plotkin_excess_payment, background_surplus_plotkin_payment
Commit 18383409 "Pay logarithmic L1 effective excess" = NO new node (modifies existing — likely consumer). Governance commits with no node: f380b270 (L1 compute promotion gate), 30cc2c42 (HGE4 deferred compute), 9f8cbb82, 90eccc05.

## FINDINGS (in progress)

### Replay + DAG hygiene (DONE)
- Pinned tree is FULL archive; tree/dag.json md5 == git show 5661ba51:dag.json (09a766...). Hash-verified.
- REPLAY: all 31 verify.py + 31 verify_audit.py PASS via ramguard tiny => 62/62 PASS. Full audit coverage (no asymmetry). Pre-existing l1_coset_chart_residue_bridge has no verify (not a v7 add).
- verify.py that read dag.json use ROOT=parents[3]=w15_tree => they check PIN dag (self-consistent). No Modal/pilot/experimental/conjectural refs in any verify script.
- CONSUMER l1_mixed_petal_amplification = TARGET on BOTH master and pin (status did NOT flip). Statement rewritten (see below). Its ONLY req edge -> imgfib (CONDITIONAL, unchanged). 31 l1 nodes attach as `ev` (evidence) edges, NOT req => they do NOT close the red. HONEST: no false DAG closure.
- All 51 req edges FROM the 31 l1 nodes -> PROVED nodes (0 non-proved). No l1 req-dep on any REFUTED node. No internal req cycle. All req-targets are within the added set => wave-15 batch is self-contained/unconditional modulo pin PROVED nodes.
- 8 l1 roots (no req dep): background_surplus_plotkin_payment, core_bipolar_signed_quotient_normal_form, intrinsic_partial_core_triple_polarity_closure, marked_constant_shift_extremal_kernel_normal_form, marked_constant_shift_subtwoell_exclusion, mixed_residual_intersection_pin, quotient_chart_bounded_core_boundary_closure, two_petal_small_support_anchor_closure.
- Added non-PROVED nodes (100 total = 96 PROVED + 2 TARGET + 2 REFUTED) are all in XR/v13_2 ladders, NOT L1: TARGET {submission_quality_paper_dossier, xr_tangent_support_mismatch_bridge}; REFUTED {v13_2_near_rational_supportwise_payment, xr_nondeep_tangent_supportwise_payment}.

### CONSUMER RED — what remains (from pin statement.md)
PROVED FRONTIER (paid cells): fixed p<=P,d<=ell+E boxes; fixed retained-core cap a<=A; fixed support codim c (direct codeword diff, no splitting); fixed (p,r_cross) boxes per source chart; super-Johnson cells (k-1)(e-1)<d^2; forced-background-overlap singletons; fixed intrinsic triple-polarity boxes; bipolar boxes; Forney/CRT/signed-core reductions on common quotient pencils. Every residual retains Omega(n/log^2 n) source-coupled rich fiber.
EXACT LIVE CONTENT (residual RED, still TARGET):
  (1) the growing-p branch;
  (2) the balanced sub-Johnson strip with e, a, c all unbounded inside the width window;
  (3) growing signed layout/core polarity;
  (4) canonical first-match supply for non-intrinsic charts.
  + explicitly flagged barriers: "zero-syndrome full-petal payment is not an affine-cell theorem"; "cross determinant quotient need not split even in an exact threshold sub-Johnson cell => recursive split-locator descent requires an additional theorem" (this barrier is itself PROVED as l1_cross_quotient_split_descent_obstruction — honest, not a smuggled pose).

### Proof soundness spot-checks (DONE)
- verify.py are CONTRACT checkers: Boolean/arithmetic identities + small-case brute force + DAG-wiring/phrase presence. They confirm internal consistency + wiring, NOT general-n validity (that lives in proof.md). Standard for this codebase.
- Johnson node (l1_fixed_support_defect_johnson_bound): brute-force max_clique asserts maximum*(d^2-n*overlap) <= n*(d-overlap) = correct Johnson bound; cross-determinant divisibility (support_locator*locator(intersection) | (w1 f2 - w2 f1)) checked over F_7. SOUND arithmetic.
- Plotkin node (l1_joint_plotkin_boundary_payment): constant-weight Plotkin bound (|family|<=2|universe|) + 3-way algebraic identity for the payment condition + "direct => petals>=3(rate-1)". SOUND.
- l1_cross_quotient_split_descent_obstruction: HONEST BARRIER, not a smuggled pose. Explicit F_23 sub-Johnson cell; cross-quotient = (X-13)(20+15X+15X^2); quadratic discriminant 14 = nonsquare mod 23 (hand-verified: 15^2-4*15*20 = -975 == 14 mod 23; QR(23)={1,2,3,4,6,8,9,12,13,16,18}, 14 not in). Proves recursive split-locator descent is NOT universal. Fully replayed by verify.py.
- Omega(n/log^2 n) rich-fiber forcing: NOT asserted in the L1 nodes; IMPORTED from petal_reserve_rich_fiber_reduction (PROVED on master, a req-parent of mixed_residual_intersection_pin). mixed_residual Scope explicitly says it does NOT prove any parameter tends to infinity / does not promote the consumer.

### MUTATION CONTROLS: 5/5 TRIP (all AssertionError)
  A Plotkin 4*ell->3*ell (breaks 3-way identity) TRIP
  B Johnson exact-pair fiber count 3->4 TRIP
  C cross-quotient discriminant 14->15 TRIP
  D req-parent petal_reserve_rich_fiber_reduction PROVED->TARGET TRIP
  E consumer statement phrase "Omega(n/log_2^2 n)" removed TRIP
Verify scripts are non-vacuous.

### #137 completeness (VERDICT: complete at bookkeeping level)
Every payment node carries an explicit Scope section naming its exclusions, and the exclusions aggregate exactly into the consumer's 4-branch EXACT LIVE CONTENT:
- cross_determinant_uniqueness: proves singleton for t*ell>2d+p (clean degree-divisibility: prod L_Ti | J*Delta, deg<=2d+v => uniqueness); defers survivor window (CD7), non-intrinsic charts, growing p.
- intrinsic_quotient_source_chart_census: 3^L intrinsic charts, L=n/ell, ell>=c_0 n/log n => 3^{O(log n)}=poly; defers non-intrinsic/partial-core/arbitrary-locator.
- intrinsic_partial_core_triple_polarity_closure: bounds by (R_0+1)(B_0+1)(P_0+1)16^L n^(...) q^(2P_0); "counterfamily must have one of p_layout,p_defect,p_petal escape cap"; defers non-intrinsic.
Intrinsic-vs-non-intrinsic is an exhaustive dichotomy; fixed-box-paid vs growing-parameter-residual is exhaustive. No case quietly dropped. NOTE: exhaustion is at the bookkeeping/statement level; per-node general-n correctness rests on proof.md prose (not machine-checked, see below).

### Unconditionality (VERDICT: UNCONDITIONAL)
- 51 internal req-parent edges (all within added PROVED batch) + 8 external pre-existing req-parents, ALL PROVED ON MASTER: petal_reserve_rich_fiber_reduction, pma_b11_first_match_router, pma_coset_subtwoell_saturation_exclusion, pma_official_rate_small_source_degree_sieve, pma_petal_pattern_root_pinning_ledger, pma_quotient_closure_scope, pma_saturated_mixed_support_kernel, pma_source_paving_bridge.
- No conditioning on any TARGET/REFUTED/CONDITIONAL node. No refuted-predicate references. No Modal/pilot/experimental in the 31 nodes (sole "experimental" hit = pre-existing l1_coset_chart_residue_bridge upstream provenance, not v7).
- imgfib (CONDITIONAL) is a req-parent of the CONSUMER only (itself TARGET), not of the 31 PROVED nodes. Fine.

### #104 consumer sweep (VERDICT: in-place rewrite; minor hygiene loss)
- Consumer statement REWRITTEN in place (not appended). PRESERVES: TARGET status (no flip), FALSIFIER ("reserve-valid super-polynomial mixed family or route-kill lower bound exceeding every n^B"), and adds non-claim ("zero-syndrome full-petal payment is not an affine-cell theorem").
- DROPS: concrete known-mass witness (catch #176: 43 mixed-petal vs 10 full-petal at (16,8,97)), catch #212/#176 provenance, Codex-v4-PMA-campaign reference, "naive induction RETRACTED 2026-07-05" history. UNDATED rewrite.

### Governance (VERDICT: responsible restraint, no launch)
- f380b270: +31 lines to notes/PRIZE_COMPUTE_REQUESTS.md "Pre-request L1" gate: explicitly DECLINES to promote L1 to a numbered compute request until a stabilization/normal-form theorem is proved; "present as a theorem frontier ... not request a large sweep." + regenerated orbit/*.svg,*.html art. NO Modal launch.
- 30cc2c42: +28 lines "Pre-request HGE4" note, defers compute until a router exists. NO launch.

### CATCHES
- w15-L1-1 (MINOR, #104 doc hygiene): consumer in-place rewrite drops known-mass witness (#176: 43 vs 10 at (16,8,97)) + catch #212/#176 provenance + is undated. REPAIR: re-append the known-mass datum + provenance + date before import.
- w15-L1-2 (OBSERVATION, verifier scope): L1 verify.py are contract-checkers (identity + small-case brute force over F_7/F_23 + DAG/phrase wiring). General-n validity of the frontier claims rests on unaudited proof.md prose. Codebase-standard, not a v7 regression; flagged so importers know the machine-checked layer != the mathematical layer.

### IMPORT-ELIGIBILITY: YES (as a batch), with w15-L1-1 repair recommended.
31 nodes all PROVED, self-contained, unconditional (external anchors master-PROVED), 62/62 verify+audit PASS, DAG-clean (ev-only to consumer, consumer stays TARGET), 5/5 mutation trips. Honest scoping throughout; one PROVED barrier (cross_quotient_split_descent_obstruction) explicitly marks the descent gap.
