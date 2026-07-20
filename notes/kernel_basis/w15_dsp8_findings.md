# SUB-AUDIT DSP8 (wave-15) — findings

PIN 5661ba51 verified == archive tree. Worktree HEAD drifted to 57d4405f (as warned).
Range 186c2b60..5661ba51 = 20 commits, all authored 2026-07-20 04:08..08:12 by AllenGrahamHart (Codex).

## CENTERPIECE (preliminary from statement read)
correlation_bound is a TARGET leaf. It has NO verify.py (only statement.md + notes/).
Every "PROVED ..." block ends in an explicit NON-CLAIM. Final block:
"This is an alternative sufficient route to C36', not a proof of the displayed inequality or of (DSP8) itself."
=> Preliminary verdict (c): REDUCES/REFORMULATES. Neither DSP8 nor max-P<=24 satellite proved.

Non-claim ledger (each PROVED block):
- ADAPTER: proves J=4K=8D identity + primitivity. (real identity)
- UNIT-PRODUCT TRACE NF: "generic cubic-SP all-pairs enumeration ... is not a closing route."
- ANTIPODAL CAYLEY ROUTER: "does not bound that energy or decorrelate it from L_a; either omission changes the consumer."
- QUOT ANHARMONIC/TWIN: "symmetry cannot merge the DSP8 summands or close the target." + "class-A richness begins at P=26 not P=25" + F97 order-32 (P,R)=(6,9) at t=23,76 edges 0,1.
- UNIT-TRACE CURVE: genus-1 unless sigma^3=27 (node, genus 0). "open content is ... estimate."
- NODAL ROUTER: Stepanov <4n^(2/3); N_sigma<12n^(2/3)+1; coeff 29376 vs envelope 76599/40. "not deleted."
- CUBE-PREIMAGE: <(51/16)|K|^(2/3); 552n^2 (p=2 mod3) / 2387n^2 (p=1 mod3); "even sharpened nodal envelope remains above 76599/40."
- RICH FM COMPILER: 10K+17K <= (1/4)(10F+17F) <= (17/4)M_21. "No factorial-moment estimate is proved."
- BI-STAR/DISJOINT-SIX: "do not bound the number of ideal-norm survivors or their quotient weights."
- ACCIDENT-DEPTH: sum rho_L(t) <= (n-2)^2; L+E=17. "reduced moment and joint-ideal survivor bound remain open."
- JOINT-STAR PARETO (HEAD): last corner Dbar_16^0+(29/22)Dbar_16^A<=(319/153)n^2. "not a proof ... of (DSP8) itself."

Arithmetic checks so far:
- 892/4 = 223. ✓ (old J-target 892n^2 <=> old K-target 223n^2 via J=4K)
- DSP8-U 160(10K^0+17K^A)<=76599n^2 => 10K^0+17K^A <= 478.744 n^2. This is WEAKER than 223. 
  Chain of "sufficient constants": 223 -> 29031/80(=362.89) -> 76599/160(=478.74), each WEAKER on K.
  => MUST verify the reformulated (DSP8) RHS/terms genuinely keep sufficiency for C36' (goalpost check).

## DAG STRUCTURE (from pin + master dag.json)
- All 16 new nodes PROVED in pin dag; ABSENT on master (new to v7, expected).
- Consumers in pin: correlation_bound=TARGET, official_order_template_survivor=TARGET,
  excess_multistar_degree_ladder=PROVED, mobius_excess_half=CONDITIONAL.
- KEY EDGE: mobius_excess_half <= REQ correlation_bound [TARGET]. All edges INTO correlation_bound
  are kind=ev (evidence), none req. => correlation_bound unproved => mobius stays CONDITIONAL => C36 NOT closed.
- ALL external req-parents of the 16 nodes are PROVED on MASTER (11 distinct):
  f3_h2_stepanov_inhouse, antipodal_tail_distance_six_split, cutoff18_double_accident_reduction,
  disjoint_distance_six_split_pencil_router, distance_four_fiber_degree_cap,
  distance_six_support_overlap_payment, double_accident_coupling_batch_odd_saturation,
  double_accident_nonzero_coupling_ideal_router, quotient_block_identity,
  rich_fiber_norm_cutoff, weighted_multistar_router. => no external unconditionality gap.
- Internal req-DAG among the 16 is acyclic and all-PROVED (adapter is the root).

## REPLAY COUNTS
- verify.py: 16/16 PASS.
- verify_audit.py: 16/16 PASS (internal mutation batteries 8-10 each).
- TOTAL 32/32 PASS. No OOM, no timeout. (ramguard tiny, from pinned tree)

## SUFFICIENCY / GOALPOST chain (reduction.md + payment nodes)
mobius target WX18: 17 X_18 <= 300 n^2, X_18 = sum_{t!=1} (P(t)-18)_+ R(t).
reduction.md "non-swap" path: 68 X_18 <= S_ns^rich <= S_ns; S_ns^rich<=1200n^2 => 17X_18<=300n^2.
  CHECK: 1200*17/68 = 300 exactly. ✓ And (m-18)_+ <= 17+(m-35)_+ ; former X_35<=n^2/2 => 17X_18<(595/2)n^2... <300n^2. ✓
DSP8 (E=6 disjoint) route via payments:
  AQM (antipodal_quotient_mass): S_A<(51/32)(n-2)n^(2/3) (AQM1); O_6,25^0+(17/10)O_6,25^A<=6Q_n+(38/5)S_A (AQM2);
    => C36' follows from 10K^0+17K^A+152S_A<=750n^2-375Q_n (AQM3); uniform 80(10K^0+17K^A)<=29031n^2 (AQM4), 29031/80=362.89.
  GOP (global_overlap_cover): <=2n global overlapping gen-gen edges => O_6,25^0+(17/10)O_6,25^A<(867/80)n^(5/3)+(17/5)S_A (GOP1);
    => C36' follows from GOP2 == (DSP8) verbatim; uniform 160(10K^0+17K^A)<=76599n^2 (GOP3), 76599/160=478.74.
  Chain of sufficient constants on 10K^0+17K^A: 223 -> 362.89 -> 478.74 (each WEAKER because overlap now paid separately).
  => NEED: verify payment PROOFS actually PROVE "C36' consumer follows from (DSP8)", i.e. the reduction is proved not asserted.

## GOALPOST RESOLVED — reformulation is SOUND, not a weakened goalpost
- "E=6 compiler" GOP invokes = (A6S8) in f3_h3_antipodal_tail_distance_six_split (PROVED on master):
  4(10 M_6,25^0+17 M_6,25^A) <= 5 B_(n,6) implies C36'; B_(n,6)=300n^2-17*6*Q_n=300n^2-102Q_n. 17*6=102 ✓
  Restated: M_6,25^0+(17/10)M_6,25^A <= B_(n,6)/8. Complete moment M = disjoint D + overlap O.
- Overlap paid: GOP1 O^0+(17/10)O^A < (867/80)n^(5/3)+(17/5)S_A (PROVED); AQM1 S_A<(51/32)(n-2)n^(2/3) (PROVED).
- Multiply-(5)-by-20 => GOP2 == (DSP8) verbatim; machine-checked (750/20=300/8, 255/20=102/8, 68/20=17/5, 867/4/20=867/80).
- GOP3 => GOP2 checked for ALL official orders n=2^13..2^41 via (2601/8)^3 n^5 < root_free^3 (i.e. n^(1/3)>20). ✓
- DSO6 cross-checks: 12.75Q+13.6Q=26.35Q, *20=527 => D^0+(17/10)D^A<=(750n^2-527Q_n)/20 exactly. ✓
- Old 223 = DSO7 (D^0+1.7D^A<=223/20 n^2 <=> 10K^0+17K^A<=223n^2 via K=2D <=> 10J+17J<=892n^2 via J=4K). ✓
- VERDICT: proving new (DSP8) genuinely closes C36'. Constant relaxed 223->478.74 ONLY because overlap now paid
  separately at O(n^(5/3)) instead of lumped at O(n^2) — a legitimate refinement, NOT a moved goalpost.

## HAND-TRACE spot checks (all reproduce statement constants)
- Adapter SPA6 J=4K=8D: verify constructs cubics, exhaustive n<=16 cross-check, checks 892==4*223. GENUINE.
- Twin: F97 order-32 (P,R)=(6,9) at t=23,76, edges (0,1) machine-verified at the field; F193 parity max P=26,
  P even for antipodal => P>=25 iff P>=26 iff M_a>=24. GENUINE. Non-claim "does not assert equality N_6^disj" present.
- Cayley: P=2+M_a via C(u)C(v)=C(a) <=> u+v=a(1+uv); boundary reps = {a,-a}. GENUINE.
- Accident-depth ADC5: B_(17,0)=11n^2+578n-289, B_(0,17)=11n^2+1156n-1156 both match formula; ADC9 L=11 => 1799. ✓
- Joint-star JDP last corner: m_16=16, d_0=58,d_A=44, a_16^0=9/29,a_16^A=9/22, w_16=29/22, C_16=11/(17*9/29)=319/153. ✓✓
  Sufficiency 17*a^0*C_E=11<B_(L,E). ADC7 endpoint 583/272 = 12243/5712 reduced by 21. ✓
- Elliptic: C_sigma X^2Y+XY^2-sigma XYZ+Z^3=0 genus1 unless sigma^3=27 (node, genus0); verify singular_sigmas=3. GENUINE.
- Stepanov: optimized <4n^(2/3) (T=1), cubic-preimage <(51/16)|K|^(2/3); both req f3_h2_stepanov_inhouse [PROVED master].

## REPLAY + MUTATION
- verify.py 16/16 PASS; verify_audit.py 16/16 PASS (internal mutation batteries 8-10 each).
- Independent mutation controls: M1 K=2D corrupt, M2 GOP 76599, M3 twin F97 edges (0,1)->(1,1),
  M4b 892==4*223 -> 224, M5 req-parent adapter flipped to CONJECTURE, M6 JDP3 last-corner 319/153->320/153.
  ALL 6/6 TRIP with AssertionError. Covers: identity, GOP constant, F97 parity, 892/223 equiv, req-parent status, JDP3 constant.

## UNCONDITIONALITY / #137 / #104 / GOVERNANCE verdicts
- UNCONDITIONALITY: all 11 external req-parents PROVED on master; internal 16-node req-DAG all-PROVED at pin, acyclic.
  No new pose introduced by the 16 (poses live only in the TARGET leaf correlation_bound + template_survivor, both pre-existing TARGETs).
  No verify.py in the 16 reads notes/ or experiments/ (w14-C3 hazard ABSENT). No conditioning on a refuted predicate.
  No EXPERIMENTAL/pilot/result.json dependency in the 16 folders (only two "No Modal computation was used" negations in joint_star audit/result).
- #137 completeness: class splits EXHAUSTIVE — antipodal/antipodal-free (dichotomy on fiber containing {a,-a});
  sigma^3=27 nodal vs smooth (at most 3 sigma, genus0 vs genus1); p=1 vs p=2 mod3 (g=gcd(3,p-1) in {3,1}, official p odd => exhaustive);
  one- vs three-cubic-root nodal slice (g in {1,3}). P>=25/27/.../35 corners are Pareto ALTERNATIVES (any one suffices), not a partition.
- #104 consumer sweep: correlation_bound (TARGET) is an IN-PLACE REWRITE across ~5 commits, BUT old 892 target preserved
  ("former 10J+17J<=892n^2, superseded"), non-claims preserved verbatim ("Quotient-pullback deletion cannot reduce it,
  and an unweighted SP count does not prove the required correlation"), F-round-1 falsifier updated honestly
  ("survived vacuously because no measured row reached P>=25" = evidence not proof). PROVED blocks are undated but each maps to a
  dated PROVED node. official_order_template_survivor stayed TARGET. excess_multistar_degree_ladder strengthened in place
  (weight-8 bi-star), still PROVED, downstream JDP corner recomputed correctly => strengthening additive/sound.
  mobius_excess_half stayed CONDITIONAL (req route = correlation_bound TARGET).
- GOVERNANCE: DSP8 range (all 07-20) touches notes/PRIZE_COMPUTE_REQUESTS.md (CR-001) as bookkeeping only — CR-001 stays
  "blocked... no large run"; only swaps which template packet to compare first. NO Modal/subprocess/.remote invocation anywhere in range.
  The only Modal shards (F-round-1 census) are dated 2026-07-19, OUTSIDE the range, untouched by it, feeding the TARGET leaf as evidence.
  F-round found max P=20 on all sampled rows => P>=25 never reached => P<=24 satellite NOT proved.

## CENTERPIECE VERDICT: (c) REDUCES / REFORMULATES (none proved). NOT (a), NOT (b).
correlation_bound (DSP8) is a TARGET leaf, unproved; every edge into it is ev. mobius_excess_half stays CONDITIONAL.
C36 / C36' / u1_x4 NOT closed. Reformulation is SOUND (not a weakened goalpost): proving new (DSP8)/(DSP8-U)/any JDP corner
genuinely closes C36' via PROVED chain [A6S8 E=6 compiler + GOP1/AQM1 overlap payment + SPA6 adapter + machine-checked arithmetic].
EXACT RESIDUAL: an unconditional bound on the disjoint primitive-shift-pair correlation 10K_25^0+17K_25^A
(equivalently 10J_25^0+17J_25^A, or the E=6 disjoint moment). It now SUFFICES to prove ANY ONE of:
  (DSP8) 10K^0+17K^A+68S_A+(867/4)n^(5/3) <= 750n^2-255Q_n;  or
  (DSP8-U) 160(10K^0+17K^A) <= 76599n^2;  or
  one JDP-Pareto corner, e.g. Dbar_16^0+(29/22)Dbar_16^A <= (319/153)n^2;  or
  the FM route 40(10F^0+17F^A)<=76599n^2 / 680 M_21<=76599n^2;  or exclusion of one accident-depth rectangle.
None of these is proved. Every payment/compiler node explicitly disclaims "supplies no estimate for the disjoint primitive-SP count".

## CATCHES (all LOW/INFO — no integrity failure found)
- w15-D1 (LOW, #104): correlation_bound TARGET statement is an in-place REWRITE across ~5 commits, not append-only.
  Benign — old 892 target + all non-claims preserved & re-labeled "former/superseded". Import note: any external cite must pin a commit.
- w15-D2 (LOW/INFO): nodal three-cubic-root (p=1 mod3) envelope 2387n^2 EXCEEDS DSP8-U allowance 76599/40=1914.975 n^2.
  Correctly flagged as residual non-claim ("closing it requires richness/disjointness, not another marginal point bound"). No overclaim.
- w15-D3 (LOW, inherited): both Stepanov nodes + GOP arithmetic verify only the 29 official orders s=13..41 by discrete
  integer/floor checks (proof: "Exact integer cubing at the 29 orders verifies (6)"). Inherited from f3_h2_stepanov_inhouse (master).
  If official H3 rows extend beyond s=41 the discrete verification would need extension. NOT a DSP8-introduced defect; confirm the
  official-order window is exactly s=13..41 at import.
- w15-D4 (INFO, merge arc-check): excess_multistar_degree_ladder is PROVED on master but strengthened IN PLACE by v7
  (commits cc4806e4/eceaa20f, statement+proof+verify changed). Merge must re-verify it + downstream on master. Self-consistent at pin.

## PROVED-BLOCK -> NODE MAP (all 16 accounted, each genuine replaying verify.py)
adapter, unit_product_trace_normal_form, antipodal_cayley_product_router, quotient_anharmonic_antipodal_twin,
unit_trace_elliptic_curve_router, nodal_trace_parameter_router, nodal_cube_preimage_envelope(+nodal_target_divisor_pruning),
rich_factorial_moment_compiler, disjoint_six_multiplicity_gate, accident_depth_compiler, joint_star_depth_pareto_compiler(HEAD),
antipodal_quotient_mass_payment, global_overlap_cover_payment, + 2 Stepanov (cubic_preimage, optimized). No non-claim dropped/contradicted.

## IMPORT-ELIGIBILITY: YES for the 16 background support nodes (as REDUCTION/REFORMULATION background).
correlation_bound + official_order_template_survivor remain TARGET; mobius_excess_half stays CONDITIONAL. No false closure.
Required at merge: re-verify excess_multistar_degree_ladder + downstream (w15-D4); confirm s-window (w15-D3).

