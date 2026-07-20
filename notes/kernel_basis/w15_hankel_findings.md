# SUB-AUDIT HANKEL — wave-15 replay audit of Codex v7

PIN = 5661ba51 (pinned tree confirmed at w15_tree). v7 worktree HEAD = 57d4405f (DIRTY/ahead).

## Node set (confirmed)
- 34 nodes total: 25 LANE A (rate_half_ca_hankel_*), 8 LANE B (rate_half_list_budget_three_antipodal_*), 1 rate_half_residual_prime_field_collapse.
- ALL 34 PROVED in pinned dag, none key=True, none gated. (matches ~35 expected)

## Commit map (v7 wave-15 range b3fd3dc5..5661ba51, 140 commits)
- v6-tail: #1 4b8fb6a0 kernel_plane_transversality, #2 3dc660c0 quadratic_moment_pin, #3 de2117f4 pure quartic ramification (-> pure_ramification_passport lineage)
- #4 ad7330bf "Reconcile wave 14 proof additions"; #13 99e368aa "Halve the deleted-pair gcd degree"
- LANE A distance-three/quotient chain: #57-#94 (1767df97..cbf645ef)
- CR-002 governance: #78 7955ceb3, #79 7991e2b7; #85 fd0481cd adjacent-crossing compute contract; #55 30cc2c42 HGE4 deferred criteria
- residual_prime_field_collapse: #68 cb59271c

## REPLAY RESULTS (ramguard tiny, pinned tree)
- verify.py: 34/34 PASS (all rc=0, PASS markers). 
- verify_audit.py: 8/8 PASS.
- TOTAL 42/42 PASS.
- COVERAGE ASYMMETRY: only 8/34 nodes carry verify_audit.py. The 8 = v6-tail (kernel_plane, quadratic_moment_pin) + all 6 LANE-B deleted-pair/harmonic/euler nodes. The ENTIRE 24-node LANE-A distance-three+quotient chain, the 2 pure_harmonic gates, the e1 route_fence, and residual_prime_field_collapse have NO verify_audit.py.

## MUTATION CONTROLS (5/5 TRIP)
- M1 resultant exponent: resultant_power_equivalence p_z^3 -> p_z^4 => AssertionError. TRIP.
- M2 endpoint-matrix coeff: endpoint_resultant_matrix beta=3(e+1)/2 +1 => alpha+beta==r fails. TRIP.
- M3 norm/degree constant: even_jacobi m=2^35 -> 2^34 => ell==2m fails. TRIP.
- M4 req-parent status flip: kernel_plane dep hankel_factor_pin PROVED->TARGET (mini-tree) => packet_check status assert fails. TRIP.
- M5 consumer/expected-phrase: even_jacobi statement "does not prove any gcd" removed (real data, mini-tree) => marker assert fails. TRIP.
5/5 trip.

## *** CATCH w15-H1 (BROKEN PIN, LANE B) ***
Consumer/pose-contract node `rate_half_list_adjacent_crossing` verify.py FAILS at the pinned commit 5661ba51 (status:FAIL, check `brackets_are_evidence` = false).
- Cause: its `brackets_are_evidence` hardcodes the EXACT sorted list of incoming edges (59 entries). All 8 wave-15 LANE-B nodes were given `ev` edges INTO adjacent_crossing (they declare it as consumer) but were NEVER registered in that list.
- Proof: incoming edges = 59 at wave-14 base b3fd3dc5 (matches list -> PASS); = 67 at pin (59+8) with list still 59 -> FAIL. Diff = exactly the 8 LANE-B nodes, zero spurious. adjacent_crossing/verify.py was never touched b3fd3dc5..HEAD; still 59 at worktree HEAD 57d4405f (fails there too).
- KB #90 violation: statement.md was appended by LANE-B commits (52ff0566, 0a00c35c, 99e368aa, de2117f4) but the verify.py pin did NOT travel with it. No re-pin ceremony exists after the LANE-B work (last re-pins d522ac00 #9 and e59a2998 #54 both PRECEDE it).
- Severity: bookkeeping/registration, NOT soundness (edges are `ev`, math unaffected). But it is a hard replay failure => LANE B is NOT import-eligible as-is.
- Repair (mechanical, low-risk): add the 8 `(NODE, "ev")` entries to the brackets_are_evidence expected list, re-run the pin green.
- LANE A consumer (band_closure) has NO verify.py, so no analogous break; residual_prime_field_collapse also feeds band_closure only. adjacent_crossing is the ONLY affected consumer.

## GOVERNANCE (clean for my cluster)
- No Modal launch attributable to LANE A/B. CR-002-J0 (added 7955ceb3, edited 7991e2b7) is a DEFERRED external request: "not authorized on the low-credit Modal account", "official cost still unknown", INCOMPLETE => no DAG change. Only a small ramguard-tiny route-selection pilot (~0.2s) vendored at experiments/prize_resolution/cr002_j0_resultant_pilot.py.
- de2117f4 / 30cc2c42 (HGE4) / fd0481cd: all negative-authorization language ("Do not launch...", "No current Modal run is authorized"). fd0481cd only touched adjacent_crossing attack/frontier + orbit SVGs (no compute run).
- App-ids ap-gWA4UOyBSv4c8C4tqDVd84 / ap-4mxCfTnbtIf2yz274On6sh are HISTORICAL WCL-lane (commit d1d015e8, NOT my nodes) records of PAST capped runs that timed out at exp 64 — documented as a route fence to justify deferral, not a new spend.

## #137 CASE-SPLIT COMPLETENESS (sound where checked)
- residual_prime_field_collapse: f in {1,2,3,4} proved complete via LTE p^deg<2^168 sieve (survivors=[1,2,3,4]); roots complete by C_2 x C_2^39 (gcd count); interval census 24+22=46 quadratic candidates each composite w/ explicit divisor; 0 cubic/quartic. Genuinely computed.
- pure_ramification_passport: 5 cases exhaustive via Riemann-Hurwitz defect-sum invariant (each collision preserves generic defect = 2N-2), embedded mutation control. Genuine.
- even_jacobi: 6 signed tests = j in {0,1,2} x sign eps in {+,-} (K_-=T_L, K_+=U_{L-1}); quadratic transforms verified exactly over Fractions m=1..7. torsion_cyclotomic covers both signs (minus=order-2^38 norm, plus=36-level tower).

## #104 CONSUMER SWEEPS
- rate_half_band_closure: TARGET (unchanged, key). Appends dated 2026-07-19 (statement + proof) explicitly say "remains TARGET" / "does not settle the lower Hankel or splitting equations". No status flip. No verify.py (frontier node).
- rate_half_list_adjacent_crossing: TARGET (unchanged, key). Statement appended by LANE-B commits; nonclaim intact ("adjacent crossing remains open for B*>=3"). BUT its verify.py FAILS => see w15-H1. No refused/withdrawn text reintroduced (scan clean).
- v13_bc_split_pencil_normal_form: CONJECTURE (unchanged). Appended 2026-07-20 by 2814a6a9 (L1/v13.2 lane, OUTSIDE my cluster) with a support-wise correction guard citing a mu_8 subset F_17 counterexample; honest, dated, status held.

## #90 POSE-CONTRACT PAIR RULE
- adjacent_crossing is a pose-contract node (TARGET, key). Its statement.md changed in-range but verify.py did NOT travel with it => pair broken (w15-H1). No refused text reintroduced.

## UNCONDITIONALITY
- All 10 external req-parents PROVED. 35 internal req edges. No conditioning on TARGET/CONJECTURE/refuted predicates. No new poses in my 34-node set (all PROVED). All Modal refs negative. No w14-C3-style pinning-note hazard in my node verify.py files (all "no Modal resource" disclaimers).

## Status: COMPLETE
