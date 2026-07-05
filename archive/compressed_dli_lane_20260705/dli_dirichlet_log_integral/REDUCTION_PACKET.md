# REDUCTION PACKET: dli chain (frontier -> interface), compressed 2026-07-05

Policy: notes/CHAIN_COMPRESSION_POLICY.md. Frontier: dli_prime_weighted_large_block_support (the weighted/RES
counting obligation). Interface: this node (the near-log-integral geometric-mean input to ejm).
Segment validated before compression: weighted re-pose end-to-end (sup forms refuted by low-mass
profiles, re-posed; 4 discrepancy nodes scoped to full-mass; tail margin 2^{-245 L_j} verified);
consumer dli_prime_block_conductor_mass survived an EXHAUSTIVE adversarial-lambda sweep n=32..2048
(sup ledger decays 0.296->0.0048, effective conductor flat ~2-2.7=O(1)).

## The 14 compressed steps (archive/compressed_dli_chain_20260705/)

### [CONDITIONAL] dli_bohr_flatness_prime
RE-POSED 2026-07-05 (weighted form): over PRIME rows F_p (Tr=id, no subfield collapse), per level j and nonzero lambda, the U-WEIGHTED fixed-frequency second moment is sublinear: E_U[ S_{j,lambda}(M) ] = o(L_j) over the central profile measure, S_{j,lambda}=sum_r m_{j,r}|mu_hat_r(lambda)|^2 for the odd-evaluation phase psi(lambda P_lambda(sigma(y))). Combined with the trivial per-profile bound eta
NOTES: AMBERED (Pro T3, verified): reduction PROVED (second-moment split + Deligne block bound); reduces to dli_prime_block_conductor_mass (weighted conductor + small-block mass = o(L_j)). Degeneracy counterexamples (P=0, singletons) verified. | EMPIRICAL EVIDENCE (local census, seconds-scale, this session

### [CONDITIONAL] dli_harmonic_conductor_ledger
SCOPED (Pro P2, verified): fixed-freq 2nd-moment flatness S_{j,lambda}=o(L_j) is FALSE over extension fields (F_{p^2}: a trace-zero lambda + subfield-valued section collapses psi to 1, S=Omega(L_j), VERIFIED) but HOLDS prime-field-wise (Tr=id, no collapse) — consistent with b2b's 'fixed prime q'. Prime rows: still needs the fixed-frequency Bohr bound (P2-A). EXTENSION rows (KoalaBear sextic F_{p^6
NOTES: RE-POSED (agents.md level-2 insight, verified): needlessly strong. Primitive core needs sum eta_j = o(t) over 34 levels => polynomial-loss/level suffices (reserve ~2^35 >> O(log n)). Sharp -2log2 geometric mean NOT needed; the PROVED seen-coordinate lever + crude near-peak (~129/level) charge should

### [CONDITIONAL] dli_log_integral_equidistribution
For every central profile and every nonzero frequency, the odd low-degree evaluations on the square-root section satisfy the near-circle log-integral geometric-mean bound -sum_y log |mu_hat_y(P_lambda(sigma(y)))|^2 >= 2(L_j-eps_j) log q - O(1), with sum_j eps_j=o(t). SCOPING CORRECTION 2026-07-05: "every central profile" is restricted to FULL-MASS central profiles (active seen-coordinate count >=
NOTES: | Full-mass scoping added 2026-07-05 (chain-coherence audit): low-mass profiles cannot meet the log-integral/discrepancy bounds (inactive coords contribute 0); scoped to full-mass, tail absorbed by the weighted ledger below.

### [CONDITIONAL] dli_odd_eval_exponential_sum_bound
For every central profile and every nonzero frequency, the normalized odd low-degree evaluations on the square-root section have Weyl sums small enough, uniformly over the harmonic ranges required by dli_et_peak_mass_reduction, with total DLI error sum_j eps_j=o(t). SCOPING CORRECTION 2026-07-05: "every central profile" is restricted to FULL-MASS central profiles (active seen-coordinate count >= (
NOTES: | Full-mass scoping added 2026-07-05 (chain-coherence audit): low-mass profiles cannot meet the log-integral/discrepancy bounds (inactive coords contribute 0); scoped to full-mass, tail absorbed by the weighted ledger below.

### [CONDITIONAL] dli_odd_evaluation_discrepancy
For every central profile and every nonzero frequency, the sequence of low-degree odd evaluations P_lambda(sigma(y)) on the square-root section has enough discrepancy control away from Dirichlet peaks to support the DLI log-integral geometric-mean bound with total loss sum_j eps_j=o(t). SCOPING CORRECTION 2026-07-05: "every central profile" is restricted to FULL-MASS central profiles (active seen-
NOTES: | Full-mass scoping added 2026-07-05 (chain-coherence audit): low-mass profiles cannot meet the log-integral/discrepancy bounds (inactive coords contribute 0); scoped to full-mass, tail absorbed by the weighted ledger below.

### [CONDITIONAL] dli_odd_phase_noncollapse_conductor
For every central profile, nonzero frequency, and harmonic m in the DLI ranges, the actual odd-evaluation phase P_lambda(sigma(y)) on the square-root section is geometrically nonconstant/non-Artin-Schreier on every relevant component, with conductor bounds whose harmonic total is o(t). This is reduced to the standard Artin-Schreier/conductor criterion plus the remaining reduced-pole and noncollaps

### [CONDITIONAL] dli_odd_phase_nontriviality_payload
For every central profile, nonzero frequency, DLI harmonic, and relevant square-root component, the actual odd-evaluation phase P_lambda(sigma(y)) is not of Artin-Schreier form g^p-g+c. This is reduced to the proved polar-obstruction soundness rule plus the remaining actual DLI polar-obstruction certificate payload.

### [CONDITIONAL] dli_odd_phase_polar_obstruction_payload
For every central profile, nonzero frequency, DLI harmonic, and relevant square-root component, construct a local certificate showing that the Artin-Schreier-reduced odd-evaluation phase P_lambda(sigma(y)) has a positive pole order not divisible by p. This is reduced to a proved reduced-phase manifest soundness rule plus the remaining actual reduced-phase manifest.

### [CONDITIONAL] dli_odd_phase_reduced_pole_budget
For every central profile, nonzero frequency, and DLI harmonic, the actual odd-evaluation phase on each square-root component is not of Artin-Schreier-trivial form, and its reduced polar divisor has harmonic total o(t). This is reduced to the proved harmonic ledger soundness rule plus the remaining actual nontriviality and polar-divisor ledger payloads.

### [CONDITIONAL] dli_peak_mass_discrepancy
For every central profile and every nonzero frequency, the odd low-degree evaluations on the square-root section satisfy the truncated-log discrepancy and peak-mass tail bounds required by dli_truncated_log_transfer, with total error sum_j eps_j=o(t). SCOPING CORRECTION 2026-07-05: "every central profile" is restricted to FULL-MASS central profiles (active seen-coordinate count >= (256-o(1))L_j).
NOTES: | Full-mass scoping added 2026-07-05 (chain-coherence audit): low-mass profiles cannot meet the log-integral/discrepancy bounds (inactive coords contribute 0); scoped to full-mass, tail absorbed by the weighted ledger below.

### [CONDITIONAL] dli_prime_block_conductor_mass
RE-POSED 2026-07-05 (weighted form; sup form had an interface mismatch with the re-posed leaf + a low-mass falsifier candidate): over prime rows F_p, per level j and uniformly in nonzero lambda, the U-WEIGHTED block ledger is sublinear: E_U[ C_j(M) + X_j(M) ] = o(L_j) over the central profile measure (weight U(M)=prod_y|D_y|), where C_j(M) = sum_{r not in X_{j,lambda}} m_{j,r} cond_{j,r}(lambda)^2
NOTES: T3 residual leaf: the deepest, most concrete form of dli — a weighted conductor + small-block mass count. Reduction to this is PROVED (second-moment split + Deligne). | AMBERED (T3-followup, verified): refuted as unconditional (small-block counterexample); PROVED conditional on dli_prime_weighted_la

### [CONDITIONAL] dli_reduced_phase_manifest_payload
Provide the actual DLI reduced-phase manifest: for every central profile, nonzero frequency, DLI harmonic, and relevant square-root component, the Artin-Schreier-reduced local expansion of P_lambda(sigma(y)), a positive pole order prime to p, a certified polar-divisor majorant for the same tuple, and an o(t) harmonic total for the majorants.
NOTES: Pro brief issued (deep analytic): the Deligne-Weil reduced-phase manifest — per-tuple prime-to-p reduced pole + conductor majorant + o(t) harmonic sum, giving geometric-mean equidistribution at -2log2. Calibrated flat. Closes dli->ejm->pcf->b2b primitive core. | Pro (verified): pole+conductor parts

### [CONDITIONAL] dli_reduced_pole_harmonic_ledger
For the same actual odd-evaluation phases, provide reduced Artin-Schreier polar-divisor bounds whose sum over the DLI harmonic ranges and components is o(t). This is reduced to a proved majorant-table soundness rule plus the remaining actual DLI reduced-pole majorant table payload.

### [CONDITIONAL] dli_reduced_pole_majorant_table_payload
Construct the actual DLI reduced-pole majorant table: for every central profile, nonzero frequency, DLI harmonic, and square-root component, bound the Artin-Schreier-reduced polar divisor of P_lambda(sigma(y)) and prove that the harmonic sum of the table is o(t). This is reduced to a proved reduced-phase manifest soundness rule plus the remaining actual reduced-phase manifest.

## Reattached side-inputs (all PROVED)
- dli_artin_schreier_conductor_criterion
- dli_circle_log_integral_constant
- dli_deligne_weyl_transfer
- dli_et_peak_mass_reduction
- dli_odd_phase_budget_ledger_soundness
- dli_odd_phase_polar_obstruction_soundness
- dli_phase_pole_conductor_manifest
- dli_reduced_phase_manifest_soundness
- dli_reduced_pole_majorant_table_soundness
- dli_truncated_log_transfer
- subfield_trace_paid_gate