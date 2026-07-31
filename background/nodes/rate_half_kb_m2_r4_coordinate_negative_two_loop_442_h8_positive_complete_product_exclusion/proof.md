# Proof

Let

```text
l^4+1=0,
b^2-2bl^3+2bl-b+1=0.                             (1)
```

The resultant of the two left sides with respect to `l` is `P_+(b)^2`.
Reduction modulo `(1)` gives the locator and forced-product identities in
`(KB44E-1)`; the denominator of the latter is protected by the outside
compiler.  Taking the cross product of the rows for the two known product
pairs `(b,c)` and `(-b^2,bc)` gives exactly `(G,A,B)` in `(KB44E-2)`.

Use the sign gauge and forced-type representatives of the invariant router.
Direct substitution of the forced value `p` gives the three residual lists
in `(KB44E-3)`.  In the first two lists, the parent signed-pair theorem
deletes indices `0,1,2`; sign reversal of `F` pairs the other twelve into
the six stated representatives.

For every remaining representative, clear denominators in the three
bilinear pair equations.  In the primary order, eliminate `x` (or `q`)
from the first equation with each of the other two, then eliminate `a`.
Every irreducible factor of the resulting polynomial in `b` has nonzero
norm against `P_+`, except that the `DF` projection itself vanishes at
indices `6,7,8`.  This exception is not a solution component: over the
deployed field the Groebner basis of `P_+` and all three original cleared
equations is `[1]` for each sign and each exceptional index.

The audit reverses the projection choice.  It shares the second pair
equation, eliminates the same intrinsic variable, and then eliminates `a`.
This gives nonzero final polynomials and nonzero deployed-field factor norms
for all 24 `cD/DE` representatives and all 30 `DF` matchings.  Hence none of
the six `H8-L,tau=+1` cells has a complete paired-product lift.

It remains to transport the other singleton placement.  Under loop exchange
and `(KB44E-4)`, division of `(1)` by `b^2` gives the same gate for `b'`, and

```text
c/b=2b'-l^3+l+1,
```

which is the `H8-M,tau=+1` locator.  The swapped common product vector,
divided by `b^2`, is

```text
(-1,-b'^2,b',c',b'c').
```

Every outside product in
`{cD,cE,sigma DE,DF,-DF,EF,-EF}` is likewise divided by `b^2`.  Exact
reduction of the protected `H8-M` forced fraction at `b'` gives `p/b^2`.
Thus sign, forced type, distinctness, and all bilinear pair equations are
preserved.  The map is involutive, so an `H8-M` completion would yield an
excluded `H8-L` completion.  Deleting the two six-cell rows gives the stated
frontier counts. QED.
