# Proof - L1 fixed-source anchored triple-polarity closure

## 1. Count anchored partitions

By `l1_fixed_source_quotient_partition_anchor_census`, one whole fixed-source
petal determines a monic degree-`ell` quotient partition up to additive
shift. Least-petal ownership therefore leaves at most `M_src` partition
classes. Fix one of them for the next three steps.

## 2. Encode canonical source charts

Orient each complete fiber `T_j` according to whether the source core
occupies more than half of it, with ties sparse. Let `C_0` be the union of
the densely oriented complete fibers. Then

```text
E_C=C symmetric_difference C_0
```

contains the sparse selected points, the holes in dense fibers, and every
core point in the residual set `R`. Hence

```text
|E_C|=p_layout.
```

The orientation vector and `E_C` reconstruct `C`, including its residual
points. Thus cores with `p_layout<=R_0` number at most

```text
2^L (R_0+1)n^R_0.                                    (1)
```

For a fixed core, choose any complete fibers disjoint from it as source
petals, costing at most `2^L`. For fixed received word `U`, core `C`, and
petal `T`, there is at most one degree-below-`k` source member agreeing with
`U` on `C union T`: two candidates would differ on at least
`k-1+ell>=k` roots. Therefore source members and their labels add no
multiplicity. A nonunique central-polynomial parametrization represents the
same canonical chart and is not counted again.

## 3. Encode supports and defects

Orient each selected source-petal support as dense or sparse. Relative to
the full/empty baseline, its total symmetric difference is `p_petal`.
Across all selected petals, the number of exact support patterns with
`p_petal<=P_0` is at most

```text
2^L(P_0+1)n^P_0.                                     (2)
```

For each complete fiber, use the actual core slice `C intersect T_j` as the
defect block and orient its exact defect as dense or sparse, again with ties
sparse. Use the empty baseline on `C intersect R`. The defect orientation
vector and its symmetric-difference set reconstruct `D`; the latter has size
exactly `p_defect`. Hence defects with `p_defect<=B_0` number at most

```text
2^L(B_0+1)n^B_0.                                     (3)
```

The explicit residual terms in `(AT3)` make (1) and (3) valid even when the
complete fibers do not cover the domain.

## 4. Count numerators in every strip

Fix the canonical chart, exact support, marks, and defect locator. In the
strict Forney window, `l1_marked_common_pencil_crt_fiber_bound` gives at most
`q^(2p_petal)` numerators. On the complementary thin edge,
`l1_marked_common_pencil_next_strip_boundary_fiber_bound` gives at most
`q^p_petal` because `ell>2P_0`. Thus `q^(2P_0)` is valid throughout every
strip. Each numerator reconstructs at most one contributor.

Multiplying the partition count, (1), the source-petal choice `2^L`, (2),
(3), and the numerator bound proves `(AT5)`.

Finally the maximal fixed source and `(AT1)` give

```text
M_src<=n/ell<=log_2 n/c_0,       L<=log_2 n/c_0,
16^L<=n^(4/c_0),       q^(2P_0)<=n^(2 gamma P_0).
```

Substitution proves `(AT6)`.
