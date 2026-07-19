# sov_hminus1_fiber_fourier_duality

- **status:** PROVED
- **closure:** proof

## Statement

Fix an official-shape row, an `h in (20,A]`, and one forced-root
higher-coefficient conditioning cell of anchored-core locators. Let

```text
c(L) = [X^{h-1}]L
```

be the `h-1` locator coefficient map from that finite conditioned family
`Omega` to the row field `F`.

For every value `a in F`,

```text
|{L in Omega : c(L)=a}|
  <= |Omega|/|F| + |F|^{-1} sum_{xi != 0} |S(xi)|,

S(xi) = sum_{L in Omega} psi(xi c(L)),
```

where `psi` is any nontrivial additive character of `F`. Hence any
project-specific bound on the nontrivial sums `S(xi)` immediately gives a
uniform fiber bound for `[X^{h-1}]L`.

## Falsifier

A finite coefficient map to a field whose fiber size exceeds the
Fourier-inversion bound above.
