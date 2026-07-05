# proof: e22_minimal_scale_partition

By `e22_dyadic_minimal_scale_selector`, the admissible quotient moduli in the
dyadic domain are powers of two and hence form a finite totally ordered set.
For any support class `R`, let

```text
A(R) = {M : |B_M(R)| < M}
```

be its admissible set of quotient scales, using the canonical full-fiber/tail
recovery from `e22_cross_scale_support_canonical_form`.

If `A(R)` is nonempty, finite total ordering gives a unique minimum

```text
M_min(R) = min A(R).
```

The criterion proved in `e22_minimal_scale_tail_criterion` says exactly that
`M` is this selected minimum if and only if `|B_M(R)|<M` and every smaller
dyadic modulus fails admissibility, i.e.

```text
|B_{M'}(R)| >= M'    for all M' < M.
```

Therefore every support class with at least one admissible scale belongs to
the cell indexed by its unique `M_min(R)`. It cannot belong to two cells,
because a finite totally ordered set cannot have two distinct minima. The
tail-minimal predicates are consequently disjoint and exhaustive on the
selected canonical representatives.
