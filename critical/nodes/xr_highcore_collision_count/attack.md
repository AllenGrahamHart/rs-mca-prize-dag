# Attack surface

The proved strip rungs force every post-strip cross-slope core to have size at
most `k`; therefore a high-core collision has core exactly `k`. In error-set
notation, with

```text
R=n-k,       h=A-k,       r=n-A=R-h,
```

two colliding rays have error-set union of size exactly `R`.

The pair-moment identity is an instrument only. Dense pencils can make
`sum_W C(mult(W),2)` much larger than the number of distinct slopes, so a
moment bound is not an honest replacement for the target.

The proved `xr_highcore_component_union_atlas` removes the chart-overlap
ambiguity. It partitions the high-core slopes into canonical collision
components `C`, chooses one witness ray per slope, and assigns the component
the union chart `U_C` of size `R+d_C`. The exact aggregate ledger is

```text
#high-core slopes = sum_C |Z_C|,
|Z_C| <= floor(C(R+d_C,d_C) R / C(d_C+h,d_C)).
```

Thus slopes, collision cores, and charts are deduplicated before payment.
The denominator is the exact information-set occupancy forced by the
agreement reserve. The tangent-strip hypothesis prevents `h` persistent
zeros and is load-bearing.

The complementary proved `xr_direction_distance_ray_bound` pays any fixed
chart with

```text
(|U|-r)^2 > |U| (|U|-d_U(y_1))
```

by at most `|U|^2` slopes. Failure gives an explicit low-weight lift of the
received direction and hence a sparse-direction/near-pencil normal form. This
is a real dichotomy, but both sides are still per-chart.

Independently of the chart atlas, the proved
`xr_all_lineray_affine_core_bound` applies the nonuniform set-pair inequality
to any one-per-slope selector. If one selector has affine span dimension
`sigma`, then

```text
#high-core slopes <= C(sigma+r,sigma).
```

The exact candidate threshold is `sigma<=3`; all six `sigma=4` bounds exceed
`8n^3`. Consequently every counterexample to P-A must have rank at least four
for every selector. Applying the theorem to the complete pair family remains
a stronger pair-count branch, but is not required for this slope corollary.

At selector rank `s>=4`, the proved
`xr_highcore_collision_line_basis_ledger` assigns each collision line `ell`
its number `b_ell` of independent `(s-1)`-minors in the size-`k` common core.
It proves

```text
sum_ell b_ell <= C(n,s-1),
#points on ell <= floor((n-k)/(A-k)).
```

A basis-poor line is not an exception: if it has `b_ell=b`, then the entire
selector lies in one union chart of excess at most `b+s-2`, where GRK applies.
Choosing a minimum-basis line self-localizes the line ledger to that smaller
chart. If every core restriction is uniform, the ledger pays through selector
ranks `13,9,7,60,40,30` on the six rows.

The proved `xr_affine_core_cogirth_ray_bound` uses the rank-`s-1` kernel slice
inside the selector. Its coordinate matroid has enough information sets by a
deletion-contraction cogirth bound, giving

```text
#slopes C(h+s-1,s-1) <= C(N,s-1)(N-s+1).
```

On the full domain this pays selector ranks through `4,4,3,11,11,10` on the
six rows. On the self-localized charts left by the line ledger, it also pays
the RowC `1/16` rank-four residue. Thus selector rank four is completely
closed on every P-A row. Subsequent covering-free affine-pencil and
common-root charges move the first open selector ranks to `5,5,5` at RowC
and `17,17,15` at the prize rows.

The P9 diagnostics show that the residual is not automatically low-rank:
every `n=16,k=8` conservative far high-core family had no selector of rank at
most three; its canonical selector had rank `9=k+1` and its giant collision
component had `d_C=k`. Therefore the remaining task is the explicit
component-excess ledger

```text
sum_C floor(C(R+d_C,d_C) R / C(d_C+h,d_C)) <= 8n^3,
```

or a sharper sum using DDR on the high-direction components and its certified
sparse-direction normal form on the complement. A proof must control the
number of canonical components and their union excesses; the raw number of
possible subsets `U` no longer appears. Any rank-based continuation must use a
rank--weight or rank--collision tradeoff specific to the retained RS family.
The line-basis and cogirth theorems supply that tradeoff. The next local attack
is their higher-rank iteration, not another bare rank bound. In the uniform
cell, an over-budget selector now has the arbitrary-rank Maxwell/trade
certificate. Minimum-union rank-two residue is empty after the Plucker
quotient, and the first surviving shell `|X|=a+3` is one
quadratic-involution pullback chart. The local continuation is therefore
ownership/counting of that chart, higher support shells, and trade rank at
least three. The shell/Maxwell router additionally excludes primitive
full-core rank two whenever its explicit deficit is positive, including very
large first- and second-shell prize-rank intervals. Composing the exact core
size caps extends this to shell depths
`22,428,333;19,217,048;4,478,600`, and the rank-three edge-zero ledger removes
the remaining primitive first-shell case. The remaining low-shell problem is
therefore proper local-circuit ownership rather than an unnamed primitive
anomaly; the nonuniform-cell and cross-component aggregations remain separate
obligations. Every rank-two relation decomposes further into four/five-block
row-scaling circuits with an exact Segre coefficient atlas. The next ownership
argument should therefore work on those constant-arity support embeddings;
it should not reintroduce arbitrary block-family enumeration.

The canonical fundamental-circuit owner removes the remaining decomposition
choice inside a fixed rank-two trade. Choose its first three/four coefficient
anchors and charge every non-anchor only through its unique fundamental
circuit. The next compiler must operate one level earlier: assign each block
to its first Maxwell core and rank-two trade, enumerate the realized support
embedding of that canonical star, and deduplicate the anchor charges across
cores. Re-enumerating all circuit decompositions of one trade is now a route
error.

Split that compiler by coefficient rank. In the three-anchor branch, do not
search over arbitrary Segre coefficients: enumerate only root-avoiding tuples
`(X,P,Q,H)` from the exact dual-`GRS_3` factorization, then verify their
selected-block extensions and first-core owner. In the four-anchor branch,
retain the fundamental four/five-block star because there is no global
Mobius hyperplane. Mixing these branches discards a proved three-moment
constraint.

The four-anchor coefficient search is also no longer free. Transform every
non-anchor into canonical anchor coordinates, enforce the explicit pulled-
back determinant quadric and support three/four, and enforce the global
centroid before attempting any support realization. The only legitimate
rank-two compiler frontier is now the map from these two exact coefficient
atlases to selected agreement-block embeddings and first-core ownership.

For that map, do not enumerate arbitrary completed blocks `A_i`. Enumerate
the active fiber `Z_i`, forced-size inactive extension `T_i`, and unique
cofactor `R_i`; the dual support-extension theorem reconstructs both
numerators and rejects inconsistent data. The next new condition must come
from simultaneous received-pair agreement and Maxwell-core ownership, since
the dual-codeword extension condition itself is now exact.

Apply the received-pair router before those remaining block checks. The
three-anchor interaction matrix must be alternating and should be split by
`eta=0` versus `eta!=0`; the four-anchor row-space plane must annihilate both
received directions. Any support enumeration that retains coefficient planes
outside these loci is searching objects that cannot come from actual
agreement blocks.

Do not enumerate the remaining `h-1` parity rows either. Interpolate the
unique kernel correction on each candidate support, compute its external
zero set, and carry only the binomial forced-size extension count. The next
proof must couple these per-row external zero sets across one canonical
circuit star and Maxwell core; independent extension enumeration would lose
the pairwise intersection budget that the target needs.

That coupling is now the exact extension-family collision ledger. Apply its
pair slack before any packing count, and use the summed multiplicity charge
instead of multiplying per-row binomial counts. The next theorem must bound
the number of coefficient-compatible support/packing records and assign each
record to its first Maxwell core; deriving the same pairwise block cap again
would not advance the frontier.
