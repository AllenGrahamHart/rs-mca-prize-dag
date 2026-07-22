# WAVE-21 fresh-context replay audit — v8 pin 1c921b1c

Base = wave-20 pin 61f3900a. Range verified = 24 commits. Master ref = 03116dee (1181/2771).

## Setup
- Pin HEAD == 1c921b1c ("Exclude broad checkpoint rows by Frobenius periodicity") — VERIFIED.
- Tree archived to w21_tree/; dag.json sha256 2aa3fb70... matches worktree == archive. VERIFIED.
- Changed files: 13 new nodes (all l1_*), 5 modified nodes (f3_h3_pgl2_pair_identity, f3_h3_quotient_galois_orbit_scalar_decomposition, f3_h3_dsp8_correlation_bound [attack.md A], f3_h3_mobius_excess_half [attack.md], l1_mixed_petal_amplification [attack+statement]), plus dag.json, verifier_manifest.json, verifier_replay.json, PRIZE_COMPUTE_REQUESTS.md, PRIZE_RESOLUTION_ROADMAP.md, KB_LOG.md, 3 orbit files.

New nodes (13):
1. l1_coarse_pfree_tame_tail_distance_upgrade
2. l1_coarse_pfree_wronskian_distance_packing
3. l1_coarse_pfree_wronskian_neighbor_compiler
4. l1_identity_pullback_role_payment_fence
5. l1_official_broad_checkpoint_frobenius_periodicity_exclusion
6. l1_official_checkpoint_characteristic_atlas
7. l1_official_coarse_pfree_entropy_reserve
8. l1_official_first_checkpoint_split_pencil_reduction
9. l1_official_frobenius_checkpoint_q_router
10. l1_official_max_split_value_complement_census
11. l1_official_newton_cofactor_window_router
12. l1_official_reserve_tame_refinement_router
13. l1_official_split_pencil_value_capacity

(sections below appended incrementally)

## DAG delta base(61f3900a) -> pin(1c921b1c)
- BASE 1151 nodes / 2656 unique edges; PIN 1164 / 2696; MASTER 1181 / 2770 unique (raw 2771 incl. 1 pre-existing duplicate edge petal_descent_classification_bridge->petal_g1_k4_scale_reserve — master quirk, not wave-21).
- +13 nodes (all PROVED, all L1 lane), 0 deletions, +40 edges, 0 edge deletions.
- Exactly ONE shared-node dag.json field flip: f3_h3_pgl2_pair_identity.statement (the C36'/joint-gcd rewrite). No status flips anywhere. Status hist delta = +13 PROVED only.
- l1_mixed_petal_amplification in-deg: base 76 -> pin 89 (13 new suppliers). Master still 76 (wave-21 not yet integrated).
- LINEAGE CONFIRMED: master-only = exactly the 30 known wave-19 survival nodes (29 xr_* + f3_hge4_ambient_order_norm_level_cap); edge gap 2770-2696=74, +40 pin-new = 114 ~ known ~114. xr_highcore_collision_count in-deg 44 pin / 65 master as pre-classified. Pin-only = the 13 wave-21 nodes. NO other divergence.

## Replay battery
- Inventory: 26 scripts in 13 new nodes + 3 changed (f3_h3_pgl2_pair_identity/verify.py, f3_h3_quotient_galois_orbit_scalar_decomposition/verify.py+verify_audit.py) = 29 total. Launcher screen: no modal/subprocess/network patterns in any -> 0 excluded.
- Result: 29 PASS / 0 FAIL / 0 TIMEOUT under ramguard tiny, run from archived tree w21_tree. Notable totals: frobenius_checkpoint_q_router 78109 checks; reserve_tame_refinement_router 10837; newton_cofactor_window_router 3513; galois_orbit_scalar_decomposition n8192_orbits=24534.
- Pin's own experiments/prize_resolution/verifier_replay.json was REPLACED (now 1 PASS entry: f3_h3_pgl2_pair_identity only; wave-20's rate_half rows removed). Ledger is per-wave scratch, consistent with prior convention, but note it does NOT cover the 26 new-node scripts.

## Mutation controls (scratch copy w21_mut/, 5 controls, all KILLED)
1. checkpoint_atlas.tsv row (8192,3583) m 2->1  => atlas verify.py AssertionError. KILLED.
2. broad_orbit_closure.tsv row (16384,5119) gcd 4->3 => periodicity verify.py AssertionError. KILLED.
3. wronskian_distance_packing tau ceil((d+2)/2)->ceil((d+1)/2) => verify.py AssertionError. KILLED.
4. pgl2_pair_identity score cap 39->40 => AssertionError (36,2) — verifier explicitly catches that cap 40 admits I_inv=36, the exact C36' margin. KILLED.
5. newton_cofactor_window_router 3,175-layer window inequality tampered => AssertionError. KILLED.

## Pin validator
- tools/verify_prize_dag.py (pin copy, on pin tree): PASS structure/refs/acyclicity/reachability/status-propagation.
- Warnings (RIPE x2, 9 artifact-kind, 25 status-artifact gaps, 1 stale header dli_prime_weighted_large_block_support) are IDENTICAL at base 61f3900a => zero new warnings from wave-21.
- Node hygiene: 13 new nodes all have statement/proof/result/audit/claim_contract/lineage/dependency_subdag/verify/verify_audit. upstream_crosswalk.md present in 11/13; absent in l1_identity_pullback_role_payment_fence + l1_official_reserve_tame_refinement_router (crosswalk is optional: only 39/744 background nodes have one; not a defect).

## Priority 3 — DSP8 compute packaging (f1df607c)
- New section "External contributor work packages" in PRIZE_COMPUTE_REQUESTS.md: CR-001-ALG-PILOT / CR-001-N8192 / CR-001-ALL / CR-001-P24, each with decision, promotion gate, DAG effect. Framed verbatim as exceeding "the local five-minute and sub-$1 policy" and "none is currently an authorized local run" — COMPLIANT with maintainer caps + PR #1050 contributor register (CPU-time budgets). CR-001 ledger row authorization changed to "external pre-request only; no large run; cost unknown".
- Workload-concentration theorem (QOD4a) added to f3_h3_quotient_galois_orbit_scalar_decomposition: C_r/D_r closed forms; top class 12,285 blocks / 75.009% of degree at n=8192; falsifier list EXTENDED (top-class workload mismatch); nonclaims kept ("exact scheduling consequences, not complexity bounds"). verify.py extended (top_workload cross-check over all levels) and verify_audit mutations 6->9. Additive, sound.
- MODAL SCREEN: zero new Modal launches in range. Every new KB entry (#126-#149 range) states "No Modal run was used"; the only credit mention is a negation ("No CR-001 production run is authorized against the remaining local Modal credit"). No new experiments/ result dirs in range.

## Priority 4 — F2 endpoint calibration (2e8c38ea)
- Confined to l1_official_coarse_pfree_entropy_reserve (CER8 addendum) + l1_mixed statement/attack + notes. NO F2/u2c summit node file touched. Content: an exactly owner-pruned F2-shaped residual with max Exc_d<=2^(15(d-r))mu_free(d) is < 2^-3393 hence empty; 16 bits/condition NOT certified; explicitly "only a constant/budget compatibility statement"; "F2 still is not an L1 supplier" retained; live gap named as map + structured subtraction + owner transport.
- Verdict: pure calibration, no pose/ladder change. FLAG for the pending F2 standing-rule re-scope: this supplies the maintainer a concrete transport-gap list and a proved constant-compatibility lemma; no conflict, but the re-scope discussion should cite CER8 (and its "never apply to the full nonempty fiber" fence).

## Priority 1 — L1 checkpoint campaign verdict (20 of 24 commits)
Residual SHRINKS strictly, in-deg 76->89, node correctly remains TARGET. Proof spot-reads (line-by-line): split_pencil_reduction (degree-cancellation, ratio-multiplicity, terminal affine-line injectivity — all arithmetic re-derived, sound), broad_checkpoint_frobenius_periodicity (F_p-coefficient Frobenius closure + Fourier inversion parity, sound given machine-verified TSV), wronskian_distance_packing (perfect-field p-th-power exclusion for W=0; PWD5 parity cases re-derived; honest F_4 fixture t=2<3 acknowledging coarse<exact). Uniform-fallback arithmetic 11(p-1)>=256 checked.
GENUINELY CLOSED sub-pieces (stratum closures banked in PROVED background nodes, no premature flips):
- "Close the deep first-checkpoint pencil band" (b32c67d4) + row-sharpening (a068a444): t=p empty for d>=2p-1-r_*(p,n), r_*=floor((p(p-1)-1)/(n-1)); terminal affine-line stratum empty.
- Value-capacity lane: 2p>n rows have NO t=p collision; 2p<=n<3p closes d>=n-p (boundary 4609 vs ratio-only 5599 at (8192,3583)).
- Atlas exhaustion (44b6918d..ee76b100): 59 (n,p) pairs total for 2^13<=n<=2^44; all 33 m=1 rows closed; 6 of 10 m=2 rows empty, other 4 EXPLICIT (exactly n/2 antipodal pairs, depths p,p+1 — classified, not open).
- polynomial-abc capacity exclusion (54eeb1d2): h=m strata empty on ALL 16 m>=3 rows.
- Frobenius periodicity (1c921b1c): all 7 rows with s=n-mp>16 empty.
EXACT NEW RESIDUAL (as printed, no smuggle): (i) coarse lane — owner-aware exchange compression counting anchor subsets X per (row,owner,j,W), or coarse ambient inflation K_d<=q 2^28148, or owner-sensitive conditional flatness with Pade coalescing; (ii) first-checkpoint lane — exactly nine rows n=m(p+1), m in {4,8,16}, 2<=deg G_Q<=m-1, plus uncontrolled widths t>p; (iii) exact lane — nonpositive Johnson gate, partial-loss excess z-ell+1, missing whole-petal anchor (wild REMOVED at official cutoff); identity endpoint s=1 fenced as containing L1 itself; (iv) F2 bridge = map + structured subtraction + owner transport (constants compatible at 15 bits).
Disclaimers verbatim-verified: "This does not promote the node", "the node remains TARGET", "proves neither that inflation bound nor the positive-cofactor Pade-graph intersection", "No refinement census should be presented as closing this gap", "not an L1 closure", "no bound on the number of Q records when m>=3", "certificate or opposing-tail enumeration is no longer an open task" (the only removal claims are the proved ones). Wave-20 core intact: Toeplitz-section flatness obligation + Pade-graph intersection retained; routers typed as coordinate transports that "Keep the Pade-graph/flatness obligation".
Contracts: all 13 have falsifier + nonclaims (2 in bullet form); no req-smuggle; multiple carry compute fences ("no contributor or Modal run remains on the seven closed rows").

## Priority 2 — 4-statement adjudication: ADOPT ALL FOUR
Set = f3_h3_pgl2_pair_identity (statement/proof/verify), f3_h3_mobius_excess_half (attack), f3_h3_dsp8_correlation_bound (attack, NEW file), f3_h3_quotient_galois_orbit_scalar_decomposition (statement/proof/result/contract/audit/verify x2).
- ALL FOUR base==master byte-identical before the change => self-supersession of shared ancestor text; NO master-held correction at risk; diffs apply cleanly to master.
- Honesty of the weakening: old open target (global cap 39 => M35) RETAINED as stronger route; new weaker open target (PAIR-RECT: I_inv>=19 => I_aff<=18) + stronger-scalar variant (PAIR56, sharp at 57) added with PROVED compiler X_18<=17(n-1)^2 => 17X_18<=289n^2<300n^2 — re-derived by hand, correct. Consumer contract f3_h3_mobius_excess_half WX18 (17X_18<=300n^2) untouched and exactly delivered => NO silent obligation drop. Sharpness claim (57 admits (19,18)) machine-checked (mutations=threshold-40,threshold-57-rejected; my external mutation 39->40 killed with witness (36,2)).
- gcd normal form (PGL1-3): C_n squarefree via J(x)=x/(x-1), (1b) identity checked; typed as "exact theorem interface, not a uniform subresultant certificate".
- QOD4a workload concentration: closed forms C_r/D_r verified for all levels by verify.py; falsifier extended; "exact scheduling consequences, not complexity bounds".
- Statuses: pgl2 PROVED (stays), mobius_excess_half CONDITIONAL (stays), dsp8 TARGET (stays), galois orbit PROVED (stays).

## Pin lists
MARKER-PINS (wave-21 constants pinned across statement/attack/CR/KB/roadmap; cross-file grep consistent; machine-checked by replayed verifiers): p>=3583; p-ell_0>=3174 / 3,175 layers; <=23 checkpoints / 253 pairs; mu_free<2^-28276; K_d<=q 2^28148; owner-pruned F2 residual <2^-3393 (15-bit sufficient / 16-bit NOT certified); r_*(p,n) + fallback floor(11(p-1)/256); depth boundary 4609 (vs 5599); atlas 59=33+10+16; nine rows n=m(p+1) m in {4,8,16}; tau_p=max(ceil((d+2)/2),min(d+1,p)); PWD packing cap fence (a+k>=n, n-a>=128 unpayable under q<2^256); R_q(t,D); n/2 antipodal pairs at depths p,p+1; PAIR-RECT 19/18, PAIR56, 57-sharp, 289n^2<300n^2; QOD4a 12,285 / 50,319,360 / 62,896,128 / 75.009% / 93.757%.
REVERSE-CONSUMER-PINS (re-check on integration): f3_h3_mobius_excess_half (WX18 verified intact); f3_h3_three_to_one_c36 (dag-only CONDITIONAL, conditions on C36-PRIME, untouched); f3_h3_dsp8_correlation_bound; f3_h3_official_order_template_survivor + f3_h3_quotient_orbit_canonical_resultant_manifest (QOD4a additive); l1 consumer bracket — l1_mixed's 76 master suppliers + textual referrers (imgfib proof/conditional, list_adjacency_closing, ~30 l1_* statement/dependency_subdag mentions): NONE quotes the two rewritten frontier sentences (grep "wild decomposition, or missing" hits only l1_mixed) => no retrofit needed; CR-001 ledger row + new external packages (PR #1050 register).

## Refusals / holds
NONE. Non-blocking flags:
1. KB numbering collision: pin KB #126-#147 (22 entries) vs master #126 = wave-20 integration entry => renumber +1 at import.
2. Pin verifier_replay.json covers only 1/29 scripts (per-wave scratch convention); full battery run here compensates; regenerate at integration.
3. F2 standing-rule re-scope (pending maintainer item): CER8 calibration is a compatible INPUT (transport-gap list + 15-bit sufficiency lemma), not a pose change.
4. upstream_crosswalk.md absent in identity_pullback_role_payment_fence + reserve_tame_refinement_router (optional; 39/744 prevalence).
5. Pre-existing master duplicate edge petal_descent_classification_bridge->petal_g1_k4_scale_reserve (raw 2771 vs 2770 unique) — master hygiene, not wave-21.

## Import spec
- Cherry-range 61f3900a..1c921b1c applies cleanly: every modified node/notes file is base==master EXCEPT notes/kernel_basis/KB_LOG.md (renumber pin entries 126-147 -> 127-148, append after master #126) and tools/verifier_manifest.json (UNION merge: master keeps its 30 survival-node entries, add pin's 32 new/changed entries — disjoint keys except the 4 f3_h3 files, take pin's).
- dag.json: add 13 nodes + 40 edges; update f3_h3_pgl2_pair_identity.statement field; NO status flips.
- Post-merge: l1_mixed in-deg 76->89; nodes 1181->1194; edges (unique) 2770->2810; rerun verify_prize_dag + the 29-script battery + regenerate verifier_replay.json and orbit SVG/HTML (per artifact-refresh standing rule, publish site after DAG update).
