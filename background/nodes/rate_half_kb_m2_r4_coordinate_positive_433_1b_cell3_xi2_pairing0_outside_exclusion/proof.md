# Proof

Fix a source-sign pair.  By `(KBP1B3-QUOT-1)`, common-curve functions are
represented in the six-element basis

```text
1, t, t^2, b, bt, bt^2
```

over `F_p(r)`.  Evaluate the proved common kernel at the missing label
`-t^2` and write its ratio as `m`.  Since outside record `xi=2` is `-de`, the
target product is

```text
de=-m.
```

Deleting the third `DE` record leaves the first residual pair `(de,de)` under
canonical matching zero.  Its paired Vieta determinant `T` is a necessary
target-free equation.

As in `(KBP1B3-XI0P0-1)`, multiplication by `T` gives a `6 x 6` matrix over
`F_p(r)`.  Its determinant agrees exactly, by cross multiplication, with the
independent norm obtained by taking the quadratic determinant first and the
cubic norm second.  Every target solution therefore has `r` among the roots
of the norm numerator.  Gcd with `r^p-r` gives all eight base-field roots:
five route boundaries and three live norm roots.

The root-replay compiler lifts every root through the cubic base equation,
quadratic `b` equation, and linear `c` recovery.  It then applies all route
guards and all six product cofactors before evaluating `T`.  Four guarded
common points remain, exactly two with `T=0`.  No target can occur away from
those two points.

For each retained point and target lane, put `d=u/f` and `e=v/f`.  The final
solver uses

```text
de*f^2-u*v = 0,
paired(de,de) = 0,
paired(u,sigma_o*v) = 0,
paired(b*f,sigma_c*c*f) = 0,
f^2*(-t^2)*(beta_0+beta_1*(-t^2))^2-(u-v)^2*a_missing^2 = 0.
```

The last sign is forced by the missing squared-sum row `(d-e)^2`.  Four of
the eight point/lane fibers have no base-field root of the colored quartic.
Each of the other four has two nonzero `f` roots.  After substituting
`v=de*f^2/u`, the two remaining equations become univariate in `u`; their gcd
has degree zero at every one of the eight `f` roots.  Hence no target tuple
exists.  Repeating the exact calculation for all four source-sign pairs
excludes all sixteen raw cases. QED.
