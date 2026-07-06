# e22_tail_removed_quotient_factor_passthrough

- **status:** PROVED
- **closure:** proof

## Statement

Let `L_T` be a squarefree touched-petal locator and suppose

```text
L_T(X) | H(X).
```

Assume the root set `T` decomposes disjointly as

```text
T = B disjoint_union union_z F_z,
```

where `B` is the chosen tail and each `F_z` is a full quotient fiber for
`x -> x^M`. By `e22_fiber_locator_saturation`,

```text
L_{F_z}(X) = X^M - z.
```

Then

```text
L_T(X) = L_B(X) * prod_z (X^M-z),
```

and if `H=L_T K`, the tail-removed cofactor satisfies

```text
H(X)/L_B(X) = prod_z (X^M-z) * K(X).
```

Thus, once the E22-specific structure theorem supplies the common tail and the
full quotient fibers, the quotient factors pass through the divisor relation
formally and with multiplicity one.

## Falsifier

A squarefree locator factorization `L_T=L_B prod_z(X^M-z)` dividing `H` while
some quotient factor fails to divide the tail-removed cofactor `H/L_B`.
