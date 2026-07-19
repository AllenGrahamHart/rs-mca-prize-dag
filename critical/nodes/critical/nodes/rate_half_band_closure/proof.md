# rate_half_band_closure proof status

No proof is currently known in this node folder.

The former AQB proof route is refuted: averaging is a convex combination of
single-box fiber counts and cannot create the required box-sharing gain.

The former P6 dihedral-sibling proof route is also refuted.  The local refutation
is recorded in `nodes/dihedral_sibling_window_certificate/proof.md`: the claimed
packet size is not a Chebyshev top-degree drop, true Dickson fibers are too
small in the first band, and the endpoint fixed-point sibling still fails the
degree audit.

The live full-determination target remains: cover the rate-`1/2` band
`2^33 < sigma <= 8,592,912,738` by a new priced mechanism.  A bracket-grade
obstruction for some band radius is a separate partial-result outcome, not a
proof of this node.

---

## WAVE-9 PIN BODY (proof addendum, 2026-07-17)


## Retraction of the fixed edge

The former target asserted safety at agreement

```text
k+8,592,912,738+1.
```

It is false. The dependency `rate_half_cyclic_rotated_prefix_floor` is valid
for every residual prefix size `1<=s<c`, and its list lower bound is
independent of `s`. Taking its maximal legal prefix `s=c-1`, with
`c=2^22` and `d=2048`, gives the same list at excess

```text
sigma_0=dc+c-1=8,594,128,895.
```

The quantitative conversion in
`rate_half_cyclic_simple_pole_mca_floor` then proves

```text
epsilon_ca,epsilon_mca>2^-83>2^-128
```

at `sigma_0` and, by radius monotonicity, at every positive excess below it.
The old proposed safe point lies strictly inside that interval.

This is not a numerical falsifier or an ordinary-list surrogate. It is the
same exact simple-pole slope count already proved in the dependency, with the
residual-prefix parameter used at its full stated range.

## Proved progress retained

The generalized pole theorem gives the uniform lower bracket

```text
a_RH(q)>=k+8,594,128,896
```

for every admissible field. The list/interleaved-list branch remains separate
and retains its proved cyclic lower floor. No list-safe or MCA-safe claim is
inferred from that lower floor.

The exact sparsification theorem
`rate_half_mca_sparse_layer_reduction` further reduces an upper certificate
at any later candidate to the conjunction of a far-pair CA bound and a sparse
mutual-layer bound. This identity is lossless; it does not estimate either
term.

The proved `rate_half_sparse_pinning_rigidity` theorem resolves the first
structural layer of the sparse term. Tangencies are at most `r` and are paid
whenever `q>=2^168`. Every remaining sparse slope is pinned to one nonzero
ambiguity polynomial and must obey the shared root, cofactor-degree, and
active-match budget printed in that node. Counting those coupled objects is
still open.

## Remaining proof

The node remains TARGET. One must locate a field-dependent agreement
`a_RH(q)` at or beyond the proved bracket, prove both terms of the exact safe
split are at most `floor(q/2^128)`, and prove the immediately preceding
agreement unsafe. The generic deep theorem and imported half-distance pincer
do not reach this near-capacity region.

## Strict `A=3` proved reduction

The proved node `rate_half_ca_hankel_strict_a3_slope_slack_ledger` now treats
every live parameter degree at the strict budget. It promotes no safe bound,
but any counterexample to `T<=2^39` must satisfy the exact `(e,h)` range,
maximal rational-normal kernel rank, row-saturation bound, clean-column bound,
and product-code weight printed there. The endpoint component classification
may be used only when `e=2^37,h=0`; larger degrees must be attacked through
their own slope-slack strata.

## Half-distance `A=3` proved reduction

The proved node
`rate_half_ca_hankel_half_distance_a3_slope_slack_ledger` handles every live
`A=3` degree at budget `2^39+1`, using the unique left singular block of the
transposed Hankel shape. Any counterexample to `T<=2^39+1` must satisfy its
exact `(e,h)` range, rational-normal rank, saturation, norm, and component
chambers. The only half-distance Hankel family not structurally routed by the
two all-degree `A=3` ledgers is now the separate `A=1` profile.

## Half-distance `A=1` proved reduction

The proved node
`rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger` strips each of
the three possible fixed cores and routes every remaining degree through an
exact Euclidean slope cap. Any `A=1` counterexample must satisfy its printed
core/degree/slack, residual saturation, norm, and component chambers. Thus
all unresolved strict and half-distance Hankel profiles now have all-degree
structural routers; excluding or realizing their strata remains open.

## Core-one maximal-degree component exclusion

The proved node
`rate_half_ca_hankel_a1_core_one_max_component_localization` sharpens the
`s=1,e=2^38-1,ell=0` face. Its exact component deficits select one dominant
`(2e_*+1,e_*)` component, bound all residual parameter degree by `e/5`, and
amplify the dominant separation rank to at least five. Rank-at-most-four
models are therefore removed from this face, but the high-rank component is
still a live obstruction.

## Core-one middle-Hankel cofactor interface

The proved node
`rate_half_ca_hankel_a1_core_one_middle_adjugate_factorization` identifies the
contracted middle catalecticant's complete adjugate as `lambda*q*q^T`. The
single linear regular factor localizes all rank loss and omission to one
projective slope. Any further attack on the mixed dominant component may use
these maximal-minor products as exact Hankel-chain equations.

## Core-one component norm interface

The proved node
`rate_half_ca_hankel_a1_core_one_component_norm_localization` combines the
cofactor and component ledgers. It supplies an exact norm power and
complementary factorization for every component, with dominant residual
degree `e-5b-1+D_*` and at least `14m+5b` completely split residual domain
fibers. This is the current exact object to exclude on the face.

## Core-one two-sided weld

The proved node
`rate_half_ca_hankel_a1_core_one_two_sided_complement_weld` interpolates the
opposite clean-slope quotient and eliminates it against the domain-saturated
complement. The resulting identities `(TSW7),(TSW8)` force the dominant
component to divide a product difference whose separated side has bidegree
at most `(e-5b-1+D_*,1)`. Classification of this welded high-rank factor is
the next obstruction.

## Zero-weld boundary

The proved node
`rate_half_ca_hankel_a1_core_one_zero_weld_quartic_boundary` uses map-degree
multiplicativity to eliminate `K=0` unless `b=0,D_*=1`. The sole survivor is
the exact quarter-bidegree factorization `(ZWB4)--(ZWB5)`, with three omitted
domain factors. Thus later work may treat the quartic separated boundary and
the nonzero-`K` weld as disjoint branches.

## Zero-weld exclusion

The proved node
`rate_half_ca_hankel_a1_core_one_zero_weld_exclusion` closes the former
quartic branch. At each of the three domain points omitted from `G_0`, the
separated identity excludes all `4e` clean roots of `Q_*`; only the one
exceptional supported slope can remain. Their total component-capacity cost
is at least `3(e-1)`, strictly above the exact capacity `C_*=e`. Therefore
`K!=0` throughout this face. The remaining task is to exclude or classify the
nonzero-weld system; no zero-weld shard remains.

## Nonzero-weld trace descent

The proved node
`rate_half_ca_hankel_a1_core_one_nonzero_weld_trace_descent` factors every
defect-domain and exceptional-slope trace as `K=-HJ`, with the small quotient
degree paid by the exact component deficit. If any trace is active, these are
the equations to classify. If every trace vanishes identically, the complete
split defect factor `B_XE_Z` divides `K`; prime allocation between `W` and
`B` then reduces the first weld to `W_1B_1-1=QK_1` in a smaller degree box.
This is exhaustive but does not yet contradict either branch.

## Trace-free allocation rigidity

The proved node
`rate_half_ca_hankel_a1_core_one_trace_free_allocation_rigidity` identifies
the global norm residual with the product of the local degree-defect
quotients. In the trace-free branch, `K_x=-H_xJ_x=0` forces `H_x=0`, so every
bad row factor divides `A,B`; the other local factor would have to divide
`E_Z` and contradicts its exceptional-root degree. The exceptional slope has
only two allocations. Cancelling the forced factors yields the exact reduced
complement square `(TFA7)`. No combinatorial allocation search remains, but
the reduced square is not yet excluded.

## Trace-free weld exclusion

The proved node
`rate_half_ca_hankel_a1_core_one_trace_free_exclusion` closes that reduced
square. One exceptional allocation contradicts the large saturated gcd. The
other makes every supported component fiber divide `P_X`, charging full
parameter deficit at each bad row. Capacity leaves only `b=0,D_*=1,c=1`,
where the exceptional degree drop requires one more `X`-degree in `A_1` than
is available after dividing `A` by `B_X`. Thus only the active-trace branch
of `(NWT4),(NWT7)` remains on this face.

## Active-trace core reduction

The proved node
`rate_half_ca_hankel_a1_core_one_active_trace_core_reduction` cancels every
zero domain trace from `A,B,K` and any zero exceptional trace through its
forced slope allocation. The resulting equations `(ACR4)` contain only
genuinely active split factors. A zero domain trace costs at least
`e_*-D_*` capacity, so none exists unless `b=0,D_*=1`; that boundary has only
the exceptional-only `c=1` core or a `c=2` core with one active deficit-one
domain row. This normalizes but does not exclude the active branch.

## Exceptional-trace allocation

The proved node
`rate_half_ca_hankel_a1_core_one_exceptional_trace_allocation` excludes the
exceptional `Z_W` allocation using the positive gcd with `P_X`. A zero
exceptional trace must instead divide `B` and cannot coexist with either
one-zero-domain boundary. Consequently every active core has the full first
complement `QV_a+P_XW_a=P`, and the exceptional status leaves exactly the
three systems `(ETA4)`.

## Exceptional-trace nonvanishing

The proved node
`rate_half_ca_hankel_a1_core_one_exceptional_trace_nonvanishing` closes the
zero-exceptional system. Its degree-`r-1` exceptional fiber would require an
`A_a` quotient of degree `D_0-r+1`, one above the exact global complement
degree. Therefore every `D_*=1` active core has nonzero exceptional trace.

## Active two-sided partition

The proved node
`rate_half_ca_hankel_a1_core_one_active_core_two_sided_partition` promotes the
two complement equations to exact squarefree divisor partitions on every
clean slope and saturated row. The complementary factors attain their global
degrees, and the active bad-row clean incidences satisfy the exact total
`(ATP7)--(ATP8)`. This identifies the current object but does not classify it.

## Active incidence reconstruction

The proved node
`rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction`
uses the exact partitions to normalize every clean and saturated fiber by its
monic locator. The nonincidence graph is connected by the strict inequalities
`T-D_*>2e_*` and `D_0-c>2r`. Equality of the two fiber evaluations therefore
turns locator ratios into unique row/column potentials and exact cycle
constraints. Coefficientwise degree-`e_*` Reed--Solomon membership is then
necessary and sufficient to interpolate the unique compatible biform; more
than `e_*` clean slopes force every saturated fiber. This is a complete
preprocessing criterion, not an exclusion of the two active systems.
Injectivity of both evaluation maps also identifies the ranks of the two
locator coefficient matrices and the core value matrix with `sr(Q)`, so the
existing dominant-component lower bound becomes a direct incidence-packet
rank gate. The node packet includes a bounded prime-field checker for this
preprocessing layer; it is not a substitute for the remaining Hankel and
active-trace classification.
