# Wave-16 fresh-context replay audit — v7 full-prize-resolution (DSP8 pair + HGE4 shift-pair + rate-half fiber-two + XR fences + C36/H3 compilers + governance)

Auditor session 2026-07-20. Catch numbering LOCAL (w16-C#). READ-ONLY both
repos. INCREMENTAL — written as the audit proceeded. Deliverables live beside
this file; temp/scripts under scratchpad prefix `w16_`.

## PINS

- **v7**: /home/u2470931/smooth-read-solomin/prize-codex-resolution-v7-20260719,
  branch codex/full-prize-resolution-v7-20260719. HEAD pinned at audit start =
  **cd1f6407** ("Route matched cycle lifts to the prime field"). All reads via
  the pinned archive tree `scratchpad/w16_tree/` (git archive cd1f6407;
  dag.json sha256 **9f0d7ed5...** verified against `git show`).
- **base** = wave-15 pin **5661ba51** ("Add DSP8 joint-star depth Pareto
  compiler"); dag.json sha256 **2a2b9087...** (matches wave-15's recorded pin
  hash exactly — base == wave-15 pin).
- **master**: /home/u2470931/smooth-read-solomin/prize, HEAD **04d4e6f4**
  (KB #105 upstream-PR crosswalk). 934 nodes. merge-base(master,pin)=
  **e59a2998** (same as wave-15). Scope = base..pin = **21 commits**.

### PROVENANCE (separating Codex-original from merged-master)
- **master HEAD 04d4e6f4 is NOT an ancestor of the pin** (merge-base=e59a2998).
  b1362c51 ("upstream PR crosswalk banked (KB #105)...") is a **linear
  re-expression** of master's KB-#105 commit onto the v7 base (patch-id
  b103a740 vs master's a14a7890 — different), NOT a git merge. It touches ONLY
  `notes/kernel_basis/KB_LOG.md` + `notes/.../upstream_pr_proposals_20260720/*`
  — **0 node folders, 0 dag change**. Import-neutral.
- Genuinely NEW-to-master node set = **14** (verified: master 934 -> pin 948,
  0 removed; base 934 -> pin 948 identical add-set). All 14 PROVED.

## VERDICT LINE (headline)

**NOTHING CLOSES. NO CRITICAL-SURFACE EVENT.** Every key consumer keeps its
status at EVERY one of the 21 commits (per-commit scan): the C36 amber
`f3_h3_mobius_excess_half` stays **CONDITIONAL**; the DSP8 leaf
`f3_h3_dsp8_correlation_bound` (14 ev in, **0 req**), `f3_hge4_norm_gate_count`,
`rate_half_list_adjacent_crossing`, `xr_tangent_support_mismatch_bridge`,
`xr_highcore_collision_count`, `xr_lowcore_spread_heart`,
`f3_h3_official_order_template_survivor` all stay **TARGET**; prize / mca_grand
/ list_grand / list_safe / packaging all **CONDITIONAL**. The 14 new nodes are
genuine PROVED support theorems wired **ev-only** into their TARGET/CONDITIONAL
consumers — sound reductions / route-fences / generator compressions that
prove NONE of the residual bounds. **Import-eligible YES** as a reduction
layer; the wave-15 LANE-B import-blocker (w15-H1) is now **REPAIRED in-branch**
(commit 370fe902) and the fiber-two pose-pair travels same-commit — this batch
is pose-consistent (adjacent_crossing verify.py returns PASS at pin).

- **DSP8 PAIR — REDUCES/FENCES, closes nothing, not the max-P<=24 satellite.**
  - `f3_h3_dsp8_nodal_stepanov_constant_barrier` (PROVED, ev->correlation_bound):
    a **proof-method BARRIER**. Proves the one-auxiliary-polynomial Stepanov
    ansatz has an intrinsic constant floor `2^(5/3)` (NSB1-2), so the
    class-blind three-cubic-root nodal envelope has leading coefficient
    `17*32*3^(4/3) > 2176 > 76599/40` (NSB4) — NO retune of A,B,D can fit the
    live `G=4K` DSP8 allowance. Verbatim: "This is a proof-method barrier, not
    a lower bound on the actual nodal record count and not a counterexample to
    DSP8." Discharges the w15-D2 residual as a genuine route-block; prunes the
    nodal-Stepanov route (must instead use target/richness/signed-disjointness/
    trace-distribution/multi-fiber).
  - `f3_h3_dsp8_smooth_trace_substar_router` (PROVED, ev->correlation_bound AND
    ev->official_order_template_survivor): a **structural candidate
    compression**. Nodal edges have max degree 3 (SSR1), so a degree-d product
    star contains a smooth-trace substar of degree >= max(d-3,0); the preferred
    (35,2) packet's degree-8/6 stars carry smooth degree-5/3 substars (elliptic
    curves), and the candidate ideal may be saturated by nonzero trace
    discriminants without losing a survivor. Verbatim: "It does not bound the
    number of smooth templates, their prime divisors, or the quotient-weighted
    DSP8 moment."
  - **NOT the max-P<=24 satellite** (the (P,R) joint-star-depth corners 25..35
    are a different coordinate from the richness P; F-round-1 richness-P=20<25
    census is dated 2026-07-19, pre-range, and is preserved verbatim, not
    re-run). **EXACT RESIDUAL unchanged**: an unconditional bound on the
    disjoint primitive-shift-pair correlation `10K_25^0+17K_25^A` (equivalently
    any one of DSP8 / DSP8-U / a JDP corner / FM 680M_21 / accident-depth
    exclusion). The barrier now additionally proves the nodal-Stepanov route
    cannot deliver it; the substar router compresses the (35,2) candidates.
    Neither is the bound.
  - **C36/H3 compiler trio** (`f3_h3_global_resultant_compression`,
    `f3_h3_cutoff_layered_gcd_compiler`,
    `f3_h3_quotient_algebra_fitting_support_compiler`; all PROVED, all
    ev->mobius_excess_half CONDITIONAL): honest **algorithmic compressions of
    the fixed-order C36' route**. (i) global product/quotient polynomials are
    resultants of the binomial `F_n(X)=((1-X)^n-1)/X` (GRC1-4) — no d^2 root
    enumeration; (ii) a quotient-lift-free layered-Hasse-gcd row compiler for
    the exact `X_18`,`Y_18` (LGC3), truncated to `B_n=O(n^(2/3))` live layers;
    (iii) a Fitting-integer / scalar-annihilator candidate-prime support
    compiler (QAF4-9). Each disclaims: "does not bound either moment / no
    official-scale algorithm." Residual = a succinct official-scale
    recurrence/modular-resultant/Smith method that ALSO aggregates the
    quotient-lift index with proved coverage+cost (the CR-001 fixed-order
    lane). Commit 5f2d43f8 ("Compress...to annihilators") is a sound
    simplification (smaller scalar annihilator output; verify PASS).

- **HGE4 SHIFT-PAIR TRIO — REDUCES `f3_hge4_norm_gate_count`, no closure, no
  smuggled poses.** norm_gate_count had in-degree 0 on base; the 3 routers are
  its FIRST evidence edges (all ev). No flip (stays TARGET).
  - `..._aggregate_adapter`: exact primitive-shift-pair interface; the finite
    target `SP_h^prim<=7000n max(1,B_h)` (PSA3) is SUFFICIENT (=> sum
    N_h^strip<14n^3). Verbatim: "proves the reduction and summation compiler,
    not (PSA3) itself, and it **creates no new conditional DAG premise**."
  - `..._orbit_aggregate_router`: `SP_h^prim=n O_h^prim`; stronger orbit
    aggregate `sum O_h^prim<=14n^2` (OAR2) suffices. A **route-separation**
    (analogue of the DSP8 barrier): the naive uniform-per-support bound can
    meet PSA3 only at zero (OAR4) — "This is a route separation, not a claim
    that primitive shift pairs are empty."
  - `..._near_square_union_router`: bijection unordered-pair <-> valid
    near-square union; exact scanner reduction factor `binom(2h-1,h-1)`
    (NSU7); "complete fixed-row generator reduction. It does not prove (NSU4)
    or supply a uniform finite-row census." **Residual: prove any of PSA3 /
    OAR2 / NSU5 — "the uniform aggregate remains open."** New sufficient
    targets are ev-only currencies, NOT req premises (no smuggle).

- **RATE-HALF BUDGET-3 FIBER-TWO (4 nodes) — REDUCES the fiber-two branch,
  closes NO chamber; pose-pair CONSISTENT (w15-H1 fixed).** All 4 ev->
  adjacent_crossing (in-degree 67->71). `path_exclusion` excludes direct
  equal-complete-fiber PATH constructions of common fiber size m>=2 (with the
  Vandermonde exclusion) — "removes one exact small-fiber case. It does not
  close the budget-three branch" (m=1, mixed-map, partial-fiber, primitive
  remain; four-cycle remains live). `cycle_quotient_embedding` reduces the
  common-X^2 four-cycle to an exhaustive three-way **quartic-pencil router**
  c in {0,1,2}: c=0 embeds in the existing antipodal census, c=1,2 are
  **denominator-mismatch** strata that stay separate — "The theorem proves
  none of these censuses empty." `cycle_boundary_transfer` + `matched_lift_
  field_router` continue the reduction (reverse-residual deg-T ledger; matched
  c=0 lifts descend to the prime field, surviving field degree 2). **No
  budget-3 chamber is CLOSED**; adjacent_crossing stays TARGET, B*>=3 nonclaim
  ("Budgets one and two are exact; the adjacent crossing remains open for
  B*>=3") survives verbatim (verify PASS).

- **XR FENCES (2 nodes) — machinery + honest narrowing; #158-consistent;
  frontier UNCHANGED.** Both ev->xr_tangent_support_mismatch_bridge (TARGET).
  `xr_mismatch_descent_dimension_area_law`: an exact **dimension-budget descent
  monovariant** (XDA1-6; long chains forced low-dimensional; caps table at the
  6 clean-rate roots). #158-consistent: "does not bound branch multiplicity,
  slopes per explanation, or generic-chart slope unions" (bounds explanations/
  dimension, not slopes — which is exactly why the bridge stays open).
  `xr_nongeneric_support_only_exponential_width_fence`: a **route fence** —
  abstract A-subset families with the exact `|Y∩Y'|<=K-1` cap exceed `16n^3`
  (binary Gilbert, `>2^(5A/8)`, XEF2-3), so support-packing alone cannot close
  the residual before the terminal Plotkin window; needs RS realization /
  first-match ownership / actual-slope fibers. Verbatim: "route fence...(XEF2)
  is not a counterexample to xr_tangent_support_mismatch_bridge." Frontier
  ranks (5,5,5 / 17,17,15) untouched — xr_highcore_collision_count /
  xr_lowcore_spread_heart stay TARGET (unchanged base->pin).

## DAG-DELTA (w16_dag_delta.py / w16_delta2.py; master 04d4e6f4 vs pin cd1f6407)

- Nodes **934 -> 948 (+14, 0 removed)**; ALL 14 added are **PROVED** (0 TARGET,
  0 REFUTED, 0 CONDITIONAL). REFUTED total 26==26 (no new refutation).
- Edges **1990 -> 2045 (+55: 54 add + the 3 wave-15-carryover kind-changes /
  wait: base->pin = +54 add, 0 remove, 0 kind-change)**. vs master the 3
  req->ev kind-changes are **wave-15 carryover** (w15-C1, NOT wave-16 — see
  below).
- **STATUS FLIPS among shared nodes: 0** (net AND per-commit — w16_keystat.py
  over all 21 commits: every gate node CONDITIONAL, every target consumer
  TARGET at every commit; node count monotone 934->948). **No auto_discharge /
  packaging / list_safe flip anywhere.**
- **14 added nodes by cluster**: DSP8 pair 2 (`f3_h3_dsp8_nodal_stepanov_
  constant_barrier`, `f3_h3_dsp8_smooth_trace_substar_router`); C36/H3
  compilers 3 (`..._global_resultant_compression`, `..._cutoff_layered_gcd_
  compiler`, `..._quotient_algebra_fitting_support_compiler`); HGE4 3
  (`f3_hge4_primitive_shift_pair_{aggregate_adapter,orbit_aggregate_router,
  near_square_union_router}`); rate-half fiber-two 4
  (`rate_half_list_budget_three_fiber_two_{cycle_boundary_transfer,cycle_
  matched_lift_field_router,cycle_quotient_embedding,path_exclusion}`); XR 2
  (`xr_mismatch_descent_dimension_area_law`, `xr_nongeneric_support_only_
  exponential_width_fence`).
- **4 shared/consumer statement changes (wave-16-specific, base->pin)**:
  `f3_h3_dsp8_correlation_bound` (inline dag stmt 1772->1885, 6->11 corners +
  the (34,3) row; FALSIFIER + F-round-1 census preserved verbatim; TARGET,
  NO verify.py); `f3_h3_dsp8_joint_star_depth_pareto_compiler` (PROVED, in-place
  near-total rewrite 6->11 integer corners, m_E=7+ceil((E+1)/2); verify.py
  re-verifies corners=11 same-commit — w16-C1); `f3_h3_official_order_template_
  survivor` (TARGET, 6->11 corners + smooth-leaf content; no verify.py);
  `xr_tangent_support_mismatch_bridge` (TARGET, open-content refinement +
  DATED notes append 2026-07-20; no verify.py).
- The 12 OTHER shared statement changes seen vs master (f1_case_tower,
  l1_mixed_petal_amplification, list_*, xr_smallcore_spread_count, etc.) are
  **wave-15 carryover** (master imported them as dated addenda so its bytes
  differ) — they are IDENTICAL base->pin, NOT touched by wave-16.

## INTEGRITY (all PASS)

- **Structural validator** (repo's own `tools/verify_prize_dag.py`, run on the
  pinned tree): **PASS — "structure, refs, acyclicity, reachability, status
  propagation"**. 948 nodes / 2045 edges; status counts CONDITIONAL:41,
  CONJECTURE:15, PROVABLE:27, PROVED:764, REFUTED:26, TARGET:68, WALL:7. 26
  REFUTED, NONE a req-child; no PROVED node with an unproved req child => no
  smuggled discharge. (Pre-existing informational warnings — 31 status-artifact
  gaps, 9 artifact-kind nodes — are OLD node ids, not wave-16, validator still
  PASS rc=0.)
- **Manifest** (w16_manifest.py): verifier_manifest.json = **1488 entries, 0
  missing, 0 stale**; every one of 618 on-disk verify*.py is listed (0 unlisted
  — no fail-open coverage gap). remote_launchers = **10, unchanged** master/
  base/pin.
- **Wiring / no smuggled poses** (w16_extparents.py): **28 external req/alt
  parents feed the 14 new nodes; ALL 28 PROVED on master** (0 absent, 0
  non-PROVED, 0 REFUTED/CONDITIONAL/TARGET). Unconditionality CLEAN.
- **Replays 42/42 PASS** (14 nodes x {verify.py + verify_audit.py} = 28, ALL
  carry both — NO lane asymmetry, unlike wave-14/15; + the touched consumer/pin
  set: adjacent_crossing, norm_gate_count, mobius_excess_half compiler,
  nodal_cube_preimage_envelope, joint_star_pareto_compiler, uniform_product_
  fiber_stepanov, unit_trace_elliptic_curve_router, affine_coset_pair_stepanov).
  All via `ramguard tiny` against the pinned tree, absolute paths.
- **THE wave-15 HARD FAILURE IS FIXED**: `rate_half_list_adjacent_crossing/
  verify.py` returns **`"status": "PASS"`** at pin — `brackets_are_evidence`
  ok, 71 expected == 71 incoming (67 wave-15 + 4 fiber-two), B*>=3 nonclaim
  intact. Commit 370fe902 added the 8 missing wave-15 LANE-B bracket entries
  (the exact w15-H1 repair); each fiber-two commit added its own bracket entry
  same-commit as its statement.md (KB #90 pose-pair honored).
- **Mutation controls 6/6 TRIP** (w16_mutate.py on scratchpad tree copy):
  M1 flip req-parent nodal_cube_preimage_envelope PROVED->TARGET => barrier
  verify AssertionError; M2 flip barrier own status => trip; M3 delete one
  fiber-two ev edge => adjacent_crossing brackets_are_evidence FAIL; M4 flip
  fiber-two node PROVED->TARGET => adjacent_crossing fiber_two_*_is_proved
  FAIL; M5 flip global_derivative_ideal_valuation PROVED->TARGET (child
  PROVED) => `verify_prize_dag` FAIL status-prop; M6b remove HGE4 marker
  `SP_h^prim<=7000n` from packet => aggregate_adapter verify AssertionError.
  (M6-first attempt — a single-file single-occurrence "7000" edit — did NOT
  trip because markers are pinned against the CONCATENATION of all packet .md;
  wave-14 A-O1 recurrence, hygiene not soundness — see w16-C4.)

## CATCHES (all LOW / INFO — no refusal warranted)

### w16-C1 (#104 + w15-D4/C5 recurrence, LOW) — 57d4405f "Extend DSP8 Pareto compiler to all integer corners"
`f3_h3_dsp8_joint_star_depth_pareto_compiler` (PROVED) statement is an
**in-place near-total rewrite** (common prefix 4 of 564 -> 644): 6 corners
(E in {6,8,10,12,14,16}) -> **11 integer corners** (6<=E<=16), with
`m_E=8+E/2` -> `m_E=7+ceil((E+1)/2)` and the odd-E rows interpolating the
next-even row's constants. This STRENGTHENS a PROVED node. **verify.py +
verify_audit.py were updated in the SAME commit** and re-verify the
strengthened claim (`corners=11 endpoint=319/153`, `profiles=529056`; replay
PASS). Non-claim PRESERVED and updated: "This theorem offers eleven
alternatives... It proves none of the moment estimates (JDP4) or (JDP5),
supplies no template generator, and gives no survivor count." IMPORT: master
carries the 6-corner version (wave-15); land the 11-corner statement + verify
pair together (pose-pair), recompute the manifest hash; re-verify on master.

### w16-C2 (#104, LOW) — in-place edits to three no-verifier consumers
`f3_h3_dsp8_correlation_bound` (TARGET leaf, inline dag stmt), `f3_h3_official_
order_template_survivor` (TARGET), `xr_tangent_support_mismatch_bridge`
(TARGET) each got IN-PLACE statement edits (6->11 corner counts + honest
residual refinements), NOT dated appends. None has a verify.py, and NO verifier
(new or existing) pins their changed text => **no same-commit pin constraint**.
Master carries the wave-15 dated-addendum versions (correlation_bound is 2276
on master vs 1885 at pin). IMPORT: land as DATED addenda onto master's text
(preserve master originals as prefix per #104); correlation_bound's FALSIFIER
and the F-round-1 census note are already preserved verbatim at pin.
xr_tangent_bridge's notes change is ALREADY a clean dated append (2026-07-20,
cp=full base length).

### w16-C3 (import hazard — SHARED-node repair, LOW/INFO) — a28a3477 "Repair live DSP8 nodal allowance pin"
Repairs the PRE-EXISTING (on-master) node
`f3_h3_dsp8_nodal_cube_preimage_envelope`: it compared its nodal envelope
constants against the STALE allowance "892" (the superseded J=G F-round
target). Corrected to the **live G=4K allowance `76599/40 = 1914.975`** across
statement.md / result.md / claim_contract.md, added verify.py asserts
(one_root ~551 < 1914.975 TRUE; three_root ~2386 > 1914.975 TRUE) + statement
marker "76599/40=1914.975", retaining "892...as the historical stronger
F-round target". **Math conclusion UNCHANGED** (three-root still exceeds the
allowance; does not close DSP8). IMPORT: this repair must be APPLIED TO
MASTER'S COPY of the node (statement/result/claim_contract/verify.py +
recompute the 2 manifest hashes) — the import is not purely additive.

### w16-C4 (hygiene observation, A-O1 recurrence) — concatenated-substring marker pins
The new-node verifiers pin claim markers against the CONCATENATION of the
packet's .md files (statement+proof+claim_contract+dependency_subdag+audit+
result). A single-file, single-occurrence edit of a redundant constant is not
caught (M6-first); removing the marker from all packet files trips (M6b).
Non-vacuity confirmed; recommend anchored/exact-line asserts at formalization.
Not a soundness defect.

### w16-C5 (governance / #260, standing annotation) — no new launch
`notes/PRIZE_COMPUTE_REQUESTS.md` L17-18 re-asserts the **UNRATIFIED sub-$1
self-authorization** ("an explicitly approved, route-deciding pilot with a
conservative total cost below `$1`; otherwise treat every entry as an outbound
contributor request") — verbatim recurrence of a487c599/b8e9d214 (wave-13/14/
15). A new **pre-request CR-002-C** (next-order cycle shard) is added but
deferred ("theorem/algorithm request only; cost unknown", "no large run should
be launched"). Annotate the sub-$1 baseline as maintainer-unratified at import.

## GOVERNANCE (#260) — CLEAN, no new in-tree launch

- **No Modal launch in range**: every roadmap increment states "no Modal job
  was launched" / "none was launched here" / "handoff rather than launched
  against the current Modal balance." remote_launchers = 10 unchanged. NO
  `*_modal.py` added; NO `result.json` / `*_result.json` artifact added (the
  `result.md` diffs are the standard per-node result.md files).
- **App-ids in range**: `ap-CRn9AwYF0xIGWOsvrDntDM`, `ap-YVuPe20N3lQuwNgedf0h5c`
  appear only in b1362c51's KB-#105 PR-proposal drafts, CITING them as
  historical provenance for an EXISTING verified result — both are
  **pre-existing** (already on base in
  `critical/nodes/rate_half_cyclic_rotated_prefix_floor/result.md`), NOT new
  launches.
- Modal cost figures in range are all deferred estimates ("Do NOT launch",
  CR-004 wclp $1.9k-$14.3k, "3-4 orders above the standing sub-$1") — no
  affirmative "was run/launched" anywhere.

## IMPORT SURGERY SPEC

### A. Import-eligible clusters (import-clean unless noted)
1. **DSP8 pair (2 nodes)** — background/nodes/{f3_h3_dsp8_nodal_stepanov_
   constant_barrier, f3_h3_dsp8_smooth_trace_substar_router} verbatim; ev->
   correlation_bound (both) + ev->official_order_template_survivor (substar).
   Land the correlation_bound / official_order_template_survivor stmt updates
   as DATED addenda (w16-C2). **Apply the a28a3477 repair to the existing
   master node nodal_cube_preimage_envelope in the SAME commit** (w16-C3).
2. **C36/H3 compiler trio (3 nodes)** — background/nodes/{f3_h3_global_
   resultant_compression, f3_h3_cutoff_layered_gcd_compiler, f3_h3_quotient_
   algebra_fitting_support_compiler} verbatim; 3 ev->mobius_excess_half +
   internal req chain; parents all PROVED on master.
3. **HGE4 trio (3 nodes)** — background/nodes/f3_hge4_primitive_shift_pair_*
   verbatim; 3 ev->norm_gate_count + internal req; parents (x81/x82/x83,
   v13_*, f3_shiftpair_weld) all PROVED on master.
4. **rate-half fiber-two (4 nodes)** — background/nodes/rate_half_list_budget_
   three_fiber_two_* verbatim; 4 ev->adjacent_crossing + internal req.
   **POSE-PAIR (KB #90, MANDATORY SAME-COMMIT)**: take the pin
   `critical/nodes/rate_half_list_adjacent_crossing/{verify.py,statement.md}`
   (71-bracket list) with the 4 nodes. Master is at in-degree 67 (it imported
   the wave-15 LANE-B); the swap to the 71-entry pair replays PASS. The
   attack/frontier/dependency_subdag body edits land as dated addenda.
5. **XR fences (2 nodes)** — background/nodes/xr_{mismatch_descent_dimension_
   area_law, nongeneric_support_only_exponential_width_fence} verbatim; 2 ev->
   tangent_support_mismatch_bridge; the bridge stmt refinement as dated
   addendum, the notes block is already a clean dated append.
6. **joint_star_depth_pareto_compiler** — PROVED shared node: land the
   11-corner statement.md + verify.py + verify_audit.py TOGETHER (w16-C1),
   recompute manifest hashes, re-verify on master.
7. **b1362c51 (KB #105)** — notes-only, 0 nodes; import-neutral (already
   master's own work re-expressed).

### B. PRE-IDENTIFIED same-commit couplings the import must land (marker-pin list)
The wave-15 import needed 6 hand-fixes; wave-16 needs only these THREE, and
**NONE is a cross-node or notes/ marker pin** — every new verifier reads ONLY
its own folder + dag.json (the w14-C3 notes-pin hazard does NOT recur):
1. **adjacent_crossing pose-pair** — verify.py (71 brackets + statement_pins_*)
   + statement.md, same-commit as the 4 fiber-two nodes + their 4 ev edges.
2. **nodal_cube_preimage_envelope (SHARED, on-master) repair** — a28a3477's
   statement/result/claim_contract/verify.py + 2 manifest hashes, same-commit
   as the DSP8 pair (its verify pins its own new "76599/40" marker).
3. **joint_star_depth_pareto_compiler pose-pair** — verify.py + statement.md
   (+ verify_audit.py) same-commit (6->11 corners).

### C. Maintainer-ratify (carried, not wave-16-new)
- The wave-15 packaging req->ev downgrades (list_adjacency_closing->list_grand,
  m_handling/m_sweep->list_safe) remain on the branch (w15-C1); still
  maintainer-ratify, still NOT auto-adopted on master (master keeps req).
- #260 unratified sub-$1 override language (w16-C5).

### D. Refusals / holds
- No packaging-PROVED flip (list_safe stays CONDITIONAL at every commit);
  no smuggled discharge; no unauthorized in-tree Modal launch; no new REFUTED
  req-child. **Nothing to refuse.**

## COMPUTE-LAW SELF-REPORT
All scripts written to scratchpad first and run via `tools/ramguard tiny`
(absolute paths, reading the pinned tree / dumped dags); dag dumps via bash
`git show`. No bare python3; no Modal; no heavy compute. Mutation copy
(`w16_mut`) confined to scratchpad; repos untouched (READ-ONLY honored).

## DELIVERABLES (scratchpad)
w16_findings.md (this file), w16_dag_delta.py, w16_delta2.py, w16_wiring.py,
w16_adjc.py, w16_extparents.py, w16_manifest.py, w16_mutate.py, w16_replay.sh,
w16_keystat.py, w16_diffnode.py, w16_cb.py, w16_checks.py; w16_tree/ (pinned
archive), w16_mut/ (mutation copy). Node-replay + validator + manifest +
mutation outputs captured in-session.
