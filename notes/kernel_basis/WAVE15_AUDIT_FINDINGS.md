# Wave-15 fresh-context replay audit — v7 full-prize-resolution (DSP8 centerpiece + L1 + XR + Hankel/deleted-pair + governance)

Auditor session 2026-07-20. Catch numbering LOCAL (w15-C#, plus sub-audit
prefixes w15-D# DSP8, w15-L# L1, w15-X# XR, w15-H# Hankel). READ-ONLY all
repos. INCREMENTAL — written as the audit proceeds.

## PINS
- **v7**: /home/u2470931/smooth-read-solomin/prize-codex-resolution-v7-20260719,
  branch codex/full-prize-resolution-v7-20260719. HEAD pinned at audit start =
  **5661ba51** ("Add DSP8 joint-star depth Pareto compiler").
  WORKTREE IS DIRTY + DRIFTING (Codex actively editing the DSP8 centerpiece
  post-pin: 11 uncommitted files incl. f3_h3_dsp8_joint_star_depth_pareto_compiler/*,
  f3_h3_dsp8_correlation_bound/statement.md, notes). PIN STANDS. All reads via
  the pinned archive tree w15_tree/ (git archive 5661ba51, dag.json sha256
  verified 2a2b9087...).
- **v6 tail**: /home/u2470931/smooth-read-solomin/prize-codex-resolution-v6-20260718
  HEAD 98148f4c. Its 3 tail commits (8f91ed84 / ca63e168 / 98148f4c) are
  REPLAYED into v7 as the first three range commits 4b8fb6a0 / 3dc660c0 /
  de2117f4 (verdict: Hankel sub-audit). PROVENANCE NOTE (w15): identical
  commit MESSAGES but DIFFERENT patch-ids vs the v6 originals (v7
  0c1d36e8/8e5c591b/729f7799 vs v6 9a57735f/b3443487/4f03faa4) => re-expressed
  onto v7's base, NOT verbatim cherry-picks; must be audited fresh in v7
  context (not shortcut-cleared from the wave-14 v6 audit).
- **master**: /home/u2470931/smooth-read-solomin/prize, HEAD **e59a2998** =
  the v7 merge-base (wave-14 import has LANDED on master; master carries 834
  nodes). Scope = e59a2998..5661ba51 = **126 commits** (verified).

## VERDICT LINE (headline)

- **DSP8 CENTERPIECE VERDICT: (c) REDUCES / REFORMULATES — none proved.
  NOT (a) closure, NOT (b) max-P<=24 satellite.** (Sub-audit DSP8, full-depth,
  no integrity failure.) `f3_h3_dsp8_correlation_bound` is a TARGET leaf with
  NO verify.py; EVERY edge into it is `ev`, none `req` => its req-consumer
  `f3_h3_mobius_excess_half` stays **CONDITIONAL**, so **C36 / C36' / u1_x4 are
  NOT closed**. The 16 new nodes are genuine PROVED support theorems that
  reformulate the leaf into new *sufficient* routes, proving none. max-P<=24
  NOT proved (F-round-1 found max P=20 on sampled rows = evidence, not a
  uniform proof).
  **The reformulation is SOUND, not a weakened goalpost** (auditor-critical
  finding): the new (DSP8) target derives from the MASTER-PROVED (A6S8)
  compiler `4(10M^0+17M^A)<=5 B_(n,6)` by the exact x20 scaling
  (machine-checked: 750/20=300/8, 255/20=102/8, 68/20=17/5, 867/4/20=867/80),
  with overlap paid separately by PROVED GOP1+AQM1; GOP3=>GOP2 verified for ALL
  official orders n=2^13..2^41. The sufficient constant on 10K^0+17K^A relaxed
  223->362.89->478.74 ONLY because overlap is now paid at O(n^(5/3)) instead of
  lumped at O(n^2) — a legitimate refinement. Old `10J+17J<=892n^2` <=>
  `10K+17K<=223n^2` (J=4K) preserved and correctly labeled "superseded."
  **EXACT RESIDUAL**: an unconditional bound on the disjoint primitive-shift-
  pair correlation `10K_25^0+17K_25^A`; it now suffices to prove ANY ONE of
  (DSP8) / (DSP8-U) 160(10K^0+17K^A)<=76599n^2 / a JDP corner
  (e.g. Dbar_16^0+(29/22)Dbar_16^A<=(319/153)n^2) / FM 680M_21<=76599n^2 /
  exclusion of one accident-depth rectangle. NONE proved.
  All 16 nodes: PROVED claim == what is actually proved (no overclaim; every
  payment/compiler node disclaims "supplies no estimate for the disjoint
  primitive-SP count"). Replays verify.py 16/16 + verify_audit.py 16/16 =
  **32/32 PASS**; independent mutations **6/6 TRIP**. Unconditional/#137/#104/
  governance all PASS (no Modal in range; F-round census dated 2026-07-19,
  outside range). **Import-eligible YES** for the 16 support nodes as a sound
  reduction/reformulation layer — no false closure; the two TARGET leaves +
  the CONDITIONAL amber are correctly left open.
  Catches (all LOW/INFO): w15-D1 (correlation_bound TARGET is in-place rewrite
  across ~5 commits, benign — old target+non-claims preserved, = my w15-C5);
  w15-D2 (nodal 3-cubic-root envelope 2387n^2 > DSP8-U allowance 1914.975n^2 —
  correctly flagged residual); w15-D3 (Stepanov+GOP verify only the 29 official
  orders s=13..41 by discrete checks — confirm the order window at import);
  w15-D4 (excess_multistar_degree_ladder PROVED strengthened in place
  cc4806e4/eceaa20f — merge must re-verify it + downstream, = my w15-C5).
- **L1 mixed petal — PAYS a large frontier, does NOT close the red**
  (sub-audit L1, import-eligible as a batch, 1 minor #104 catch). 31 new
  PROVED nodes (two ladders) attach as **ev only**; consumer
  l1_mixed_petal_amplification stays **TARGET** both master and pin (no
  flip). PAID: fixed-p bounded-d boxes, retained-core cap, support-codim,
  super-Johnson cells, forced-background-overlap singletons, wide
  cross-determinant cells, intrinsic triple-polarity/bipolar boxes,
  Forney/CRT reductions — each residual keeps its Omega(n/log^2 n)
  rich-fiber (imported from PROVED petal_reserve_rich_fiber_reduction, not
  asserted). **EXACT RESIDUAL RED**: (1) growing-p branch; (2) balanced
  sub-Johnson strip with e,a,c all unbounded; (3) growing signed
  layout/core polarity; (4) canonical first-match supply for non-intrinsic
  charts; + 2 flagged barriers. **NO smuggled poses** — the one "additional
  theorem needed" is itself the PROVED barrier node
  l1_cross_quotient_split_descent_obstruction (explicit F_23 sub-Johnson
  cell, hand-verified nonsquare-discriminant). Replays **62/62 PASS** (full
  verify+verify_audit, NO coverage asymmetry), mutations **5/5 TRIP**.
  Unconditional (8 external req parents all PROVED on master); no
  Modal/pilot refs; governance = pre-request gates DECLINE to launch L1
  compute. **Catch w15-L1-1 (#104, MINOR)**: the consumer in-place rewrite
  (my w15-C5) DROPS the concrete known-mass witness (catch #176: 43 vs 10 at
  (16,8,97)) + provenance and is undated — re-append witness+provenance+date
  at import. w15-L1-2 (observation): L1 verify.py are contract/small-case
  checkers; general-n frontier rests on proof.md prose (codebase-standard).
- **XR split-pencil — SOUND / IMPORT-ELIGIBLE, closes NOTHING on the
  frontier** (sub-audit XR, no hard catches). The wave is machinery + honest
  narrowing of the nongeneric support-mismatch branch. Frontier ranks
  5,5,5 / 17,17,15 UNCHANGED; xr_highcore_collision_count and
  xr_lowcore_spread_heart both stay TARGET. **9 added nodes** (my brief
  miscounted 10): 7 PROVED lemmas, 1 honest TARGET bridge
  (xr_tangent_support_mismatch_bridge), 1 contained REFUTED
  (xr_nondeep_tangent_supportwise_payment — real F_17 rate-1/4 falsifier;
  only ev-wired to the TARGET bridge as a regression fixture; NO PROVED/req
  consumer). #158 checks PASS (invariant-excess descent is a genuine
  monovariant; Plotkin width bounds explanations NOT slopes — which is why
  the bridge stays open). Replays 9/9 PASS; mutations 4/4 TRIP.
  **xr_clean_residual_any_gate notes = PURE DATED APPEND (auditor cross-check
  AND sub-audit agree): +4 blocks dated 2026-07-20, 0 removed — the AMBER
  AUDIT / STRESS-VERIFIED auditor notes are INTACT; NOT an auditor-note
  edit.** Exact residual = two open currencies (distinct slopes across generic
  full-external-zero chart unions; slopes per joint explanation over the
  low-core family) — both must fit <=16n^3.
  Catches: w15-X1 (plotkin verify_audit labels 9 prose-string pins as
  "mutations=9" — coverage-label, LOW), w15-X2 (REFUTED node's live ev edge =
  benign regression fixture), w15-X3 (node count 9 not 10).
- **Hankel exceptional + deleted-pair + v6-tail — SOUND reductions, close
  NOTHING on the band; LANE B IMPORT-BLOCKED by a broken pose-contract pin**
  (sub-audit HANKEL). 34 nodes all PROVED. Replays: verify.py 34/34 PASS,
  verify_audit.py 8/8 PASS; mutations 5/5 TRIP.
  - **V6-TAIL (4b8fb6a0/3dc660c0/de2117f4): import-eligible, does NOT close
    the D_*=1 trace system.** kernel_plane_transversality (exact 2-vector
    kernel-plane certificate) + quadratic_moment_pin (its 3-scalar moment
    restatement) both explicitly disclaim closure; de2117f4 minted a LANE-B
    reduction. Band stays TARGET; residual = lower-Hankel chain, reciprocal
    divisibilities, corrected-square exclusion, split-fiber.
  - **LANE A (Hankel exceptional-only, 25 nodes): closes nothing**, exact
    reductions/necessary-gates only, each with a non-closure disclaimer;
    fully normalizes the distance-three exceptional-only chart and opens a
    macroscopic quotient-distance gap (distances 4..183251937964 impossible;
    high-distance tail begins 183251937965). Attacks ONLY the D_*=1
    exceptional-only distance-three stratum; D_*=0 / c=2 / z=0 UNTOUCHED.
    Import-clean (feeds band_closure via ev; band has no checker; no edge to
    adjacent_crossing). Band TARGET.
  - **LANE B (deleted-pair/harmonic/euler, 8 nodes + residual): reduces
    further, honestly** — even_jacobi halves the gcd degree 2^36->2^35 (the
    99e368aa "Halve" arc; Jacobi transform w=2x^2-1 verified exactly),
    deleted-pair chamber -> 6 gcd-triviality tests (EJN7) deferred to
    CR-002-J0; pure boundary -> 4 Belyi + 1 almost-Belyi passports + harmonic
    gates (harmonic-matched cover + Delta_H factorization open). Every node
    disclaims closure.
  - **Bonus micro-closure (sound)**: rate_half_residual_prime_field_collapse
    genuinely closes the extension-field shard for the band budget set
    B in {2^39, 2^39+1} — LTE forces f in {1,2,3,4}, 46 quadratic candidates
    all proven composite, no cubic/quartic => field is prime F_p, p>2^167.
    Narrows structure, not band coverage.

## DAG-DELTA (w15_dag_delta.py; master e59a2998 vs pin 5661ba51)

- Nodes **834 -> 934 (+100, 0 removed)**. Status of added: **96 PROVED, 2
  TARGET, 2 REFUTED**.
  - 2 TARGET: `submission_quality_paper_dossier`, `xr_tangent_support_mismatch_bridge`.
  - 2 REFUTED (honest refutations, tied to the "Correct/Repair" commits):
    `v13_2_near_rational_supportwise_payment`, `xr_nondeep_tangent_supportwise_payment`.
- Edges **1634 -> 1991 (+357: 360 add, 3 kind-changed)**.
- **STATUS FLIPS among shared nodes: 0 net.** (Transient oscillation, see
  w15-C2.) No CONDITIONAL/TARGET -> PROVED discharge anywhere.
- **3 edge-kind changes req -> ev** (NOT removals) — all in commit 25b01f9a
  (see w15-C1): m_sweep->list_safe, m_handling->list_safe,
  list_adjacency_closing->list_grand.
- 11 shared nodes with statement changes: f1_case_tower,
  f3_h3_dsp8_correlation_bound, f3_h3_excess_multistar_degree_ladder,
  f3_h3_official_order_template_survivor, l1_mixed_petal_amplification,
  list_adjacency_closing, list_safe, v13_bc_split_pencil_normal_form,
  xr_clean_residual_any_gate (statement+notes), xr_smallcore_spread_count,
  xr_strip_classification_rungs.

### Added-node cluster breakdown (100)
- DSP8 program: 16 (14 f3_h3_dsp8_* + 2 f3_affine_coset_pair_* +
  f3_h3_quotient_anharmonic_antipodal_twin). [sub-audit DSP8]
- L1: 31 l1_*. [sub-audit L1]
- Hankel exceptional-only / distance-three: ~25 rate_half_ca_hankel_*.
  [sub-audit HANKEL, Lane A]
- Antipodal deleted-pair/harmonic/euler: 9
  rate_half_list_budget_three_antipodal_* + rate_half_residual_prime_field_collapse.
  [sub-audit HANKEL, Lane B]
- XR: 10 xr_*. [sub-audit XR]
- WCL: 4 dli_wcl_* (main thread — Modal-independent, see GOVERNANCE).
- Governance/vendor/submission: paving_rf3_double_prime_koalabear_safe_rows,
  upstream_m1_koalabear_rank9_moving_root_slack_boundary,
  submission_quality_paper_dossier, v13_2_discrete_subfield_census_guard,
  v13_2_near_rational_pair_proximity, v13_2_near_rational_supportwise_payment(REFUTED).

## INTEGRITY (main thread — all PASS)

- **Structural validator (w15_validate.py) PASS**: 934 nodes / 1991 edges;
  0 duplicate ids; all edge endpoints exist; all statuses/kinds legal;
  ACYCLIC over req+alt; **26 REFUTED nodes, NONE is a req-child** (the 2 new
  REFUTED payments are correctly non-load-bearing); **STATUS-PROPAGATION
  CLEAN — no PROVED node has an unproved req child** => no smuggled discharge
  anywhere in the +100.
- **Manifest (w15_manifest.py) PASS**: verifier_manifest.json = 1432 hash
  pairs, ALL match at pin (0 missing, 0 stale).
- **Main-thread mutation controls 2/2 TRIP** (w15_mutate.py on scratchpad dag
  copies): (a) a PROVED node's req-parent flipped to TARGET => validator FAILS
  STATUS-PROP ("s0_zero_open(PROVED) req axes_verified=TARGET"); (b) a REFUTED
  node added as a req-child => validator FAILS ("REFUTED node required").
  Validator is non-vacuous.
- **Per-commit transient scan (w15_flipscan.py, base + 126 dumped dags)**:
  the ONLY status-field changes across the whole range are the transient amber
  pair (w15-C2); the ONLY edge-kind changes are the 3 req->ev of w15-C1. No
  other shared-node status touched at ANY commit.
- **Wiring / no-smuggled-poses (w15_extparents.py) PASS**: 32 distinct
  external req/alt parents feed the +100; 30 PROVED, 2 CONDITIONAL
  (list_grand, mca_grand — consumed only by the TARGET submission dossier).
  0 external parents absent on master; 0 REFUTED req-parents. No new open
  conjecture leaned on at the wiring level.

## CATCHES (main thread)

### w15-C1 (packaging re-architecture — SOUND but MAINTAINER-RATIFY, #104) — commit 25b01f9a "Narrow list adjacency to base arity"
Three req edges DOWNGRADED req -> ev (not removed): m_sweep->list_safe,
m_handling->list_safe, list_adjacency_closing->list_grand. Plus IN-PLACE
statement rewrites of THREE critical/shared nodes (list_safe,
list_adjacency_closing, list_grand) + list_safe/conditional.md proof rewrite
+ a ledger.md entry.
- **SOUND, NOT a discharge**: req-reachability (w15_reach.py) shows list_grand
  and prize STILL transitively req-reach list_adjacency_closing (now via
  list_large_m_scope_closure -> list_adjacency_closing, which persists). The
  m_handling/m_sweep obligations were NEVER in the grand/prize req-closure on
  master either (list_safe is required by nothing; it feeds via ev), so
  downgrading them removes no grand-gate obligation. list_safe narrowed to the
  ordinary m=1 case; arbitrary arity re-routed through list_large_m_scope_closure.
  Honestly documented: ledger.md "No mathematical status changed."
- **BUT #104 hazards for import**: (a) list_adjacency_closing statement is an
  IN-PLACE REWRITE (496->376 chars, common prefix 23) that DELETES the dated
  "RATE SCOPE (amber audit 2026-07-06)" annotation. (b) list_safe/list_grand
  statements also rewritten in place. (c) This restructures the CRITICAL list
  corridor's req topology. IMPORT: preserve master statements incl. the
  2026-07-06 annotation; land the m=1 narrowing as dated addenda; the req->ev
  topology change needs explicit maintainer ratification (it is a change to
  how the prize's list side is gated, even though obligations are preserved).
  NOT a refused packaging-PROVED flip (list_safe stays CONDITIONAL).

### w15-C2 (transient amber oscillation — governance observation, net zero)
At an intermediate state the C36 amber `f3_h3_mobius_excess_half` and
`dli_wcl_zone_coverage` read TARGET (not CONDITIONAL); commit 6b6cb821
"Merge canonical amber ceremonies" restored both to CONDITIONAL. At pin BOTH
are CONDITIONAL (verified in w15_tree dag). No commit diff shows any
CONDITIONAL->PROVED move. The DSP8 correlation_bound alt-leaf was "minted at
the C36 amber ceremony" (TARGET) — i.e. the DSP8 program ADDS an alt leaf to
the amber, it does not discharge it. Net-zero; document, do not refuse.

### w15-C3 (v13.2 self-correction arc — HONEST) — commits 4d1a8677 + 2814a6a9
Arc-check: an OLD v13.2 inference asserted a locus "numerically empty"; "exact
replay refutes that inference" (a below-one bit floor). Disposition is honest:
- `v13_2_near_rational_supportwise_payment` minted REFUTED (the wrong payment
  method), not required by anything (validator confirms).
- `v13_2_near_rational_pair_proximity` + `v13_2_discrete_subfield_census_guard`
  added PROVED as the corrected replacements.
- A "V13.2 CENSUS CORRECTION (2026-07-19)" marker inserted into
  `f1_case_tower.statement`; f1_case_tower stays PROVED (its structural proof
  "does not consume the old table"). w14-C3-class coupling: the guard node's
  verify.py PINS the "V13.2 CENSUS CORRECTION" marker inside f1_case_tower's
  statement => the statement edit and the guard node must land in the SAME
  import commit. IMPORT #104 note: the f1_case_tower edit inserts the marker
  mid-statement near the dated 2026-07-07 TOWER DEPTH DATUM block (common
  prefix 239 of 799, +41 net) — VERIFY at import the 2026-07-07 datum is
  preserved verbatim; prefer append-after.

### w15-C4 (v13_bc_split_pencil_normal_form — CLEAN append, no action)
Statement is a DATED pure append (+415, common prefix = full master length):
"V13.2 SUPPORT-WISE GUARD (2026-07-20) ... does not pay other support-wise MCA
witnesses ... exact rate-half mu_8 subset F_17 counterexample ...". Good #104
hygiene; explicit non-claim; references the refuted payment's F_17
counterexample.

### w15-C5 (consolidated #104 — in-place shared-statement rewrites, RECURS wave-14 w14-C1/C2)
Independent auditor cross-reads (w15_l1stmt.py, w15_stmt.py) show the
DSP8/L1 consumer shared-node statements are IN-PLACE REWRITES, not dated
appends (unlike the clean v13_bc append, w15-C4):
- `l1_mixed_petal_amplification` (TARGET->TARGET): common prefix 57 of 1687,
  -> 2225; bulk rewritten, adds "PROVED FRONTIER" content. [L1 sub-audit
  assesses residual/falsifier preservation]
- `f3_h3_official_order_template_survivor` (TARGET->TARGET): prefix 28 of 635
  -> 936; adds the six (P,R) corner alternatives. [DSP8 sub-audit]
- `f3_h3_excess_multistar_degree_ladder` (PROVED->PROVED): prefix 166 of 278
  -> 335; STRENGTHENS a PROVED node's claim ("P>=25 forces (8,6) bi-star,
  P>=33 forces (12,10) bi-star") — the DSP8 sub-audit must confirm the
  verify.py actually proves the strengthened (12,10) claim.
- plus list_adjacency_closing / list_safe / list_grand (w15-C1).
IMPORT: land these as dated addenda onto master's statement text (preserve
master originals as prefix per #104); for the PROVED excess_multistar ladder,
ensure the verifier covers the strengthened claim before adopting.

### w15-H1 (IMPORT-BLOCKING — broken pose-contract pin, KB #90) — LANE B
**AUDITOR-VERIFIED**: `critical/nodes/rate_half_list_adjacent_crossing/verify.py`
emits `"status": "FAIL"` at pin 5661ba51 (the `brackets_are_evidence` check;
nonclaim "adjacent crossing remains open for B*>=3" intact). Cause: the 8
LANE-B nodes were given `ev` edges into adjacent_crossing (they declare it
consumer) and its statement.md was appended, but the verify.py's hard-coded
incoming-edge list (59 entries) was NOT updated — incoming is now 67 (59+8),
diff = exactly the 8 LANE-B nodes, 0 spurious. The pose-contract PAIR
(verify.py + statement.md) did NOT travel together; no re-pin ceremony after
the LANE-B work. Severity: registration/bookkeeping, NOT soundness (edges are
ev; math unaffected) — but a HARD replay failure => the batch pin is RED and
**LANE B is not import-eligible until fixed**. REPAIR (mechanical): add the 8
`(NODE,"ev")` entries to the `brackets_are_evidence` expected list and re-pin
in the SAME commit as the LANE-B nodes (KB #90). LANE A + v6-tail unaffected
(band_closure has no checker).

### w15-H2 / w15-H3 (coverage, minor)
- w15-H2: 26/34 Hankel nodes lack verify_audit.py (only 8/34 carry one) —
  the wave-13/14 lane-asymmetry recurs on the distance-three/quotient chain.
- w15-H3: some LANE-A checkers are thin witnesses (endpoint_resultant_matrix
  verifies exponent-bookkeeping not the actual resultants; several exercise a
  single e=1 / F_17 witness) — general-e algebra rests on proof.md. No
  overclaim (statements are theorems with proofs), but checkers are witnesses.

## GOVERNANCE (main thread)

### Modal / #260
- **remote_launchers UNCHANGED at 10** (identical set master vs pin). No new
  registered launcher. **No result.json added under ANY node folder in range.**
  Every roadmap increment annotated "No Modal job was launched" (proof-asset
  count climbs 662 -> 835, all so annotated).
- **a487c599 "Record the deferred compute handoff policy"** (+15 lines, no
  code): formalizes a conservative spend-freeze ("$3 credit... no large run
  authorized... treat every entry as an outbound contributor request") and
  adds a pre-request/numbered-request distinction. BUT re-asserts the
  UNRATIFIED sub-$1 self-authorization ("preserve it for an explicitly
  approved... pilot with a conservative total cost below $1") — #260
  recurrence; annotate at import that this override is maintainer-unratified.
- **WCL Modal ingest via merge d55bf205 (side-branch d3996995)**: imported a
  Modal RESULT artifact `dli_wcl_weight5_recursive_norm_full_result.json`
  (consumed by the PRE-EXISTING node dli_wcl_ell2_weight6_recursive_norm_exclusion,
  under experiments/), WCL sizing modal scripts (wclp_*), and a DSP8 F-round
  census modal script (dsp8r1_census_modal.py; NO dsp8r1 result.json =>
  F-round not Modal-run). Economics note b8e9d214 is HONEST/CONSERVATIVE:
  full classification "33,000-39,000 CPU-hours ($6k-$14.3k)... Do NOT launch
  it", deferred to CR-004 for a funded contributor, and flags an unresolved
  "Norm(u)-saturation soundness gap" in the sizing report. It DOES report a
  measured "$45-60 / 250-280 CPU-hour" sizing from d3996995, framed as ingested
  contributor work. #260 item: disambiguate at import whether the $45-60 sizing
  is campaign spend or ingested; either way no NEW large launch, and the 4 new
  WCL nodes are Modal-INDEPENDENT (pure symbolic divisor-descent proofs; their
  verify.py reference no Modal/result.json).
- **Modal app-ids enumerated (#260 duty)**: two app-ids appear in-tree —
  `ap-gWA4UOyBSv4c8C4tqDVd84`, `ap-4mxCfTnbtIf2yz274On6sh` — both HISTORICAL
  WCL-lane records (commit d1d015e8) of TIMED-OUT past runs used as a route
  fence, NOT new launches. CR-002-J0 (7955ceb3/7991e2b7) is a deferred
  external request "not authorized on the low-credit Modal account", marked
  INCOMPLETE => no DAG change; only a ~0.2s ramguard-tiny pilot vendored.
- **Master merge 77f03b45** (conflicts dag.json + 3 orbit renders) resolved
  cleanly (no leftover markers; 0 net status flips => no master repair dropped);
  ingested c1r3 census/modal artifacts + modal_verifier_replay.json via master
  reconciliation.

### Modal cost enumeration (complete, w15 grep of range notes)
Only dollar/CPU figures in-range: `$3` remaining credit; sub-`$1` / below-`$1`
self-authorization ceiling (a487c599, unratified #260); `$45-$60` WCL sizing
(measured, ingested from d3996995 via merge d55bf205 — the SOLE actual-compute
figure); DEFERRED full-run estimates `$6k-$14.3k` and `$1.9k-$5.3k` (CR-004,
"Do NOT launch"). NO affirmative "job was run/launched" statement anywhere;
every increment reads "no Modal job was launched." => No in-tree campaign
launch; the $45-60 sizing is the only actual spend and is framed as ingested
contributor work (provenance to disambiguate at import).

### Vendored / submission nodes (main thread — SOUND)
- KoalaBear vendors `upstream_m1_koalabear_rank9_moving_root_slack_boundary`
  (596c7e2b) + `paving_rf3_double_prime_koalabear_safe_rows` (fe6040e4): both
  PROVED with SELF-CONTAINED verify.py (no modal/result/http/subprocess).
  Provenance clear in ids; feed rate_half_band_closure. Import-clean.
- `submission_quality_paper_dossier` (ac25985e): honestly **TARGET**
  (closure=artifact, deps mca_grand+list_grand). NO prize-solved overclaim:
  prize / mca_grand / list_grand / packaging ALL remain CONDITIONAL at pin.
  Minor: dossier statement uses present tense "proves and certifies both
  problems" while TARGET — acceptable given TARGET status + CONDITIONAL deps.

## COMPUTE-LAW SELF-REPORT (auditor)
- One trivial slip: an early probe script was written into the repo tree then
  removed (no tracked-file writes); corrected — all subsequent scripts in
  scratchpad, run via `ramguard tiny`, absolute paths, reading pinned tree.
- All heavy work avoided; no Modal; dag dumps done in bash (no python RAM).

## REPLAY GRAND TOTAL (verified counts)
- Node replays: **DSP8 32/32** (16 verify + 16 verify_audit) + **L1 62/62** +
  **XR 9/9** + **Hankel 42/42** (34 verify + 8 verify_audit) = **145/145 PASS**
  on the audited node set. PLUS main-thread structural validator PASS
  (934/1991), manifest 1432/1432 hashes, wiring/no-poses PASS.
- **THE ONE HARD FAILURE**: `rate_half_list_adjacent_crossing/verify.py`
  returns status:FAIL at pin (w15-H1, import-blocking, LANE B) —
  AUDITOR-VERIFIED.
- Mutation controls: **DSP8 6/6 + L1 5/5 + XR 4/4 + Hankel 5/5 + main-thread
  2/2 = 22/22 TRIP.**
- Per-commit scan: 126 commits, 0 net status flips (1 transient amber pair),
  3 req->ev edge-kind changes (all commit 25b01f9a), 0 node removals.

## IMPORT SURGERY SPEC

### A. Import-eligible clusters (with repairs)
1. **DSP8 (16 nodes)** — import as a sound REDUCTION/REFORMULATION layer; NO
   false closure (correlation_bound + official_order_template_survivor stay
   TARGET, mobius stays CONDITIONAL). Land the correlation_bound /
   official_order_template_survivor / excess_multistar_degree_ladder statement
   changes as DATED addenda on master text (w15-C5/D1). RE-VERIFY the
   in-place-strengthened PROVED `excess_multistar_degree_ladder` + downstream
   on master (w15-D4). Confirm the official-order window s=13..41 (w15-D3).
2. **L1 (31 nodes)** — import as an ev-only paying batch; consumer stays
   TARGET. Re-append the dropped known-mass witness (catch #176: 43 vs 10 at
   (16,8,97)) + provenance + date to l1_mixed_petal_amplification (w15-L1-1).
3. **Hankel LANE A + v6-tail (26 nodes)** — import-clean; feed band_closure
   via ev; band stays TARGET. (Optionally add verify_audit.py, w15-H2/H3.)
4. **XR (9 nodes)** — import-clean; the REFUTED node's ev fixture is benign;
   xr_clean_residual_any_gate notes = clean dated append (no repair).
5. **WCL (4 nodes) + vendor (KoalaBear x2) + v13.2 (3 nodes incl. 1 REFUTED)
   + submission dossier** — import-clean. v13.2: land the f1_case_tower
   "V13.2 CENSUS CORRECTION" marker in the SAME commit as the guard node
   (verify.py pins it), preserving the 2026-07-07 TOWER DEPTH DATUM (w15-C3).

### B. IMPORT-BLOCKED until repaired
- **Hankel LANE B (8 nodes + residual)** — BLOCKED by w15-H1: update
  `rate_half_list_adjacent_crossing/verify.py` bracket list with the 8
  `(NODE,"ev")` entries and RE-PIN in the same commit (KB #90 pose-pair
  rule), then re-replay to green before importing.

### C. Packaging re-architecture (25b01f9a) — MAINTAINER-RATIFY, do not auto-adopt
- The req->ev downgrades on the CRITICAL list corridor + in-place rewrites of
  list_safe/list_adjacency_closing/list_grand statements (deleting the dated
  2026-07-06 amber-audit annotation) are SOUND (obligation preserved) but
  change the prize's list-side gate topology and delete dated annotations.
  Surface to the maintainer; preserve master statements + dated addenda at
  import.

### D. Refusals / governance holds (no outright refusal warranted)
- No packaging-PROVED flip; no smuggled discharge; no unauthorized in-tree
  Modal launch. Maintainer-ratify holds: (1) w15-C1/Section C above;
  (2) #260 unratified sub-$1 override language (a487c599, b8e9d214);
  (3) the ingested WCL $45-60 sizing spend provenance + its flagged
  Norm(u)-saturation soundness gap (CR-004 deferred, "do not launch").
