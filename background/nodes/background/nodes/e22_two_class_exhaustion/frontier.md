# frontier: e22_two_class_exhaustion

Closed by `proof.md`.

The previous frontier reduced any third-class counterexample to the
ratio-flat condition `L_Z/L_C` constant on one full petal. The proof closes
that condition algebraically: if `Z` is obtained from the core by replacing
`r` core roots with background roots, then `r <= background_size < ell`.
Constancy on an `ell`-point petal forces a degree-`r` polynomial to vanish on
`ell` distinct points, hence the replacement is empty and the codeword is
planted.

The old detached Modal run remains non-certifying evidence only; it is no
longer needed for the no-third-class part.

Remaining E22 work has moved to `e22_challenger_staircase_pricing`: exact
counting and pricing of the mixed/full-petal challenger class.
