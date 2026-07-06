# sov_nonconstant_affine_character_cancellation

- **status:** PROVED
- **closure:** proof

## Statement

Let `V` be a finite-dimensional affine space over the row field `F`, let
`psi` be a nontrivial additive character of `F`, and let

```text
c(v) = ell(v) + b
```

be an affine-linear map `V -> F` whose linear part `ell` is nonzero. Then, for
every `xi != 0`,

```text
sum_{v in V} psi(xi c(v)) = 0.
```

Consequently, if a forced-root conditioning cell is partitioned into
disjoint affine pieces on which `c(L)=[X^{h-1}]L` is nonconstant affine-linear,
plus an exceptional set `E`, then every nontrivial character sum over the
whole cell has absolute value at most `|E|`.

## Falsifier

A nonconstant affine-linear map over a finite field whose nontrivial additive
character sum is nonzero.
