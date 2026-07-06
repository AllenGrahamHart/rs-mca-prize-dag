# proof: sov_hminus1_fiber_fourier_duality

Let `Omega` be a finite forced-root conditioned anchored-core family, and let
`c: Omega -> F` be the coefficient map `c(L)=[X^{h-1}]L`. Fix a nontrivial
additive character `psi` of the finite field `F`.

The additive-character orthogonality relation says that, for every `u in F`,

```text
1_{u=0} = |F|^{-1} sum_{xi in F} psi(xi u).
```

Apply this with `u=c(L)-a` and sum over `L in Omega`:

```text
N(a)
 = sum_{L in Omega} 1_{c(L)=a}
 = |F|^{-1} sum_{xi in F} psi(-xi a)
       sum_{L in Omega} psi(xi c(L)).
```

The `xi=0` term is exactly `|Omega|/|F|`. For each nonzero `xi`, multiplication
by `psi(-xi a)` has absolute value one, so the triangle inequality gives

```text
N(a) <= |Omega|/|F|
        + |F|^{-1} sum_{xi != 0} |S(xi)|,
```

where `S(xi)=sum_{L in Omega} psi(xi c(L))`.

This proves the fiber-duality reduction. The node
`sov_hminus1_character_sum_bound` carries the remaining mathematical work:
bounding those nontrivial sums for the actual anchored-core families strongly
enough to meet the active-core budget.
