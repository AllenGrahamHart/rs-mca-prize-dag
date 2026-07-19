# proof: e22_lower_scale_intersection_formula_payload

Fix a dyadic domain and dyadic scales `M_i<M_j`. For any support `R` and
scale `M`, let

```text
F_M(R) = union of all M-fibers fully contained in R,
B_M(R) = R \ F_M(R).
```

By `e22_cross_scale_support_canonical_form`, admissibility at scale `M` is
exactly `|B_M(R)|<M`, and the recovered tail is canonical from `R`.

Let `S` be any subset of the dyadic scales below `M_i`, and set

```text
C = {M_i, M_j} union S.
```

We define a finite dyadic-tree polynomial for this constrained set. Inside one
dyadic block of size `L`, the variable `X` records the number of selected
support points in that block. For every `M in C`, the variable `Y_M` records
the contribution to the recovered scale-`M` tail.

For a point block,

```text
P_1 = 1 + X.
```

For a dyadic block of size `L>1`, combine the two child blocks and then, if
`L` is one of the constrained scales, record the scale-`L` tail contribution:

```text
P_L = tau_L(P_{L/2}^2),

tau_L(X^s m) =
    X^s Y_L^s m       if L in C and s < L,
    X^s m             otherwise.
```

This is a finite coefficient formula because the recursion stops after
`log_2 n` levels and all exponents are bounded by the block size.

The atoms of the formula are dyadic occupancy trees: at each leaf, the point
is either outside or inside the support. The map from an atom to its selected
leaves is a bijection from formula atoms to supports `R`.

We prove by induction on `L` that, for every atom in a size-`L` block:

1. the exponent of `X` is the support size inside that block; and
2. for each constrained scale `M<=L`, the accumulated exponent of `Y_M` is
   the total size of the support lying in non-full `M`-blocks inside the
   size-`L` block.

The base `L=1` is immediate. For the induction step, multiplication of the
two child polynomials adds the child support sizes and all already-recorded
smaller-scale tail contributions. If `L` is not constrained, no scale-`L`
tail counter is needed. If `L` is constrained, a size-`L` block contributes
nothing to `B_L(R)` when it is full and contributes all of its support points
when it is not full. This is exactly the operator `tau_L`. Thus the induction
proves that the `Y_M` exponent in the top polynomial is `|B_M(R)|` for every
`M in C`.

Consequently the coefficient slice

```text
|B_{M_i}(R)| < M_i,
|B_{M_j}(R)| < M_j,
|B_M(R)| < M  for every M in S
```

is exactly the set of residual-profile supports that are admissible at
`M_i`, raw-admissible at `M_j`, and admissible at all scales in `S`. The
equivalence with the raw `M_j` residual universe is the same canonical
scale-`M_i` data counted by `e22_residual_profile_generating_function`.

Finally attach to each atom the multiplicity weight assigned to its canonical
support class by `dyadic_profile_evaluation`. Since the atom-support map is a
bijection and the weight is copied from that proved multiplicity convention,
the weighted coefficient sum agrees term-by-term with the required weighted
intersection count. The construction works for arbitrary `S`, so every
lower-scale admissibility intersection is covered.
