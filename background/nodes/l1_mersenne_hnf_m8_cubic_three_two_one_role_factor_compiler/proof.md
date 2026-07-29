# Proof - L1 Mersenne HNF m=8 cubic three-two-one role-factor compiler

For an ordered distinct-color triple, affine normalization gives
`(0,1,lambda)`. Equations (1) in the affine-color proof show that its
invariant is

```text
T=-27Q^2/P^3=B(lambda)^2/A(lambda)^3.               (1)
```

The polynomial `Theta_8(T)` in (TAC5) vanishes exactly on the seven
characteristic-zero affine color shapes, counted in four rational Galois
packets. Homogenizing its four factors under (1) gives precisely the four
polynomials in (RFC2). Therefore every root of `Lambda_321` is a root of
`Omega_321`.

Conversely, `A` and `B` have no common root. Indeed

```text
4A^3-B^2=27lambda^2(lambda-1)^2.                    (2)
```

Thus a root of one `Omega_i` has a defined invariant `T=B^2/A^3`, and that
invariant is a root of `Theta_8`. It reconstructs one of the seven affine
classes of three distinct eighth roots. Its six ordered affine
normalizations give exactly the role ratios (RPC4), with the usual
multiplicity when an isosceles class has a smaller set of distinct ratios.
Hence every root of `Omega_321` is a role root.

The four degrees in (RFC2) sum to 42, equal to `deg Lambda_321`. The two
polynomials have the same root multiset over characteristic zero and are
therefore nonzero scalar multiples. Their primitive integral models remain
the safe equations after reduction to an official characteristic; factors
may merge but no ordered color role is lost. This proves (RFC3)--(RFC4).
QED.
