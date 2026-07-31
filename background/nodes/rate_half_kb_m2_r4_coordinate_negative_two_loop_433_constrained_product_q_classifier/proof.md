# Proof

Substitute `b=-c^3` into the five product rows `(KB43P-1)`.

For `X2`, every nontrivial maximal minor is a protected nonzero factor times

```text
F_-(c,M)=(c^2+1)(M+1)^2-c(M-1)^2.                (1)
```

For `N1` the same statement holds with

```text
F_+(c,M)=(c^2+1)(M+1)^2+c(M-1)^2.                (2)
```

Let `Q_X,Q_N` be the second squared weld after removing its protected factor
`c^2(c-1)^2`.  Exact elimination in `c` gives

```text
Res_c(F_-,Q_X)=M^2(M^2+1)^4 P_8(M)^2,
Res_c(F_+,Q_N)=16M^2 P_8(M)^2.                   (3)
```

In `X2`, `M=0` and `M^2+1=0` are label collisions; in `N1`, `M=0` is.
Thus `(3)` forces `(KB43C-1)`.  Conversely direct ideal reduction gives

```text
Q_X mod <F_-,P_8>=0,       Q_N mod <F_+,P_8>=0,
```

and all five product minors reduce to zero as well.  This proves
`(KB43C-2)--(KB43C-3)`.

For `L1`, reduce first by `M^2+1` and divide only the protected factors
`2,c,c-1,c+1`.  A lexicographic basis for the remaining product minors and
squared weld contains

```text
(c^2+c+1)^2(2c^4+3c^2+2),
3L-4c^3-2c+M.                                    (4)
```

The first factor in `(4)` gives `c^3=1`, hence `b=-1`, a forbidden equality
of the signed `A,B` pairs.  The second factor and linear basis row are
exactly `(KB43C-4)`.  Conversely all stripped minors and the squared weld
reduce to zero modulo those three equations.

The degree counts give `4*2=8`, `4*2=8`, and `2*4=8` candidates.  Direct
finite-field substitution checks the three packets `(KB43C-5)`: each has
five distinct `K` labels, three distinct signed `J` pairs, five distinct
products, product rank three, and zero squared-weld residual.

Finally, the first label identity gives one sign equation between the two
`AB` orbits.  The squared second weld gives a sign `+/-1`; reversing the
`BC` deck assignment realizes the required sign without changing any
product.  The product-to-q theorem then reconstructs all five common-`K`
Vieta rows. QED.
