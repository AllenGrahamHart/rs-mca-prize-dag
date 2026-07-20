# SUB-AUDIT XR (wave-15) — findings (INCREMENTAL)

Pin 5661ba51. Read-only. Pinned tree = w15_tree (git archive verified).

## Node inventory / statuses (from pinned dag.json, 934 nodes)
Added xr_ nodes in w15_added_nodes.txt = **9** (lines 92-100), NOT 10 (prompt header says "10" — miscount; only 9 exist and only 9 listed in YOUR NODE SET). 

| node | status | dir | feeds |
|---|---|---|---|
| xr_lowcore_u0_loop_defect_ratio_router | PROVED | background/ | xr_lowcore_spread_heart (TARGET) |
| xr_tangent_support_mismatch_bridge | TARGET | critical/ | xr_clean_residual_any_gate (COND) |
| xr_nondeep_tangent_supportwise_payment | REFUTED | background/ | xr_tangent_support_mismatch_bridge (TARGET) ONLY |
| xr_true_tangent_coordinate_injection | PROVED | critical/ | bridge, clean_residual (COND), plotkin_width |
| xr_tangent_mismatch_external_zero_factor_reduction | PROVED | background/ | bridge |
| xr_tangent_mismatch_full_external_zero_canonicalization | PROVED | background/ | bridge |
| xr_mismatch_chart_nongeneric_joint_support_equivalence | PROVED | background/ | bridge, plotkin_width |
| xr_mismatch_nongeneric_invariant_excess_descent | PROVED | background/ | bridge, plotkin_width |
| xr_nongeneric_explanation_plotkin_width | PROVED | background/ | bridge, lowcore_spread_heart(TARGET), clean_residual(COND) |

Frontier consumers: xr_highcore_collision_count TARGET, xr_lowcore_spread_heart TARGET, xr_clean_residual_any_gate CONDITIONAL, xr_smallcore_spread_count CONDITIONAL, xr_strip_classification_rungs PROVED.

## Refuted node — HONEST
- Refuted claim: a globally tangent pair fits in n-A+1 tangent slot WITHOUT deep hypothesis. FALSE.
- Concrete falsifier: RS[F_17, mu_8, 2], A=3, pair u=(0,0,0,0,0,0,1,1) v=(0,0,0,0,0,0,1,2): 8 exact-A bad slopes {1,2,4,8,9,13,15,16} vs slot r+1=6. Deep hyp 3r=15>n-K=6 fails.
- Only edge OUT of refuted node -> TARGET bridge. No PROVED consumer depends on it. Honest refutation, real falsifier, not a quiet retraction.

## #104 sweep — auditor-note edit check
- clean_residual_any_gate: statement changed (scope-repair, adds +(n-A+1)+16n^3 and support-wise repair) AND notes: **4 segments APPENDED** (all 2026-07-20), **ZERO removed/edited**. Pre-existing AMBER AUDIT + STRESS-VERIFIED auditor notes INTACT. => NO auditor-note edit. CLEAN.
- smallcore_spread_count: notes UNCHANGED (9->9); statement got "SUPPORT-WISE SCOPE REPAIR" narrowing appended. Honest narrowing.
- strip_classification_rungs: notes empty both; statement scope-repaired (references refuted node + bridge). Honest.

## #158 checks (descent/width secretly bounding the thing)
- plotkin_width: PROVED. Bounds # DISTINCT EXPLANATIONS + instance-tree size via constant-weight Plotkin/Rankin. EXPLICITLY scoped: "does not aggregate slopes across generic charts or bound slope fiber of one explanation... narrows but does not promote the bridge." No #158 overclaim. Proof arithmetic (XW3/XW4/XW5/XW6/XW7-9) checked by hand — sound.
- invariant_excess_descent: PROVED. Genuine monovariant: N drops >= h+1/transition (A_j>=h+1 from K_j>=1), h=A-K invariant (d subtracted from both). Depth <= floor(n/(h+1))-1 => caps 169,169,255,254,254,510. Explicitly disclaims branch/slope bounds. No circularity.

## Frontier impact
The 9 nodes CLOSE NOTHING on the frontier. highcore_collision_count and lowcore_spread_heart remain TARGET. The bridge remains TARGET. Residual = the two OPEN slope currencies named in the bridge (generic canonical chart-union slopes; pre-terminal slope-to-explanation fibers). Nodes add machinery + narrow the bridge only.

## Per-node soundness (hand-traced) — ALL SOUND, honestly scoped
- true_tangent_coordinate_injection (PROVED): bad slopes with witness codeword c0+z c1 inject into T via one nonzero coordinate root; ≤|T|≤n-A. Sound.
- external_zero_factor_reduction (PROVED): W=S\T, P_W|q_z, scaled chart dim K-d, agr A-d, excess h. Sound; disclaims summation over W.
- full_external_zero_canonicalization (PROVED): full Z_z⊇W, |I_z|≥A-|W|≥A-d_z, excess A-K; one chart per slope under fixed order. Sound; disclaims count over Z_z.
- chart_nongeneric_joint_support_equivalence (PROVED): nongenericity iff a 2nd joint A-support extends Z; distinct explanations pairwise ≤K-1. Sound.
- invariant_excess_descent (PROVED): monovariant N↓≥h+1, h invariant → depth ≤ floor(n/(h+1))-1 = 169,169,255,254,254,510 < 256/512. Genuine potential, NOT circular. Explicitly disclaims branch/slope bound.
- plotkin_width (PROVED): constant-weight Plotkin/Rankin on distinct EXPLANATIONS; XW3/4/5/6/7-9 arithmetic hand-checked sound. Explicitly bounds explanations+tree, NOT slopes; "narrows but does not promote."
- u0_loop_defect_ratio_router (PROVED): ratio-fiber geometry + rich-core peeling; line cap floor(R/(h+1)); explicitly does NOT pay residual v≤1,2,6.

## #158 verdict: NO overclaim. Both "descent depth" (invariant_excess) and "width" (plotkin) nodes explicitly state they do NOT bound the slope currency; the bridge stays TARGET precisely because slopes remain open. Descent audit: "A bounded depth does not authorize a large search unless a width or aggregate compiler is also proved."

## Replays: 9/9 PASS
- nondeep(REFUTED-confirmed, 8 slopes [1,2,4,8,9,13,15,16]); true_tangent(6561=3^8); factor_reduction(29070); canonicalization(29070,4230); chart_equiv(142198); excess_descent(4495, caps[169,169,255,254,254,510]); plotkin(strict1395,log840,trees99,logtrees48,tan420); plotkin_audit(9 string-pins); u0_router(3 fixtures,22 peel,3 profiles).
- Coverage asymmetry: 8 verify.py + only 1 verify_audit.py (plotkin), and that audit is 9 PROSE-PRESENCE string assertions ("H=h+1","1+104H","420H^2",... in statement/proof/audit), NOT 9 math mutations. Bridge(TARGET) has no verify (correct).

## Mutation controls: 4/4 TRIP (+9/9 internal plotkin-audit string-pins)
- MC1 descent cap 169→168: AssertionError (cap==expected_cap). TRIP.
- MC2 plotkin tree 104H→103H: AssertionError (instances==1+103H). TRIP.
- MC3 consumer edge target →_MUTANT: AssertionError (required-edge subset). TRIP.
- MC4 node status PROVED→CONDITIONAL: AssertionError. TRIP.

## Unconditionality: STRONG PASS
- All 7 PROVED nodes: req-closure entirely PROVED/AXIOM/PINNED (zero non-PROVED req-ancestor).
- No PROVED node has any REFUTED node in its req+ev closure.
- REFUTED xr_nondeep_tangent_supportwise_payment: only downstream edge = ev→TARGET bridge (regression fixture). Transitive downstream PROVED nodes: NONE. All downstream = CONDITIONAL/TARGET/CONJECTURE (prize, mca_grand, clean_residual...). Properly contained.
- New poses: exactly ONE new TARGET (the bridge) — honest, with falsifier + attack_surface. No PROVED node introduces a hidden pose.
- No EXPERIMENTAL/Modal/pilot/TODO/placeholder. Verifier dag.json reads = own status/edge self-consistency (legit).

## Arc-check (commit 85 f6f54948 "Repair the XR nondeep tangent scope")
What was wrong: clean_residual_any_gate's former one-premise amber SILENTLY treated globally-nongeneric pairs as tangent-paid outside the deep range. Commit 85 exposed this via the F_17 rate-1/4 counterexample (minted REFUTED node), added the TARGET bridge as explicit complementary premise, and narrowed clean_residual/strip/smallcore statements. Honest self-correction: refuted claim preserved WITH falsifier, no official row refuted, no auditor note deleted, consumer correctly kept CONDITIONAL on the new open bridge.

## #104 auditor-note verdict: CLEAN
clean_residual_any_gate: 4 note segments APPENDED (2026-07-20), 0 removed/edited; AMBER AUDIT + STRESS-VERIFIED auditor notes intact. smallcore/strip: notes unchanged; statements narrowed (scope-repair). No auditor-note edit.

## Frontier impact / residual
Ranks 5,5,5 / 17,17,15 UNCHANGED. Neither xr_highcore_collision_count nor xr_lowcore_spread_heart closed or numerically reduced. The wave adds PROVED machinery + narrows the NONGENERIC branch (new TARGET bridge). Exact residual:
 (A) Bridge (nongeneric): (1) distinct slopes across union of generic full-external-zero charts (no binomial chart factor); (2) slopes per joint explanation before the paid terminal window, aggregated over the low-core family. Both must fit ≤16n^3.
 (B) Generic branch UNTOUCHED: xr_highcore_collision_count (≤8n^3) + xr_lowcore_spread_heart (≤8n^3) remain TARGET; u0 router + plotkin narrow lowcore but leave v≤1,2,6 and slope-fiber open.

## Catches (all LOW/informational — no hard catch, no soundness defect)
- w15-X1 (LOW, coverage-label): plotkin verify_audit prints "mutations=9" but performs 9 prose-string presence checks, not 9 falsification mutations. Real math verification is verify.py. Suggest relabel or add true math-mutation audit. Not a soundness issue.
- w15-X2 (LOW, benign wiring): REFUTED node retains a live ev-edge into the TARGET bridge and appears in bridge dependency_subdag. Confirmed CORRECT (regression fixture); no req-consumer, no PROVED downstream. Flag as the sole place a refuted node stays wired; benign.
- w15-X3 (LOW, prompt miscount): only 9 xr_ nodes added (w15_added_nodes lines 92-100), not 10. Two live under critical/nodes/ (bridge, true_tangent_coordinate_injection), 7 under background/nodes/.

## Import-eligibility: ELIGIBLE (no repairs required)
7 PROVED lemmas (unconditional, verifies pass, mutations trip), 1 honest TARGET (bridge), 1 honest REFUTED (contained). NO auditor-note edit. Caveat for reviewers: wave does NOT resolve P-A/P-B; both frontier TARGETs + bridge remain open with the exact 2-currency residual above.
