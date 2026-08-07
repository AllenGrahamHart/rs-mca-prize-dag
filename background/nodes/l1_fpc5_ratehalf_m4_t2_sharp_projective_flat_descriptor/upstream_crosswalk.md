# Upstream crosswalk

This node is a concrete LIST/FPC5 instance of the split-locator object called
`D_j(D)` in `experimental/m1.tex` and of the master-flatness target in
`experimental/cap25_v13_missing_inputs_strategy.md`.

The emitted parameters are

```text
root domain D=C,       |C|=5ell-5,
locator degree j=2ell-3,
projective dimension r=ell-2,
affine codimension s=ell-1.
```

The common-GCD reduction agrees with upstream `lem:gcd`. The companion sharp
gcd-triviality theorem proves that the actual FPC5 flat has no nontrivial
common factor, so this branch enters the primitive growing-dimensional
regime directly. Its additional structure is the guarded cofactor congruence
together with primitive and untouched-petal inequalities. A future
master-flatness or compression result can consume the descriptor directly;
until such a count is proved, this is a portable reduction rather than a
closure claim.
