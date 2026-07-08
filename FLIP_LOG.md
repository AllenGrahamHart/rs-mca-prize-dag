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
combined support compiler, and the boundary-style support evidence.  It does
not launch Modal and does not run the older 55s aggregate.

Focused replay:

```text
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=2.25 maxrss=49904
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
