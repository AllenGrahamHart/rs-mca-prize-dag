# proof: e22_dyadic_minimal_scale_selector

In a dyadic domain `n=2^m`, every quotient modulus dividing `n` is a power of
two. Hence the admissible quotient moduli form a finite totally ordered set:

```text
1, 2, 4, ..., 2^m.
```

The node `e22_cross_scale_support_canonical_form` associates to a support `R`
the canonical set

```text
A(R) = {M : M > t and |B_M(R)| < M},
```

where `B_M(R)` is recovered from `R` by deleting all full `M`-fibers contained
in `R`. This set depends only on `R`, not on a chosen staircase
representation.

If `A(R)` is nonempty, then because it is a finite subset of a total order it
has a unique smallest element:

```text
M_min(R) = min A(R).
```

The recovered tail `B_{M_min}(R)` and selected full `M_min`-fibers are already
canonical by `e22_cross_scale_support_canonical_form`. Therefore the tuple

```text
(R, M_min(R), B_{M_min}(R), selected M_min-fibers)
```

is a canonical representative of the cross-scale class. Equal supports have
the same canonical admissible-modulus set and hence the same selected
representative. Distinct supports remain distinct because the representative
includes `R`.

This proves the dyadic minimal-scale selector. It does not prove that the
staircase pricing column already counts exactly these selected
representatives; that compatibility is the target
`e22_minimal_scale_pricing_compatibility`.
