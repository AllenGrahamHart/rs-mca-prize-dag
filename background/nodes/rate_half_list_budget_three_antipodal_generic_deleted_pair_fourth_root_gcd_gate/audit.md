# Audit

The derivative in `(FGG3)` is with respect to the polynomial coordinate `x`,
not the source trace `chi` used by the preceding router.

The gate uses the full polynomial identity `R=AS+T`. A prefix Euclidean
quotient or a sampled fourth-power check does not imply the divisibility in
`(FGG5)`.

No hidden coprimality hypothesis is used. From `W^2|R` one always has
`W|R'`, including when `W` has repeated roots or shares a factor with
`xD_0`.

The useful implementation form is not to square a degree-`6M-1` polynomial
densely. Compute `P mod S`, square that residue modulo `S`, and require zero;
also certify the exact gcd degree. This remains an official-degree operation
until a separate recurrence or displacement representation is proved.

Passing the gcd gate is only necessary. It does not reconstruct `W` or prove
that `T` is a fourth power.
