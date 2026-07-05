# proof: e22_minimal_scale_tail_criterion

The proved node `e22_cross_scale_support_canonical_form` says that for every
dyadic quotient modulus `M`, the support `R` has a candidate tail-plus-full-
fibers representation at scale `M` exactly when

```text
|B_M(R)| < M,
```

where `B_M(R)` is recovered canonically from `R`.

The proved node `e22_dyadic_minimal_scale_selector` then selects the smallest
admissible dyadic modulus in this candidate set. Because the dyadic moduli are
the finite chain

```text
1, 2, 4, ..., n,
```

being the selected minimal scale is equivalent to two conditions:

1. `M` itself is admissible, i.e. `|B_M(R)| < M`; and
2. no smaller admissible dyadic modulus is a candidate, i.e. for every
   smaller admissible `M' < M`, `|B_{M'}(R)| >= M'`.

Both directions are immediate from the definition of the minimum in a finite
ordered set. This proves the tail-minimality criterion.
