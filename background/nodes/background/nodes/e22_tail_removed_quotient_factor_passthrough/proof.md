# proof: e22_tail_removed_quotient_factor_passthrough

Because `T` is a disjoint union of the tail `B` and the quotient fibers
`F_z`, its squarefree locator factors as the product of the locators of those
disjoint pieces:

```text
L_T(X) = L_B(X) * prod_z L_{F_z}(X).
```

The proved node `e22_fiber_locator_saturation` identifies each full fiber
locator as

```text
L_{F_z}(X) = X^M-z.
```

Therefore

```text
L_T(X) = L_B(X) * prod_z (X^M-z).
```

If `L_T | H`, write `H=L_T K`. Substituting the factorization gives

```text
H(X) = L_B(X) * prod_z (X^M-z) * K(X).
```

Dividing by the tail locator `L_B` leaves

```text
H(X)/L_B(X) = prod_z (X^M-z) * K(X).
```

Since the locator is squarefree and the quotient values `z` are distinct, the
fiber factors are pairwise coprime and occur with multiplicity one. Hence each
declared quotient factor divides the tail-removed cofactor exactly as claimed.
