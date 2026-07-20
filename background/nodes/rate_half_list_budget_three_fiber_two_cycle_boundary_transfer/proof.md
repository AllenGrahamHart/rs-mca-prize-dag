# Proof

The cycle router supplies `(F2B1)` with a monic squarefree quartic `D_*`, four
distinct pencil parameters, `N=4s=4r+4`, and characteristic greater than `N`.
These are exactly the parameter-uniform hypotheses of the reverse-residual,
fourth-root, secondary-gap, and two-window theorems; none of their proofs uses
the special identity `D_*=product_i(Y-rho_i^2)`.

The reverse-residual formula immediately gives `(F2B3)`. For the generic
floor,

```text
v=ceil((r-4)/2)=s/2-2,
h=r-v=s/2+1.
```

Therefore `2h=s+2` and

```text
deg T=r+4-2h=(s+3)-(s+2)=1.                           (1)
```

For the intermediate floor, `s=2^38` is congruent to one modulo three, so

```text
v=ceil((2r-4)/3)=(2s-5)/3,
h=r-v=(s+2)/3.
```

Again `3h=s+2`, and `(F2B3)` gives `deg T=1`. This proves `(F2B4)`. Notice
that the old order had a quadratic intermediate residual; the rounding
changes at the doubled dyadic order.

For either boundary, `qh=s+2`. The fourth-root theorem therefore gives zeros
from index `r+1=s` through `qh-1=s+1` and a nonzero coefficient at `s+2`.
This is `(F2B5)`. On the generic boundary, substituting
`h=s/2+1` in the secondary-gap theorem gives `(F2B6)`. The identities
`N=8h-8`, `r=2h-3`, and `h-3=s/2-2` give `(F2B7)` and import the complete
two-window square identity.

If `D_*` has two antipodal root pairs, the parity proof applies to this
quartic regardless of how its roots arose in the cycle router. Since
`N=2^40=16*2^36`, substitution in its exact statement gives `(F2B8)`.

On the pure outer stratum, the pure-quartic theorem is also stated for an
arbitrary monic quartic denominator. It gives `v=r-1`, the linear Wronskian
factor, squarefreeness of both pencil directions, and the one-point overlap
cap. This proves `(F2B9)` and its accompanying claims.

It remains to audit the canonical matching. Reverse the four monic factors
and absorb the leading coefficient of `V` into centered parameters `w_i`.
The canonical-span proof is purely the expansion

```text
product_i(B+w_i z^h Cbar)
 =B^4+alpha z^(2h)B^2Cbar^2
       +beta z^(3h)BCbar^3+gamma z^(4h)Cbar^4.         (2)
```

Thus its truncation, normalized square root, span identity, uniqueness of
`alpha,beta,gamma`, and split quartic `(F2B10)` all transfer unchanged.

The cycle router supplies two constant relations whose coefficient columns
are

```text
(1,rho_i,w_i,rho_iw_i)^T.                              (3)
```

As in the Mobius-weld proof, singularity of `(3)`, together with distinctness
of both point sets, is equivalent to one fractional-linear matching
`w_i=T(rho_i)`. This proves necessity of the completion-root matching.

Conversely, factor `(F2B10)` with such a matching. The canonical span identity
reverses `(2)` and reconstructs the four pairwise-coprime factors
`G_i=U+w_iV`. The matched columns `(3)` have a one-dimensional kernel with no
zero entry, giving both cycle relations. The router's factor inventory groups
`D_*(X^2) product_i G_i(X^2)` into the exceptional factor and the four
linear completion factors, recovering `(F2C1)--(F2C5)` and hence the original
cycle locators.

When `c=0`, the denominator roots are exactly `rho_i^2`, so this is the old
square-root-lift matching. For `c=1,2`, the denominator contains exceptional-
pair squares absent from the completion-root set. Replacing `rho_i` by an
arbitrary square-root lift of those denominator roots changes the cross-ratio
condition and is not justified. This proves the stated stopping point and all
claims. QED.
