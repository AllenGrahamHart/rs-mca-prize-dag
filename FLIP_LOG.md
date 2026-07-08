# F3 Flip Log 2026-07-08

## Initial stage: T3 h=2 constant campaign

Stage selected: T3 constant optimization for the already-proved h=2 in-house
chain.  This is independent of the harder T1 rich-curve proof and immediately
shrinks the finite midrange that would need exact certificates if the in-house
chain were used without the external Cochrane--Pinner import.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H2_RICH_COSET_OPTIMIZED.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_rich_coset_optimized.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_rich_coset_optimized.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_hbk_conditional_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_rich_coset_stepanov.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_per_row_accident_pose.py
```

Digest:

```text
H2_RICH_COSET_OPTIMIZED_PASS
H2_HBK_CONDITIONAL_COMPILER_PASS
H2_RICH_COSET_STEPANOV_PASS
H3_PER_ROW_ACCIDENT_POSE_PASS
```

Result: the same rich-coset Stepanov proof now has exact floor bookkeeping with
`K=66` instead of the old conservative `K=129`.  The propagated in-house h=2
constant improves from

```text
E(H) <= 83851 h^(5/2)
```

to

```text
E(H) <= 22111 h^(5/2).
```

The h=2 `T_2 < h^3` crossover moves from `7030990201/64` to
`488896321/64`, i.e. integer `h >= 7,639,006`.  Therefore the in-house h=2
chain covers all official power-of-two rows from `2^23` upward; only
`2^13` through `2^22` remain a finite midrange if the external import is not
used.

Next step: start T1 with a rich-curve denominator-clearing and coefficient
count packet, or continue T3 by estimating exact-census cost for the h=2
midrange rows `2^13..2^22`.

## T1 groundwork: rich-curve denominator compiler

Stage selected: T1 denominator clearing for degree-2 rational signature-curve
maps.  This isolates the first arithmetic obligation in the rich-curve
Stepanov route before attempting the nonvanishing and family coefficient-count
steps.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RICH_CURVE_DENOMINATOR_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_denominator_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_denominator_compiler.py
```

Digest:

```text
H3_RICH_CURVE_DENOMINATOR_COMPILER_PASS
```

Result: for `r_i=P_i/Q_i` with `deg P_i, deg Q_i <= 2` and auxiliary
`Phi(X,Y_1,Y_2,Y_3)` with `deg_X < A`, `deg_{Y_i} < B`, the clearing
denominator

```text
Q_1^{h(B-1)} Q_2^{h(B-1)} Q_3^{h(B-1)}
```

turns `Phi(X,r_1^h,r_2^h,r_3^h)` into a polynomial of degree at most

```text
(A - 1) + 6 h (B - 1).
```

The verifier checks the identity exactly over finite fields for 60 deterministic
degree-2 rational-map cases.  This does not prove T1; it pins the degree input
for the eventual multiplicity contradiction.

Next step: T1 coefficient-count/nonvanishing packet for this cleared
four-variable auxiliary polynomial, or T3 h=2 midrange certificate-cost table.

## T3 h=2 finite-midrange certificate-cost table

Stage selected: T3 finite-midrange accounting for the optimized in-house h=2
chain.  This does not try to replace the external Cochrane--Pinner import; it
states exactly what remains if the in-house chain alone is used.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H2_MIDRANGE_CERTIFICATE_COSTS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_midrange_certificate_costs.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_midrange_certificate_costs.py
```

Digest:

```text
H2_MIDRANGE_CERTIFICATE_COSTS_PASS
```

Result: the optimized h=2 in-house theorem covers official powers
`2^23..2^41`.  With the explicit planning shard size
`S = 2^26` ordered differences and the policy threshold `< 2000` shards, direct
exact-census certificates are plausibly feasible for `2^13..2^18`.  The honest
remaining in-house finite midrange is therefore exactly `2^19..2^22`.

Next step: return to T1 by attempting the rich-curve coefficient-count and
nonvanishing packet, or continue T3 by designing the actual h=2 certificate
runner for the feasible rows.

## T1 repair: rich-curve degeneracy audit

Stage selected: T1 theorem-statement audit before attempting the full
coefficient-count/nonvanishing lemma.  The denominator compiler applies to all
degree-2 rational maps, but the proposed rich-curve theorem cannot.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RICH_CURVE_DEGENERACY_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_degeneracy_audit.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_degeneracy_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_denominator_compiler.py
```

Digest:

```text
H3_RICH_CURVE_DEGENERACY_AUDIT_PASS
H3_RICH_CURVE_DENOMINATOR_COMPILER_PASS
```

Result: the overbroad T1 wording is false without degeneracy exclusions.  The
degree-1 subfamily `r_i(X)=c_i X` with all `c_i in H` has exactly `T=h`
simultaneous `H`-points for one curve, contradicting any one-curve
`C h^alpha`, `alpha < 1`, rich-curve estimate at large `h`.  Therefore the
next coefficient-count/nonvanishing packet must explicitly exclude or pay
multiplicative-dependence cells: toral `(0,0)`, the `3 | q-1` line
degenerations, and any curve where membership conditions differ only by
`H`-constant factors.

Next step: formulate the repaired rich-curve Stepanov target with these
degenerate cells removed, then attack the reduced-condition nonvanishing lemma.

## T1 guard: constant-ratio degeneracy filter

Stage selected: operationalize the first repaired-T1 exclusion.  This filter
does not enumerate every F3 signature-curve degeneration; it cheaply detects
the constant-ratio cases that collapse repeated `H`-membership conditions or
make two conditions incompatible.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RICH_CURVE_DEGENERACY_FILTER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_degeneracy_filter.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_degeneracy_filter.py
```

Digest:

```text
H3_RICH_CURVE_DEGENERACY_FILTER_PASS
```

Result: for rational maps `r_i=P_i/Q_i`, the script exactly tests whether
`r_i/r_j=lambda` in `F_p(X)`.  If `lambda in H`, the two conditions are
collapsed; if `lambda notin H`, they are incompatible.  The replay verifies
collapsed linear maps (`T=h`), incompatible linear maps (`T=0`), shifted
nonconstant-ratio maps, and a collapsed Mobius example (`T=h-1` because one
subgroup value maps to the pole).

Next step: use this guard while formulating the genuine noncollapsed
rich-curve target; the toral and `3 | q-1` hyperbola-line cells still need the
signature-geometry-specific classifier.

## T1 compiler: reduced-condition arithmetic

Stage selected: coefficient-count arithmetic for the repaired h=3 rich-curve
Stepanov route.  This is deliberately conditional: it does not prove the
reduced derivative condition count or the sparse nonvanishing lemma.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RICH_CURVE_REDUCED_CONDITION_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_reduced_condition_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_reduced_condition_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_degeneracy_filter.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_denominator_compiler.py
```

Digest:

```text
H3_RICH_CURVE_REDUCED_CONDITION_COMPILER_PASS
H3_RICH_CURVE_DEGENERACY_FILTER_PASS
H3_RICH_CURVE_DENOMINATOR_COMPILER_PASS
```

Result: if the repaired signature curves satisfy `RC-RED(C_red)`, meaning
each derivative order reduces to at most `C_red(A+D)` coefficient conditions
per curve, and if `RC-NV` gives nonzero substitution on every repaired curve,
then the exact arithmetic compiler is:

```text
C_red D (A+D) |Z| < A B^3
    => auxiliary exists,
sum_z T(z) < |Z| ((A-1)+6h(B-1)) / D.
```

This isolates the genuine T1 proof debt.  The denominator degree and
linear-system arithmetic are no longer vague; the missing mathematical gates
are exactly the reduced-condition lemma and the nonvanishing lemma after the
degeneracy filters.

## T2 refinement: h=3 activation-bound compiler

Stage selected: repair the h=3 per-row accident compiler so it consumes the
right sparsity object.  The rational norm-gcd pair-coprimality heuristic was
too strong and is refuted by the banked random sample; the actual object is
prime-ideal/common-root activation at primitive `n`th roots.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_ACTIVATION_BOUND_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_activation_bound_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_activation_bound_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_all_core_census_summary.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_per_row_accident_pose.py
```

Expected digest:

```text
H3_ACTIVATION_BOUND_COMPILER_PASS
H3_ALL_CORE_CENSUS_SUMMARY_DONE
H3_PER_ROW_ACCIDENT_POSE_PASS
```

Result: the compiler now states the exact conditional needed for h=3:

```text
H3-ACT(C): A_3(n,p) <= C n
```

where `A_3(n,p)` counts actual non-toral common-root activations, not rational
norm coincidences.  If `C=16`, the existing toral + Poisson + activation
arithmetic gives `T_3 < n^3` for every `n >= 17`.  In the banked `n=96`
all-core aggregate, the maximum oriented per-prime activation count is `92`,
below `n`; this is evidence only because the aggregate is not
Burnside-deduplicated, but it tests the right per-row object.

## Interim report: current F3 flip residual map

Stage selected: write a replayable interim report before further T1/T4 work,
so the branch has an exact map of what is proved, what is conditional, and what
still blocks a node promotion.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digest:

```text
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the report keeps the non-completion status explicit.  The three
promotion blockers are h=3 (`H3-ACT(C)` via `RC-RED` + `RC-NV` or certificates),
h=5 (symbolic norm-gate incompatibility or row-family certificates), and h=8
(n=64 non-antipodal x83 support branch).

## T4 h=5 structural reduction

Stage selected: sharpen the h=5 blocker using already-proved DAG inputs.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_STRUCTURAL_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_structural_reduction.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_structural_reduction.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digest:

```text
H5_STRUCTURAL_REDUCTION_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: h=5 has no remaining classification branch.  Since `5` is not a power
of two, `x24_char0_dyadic_descent` kills the char-zero branch; `x83` leaves only
p-specific norm-gate events.  The h=5 blocker is therefore precisely:
symbolically exclude that norm-gate branch at `p = 1 mod n`, `p >= n^2`, or
replace selected row evidence with a complete official-row certificate family.

## T1 foundation: h=3 hyperbola identity

Stage selected: bank the symbolic hyperbola normal form locally.  The existing
Modal script verifies the identity on enumerated finite trades; this packet
proves the algebraic identity that the rich-curve `RC-RED` and `RC-NV` gates
consume.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_HYPERBOLA_IDENTITY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_hyperbola_identity.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_hyperbola_identity.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digest:

```text
H3_HYPERBOLA_IDENTITY_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: for `F(T)=T^3+aT^2+bT+c`,

```text
G_F(u,v) = u^2 + uv + v^2 + a(u+v) + b = X Y - Delta
```

with the explicit `omega`-coordinates printed in the note.  This does not close
`RC-RED` or `RC-NV`; it makes the normal-form input replayable without Modal.

## T2 evidence upgrade: h=3 activation orbit dedup

Stage selected: perform the final affine/Galois-side-swap deduplication on the
banked `n=96` all-core activation list.  This targets the exact object
`H3-ACT(C)` counts: normalized activated shape orbits per prime.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_ACTIVATION_ORBIT_DEDUP.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_activation_orbit_dedup.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_activation_orbit_dedup.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digest:

```text
H3_ACTIVATION_ORBIT_DEDUP_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the `720` oriented activation records collapse to `167`
affine/Galois pair-orbits over `82` threshold primes.  The maximum deduped
per-prime activation count is `27` at `p=37633`, and no canonical orbit appears
at two different threshold primes.  This is evidence only, but it sharpens the
observed `n=96` scale from the raw oriented max `92 < 96` to a normalized max
`27 < 96`.

Next step: either attack `RC-RED` for the actual hyperbola normal-form curves,
or pivot to T4(a)'s h=4 rigidity route while T1's nonvanishing gate is still
open.

## T4 local replay audit: h=4..8 residual map

Stage selected: T4(a) status verification without heavy compute.  The local
aggregate replay scripts verify the current h=4..8 certificate state and show
that h=4's structural rigidity route is already banked.

Banked file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_T4_LOCAL_REPLAY_AUDIT.md
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_h8_bonus_sweep_replay.py
```

Digest:

```text
H4_H5_BONUS_REDUCTION_PASS
H6_H8_BONUS_SWEEP_PASS
```

Result: h=4 is structurally classified by the already-PROVED
`h4_terminal_dichotomy`; there is no broad h=4 identity gap left in T4(a).
The live h=4 residue is the explicit norm-gate/certificate column.  h=5 has
strong row evidence through n=128 but still lacks a uniform no-primitive theorem.
h=6/h=7 full anchored certificates replay; the h=6 `p=4993` nontoral row is
small and already classified as a paid h=3 square-lift.  h=8 remains partial at
n=64, with the x83 radius-three shells replayed but no full non-antipodal
signature join.

Next step: attack either the h=5 norm-gate incompatibility theorem or the h=8
n=64 x83 non-antipodal certifier; do not spend time reproving h=4 rigidity.

## T4 h=5 finite-certificate coverage audit

Stage selected: convert the h=5 selected-row certificate pile into a precise
coverage table.  This is a dossier/audit step, not a new h=5 theorem.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Digest:

```text
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
```

Result: the current h=5 evidence consists of exactly 20 complete selected
zero-row certificates:

```text
n=32:  7 primes
n=64:  5 primes
n=96:  1 prime
n=128: 7 primes
```

All rows have zero anchored toral trades, zero anchored nontoral trades, and no
direct `n^3` alarm.  The verifier also checks `p = 1 mod n`, `p > n^2`, and
the n=128 shard totals.  The selected rows cover 1,873,896,556 right-side
probes in total.  The audit explicitly records that this is not contiguous
prime coverage and not a uniform h=5 no-primitive theorem: up to the largest
certified prime, the n=32 and n=64 rows leave 395 and 689 admissible primes
uncertified, respectively.

Next step: either attack the symbolic h=5 norm-gate/no-primitive theorem, or
move to the h=8 n=64 x83 non-antipodal certifier residual.

## T4 h=8 residual-frontier audit

Stage selected: pin the h=8 n=64 residual after the x83 shell work.  This is a
frontier audit, not a new certificate search.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H8_RESIDUAL_FRONTIER_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_residual_frontier_audit.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_residual_frontier_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_h8_bonus_sweep_replay.py
```

Digest:

```text
H8_RESIDUAL_FRONTIER_AUDIT_PASS
H6_H8_BONUS_SWEEP_PASS
```

Result: h=8 has six complete n=32 zero-nontoral certificates, and the h=8 n=64
x83 radius-three shell is fully checked at `p=4289` and at the q3 prime
`p=262337`, processing `67,800,320` candidates per prime with `full_zero=0`.
The q3 suffix profile is `[67800000, 320, 0, 0, 0, 0, 0, 0]`, so the local
radius-three shell dies at obstruction depth two.  The two h=8 n=64 rows
remain partial (`boundary_n64_h8_p193` and `q3_n64_h8`); a blind n=64 h=8
join would require `binom(63,7)=553,270,671` left records, about `16.49 GiB` at
32 bytes/record, before the `binom(63,8)` right scan.  The honest next step is
therefore an x83-keyed non-antipodal certifier or a true external/sharded join,
not a local blind hash table.

Next step: return to the symbolic h=5 norm-gate/no-primitive theorem, or start
designing the h=8 x83-keyed non-antipodal join.

## T4 h=8 x83 support-certifier reduction

Stage selected: prove the bookkeeping reduction that lets the h=8 n=64
residual be attacked at the support level instead of by a blind left/right
signature join.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H8_X83_SUPPORT_CERTIFIER_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_x83_support_certifier_reduction.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_x83_support_certifier_reduction.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_residual_frontier_audit.py
```

Digest:

```text
H8_X83_SUPPORT_CERTIFIER_REDUCTION_PASS
H8_RESIDUAL_FRONTIER_AUDIT_PASS
```

Result: if a 16-support `R` satisfies the x83 full-zero condition
`L_R = S_R^2 - lambda` with nonzero square `lambda=alpha^2`, then the roots of
`S_R-alpha` and `S_R+alpha` canonically split `R` into the two h=8 trade sides.
Conversely, any h=8 trade pair gives this x83 factorization.  The replay
recovers all banked paid square-lift supports at `p=193,4289,262337` and rejects
a fixed nonzero-control support.  Therefore a future non-antipodal
support-level x83 certificate is sound; it does not need the `binom(63,7)`
blind left table.

Next step: implement or specify the actual h=8 non-antipodal support
enumerator, or return to the h=5 symbolic no-primitive theorem.

## T1 h=3 rich-curve log-jet reduction

Stage selected: remove one of the two named h=3 T1 gates by proving the
reduced derivative condition count for degree-2 rational signature curves.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RICH_CURVE_LOGJET_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_logjet_reduction.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_logjet_reduction.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_reduced_condition_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H3_RICH_CURVE_LOGJET_REDUCTION_PASS
H3_RICH_CURVE_REDUCED_CONDITION_COMPILER_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: for `m(X)=X^a prod_i (P_i/Q_i)^(h b_i)` and
`S=X prod_i P_i Q_i`, the recurrence

```text
W_0=1,     W_{j+1}=S W_j' + (M-jS')W_j,
M = S d(log m)/dX
```

gives `S^j m^(j)=m W_j` and `deg W_j <= 12j` for degree-2 rational maps.
At subgroup-admissible points, `m=X^a`, so each derivative-order condition is
over-imposed by a polynomial of degree `< A+12D`.  This proves `RC-RED(13)`.
The h=3 T1 wall is now the nonvanishing gate `RC-NV` plus constants, not the
reduced-condition count.

## T1 h=3 nonvanishing rank audit

Stage selected: repair the statement of the remaining nonvanishing gate after
`RC-RED(13)`.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RICH_CURVE_NV_RANK_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_nv_rank_audit.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_nv_rank_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H3_RICH_CURVE_NV_RANK_AUDIT_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: full injectivity of the h=3 substitution map is not the right `RC-NV`
target.  In the first three compiler rows, `A B^3` exceeds the direct-sum
one-variable image cap `|Z|(L+1)`, so the substitution map has a nontrivial
kernel for dimension reasons.  The sufficient and exact target is rank-form
nonvanishing:

```text
rank(S_Z) > 13 D (A + D) |Z|.
```

All audited compiler rows have positive image-cap room above this condition
count.  The next T1 theorem should therefore prove this rank lower bound after
the degeneracy filters, not full coefficient-box injectivity.

## T1 h=3 rank-form finite-field sample

Stage selected: test whether the corrected rank-form nonvanishing target
separates the known collapsed family from a repaired degree-2 sample.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RICH_CURVE_RANK_SAMPLE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_rank_sample.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_rank_sample.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H3_RICH_CURVE_RANK_SAMPLE_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: in the toy row `p=769, h=32, A=5, B=4, D=1`, the condition count is
`78`.  The collapsed constant-ratio family `X,3X,5X` has substitution rank
`50` and fails the rank target; the deterministic repaired random degree-2
curve has full coefficient rank `320` and passes.  This is sample evidence
only, but it checks that `RC-RANK` is aimed at the same degeneracy geometry as
the previous filters.
