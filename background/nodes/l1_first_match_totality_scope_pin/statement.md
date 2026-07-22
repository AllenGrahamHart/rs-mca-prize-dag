# L1 first-match totality scope pin

- **status:** PROVED
- **role:** separate chart coverage from chart payment
- **consumer:** `l1_mixed_petal_amplification`
- **upstream source:** `przchojecki/rs-mca@18cfc199`,
  `experimental/lean/asymptotic_spine/AsymptoticSpine/PrefixAtlas.lean`

## Statement

Let `I` be any finite set of distinct image-fiber contributors. For each
`x in I`, let `A_x` be a nonempty finite set of chart keys carrying
`x`, and fix a total order on all keys. Define

```text
owner(x)=min A_x,
C_chi={x in I:owner(x)=chi}.                              (FT1)
```

Then the nonempty owner cells form a disjoint partition:

```text
I=disjoint_union_chi C_chi,
|I|=sum_chi |C_chi|.                                     (FT2)
```

Consequently, if `U_chi` is a valid upper bound for the image contributors
first-owned by `chi`, then

```text
|I|<=sum_chi U_chi.                                      (FT3)
```

The same conclusion holds when each contributor has one total key
`Phi(x)`: the fibers `Phi^(-1)(z)` are automatically exhaustive. This is the
finite set-theoretic content of upstream's kernel-checked
`prefixFibreAtlas_total` theorem.

## L1 consequence

The non-intrinsic L1 residual is not a missing-atlas or set-cover problem.
Every contributor already carried by at least one chart can be assigned
canonically to its first chart without duplication. For a generic chart
family, the remaining obligation is a **payment theorem** proving that the
complete sum of owner-cell bounds in `(FT3)` is polynomial. Neither
first-match totality nor disjointness bounds the number of realized chart keys
or the sum of their budgets.

For maximal sunflower source layouts, the later theorem
`l1_general_first_layout_domination` is stronger than this generic partition:
all listed non-anchors are carried by the first layout, and all possible later
source-layout mass lies among its `M` anchors. Thus the source-layout sum is
retired. The remaining use of `(FT3)` is for contributor-dependent internal
quotient/Forney recharts inside that fixed first source, where universal
non-planted carriage has not been proved.

## Scope

This theorem supplies no per-cell estimate, no polynomial chart count, no
split-pencil stability, and no bound on the growing-polarity or balanced
sub-Johnson branches. It does not promote the L1 consumer.
