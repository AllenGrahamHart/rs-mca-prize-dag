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

## T1/T3 h=3 rank-form parameter compiler

Stage selected: compile the current diagonal Stepanov parameter boxes under
the rank-form nonvanishing assumption.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RANK_PARAMETER_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rank_parameter_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rank_parameter_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H3_RANK_PARAMETER_COMPILER_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: assuming `RC-RANK`, the exact diagonal-box compiler verifies
`conditions < coeffs` and `conditions < image_cap` for representative rows and
prints the conditional bound `sum_z T(z) <= |Z|L/D`.  The high official rows
have real arithmetic slack: for `n=2^41`, the table gives `0.282n` at
`|Z|=256` and `0.647n` at `|Z|=512`.  This does not prove `H3-ACT(C)`; the
remaining missing ingredients are the actual rank theorem and the geometric
batching/charging map from h=3 activated shapes to repaired curve families.

## T1/T2 h=3 bridge-budget compiler

Stage selected: compile the maximum repaired curve-family size tolerated by
the current diagonal Stepanov arithmetic while still implying `H3-ACT(16)`.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_BRIDGE_BUDGET_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H3_BRIDGE_BUDGET_COMPILER_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: under `RC-RANK`, if row `n=2^s` batches activated h=3 shape pairs into
at most `Z_budget(s)` repaired curves, then `H3-ACT(16)` follows.  The verified
budgets include `Z_budget(13)=11`, `Z_budget(20)=58`, `Z_budget(23)=116`,
`Z_budget(32)=927`, and `Z_budget(39)=Z_budget(40)=Z_budget(41)=4529` under
the diagonal search with `B_max=20000`.  This does not prove the geometric
batching theorem; it makes the missing bridge numerically explicit.

## T2 h=3 pair-coprimality pilot integrated replay

Stage selected: promote the existing exact n=96 ladder pilot into the aggregate
F3 interim replay.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_PAIR_COPRIMALITY_PILOT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_coprimality_pilot.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_coprimality_pilot.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H3_PAIR_COPRIMALITY_PILOT_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the exact seven-prime n=96 ladder has three activated shapes, each
activating at exactly one threshold prime.  Their common obstruction norm
factors are `{1153,9601}`, `{97,13249}`, and `{18433}`; the extra rational norm
factors are below threshold.  This reinforces the prime-ideal/common-root
formulation and keeps the aggregate replay aware of the local norm-factor
evidence.

## T1 h=3 private-divisor full-rank refutation

Stage selected: test and falsify a tempting shortcut to the remaining
rank-form nonvanishing theorem.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_PRIVATE_DIVISOR_FULL_RANK_REFUTATION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_divisor_full_rank_refutation.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_divisor_full_rank_refutation.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H3_PRIVATE_DIVISOR_FULL_RANK_REFUTATION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the constructed curve
`(X-2)/(X-3), (X-5)/(X-7), (X-11)/(X-13)` has private zeros for
`X,r_1,r_2,r_3`, but its exact substitution rank in the toy box
`p=769,h=32,A=5,B=4,D=1` is `293 < 320`.  Therefore private divisors do not
imply full coefficient-rank injectivity.  The weaker toy rank target still
holds (`78 < 293`), so this only refutes the overstrong proof route.

## T4 h=8 support-universe compiler

Stage selected: quantify the h=8 n=64 non-antipodal support target after the
x83 support-to-trade reduction.  This is exact combinatorial bookkeeping, not a
new search.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H8_SUPPORT_UNIVERSE_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_support_universe_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_support_universe_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H8_SUPPORT_UNIVERSE_COMPILER_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the anchored h=8 n=64 support universe has
`binom(63,15) = 122,131,734,269,895` supports.  The antipodal subfamily has
`binom(31,7) = 2,629,575`, leaving `122,131,731,640,320` anchored
non-antipodal supports.  The seven-support paid-branch radius `<= 3` shell
workload is `68,753,223`, about `0.562943` ppm of the non-antipodal universe.
This pins the residual: local shell certificates are useful evidence, but h=8
closure still needs a global x83 support-key certificate or an external/sharded
join.

## T4 h=8 rotation-orbit compiler

Stage selected: quantify the largest safe symmetry reduction that does not need
an unproved exponent-unit invariance claim.  Root scaling preserves the x83
support condition, so cyclic rotations are safe to quotient by.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H8_ROTATION_ORBIT_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_rotation_orbit_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_rotation_orbit_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H8_ROTATION_ORBIT_COMPILER_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: Burnside's lemma over the size-64 rotation group gives
`7,633,233,556,276` orbits of all 16-supports.  The antipodal subfamily has
`328,756` rotation orbits, so the safe rotation-quotiented non-antipodal target
still has `7,633,233,227,520` orbits.  This is only an average factor of about
`16` below the anchored non-antipodal support count; it is useful
canonicalization hygiene, not a feasible direct global enumeration route.

## T4 h=8 exponent-unit symmetry falsifier

Stage selected: test the tempting larger support-canonicalization group
`e -> ue mod 64`.  The rotation compiler deliberately avoided this quotient
because the x83 equations are polynomial in the actual roots, not just in the
abstract cyclic group.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H8_EXPONENT_UNIT_FALSIFIER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_exponent_unit_falsifier.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_exponent_unit_falsifier.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H8_EXPONENT_UNIT_FALSIFIER_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: at `p=193`, the banked full-zero support
`{0,1,2,9,10,16,24,25,32,33,34,41,42,48,56,57}` maps under the exponent unit
`u=3` to `{0,3,6,8,11,16,27,30,32,35,38,40,43,48,59,62}`, whose obstruction
vector is `[0,180,0,60,0,20,0]` and whose `lambda=30` is nonsquare.  Therefore
arbitrary exponent-unit maps are not x83 support symmetries.  The h=8 global
certifier can safely use root-scaling rotations, but not the full exponent-unit
group without rechecking each image.

## T4 h=5 certificate coverage integrated replay

Stage selected: integrate the existing h=5 certificate coverage audit into the
main lightweight F3 replay.  h=5 is one of the three explicit promotion
blockers, and the selected-row certificates should be visible in the aggregate
status rather than only in a side replay.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the audit verifies `20` complete h=5 zero rows and
`1,873,896,556` total right-side probes.  The selected-row limitation is now
explicit in the aggregate report: up to the largest certified primes, the bank
misses `395` admissible primes for `n=32` and `689` for `n=64`; the `n=96` and
`n=128` evidence remains boundary/nearby-window evidence, not a uniform theorem.

## T4 h=8 x83 interface and one-exchange shell integrated replay

Stage selected: integrate the existing h=8 x83 obstruction interface and the
complete one-exchange shell check into the main lightweight F3 replay.  These
are light enough to run locally and they are the front-end for the remaining
support-certifier target.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H8_N64_X83_OBSTRUCTION_INTERFACE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H8_N64_X83_NEARLIFT_SHELL.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_obstruction_interface.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_nearlift_shell.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H8_N64_X83_INTERFACE_PASS
H8_N64_X83_NEARLIFT_SHELL_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the aggregate replay now checks that the paid antipodal h=8 branch is
aligned with x83 obstructions at `p in {193,4289,262337}`, deterministic
non-antipodal samples have no full zero at the two boundary-style primes, and
the complete one-exchange shell around the seven paid supports at each of
`p=4289,262337` has `full_zero=0`.  The radius-two shell remains a separate
heavier replay, not part of the aggregate.

## T1 h=3 rich-curve guard integration

Stage selected: integrate the already-banked h=3 denominator and degeneracy
guard packets into the aggregate F3 replay.  These are prerequisites for a
sound `RC-RANK` theorem statement: the denominator bound fixes the degree
budget, and the degeneracy guards prevent collapsed multiplicative-dependence
families from being treated as rich-curve input.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RICH_CURVE_DENOMINATOR_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RICH_CURVE_DEGENERACY_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RICH_CURVE_DEGENERACY_FILTER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_denominator_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_degeneracy_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_degeneracy_filter.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H3_RICH_CURVE_DENOMINATOR_COMPILER_PASS
H3_RICH_CURVE_DEGENERACY_AUDIT_PASS
H3_RICH_CURVE_DEGENERACY_FILTER_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the aggregate replay now checks the degree-clearing identity
`deg <= (A-1)+6h(B-1)` and the collapsed-ratio obstruction before the
reduced-condition/rank-form packets.  The h=3 blocker remains `RC-RANK` plus
the geometric batching bridge, but the replayed theorem surface now includes
the hypotheses needed to state that target honestly.

## T1/T2 h=3 bridge-budget parameter lift

Stage selected: rerun the h=3 bridge-budget compiler with a larger exact
diagonal search cap.  This is pure integer arithmetic and directly relaxes the
missing geometric batching theorem at the largest official rows.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_BRIDGE_BUDGET_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H3_BRIDGE_BUDGET_COMPILER_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: raising the diagonal search cap from `B_max=20000` to `B_max=50000`
keeps the official budgets unchanged through `s=38` and improves the large-row
bridge contracts:

```text
s=39: Z_budget 4529 -> 4674
s=40: Z_budget 4529 -> 5889
s=41: Z_budget 4529 -> 7420
```

The compiler still verifies maximality in its stated search box:
`Z_budget` passes and `Z_budget+1` fails.  This does not prove the geometric
batching theorem, but it gives that theorem more room exactly where the prior
table had plateaued.

## T1/T2 h=3 bridge-budget verifier optimization

Stage selected: keep the improved `B_max=50000` bridge budgets while bringing
the aggregate replay back under the light-compute ceiling with room to spare.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_BRIDGE_BUDGET_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H3_BRIDGE_BUDGET_COMPILER_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the bridge compiler now verifies each `Z_budget` with a pinned passing
diagonal-box witness and still exhaustively scans `Z_budget+1` under
`B_max=50000` to prove failure.  Monotonicity in `Z` then gives the same
maximality claim inside the stated search box, while reducing the standalone
runtime from about `2.9s` to about half that.

## T1/T2 h=3 interim-report sync

Stage selected: keep the main F3 interim report aligned with the stronger
bridge-budget verifier.

Banked file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Change: the h=3 bridge-budget section now states the precise current status:
`Z_budget` is verified by a pinned passing witness, `Z_budget+1` is exhaustively
replayed as failing in the `B_max=50000` diagonal search box, and monotonicity
therefore gives maximality only inside that stated box.  The report still keeps
`RC-RANK`, geometric batching, and other Stepanov parameter families as open.

## T3 h=3 bridge-budget B_max stress

Stage selected: test whether the current bridge budgets are merely an artifact
of the `B_max=50000` diagonal search cap.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_BRIDGE_BUDGET_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_bmax_stress.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_bmax_stress.py
```

Digest:

```text
H3_BRIDGE_BUDGET_BMAX_STRESS_PASS
```

Result: the stress verifier recomputes `Z_budget+1` for every official exponent
with `B_max=500000`, and every next budget still fails.  By monotonicity in
`Z`, no larger bridge family passes inside this ten-times-larger diagonal box.
The closest stressed failures are `s=13,14,15,16,18`, with margins
`6297, 9836, 22892, 51554, 53037` respectively.

## T3 h=3 non-diagonal low/mid-row budget lift

Stage selected: optimize the h=3 bridge-budget arithmetic beyond the
conservative diagonal `A=D` boxes, starting with the low and middle official
rows where the batching budget is tightest.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_NONDIAGONAL_LOWROW_BUDGET.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_nondiagonal_lowrow_budget.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_nondiagonal_lowrow_budget.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Digest:

```text
H3_NONDIAGONAL_LOWROW_BUDGET_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: for `s=13..35`, exact non-diagonal optimization
raises the bridge budgets

```text
11,14,18,23,29,36,46,58,73,92,116
  -> 16,21,26,33,42,53,67,84,106,134,168

146,184,232,292,368,463
  -> 212,267,337,425,535,674

584,736,927,1168,1472,1855
  -> 850,1071,1349,1700,2142,2699.
```

The verifier checks a passing witness at the improved `Z` and an exhaustive
`Z+1` failure up to the exact analytic `B` cap for any possible passing box.
The largest cap in these rows is `B <= 15470`, so this also removes the fixed
`B <= 50000` caveat from the low/mid-row packet.  This reduces the low/mid-row
geometric batching burden; it does not close `RC-RANK` or the bridge theorem.

## T3 h=3 high-row non-diagonal budget lift

Stage selected: bank the next verified non-diagonal bridge-budget rows and,
after the analytic-cap speedup, include them in the aggregate interim replay.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_NONDIAGONAL_HIGHROW_BUDGET.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_nondiagonal_highrow_budget.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_nondiagonal_highrow_budget.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digest:

```text
H3_NONDIAGONAL_HIGHROW_BUDGET_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: for `s=36..41`, exact non-diagonal optimization with `B <= 50000`
raises the bridge budgets

```text
2337,2944,3710,4674,5889,7420 -> 3400,4284,5397,6800,8568,10795.
```

The high-row verifier checks a passing witness at the improved `Z` and an
exhaustive `Z+1` failure up to the exact analytic `B` cap for any possible
passing box.  The largest cap in these rows is `B <= 61923`, so the check
remains light while removing the fixed `B <= 50000` caveat for this
high-row packet.  This further reduces the h=3 batching burden, still
conditional on `RC-RANK` and the actual geometric bridge theorem.

## T1 h=3 rank-sample family corollary

Stage selected: strengthen the existing `RC-RANK` finite-field sample without
adding a slow multi-curve computation.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RICH_CURVE_RANK_SAMPLE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_rank_sample.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_rank_sample.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digest:

```text
H3_RICH_CURVE_RANK_SAMPLE_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the existing repaired random curve has rank `320`, the full coefficient
dimension in the toy box `p=769, h=32, A=5, B=4, D=1`.  Therefore any direct-sum
family containing it has rank at least `320`, so the toy family-level
`RC-RANK` inequality holds for `Z <= 4`; `Z=5` is impossible for these fixed
parameters because `5*78 > 320`.  This is sample evidence only, not `RC-RANK`.

## T4 h=8 dihedral-reflection symmetry falsifier

Stage selected: strengthen the h=8 certifier-design guardrail by testing the
most tempting extension of rotation symmetry, namely exponent reflection.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H8_EXPONENT_UNIT_FALSIFIER.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H8_ROTATION_ORBIT_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_exponent_unit_falsifier.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_exponent_unit_falsifier.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digest:

```text
H8_EXPONENT_UNIT_FALSIFIER_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the same banked `p=193` x83 full-zero support refutes both the unit
map `e -> 3e mod 64` and reflection `e -> -e mod 64`.  The reflected support
has obstruction vector `[0, 64, 0, 82, 0, 87, 0]` and nonsquare
`lambda = 125`, so the h=8 support certifier cannot soundly quotient by the
dihedral exponent group without rechecking the x83 classifier.

## T4 h=8 near-lift radius-two expectation hardening

Stage selected: harden the h=8 near-lift shell verifier so the already-banked
radius-one and radius-two shell rows are asserted, not merely printed.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H8_N64_X83_NEARLIFT_SHELL.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_nearlift_shell.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_nearlift_shell.py
F3_H8_X83_SHELL_RADIUS=2 F3_H8_X83_SHELL_PRIMES=4289 \
  python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_nearlift_shell.py
F3_H8_X83_SHELL_RADIUS=2 F3_H8_X83_SHELL_PRIMES=262337 \
  python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_nearlift_shell.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H8_N64_X83_NEARLIFT_SHELL_PASS
H8_N64_X83_NEARLIFT_RADIUS2_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the verifier now asserts the four pinned shell rows:

```text
p=4289,r=1:   supports=5,376   first_zero=0    full_zero=0
p=262337,r=1: supports=5,376   first_zero=0    full_zero=0
p=4289,r=2:   supports=947,520 first_zero=1504 full_zero=0
p=262337,r=2: supports=947,520 first_zero=1344 full_zero=0
```

The final single-prime radius-two replays took 33.19s and 38.06s locally, so they are
kept as standalone commands rather than folded into the default aggregate.

## T4 h=5 n32 contiguous-prefix certificate expansion

Stage selected: convert the h=5 `n=32` evidence from sparse selected primes to
a certified contiguous low-prime prefix, while keeping the replay local and
under the 60-second cap.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N32_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N32_MULTIROW_CERTIFICATE_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the `n=32,h=5` certificate bank now covers every admissible prime
`p = 1 mod 32` with `32^2 < p <= 8161`, plus the previous high selected rows
`{12289, 32801, 40961, 61441, 65537}`.  This is `56` complete zero rows at
`n=32`, up from `7`.  The full generator replay took `33.05s` locally and
processed `9,515,016` total right-side subsets.  The h=5 coverage audit now
checks `69` total complete zero rows and `1,882,222,195` total right-side
probes; remaining missing admissible primes up to the current max are `346` for
`n=32` and `689` for `n=64`.

## T4 h=5 n64 contiguous-prefix certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from sparse
selected primes to a certified contiguous low-prime prefix, while keeping the
full generator under the local 60-second cap.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_MULTIROW_CERTIFICATE_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the `n=64,h=5` certificate bank now covers every admissible prime
`p = 1 mod 64` with `64^2 < p <= 6337`, plus the previous high selected rows
`{12289, 40961, 65537, 262337}`.  This is `13` complete zero rows at `n=64`,
up from `5`.  The full generator replay took `52.45s` locally and processed
`91,375,011` total right-side subsets.  The h=5 coverage audit now checks `77`
total complete zero rows and `1,938,452,971` total right-side probes; remaining
missing admissible primes up to the current max are `346` for `n=32` and `681`
for `n=64`.

## T4 h=5 n32 second-prefix certificate expansion

Stage selected: extend the h=5 `n=32` contiguous low-prime certificate prefix
from `p <= 8161` through `p <= 12289`, while keeping the full generator under
the local 60-second cap.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N32_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N32_MULTIROW_CERTIFICATE_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the `n=32,h=5` certificate bank now covers every admissible prime
`p = 1 mod 32` with `32^2 < p <= 12289`, plus the previous high selected rows
`{32801, 40961, 61441, 65537}`.  This is `85` complete zero rows at `n=32`,
up from `56`.  The generator now compiles its C++ checker once per run and
passes the prime at runtime; the full replay took `5.20s` locally and processed
`14,442,435` total right-side subsets.  The h=5 coverage audit now checks `106`
total complete zero rows and `1,943,380,390` total right-side probes; remaining
missing admissible primes up to the current max are `317` for `n=32` and `681`
for `n=64`.

## T4 h=5 n64 second-prefix certificate expansion

Stage selected: extend the h=5 `n=64` contiguous low-prime certificate prefix
from `p <= 6337` through `p <= 6977`.  A larger local extension was not attempted
because the 15-row replay already runs close to the 60-second cap.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_MULTIROW_CERTIFICATE_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the `n=64,h=5` certificate bank now covers every admissible prime
`p = 1 mod 64` with `64^2 < p <= 6977`, plus the previous high selected rows
`{12289, 40961, 65537, 262337}`.  This is `15` complete zero rows at `n=64`,
up from `13`.  The generator now compiles its C++ checker once per run and
passes the prime at runtime; the full replay took `56.08s` locally and
processed `105,432,705` total right-side subsets.  The h=5 coverage audit now
checks `108` total complete zero rows and `1,957,438,084` total right-side
probes; remaining missing admissible primes up to the current max are `317` for
`n=32` and `679` for `n=64`.

## T4 h=5 n32 complete-to-current-max certificate expansion

Stage selected: extend the h=5 `n=32` certificate bank from the low-prime prefix
plus selected high rows to every admissible prime through the current certified
maximum `65537`.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N32_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N32_MULTIROW_CERTIFICATE_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the `n=32,h=5` certificate bank now covers every admissible prime
`p = 1 mod 32` with `32^2 < p <= 65537`.  This is `402` complete zero rows at
`n=32`, up from `85`, and there are no missing admissible primes up to the
current maximum certified n=32 prime.  The generator's default replay is now
compact and writes the JSON without printing every row; it took `19.18s`
locally and processed `68,304,222` total right-side subsets.  The h=5 coverage
audit now checks `425` total complete zero rows and `2,011,299,871` total
right-side probes; remaining missing admissible primes up to the current max
are `0` for `n=32` and `679` for `n=64`.

## T4 h=5 n64 chunked prefix-to-12289 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from prefix
coverage through `p <= 6977` to prefix coverage through `p <= 12289`, using two
explicit chunk replays so no local task exceeds the 60-second cap.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_12289_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_12289_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_12289_chunk_b.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_12289_chunk_b.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_12289_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_12289_chunk_b.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_MULTIROW_CERTIFICATE_PASS
H5_N64_PREFIX_12289_CHUNK_A_PASS
H5_N64_PREFIX_12289_CHUNK_B_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the `n=64,h=5` certificate bank now covers every admissible prime
`p = 1 mod 64` with `64^2 < p <= 12289`, plus the previous high selected rows
`{40961, 65537, 262337}`.  This is `36` complete zero rows at `n=64`, up from
`15`.  The two new chunks took `44.94s` and `48.75s` locally and processed
`147,605,787` additional right-side subsets.  The h=5 coverage audit now checks
`446` total complete zero rows and `2,158,905,658` total right-side probes;
remaining missing admissible primes up to the current max are `0` for `n=32`
and `658` for `n=64`.

## T4 h=5 n64 chunked prefix-to-20353 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from prefix
coverage through `p <= 12289` to prefix coverage through `p <= 20353`, again
using explicit chunks so no local certificate task exceeds the 60-second cap.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_20353_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_20353_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_20353_chunk_b.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_20353_chunk_b.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_20353_chunk_c.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_20353_chunk_c.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_20353_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_20353_chunk_b.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_20353_chunk_c.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_20353_CHUNK_A_PASS
H5_N64_PREFIX_20353_CHUNK_B_PASS
H5_N64_PREFIX_20353_CHUNK_C_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the `n=64,h=5` certificate bank now covers every admissible prime
`p = 1 mod 64` with `64^2 < p <= 20353`, plus the previous high selected rows
`{40961, 65537, 262337}`.  This is `63` complete zero rows at `n=64`, up from
`36`.  The three new chunks took `36.73s`, `36.66s`, and `25.98s` locally and
processed `189,778,869` additional right-side subsets.  The h=5 coverage audit
now checks `473` total complete zero rows and `2,348,684,527` total right-side
probes; remaining missing admissible primes up to the current max are `0` for
`n=32` and `631` for `n=64`.

## T1 h=3 rank-stress packet

Stage selected: strengthen the evidence around the remaining h=3 `RC-RANK`
gate rather than extending h=5 finite certificates again.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RICH_CURVE_RANK_STRESS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_rank_stress.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_rank_stress.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H3_RICH_CURVE_RANK_STRESS_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the focused verifier passes in `6.71s` locally.  It adds three exact
non-collapsed rank controls at `p=769,h=32,A=5,B=4,D=1`:

```text
private-divisor rational: rank=293 > 78
shifted polynomial:       rank=247 > 78
shared denominator:       rank=247 > 78
```

It also derives the duplicate-image warning: the private-divisor curve repeated
twice still passes (`293 > 156`), while repeating it four times fails
(`293 < 312`).  The default aggregate replay now includes this packet and still
passes in `41.32s` locally.

## T1 h=3 rank-effective bridge interface

Stage selected: repair the h=3 geometric bridge contract after the duplicate
rank warning.  The bridge must bound rank-effective curve-image capacity, not
raw multiplicity.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RANK_EFFECTIVE_BRIDGE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rank_effective_bridge.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_BRIDGE_BUDGET_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rank_effective_bridge.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H3_RANK_EFFECTIVE_BRIDGE_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: focused verifier passes in `0.01s` locally (`maxrss=10368`).  The
default aggregate replay includes this packet and still passes in `40.76s`
locally (`maxrss=98672`).

## T1 h=3 RC-RANK small-H guardrail

Stage selected: prevent the future `RC-RANK` theorem from being over-stated.
The rank-stress private-divisor curve is non-collapsed, but the same curve can
still fail the rank inequality at tiny subgroup orders.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RC_RANK_HFLOOR_GUARD.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rc_rank_hfloor_guard.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_BRIDGE_BUDGET_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_NONDIAGONAL_LOWROW_BUDGET.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_NONDIAGONAL_HIGHROW_BUDGET.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rc_rank_hfloor_guard.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H3_RC_RANK_HFLOOR_GUARD_PASS
H3_BRIDGE_BUDGET_COMPILER_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: focused guardrail verifier passes in `14.21s` locally
(`maxrss=23352`).  The bridge-budget compiler still passes in `1.33s`
locally after the rank-capacity wording update.  The default aggregate replay
is unchanged except for the bridge compiler wording and still passes in
`43.05s` locally (`maxrss=98636`).

## T1 h=3 private-linear degree-span explanation

Stage selected: sharpen the small-H guardrail from a table into an exact model
formula for the private linear-divisor control.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RC_RANK_HFLOOR_GUARD.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rc_rank_hfloor_guard.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rc_rank_hfloor_guard.py
```

Expected digest:

```text
H3_RC_RANK_HFLOOR_GUARD_PASS
```

Result: focused verifier passes in `14.15s` locally (`maxrss=23324`) and now
checks the formula `rank = min(A B^3, A + 3H(B-1))` for the private-linear
control.  The default aggregate replay still passes in `44.63s` locally
(`maxrss=98672`).

## T4 h=5 n64 prefix-to-23873 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from complete
prefix coverage through `p <= 20353` to prefix coverage through `p <= 23873`,
using one 10-prime local chunk.

Pre-registered primes:

```text
20929, 21121, 21313, 21377, 21569,
22273, 22721, 23041, 23297, 23873
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_23873_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_23873_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_23873_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_23873_CHUNK_A_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the new chunk passes in `47.09s` locally (`maxrss=86600`) and writes
10 complete zero rows.  The h=5 coverage audit now verifies `483` total
complete zero rows and `2,418,972,997` total right-side probes.  The `n=64`
bank covers every admissible prime through `p <= 23873`, plus
`{40961, 65537, 262337}`; remaining missing admissible primes up to the current
max are `621`.  The h4/h5 bonus replay now reports `73` n=64 complete zero
certificates and passes in `0.03s` locally.  The default aggregate replay still
passes in `42.06s` locally (`maxrss=98668`).

## T4 h=5 n64 prefix-to-26177 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from complete
prefix coverage through `p <= 23873` to prefix coverage through `p <= 26177`,
using one 8-prime local chunk.

Pre-registered primes:

```text
24001, 25153, 25409, 25537,
25601, 25793, 26113, 26177
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_26177_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_26177_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_26177_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_26177_CHUNK_A_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the new chunk passes in `36.51s` locally (`maxrss=86192`) and writes
8 complete zero rows.  The h=5 coverage audit now verifies `491` total
complete zero rows and `2,475,203,773` total right-side probes.  The `n=64`
bank covers every admissible prime through `p <= 26177`, plus
`{40961, 65537, 262337}`; remaining missing admissible primes up to the current
max are `613`.  The h4/h5 bonus replay now reports `81` n=64 complete zero
certificates and passes in `0.03s` locally.  The default aggregate replay still
passes in `42.74s` locally (`maxrss=98632`).

## T4 h=5 n64 prefix-to-28097 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from complete
prefix coverage through `p <= 26177` to prefix coverage through `p <= 28097`,
using one 7-prime local chunk.

Pre-registered primes:

```text
26497, 26561, 26881, 27073, 27329, 27457, 28097
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_28097_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_28097_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_28097_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_28097_CHUNK_A_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the new chunk passes in `33.21s` locally (`maxrss=86396`) and writes
7 complete zero rows.  The h=5 coverage audit now verifies `498` total
complete zero rows and `2,524,405,702` total right-side probes.  The `n=64`
bank covers every admissible prime through `p <= 28097`, plus
`{40961, 65537, 262337}`; remaining missing admissible primes up to the current
max are `606`.  The h4/h5 bonus replay now reports `88` n=64 complete zero
certificates and passes in `0.03s` locally.  The default aggregate replay still
passes in `41.14s` locally (`maxrss=98656`).

## T4 h=5 n64 prefix-to-30977 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from complete
prefix coverage through `p <= 28097` to prefix coverage through `p <= 30977`,
using one 7-prime local chunk.

Pre-registered primes:

```text
28289, 29569, 29633, 29761, 30529, 30593, 30977
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_30977_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_30977_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H4_H5_BONUS_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_30977_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_30977_CHUNK_A_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the new chunk passes in `31.09s` locally (`maxrss=86360`) and writes
7 complete zero rows.  The h=5 coverage audit now verifies `505` total
complete zero rows and `2,573,607,631` total right-side probes.  The `n=64`
bank covers every admissible prime through `p <= 30977`, plus
`{40961, 65537, 262337}`; remaining missing admissible primes up to the current
max are `599`.  The h4/h5 bonus replay reports `95` n=64 complete zero
certificates and passes in `0.04s` locally (`maxrss=14564`).  The default
aggregate replay still passes in `42.62s` locally (`maxrss=98672`).

## T4 h=5 n64 prefix-to-33601 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from complete
prefix coverage through `p <= 30977` to prefix coverage through `p <= 33601`,
using one 7-prime local chunk.

Pre-registered primes:

```text
31489, 31873, 32257, 32321, 32833, 33409, 33601
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_33601_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_33601_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H4_H5_BONUS_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_33601_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_33601_CHUNK_A_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the new chunk passes in `33.31s` locally (`maxrss=86120`) and writes
7 complete zero rows.  The h=5 coverage audit now verifies `512` total
complete zero rows and `2,622,809,560` total right-side probes, passing in
`0.06s` locally (`maxrss=13056`).  The `n=64` bank covers every admissible
prime through `p <= 33601`, plus
`{40961, 65537, 262337}`; remaining missing admissible primes up to the current
max are `592`.  The h4/h5 bonus replay reports `102` n=64 complete zero
certificates and passes in `0.05s` locally (`maxrss=14340`).  The default
aggregate replay still passes in `41.14s` locally (`maxrss=98548`).

## T4 h=5 n64 prefix-to-36161 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from complete
prefix coverage through `p <= 33601` to prefix coverage through `p <= 36161`,
using one 8-prime local chunk.

Pre-registered primes:

```text
33857, 34369, 35201, 35393, 35521, 35969, 36097, 36161
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_36161_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_36161_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H4_H5_BONUS_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_36161_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_36161_CHUNK_A_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the new chunk passes in `33.65s` locally (`maxrss=86588`) and writes
8 complete zero rows.  The h=5 coverage audit now verifies `520` total
complete zero rows and `2,679,040,336` total right-side probes, passing in
`0.07s` locally (`maxrss=12800`).  The `n=64` bank covers every admissible
prime through `p <= 36161`, plus
`{40961, 65537, 262337}`; remaining missing admissible primes up to the current
max are `584`.  The h4/h5 bonus replay reports `110` n=64 complete zero
certificates and passes in `0.05s` locally (`maxrss=14320`).  The default
aggregate replay still passes in `40.49s` locally (`maxrss=98656`).

## T4 h=5 n64 prefix-to-38977 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from complete
prefix coverage through `p <= 36161` to prefix coverage through `p <= 38977`,
using one 10-prime local chunk.

Pre-registered primes:

```text
36353, 36929, 37057, 37313, 37441, 37633, 37889, 38273, 38593, 38977
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_38977_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_38977_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H4_H5_BONUS_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_38977_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_38977_CHUNK_A_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Result: the new chunk passes in `39.40s` locally (`maxrss=86380`) and writes
10 complete zero rows.  The h=5 coverage audit now verifies `530` total
complete zero rows and `2,749,328,806` total right-side probes, passing in
`0.07s` locally (`maxrss=13056`).  The `n=64` bank covers every admissible
prime through `p <= 38977`, plus
`{40961, 65537, 262337}`; remaining missing admissible primes up to the current
max are `574`.  The h4/h5 bonus replay reports `120` n=64 complete zero
certificates and passes in `0.04s` locally (`maxrss=14576`).  The default
aggregate replay still passes in `43.90s` locally (`maxrss=98612`).

## T4 h=5 n64 prefix-to-40577 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from complete
prefix coverage through `p <= 38977` to prefix coverage through `p <= 40577`.
This deliberately stops before the already-selected high row `p=40961`, so the
expected-prime ledgers remain duplicate-free.

Pre-registered primes:

```text
39041, 39233, 39937, 40129, 40193, 40577
```

Planned replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_40577_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_40577_CHUNK_A_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_40577_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_40577_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H4_H5_BONUS_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Result: the new chunk passes in `25.41s` locally (`maxrss=86592`) and writes
6 complete zero rows.  The h=5 coverage audit now verifies `536` total
complete zero rows and `2,791,501,888` total right-side probes, passing in
`0.08s` locally (`maxrss=12928`).  The `n=64` bank covers every admissible
prime through `p <= 40577`, plus `{40961, 65537, 262337}`; remaining missing
admissible primes up to the current max are `568`.  The h4/h5 bonus replay
reports `126` n=64 complete zero certificates and passes in `0.04s` locally
(`maxrss=14584`).  The default aggregate replay still passes in `39.97s`
locally (`maxrss=98680`).

## T4 h=5 n64 prefix-to-40961 certificate expansion

Stage selected: fill the missing admissible prime `p=40897` between the
new `40577` prefix and the already-selected row `p=40961`.  This should turn
the `n=64` certificate bank into a duplicate-free contiguous admissible prefix
through `p <= 40961`, plus high selected rows `{65537,262337}`.

Pre-registered primes:

```text
40897
```

Planned replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_40961_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_40961_CHUNK_A_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_40961_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_40961_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H4_H5_BONUS_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Result: the new chunk passes in `4.85s` locally (`maxrss=86456`) and writes
1 complete zero row.  The h=5 coverage audit now verifies `537` total
complete zero rows and `2,798,530,735` total right-side probes, passing in
`0.07s` locally (`maxrss=12928`).  The `n=64` bank now covers every admissible
prime through `p <= 40961`, plus `{65537, 262337}`; remaining missing
admissible primes up to the current max are `567`.  The h4/h5 bonus replay
reports `127` n=64 complete zero certificates and passes in `0.08s` locally
(`maxrss=14576`).  The default aggregate replay still passes in `37.32s`
locally (`maxrss=98680`).

## T4 h=5 n64 prefix-to-44417 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from complete
prefix coverage through `p <= 40961` to prefix coverage through `p <= 44417`,
using one 10-prime local chunk.

Pre-registered primes:

```text
41281, 41729, 42433, 42689, 43201, 43457, 43649, 43777, 43969, 44417
```

Planned replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_44417_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_44417_CHUNK_A_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_44417_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_44417_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H4_H5_BONUS_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Result: the new chunk passes in `39.65s` locally (`maxrss=86520`) and writes
10 complete zero rows.  The h=5 coverage audit now verifies `547` total
complete zero rows and `2,868,819,205` total right-side probes, passing in
`0.06s` locally (`maxrss=13056`).  The `n=64` bank now covers every admissible
prime through `p <= 44417`, plus `{65537, 262337}`; remaining missing
admissible primes up to the current max are `557`.  The h4/h5 bonus replay
reports `137` n=64 complete zero certificates and passes in `0.04s` locally
(`maxrss=14412`).  The default aggregate replay still passes in `45.63s`
locally (`maxrss=98580`).

## T4 h=5 n64 prefix-to-48193 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from complete
prefix coverage through `p <= 44417` to prefix coverage through `p <= 48193`,
using one 12-prime local chunk.

Pre-registered primes:

```text
45121, 45377, 45569, 45697, 45953, 46273, 46337, 47041, 47297, 47681, 47809, 48193
```

Planned replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_48193_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_48193_CHUNK_A_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_48193_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_48193_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H4_H5_BONUS_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Result: the clean rerun after the disk-space interruption passes in `50.61s`
locally (`maxrss=85920`) and writes 12 complete zero rows.  The h=5 coverage
audit now verifies `559` total complete zero rows and `2,953,165,369` total
right-side probes, passing in `0.08s` locally (`maxrss=13184`).  The `n=64`
bank now covers every admissible prime through `p <= 48193`, plus
`{65537, 262337}`; remaining missing admissible primes up to the current max
are `545`.  The h4/h5 bonus replay reports `149` n=64 complete zero
certificates and passes in `0.04s` locally (`maxrss=14720`).  The default
aggregate replay still passes in `48.98s` locally (`maxrss=98668`).
