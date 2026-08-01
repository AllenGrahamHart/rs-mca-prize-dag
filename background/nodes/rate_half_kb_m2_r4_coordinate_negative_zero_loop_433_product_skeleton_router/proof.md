# Proof

Substitution of `(KBZ433P-1)` into

```text
Gamma yz-Alpha(y+z)-Beta=0
```

gives `(KBZ433P-2)`; direct evaluation on all four common `(b,c)` rows shows
`Alpha=0`, `Gamma!=0`, and nonzero involution determinant.

Let `N=p^6-1`, `M=N/(p-1)`, and choose a generator `g` of
`F_(p^6)^*` whose `M`-th power is the primitive base-field generator `3`.
Such a choice exists in the cyclic extension group: start with any
generator and modify its exponent within its residue class modulo `p-1` to
avoid every additional prime divisor of `M`.
Every signed outside product is a monomial in `D,E,F` with coefficient in
`F_p`.  After taking discrete logarithms, a forced-mate choice and a perfect
matching of the six residual products become four linear congruences

```text
A (log_g D,log_g E,log_g F)^T = v mod N,           (KBZ433P-4)
```

where the base-field logarithms in `v` are multiplied by `M`.  Smith normal
form of each `4 x 3` integer matrix `A` decides compatibility and enumerates
every isolated solution.  Replaying `(KBZ433P-4)` checks every enumerated
triple.  Comparing doubled target logs and all twelve product logs gives the
two injectivity guards and the census `(KBZ433P-3)`.

The 16 compatible positive-dimensional `Z2` systems per common `(b,c)` row
have rank two.  For each one, direct polynomial reduction of all
target-square and product
differences by its binomial ideal exhibits a forced collision.  Thus no
unexamined free parameter can restore the guard.  `Z3` has no family, and
its 864 isolated solutions all fail a guard.  This proves the two
exclusions.

For `Z0,Z1,Z4`, exact exponent triples replay the four congruences and both
guards.  They prove only survival of this necessary product gate.  Common
root signs do not change `(b,c)`, and target sign/exchange transports the
result through `[2,5,6,9]`. QED.
