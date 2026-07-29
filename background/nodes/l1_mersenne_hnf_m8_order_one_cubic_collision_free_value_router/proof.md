# Proof - L1 Mersenne HNF m=8 order-one cubic collision-free value router

Let `x_1,...,x_6` be the roots of the monic squarefree sextic `L`. The root
formula for the resultant gives

```text
V_E(X)=product_(i=1)^6 (X-E(x_i)).                   (1)
```

In the collision-free chamber these are six distinct members of `mu_8`.
If the two missing colors are `alpha,beta`, then

```text
V_E(X)(X-alpha)(X-beta)=X^8-1.                       (2)
```

This proves the value-resultant identity before orbit normalization.

Identify colors with exponents in `Z/8Z`. Translation preserves the
unordered circular distance

```text
delta=min(|a-b|,8-|a-b|) in {1,2,3,4}.              (3)
```

It is also complete: translate one endpoint to zero and, if necessary,
exchange the pair. Thus the representatives are exactly (CFV1). The
distance-one, -two, and -three orbits have eight pairs each, while the
antipodal distance-four orbit has four, accounting for all
`8+8+8+4=28` missing pairs.

Multiplying `E` by the inverse translation color rotates its six values and
the missing pair to the chosen representative. This scaled polynomial is
still an exact cubic with nonzero leader and satisfies (2), although it is
used only as a variable in the necessary value system rather than asserted
to be the actual rootwise norm interpolant. Hence every actual packet maps
to one of the four systems in (CFV3).

The conic and norm-color equations are inherited necessary conditions. All
resultants have fixed input degrees six and three, independently of the
official exponent. A unit ideal therefore excludes the packet, while a
retained point still owes the assignment-preserving Frobenius, full
cyclotomic, and inner conditions. QED.
