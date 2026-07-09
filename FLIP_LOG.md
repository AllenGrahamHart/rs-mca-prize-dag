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

## T4 h=5 n64 prefix-to-51521 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from complete
prefix coverage through `p <= 48193` to prefix coverage through `p <= 51521`.
The initial 10-prime local chunk hit the 60-second timeout, so the same
pre-registered prime set is split into two five-prime chunks.

Pre-registered primes:

```text
48449, 49409, 49537, 49921, 50177, 50497, 50753, 51137, 51329, 51521
```

Planned replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_51521_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_51521_chunk_b.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_51521_CHUNK_A_PASS
H5_N64_PREFIX_51521_CHUNK_B_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Timing gate:

```text
10-prime chunk attempt: timeout at 60.00s (`maxrss=86408`), no JSON emitted.
Proceeding with the two five-prime chunks above.
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_51521_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_51521_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_51521_chunk_b.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_51521_chunk_b.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H4_H5_BONUS_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Result: after the timeout split, chunk A passes in `30.76s` locally
(`maxrss=86544`) and chunk B passes in `32.69s` locally (`maxrss=86576`),
writing 10 complete zero rows total.  The h=5 coverage audit now verifies
`569` total complete zero rows and `3,023,453,839` total right-side probes,
passing in `0.10s` locally (`maxrss=13184`).  The `n=64` bank now covers every
admissible prime through `p <= 51521`, plus `{65537, 262337}`; remaining
missing admissible primes up to the current max are `535`.  The h4/h5 bonus
replay reports `159` n=64 complete zero certificates and passes in `0.08s`
locally (`maxrss=14604`).  The default aggregate replay still passes in
`50.25s` locally (`maxrss=98732`).

## T4 h=5 n64 prefix-to-53377 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from complete
prefix coverage through `p <= 51521` to prefix coverage through `p <= 53377`,
using one five-prime local chunk.

Pre-registered primes:

```text
51713, 52289, 52609, 52673, 53377
```

Planned replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_53377_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_53377_CHUNK_A_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_53377_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_53377_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H4_H5_BONUS_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Result: chunk A passes in `21.16s` locally (`maxrss=86196`), writing five
complete zero rows.  The h=5 coverage audit now verifies `574` total complete
zero rows and `3,058,598,074` total right-side probes, passing in `0.07s`
locally (`maxrss=13056`).  The `n=64` bank now covers every admissible prime
through `p <= 53377`, plus `{65537, 262337}`; remaining missing admissible
primes up to the current max are `530`.  The h4/h5 bonus replay reports `164`
n=64 complete zero certificates and passes in `0.04s` locally
(`maxrss=14476`).  The default aggregate replay still passes in `39.01s`
locally (`maxrss=98652`).

## T4 h=5 n64 prefix-to-54721 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from complete
prefix coverage through `p <= 53377` to prefix coverage through `p <= 54721`,
using one five-prime local chunk.

Pre-registered primes:

```text
53441, 53569, 53633, 54401, 54721
```

Planned replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_54721_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_54721_CHUNK_A_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_54721_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_54721_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H4_H5_BONUS_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Result: chunk A passes in `21.20s` locally (`maxrss=86728`), writing five
complete zero rows.  The h=5 coverage audit now verifies `579` total complete
zero rows and `3,093,742,309` total right-side probes, passing in `0.07s`
locally (`maxrss=13184`).  The `n=64` bank now covers every admissible prime
through `p <= 54721`, plus `{65537, 262337}`; remaining missing admissible
primes up to the current max are `525`.  The h4/h5 bonus replay reports `169`
n=64 complete zero certificates and passes in `0.03s` locally
(`maxrss=14616`).  The default aggregate replay still passes in `37.65s`
locally (`maxrss=98792`).

## T4 h=5 n64 prefix-to-57793 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from complete
prefix coverage through `p <= 54721` to prefix coverage through `p <= 57793`,
using one five-prime local chunk.

Pre-registered primes:

```text
55681, 56897, 57089, 57601, 57793
```

Planned replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_57793_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_57793_CHUNK_A_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_57793_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_57793_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H4_H5_BONUS_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Result: chunk A passes in `20.43s` locally (`maxrss=86332`), writing five
complete zero rows.  The h=5 coverage audit now verifies `584` total complete
zero rows and `3,128,886,544` total right-side probes, passing in `0.07s`
locally (`maxrss=13056`).  The `n=64` bank now covers every admissible prime
through `p <= 57793`, plus `{65537, 262337}`; remaining missing admissible
primes up to the current max are `520`.  The h4/h5 bonus replay reports `174`
n=64 complete zero certificates and passes in `0.04s` locally
(`maxrss=14616`).  The default aggregate replay still passes in `37.22s`
locally (`maxrss=98692`).

## T4 h=5 n64 prefix-to-60161 certificate expansion

Stage selected: extend the h=5 `n=64` finite certificate bank from complete
prefix coverage through `p <= 57793` to prefix coverage through `p <= 60161`,
using one five-prime local chunk.

Pre-registered primes:

```text
58049, 58369, 59009, 59393, 60161
```

Planned replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_60161_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digests:

```text
H5_N64_PREFIX_60161_CHUNK_A_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_60161_chunk_a.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_60161_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CERTIFICATE_COVERAGE_AUDIT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H4_H5_BONUS_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

Result: chunk A passes in `19.88s` locally (`maxrss=86360`), writing five
complete zero rows.  The h=5 coverage audit now verifies `589` total complete
zero rows and `3,164,030,779` total right-side probes, passing in `0.07s`
locally (`maxrss=13312`).  The `n=64` bank now covers every admissible prime
through `p <= 60161`, plus `{65537, 262337}`; remaining missing admissible
primes up to the current max are `515`.  The h4/h5 bonus replay reports `179`
n=64 complete zero certificates and passes in `0.04s` locally
(`maxrss=14740`).  The default aggregate replay still passes in `37.57s`
locally (`maxrss=98672`).

## T1/T2 h=3 RC-RANK model-lemma repair

Stage selected: stop linear h=5 prefix expansion and sharpen the h=3
`RC-RANK` theorem statement.  The new packet records the algebraic part of the
rank guardrails:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RC_RANK_MODEL_LEMMAS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rc_rank_model_lemmas.py
```

Pre-registered claims:

```text
1. Constant-ratio collapsed curves have exact rank
   |{a + Hs : 0 <= a < A, 0 <= s <= 3(B-1)}|.
2. Private-linear cleared substitutions have rank at most
   min(A B^3, A + 3H(B-1)).
3. Therefore any private-linear RC-RANK theorem needs an explicit H-floor;
   in the toy box A=5,B=4,D=1 the first possible one-curve pass is H=9.
```

Result: this does not prove `RC-RANK`, but it proves the model obstruction
behind the existing finite-field guardrail.  The remaining h=3 lower-bound
target is now sharper: prove private-linear degree-space fullness, or a weaker
rank lower bound still beating `13D(A+D)|Z|`, under explicit repaired
signature-curve hypotheses.  The standalone replay passes in `0.01s` locally
(`maxrss=10624`), and the default aggregate replay passes with the new packet
included in `37.07s` locally (`maxrss=98584`).

## T1/T2 h=3 RC-RANK generic-open reduction

Stage selected: turn the private-linear rank target into a precise algebraic
avoidance statement rather than another finite sample.

New packet:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RC_RANK_GENERIC_OPEN.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rc_rank_generic_open.py
```

Pre-registered claims:

```text
1. For fixed A,B,D,H, rank >= r is equivalent to nonvanishing of at least one
   r-minor of the universal cleared-substitution matrix.
2. The pinned private-linear finite-field witness has rank
   293 = A + 3H(B-1), so the private-linear degree-space-fullness open set is
   nonempty in the toy box.
3. The remaining F3 theorem is an avoidance theorem: show the repaired
   signature-curve parameter image lies in a rank-good minor open set with
   enough rank-effective capacity.
```

Result: this is not `RC-RANK`, but it removes a vacuity concern.  The next
symbolic target is `F3-RANK-AVOID`, not full injectivity and not raw
private-divisor counting.  The standalone replay passes in `2.81s` locally
(`maxrss=18688`), and the default aggregate replay passes with this packet
included in `40.56s` locally (`maxrss=98796`).

Follow-up: the generic-open verifier now also consumes the deterministic
repaired degree-2 random curve from the rank-sample packet.  Its exact rank is
`320 = A B^3`, so the repaired degree-2 full coefficient-rank open set is
nonempty in the same toy box.  This aligns the generic-open packet with the
degree-2 rank room used by the current non-diagonal compiler.  The standalone
generic-open replay now passes in `11.10s` locally (`maxrss=22712`).  The
default aggregate replay remains under the cap but is now close, passing in
`53.61s` locally (`maxrss=98752`); future aggregate additions should replace or
merge checks rather than simply adding runtime.

Follow-up runtime repair: the degree-2 random rank is now consumed as a pinned
input from `F3_H3_RICH_CURVE_RANK_SAMPLE.md` instead of being recomputed inside
the generic-open verifier.  The aggregate replay still checks that exact rank
through the rank-sample packet before the generic-open packet runs.  The
standalone generic-open replay is back down to `2.92s` locally
(`maxrss=18688`), and the default aggregate replay passes in `43.86s` locally
(`maxrss=98664`).

## T1/T2 h=3 private-linear compiler guard

Stage selected: audit whether a private-linear rank theorem would be strong
enough to justify the current non-diagonal h=3 bridge compiler.

New packet:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_PRIVATE_LINEAR_COMPILER_GUARD.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_compiler_guard.py
```

Result: every current official non-diagonal witness row `s=13..41` needs the
full degree-2 rank room `A + 6n(B-1)`; its per-curve condition count is larger
than the private-linear degree room `A + 3n(B-1)`.  Therefore the next theorem
route must split cleanly:

```text
prove degree-2 repaired-curve rank, or
rerun the compiler under the private-linear degree cap.
```

The verifier also checks representative private-linear retuned passing boxes at
`s in {13,16,20,23,32,41}`.  These are not maximality claims; they only show
the private-linear route is not vacuous.  Standalone replay passes in `0.02s`
locally (`maxrss=12928`), and the default aggregate replay passes with this
packet included in `46.09s` locally (`maxrss=98796`).

## T1/T2 h=3 rank-avoidance interface

Stage selected: pin the exact theorem interface that would turn the current
h=3 non-diagonal compiler into `H3-ACT(16)`.

New packet:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RANK_AVOID_INTERFACE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rank_avoid_interface.py
```

Result: the packet verifies that the current improved `Z_budget` table covers
every official exponent `s=13..41`, with `Z_budget(13)=16` and
`Z_budget(41)=10795`, and checks the pinned witness inequalities for every
row.  The remaining h=3 theorem pair is now stated as:

```text
F3-RANK-AVOID + H3-BRIDGE-RANKCAP(Z_budget(s)) => H3-ACT(16).
```

This is an interface pin, not a proof of either remaining theorem.  Standalone
replay passes in `0.04s` locally (`maxrss=12928`).  The default aggregate
replay passes with this packet included in `53.00s` locally (`maxrss=98768`).

## T2 h=3 activation symmetry lemma

Stage selected: bank a bridge-side symmetry lemma used by the activation
deduplication and future geometric batching theorem.

New packet:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_ACTIVATION_SYMMETRY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_activation_symmetry.py
```

Result: affine/unit exponent maps and side swap preserve the h=3 activation
predicate when the primitive-root embedding is transformed contragrediently.
The packet explicitly records that activation need not be invariant at a fixed
chosen generator.  The verifier checks finite-field samples over
`p in {97,193,577,769}` and all `720` banked activation records.  Standalone
replay passes in `0.17s` locally (`maxrss=13184`).  The default aggregate
replay passes with this packet included in `41.36s` locally (`maxrss=98780`).

## T1 h=3 hyperbola-line degeneracy classifier

Stage selected: close a bridge-side theorem-statement ambiguity without adding
another numerical search.  The repaired h=3 rich-curve route already names
toral, constant-ratio, and hyperbola-line cells as the exceptional geometry
that must be paid or excluded before `RC-RANK` is applied.  The constant-ratio
cell was already operationalized; this packet classifies the hyperbola-line
cell exactly.

New packet:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_HYPERBOLA_LINE_DEGENERACY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_hyperbola_line_degeneracy.py
```

Result: in the h=3 hyperbola normal form,

```text
Delta = a^2/3 - b.
```

Thus the rational-line degeneration over a field containing `omega` is exactly
the codimension-one cell `b=a^2/3`.  On that cell,

```text
G_F(u,v)
  = (u - omega v + a(1 - omega)/3)
    (u - omega^2 v + a(omega + 2)/3).
```

For `Delta != 0`, the affine conic `XY=Delta` is irreducible.  This does not
prove the activation bound, but it makes the hyperbola-line exclusion precise
for the eventual bridge/rank theorem.  Standalone replay passes in `0.31s`
locally (`maxrss=49876`).  The default aggregate replay passes with this packet
included in `40.83s` locally (`maxrss=98668`).

## T4 h=8 antipodal x83 quotient reduction

Stage selected: bank a symbolic reduction that keeps the h=8 n=64 residual
focused on primitive non-antipodal supports.  The existing x83 interface
verified the paid antipodal square-lift branch at three primes; this packet
proves the quotient mechanism behind that behavior.

New packet:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H8_ANTIPODAL_X83_QUOTIENT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_antipodal_x83_quotient.py
```

Result: if `R` is an antipodal 16-support in `mu_64`, then

```text
L_R(X) = M_A(X^2)
```

for its quotient 8-support `A` in `mu_32`.  The forced square-root recursion
commutes with this substitution:

```text
S_R(X) = N_A(X^2),
obs_8(R) = (0, obs_4(A)_1, 0, obs_4(A)_2, 0, obs_4(A)_3, 0),
lambda_8(R) = lambda_4(A).
```

Therefore antipodal x83 full-zero supports are exactly h=4 quotient full-zero
supports lifted antipodally, and are paid by the h=4 quotient ledger.  The
remaining h=8 n=64 support certifier can restrict to non-antipodal supports.
Standalone replay passes in `0.25s` locally (`maxrss=14080`).  The default
aggregate replay passes with this packet included in `50.53s` locally
(`maxrss=98772`).

## T1 h=3 RC-RANK normalization invariance

Stage selected: bank a rank theorem hygiene lemma before any further
rank-avoidance attempt.  The future `F3-RANK-AVOID` theorem should be allowed
to choose convenient repaired curve representatives, but only along operations
that provably preserve the cleared substitution rank.

New packet:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RC_RANK_NORMALIZATION_INVARIANCE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rc_rank_normalization_invariance.py
```

Result: these normalizations are rank-safe:

```text
source affine reparametrization: X -> mX+t, m != 0
target coordinate scaling:      r_i -> c_i r_i, c_i != 0
target coordinate permutation:  (r_1,r_2,r_3) -> (r_pi(1),r_pi(2),r_pi(3))
target coordinate inversion:    r_i -> r_i^{-1}
```

The first acts by an invertible linear map on the cleared coefficient space
and preserves the `deg_X < A` source span; the second only rescales columns by
nonzero factors; the last two only permute the multi-index columns.  Therefore
these operations preserve the `RC-RANK` inequality.  This is not a proof of
`RC-RANK`.  At this stage the packet did not yet include arbitrary non-affine
Mobius reparametrizations; the later source-Mobius entry below supersedes that
limitation.  Standalone replay passes in `0.07s` locally (`maxrss=12928`).
The default aggregate replay passes with this packet included in `41.63s`
locally (`maxrss=98780`).

## T4 h=8 non-antipodal aperiodicity

Stage selected: remove a possible periodic subcase from the h=8 n=64 support
residual.  The rotation-orbit compiler already counts non-antipodal support
orbits; this packet proves that every such orbit is genuinely aperiodic.

New packet:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H8_NONANTIPODAL_APERIODIC.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_nonantipodal_aperiodic.py
```

Result: if a 16-support in `Z/64Z` is fixed by a nonzero rotation, its
stabilizer order divides `16`; the stabilizer therefore contains the unique
half-turn by `32`.  Thus every rotation-periodic 16-support is antipodal.
Contrapositively, non-antipodal 16-supports have trivial rotation stabilizer.

The exact count identity is now:

```text
122,131,731,640,320 = 16 * 7,633,233,227,520.
```

So the h=8 n=64 primitive support certifier can target aperiodic
non-antipodal rotation orbits directly; periodic supports are antipodal and
fall under the paid quotient ledger.  Standalone replay passes in `0.02s`
locally (`maxrss=10624`).  The default aggregate replay passes with this
packet included in `41.87s` locally (`maxrss=98804`).

## T1 h=3 official degeneracy ledger

Stage selected: reduce the repaired h=3 rich-curve theorem statement to the
actual official F3 rows.  The general h=3 notes keep a toral term because
nonofficial evidence rows such as `n=96` have `3 | n`, but the prize rows are
all powers of two.

New packet:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_OFFICIAL_DEGENERACY_LEDGER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_official_degeneracy_ledger.py
```

Result: for every official row `n=2^s`, `13 <= s <= 41`,

```text
toral_bound(n) = 0.
```

Thus the official h=3 repaired rank theorem still has to exclude or pay
constant-ratio cells and the hyperbola-line cell `b=a^2/3`, but not a toral
budget.  This is a ledger simplification, not a proof of `RC-RANK` or the
geometric bridge.  Standalone replay passes in `0.03s` locally
(`maxrss=11648`).  The default aggregate replay passes with this packet
included in `42.86s` locally (`maxrss=98780`).

## T1 h=3 private-linear low/mid-row budget

Stage selected: make the private-linear fallback route concrete for the first
official h=3 rows.  The private-linear compiler guard says the current
degree-2 budget table cannot be reused if the eventual rank theorem only proves
private-linear degree-space fullness; this packet starts the required retuned
compiler.

New packet:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_PRIVATE_LINEAR_LOWROW_BUDGET.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_lowrow_budget.py
```

Result: with `L_private=(A-1)+3n(B-1)`, the exact low/mid-row budgets are:

```text
s=13: Z_private=23
s=14: Z_private=29
s=15: Z_private=37
s=16: Z_private=47
s=17: Z_private=59
s=18: Z_private=75
s=19: Z_private=94
s=20: Z_private=119
s=21: Z_private=150
s=22: Z_private=189
s=23: Z_private=238
s=24: Z_private=300
s=25: Z_private=378
s=26: Z_private=477
s=27: Z_private=601
s=28: Z_private=757
s=29: Z_private=954
s=30: Z_private=1202
s=31: Z_private=1514
s=32: Z_private=1908
```

For each row the verifier checks a pinned passing witness and scans the exact
finite `B` cap for `Z+1` failure.  This is a conditional arithmetic compiler
slice only: it does not prove private-linear rank, it does not cover `s>=33`,
and it does not prove the geometric bridge.  Standalone replay passes in
`0.65s` locally (`maxrss=13184`).  The default aggregate replay passes with
this packet included in `39.37s` locally (`maxrss=98684`).

## T1/T4 continuation: official-row interfaces and guardrails

Stage selected: keep pushing toward the F3 flip while preserving honest
blockers.  The latest work tightens the h=3 rank theorem statement, clarifies
the h=5 certificate route, and makes h=8 support-orbit certification safer.

New h=3 packets:

```text
F3_H3_PRIVATE_LINEAR_ONE_FACTOR_RANK.md
F3_H3_PRIVATE_LINEAR_TWO_FACTOR_GUARDRAIL.md
F3_H3_PRIVATE_LINEAR_BAD_PRIME_GUARDRAIL.md
F3_H3_PRIVATE_LINEAR_LOWROW_BUDGET.md
F3_H3_RANK_AVOID_INTERFACE.md
```

Results:

- the private-linear arithmetic compiler now covers every official row
  `s=13..41`, with `Z_private(13)=23` and `Z_private(41)=15267`;
- one private-linear factor has the expected rank
  `min(AB,A+H(B-1))`;
- naive two-factor induction is false over Q at `A=1,B=3,H=2`;
- characteristic-zero private-linear fullness is not enough by itself:
  a three-factor matrix has full rank `109` over Q but drops to rank `108`
  modulo `1009`;
- the h=3 rank-avoidance interface now explicitly requires finite-row minor
  nonvanishing over the actual row field.

New h=5 packet:

```text
F3_H5_CERTIFICATE_SCALING_FRONTIER.md
```

Result: the current h=5 MITM certificate format is not a clean uniform route.
At n=256, the left table is `binom(255,4)=172,061,505` records, at least
`5.13 GiB` before metadata, and at n=512 the right side needs about `35,836`
shards at the n=128 right-probe rate.  This points back to a symbolic norm-gate
theorem or a redesigned certificate join.

New h=8 packets:

```text
F3_H8_LOCATOR_PARITY_ANTIPODAL.md
F3_H8_X83_SPLIT_ROTATION_EQUIVARIANCE.md
```

Results:

- a 16-support in `mu_64` is antipodal iff its locator is even, so the paid
  quotient branch has a coefficient-level detector;
- the x83 `S_R +/- alpha` split commutes with root-scaling rotations up to side
  swap, so future orbit-level certifiers can rotate recovered splits safely.

Current default replay:

```text
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
elapsed=45.78 maxrss=98808
```

Remaining blockers are unchanged in kind:

```text
h=3: finite-row rank/minor avoidance plus geometric bridge;
h=5: uniform p-specific norm-gate exclusion or redesigned certificates;
h=8: non-antipodal n=64 x83 support certification or external/sharded join.
```

## Report checkpoint and replay-surface correction

Stage selected: consolidate the current F3 flip branch before the next proof
attempt.  The brief asks for a top-level report with confidence-ranked claims,
replay commands, and an explicit residual-gap statement; until now the branch
only had the detailed node-level interim report.

Banked file:

```text
FLIP_REPORT.md
```

Result: the top-level report states that this is not a flip dossier, separates
proved/replayed packets from conditional interfaces and evidence-only rows, and
keeps the three blockers explicit:

```text
h=3: finite-row rank/minor avoidance plus geometric bridge;
h=5: uniform p-specific norm-gate exclusion or redesigned certificates;
h=8: non-antipodal n=64 x83 support certification or external/sharded join.
```

Replay correction: the interim report already cited the h=3 small-`H` rank
guardrail, but the aggregate replay script did not call its verifier.  The
aggregate replay now includes:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rc_rank_hfloor_guard.py
```

Current default replay:

```text
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
elapsed=57.58 maxrss=98808
```

This is still under the 60 second laptop-safe cap.  Next step should be a
proof-facing h=3 rank/bridge lemma or an h=8 certifier construction, not
additional broad auditing.

## T4 h=8 non-antipodal x83 certifier skeleton

Stage selected: push the h=8 residual from "large open support universe" to a
concrete shardable certificate runner interface, without launching a global
search on the laptop.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H8_X83_ORBIT_CERTIFIER_SKELETON.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_x83_orbit_certifier_skeleton.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_x83_orbit_certifier_skeleton.py
```

Expected digest:

```text
H8_X83_ORBIT_CERTIFIER_SKELETON_PASS
```

Result: the script rank-unranks anchored 16-supports, excludes the antipodal
branch, canonicalizes non-antipodal supports under the proved root-scaling
rotation, tests x83 only on canonical anchored representatives, and prints
`next_rank` for resumable shards.  It also emits a machine-readable
`CERT_RECORD` JSON line for future manifest assembly.  The environment
controls are:

```text
F3_H8_ORBIT_P
F3_H8_ORBIT_SHARDS
F3_H8_ORBIT_SHARD
F3_H8_ORBIT_START_RANK
F3_H8_ORBIT_STOP_RANK
F3_H8_ORBIT_MAX_SUPPORTS
F3_H8_ORBIT_SECONDS
```

The bounded dry run checks the first `2048` anchored supports at `p=4289`,
finds `1978` canonical non-antipodal representatives, and finds no x83
full-zero support in that prefix.  A resumed shard slice also replays.  This is
not evidence for global h=8 closure; it is the certifier construction needed
to make future 60-second Modal shards produce partial, resumable records.

The script is deliberately not added to the default aggregate replay because
the current aggregate already runs close to the 60 second laptop cap.

## T1 h=3 conic degree-2 chart

Stage selected: bank a bridge-side parametrization lemma rather than another
activation census.  The rich-curve machinery assumes degree-2 rational
membership maps; this packet proves that the actual h=3 same-fiber conics have
such maps over the row field itself.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CONIC_DEGREE2_CHART.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_degree2_chart.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_degree2_chart.py
```

Expected digest:

```text
H3_CONIC_DEGREE2_CHART_PASS
```

Result: for a row-field point `(u0,v0)` on
`G(u,v)=u^2+uv+v^2+a(u+v)+b=0`, the line-through-point chart gives

```text
S(t) = -((2u0+v0+a) + t(u0+2v0+a))/(t^2+t+1),
U(t)=u0+S(t),
V(t)=v0+tS(t),
W(t)=-a-U(t)-V(t).
```

Then `G(U,V)=0`, `U+V+W=-a`, `UV+UW+VW=b`, and
`F0(U)=F0(V)=F0(W)` for `F0(T)=T^3+aT^2+bT`.  After clearing the denominator
`t^2+t+1`, all three membership maps have numerator and denominator degree at
most `2`.  The affine chart plus the `t=infinity` vertical mate covers the
finite conic points in the replayed small fields.  This supports the degree-2
rich-curve setup; it does not prove rank-minor avoidance or geometric
batching.

The aggregate replay now includes this verifier and still passes under the
60 second cap:

```text
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
elapsed=57.07 maxrss=98564
```

## T1 h=3 local fiber-count bridge

Stage selected: pin the local multiplicity between triples, ordered conic
points, and activated pairs.  This is a bridge bookkeeping lemma, not a global
activation bound.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_LOCAL_FIBER_COUNT_BRIDGE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_local_fiber_count_bridge.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_local_fiber_count_bridge.py
```

Expected digest:

```text
H3_LOCAL_FIBER_COUNT_BRIDGE_PASS
```

Result: for each fixed `(s1,s2)`,

```text
R(s1,s2) = 6 N(s1,s2),
local activated pairs = binom(N(s1,s2),2)
                      = R(s1,s2)(R(s1,s2)-6)/72.
```

Here `N` counts unordered 3-subsets of `H` with elementary data `(s1,s2)`,
while `R` counts ordered pairwise-distinct same-fiber triples.  In conic form,
these are exactly the ordered points with
`G(u,v)=0` and `w=-a-u-v in H`.  The verifier checks the identity on
`(p,n)=(97,16),(97,32),(193,64)`.

The aggregate replay now includes this verifier and still passes under the
60 second cap:

```text
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
elapsed=57.28 maxrss=98800
```

## T2 h=3 dilation lift bound

Stage selected: bank the normalization step used by the h=3 activation
compiler.  `A_3(n,p)` is counted modulo common multiplication by `H`, while
the compiler uses an unnormalized contribution term `n A_3(n,p)`.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_DILATION_LIFT_BOUND.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_dilation_lift_bound.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_dilation_lift_bound.py
```

Expected digest:

```text
H3_DILATION_LIFT_BOUND_PASS
```

Result: for any stable set `X` of activated unordered h=3 shape pairs,
orbit-stabilizer gives

```text
|X| <= n |X/H|.
```

This is deliberately not a freeness claim.  The finite-field verifier finds
nontrivial side-swap stabilizer orbits in the test rows, and those only reduce
the raw lift size.  The replayed rows are:

```text
p=97,  n=16: raw=16,    normalized=1,   n*normalized=16
p=97,  n=32: raw=960,   normalized=31,  n*normalized=992
p=193, n=64: raw=20192, normalized=317, n*normalized=20288
```

This supports the existing compiler term:

```text
T_3 <= toral + poisson_boundary + n A_3(n,p).
```

It does not prove `A_3(n,p) <= Cn`.

The aggregate replay now includes this verifier and still passes under the
60 second cap, but with little slack:

```text
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
elapsed=59.43 maxrss=98808
```

Do not add more checks to the default aggregate without first slimming or
moving an existing check to standalone replay.

## T1 h=3 conic-chart ratio guard

Stage selected: connect the field-rational conic chart to the existing
constant-ratio degeneracy filter.  This narrows the repaired h=3 bridge target
without adding another default aggregate check.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CONIC_CHART_RATIO_GUARD.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_chart_ratio_guard.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_chart_ratio_guard.py
```

Expected digest:

```text
H3_CONIC_CHART_RATIO_GUARD_PASS
```

Result: after the hyperbola-line cell `a^2=3b` is excluded, none of

```text
U(t)/V(t), U(t)/W(t), V(t)/W(t)
```

is constant in the conic chart.  The proof is geometric: a constant ratio would
force the dense chart image to lie on an affine line, hence force the conic to
have a line component, which is exactly the already banked hyperbola-line cell.
The verifier checks four nondegenerate finite-field charts and a toral positive
control where ratio collapse is detected.

This is standalone only; it is not added to the default aggregate while that
replay sits at `elapsed=59.43`.

## Replay maintenance: slim h=3 generic-open check

Stage selected: recover default aggregate replay margin after the h=3 compiler
support packets pushed the runner close to the 60 second cap.

Changed files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RC_RANK_GENERIC_OPEN.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rc_rank_generic_open.py
```

Result: the generic-open verifier now consumes the private-linear rank `293`
as a pinned input from `F3_H3_RICH_CURVE_RANK_STRESS.md`, just as it already
consumed the degree-2 full-rank witness `320` from the rank-sample packet.  In
the aggregate replay, the rank-stress and rank-sample scripts remain the
authoritative exact matrix checks; the generic-open script only verifies the
minor-open reduction arithmetic and capacity consequences.

Focused replay:

```text
H3_RC_RANK_GENERIC_OPEN_PASS
```

Default aggregate replay after slimming:

```text
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
elapsed=56.51 maxrss=98836
```

## T1 h=3 conic-chart H-point coverage

Stage selected: pin the additive loss between the affine conic chart count and
the ordered same-fiber `H`-triple count.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CONIC_CHART_HPOINT_COVERAGE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_chart_hpoint_coverage.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_chart_hpoint_coverage.py
```

Expected digest:

```text
H3_CONIC_CHART_HPOINT_COVERAGE_PASS
```

Result: for a fixed same-`(e1,e2)` conic and base point, the affine chart
counts every ordered `H`-triple except possibly the vertical/projective mate:

```text
R = T_chart + epsilon,   epsilon in {0,1}.
```

The standalone verifier checks selected rich fibers in rows
`(p,n)=(97,16),(97,32),(193,64)` and finds the expected one vertical point per
selected fiber.  This is bridge bookkeeping only; it does not prove a global
bound on the number of conics or on rank-capacity consumption.

## T1 h=3 pair-count from charts compiler

Stage selected: turn the local conic-chart count into the exact activated
pair-count arithmetic, and record why the future bridge theorem needs more
than a linear incidence estimate.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_PAIR_COUNT_FROM_CHARTS_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_pair_count_from_charts_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_pair_count_from_charts_compiler.py
```

Expected digest:

```text
H3_PAIR_COUNT_FROM_CHARTS_COMPILER_PASS
```

Result: if a repaired chart `z` has finite count `T_z`, vertical contribution
`epsilon_z in {0,1}`, and ordered triple count `R_z=T_z+epsilon_z`, then its
activated local pair contribution is

```text
P_z = binom(R_z/6,2) = R_z(R_z-6)/72.
```

Consequently, a chart ledger with `T_z <= M`, `sum_z T_z <= S`, and at most
`Z` charts gives

```text
P_total <= (M+1)(S+Z)/72.
```

For the normalized h=3 target, it is sufficient to prove

```text
(M+1)(S+Z) <= 1152 n.
```

The standalone verifier replays this arithmetic on selected rich fibers in
rows `(p,n)=(97,16),(97,32),(193,64)`.  This is not added to the aggregate
replay; it is a bridge-side compiler showing that `H3-ACT(16)` needs total
chart mass plus a max-fiber, level-set, or equivalent rank-capacity bound.

## T1 h=3 L2 and level-set bridge compiler

Stage selected: weaken the previous max-times-total sufficient condition to
the exact quadratic ledger paid by activated pairs.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_L2_LEVELSET_BRIDGE_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_l2_levelset_bridge_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_l2_levelset_bridge_compiler.py
```

Expected digest:

```text
H3_L2_LEVELSET_BRIDGE_COMPILER_PASS
```

Result: for ordered same-fiber counts `R_z`, the normalized h=3 pair target is
equivalent to

```text
sum_z R_z(R_z-6) <= 1152 n.
```

The same condition can be written as the weighted level-set identity

```text
P_total = sum_{m >= 2} (m-1) L_m,     L_m = #{z : R_z/6 >= m}.
```

The previous max-fiber condition is therefore only one sufficient corollary,
via `sum R_z^2 <= max(R_z) sum R_z`.  The future bridge theorem can close h=3
by proving this exact L2 ledger or the equivalent level-set tail bound; it does
not need a separate uniform max-fiber theorem if a sharper tail theorem is
available.

## T1 h=3 conic base-point equivalence

Stage selected: prevent the h=3 bridge from charging duplicate geometric curve
images when many ordered triples lie in the same same-`(e1,e2)` conic fiber.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CONIC_BASEPOINT_EQUIVALENCE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_basepoint_equivalence.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_basepoint_equivalence.py
```

Expected digest:

```text
H3_CONIC_BASEPOINT_EQUIVALENCE_PASS
```

Result: if two row-field base points lie on the same nondegenerate
same-fiber conic, their line-through-point charts have the same projective
conic image.  After restricting to `H^3` and adding the one vertical mate, both
recover the same ordered same-fiber triple ledger `R(s1,s2)`.

Therefore incidence bookkeeping may choose one base point per nonempty conic
fiber.  The future bridge should not pay one geometric curve image per ordered
triple.  This is still not a rank theorem: if `RC-RANK` depends on the exact
rational parametrization, it needs a deterministic base-point rule or a
separate Mobius-reparametrization invariance lemma.

## T1 h=3 RC-RANK source Mobius invariance

Stage selected: discharge the parametrization caveat left by the conic
base-point equivalence packet.

Changed files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RC_RANK_NORMALIZATION_INVARIANCE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rc_rank_normalization_invariance.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rc_rank_normalization_invariance.py
```

Expected digest:

```text
H3_RC_RANK_NORMALIZATION_INVARIANCE_PASS
```

Result: the rank-normalization lemma now covers full source Mobius
reparametrizations

```text
X -> (alpha X + beta)/(gamma X + delta).
```

After clearing each degree-2 rational map by `(gamma X + delta)^2`, the common
product denominator contributes a fixed factor, and the source monomial span is
the standard degree-`A-1` binary-form representation under `PGL_2`.  The
cleared substitution rank is therefore unchanged.  This means changing the
base point on a nondegenerate same-fiber conic changes only the parametrization
and not the `RC-RANK` target.

## T1 h=3 private-linear PGL2 normal form

Stage selected: use source-Mobius rank invariance to reduce the private-linear
rank-avoidance target to its essential parameters.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_PRIVATE_LINEAR_PGL2_NORMAL_FORM.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_pgl2_normal_form.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_pgl2_normal_form.py
```

Expected digest:

```text
H3_PRIVATE_LINEAR_PGL2_NORMAL_FORM_PASS
```

Result: for a private-linear triple

```text
r_i(X)=(X-alpha_i)/(X-beta_i),
```

with distinct zero/pole points, the source transformation

```text
T(X)=((X-alpha_1)/(X-beta_1))
     /((alpha_2-alpha_1)/(alpha_2-beta_1))
```

sends `alpha_1,beta_1,alpha_2` to `0,infinity,1`.  After target scalings the
triple is

```text
Y,        (Y-1)/(Y-lambda),        (Y-eta)/(Y-theta).
```

The verifier checks this value identity over `F_97,F_193,F_769` and checks, in
the small rank model, that the original and normal-form triples have the same
cleared substitution rank.  This does not prove private-linear `RC-RANK`; it
reduces the finite-row bad-minor avoidance problem to the explicit
three-parameter normal-form family.

## T1 h=3 private-linear normal-form degeneracy chart

Stage selected: make the private-linear repaired open set explicit in the
`(lambda,eta,theta)` normal-form coordinates.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_PRIVATE_LINEAR_NORMAL_FORM_DEGENERACY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_normal_form_degeneracy.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_normal_form_degeneracy.py
```

Expected digest:

```text
H3_PRIVATE_LINEAR_NORMAL_FORM_DEGENERACY_PASS
```

Result: in the normal form

```text
Y,        (Y-1)/(Y-lambda),        (Y-eta)/(Y-theta),
```

the private-divisor open set is exactly

```text
lambda, eta, theta notin {0,1},
lambda, eta, theta pairwise distinct.
```

The ratios `r_1/r_2` and `r_1/r_3` are never constant, and `r_2/r_3` is
constant precisely when `{1,theta}={lambda,eta}`.  Therefore the
private-divisor open set automatically excludes pairwise constant-ratio
collapse.  The finite-field verifier enumerates the chart over
`F_17,F_19,F_23`.

## T1 h=3 private-linear minor-degree compiler

Stage selected: convert the normal-form private-linear rank target into an
explicit bounded-degree bad-locus problem.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_PRIVATE_LINEAR_MINOR_DEGREE_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_minor_degree_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_minor_degree_compiler.py
```

Expected digest:

```text
H3_PRIVATE_LINEAR_MINOR_DEGREE_COMPILER_PASS
```

Result: in the normal form, each cleared matrix entry has

```text
deg_lambda <= H(B-1),
deg_eta + deg_theta <= H(B-1),
total degree <= 2H(B-1).
```

Therefore any `r x r` rank minor has

```text
deg_lambda <= rH(B-1),
deg_eta + deg_theta <= rH(B-1),
total degree <= 2rH(B-1).
```

The verifier constructs the symbolic normal-form coefficient matrix for small
`(A,B,H)` boxes and checks the entry and sample-minor degree bounds.  This
does not prove nonvanishing; it sharpens `F3-PRIVATE-LINEAR-RANK-AVOID` to
bounded-degree minor avoidance over the actual row field.

## T2 h=3 moment bookkeeping identity

Stage selected: isolate the exact ordered-triple moment identity named in the
h=3 Stepanov-swing program.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_MOMENT_BOOKKEEPING_IDENTITY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_moment_bookkeeping_identity.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_moment_bookkeeping_identity.py
```

Expected digest:

```text
H3_MOMENT_BOOKKEEPING_IDENTITY_PASS
```

Result: for the ordered-triple moment

```text
M = #{(x,y) in H^3 x H^3 : sum(x)=sum(y), sum(x^2)=sum(y^2)},
```

the exact identity is

```text
M = trivial + 72 T_3 + repeat_residue,
trivial = 36 binom(n,3) + 9 n(n-1) + n.
```

The factor `72` is `2*6*6` from an unordered disjoint pair of distinct-entry
triples.  The repeat residue is real: the focused replay gets nonzero
`repeat_residue` on `(p,n)=(97,16),(97,32),(193,64)`.  Therefore a moment-form
h=3 proof must bound or pay this term instead of replacing `M-trivial` by
`72T_3`.

## Replay maintenance: aggregate after Mobius/rank-interface changes

The default aggregate replay still passes under the 60 second cap after the
source-Mobius normalization update:

```text
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
elapsed=55.63 maxrss=98688
```

## T2 h=3 repeat-residue boundary compiler

Stage selected: refine the nonzero repeat residue from the h=3 moment identity
into an exact boundary ledger rather than running further broad searches.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_RESIDUE_BOUNDARY_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_residue_boundary_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_residue_boundary_compiler.py
```

Expected digest:

```text
H3_REPEAT_RESIDUE_BOUNDARY_COMPILER_PASS
```

Result: repeated-entry multisets over a fixed `(sum, sumsq)` signature have
ordered repeated weight `R_sigma in {0,1,3,6}`.  The exact residue formula is

```text
repeat_residue_sigma = 2 D_sigma R_sigma + R_sigma^2 - Q_sigma,
```

and hence

```text
repeat_residue <= 12 D_boundary + 18 Z_repeat.
```

Focused replay:

```text
p=97 n=16 repeat_residue=288 D_boundary=0 Z_repeat=240 bound=4320
p=97 n=32 repeat_residue=17664 D_boundary=2688 Z_repeat=960 bound=49536
p=193 n=64 repeat_residue=135552 D_boundary=20352 Z_repeat=3776 bound=312192
H3_REPEAT_RESIDUE_BOUNDARY_COMPILER_PASS
elapsed=0.14 maxrss=22788
```

## T2 h=3 repeat-boundary line compiler

Stage selected: push the new repeat-residue boundary toward a theorem target by
normalizing `D_boundary` into a two-parameter line-pencil membership count.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_BOUNDARY_LINE_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_line_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_line_compiler.py
```

Expected digest:

```text
H3_REPEAT_BOUNDARY_LINE_COMPILER_PASS
```

Result: normalized distinct triples over repeated signatures are represented by
the line pencil

```text
1+t,
1+rt,
1-(r/(r+1))t,
1+((r^2+r+1)/(r+1))t.
```

If `B_line` counts pairs `(r,t)` for which all four values lie in `H` and the
first three are distinct, then

```text
D_boundary <= n B_line,
Z_repeat <= n^2,
repeat_residue <= 12 n B_line + 18 n^2.
```

Focused replay:

```text
p=97 n=16 D_boundary=0 nB_line=0 B_line=0 Z_repeat=240 n^2=256
p=97 n=32 D_boundary=2688 nB_line=2880 B_line=90 Z_repeat=960 n^2=1024
p=193 n=64 D_boundary=20352 nB_line=21888 B_line=342 Z_repeat=3776 n^2=4096
H3_REPEAT_BOUNDARY_LINE_COMPILER_PASS
elapsed=0.17 maxrss=22312
```

## T2 h=3 repeat-boundary LP4 Stepanov compiler

Stage selected: connect the new line-pencil boundary target to the existing
Stepanov bookkeeping, while keeping the new four-form nonvanishing theorem
explicit.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_BOUNDARY_LP4_STEPANOV_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_lp4_stepanov_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_lp4_stepanov_compiler.py
```

Expected digest:

```text
H3_REPEAT_BOUNDARY_LP4_STEPANOV_COMPILER_PASS
```

Result: for a repaired family `R` of repeat-boundary line parameters, the
four-affine-form auxiliary has

```text
coeffs = A B^4,
degree = (A-1)+4n(B-1),
conditions <= 5D(A+D)|R|.
```

Thus `LP4-RED(5)` is banked.  The remaining theorem is the named
`LP4-RANK/LP4-NV` nonvanishing gate; the h=2 rich-coset theorem alone only sees
two of the four membership conditions and gives the wrong scale.

Focused replay:

```text
LP4-RED supplied; remaining gate: LP4-RANK/LP4-NV
H3_REPEAT_BOUNDARY_LP4_STEPANOV_COMPILER_PASS
elapsed=0.03 maxrss=12800
```

## T2 h=3 repeat-boundary q0 cell

Stage selected: prove a genuine subcell of the new line-pencil boundary rather
than leaving every line parameter to the future LP4 theorem.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_BOUNDARY_Q0_CELL.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_q0_cell.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_q0_cell.py
```

Expected digest:

```text
H3_REPEAT_BOUNDARY_Q0_CELL_PASS
```

Result: the triple-repeat line cell `r^2+r+1=0` has at most two line
parameters.  On each one, dropping the third nonconstant form leaves a
two-affine multiplicative-coset intersection, so the optimized h=2 Stepanov
argument gives

```text
B_q0 <= 132 n^(2/3),
12 n B_q0 <= 1584 n^(5/3).
```

The future LP4 theorem can exclude this lower-condition cell.

Focused replay:

```text
p=97 n=16 q0_roots=2 q0_count=0
p=97 n=32 q0_roots=2 q0_count=6
p=193 n=64 q0_roots=2 q0_count=6
p=257 n=128 q0_roots=0 q0_count=0
H3_REPEAT_BOUNDARY_Q0_CELL_PASS
elapsed=0.02 maxrss=11392
```

## T2 h=3 repeat-boundary fiber cap

Stage selected: extract a support-reduction route from the h=2 coset-pair
Stepanov corollary for all line-pencil parameters, not just q0.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_BOUNDARY_FIBER_CAP.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_fiber_cap.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_fiber_cap.py
```

Expected digest:

```text
H3_REPEAT_BOUNDARY_FIBER_CAP_PASS
```

Result: for every fixed nondegenerate line parameter, dropping two membership
conditions leaves a two-affine multiplicative-coset intersection, so

```text
T_r <= 66 n^(2/3).
```

After paying q0, the repeat boundary satisfies

```text
B_line <= 132 n^(2/3) + 66 n^(2/3) R_genuine,
repeat_residue
  <= 1584 n^(5/3) + 792 n^(5/3) R_genuine + 18n^2.
```

A future support bound `R_genuine=O(n^beta)`, `beta<4/3`, is enough for a
subcubic repeat-residue payment.

Focused replay:

```text
p=97 n=32 B_line=90 support=62 genuine_support=60 max_fiber=3
p=193 n=64 B_line=342 support=170 genuine_support=168 max_fiber=5
p=257 n=128 B_line=3786 support=252 genuine_support=252 max_fiber=20
H3_REPEAT_BOUNDARY_FIBER_CAP_PASS
elapsed=0.04 maxrss=11516
```

## T2 h=3 repeat-boundary LP4 rank guardrail

Stage selected: rule out a false LP4 nonvanishing shortcut before spending
more effort on the line-pencil theorem.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_BOUNDARY_LP4_RANK_GUARDRAIL.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_lp4_rank_guardrail.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_lp4_rank_guardrail.py
```

Expected digest:

```text
H3_REPEAT_BOUNDARY_LP4_RANK_GUARDRAIL_PASS
```

Result: the full-degree-space shortcut for affine products is false.  For
`A=1,B=3,H=2` and roots `(2,5)`, the nine polynomials
`P_ij=(X-2)^(2i)(X-5)^(2j)` have exact rational rank `8`, not `9`, with

```text
81 P00 - 18 P01 + P02 - 18 P10 - 2 P11 + P20 = 0.
```

Therefore the remaining LP4 theorem must prove the actual weaker rank
threshold, or the proof must proceed through the active-support route.

Focused replay:

```text
rank=8 expected_full_degree_rank=9
H3_REPEAT_BOUNDARY_LP4_RANK_GUARDRAIL_PASS
elapsed=0.41 maxrss=50020
```

## T2 h=3 repeat-boundary support symmetry

Stage selected: quotient the remaining support target by the exact permutation
symmetry of the three distinct boundary entries.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_BOUNDARY_SUPPORT_SYMMETRY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_support_symmetry.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_support_symmetry.py
```

Expected digest:

```text
H3_REPEAT_BOUNDARY_SUPPORT_SYMMETRY_PASS
```

Result: outside the paid q0 cell and the coefficient-collision cells, active
line parameters are closed under

```text
r, 1/r, -r/(r+1), -(r+1)/r, -(r+1), -1/(r+1).
```

Thus the genuine support is a union of six-element `S_3` Mobius orbits, and
`R_genuine=6R_orb`.

Focused replay:

```text
p=97 n=32 genuine_support=60 s3_orbits=10
p=193 n=64 genuine_support=168 s3_orbits=28
p=257 n=128 genuine_support=252 s3_orbits=42
H3_REPEAT_BOUNDARY_SUPPORT_SYMMETRY_PASS
elapsed=0.03 maxrss=11520
```

## h=2 affine coset-pair Stepanov corollary

Stage selected: factor out the h=2 corollary used by the q0 and fiber-cap
repeat-boundary packets.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H2_AFFINE_COSET_PAIR_STEPANOV.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_affine_coset_pair_stepanov.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_affine_coset_pair_stepanov.py
```

Expected digest:

```text
H2_AFFINE_COSET_PAIR_STEPANOV_PASS
```

Result: the optimized h=2 proof extends unchanged to shifted intersections of
two affine multiplicative cosets:

```text
#{X : L_1(X) in H, L_2(X) in H} <= 66 n^(2/3)
```

under `n^4 < p^3`, provided the two affine forms are not proportional.  This
is the input for `B_q0 <= 132 n^(2/3)` and the fixed-fiber cap
`T_r <= 66 n^(2/3)`.

Focused replay:

```text
H2_AFFINE_COSET_PAIR_STEPANOV_PASS
elapsed=0.03 maxrss=11392
```

## T2 h=3 repeat-boundary support compiler

Stage selected: combine the q0 payment, fixed-fiber cap, and `S_3` support
quotient into one explicit repeat-residue theorem interface.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_BOUNDARY_SUPPORT_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_support_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_support_compiler.py
```

Expected digest:

```text
H3_REPEAT_BOUNDARY_SUPPORT_COMPILER_PASS
```

Result: the repeat-residue branch now has the single quotient-support target

```text
B_line <= 132 n^(2/3) + 396 R_orb n^(2/3),
repeat_residue
  <= 1584 n^(5/3) + 4752 R_orb n^(5/3) + 18n^2.
```

Thus any theorem `R_orb <= C n^beta` with `beta < 4/3` pays the repeat residue
subcubically; the linear quotient-support target gives an `O_C(n^(8/3))`
payment.

Focused replay:

```text
p=97 n=32 B_line=90 R_orb=10 B_line_bound=41291
p=193 n=64 B_line=342 R_orb=28 B_line_bound=179520
p=257 n=128 B_line=3786 R_orb=42 B_line_bound=425957
H3_REPEAT_BOUNDARY_SUPPORT_COMPILER_PASS
elapsed=0.18 maxrss=22552
```

## T2 h=3 repeat-boundary focused replay

Stage selected: add a standalone replay harness for the new repeat-boundary
chain without lengthening the default F3 aggregate replay.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_BOUNDARY_REPLAY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_replay.py
```

Expected digest:

```text
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
```

Result: the focused replay covers the h=2 affine coset-pair input, the h=3
moment identity, every repeat-boundary compiler/payment/guardrail packet, the
combined support compiler, the boundary-style support evidence, and the
forced-point/fiber reductions.  It does not launch Modal and does not run the
older 55s aggregate.

Focused replay:

```text
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T3 h=3 repeat-support crossover

Stage selected: translate the new quotient-support theorem target into
official-row constant pressure.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SUPPORT_CROSSOVER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_support_crossover.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_support_crossover.py
```

Expected digest:

```text
H3_REPEAT_SUPPORT_CROSSOVER_PASS
```

Result: assuming a future linear quotient-support theorem `R_orb <= Cn`, the
proof-safe sufficient bound

```text
repeat_residue <= (4752C+1602)n^(8/3)
```

is below `n^3` when `n>(4752C+1602)^3`.  Representative official coverage:

```text
C=1/2: first_official=36, coverage=2^36..2^41
C=1:   first_official=38, coverage=2^38..2^41
C=2:   first_official=41, coverage=2^41..2^41
C=4:   no official row by this sufficient test
```

Focused replay:

```text
H3_REPEAT_SUPPORT_CROSSOVER_PASS
elapsed=0.02 maxrss=11776
```

## T2/T3 h=3 repeat-support boundary evidence

Stage selected: test the remaining quotient-support target on boundary-style
rows using the efficient `u,v in H` scan, and bank any falsifier to support
emptiness.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SUPPORT_BOUNDARY_EVIDENCE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_support_boundary_evidence.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_support_boundary_evidence.py
```

Expected digest:

```text
H3_REPEAT_SUPPORT_BOUNDARY_EVIDENCE_PASS
```

Result: boundary-style rows have tiny repeat-boundary support in this finite
sample, but support emptiness is false:

```text
n=16,32,64,128: B_line=0
n=256,p=65537: B_line=48, support=48, R_orb=8
n=512,1024: B_line=0
```

The support theorem should therefore bound `R_orb`, not try to prove
`B_line=0`.

Focused replay:

```text
H3_REPEAT_SUPPORT_BOUNDARY_EVIDENCE_PASS
elapsed=1.07 maxrss=10752
```

## T2/T3 h=3 repeat-support forced-point reduction

Stage selected: refine the nonzero boundary-support row into a structural
support route instead of treating it as arbitrary line support.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SUPPORT_FORCED_POINT_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_support_forced_point_reduction.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_support_forced_point_reduction.py
```

Expected digest:

```text
H3_REPEAT_SUPPORT_FORCED_POINT_REDUCTION_PASS
```

Result: if a forced-coordinate set `A` covers all active triples, then

```text
B_line <= 3 sum_{a in A} N_a,
```

where `N_a` is a one-variable PGL2 fiber count.  On the nonzero boundary row
`n=256,p=65537`, every active triple contains `2`, and the reduction is exact:

```text
B_line=48, common={2}, N_2=16, 3N_2=48.
```

Focused replay:

```text
H3_REPEAT_SUPPORT_FORCED_POINT_REDUCTION_PASS
elapsed=1.98 maxrss=11264
```

## T2 h=3 repeat forced-fiber Stepanov compiler

Stage selected: turn the forced-coordinate support route into an explicit
Stepanov compiler with its own rank/nonvanishing gate.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_FORCED_FIBER_STEPANOV_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_forced_fiber_stepanov_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_forced_fiber_stepanov_compiler.py
```

Expected digest:

```text
H3_REPEAT_FORCED_FIBER_STEPANOV_COMPILER_PASS
```

Result: for fixed forced coordinate `a`, `w_a` has degree at most `1/1` and
`lambda_a` has degree `2/1`.  The forced-fiber auxiliary
`Phi(X,Y_1,Y_2)` has

```text
coeffs = A B^2,
degree = (A-1)+3n(B-1),
conditions <= 5D(A+D)F.
```

Thus `FF-RED(5)` is supplied.  The remaining theorem gate for this route is
`FF-RANK/FF-NV`.

Focused replay:

```text
FF-RED(5) supplied; remaining gate: FF-RANK/FF-NV
H3_REPEAT_FORCED_FIBER_STEPANOV_COMPILER_PASS
elapsed=0.33 maxrss=50104
```

## T2 h=3 repeat forced-fiber degree bound

Stage selected: check whether the forced-coordinate route needs the full
forced-fiber Stepanov theorem, or whether an elementary fiber-degree bound is
already enough.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_FORCED_FIBER_DEGREE_BOUND.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_forced_fiber_degree_bound.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_forced_fiber_degree_bound.py
```

Expected digest:

```text
H3_REPEAT_FORCED_FIBER_DEGREE_BOUND_PASS
```

Result: for every fixed forced coordinate `a`, the map `lambda_a` is degree
`2/1`, so each `mu in H` has at most two preimages.  Hence

```text
N_a <= 2n,
B_line <= 6|A0|n
```

for any forced-coordinate cover `A0`.  A sublinear forced cover is enough for
a subcubic repeat-residue payment.

Focused replay:

```text
H3_REPEAT_FORCED_FIBER_DEGREE_BOUND_PASS
elapsed=0.35 maxrss=49888
```

## T3 h=3 repeat forced-cover crossover

Stage selected: translate the elementary forced-fiber degree bound into
official-row constant pressure for possible forced-coordinate covers.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_FORCED_COVER_CROSSOVER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_forced_cover_crossover.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_forced_cover_crossover.py
```

Expected digest:

```text
H3_REPEAT_FORCED_COVER_CROSSOVER_PASS
```

Result: if a forced-coordinate cover has size `F`, then

```text
repeat_residue <= (72F+18)n^2.
```

Representative official coverage:

```text
F=64:            2^13..2^41
F=128:           2^14..2^41
F=1024:          2^17..2^41
F<=ceil(sqrt n): 2^13..2^41
F<=ceil(n^(2/3)): 2^19..2^41
```

Focused replay:

```text
H3_REPEAT_FORCED_COVER_CROSSOVER_PASS
elapsed=0.01 maxrss=10624
```

## T2/T3 h=3 repeat coordinate-cover ledger

Stage selected: turn the forced-cover target into a canonical measurable object
and check whether it is sharp enough on the boundary evidence rows.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_COORDINATE_COVER_LEDGER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_coordinate_cover_ledger.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_coordinate_cover_ledger.py
```

Expected digest:

```text
H3_REPEAT_COORDINATE_COVER_LEDGER_PASS
```

Result: the canonical coordinate cover `A_coord` covers every active triple and
therefore gives

```text
repeat_residue <= (72 C_coord + 18)n^2.
```

On the nonzero boundary row `n=256,p=65537`, the ledger has

```text
B_line=48, support=48, C_coord=17,
cover_bound=81395712 > n^3=16777216.
```

Thus `C_coord` is structurally small but too crude for that row; the sharper
common forced cover `{2}` is still needed.

Focused replay:

```text
H3_REPEAT_COORDINATE_COVER_LEDGER_PASS
elapsed=2.02 maxrss=10752
```

## T2/T3 h=3 repeat coordinate-hitting ledger

Stage selected: replace the crude coordinate-union cover with the minimum
hitting number of the active coordinate hypergraph.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_COORDINATE_HITTING_LEDGER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_coordinate_hitting_ledger.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_coordinate_hitting_ledger.py
```

Expected digest:

```text
H3_REPEAT_COORDINATE_HITTING_LEDGER_PASS
```

Result: if `tau_coord` is the minimum size of a coordinate set hitting every
active edge `{u,v,w}`, then

```text
repeat_residue <= (72 tau_coord + 18)n^2.
```

On the nonzero boundary row `n=256,p=65537`, the active coordinate hypergraph
has eight distinct edges and

```text
tau_coord=1, hitting_set={2},
residue_bound=5898240 < n^3=16777216.
```

Thus the row that defeated zero-support is still paid by the elementary
forced-coordinate route.  The uniform target is now the weaker statement
`tau_coord <= C n^eta`, `eta<1`, rather than a bound for the full coordinate
union `C_coord`.

Focused replay:

```text
H3_REPEAT_COORDINATE_HITTING_LEDGER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T2/T3 h=3 repeat forced-coordinate-2 normal form

Stage selected: explain the singleton hitter `{2}` by an algebraic normal
form rather than treating it as only a finite accident.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_FORCED_TWO_NORMAL_FORM.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_forced_two_normal_form.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_forced_two_normal_form.py
```

Expected digest:

```text
H3_REPEAT_FORCED_TWO_NORMAL_FORM_PASS
```

Result: when the forced coordinate is `2`,

```text
w_2(v)=v^{-1},     lambda_2(v)=v+v^{-1}.
```

So every active edge hit by `2` has inverse-pair form `{2,v,v^{-1}}`.  On the
nonzero boundary row `n=256,p=65537`, all eight active coordinate edges are of
this form and

```text
N_2=16, B_line=48=3N_2.
```

This keeps the next structural target concrete: prove that the active
non-q0 support is hit by `2`, or isolate a small exceptional hitting set for
edges not hit by `2`.

Focused replay:

```text
H3_REPEAT_FORCED_TWO_NORMAL_FORM_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T2/T3 h=3 repeat hitting exception scan

Stage selected: falsify the tempting pure fixed-`2` cover target before
building more proof structure on it.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_HITTING_EXCEPTION_SCAN.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_hitting_exception_scan.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_hitting_exception_scan.py
```

Expected digest:

```text
H3_REPEAT_HITTING_EXCEPTION_SCAN_PASS
```

Result: pure forced-`2` cover is false even in boundary-style rows:

```text
p=337   n=16  active_edges=1 non_two_edges=1 tau_coord=1
p=2017  n=32  active_edges=1 non_two_edges=1 tau_coord=1
p=91393 n=256 active_edges=2 non_two_edges=2 tau_coord=1
```

The positive signal is that all scanned witness rows still have a singleton
coordinate hitting set.  The proof target should remain `tau_coord <= Cn^eta`,
possibly via several forced-coordinate cells, rather than a fixed `2` cell.

Focused replay:

```text
H3_REPEAT_HITTING_EXCEPTION_SCAN_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T2/T3 h=3 repeat singleton-hitting stress

Stage selected: after fixed-`2` cover was falsified, test the stronger star
target `tau_coord <= 1` directly in bounded boundary-style windows.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SINGLETON_HITTING_STRESS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_singleton_hitting_stress.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_singleton_hitting_stress.py
```

Expected digest:

```text
H3_REPEAT_SINGLETON_HITTING_STRESS_PASS
```

Result: no `tau_coord>1` row appears in the bounded scan:

```text
n=16  scanned_primes=200 nonzero_rows=1 max_row=p=337,B=6,edges=1,tau=1
n=32  scanned_primes=200 nonzero_rows=1 max_row=p=2017,B=6,edges=1,tau=1
n=64  scanned_primes=200 nonzero_rows=5 max_row=p=65537,B=24,edges=4,tau=1
n=128 scanned_primes=120 nonzero_rows=3 max_row=p=65537,B=48,edges=8,tau=1
n=256 scanned_primes=80  nonzero_rows=6 max_row=p=65537,B=48,edges=8,tau=1
```

The payoff is large: `tau_coord <= 1` implies

```text
repeat_residue <= 90n^2,
```

which is below `n^3` for every official row.  This is finite stress evidence,
not a proof.

Standalone timing:

```text
H3_REPEAT_SINGLETON_HITTING_STRESS_PASS
elapsed=6.01 maxrss=10496
```

Focused replay:

```text
H3_REPEAT_SINGLETON_HITTING_STRESS_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T2/T3 h=3 repeat star-obstruction compiler

Stage selected: turn the singleton-hitting target into a finite-pattern
algebraic obstruction.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_STAR_OBSTRUCTION_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_star_obstruction_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_star_obstruction_compiler.py
```

Expected digest:

```text
H3_REPEAT_STAR_OBSTRUCTION_COMPILER_PASS
```

Result: for the 3-uniform active coordinate hypergraph,

```text
tau_coord > 1
```

is equivalent to the existence of at most four distinct active edges with empty
total intersection.  So the star theorem can be attacked by ruling out a
four-edge repeat-boundary incidence pattern.  The current witness rows all have
`obstruction_edges=0`, as expected from `tau_coord=1`.

Guardrail update: the extractor now deduplicates witness edges and includes
the non-boundary contrast row

```text
p=97 n=32 active_edges=15 tau_coord=7 obstruction_edges=2
```

so the obstruction pattern is real outside the boundary-style regime.

Focused replay:

```text
H3_REPEAT_STAR_OBSTRUCTION_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T2/T3 h=3 repeat edge reciprocal form

Stage selected: put the star-obstruction target into a symmetric algebraic
normal form.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_EDGE_RECIPROCAL_FORM.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_edge_reciprocal_form.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_edge_reciprocal_form.py
```

Expected digest:

```text
H3_REPEAT_EDGE_RECIPROCAL_FORM_PASS
```

Result: setting `x=u-1`, `y=v-1`, `z=w-1`, the active edge condition is
equivalent to

```text
xy+xz+yz=0,    lambda=1+x+y+z in H.
```

This turns a four-edge star obstruction into a concrete system of shifted
reciprocal triples with no common unshifted coordinate.

Focused replay:

```text
H3_REPEAT_EDGE_RECIPROCAL_FORM_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T2/T3 h=3 repeat star-obstruction taxonomy

Stage selected: split the star obstruction into algebraically distinct cases.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_STAR_OBSTRUCTION_TAXONOMY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_star_obstruction_taxonomy.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_star_obstruction_taxonomy.py
```

Expected digest:

```text
H3_REPEAT_STAR_OBSTRUCTION_TAXONOMY_PASS
```

Result: a non-star obstruction is either a disjoint active-edge pair or a
pairwise-intersecting active-edge family with empty total intersection.  With
the four-edge compiler, proving singleton hitting now reduces to:

```text
H3-NO-DISJOINT-EDGES
H3-NO-PAIRWISE-CORELESS
```

The boundary witness rows are all classified as `star`; the non-boundary
contrast row `(p,n)=(97,32)` is classified as `disjoint_pair`.

Focused replay:

```text
H3_REPEAT_STAR_OBSTRUCTION_TAXONOMY_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T2/T3 h=3 repeat edge cubic gcd form

Stage selected: recast singleton hitting as a common-root statement for the
active edge cubics.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_EDGE_CUBIC_GCD_FORM.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_edge_cubic_gcd_form.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_edge_cubic_gcd_form.py
```

Expected digest:

```text
H3_REPEAT_EDGE_CUBIC_GCD_FORM_PASS
```

Result: for an active edge `E={u,v,w}` with `lambda=u+v+w-2`, the cubic

```text
P_E(T)=T^3-(lambda+2)T^2+(2lambda+1)T-uvw
```

has subgroup roots exactly `E`.  Therefore singleton hitting is equivalent to
the active cubics having positive-degree gcd.  The non-boundary contrast row
has `gcd_positive=0`; the boundary witness rows have `gcd_positive=1`.

Focused replay:

```text
H3_REPEAT_EDGE_CUBIC_GCD_FORM_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T2/T3 h=3 repeat pair-intersection compiler

Stage selected: split the disjoint active-edge obstruction using the
difference of active edge cubics.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_PAIR_INTERSECTION_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_pair_intersection_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_pair_intersection_compiler.py
```

Expected digest:

```text
H3_REPEAT_PAIR_INTERSECTION_COMPILER_PASS
```

Result: subtracting two active edge cubics gives a quadratic:

```text
P_E(T)-P_F(T)=-(lambda-mu)T^2+2(lambda-mu)T-(m-n).
```

Hence disjoint active-edge pairs split into:

```text
SAME-LAMBDA
QUADRATIC-MISS
```

The boundary witness rows have no disjoint pairs.  The non-boundary contrast
row `(p,n)=(97,32)` has `83` disjoint pairs, split as `same_lambda=1` and
`quadratic_miss=82`.

Focused replay:

```text
H3_REPEAT_PAIR_INTERSECTION_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T2/T3 h=3 repeat lambda-fiber ledger

Stage selected: make the same-`lambda` obstruction into an exact fiber
statistic.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LAMBDA_FIBER_LEDGER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_fiber_ledger.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_fiber_ledger.py
```

Expected digest:

```text
H3_REPEAT_LAMBDA_FIBER_LEDGER_PASS
```

Result: if `K_lambda` is the number of active edges with a fixed `lambda`, then

```text
same_lambda_pairs = sum_lambda binom(K_lambda,2).
```

The boundary witness rows have `max_K_lambda=1`.  The non-boundary contrast row
`(p,n)=(97,32)` has `max_K_lambda=2` and `same_lambda_pairs=1`.

Focused replay:

```text
H3_REPEAT_LAMBDA_FIBER_LEDGER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T2/T3 h=3 repeat quadratic-rho compiler

Stage selected: normalize the lambda-distinct quadratic-miss condition to a
single scalar `rho`.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_QUADRATIC_RHO_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_quadratic_rho_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_quadratic_rho_compiler.py
```

Expected digest:

```text
H3_REPEAT_QUADRATIC_RHO_COMPILER_PASS
```

Result: for lambda-distinct active edges with data `(lambda,m)` and `(mu,n)`,

```text
rho=(m-n)/(lambda-mu),
```

and their common coordinates are exactly

```text
{t in E : t(2-t)=rho}.
```

Boundary witness rows have no rho misses.  The non-boundary contrast row
`(p,n)=(97,32)` has `lambda_distinct_pairs=104`, `rho_hit=22`,
`rho_miss=82`.

Focused replay:

```text
H3_REPEAT_QUADRATIC_RHO_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T2/T3 h=3 repeat pairwise-coreless compiler

Stage selected: split the pairwise-coreless obstruction into minimal
hypergraph shapes.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_PAIRWISE_CORELESS_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_pairwise_coreless_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_pairwise_coreless_compiler.py
```

Expected digest:

```text
H3_REPEAT_PAIRWISE_CORELESS_COMPILER_PASS
```

Result: a pairwise-intersecting coreless obstruction on at most four active
3-edges is either:

```text
THREE-EDGE-CORELESS
TETRAHEDRON
```

In the tetrahedron case, the four edges are exactly the four 3-subsets of a
four-point set.  Thus `H3-NO-PAIRWISE-CORELESS` splits into
`H3-NO-THREE-EDGE-CORELESS` and `H3-NO-TETRAHEDRON`.

Focused replay:

```text
H3_REPEAT_PAIRWISE_CORELESS_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T2/T3 h=3 repeat affine value-slope compiler

Stage selected: unify the lambda-injectivity and rho-hit targets through one
explicit polynomial family.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_AFFINE_VALUE_SLOPE_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_affine_value_slope_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_affine_value_slope_compiler.py
```

Expected digest:

```text
H3_REPEAT_AFFINE_VALUE_SLOPE_COMPILER_PASS
```

Result:

```text
A_lambda(T)=T(T-1)^2+lambda*T(2-T).
```

Active edges are 3-point H-level fibers `A_lambda(T)=m`; lambda-distinct rho
values are secant slopes in the lambda direction and are hit exactly when
`rho=t(2-t)` for some active root `t`.

Focused replay:

```text
H3_REPEAT_AFFINE_VALUE_SLOPE_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T2/T3 h=3 repeat coreless-pattern compiler

Stage selected: refine the three-edge coreless obstruction into its exact
3-uniform hypergraph patterns.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_CORELESS_PATTERN_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_coreless_pattern_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_coreless_pattern_compiler.py
```

Expected digest:

```text
H3_REPEAT_CORELESS_PATTERN_COMPILER_PASS
```

Result: a pairwise-intersecting coreless triple of 3-edges has pair-intersection
size pattern either

```text
(1,1,1) loose triangle
(1,1,2) pinched triangle
```

and the four-edge no-three-core case is still the tetrahedron.  Thus the
pairwise-coreless branch is now split into `H3-NO-LOOSE-TRIANGLE`,
`H3-NO-PINCHED-TRIANGLE`, and `H3-NO-TETRAHEDRON`.

Focused replay:

```text
H3_REPEAT_CORELESS_PATTERN_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T2/T3 h=3 repeat linear-hypergraph compiler

Stage selected: use the active-edge formula to remove non-linear coreless
patterns.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LINEAR_HYPERGRAPH_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_linear_hypergraph_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_linear_hypergraph_compiler.py
```

Expected digest:

```text
H3_REPEAT_LINEAR_HYPERGRAPH_COMPILER_PASS
```

Result: any active coordinate pair `a,b` determines the third coordinate

```text
c = 1 - (a-1)(b-1)/(a+b-2).
```

Thus distinct active edges intersect in at most one coordinate.  Pinched
triangles and tetrahedra repeat coordinate pairs, so they are impossible for
active repeat-boundary edges.  The surviving obstruction targets are now:

```text
H3-VALUE-INJECTIVE
H3-SLOPE-HIT
H3-NO-LOOSE-TRIANGLE
```

Focused replay:

```text
H3_REPEAT_LINEAR_HYPERGRAPH_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.49 maxrss=50104
```

## T2/T3 h=3 repeat loose-triangle shadow compiler

Stage selected: turn the remaining loose-triangle target into an exact
active-pair shadow graph condition.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_TRIANGLE_SHADOW_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_triangle_shadow_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_triangle_shadow_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_TRIANGLE_SHADOW_COMPILER_PASS
```

Result: after the linear-hypergraph compiler, every shadow pair has at most one
active-edge owner.  Therefore a shadow triangle is either contained in a single
active edge, or it is supported by three distinct active edges and is exactly a
loose-triangle obstruction

```text
{a,b,x}, {a,c,y}, {b,c,z}.
```

The boundary-style guardrail rows have no loose shadow triangles.  The
non-boundary contrast row `(p,n)=(97,32)` has two, so this final
pairwise-coreless target is non-vacuous.

Focused replay:

```text
H3_REPEAT_LOOSE_TRIANGLE_SHADOW_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.14 maxrss=50040
```

## T2/T3 h=3 repeat loose reciprocal-closure compiler

Stage selected: rewrite the loose-triangle target in the reciprocal chart
`r=1/(u-1)`.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_RECIPROCAL_CLOSURE_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_reciprocal_closure_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_reciprocal_closure_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_RECIPROCAL_CLOSURE_COMPILER_PASS
```

Result: with `r(u)=1/(u-1)`, active edges are zero-sum triples.  An active
pair `{r,s}` has forced third reciprocal coordinate `-(r+s)` and lambda test

```text
1+1/r+1/s-1/(r+s) in H.
```

Therefore a triangle in the reciprocal active-pair graph is contained exactly
when `r+s+t=0`; otherwise it is a loose-triangle obstruction.  The compiler
checks that this reciprocal count agrees with the coordinate-shadow count on
the boundary guardrails and on the `(p,n)=(97,32)` contrast row.

Focused replay:

```text
H3_REPEAT_LOOSE_RECIPROCAL_CLOSURE_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=17.91 maxrss=50104
```

## T2/T3 h=3 repeat reciprocal-product compiler

Stage selected: rewrite the disjoint-edge branch in reciprocal edge
invariants.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_RECIPROCAL_PRODUCT_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_reciprocal_product_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_reciprocal_product_compiler.py
```

Expected digest:

```text
H3_REPEAT_RECIPROCAL_PRODUCT_COMPILER_PASS
```

Result: if `{r,s,t}` are reciprocal roots of an active edge, then
`r+s+t=0`; writing `R=rst`, the edge has reciprocal cubic

```text
X^3+(lambda-1)R X-R.
```

The coordinate product is `m=lambda+R^-1`, so fixed-`lambda` injectivity is
uniqueness of active reciprocal product `R`.  For lambda-distinct edges
`(lambda,R)` and `(mu,S)`,

```text
rho = 1 + (R^-1-S^-1)/(lambda-mu),
```

and the source-edge hit values are `1-r^-2` on reciprocal roots.

Focused replay:

```text
H3_REPEAT_RECIPROCAL_PRODUCT_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=17.86 maxrss=50104
```

## T2/T3 h=3 repeat lambda-root fiber compiler

Stage selected: convert fixed-`lambda` reciprocal-product uniqueness into an
explicit rational-map fiber target.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LAMBDA_ROOT_FIBER_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_root_fiber_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_root_fiber_compiler.py
```

Expected digest:

```text
H3_REPEAT_LAMBDA_ROOT_FIBER_COMPILER_PASS
```

Result: for fixed `lambda`, a reciprocal root `r` determines the reciprocal
product by

```text
Phi_lambda(r)=r^3/(1-(lambda-1)r).
```

Active edges with that lambda are exactly the 3-point fibers of `Phi_lambda`
on `S={1/(u-1):u in H,u!=1}`.  Thus `H3-VALUE-INJECTIVE` has become the
fiber-uniqueness target: each `Phi_lambda` has at most one 3-point fiber on
`S`.  The boundary guardrails have max one such fiber per lambda; the
non-boundary contrast row has one lambda with two.

Focused replay:

```text
H3_REPEAT_LAMBDA_ROOT_FIBER_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=17.06 maxrss=50104
```

## T2/T3 h=3 repeat lambda-ratio parametrization

Stage selected: parametrize a 3-point `Phi_lambda` fiber by an ordered ratio
of two reciprocal roots.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LAMBDA_RATIO_PARAMETRIZATION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_ratio_parametrization.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_ratio_parametrization.py
```

Expected digest:

```text
H3_REPEAT_LAMBDA_RATIO_PARAMETRIZATION_PASS
```

Result: for `lambda != 1`, an ordered root ratio `z=s/r` reconstructs the
entire reciprocal fiber by

```text
r = (1+z+z^2)/((lambda-1)z(1+z)),
s = zr,
t = -(1+z)r.
```

For `lambda=1`, the branch is `Phi_1(r)=r^3` and the only possible ratios
satisfy `z^2+z+1=0`.  The boundary guardrails exercise the generic branch; the
contrast row exercises the `lambda=1` branch.

Focused replay:

```text
H3_REPEAT_LAMBDA_RATIO_PARAMETRIZATION_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=19.51 maxrss=50116
```

## T2/T3 h=3 repeat lambda-ratio membership compiler

Stage selected: turn the generic ratio parametrization into explicit
subgroup-membership functions.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LAMBDA_RATIO_MEMBERSHIP_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_ratio_membership_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_ratio_membership_compiler.py
```

Expected digest:

```text
H3_REPEAT_LAMBDA_RATIO_MEMBERSHIP_COMPILER_PASS
```

Result: for `lambda != 1`, with `a=lambda-1` and `N=1+z+z^2`, the original
coordinates of the ratio-parametrized fiber are

```text
U=1+a z(1+z)/N,
V=1+a(1+z)/N,
W=1-a z/N.
```

So the generic same-lambda target is a three-membership problem
`U,V,W in H` on the ratio line.  The `lambda=1` branch is kept separate as a
primitive-cube scale condition.

Focused replay:

```text
H3_REPEAT_LAMBDA_RATIO_MEMBERSHIP_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=17.00 maxrss=50108
```

## T2/T3 h=3 repeat lambda-ratio orbit compiler

Stage selected: quotient ordered root ratios by the `S_3` symmetry of a
3-point reciprocal fiber.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LAMBDA_RATIO_ORBIT_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_ratio_orbit_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_ratio_orbit_compiler.py
```

Expected digest:

```text
H3_REPEAT_LAMBDA_RATIO_ORBIT_COMPILER_PASS
```

Result: the six ordered ratios attached to a generic reciprocal edge are

```text
z, 1/z, -(1+z), -1/(1+z), -(1+z)/z, -z/(1+z).
```

So the generic same-lambda target is uniqueness of an admissible `S_3` ratio
orbit.  The `lambda=1` primitive-cube branch has only two ordered ratios and
is kept separate.

Focused replay:

```text
H3_REPEAT_LAMBDA_RATIO_ORBIT_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.99 maxrss=50040
```

## T2/T3 h=3 repeat lambda=1 scale compiler

Stage selected: isolate the exceptional `lambda=1` branch exposed by the
ratio parametrization.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LAMBDA_ONE_SCALE_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_one_scale_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_one_scale_compiler.py
```

Expected digest:

```text
H3_REPEAT_LAMBDA_ONE_SCALE_COMPILER_PASS
```

Result: when `lambda=1`, reciprocal roots are `{r,omega r,omega^2 r}`.  With
`x=1/r`, active edges are exactly scale orbits satisfying

```text
{1+x, 1+omega x, 1+omega^2 x} subset H.
```

The boundary guardrail rows have no active `lambda=1` scale orbit.  The
contrast row `(p,n)=(97,32)` has one.

Focused replay:

```text
H3_REPEAT_LAMBDA_ONE_SCALE_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.85 maxrss=50104
```

## T2/T3 h=3 repeat slope-ratio compiler

Stage selected: rewrite the lambda-distinct `H3-SLOPE-HIT` target in the same
ratio coordinates as the fixed-lambda branch.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SLOPE_RATIO_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_ratio_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_ratio_compiler.py
```

Expected digest:

```text
H3_REPEAT_SLOPE_RATIO_COMPILER_PASS
```

Result: for the generic branch,

```text
R^-1 = -(lambda-1)^3 z^2(1+z)^2/(1+z+z^2)^3.
```

For lambda-distinct edges `(lambda,R)` and `(mu,S)`,

```text
rho = 1 + (R^-1-S^-1)/(lambda-mu).
```

The slope-hit target is exactly that this rho is one of the three source slope
values `u(2-u)`.  The compiler also handles pairs involving the `lambda=1`
scale branch via `R^-1=x^3`.

Focused replay:

```text
H3_REPEAT_SLOPE_RATIO_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.83 maxrss=50104
```

## T2/T3 h=3 repeat slope numerator compiler

Stage selected: denominator-clear the slope-ratio hit condition into explicit
factored numerator equations.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SLOPE_NUMERATOR_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_numerator_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_numerator_compiler.py
```

Expected digest:

```text
H3_REPEAT_SLOPE_NUMERATOR_COMPILER_PASS
```

Result: for a generic source edge, write

```text
A=-(lambda-1)^3 z^2(1+z)^2, B=(1+z+z^2)^3.
```

For a lambda-distinct target with invariant `S^-1`,

```text
rho_num=(lambda-mu)B + A - S^-1 B.
```

The three slope-hit alternatives are the numerator equations

```text
Q_i = rho_num - S_i(lambda-mu)(1+z+z^2) = 0.
```

Thus the generic source target is the factored vanishing
`Q_0 Q_1 Q_2=0`; the `lambda=1` source branch uses the parallel scale-source
product.  Boundary guardrails have only zero products for checked pairs; the
contrast row has 82 nonzero products.

Focused replay:

```text
H3_REPEAT_SLOPE_NUMERATOR_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.26 maxrss=50024
```

## T2/T3 h=3 repeat loose pair-membership compiler

Stage selected: write the loose-triangle active-pair graph as explicit
reciprocal membership functions.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_PAIR_MEMBERSHIP_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_pair_membership_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_pair_membership_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_PAIR_MEMBERSHIP_COMPILER_PASS
```

Result: for `r,s in S`, the active pair condition is exactly

```text
1+1/r, 1+1/s, 1-1/(r+s), 1+1/r+1/s-1/(r+s) in H
```

with the non-pole and distinctness exclusions.  The loose target is then:
if `{r,s}`, `{r,t}`, and `{s,t}` are active pairs, then `r+s+t=0`.
Boundary guardrails have no loose pair-graph triangles; the contrast row has
two.

Focused replay:

```text
H3_REPEAT_LOOSE_PAIR_MEMBERSHIP_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=16.45 maxrss=50108
```

## T2/T3 h=3 repeat same-lambda collision system

Stage selected: phrase fixed-`lambda` failure as an explicit collision system
in the ratio-orbit and scale coordinates.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SAME_LAMBDA_COLLISION_SYSTEM.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_collision_system.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_collision_system.py
```

Expected digest:

```text
H3_REPEAT_SAME_LAMBDA_COLLISION_SYSTEM_PASS
```

Result: `H3-VALUE-INJECTIVE` is exactly absence of:

```text
two admissible generic S3 ratio orbits for one lambda != 1;
two admissible primitive-cube scale orbits for lambda = 1.
```

Boundary guardrails have no such systems.  The contrast row has exactly one
generic same-lambda collision, at `lambda=27`.

Focused replay:

```text
H3_REPEAT_SAME_LAMBDA_COLLISION_SYSTEM_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=20.81 maxrss=50160
```

## T2/T3 h=3 repeat loose six-point system

Stage selected: turn the loose pair-graph triangle into an explicit six-point
additive system.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_SIX_POINT_SYSTEM.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_six_point_system.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_six_point_system.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_SIX_POINT_SYSTEM_PASS
```

Result: a genuine loose obstruction is exactly a solution of

```text
r,s,t,-(r+s),-(r+t),-(s+t) in S
Lambda(r,s), Lambda(r,t), Lambda(s,t) in H
r+s+t != 0.
```

The six reciprocal points are distinct and form the three zero-sum active
edges with empty total intersection.  Boundary guardrails have no such system;
the contrast row has two.

Focused replay:

```text
H3_REPEAT_LOOSE_SIX_POINT_SYSTEM_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=17.96 maxrss=50036
```

## T2/T3 h=3 repeat loose normalized system

Stage selected: normalize a loose six-point system by scaling one core
reciprocal vertex.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_NORMALIZED_SYSTEM.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_normalized_system.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_normalized_system.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_NORMALIZED_SYSTEM_PASS
```

Result: with `s=ar`, `t=br`, and `X=1/r`, a loose six-point system becomes
six coordinate tests

```text
1+X/q in H, q in {1,a,b,-(1+a),-(1+b),-(a+b)}
```

plus three lambda tests and `1+a+b != 0`.  The contrast row has two loose
systems, giving twelve ordered normalizations; boundary guardrails have none.

Focused replay:

```text
H3_REPEAT_LOOSE_NORMALIZED_SYSTEM_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=19.23 maxrss=50108
```

## T2/T3 h=3 repeat loose affine-slope compiler

Stage selected: package the normalized loose system as a single affine-line
subgroup membership problem.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_AFFINE_SLOPE_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_affine_slope_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_affine_slope_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_AFFINE_SLOPE_COMPILER_PASS
```

Result: with `s=ar`, `t=br`, and `X=1/r`, every normalized loose membership
test has the form `1+c_i X in H`.  The six coordinate slopes are

```text
1, 1/a, 1/b, -1/(1+a), -1/(1+b), -1/(a+b)
```

and the three lambda slopes are

```text
1+1/a-1/(1+a), 1+1/b-1/(1+b), 1/a+1/b-1/(a+b).
```

Boundary guardrails have no such affine nine-slope system.  The contrast row
has two loose systems, twelve ordered normalizations, and six distinct sorted
nine-slope sets.

Focused replay:

```text
H3_REPEAT_LOOSE_AFFINE_SLOPE_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=18.55 maxrss=50108
```

## T2/T3 h=3 repeat loose normalized-orbit compiler

Stage selected: quotient normalized loose systems by the `S_3` action on the
three core vertices.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_NORMALIZED_ORBIT_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_normalized_orbit_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_normalized_orbit_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_NORMALIZED_ORBIT_COMPILER_PASS
```

Result: the six ordered normalizations of one loose core have ratio pairs

```text
(a,b), (b,a), (1/a,b/a), (b/a,1/a), (1/b,a/b), (a/b,1/b).
```

The contrast row has two normalized loose orbits and six distinct sorted
nine-slope sets.  Boundary guardrails have no normalized loose orbits.

Focused replay:

```text
H3_REPEAT_LOOSE_NORMALIZED_ORBIT_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=19.09 maxrss=50232
```

## T2/T3 h=3 repeat loose slope-multiplicity ledger

Stage selected: record the effective number of distinct affine slopes in the
normalized loose target.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_SLOPE_MULTIPLICITY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_slope_multiplicity.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_slope_multiplicity.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_SLOPE_MULTIPLICITY_PASS
```

Result: the six coordinate slopes are distinct under the full normalized
loose-system hypotheses, meaning non-poles plus distinctness of the six
reciprocal points.  The lambda slopes are mutually distinct in a genuine loose
system; remaining duplicates are lambda-coordinate collisions.  In the contrast
row, six ordered normalizations have nine distinct slopes and six have eight
distinct slopes with one duplicate.  Boundary guardrails have no loose slope
patterns.

Focused replay:

```text
H3_REPEAT_LOOSE_SLOPE_MULTIPLICITY_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=20.05 maxrss=50108
```

## T2/T3 h=3 repeat loose coordinate-slope distinctness

Stage selected: make the coordinate-slope distinctness claim in the normalized
loose target symbolic rather than finite-row implicit.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_COORDINATE_SLOPE_DISTINCTNESS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_coordinate_slope_distinctness.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_coordinate_slope_distinctness.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_COORDINATE_SLOPE_DISTINCTNESS_PASS
```

Result: the six coordinate slopes are the inverses of the six normalized
reciprocal multipliers.  Under the full normalized loose-system hypotheses,
the multipliers are distinct and nonzero, so the six coordinate slopes are
distinct.  The collision table also records why non-poles alone are too weak:
collisions such as `a=1` are ordinary six-point distinctness failures, while
`1+a+b=0` is the contained zero-sum triangle case.

Focused replay:

```text
H3_REPEAT_LOOSE_COORDINATE_SLOPE_DISTINCTNESS_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=19.37 maxrss=50232
```

## T2/T3 h=3 repeat loose lambda-slope collision compiler

Stage selected: classify the remaining possible slope multiplicities in the
normalized loose target.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_LAMBDA_SLOPE_COLLISIONS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_lambda_slope_collisions.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_lambda_slope_collisions.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_LAMBDA_SLOPE_COLLISIONS_PASS
```

Result: the lambda slopes

```text
L_a, L_b, L_ab
```

are mutually distinct in a genuine normalized loose system.  The three
lambda-lambda collision numerators factor as

```text
-(a-b)(a+b+1),  a(b-1)(a+b+1),  b(a-1)(a+b+1),
```

so every such collision violates non-poles, looseness, or six-point
distinctness.  The only remaining multiplicity branch is
lambda-coordinate collision, now reduced to nine explicit divisors.

Focused replay:

```text
H3_REPEAT_LOOSE_LAMBDA_SLOPE_COLLISIONS_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=34.21 maxrss=52072
```

## T2/T3 h=3 repeat loose collision-orbit compiler

Stage selected: quotient the nine lambda-coordinate collision divisors by the
normalized `S_3` action.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_COLLISION_ORBIT_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_collision_orbit_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_collision_orbit_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_COLLISION_ORBIT_COMPILER_PASS
```

Result: the nine lambda-coordinate collision divisors split into two
normalized branch types.  Orbit A has size `3`, represented by `L_a=1/b`.
Orbit B has size `6`, represented by `L_a=-1/(1+b)`.  Future loose-line
arguments can therefore split into the generic nine-slope branch plus these
two special branches, rather than nine raw cases.

Focused replay:

```text
H3_REPEAT_LOOSE_COLLISION_ORBIT_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=32.91 maxrss=52000
```

## T2/T3 h=3 repeat loose collision-branch parametrization

Stage selected: solve the two normalized lambda-coordinate collision branch
representatives for `b`.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_COLLISION_BRANCH_PARAMETRIZATION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_collision_branch_parametrization.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_collision_branch_parametrization.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_COLLISION_BRANCH_PARAMETRIZATION_PASS
```

Result: with `D=a^2+a+1`, the two special branch types are

```text
branch A: b = a(a+1)/D,
branch B: b = -(2a^2+2a+1)/D.
```

The replay also emits the one-variable secondary-collision pullbacks inside
each branch.  This makes the loose multiplicity branch a generic two-variable
case plus two explicit one-variable special families.

Focused replay:

```text
H3_REPEAT_LOOSE_COLLISION_BRANCH_PARAMETRIZATION_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=33.68 maxrss=52068
```

## T2/T3 h=3 repeat loose case-split interface

Stage selected: compose the loose distinctness, collision, orbit, and branch
parametrization packets into the exact counting interface.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_CASE_SPLIT_INTERFACE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_case_split_interface.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_case_split_interface.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_CASE_SPLIT_INTERFACE_PASS
```

Result: the loose affine-line target is now organized as:

```text
generic:  nine distinct slopes;
branch A: b = a(a+1)/(a^2+a+1);
branch B: b = -(2a^2+2a+1)/(a^2+a+1).
```

Secondary subcells are exactly the one-variable pullbacks already emitted by
the branch-parametrization compiler.

Focused replay:

```text
H3_REPEAT_LOOSE_CASE_SPLIT_INTERFACE_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=33.63 maxrss=52156
```

## T2/T3 h=3 repeat loose branch slope maps

Stage selected: write the two normalized collision branches as explicit
one-parameter slope families with degree budgets.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_BRANCH_SLOPE_MAPS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_branch_slope_maps.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_branch_slope_maps.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_BRANCH_SLOPE_MAPS_PASS
```

Result: branch A has the forced duplicate `C_b=L_a` and eight unique slope
maps of rational degree at most `4`.  Branch B has the forced duplicate
`C_1b=L_a` and eight unique slope maps of rational degree at most `6`.
Therefore the special loose branches are explicit one-parameter rational
slope families, but not degree-2 rich-curve instances.

Focused replay:

```text
H3_REPEAT_LOOSE_BRANCH_SLOPE_MAPS_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=37.09 maxrss=52836
```

## T2/T3 h=3 repeat loose branch degree compiler

Stage selected: compile denominator-clearing degree budgets for the two special
branch membership maps `1+c_i(a)X`.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_BRANCH_DEGREE_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_branch_degree_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_branch_degree_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_BRANCH_DEGREE_COMPILER_PASS
```

Result: writing `1+c_i(a)X=P_i(a,X)/Q_i(a)`, branch A has aggregate degree
budgets `S_a=17`, `S_total=22`; branch B has `S_a=19`, `S_total=24`.  For an
auxiliary with `deg_a<A`, `deg_X<C`, `deg_Y<B` and subgroup order `n`, the
cleared branch polynomial has

```text
deg_a     <= A-1+n(B-1)S_a,
deg_X     <= C-1+8n(B-1),
total_deg <= A+C-2+n(B-1)S_total.
```

Focused replay:

```text
H3_REPEAT_LOOSE_BRANCH_DEGREE_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=56.89 maxrss=52728
```

The focused replay remains under one minute but is now close to that boundary;
future additions to this harness should replace or optimize existing symbolic
loose-branch checks rather than growing it blindly.

## T2/T3 h=3 repeat loose generic degree compiler

Stage selected: compile denominator-clearing degree budgets for the generic
nine-slope loose membership maps `1+c_i(a,b)X`.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_GENERIC_DEGREE_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_generic_degree_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_generic_degree_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_GENERIC_DEGREE_COMPILER_PASS
```

Result: writing `1+c_i(a,b)X=P_i(a,b,X)/Q_i(a,b)`, the generic nine-map target
has aggregate budgets `S_a=7`, `S_b=7`, and `S_total=15`.  For an auxiliary
with `deg_a<A`, `deg_b<B0`, `deg_X<C`, `deg_Y<Y` and subgroup order `n`,

```text
deg_a     <= A-1+7n(Y-1),
deg_b     <= B0-1+7n(Y-1),
deg_X     <= C-1+9n(Y-1),
total_deg <= A+B0+C-3+15n(Y-1).
```

Focused replay:

```text
H3_REPEAT_LOOSE_GENERIC_DEGREE_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=39.54 maxrss=52900
```

## T2/T3 h=3 repeat loose Stepanov compiler

Stage selected: package the generic and two special loose degree budgets into
one conditional Stepanov arithmetic interface.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_STEPANOV_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_stepanov_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_stepanov_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_STEPANOV_COMPILER_PASS
```

Result: for a loose target with `m` parameter variables, `k` membership maps,
parameter box degree `P`, source degree `C`, subgroup degree `B`, multiplicity
`D`, and repaired parameter family `Z`,

```text
coefficients = P^m C B^k,
conditions   <= D(C+kD) |Z|,
L_X          = C-1+k n(B-1).
```

The parameter monomials enlarge the auxiliary space but do not multiply the
reduced `X`-jet condition count once the parameter value is fixed.  A strong
rank sufficient form additionally needs `rank(substitution over Z) >
D(C+kD)|Z|`; per independent fiber this requires enough `X`-degree capacity,
e.g. `L_X+1 > D(C+kD)`.

The missing gates are now explicitly:

```text
LOOSE-GEN-RANK/NV,
LOOSE-A-RANK/NV,
LOOSE-B-RANK/NV.
```

Focused replay:

```text
H3_REPEAT_LOOSE_STEPANOV_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=40.37 maxrss=52876
```

## T2/T3 h=3 repeat loose rank-minor compiler

Stage selected: turn the strong sufficient loose rank gates into explicit
rank-minor degree bounds.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_RANK_MINOR_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_rank_minor_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_rank_minor_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_RANK_MINOR_COMPILER_PASS
```

Result: for the replayed sample box `P=16, C=512, B=4, D=2, |Z|=1, n=32`,
the strong rank targets are:

```text
generic:  r=1061, entry degree 1470, minor degree <= 1559670;
branch A: r=1057, entry degree 2127, minor degree <= 2248239;
branch B: r=1057, entry degree 2319, minor degree <= 2451183.
```

This does not prove the rank gates; it states their bounded-degree bad-minor
avoidance form.

Focused replay:

```text
H3_REPEAT_LOOSE_RANK_MINOR_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=37.78 maxrss=52900
```

## T2/T3 h=3 repeat star conditional assembly

Stage selected: connect the disjoint-pair and loose-triangle gates back to the
repeat-boundary residue payment.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_STAR_CONDITIONAL_ASSEMBLY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_star_conditional_assembly.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_star_conditional_assembly.py
```

Expected digest:

```text
H3_REPEAT_STAR_CONDITIONAL_ASSEMBLY_PASS
```

Result: the five gates

```text
H3-VALUE-INJECTIVE,
H3-SLOPE-RATIO-HIT,
LOOSE-GEN-RANK/NV,
LOOSE-A-RANK/NV,
LOOSE-B-RANK/NV
```

imply `tau_coord<=1`, hence

```text
repeat_residue <= 90n^2.
```

This is below `n^3` for every official row `n=2^13..2^41`.

Focused replay:

```text
H3_REPEAT_STAR_CONDITIONAL_ASSEMBLY_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=37.23 maxrss=52720
```

## T2/T3 h=3 repeat same-lambda degree compiler

Stage selected: give `H3-VALUE-INJECTIVE` explicit collision-incidence degree
budgets.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SAME_LAMBDA_DEGREE_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_degree_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_degree_compiler.py
```

Expected digest:

```text
H3_REPEAT_SAME_LAMBDA_DEGREE_COMPILER_PASS
```

Result: the generic same-lambda collision target has variables `(a,z,y)`, six
membership maps, and degree sums

```text
S_a=6, S_z=6, S_y=6, S_total=14.
```

The `lambda=1` scale collision target has two scale variables, six affine maps,
and `S_total=6` over a field containing a primitive cube root.

Focused replay:

```text
H3_REPEAT_SAME_LAMBDA_DEGREE_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=38.04 maxrss=52776
```

## T2/T3 h=3 repeat slope-miss degree compiler

Stage selected: give the generic `H3-SLOPE-RATIO-HIT` miss target explicit
membership and numerator degree budgets.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SLOPE_MISS_DEGREE_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_miss_degree_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_miss_degree_compiler.py
```

Expected digest:

```text
H3_REPEAT_SLOPE_MISS_DEGREE_COMPILER_PASS
```

Result: the generic lambda-distinct source/target system has six membership
maps with

```text
S_a=3, S_b=3, S_z=6, S_y=6, S_total=14.
```

The three cleared slope-hit factors have total degrees `15,13,13`; their
product has total degree bounded by `41`.  The scale-source branch remains
separate.

Focused replay:

```text
H3_REPEAT_SLOPE_MISS_DEGREE_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=39.47 maxrss=52896
```

## T2/T3 h=3 repeat same-lambda orbit-domain compiler

Stage selected: make the non-diagonal domain in `H3-VALUE-INJECTIVE` explicit
before attempting any emptiness/counting argument.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SAME_LAMBDA_ORBIT_DOMAIN.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_orbit_domain.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_orbit_domain.py
```

Expected digest:

```text
H3_REPEAT_SAME_LAMBDA_ORBIT_DOMAIN_PASS
```

Result: for generic same-lambda collisions, two ratio representatives `z,y`
are genuinely off the same `S_3` orbit exactly when the six divisors

```text
y-z, yz-1, y+z+1, y(1+z)+1, yz+z+1, y(1+z)+z
```

are all nonzero.  Their product has degree profile
`deg_z=6, deg_y=6, total=10`; the non-pole product has profile
`deg_z=4, deg_y=4, total=8`.  In the `lambda=1` scale branch, two scale
representatives are distinct exactly when `x^3-y^3 != 0`.

Focused replay:

```text
H3_REPEAT_SAME_LAMBDA_ORBIT_DOMAIN_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=38.62 maxrss=52900
```

## T2/T3 h=3 repeat slope mixed degree compiler

Stage selected: close the explicit generic/scale branch gap left by the
generic slope-miss degree compiler.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SLOPE_MIXED_DEGREE_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_mixed_degree_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_mixed_degree_compiler.py
```

Expected digest:

```text
H3_REPEAT_SLOPE_MIXED_DEGREE_COMPILER_PASS
```

Result: mixed generic/scale lambda-distinct pairs have six membership maps
with `S_total=10`.  With the generic edge used as source, the three hit
factors each have degree profile

```text
deg_a=3, deg_z=6, deg_x=3, total=9.
```

Thus the mixed hit-product total degree is at most `27`.  The reverse
scale-source orientation has the same total bound and is recorded for the
existing oriented numerator compiler.

Focused replay:

```text
H3_REPEAT_SLOPE_MIXED_DEGREE_COMPILER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=39.65 maxrss=52772
```

## T2/T3 h=3 repeat slope branch assembly

Stage selected: make the `H3-SLOPE-RATIO-HIT` branch structure explicit after
banking the generic and mixed degree compilers.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SLOPE_BRANCH_ASSEMBLY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_branch_assembly.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_branch_assembly.py
```

Expected digest:

```text
H3_REPEAT_SLOPE_BRANCH_ASSEMBLY_PASS
```

Result: `H3-SLOPE-RATIO-HIT` is covered by two branch gates:

```text
H3-SLOPE-GG-HIT,
H3-SLOPE-MIXED-HIT.
```

The scale-scale case is impossible for lambda-distinct pairs.  The current
degree interfaces are `S_total=14`, product total `<=41` for generic-generic,
and `S_total=10`, product total `<=27` for mixed generic/scale.

Focused replay:

```text
H3_REPEAT_SLOPE_BRANCH_ASSEMBLY_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=39.86 maxrss=52892
```

## T2/T3 h=3 repeat loose secondary subcells

Stage selected: quantify the finite lower-dimensional exceptions inside the
two one-parameter loose collision branches.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_SECONDARY_SUBCELLS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_secondary_subcells.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_secondary_subcells.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_SECONDARY_SUBCELLS_PASS
```

Result: after stripping structural non-poles `a`, `a+1`, and `a^2+a+1`,
the residual secondary products have degrees

```text
branch A: 24,
branch B: 29.
```

Away from those finite parameter loci, the special branches have exactly
eight distinct slopes.  Tiny finite guardrails over `p=5,7,11,13,17,97`
checked `186` valid branch parameters.

Focused replay:

```text
H3_REPEAT_LOOSE_SECONDARY_SUBCELLS_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=41.50 maxrss=53256
```

## T2/T3 h=3 repeat loose secondary payment

Stage selected: pay the finite secondary loose subcells directly, instead of
leaving them inside the branch rank/nonvanishing gates.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_SECONDARY_PAYMENT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_secondary_payment.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_secondary_payment.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_SECONDARY_PAYMENT_PASS
```

Result: branch A has at most `24` secondary parameters and branch B at most
`29`.  For each fixed secondary parameter, the slope `1` condition alone
gives at most `n` values of `X`, so the combined secondary payment is

```text
53n.
```

This is below `n^2` for every official row `n=2^13..2^41`.

Focused replay:

```text
H3_REPEAT_LOOSE_SECONDARY_PAYMENT_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=42.48 maxrss=53128
```

## T2/T3 h=3 repeat same-lambda scale count

Stage selected: bound the exceptional `lambda=1` same-lambda scale branch
directly in count/payment routes.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SAME_LAMBDA_SCALE_COUNT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_scale_count.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_scale_count.py
```

Expected digest:

```text
H3_REPEAT_SAME_LAMBDA_SCALE_COUNT_PASS
```

Result: if a primitive cube root exists, the number of admissible
`lambda=1` scale orbits is bounded by

```text
K_1 <= floor((n-1)/3).
```

Therefore scale same-lambda collision pairs are bounded by
`binom(floor((n-1)/3),2)`, which is below `n^2` on every official row.  If no
primitive cube root exists, the scale branch is empty.

Focused replay:

```text
H3_REPEAT_SAME_LAMBDA_SCALE_COUNT_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=42.61 maxrss=53476
```

## T2/T3 h=3 repeat same-lambda branch assembly

Stage selected: split the same-lambda value gate into strict generic/scale
subgates and record the separate scale count route.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SAME_LAMBDA_BRANCH_ASSEMBLY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_branch_assembly.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_branch_assembly.py
```

Expected digest:

```text
H3_REPEAT_SAME_LAMBDA_BRANCH_ASSEMBLY_PASS
```

Result: the strict value gate decomposes as

```text
H3-VALUE-GEN-INJECTIVE + H3-VALUE-SCALE-INJECTIVE
  => H3-VALUE-INJECTIVE.
```

The generic branch has membership `S_total=14` and off-orbit product total
degree `10`; the scale branch has membership `S_total=6` and off-orbit degree
`3`.  Count routes can instead keep the generic strict gate and pay at most
`binom(floor((n-1)/3),2)` scale collision pairs.

Focused replay:

```text
H3_REPEAT_SAME_LAMBDA_BRANCH_ASSEMBLY_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=41.39 maxrss=53264
```

## T2/T3 h=3 repeat star refined assembly

Stage selected: connect the new branch gates back to the strict
repeat-boundary star route without conflating paid exceptional ledgers with
`tau_coord<=1`.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_STAR_REFINED_ASSEMBLY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_star_refined_assembly.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_star_refined_assembly.py
```

Expected digest:

```text
H3_REPEAT_STAR_REFINED_ASSEMBLY_PASS
```

Result: the strict branch-level route has seven primitive gates:

```text
H3-VALUE-GEN-INJECTIVE,
H3-VALUE-SCALE-INJECTIVE,
H3-SLOPE-GG-HIT,
H3-SLOPE-MIXED-HIT,
LOOSE-GEN-RANK/NV,
LOOSE-A-RANK/NV,
LOOSE-B-RANK/NV.
```

These imply the coarse five-gate star route and hence
`repeat_residue <= 90n^2`.  The scale-pair bound and loose-secondary `53n`
payment are recorded as count-route ledgers, not as premises for the strict
`tau_coord<=1` theorem.

Focused replay:

```text
H3_REPEAT_STAR_REFINED_ASSEMBLY_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=41.74 maxrss=53260
```

## T2/T3 h=3 repeat frontier ledger

Stage selected: create a replayed single-source ledger for the current
branch-level h=3 repeat-boundary frontier.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_FRONTIER_LEDGER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_frontier_ledger.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_frontier_ledger.py
```

Expected digest:

```text
H3_REPEAT_FRONTIER_LEDGER_PASS
```

Result: the ledger imports the same-lambda, slope, loose degree, loose
rank-minor, and paid-ledger compilers and verifies the current strict branch
frontier:

```text
H3-VALUE-GEN-INJECTIVE:   S_total=14, extra=10,
H3-VALUE-SCALE-INJECTIVE: S_total=6,  extra=3,
H3-SLOPE-GG-HIT:          S_total=14, extra=41,
H3-SLOPE-MIXED-HIT:       S_total=10, extra=27,
LOOSE-GEN-RANK/NV:        S_total=15,
LOOSE-A-RANK/NV:          S_total=22,
LOOSE-B-RANK/NV:          S_total=24.
```

It also replays the sample loose rank-minor degrees and the first-official
paid ledgers: scale pairs `<=3725085`, loose secondary `<=434176`.

Focused replay:

```text
H3_REPEAT_FRONTIER_LEDGER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=43.19 maxrss=53264
```

## T2/T3 h=3 repeat LP4 exception ledger

Stage selected: make the generic LP4 line-pencil gate's excluded and paid
line-parameter cells explicit.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LP4_EXCEPTION_LEDGER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lp4_exception_ledger.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lp4_exception_ledger.py
```

Expected digest:

```text
H3_REPEAT_LP4_EXCEPTION_LEDGER_PASS
```

Result: the first three LP4 coefficients collide only for

```text
r in {0, -1, 1, -1/2, -2}.
```

The first two values are invalid and the other three force duplicate boundary
coordinates, so they do not contribute to the distinct-boundary LP4 target.
The remaining exceptional cell `r^2+r+1=0` is q0, already paid by
`B_q0 <= 132 n^(2/3)` and repeat contribution `<=1584 n^(5/3)`.

Focused replay:

```text
H3_REPEAT_LP4_EXCEPTION_LEDGER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=45.82 maxrss=53264
```

## T2/T3 h=3 repeat support crossover

Stage selected: replace the stale conservative prose thresholds for a linear
quotient-support theorem with an exact replayed integer-cap crossover table.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SUPPORT_CROSSOVER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_support_crossover.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_support_crossover.py
```

Expected digest:

```text
H3_REPEAT_SUPPORT_CROSSOVER_PASS
```

Result: using

```text
B_line <= ceil(132 n^(2/3)) + 6 floor(Cn) ceil(66 n^(2/3)),
```

the official-row tails for `R_orb <= Cn` are:

```text
C=1/4: 2^31..2^41,
C=1/2: 2^34..2^41,
C=1:   2^37..2^41,
C=2:   2^40..2^41,
C=4:   no official tail.
```

Focused replay:

```text
H3_REPEAT_SUPPORT_CROSSOVER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=43.61 maxrss=53264
```

## 2026-07-09 resumed frontier tightening

Stage selected: proof-surface tightening on the current h=3/T4 blockers, with
no broad numerical sweep.  The aim was to prevent stale interfaces from
misdirecting the next theorem attempt.

Banked commits:

```text
13ed128 Add h3 conic bridge accounting ledger
526b3ee Clarify h3 repeat count-route frontier
496865d Add h5 reciprocal compatibility compiler
642160d Record h8 rotation-orbit residual target
60d0105 Add h5 central reciprocal compatibility row
949a1ac Add h3 bridge-budget lineage ledger
```

Key results:

```text
h=3 conic bridge: charge one conic image/key per same-(e1,e2) fiber,
not one per ordered triple or basepoint.

h=3 repeat frontier: strict route has seven gates; count route pays the
lambda=1 scale branch and leaves six strict gates.

h=3 bridge budget: active Z_budget is the non-diagonal table 16..10795;
the diagonal 11..7420 table is legacy only.

h=5 norm gate: reciprocal elimination gives four delta-free equations:
C14,C24,C34 plus central C54, with max total degree 10.

h=8 residual: safe rotation canonicalization reduces the non-antipodal
support target to 7,633,233,227,520 orbits, still far from a direct
laptop-scale enumeration.
```

Replays:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_bridge_accounting_ledger.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_frontier_ledger.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_lineage.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_reciprocal_compatibility_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_t4_residual_frontier_ledger.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_frontier_ledger.py
```

Expected digests:

```text
H3_CONIC_BRIDGE_ACCOUNTING_LEDGER_PASS
H3_REPEAT_FRONTIER_LEDGER_PASS
H3_BRIDGE_BUDGET_LINEAGE_PASS
H5_RECIPROCAL_COMPATIBILITY_COMPILER_PASS
F3_T4_RESIDUAL_FRONTIER_LEDGER_PASS
H3_FRONTIER_LEDGER_PASS
```

## 2026-07-09 h=3 exact-profile bridge budget

Stage selected: consume the exact rich-curve reduced-condition profile in the
h=3 bridge-budget arithmetic.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_EXACT_PROFILE_BRIDGE_BUDGET.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_exact_profile_bridge_budget.py
```

The compiler replaces the legacy condition count

```text
13D(A+D)|Z|
```

by the proved exact profile

```text
|Z|*(DA + 6D(D-1)).
```

For every official row `n=2^s`, `13 <= s <= 41`, it verifies a passing
non-diagonal box with

```text
Z_exact = 33..21421,
```

where the active legacy non-diagonal table had

```text
Z_legacy = 16..10795.
```

The total gain over the active non-diagonal table is `51451`.  The compiler
also verifies maximality within the same box search: `Z_exact+1` has no
feasible box under the analytic `B` cap derived from the `16n` target and the
image-rank room condition.

This does not prove `RC-NV` or the bridge assignment theorem; it gives those
future steps a larger conditional budget once the exact-profile rank theorem
is proved.

Replays:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_exact_profile_bridge_budget.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_frontier_ledger.py
```

Expected digests:

```text
H3_EXACT_PROFILE_BRIDGE_BUDGET_PASS
H3_FRONTIER_LEDGER_PASS
```

## 2026-07-09 h=3 exact-profile rank-capacity guard

Stage selected: prevent the exact-profile bridge budget from being interpreted
as duplicate curve-image capacity.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_EXACT_PROFILE_RANK_CAPACITY_GUARD.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_exact_profile_rank_capacity_guard.py
```

For every official exact-profile box, the compiler verifies

```text
floor((A B^3 - 1) / (DA+6D(D-1))) = Z_exact,
floor(((A + 6n(B-1)) - 1) / (DA+6D(D-1))) = 1,
floor((A(3B-2) - 1) / (DA+6D(D-1))) = 0.
```

Thus the larger `Z_exact=33..21421` budget buys more distinct rank-effective
repaired images.  It does not allow one repaired curve image to be paid twice,
and it does not resurrect the constant-ratio collapsed cells.  This is still
only an arithmetic guard; `RC-RANK` and the bridge assignment remain open.

Replays:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_exact_profile_rank_capacity_guard.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_frontier_ledger.py
```

Expected digests:

```text
H3_EXACT_PROFILE_RANK_CAPACITY_GUARD_PASS
H3_FRONTIER_LEDGER_PASS
```

Residual next targets remain unchanged: finite-row-valid h=3 rank/minor
avoidance plus the matching bridge assignment, symbolic h=5 norm-gate
incompatibility, and h=8 non-antipodal support certification.

## 2026-07-09 h=5 reciprocal chart cover

Stage selected: remove the remaining chart-choice caveat from the h=5
reciprocal norm-gate interface.

Banked commits:

```text
3692b3d Add h5 base-free reciprocal system
eb5bff2 Add h5 reciprocal open-cover exclusion
```

Key results:

```text
Base-free reciprocal system:
  Treat E1,E2,E3,E4 and the central l5 row as five slots.
  Vanishing of all 2x2 minors gives 10 pairwise equations.
  All are linear in bar_l5..bar_l9 and have max total degree 10.

Open cover:
  If any denominator slot is nonzero, the pairwise equations recover delta.
  The only uncovered cell is bar_l5=...=bar_l9=0.
  On official rows n=2^s this cell is empty: it forces L_R(X)=X^10+l0,
  but x -> x^10 has fibers of size gcd(10,2^s)=2 in mu_{2^s}, too small
  for a 10-support.
```

Replays:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_basefree_reciprocal_system.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_reciprocal_open_cover.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_t4_residual_frontier_ledger.py
```

Expected digests:

```text
H5_BASEFREE_RECIPROCAL_SYSTEM_PASS
H5_RECIPROCAL_OPEN_COVER_PASS
F3_T4_RESIDUAL_FRONTIER_LEDGER_PASS
```

## 2026-07-09 h=3 rich-curve exact condition profile

Stage selected: optimize the arithmetic side of the h=3 rich-curve
`RC-RED` route without changing the open nonvanishing theorem.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RICH_CURVE_CONDITION_PROFILE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_condition_profile.py
```

The log-jet proof gives, for derivative order `j`, a reduced numerator degree
at most `(A-1)+12j`.  Therefore the exact over-imposed condition profile per
repaired curve is

```text
sum_{j=0}^{D-1}(A+12j) = DA + 6D(D-1),
```

instead of the legacy sufficient bound

```text
13D(A+D).
```

On the five reduced-condition sample boxes, the exact profile uses only
`7.84%..8.77%` of the legacy condition count and saves `3,444,473,440`
sample conditions in total.  This does not prove `RC-NV`, but it gives future
bridge-budget optimizers the sharper arithmetic target:

```text
rank(S_Z) > (DA + 6D(D-1)) |Z|.
```

Existing official budget tables remain valid because they use the larger
legacy condition count.

Replays:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_condition_profile.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_reduced_condition_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_nv_rank_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_frontier_ledger.py
```

Expected digests:

```text
H3_RICH_CURVE_CONDITION_PROFILE_PASS
H3_RICH_CURVE_REDUCED_CONDITION_COMPILER_PASS
H3_RICH_CURVE_NV_RANK_AUDIT_PASS
H3_FRONTIER_LEDGER_PASS
```

Residual h=5 target: prove the resulting official-row rank-one compatibility
system has no support solutions, or replace it by a scalable certificate
family.

## 2026-07-09 h=5 unit-norm reciprocal gate

Stage selected: use the root-of-unity nature of the h=5 support product to add
delta-free Hermitian equations to the symbolic norm-gate target.

Banked commit:

```text
6311ceb Add h5 unit-norm reciprocal gate
```

Key result:

```text
For reciprocal rows P_j = D_j delta*bar_l(10-j), the identity
delta*bar_delta=1 gives

  P_j * conjugate(P_j) = D_j^2 l(10-j) bar_l(10-j),  j=1..4.

The replay verifies four equations N1..N4 with term counts
485,325,170,101 and max total degree 18.
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_unit_norm_reciprocal_gate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_t4_residual_frontier_ledger.py
```

Expected digests:

```text
H5_UNIT_NORM_RECIPROCAL_GATE_PASS
F3_T4_RESIDUAL_FRONTIER_LEDGER_PASS
```

Residual h=5 target: combine the rank-one compatibility system, the official
open cover, and the unit-norm equations to prove symbolic incompatibility, or
replace this route with a scalable certificate family.

## 2026-07-09 h=5 chart-local reciprocal recovery

Stage selected: localize the h=5 reciprocal norm-gate equations chart by chart,
so the remaining symbolic target is smaller than the global equation pile.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CHART_RECOVERY_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_chart_recovery_compiler.py
```

Key result:

```text
On chart i, the four incident 2x2 minors recover
  delta = slot_i_num / slot_i_den.

For charts 1..4, unit norm is the matching Hermitian equation N_i.
For the central chart bar_l5 != 0, delta=l5/bar_l5 has unit norm
identically, so no Hermitian row is needed there.
```

The replay verifies the five chart obligations:

```text
chart 1: C12,C13,C14,C15 + N1
chart 2: C12,C23,C24,C25 + N2
chart 3: C13,C23,C34,C35 + N3
chart 4: C14,C24,C34,C45 + N4
chart 5: C15,C25,C35,C45 + tautological unit norm
```

The central tautology is also verified as a saturated ideal statement:

```text
l5*N_i in <C_i5, conjugate(C_i5)> for i=1..4.
```

The abstract rank-one unit-propagation compiler adds the general identity:

```text
B_i*bar_B_i*N_j - B_j*bar_B_j*N_i
  in <C_ij, conjugate(C_ij)>.
```

It verifies all `5*4=20` ordered chart-to-slot syzygies.

The abstract rank-one minor-propagation compiler adds the parallel identity:

```text
B_i*C_jk + B_k*C_ij - B_j*C_ik = 0.
```

It verifies all `5*binom(4,2)=30` chart-to-nonincident-minor syzygies, so the
four incident minors on a chart imply all ten pairwise minors after saturating
by the chart denominator.

The chart compiler now also profiles the five local systems:

```text
chart terms: 615,443,273,195,67
central chart: 4 equations, 67 total terms, max degree 10
```

The central chart graph compiler then verifies that the four central equations
are linear in `bar_l9,bar_l8,bar_l7,bar_l6` respectively:

```text
Cj5 = bar_l5*P_j - D_j*l5*bar_l(10-j).
```

Thus, on `bar_l5 != 0`, the central chart is an explicit rational graph after
saturating by `l5*bar_l5`.

The central fixed-point skeleton profiles the next compatibility step without
expanding it:

```text
pre-cancellation term bounds: 117907944 .. 1255488415957
max fixed-point total degree bound: 91
```

This records that the central chart should be attacked through the structured
graph, not by full fixed-point expansion.

The weighted-homogeneity compiler verifies the root-scaling grading:

```text
l5..l9 weights: 5,4,3,2,1
bar_l5..bar_l9 weights: -5,-4,-3,-2,-1
pairwise minor weights: 1..7
unit-row weights: 0
```

The official scaling-action compiler keeps the quotient finite-row honest:

```text
central chart stabilizer in mu_{2^s}: 1
central orbit size: n
```

This uses `bar_l5 != 0` and `gcd(5,2^s)=1`; arbitrary ambient scaling is not
an official-row symmetry.

Replays:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_official_scaling_action.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_weighted_homogeneity.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_fixedpoint_skeleton.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_chart_graph.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_rank_one_minor_propagation.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_rank_one_unit_propagation.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_chart_recovery_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_t4_residual_frontier_ledger.py
```

Expected digests:

```text
H5_OFFICIAL_SCALING_ACTION_PASS
H5_WEIGHTED_HOMOGENEITY_PASS
H5_CENTRAL_FIXEDPOINT_SKELETON_PASS
H5_CENTRAL_CHART_GRAPH_PASS
H5_RANK_ONE_MINOR_PROPAGATION_PASS
H5_RANK_ONE_UNIT_PROPAGATION_PASS
H5_CHART_RECOVERY_COMPILER_PASS
F3_T4_RESIDUAL_FRONTIER_LEDGER_PASS
```

Residual h=5 target: prove that no official-row support satisfies any one of
these five chart-local systems, or replace the route with a scalable
certificate family.

## 2026-07-09 h=3 lambda-one scale h=2 cap

Stage selected: sharpen the paid count route for the `lambda=1` scale branch
in the h=3 repeat-boundary star frontier.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LAMBDA_ONE_SCALE_H2_CAP.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_one_scale_h2_cap.py
```

Key result:

```text
{1+x,1+omega*x,1+omega^2*x} subset H
  => 1+x in H and 1+omega*x in H.

With Y=1+x, the second condition is omega*Y+(1-omega) in H,
so the h=2 affine-coset pair corollary gives at most 66 n^(2/3)
x-values.
```

Thus the scale-orbit count route now uses

```text
K_1 <= min(floor((n-1)/3), floor(ceil(66 n^(2/3))/3)).
```

The h=2 cap first improves the trivial orbit bound at `n=2^19`; the
first-official pair bound remains `3725085`.

Replays:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_one_scale_h2_cap.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_branch_assembly.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_frontier_ledger.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_frontier_ledger.py
```

Expected digests:

```text
H3_REPEAT_LAMBDA_ONE_SCALE_H2_CAP_PASS
H3_REPEAT_SAME_LAMBDA_BRANCH_ASSEMBLY_PASS
H3_REPEAT_FRONTIER_LEDGER_PASS
H3_FRONTIER_LEDGER_PASS
```

## 2026-07-09 h=3 repeat quotient/factorization refinements

Stage selected: tighten two open repeat-boundary star gates without adding a
new finite sweep.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SAME_LAMBDA_J_INVARIANT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_j_invariant.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SLOPE_EQUALITY_FACTORIZATION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_equality_factorization.py
```

Same-lambda refinement:

```text
J(z) = (1+z+z^2)^3 / (z^2(1+z)^2)
R(a,z) = -J(z)/a^3
numerator(J(z)-J(y)) = - generic_off_orbit_product(z,y)
```

Thus the degree-10 generic off-orbit product is the complete `S_3` quotient
invariant for ratio orbits.  `H3-VALUE-GEN-INJECTIVE` remains open, but is now
a value-uniqueness target for `J`, not a raw six-factor exclusion.  The
J-ramification compiler further shows that, on the generic domain, the only
remaining critical orbit is `{1,-2,-1/2}` with critical value `27/4`, and this
is exactly the duplicate-coordinate locus excluded by active-edge distinctness.

Slope refinement:

```text
generic-generic:
  Q_i = +/- product_j (source_increment_i*M - target_increment_j*N)
  product total degree = 41

mixed generic/scale:
  Q_i = +/- (source_increment_i^3 - x^3*N^3)
  product total degree = 27

mixed scale/generic:
  Q_{c^2} = +/- product_j(c*x*M - target_increment_j), c^3=1
  product total degree = 27
```

Thus `H3-SLOPE-GG-HIT` and `H3-SLOPE-MIXED-HIT` are exactly
coordinate-intersection targets after denominator clearing, in both mixed
orientations after cube-root relabelling.  The important negative information
is that the `lambda=1` scale count does not by itself pay the mixed slope
branch; a proof still needs forced generic/scale overlap or a separate residue
payment for mixed misses.

Focused replay:

```bash
/usr/bin/time -f 'elapsed=%e maxrss=%M' \
  python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_replay.py
```

Digest and timing:

```text
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=45.74 maxrss=53264
```

## 2026-07-09 h=5 central weighted slice

Stage selected: tighten the central-chart h=5 norm-gate target without
launching a new certificate sweep.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CENTRAL_WEIGHTED_SLICE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_weighted_slice.py
```

Key result:

```text
l5..l9 weights = 5,4,3,2,1
bar_l5..bar_l9 weights = -5,-4,-3,-2,-1
l5*bar_l5 has weight 0
```

For algebraic emptiness proofs on the central chart, any solution with
`l5*bar_l5=1` can be scaled over an algebraic extension to the slice

```text
l5 = 1,
bar_l5 = 1.
```

On this slice the four central graph equations remain linear in
`bar_l9,bar_l8,bar_l7,bar_l6` and have profile:

```text
C15: 23 terms, degree 9
C25: 19 terms, degree 8
C35: 14 terms, degree 7
C45: 11 terms, degree 6
```

The total central term count remains `67`, while the max graph degree drops
from `10` to `9`.

Caveat: this is an algebraic emptiness slice only.  It is not the official
finite-row orbit quotient; official row counting still uses the finite
`mu_n` action from the scaling-action packet.

Replays:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_weighted_slice.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_t4_residual_frontier_ledger.py
```

Expected digests:

```text
H5_CENTRAL_WEIGHTED_SLICE_PASS
F3_T4_RESIDUAL_FRONTIER_LEDGER_PASS
```

## 2026-07-09 h=5 central slice fixed-point skeleton

Stage selected: profile the central fixed-point compatibility after the
weighted slice, still without forming expanded fixed-point numerators.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CENTRAL_SLICE_FIXEDPOINT_SKELETON.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_slice_fixedpoint_skeleton.py
```

Key result:

```text
unsliced total degree bounds: 91, 81, 71, 61
sliced degree bounds:        81, 72, 63, 54
degree drops:                10, 9, 8, 7
```

The slice improves degree bookkeeping, but it does not improve the
pre-cancellation expansion-size bounds:

```text
F1 <= 1,255,488,415,957 terms
F2 <=    57,067,651,704 terms
F3 <=     2,593,979,107 terms
F4 <=       117,907,944 terms
```

Conclusion: the central slice is a useful normalization, but direct fixed-point
expansion remains the wrong primitive.  A central-chart proof should preserve
the sparse graph/saturation structure.

Replays:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_slice_fixedpoint_skeleton.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_t4_residual_frontier_ledger.py
```

Expected digests:

```text
H5_CENTRAL_SLICE_FIXEDPOINT_SKELETON_PASS
F3_T4_RESIDUAL_FRONTIER_LEDGER_PASS
```

## 2026-07-09 h=5 central slice tangent compiler

Stage selected: extract a local normal form from the weighted central slice,
without expanding the fixed-point equations.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CENTRAL_SLICE_TANGENT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_slice_tangent.py
```

Key graph tangent on the slice `l5=bar_l5=1`:

```text
bar_l9 = (1/2) l6 + higher order terms
bar_l8 = (1/2) l7 + higher order terms
bar_l7 = (1/2) l8 + higher order terms
bar_l6 = (1/2) l9 + higher order terms
```

Thus, in the orders `l6,l7,l8,l9` and `bar_l6,bar_l7,bar_l8,bar_l9`, the
graph tangent is the `1/2` anti-diagonal matrix.  Conjugating the graph gives
the same tangent matrix, so the relaxed fixed-point map has tangent `1/4 I`
and the fixed-point equations have linear part `3/4 I` with determinant
`81/256`.

Conclusion: away from characteristics `2` and `3`, the normalized origin is a
simple isolated fixed point of the relaxed sliced central graph.  This is a
local algebraic route guide, not an official-row h=5 closure and not a global
central-chart emptiness proof.

Replays:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_slice_tangent.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_t4_residual_frontier_ledger.py
```

Expected digests:

```text
H5_CENTRAL_SLICE_TANGENT_PASS
F3_T4_RESIDUAL_FRONTIER_LEDGER_PASS
```

## 2026-07-09 h=3 mixed slope reverse factorization

Stage selected: sharpen the `H3-SLOPE-MIXED-HIT` interface without launching a
finite search.

Updated files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SLOPE_EQUALITY_FACTORIZATION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_equality_factorization.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_FRONTIER_LEDGER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_frontier_ledger.py
```

New exact reverse-orientation identity:

```text
for c^3=1:
  Q_{c^2} = +/- product_j(c*x*M(y) - target_increment_j)
```

The square map permutes the three cube-root labels, so the scale-source /
generic-target orientation is the same coordinate-overlap condition as the
generic-source / scale-target orientation, after relabelling.  The product
total remains `27`.

Conclusion: this does not prove `H3-SLOPE-MIXED-HIT`, but it removes an
orientation caveat from the mixed slope target.  Any future mixed-branch proof
can target coordinate overlap without caring which edge was oriented as the
source.

Replays:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_equality_factorization.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_frontier_ledger.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_frontier_ledger.py
```

Expected digests:

```text
H3_REPEAT_SLOPE_EQUALITY_FACTORIZATION_PASS
H3_REPEAT_FRONTIER_LEDGER_PASS
H3_FRONTIER_LEDGER_PASS
```

## 2026-07-09 h=3 same-lambda J ramification

Stage selected: isolate structural ramification of the same-lambda quotient
invariant, without attempting a finite-field value-injectivity proof.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_SAME_LAMBDA_J_RAMIFICATION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_j_ramification.py
```

Exact derivative profile:

```text
J'(z) numerator   = (z-1)(z+2)(2z+1)(z^2+z+1)^2
J'(z) denominator = z^3(z+1)^3
```

The generic same-lambda ratio domain already excludes
`z=0`, `z=-1`, and `z^2+z+1=0`.  Therefore, away from characteristics `2`
and `3`, the only admissible critical orbit is

```text
{1, -2, -1/2},
```

with common critical value `27/4`.

This orbit is also exactly the duplicate-coordinate locus for the normalized
reciprocal triple `{r,zr,-(1+z)r}`.  After active-edge distinctness is imposed,
`J` has `0` active critical points on the generic domain.

The product-parameter compiler translates this into the original active-edge
cubic:

```text
U+V+W = a+3
UV+UW+VW = 2a+3
m(z)=UVW = a+1-a^3/J(z)
```

The product derivative has numerator
`a^3 z(z-1)(z+1)(z+2)(2z+1)`, so the product coordinate also has `0` active
critical points after generic non-poles and distinctness exclusions.

Conclusion: `H3-VALUE-GEN-INJECTIVE` remains open, but the remaining obstacle
is not hidden ramification of the quotient map `J`; it is the arithmetic
question of whether two distinct admissible `S_3` ratio orbits can satisfy the
same six membership conditions for fixed `lambda`.

Replays:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_j_ramification.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_product_parameter.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_frontier_ledger.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_frontier_ledger.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_replay.py
```

Expected digests:

```text
H3_REPEAT_SAME_LAMBDA_J_RAMIFICATION_PASS
H3_REPEAT_SAME_LAMBDA_PRODUCT_PARAMETER_PASS
H3_REPEAT_FRONTIER_LEDGER_PASS
H3_FRONTIER_LEDGER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
```

## 2026-07-09 h=5 central slice quadratic normal form

Stage selected: improve the symbolic `T4-H5-NORM-GATE` route without expanding
the huge central fixed-point numerators.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_CENTRAL_SLICE_QUADRATIC_NORMAL_FORM.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_slice_quadratic_normal_form.py
```

The compiler composes the central weighted-slice graph only through total
degree two, using simultaneous substitution to avoid cascading graph
components.  The relaxed fixed map through degree two is:

```text
F_l6 = l6/4
F_l7 = (3 l6^2 + 8 l7)/32
F_l8 = (3 l6 l7 + 4 l8)/16
F_l9 = (6 l6 l8 + 3 l7^2 + 8 l9)/32
```

Thus the fixed equations are `3/4` times the triangular quadratic system:

```text
l6 = 0
l7 - l6^2/8 = 0
l8 - l6 l7/4 = 0
l9 - l6 l8/4 - l7^2/8 = 0
```

The linear determinant remains `81/256`.  This still does not prove the h=5
central chart empty, but it gives a sharper local normal form for the
sparse/saturated route and confirms that the origin has no quadratic branch
hidden by the tangent calculation.

Replays:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_slice_quadratic_normal_form.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_t4_residual_frontier_ledger.py
```

Expected digests:

```text
H5_CENTRAL_SLICE_QUADRATIC_NORMAL_FORM_PASS
F3_T4_RESIDUAL_FRONTIER_LEDGER_PASS
```

## 2026-07-09 h=3 loose branch geometry

Stage selected: sharpen the `LOOSE-A-RANK/NV` and `LOOSE-B-RANK/NV`
interfaces without launching a finite search.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LOOSE_BRANCH_GEOMETRY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_branch_geometry.py
```

Exact branch relation:

```text
b_A(a) = a(a+1)/(a^2+a+1)
b_B(a) = -(2a^2+2a+1)/(a^2+a+1) = -1-b_A(a)
```

For both branches, `db/da` has denominator `(a^2+a+1)^2` and finite critical
factor `2a+1` up to sign.  The compiler verifies that this factor occurs in
the six-reciprocal-multiplier distinctness product, so after clean loose
distinctness there are `0` active finite branch-map ramification points.

The two clean eight-slope targets share exactly six unique slope maps:

```text
branch_A.C_1  = branch_B.C_1
branch_A.C_a  = branch_B.C_a
branch_A.C_b  = branch_B.C_1b
branch_A.C_1a = branch_B.C_1a
branch_A.C_1b = branch_B.C_b
branch_A.L_b  = branch_B.L_b
```

The private maps on both branches are `C_ab` and `L_ab`.  Conclusion:
branch-A and branch-B rank/NV proofs can share any argument that only uses the
six common maps, but a full eight-map proof still has to handle the private
maps separately.  This explains the branch-B degree premium without closing
either loose rank gate.

Replays:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_branch_geometry.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_frontier_ledger.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_frontier_ledger.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_replay.py
```

Expected digests:

```text
H3_REPEAT_LOOSE_BRANCH_GEOMETRY_PASS
H3_REPEAT_FRONTIER_LEDGER_PASS
H3_FRONTIER_LEDGER_PASS
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
```
