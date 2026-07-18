# Wave-10 fresh-context replay audit — v4 overnight tail (rate-half safe side, Hankel endpoint, XR rank-two) + v5 delta (packaging, list leaves, C36)

Auditor session 2026-07-18. Catch numbering LOCAL (w10-C#). READ-ONLY all three repos.

## PINS

- **v4**: /home/u2470931/smooth-read-solomin/prize-codex-resolution-v4-20260713, branch
  codex/full-prize-resolution-v4-20260713. Scope **4442ffd5..899326a8** (35 commits,
  2026-07-17 21:37 .. 07-18 04:54). HEAD == 899326a8 at audit start (== the wave-9 close
  pin; NO wave-11 drift). Worktree has ONE untracked file:
  experiments/prize_resolution/dli_wcl_weight5_recursive_norm_full_result.json (weight-5
  sweep output, NOT committed — see Cluster 5).
- **v5**: /home/u2470931/smooth-read-solomin/prize-codex-resolution-v5-20260718, branch
  codex/full-prize-resolution-v5-20260718. HEAD pinned at start = **d5a89194**
  (clean worktree). BRANCH POINT: **20dc014a = master's HEAD** (post-wave-9 import
  "Modal execution re-pin after wave-9: 201/201 PASS"). v5 does NOT contain v4's history
  (merge-base(v5, v4-HEAD) is not 899326a8; v4's 35-commit tail is absent from v5's line).
  v5-unique scope = **20dc014a..d5a89194 (17 commits, 07-18 05:01 .. 10:22)**.
  STRUCTURAL FACT: v4 and v5 are PARALLEL campaigns off different bases attacking the same
  post-wave-9 frontier; v5 re-derives/ports content (e.g. 07baa74c "Port C36
  identity-deficit endpoint" = byte-level port of v4's 899326a8 node) rather than merging v4.
- **master**: /home/u2470931/smooth-read-solomin/prize, branch master, HEAD 20dc014a.

## VERDICT LINE (updated as clusters complete)

- CLUSTER 1 (v4 rate-half safe-side suite): **IMPORT-WITH-REPAIRS (custody-minor) — THE
  CROSSING IS NOW DETERMINED, UNCONDITIONALLY AND EXACTLY, ON THE EXPLICIT FIELD RANGE
  2^128 < q < (B_Q+1)*2^128 ~ 2^166.5028** (a_RH(q) = n - floor(q/2^128) + 1), resting only
  on master's wave-6 PROVED mca_quadratic_prize_rows; sparse side safe through the explicit
  curve a_sp(q) = n - min(2^39, floor(q/2^128)) (= 3n/4 for q >= 2^167); high-field bracket
  a_RH <= 3n/4 for q >= 2^169. All 7 verifiers PASS; 25/25 independent checks PASS
  (w10_checks.py incl. own-convention exhaustive toy). Extension to q < 2^167 is GATED on
  Cluster 2's Hankel verdict. No arc weakening in-range; zero flips.
- CLUSTER 2 (v4 Hankel endpoint suite, 12 nodes): **IMPORT-CLEAN (custody letter-violation
  w10-H2 only). All 12 nodes concern B_ca^far ONLY (never S_sparse); four load-bearing
  proofs hand-traced sound by the sub-auditor (Prony/locator equivalence; minor-degree root
  count; endpoint annihilation; divided-power apolar CI + Forney minimal basis + KCF +
  residual contraction, A>=5 floor arithmetic verified); 12/12 verifiers PASS; independent
  cross-checks incl. exact-tightness brute force of the pullback capacity formula. The
  decisive theorem (ad55d857) has an UNCONDITIONAL layer: B_ca^far(n-r) <= r+1 for EVERY
  radius r <= 2^39-2 across ALL rank profiles. The two branch-"Close" commits are
  conditional case-splits (no q-range by themselves). The seven endpoint nodes are
  conditional normal-form theorems about a hypothetical failing profile at strict budget
  e=m only — they rigidify but do NOT shrink the open budget set (w10-H5). Zero
  conjecture/corridor/f3_h3 dependencies; arc strictly monotone (two in-range
  self-corrections, both strengthenings). Its only external conditionality (w10-H4:
  rate_half_quadratic_exact_range) is discharged by THIS audit's Cluster 1. Full detail:
  w10_hankel_report.md.**
- CLUSTER 3 (v4 XR rank-two suite, 5 nodes): **IMPORT-WITH-REPAIRS (w8-C7-pattern custody
  only). All 5 nodes SOUND (sub-audit: support atlas + rational-fibers fully hand-traced;
  atlas totality PROVED not assumed — #158 check PASS), 5/5 verifiers PASS with mutation
  controls. Master's rank-2 chart first-match audit PARTIALLY PAID (chart caps 12/12/9 &
  13/13/10 contract to <= 8 coordinates; pair-cap-3 slice discharged; 3/5 profiles = forced
  syzygies; exact witnesses block further generic arguments). (u,v) <= (60,7) untouched;
  frontier ranks 5,5,5 / 17,17,15 UNCHANGED at pin; both reds stay TARGET. Catches
  w10-X1..X4 (see w10_xr_report.md).**
- CLUSTER 4 (v5 delta): **packaging flips REFUSED (w10-C1/C2); list-leaf suite SOUND and
  the list safe side is now OWNED (w9-C3 answered); cyclic floor re-instantiation DOUBLES
  the unsafe reach to 2^34-1; C36 chain dependency-CLEAN (no cluster-A deps). 13/13 v5
  verifier replays PASS; all headline constants independently reproduced.**
- CLUSTER 5 (C36 energy endpoint + codegree fences + weight-5 state): **identity-deficit
  endpoint AUDITED-SOUND (dependency-clean, verifier PASS, ported byte-identically to v5);
  diagonal-ratio fence + unordered Newton prefix DEFERRED with unaudited wave-8 Cluster A
  (their req parents are cluster-A nodes absent from master); weight-5 (1,5) sweep DID NOT
  COMPLETE in-range (zero dli commits in v4 range; only an untracked 2KB PARTIAL
  prefix-test artifact, 128/2,296,920 rows, max_v2=17, status PARTIAL — pre-registered
  expectations stand, nothing to verdict).**

## DAG-STATUS-DELTA TABLE — v4 range 4442ffd5..899326a8 (per-commit, w10_dag_delta.py)

Net: **702 -> 728 nodes; 26 NEW nodes, ALL PROVED; 0 removed; NET STATUS FLIPS: ZERO;
1315 -> 1383 edges (68 new, 0 removed).** No auto_discharge sweep fires in this range
(packaging/list_safe/descriptor all untouched in v4). rate_half_band_closure stays TARGET
throughout; its dag statement GROWS append-style 543 -> 1029 chars (per-commit deltas in
w10_dag_delta_output.txt). Statement-field changes on existing nodes:
rate_half_sparse_pinning_rigidity (443->520, eb553b92 sparse safe curve add),
rate_half_band_closure (x4 growth steps), plus growth on 4 of the new nodes themselves.

New v4 nodes by cluster:
- Cluster 1 (rate-half safe side, 7): mca_full_agreement_endpoint (19d19f93),
  rate_half_half_distance_safe_bracket (0b313b01), rate_half_far_ca_rider_reduction
  (ce16a7fc), rate_half_quadratic_exact_range (e86b0b88+568178b8),
  rate_half_postquadratic_mds_extension_fence (d4e37c9a),
  rate_half_far_ca_anchor_pencil_normal_form (8997e257) + sparse-curve statement growth on
  the wave-9 node rate_half_sparse_pinning_rigidity (eb553b92).
- Cluster 2 (Hankel, 12): rate_half_ca_hankel_{split_pencil_equivalence, fullrank_branch,
  fixed_kernel_branch, minimal_index_budget, exceptional_root_charge,
  endpoint_saturation_rigidity, endpoint_norm_factorization,
  endpoint_rational_branch_exclusion, endpoint_component_defect_localization,
  endpoint_separated_pullback_exclusion, endpoint_rational_normal_kernel_curve,
  endpoint_dominant_rank_amplification}.
- Cluster 3 (XR, 5): xr_split_pencil_trade_rank_two_support_atlas,
  xr_split_pencil_rank_two_maxwell_properness, xr_split_pencil_six_face_syzygy_quotient,
  xr_split_pencil_nonlocal_rank_two_rational_fibers, xr_lowcore_u1_augmented_paving_scope_fence.
- Cluster 5 (C36, 3): f3_h3_diagonal_ratio_energy_profile_fence (f4748361),
  f3_h3_unordered_newton_prefix (bde33876), f3_h3_identity_deficit_energy_close (899326a8).

All 26 wire ev into their red (rate_half_band_closure / xr_highcore_collision_count +
xr_lowcore_spread_heart / f3_h3_mobius_excess_half); req edges form internal chains only.
b1098e12 ("Fence fixed-tail Hankel shortcut") is note-only (no dag delta).

## DAG-STATUS-DELTA TABLE — v5 range 20dc014a..d5a89194 (per-commit)

Net: **684 -> 694 nodes; 10 NEW (9 PROVED + 1 TARGET rate_half_list_adjacent_crossing);
0 removed; 2 STATUS FLIPS (both at 143de622, both REFUSED — see Cluster 4); 1277 -> 1305
edges; 3 edge-kind DEMOTIONS req->ev (a47b87c0); heavy in-place statement rewrites of
master nodes.**

Per-commit:
| commit | dag delta |
|---|---|
| 07baa74c | NEW f3_h3_identity_deficit_energy_close [PROVED] (byte-port of v4 899326a8) |
| a33aa391 | NEW f3_h3_shifted_energy_zero_normalization [PROVED] |
| 10b19289 | NEW f3_h3_cubic_block_tail_energy_fence [PROVED] |
| cba61ec2 | NEW f3_h3_uniform_product_fiber_stepanov [PROVED] — NOTE: same node id exists in
  v4's wave-8 Cluster A (UNAUDITED); v5 re-mints it independently on the master base |
| 99b64378 | NEW f3_h3_global_derivative_ideal_valuation [PROVED] |
| 373bbc56 | STMT rewrites harness (884->598), dossier_partial (684->448); +EDGE
  descriptor->packaging req (CONTRADICTS master's "demoted to ev" note) |
| 143de622 | **FLIP packaging CONDITIONAL->PROVED; FLIP descriptor TARGET->PROVED**; STMT
  rewrites packaging/compiler/harness/descriptor/dossier_partial |
| a47b87c0 | STMT rewrites list_safe (132->224), list_adjacency_closing (496->376);
  EDGE-KIND DEMOTIONS req->ev: m_handling->list_safe, m_sweep->list_safe,
  list_adjacency_closing->list_grand |
| 732e9dfd | NEW rate_half_list_adjacent_crossing [TARGET]; ev from cyclic floor; req into
  list_adjacency_closing |
| 1e26255b | STMT REPLACEMENTS: rate_half_band_closure 8231->395 (!), cyclic floor 657->494,
  simple_pole_mca_floor 384->314; heavy file rewrites of master-imported nodes |
| c67775dd | NEW f3_h3_cutoff18_double_accident_reduction [PROVED]; STMT
  f3_h3_mobius_excess_half 1687->333 (in-place shrink of the RED's statement) |
| d11d8115 | (no dag delta; file-only twin of c67775dd) |
| a6a183f7 | NEW f3_h3_double_accident_derivative_ideal [PROVED] |
| 328c4b5b | STMT growth on double_accident_derivative_ideal + req edge from
  uniform_product_fiber_stepanov |
| ce2b2fcf | NEW rate_half_list_integer_johnson_safe_anchor [PROVED] |
| 24a56ac8 | STMT rate_half_band_closure 395->467, mca_quadratic_prize_rows 487->465; +ev
  mca_quadratic_prize_rows->rate_half_band_closure |
| d5a89194 | NEW rate_half_list_low_budget_exact_crossing [PROVED] |

## CLUSTER 4 — V5 PACKAGING FORENSICS (mandatory-first item) — BOTH FLIPS REFUSED

Mechanism (fully traced):
1. Master baseline: packaging = gate:all CONDITIONAL with req parents
   {compiler, harness, dossier_partial, bridge_ledger} ALL PROVED — i.e. master HOLDS the
   amber deliberately (node notes carry the MAINTAINER SIGNAL: packaging must target Paper
   D's certificate grammar, "not a parallel standalone dossier"). Master possesses its own
   tools/auto_discharge.py (adopted post-wave-8, with a regression rule) but does not run
   it on packaging; NOTE: master's auto_discharge.py STILL has the w8-C10 artifact-path bug
   (writes to tools/../nodes/<id>/, a nonexistent tree — background/critical prefixes
   missing), so its regression sweep can never fire in practice (w10-C3).
   Master's descriptor = TARGET, notes: "tool — not truth-apt ... packaging convenience,
   not a load-bearing hypothesis — demoted to ev of its consumers".
2. v5 373bbc56 ("Repair composed harness and packaging frontier"): rewrites harness +
   dossier_partial dag statements IN PLACE (shrinks 884->598, 684->448) and adds a NEW
   **req** edge descriptor -> packaging — the exact opposite of master's recorded demotion
   decision (ev-of-consumers).
3. v5 143de622 ("Close row descriptor and packaging artifacts"): builds the missing tool
   (tools/prize_row_descriptor.py, 155 lines) + descriptor/verify.py + hand-written
   proof.md; flips descriptor TARGET->PROVED; REWRITES the packaging dag statement in
   place, NARROWING the claim ("every constant descriptor-generated" -> "every row-derived
   scalar is descriptor-generated, while theorem counts remain provenance-pinned
   proof-packet inputs"); writes a MANUAL packaging/proof.md ("These five proved components
   establish the repaired packaging statement") and flips packaging CONDITIONAL->PROVED.
   NOT an auto_discharge sweep (no "(auto-discharged)" artifact; hand-written proof), but
   the same one-way outcome.

VERDICTS:
- packaging CONDITIONAL->PROVED: **REFUSED** (standing refusal; master's amber is a
  deliberate maintainer-signal choice; v5's close is of a NARROWED restatement, not of
  master's statement; and it rests on the descriptor req edge that reverses master's
  recorded demotion). w10-C1.
- descriptor TARGET->PROVED: **REFUSED AS A FLIP; content importable.** The tool artifact +
  propositional statement + verify.py genuinely answer master's own queue item ("reword to
  propositional core"; missing-tool flag). Import the FILES (tools/prize_row_descriptor.py,
  descriptor/{proof.md, verify.py, statement addendum, artifact_audit/frontier updates}) as
  content + a surfaced RECOMMENDATION to flip descriptor after master review; keep the
  packaging wiring as ev per master's demotion note, NOT req. w10-C2.
- harness/dossier_partial/compiler/packaging/descriptor statement rewrites: in-place
  rewrites of master dag statements -> dated addenda on import (#104). w10-C4.

### Cluster 4 continued — the v5 rate-half list suite (a47b87c0, 732e9dfd, 1e26255b,
ce2b2fcf, 24a56ac8, d5a89194)

1. **732e9dfd "Expose rate-half list safe-side leaf" — YES, it OWNS the w9-C3 gap.** New
   TARGET node rate_half_list_adjacent_crossing = the exact list mirror of (RH-ADJ): find
   a_L(C) with L_1(a_L) <= B* < L_1(a_L-1), req-wired INTO list_adjacency_closing (so the
   rate-half row of the adjacent claim now has a named owner instead of "no owner"), ev-fed
   by the cyclic floor. Verifier PASS incl. the check floor_disclaims_safe_side and the
   honest nonclaim "Budgets one and two are exact; the adjacent crossing remains open for
   B*>=3". IMPORT (as the w9-C3 repair vehicle).
2. **ce2b2fcf "Add rate-half list Johnson safe anchor" — PROVED
   rate_half_list_integer_johnson_safe_anchor, HAND-TRACED SOUND** (exact-integer Johnson:
   ell=B+1 codewords, incidence floor n*C(d,2)+rd via convex minimization at ell*a=nd+r vs
   pairwise cap C(ell,2)(k-1) — every step re-derived). Gives the computable safe anchor
   a_IJ; bracket k+2^34 <= a_L <= a_IJ on B*>=3; a_IJ=3n/4 for B* in {1,2,3};
   = floor(sqrt(n(k-1)))+1 = 1,554,944,255,988 for B* >= 332,114,441,762. My independent
   reproduction (w10_v5checks.py): anchor exact at 3n/4 two-sided for B=1,2,3; sqrt-anchor
   threshold TIGHT at 332,114,441,762 (fails at threshold-1); verifier PASS
   (threshold=332114441762 first_johnson=1554944255988 — exact match to my values).
   "No predecessor-unsafety claim is made" — honest.
3. **d5a89194 "Close rate-half list budgets one and two" — PROVED
   rate_half_list_low_budget_exact_crossing: the LIST crossing is DETERMINED for
   B* in {1,2}** (i.e. every official rate-half field 2^128 < q < 3*2^128): exactly
   a_L = 3n/4 (Johnson safe at 3n/4 by margins 1 and 3 — my independent margins match;
   explicit 2-/3-codeword constructions unsafe at 3n/4-1; feasibility 2(3n/4-1) <= n+(k-1)
   re-checked). "No claim for B>=3 or for MCA/CA" — trigger separation preserved. Verifier
   PASS (official_margins=1,3 fixtures=2).
4. **1e26255b "Optimize rate-half cyclic floor" — GENUINE DOUBLING of the unsafe reach,
   content sound; custody violations in form.** Re-instantiates the wave-8/9-audited
   general cyclic theorem at c=2^33, N=256, d=1, s=c-1: excess dc+s = 2^34-1 =
   17,179,869,183 (vs wave-9 sigma_0 = 8,594,128,895; ratio 1.999), with a FIELD-
   INDEPENDENT list ceil(C(255,129)/256) ~ 2^242.65 (d=1 kills the q^(d-1) division), so
   list-unsafety through excess 2^34-1 for EVERY q < 2^256 with 114.65 bits of margin
   (verifier prints cap_list_log2=242.650300488 = my independent value; new
   cap_uniform_extremality_checks=74 machine-checks the "unique maximal-prefix optimum"
   claim). All theorem hypotheses verified (c|k, 0<s<c, d<=N/2-1); the wave-9 general-
   theorem audit covers this instantiation (its s<c and prefix-coset arguments were derived
   for ALL parameters; d=1 prefix = a_0 alone, N*q^0 classes). The simple-pole MCA
   conversion at the new list: E > 2^-128 (indeed > 2^-42) at q ~ 2^129..2^256 — my exact-
   integer check. CONSEQUENCE: the MCA lower bracket improves to **a_RH(q) >= k + 2^34**
   and the LIST unsafe side extends to the same reach (v5 band statement records both).
   CUSTODY (w10-C4/C7): in-place rewrites of the two master-imported floor nodes + band
   statement 8231->395 + ONE in-place edit of a prior QUALITY.md block (the old sigma_max
   constant line deleted) — restore + append on import.
5. **24a56ac8 "Close rate-half MCA low-field slice"** — v5 INDEPENDENTLY derives v4's
   low-field determination from the same master staircase node (band statement: "The
   universal quadratic staircase closes the complete slice 1<=B*<=389500552609 with
   a_RH=n-B*+1"; +ev edge mca_quadratic_prize_rows -> rate_half_band_closure; no new
   node). CONVERGENT with v4's rate_half_quadratic_exact_range — two independent
   derivations of the same determination from the same PROVED parent: strong
   cross-validation. Note v5's band text still calls the predecessor witness open on
   B* > B_Q — superseded by v4's (RQ2) universal tangent witness on import (reconcile in
   the merged addendum).
6. **a47b87c0 "Narrow list adjacency to base arity" — SURFACE AS GENUINE STRUCTURAL CHOICE
   (recommend ACCEPT with addenda).** Rewrites list_safe + list_adjacency_closing +
   list_grand statements in place, narrowing the m-quantifier obligations to the ordinary
   code m=1 and delegating arity transport to the master node list_large_m_scope_closure
   (CONDITIONAL: base adjacent crossing => same crossing at every constant arity, via
   master-PROVED list_subsqrt_interleaving_collapse, B*^2 < |F|). Edge-kind demotions
   req->ev {m_handling, m_sweep} -> list_safe and list_adjacency_closing -> list_grand: NO
   discharge-mechanics effect (both demoted parents are PROVED on master, so list_safe's
   gate was and stays all-green-but-held); the change is semantic re-routing, not gate
   weakening. Status of list_safe/list_grand UNCHANGED (CONDITIONAL). Because list_safe is
   key:true, the statement narrowing is a genuine choice: surface to master; the transport
   wiring is coherent and the m=1 reduction is mathematically right by the collapse
   theorem; land as dated addenda (w10-C4), never as replacement.

### Cluster 4 continued — the v5 C36 chain (07baa74c..328c4b5b, 7 nodes + red re-pose)

- **DEPENDENCY CHECK vs unaudited wave-8 Cluster A: CLEAN.** Every req parent of the 7 new
  f3_h3 nodes is either master-PROVED (f3_h2_stepanov_inhouse, f3_h3_quotient_block_
  identity, f3_h3_shifted_product_sidon) or v5-new — v5 branched from master, which never
  imported Cluster A, so NOTHING in this chain depends on it. (Contrast v4's two C36
  satellites — Cluster 5 below.) The chain is independently auditable NOW.
- IMPORT HAZARD (w10-C8): v5 re-mints node id f3_h3_uniform_product_fiber_stepanov — the
  SAME id exists in v4's unaudited Cluster A with different provenance. Import must pick
  ONE (recommend v5's, which is dependency-free and replayed PASS) and record the collision.
- Content (normal-depth + replays, 7/7 PASS with mutation controls): identity-deficit port
  (see Cluster 5 — proof.md/verify.py byte-identical to v4's, statement adds only metadata
  lines); shifted-energy zero normalization (a33aa391 — an ADDITIVE convention bridge
  E_x(S)=E_x(A)+(2n-1)^2, aligning centered/full-shift external sources; NOT a walk-back of
  the ported claim); cubic block tail energy fence (rows=29, honest violations listed);
  uniform product fiber Stepanov (29 official orders); global derivative-ideal valuation +
  cutoff18 double-accident reduction + double-accident derivative ideal: the split X_18 =
  A_18 + Y_18 with A_18 <= (n-1)^2 is exact (my check: 17(n-1)^2 + 283n^2+34n-17 = 300n^2
  on the nose), so the red's sufficient task reduces to 17Y_18 <= 283n^2+34n-17 (every
  positive Y_18 record = simultaneous rich-product AND quotient-collision event — the
  "double accident"); the derivative-ideal node localizes exceptional primes into an
  explicit odd integer f_n with p|f_n iff Y_18>0, honestly recording "the global
  discriminant-height envelope is quantitatively insufficient and a residual-size or
  target-local valuation bound remains open". C36 red STAYS TARGET; its dag statement was
  REPLACED in place 1687->333 chars (records the new pose 17X_18<=300n^2 + banked
  reduction; drops the p-range/history text) — custody w10-C4: master merges as dated
  addendum preserving the p-range sentence.

## CLUSTER 5 — V4 C36 ENERGY ENDPOINT + CODEGREE FENCES + WEIGHT-5 STATE

1. **f3_h3_identity_deficit_energy_close (899326a8 "Tighten C36 energy endpoint") —
   AUDITED SOUND, dependency-clean (req = two master-PROVED nodes).** Claim: with P/R the
   product/quotient fiber counts of A=(1-H)\{0}: sum R(t)^2 = E_x(A) and N_3to1 =
   E_x(A) - (1/2)sum_t (P(t)-R(t))^2 — I re-derived both as pure algebra (quadruple
   bijection dc'=d'c <-> ab=a'b'; expansion of the square). With R(1)=n-1, P(1)<4n^(2/3)
   (Stepanov input), the energy estimate 4E_x(A) <= 145(n-1)^2 implies C36' via the
   identity-coordinate deficit ((143/4)n^2-scale after subtracting (1/2)(n-1-4n^(2/3))^2 <
   36n^2 - 16n^(4/3) - n/2 on all 29 official orders — verifier checks every order with 29
   constant mutations + 3 dag mutations, PASS). This is a strictly weaker sufficient energy
   target than the prior E_x(A) <= 35n^2 (their inequality (145/4)(n-1)^2 > 35n^2 checked).
   It is a REDUCTION (conditional endpoint), not an unconditional close — title
   "Tighten... endpoint" is accurate. IMPORT-CLEAN (both copies; keep v5's port as the
   master file, byte-identical proof/verify).
2. **f3_h3_diagonal_ratio_energy_profile_fence (f4748361) + f3_h3_unordered_newton_prefix
   (bde33876): DEFERRED with wave-8 Cluster A** — their req parents
   (f3_h3_product_fiber_codegree_budget, f3_h3_unordered_derivative_ideal_reduction) are
   Cluster-A nodes ABSENT from master. Characterization: the first is a route fence
   (scalar-codegree route to one shifted-energy problem), the second an arithmetic route
   (Newton prefix of the unordered product multiset over mu_n). Add both to the Cluster-A
   audit queue at the wave-10 pin. Pre-registered expectation: fence direction only (no
   payment); Newton prefix = exact symmetric-function arithmetic replayable in isolation.
3. **Weight-5 (1,5) streaming: DID NOT COMPLETE IN-RANGE.** Zero dli-touching commits in
   4442ffd5..899326a8 (checked by name filter). The worktree holds ONE untracked 2KB file
   dli_wcl_weight5_recursive_norm_full_result.json, mtime Jul 17 16:52 (BEFORE the range
   start — a wave-9-era infra leftover): schema weight5-recursive-norm-full-v2, scope
   "prefix test", status "PARTIAL", covered_rows=128 (of 2,296,920 classes), batch_count=2,
   factor_records=362, max_v2_prime_minus_1=17, two unresolved FACTOR_TIMEOUT_60S cases,
   errors=[]. Nothing to verdict against the pre-registered expectation (pilot max_v2=21
   was from the earlier 60k-line sample; this prefix shows 17; both << 41, consistent-with-
   closure-but-proving-nothing). DEFER continues with wave-9 expectations unchanged.

## CLUSTER 1 — V4 RATE-HALF SAFE-SIDE SUITE (19d19f93..8997e257 + eb553b92) — FULL DETAIL

### The decisive answers (task questions a-c)

**(a) Which ranges now have PROVED safe-side theorems (MCA side; the list side is untouched
by v4 — trigger separation preserved, no surrogate use anywhere in the suite):**

1. `rate_half_quadratic_exact_range` (e86b0b88+568178b8, PROVED): for the official row
   (n=2^41, k=2^40), with B = floor(q/2^128) and B_Q = r_Q+1 = 389,500,552,609
   (r_Q = 3k - floor(sqrt(7 k^2)) - 1 = 389,500,552,608 = largest radius satisfying the
   staircase hypothesis (n-r)^2 >= n(k+r)):
   - (RQ1) for 1 <= B <= B_Q: **a_RH(q) = n - B + 1 with B_mca(a_RH)=B <= B* <
     B_mca(a_RH-1)** — the EXACT adjacent certificate, BOTH halves. Safe half = staircase
     equality; unsafe half = the universal MDS coordinate-tangent lower family (B_mca(n-r)
     >= r+1 at every radius) — i.e. the "new lower family" wave-9's residual leg 3 demanded
     was ALREADY in-repo since wave-6 inside mca_quadratic_prize_rows; v4's contribution is
     recognizing and composing it.
   - (RQ2/RQ3) for all 1 <= B <= k-1: bracket n-B+1 <= a_RH(q) <= n - min(B-1, r_Q).
   - (RQ4) for B_Q < B <= 2^39+1: adjacency at a_0 = n-B+1 is EQUIVALENT to the single
     far-CA bound B_ca^far(a_0) <= B (sparse numerator auto-closed at <= B-1; unsafe side
     universal).
2. `rate_half_sparse_pinning_rigidity` sparse-safe-curve addendum (eb553b92): at a = n-r
   with r <= tau (equivalently r <= (n-k)/2), non-tangent sparse bad slopes are impossible
   (wave-9 PR1: non-tangent forces e >= tau+1 > r >= e) and tangent <= e <= r, so
   S_sparse(n-r) <= r. Explicit curve **a_sp(q) = n - min(2^39, B)**: sparse numerator safe
   there; = 3n/4 for q >= 2^167. HAND-TRACED SOUND (two-line consequence of the wave-9
   audited PR1 + tangent-per-coordinate count).
3. `rate_half_half_distance_safe_bracket` (0b313b01, PROVED, "proof with published CA
   import"): for q >= 2^169, B_mca(3n/4) <= n <= B*(q) via the published unique-decoding
   proximity-gap bound imported by master's mca_from_ca_reduction + the exact MCA
   half-distance theorem. Bracket (HD2): k+8,594,128,896 <= a_RH(q) <= 3n/4 (q >= 2^169).
   Honest scope: "not a self-contained extension of that input; does not reach the
   near-capacity crossing".
4. `mca_full_agreement_endpoint` (19d19f93, PROVED): B_mca(n) = 1 exactly for every proper
   linear code (two bad slopes force both components into C, contradicting non-mutual);
   epsilon_mca(C,0) = 1/q <= 2^-128 iff q >= 2^128 — certifies a safe endpoint on every
   admissible field and (FA2) that the grand threshold is empty for q < 2^128. HAND-TRACED
   SOUND.
5. Structural reductions (no bound asserted, honest nonclaims): `rate_half_far_ca_rider_
   reduction` (ce16a7fc): B_ca^far(n-r) <= 1 + (r+1) L_2(n-2r), at rate half the pair-list
   agreement is exactly 2tau; explicitly "does not assert (RR4) holds".
   `rate_half_far_ca_anchor_pencil_normal_form` (8997e257): exact anchor-pencil
   presentation (AP1)-(AP3) of non-anchor bad slopes with UNIQUE witness codeword when
   2r < d_min (holds on the whole unresolved range r <= 2^39 vs d_min = 2^40+1) — the
   entry point for the Cluster-2 Hankel suite. Both HAND-TRACED SOUND (AP2's lower bound
   from column-farness, AP3's pigeonhole, uniqueness re-derived).
6. `rate_half_postquadratic_mds_extension_fence` (d4e37c9a, PROVED counterexample): at
   (n,k,q)=(4,2,5) a column-far pair with FOUR CA-bad slopes at the first post-quadratic
   radius r=1 (4 > r+1 = 2) — the staircase equality is NOT MDS-universal beyond the
   quadratic range; any official extension must use the long smooth domain. I reproduced
   the counterexample with my own code (w10_checks: 4 slopes, column-farness both
   components, margin -3). Honest fence.

**(b) Is the crossing DETERMINED anywhere / what bracket exists:** YES — decisively more
than at wave-9:
- **DETERMINED (unconditional, exact, field-dependent): every admissible
  2^128 < q < (B_Q+1)*2^128 = 132540169959144315698788704090115531231543332700160
  (~2^166.502834419), by the closed formula a_RH(q) = n - floor(q/2^128) + 1.** This is
  exactly the (RH-ADJ) deliverable on that range. The wave-6 certified rate-half prize row
  p (B = 389,500,552,609 = B_Q exactly) is the LAST determined field — coherent.
- **DETERMINED (now FULLY AUDITED end-to-end via Cluster 2): every admissible
  2^128 < q < 2^167 (exclusive), i.e. all budgets B <= 2^39-1.** Composition, each leg
  audited: RQ1 covers B <= B_Q (Cluster 1); (RQ4) reduces B_Q < B <= 2^39+1 to the single
  far-CA bound (Cluster 1); the Hankel suite's UNCONDITIONAL layer B_ca^far(n-r) <= r+1
  for every r <= 2^39-2 supplies exactly that bound through B = 2^39-1 (Cluster 2,
  hand-traced + replayed); RQ2's universal tangent family supplies the unsafe side
  (Cluster 1). The composition BYPASSES wave-9's PR4 q >= 2^168 tangent caveat entirely
  (sparse side auto-closed at <= half distance below 2^167 — no gap). The Hankel report's
  w10-H4 conditionality (on rate_half_quadratic_exact_range) is discharged by this
  cluster's audit; w10-H1: the "through 2^167" title is exclusive — budget 2^39 (= q in
  [2^167, 2^167+2^128)) is OPEN.
- BRACKETS beyond: a_RH(q) in [k+8,594,128,896, n] for all admissible q (FA3);
  sharpened to [k+8,594,128,896, 3n/4] for q >= 2^169 (HD2).

**(c) Exact residual of rate_half_band_closure (RH-ADJ) after this suite (at v4 pin,
band statement + my verification):**
- Budgets B in {2^39, 2^39+1} (q in [2^167, (2^39+2)*2^128)): far-CA moving-kernel Hankel
  profiles — CONFIRMED by the sub-audit as exactly: B=2^39 strict A=3, s=0,
  e in [2^37, floor((2^39-1)/3)]; B=2^39+1 A=3 with e >= 2^37+1 plus the A=1 rows (ERC6).
- B > 2^39+1 (q above ~2^167.000...): BOTH numerators open again at near-capacity
  candidates; only the brackets above; the far-CA obligation reduced structurally to the
  deficient interleaved pair list L_2(2tau) with rider price r+1 (bounding L_2(2tau) or
  sharpening the rider is the posed open work), plus the anchor-pencil object; the sparse
  side for q >= 2^168 reduced to the coupled non-tangent system (PR1)-(PR3) (wave-9), and
  fully safe only along a_sp(q).
- The node correctly stays TARGET; falsifier preserved; the conjectural corridor map
  explicitly disclaimed as an optimality certificate.

### (d) Hand-traces, replays, constants

- Hand-traces: full-agreement endpoint, sparse safe curve, anchor-pencil (AP1)-(AP3) +
  uniqueness, rider reduction (normal-depth; the 2r-translation + per-pair rider), and the
  quadratic-range composition (staircase equality at r=B-1 + universal tangent at r=B +
  sparse auto-close for B <= 2^39+1 + the split identity) — ALL SOUND. The heavy lifting
  ((QMS) itself) is master's wave-6 PROVED mca_quadratic_prize_rows (upstream source
  przchojecki/rs-mca@9262f63c) — dependency is an in-repo PROVED theorem, NOT planning
  prose; no conjectural input anywhere in the chain.
- Verifier replays (ramguard tiny, pinned mini-tree): 7/7 PASS —
  mca_full_agreement_endpoint (exhaustive toy incl. exact support-wise mutual semantics via
  subset enumeration; maxima=[2,2,1]); rate_half_quadratic_exact_range (two-sided margin
  asserts at r_Q/r_Q+1, exclusive-endpoint division both sides, toy staircase sweep with
  predicted==max(admissible)); rate_half_half_distance_safe_bracket
  (agreement=1649267441664 radius=2^39 budget=2^41); rate_half_far_ca_rider_reduction
  (rows=(24,2),(504,3)); rate_half_postquadratic_mds_extension_fence (maximum=4,
  exhaustive histogram); rate_half_far_ca_anchor_pencil_normal_form (anchors=4
  presentations=12); rate_half_sparse_pinning_rigidity updated verify (same wave-9 counts
  + NEW safe-curve arithmetic block added by eb553b92 — the new claim IS machine-checked).
- Independent constants (w10_checks.py, 25/25 PASS, own code): isqrt(7k^2) two-sided; r_Q,
  B_Q, exclusive endpoint (exact integer + log2 = 166.502834419); wave-6 row budget == B_Q,
  n | p-1, row < endpoint; staircase margins +5,154,112,775,168 / -663,955,886,271
  two-sided; bracket coherence n-B_Q+1 >= k+sigma_0+1; sparse-auto boundary B <= 2^39+1
  tight both sides; 2^167 and 2^169 budget boundaries two-sided; 3n/4 constant; full fence
  counterexample replay; own exhaustive RS(4,1,F_5) staircase toy (B(4)=1, B(3)=2=r+1).

### (e) Arc check: CLEAN

No claim weakened or reverted in-range: zero status flips in the entire v4 range; all six
statement-field changes on the suite are strengthenings/honest-scoping additions; the only
deletions in rate_half_band_closure/statement.md are the 5 lines of the wave-9 "Attack
surface" guidance paragraph, superseded by the new results (content-forced; custody form =
dated addendum on import, w9-C1 pattern continues — w10-C5). QUALITY.md: not modified in
this range (checked via diff stat). The "Close" titles of e86b0b88 etc. are, for once,
backed: nothing walks them back in-range.

### Custody (cluster 1)

- w10-C5: v4 edits master-shared critical/nodes/rate_half_band_closure/{statement.md
  (+334/-5), proof.md (+392/-6)} — near-append; on master both land as ONE dated
  "QUADRATIC EXACT RANGE + SAFE CURVE + BRACKETS (wave-10 audited)" addendum; the 5 deleted
  guidance lines stay in master's text with a superseded note.
- New node folders (6 x 6 files, background/) IMPORT-CLEAN verbatim; eb553b92's
  sparse_pinning_rigidity deltas (statement/proof/claim_contract/verify) are addenda on the
  wave-9-imported node.

## CATCHES (running)

- w10-C1 (REFUSAL): v5 143de622 packaging CONDITIONAL->PROVED — refused; mechanism = gate
  expansion (373bbc56 req edge descriptor->packaging, reversing master's ev-demotion) +
  claim narrowing (packaging statement rewritten in place) + manual proof.md close.
- w10-C2 (flip refusal, content split): descriptor TARGET->PROVED refused as a status flip
  (genuine close candidate — surface to master with recommendation; the tool + proposition
  + verifier are importable content).
- w10-C3 (master-side latent, mirrors w8-C10): master's own tools/auto_discharge.py writes
  discharge/regression artifacts to nonexistent tools/../nodes/ — the advertised regression
  rule is dead code on master too. Fix path to background|critical/nodes/.
- w10-C4 (custody): v5 in-place rewrites of master dag statements + node files (harness,
  dossier_partial, compiler, packaging, descriptor, list_safe, list_adjacency_closing,
  list_grand, rate_half_band_closure 8231->395 chars, rate_half_cyclic_rotated_prefix_floor,
  rate_half_cyclic_simple_pole_mca_floor, f3_h3_mobius_excess_half 1687->333) — ALL land as
  dated addenda on import, master text preserved.
- w10-C5 (custody, cluster 1): v4 near-append edits of master-shared
  rate_half_band_closure/{statement.md +334/-5, proof.md +392/-6} — one dated addendum on
  import; the 5 deleted wave-9 guidance lines stay with a superseded note (w9-C1 pattern).
- w10-C6 (genuine choice, surfaced): v5 a47b87c0 narrows list_safe/list_adjacency_closing/
  list_grand to base arity m=1 with transport delegated to list_large_m_scope_closure
  (req->ev demotions of two PROVED parents; no discharge-mechanics effect; statuses
  unchanged). Mathematically coherent via master-PROVED list_subsqrt_interleaving_collapse.
  RECOMMEND ACCEPT as dated addenda; never silently.
- w10-C7 (custody, minor, w9-C5 pattern): v5 1e26255b edited a PRIOR QUALITY.md block of
  rate_half_band_closure in place (old sigma_max constant line deleted). Restore + append
  on import.
- w10-C8 (import hazard): node-id COLLISION f3_h3_uniform_product_fiber_stepanov — v5's
  new dependency-free node vs v4's unaudited wave-8 Cluster A node of the same id.
  Import exactly one (recommend v5's, replayed PASS); record the collision in the
  Cluster-A audit queue.
- w10-H1..H5 (Hankel sub-audit, see w10_hankel_report.md): H1 "through 2^167" is
  exclusive-boundary-loose (budget 2^39 open); H2 band_closure append-only letter
  violation (3 pre-suite lines rewritten + in-place edits of same-suite text; all
  strengthenings — addendum repair on import); H3 endpoint-chain verifiers check integer
  ledgers only, algebra is hand-proof (disclosed in-node); H4 q-range headlines
  conditional on rate_half_quadratic_exact_range — DISCHARGED by Cluster 1 of this audit;
  H5 the seven endpoint nodes rigidify the failing profile but do not shrink the open
  budget set — do not read as coverage progress.
- w10-X1..X4 (XR sub-audit, see w10_xr_report.md): X1 in-place rewrites of P-A red's
  frontier/claim_contract/dependency_subdag (w8-C7 pattern, addenda on import; no auditor
  notes touched); X2 pre-existing stale "16,16,15" claim_contract line vs 17,17,15 of
  record — fix on master; X3 ledger summaries drop the syzygy node's selected-block/
  defined-color hypotheses (wording only); X4 quotient verifier's residual-profile check
  decorative (real derivation machine-checked in the atlas verifier).

## IMPORT SURGERY SPEC (exact; statements MERGED never replaced; v4 content at pin
899326a8, v5 content at pin d5a89194; master deps all verified PROVED:
mca_quadratic_prize_rows, mca_from_ca_reduction, rate_half_mca_sparse_layer_reduction,
rate_half_sparse_pinning_rigidity, rate_half_cyclic_simple_pole_mca_floor)

### Ordering constraint

Land A (v4 rate-half) and C (v5 rate-half) in ONE master session: both rewrite the same
rate_half_band_closure statement narrative and the two floor nodes; a single merged dated
addendum must reconcile them (v4's determined slice + universal predecessor witness
supersedes v5's "predecessor witness open" sentence; v5's k+2^34 floor supersedes v4's
k+8,594,128,896 bracket lines).

### A. v4 rate-half safe side (Cluster 1)

1. NEW NODE FOLDERS verbatim from 899326a8 (background/nodes/, 6 files each):
   mca_full_agreement_endpoint, rate_half_half_distance_safe_bracket,
   rate_half_far_ca_rider_reduction, rate_half_quadratic_exact_range,
   rate_half_postquadratic_mds_extension_fence, rate_half_far_ca_anchor_pencil_normal_form.
   Dag: 6 PROVED entries + edges as at pin: {mca_full_agreement_endpoint -> band ev;
   mca_from_ca_reduction -> half_distance_safe_bracket req; half_distance_safe_bracket ->
   band ev; far_ca_rider_reduction -> band ev; mca_quadratic_prize_rows ->
   quadratic_exact_range req; rate_half_mca_sparse_layer_reduction ->
   quadratic_exact_range req; rate_half_sparse_pinning_rigidity -> quadratic_exact_range
   req; quadratic_exact_range -> band ev; postquadratic_mds_extension_fence -> band ev;
   far_ca_anchor_pencil_normal_form -> band ev}.
2. rate_half_sparse_pinning_rigidity (master node): dated addendum "EXPLICIT SPARSE-SAFE
   CURVE (wave-10 audited)" = the eb553b92 statement/proof/claim_contract deltas; verify.py
   updated to the pin version (adds the safe-curve arithmetic block).
3. rate_half_band_closure: ONE dated addendum "QUADRATIC EXACT RANGE + SAFE BRACKETS +
   OPTIMIZED FLOOR (wave-10 audited)" carrying: v4's statement.md/proof.md additions (incl.
   the exact-range section, safe-side reduction narrative, Hankel section PER CLUSTER-2
   VERDICT), the 5 superseded wave-9 guidance lines marked superseded not deleted, v5's
   band statement content (staircase slice + k+2^34 floor), and the reconciliation
   paragraph. Dag statement: append per house convention.
4. tools/verifier_manifest.json entries for the 6 new + 1 updated verify.py.

### B. v4 Hankel suite (Cluster 2) — IMPORTABLE (sub-audit verdict: IMPORT-CLEAN)

12 node folders verbatim from 899326a8 (background/nodes/rate_half_ca_hankel_*/), dag: 12
PROVED entries + the 20 edges at pin (internal req chain + 12 ev into
rate_half_band_closure; req from rate_half_quadratic_exact_range into
minimal_index_budget), manifest lines; the band statement Hankel paragraphs ride A.3's
addendum with the w10-H2 letter-repair (the 3 rewritten pre-suite "Remaining proof" lines
restored + superseded-note). Import note per w10-H5: the seven endpoint nodes must NOT be
read as q-axis coverage progress (they rigidify the residual profile at strict budget e=m
only); per w10-H1 record the open budgets as {2^39, 2^39+1} explicitly.

### C. v5 rate-half list suite (Cluster 4)

1. NEW NODE FOLDERS verbatim from d5a89194: critical/nodes/rate_half_list_adjacent_crossing
   (TARGET pose; the w9-C3 repair vehicle), background/nodes/rate_half_list_integer_
   johnson_safe_anchor, background/nodes/rate_half_list_low_budget_exact_crossing. Dag: 1
   TARGET + 2 PROVED + edges {cyclic_floor -> list_adjacent_crossing ev;
   list_adjacent_crossing -> list_adjacency_closing req; cyclic_floor -> johnson_safe_anchor
   req; johnson_safe_anchor -> list_adjacent_crossing ev; johnson_safe_anchor ->
   low_budget_exact_crossing req; low_budget_exact_crossing -> list_adjacent_crossing ev}.
2. Cyclic floor optimization (1e26255b): import the re-instantiation as dated addenda on
   the two master floor nodes (statement/proof/verify updated to pin versions — verify.py
   changes are strengthenings; hashes on repaired statements); w10-C7 QUALITY repair
   (restore deleted constant line + append); band handled in A.3. The k+2^34 reach
   REPLACES sigma_0 as the bracket constant everywhere forward-facing, with sigma_0 kept
   as history (forced-corrections authority: this is a proved constant improvement — apply
   directly, note in log).
3. a47b87c0 base-arity narrowing: dated addenda on list_safe/list_adjacency_closing/
   list_grand/list_large_m_scope_closure conditional+statement files recording the m=1
   re-scoping + transport delegation; edge-kind changes applied WITH the addenda (w10-C6
   surfaced choice, recommend ACCEPT); statuses untouched.
4. w9-C2/C3 correction addenda (from wave-9 spec) can now cite the NEW owner: the list
   safe side is owned by rate_half_list_adjacent_crossing; unsafe side proved through
   excess 2^34-1; crossing determined for B* in {1,2} (list) — update the correction text
   accordingly.

### D. v5 C36 chain (Cluster 4)

7 node folders verbatim (background/nodes/f3_h3_{identity_deficit_energy_close,
shifted_energy_zero_normalization, cubic_block_tail_energy_fence,
uniform_product_fiber_stepanov, global_derivative_ideal_valuation,
cutoff18_double_accident_reduction, double_accident_derivative_ideal}) + dag PROVED
entries + edges as at v5 pin. f3_h3_mobius_excess_half: dated addendum = the new pose
(17X_18 <= 300n^2 + Y_18 reduction) APPENDED to master's 1687-char statement (p-range
preserved); attack/frontier/source_scope_audit deltas as addenda. w10-C8 collision
recorded. (v4's identity_deficit copy is subsumed — same proof/verify bytes.)

### E. v5 packaging/descriptor (Cluster 4) — REFUSALS + content

- REFUSE both status flips (packaging stays CONDITIONAL, descriptor stays TARGET on
  master).
- IMPORT as content: tools/prize_row_descriptor.py + descriptor/{verify.py, proof.md,
  statement/artifact_audit/frontier deltas as addenda} + compiler/harness/dossier_partial
  audit.py improvements + tools/build_incremental_verifier_replay.py + the
  incremental_verifier_replay.json artifacts (fail-closed replay infrastructure — useful).
- SURFACE: the descriptor-close recommendation (flip descriptor after master review);
  the descriptor->packaging edge as ev NOT req (master's demotion note stands); the
  packaging statement narrowing (theorem counts provenance-pinned) as a proposal.
- Fix w10-C3 on master (auto_discharge artifact path) regardless.

### F. v4 XR suite (Cluster 3)

5 node folders verbatim + 16 edges at pin + manifest lines; w10-X1 custody addenda on the
P-A red's frontier/claim_contract/dependency_subdag; fix w10-X2 stale "16,16,15" line;
frontier ranks/records unchanged (no residual text rewrite needed beyond the partial-pay
crosswalk note into the rank-2 chart audit item).

### G. Deferred

- v4 f3_h3_diagonal_ratio_energy_profile_fence + f3_h3_unordered_newton_prefix: Cluster-A
  audit queue at wave-10 pin.
- Weight-5 (1,5): no import (no claims); expectations unchanged.
- Full re-audit of mca_quadratic_prize_rows internals if the exact range ever needs
  hardening beyond master's wave-6 audit (currently trusted baseline).

## PROCEDURAL LOG

- One compute-law slip early: a bare `python3` heredoc JSON parse (packaging parent listing)
  — flagged, no incident; all subsequent Python under tools/ramguard tiny from scratchpad,
  heavy on Modal.
- Deliverables: w10_findings.md (this file), w10_checks.py (25/25 PASS — cluster-1
  constants + own-convention exhaustive MCA toy + fence counterexample replay),
  w10_v5checks.py (v5 floor/Johnson constants — ALL PASS), w10_dag_delta.py +
  w10_dag_delta_output.txt + w10_dags/{v4,v5} (52 per-commit dag dumps), w10_depstat.py +
  w10_c36dep.py (dependency forensics), w10_tree/ + w10_tree_v5/ (pinned replay
  mini-trees; 7 v4 + 13 v5 verifier replays ALL PASS), w10_hankel_report.md (Cluster 2
  sub-audit, 12/12 PASS), w10_xr_report.md (Cluster 3 sub-audit, 5/5 PASS).
- Sub-audits ran as background agents with the same read-only/pin/ramguard laws; their
  reports live beside this file and their catches are merged above (w10-H*, w10-X*).
