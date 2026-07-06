# e22_cross_scale_support_canonical_form

- **status:** PROVED
- **closure:** proof

## Statement

For any E22 staircase support `R`, the set of quotient moduli `M>t` for which
`R` has a tail-plus-full-`M`-fibers representation is recovered canonically
from `R`.

For each divisor `M` of the domain size, let

```text
F_M(R) = union of all M-fibers fully contained in R
B_M(R) = R \ F_M(R).
```

Then `R` has a candidate tail-plus-full-fibers representation at scale `M`
exactly when `|B_M(R)| < M`. In that case `B_M(R)` is the recovered tail and
the full fibers in `F_M(R)` are the selected quotient fibers. This
canonicalization may include tail-only candidate scales; downstream
nondegeneracy and pricing multiplicity are handled by
`e22_cross_scale_pricing_multiplicity`.

Therefore equal-support cross-scale representations have the same canonical
support-scale data.

## Falsifier

A support `R` with a staircase representation at `M` that is not recovered by
the full-fiber/tail rule, or equal supports with different canonical scale
data.
