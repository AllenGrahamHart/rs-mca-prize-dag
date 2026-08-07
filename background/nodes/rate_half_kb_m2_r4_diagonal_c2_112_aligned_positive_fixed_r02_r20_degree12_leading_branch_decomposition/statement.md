# Fixed R02/R20 degree-12 leading-branch decomposition

- **status:** PROVED
- **scope:** the unresolved degree-12 generic resultant factor on the two
  `F04` target representatives
- **closure:** exact leading-factor census and pseudo-remainder route cut

Writing the route equations as polynomials in `x` over the `(s,p)` base:

1. `R12` has `deg_x=6` and the same irreducible nonnamed degree-6 leading
   factor on `R02` and `R20`.
2. `E2` has `deg_x=36`. Its leading coefficient is `s L22` on `R02` and
   `s L23` on `R20`, where each displayed factor is irreducible and
   nonnamed.
3. `E3` has `deg_x=35`. Its leading coefficient is a nonnamed irreducible
   `L23` on `R02` and `L24` on `R20`.

Thus division over `F_p(s,p)` inverts genuine branches and cannot by itself
prove exhaustive emptiness. On `R02`, three exact content-primitive
pseudo-remainder steps lower `x`-degree only to `35,34,34` while their term
counts grow to `40921,83811,149340`. No fixed cell is closed here.

On the two `F04-R02` large leading curves, exact seed ideals are
one-dimensional with basis sizes `25` and `27`. Reducing the two essential
rows still leaves `5783`--`6100` terms and the full intersections time out.
Branch-aware pseudo-division modulo the degree-22 curve does reach
`x`-degree five, but its two remainders have `23616` and `23484` terms and
coefficient degrees `205` and `204`; the final intersection again times out.
These are route fences, not cell closures.

## Falsifier

A leading factor with a different fingerprint, a factor classified as named,
or a pseudo-remainder prefix with different exact hashes or degree/term data.
