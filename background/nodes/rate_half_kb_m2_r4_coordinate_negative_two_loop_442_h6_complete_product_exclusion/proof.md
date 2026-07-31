# Proof

Modulo `l^2-l+1`, the protected numerator and denominator of the forced
H6 product reduce to

```text
N=b(b+1)l,       H=-(b+1)l.
```

The outside compiler proves `H!=0`, hence `p_xi=N/H=-b`.  Taking the cross
product of the rows belonging to the known pairs `(-1,c)` and
`(-b^2,tau bc)` gives `(KB44F-3)`.

If the forced type is `DF`, then `DF=-b`, while the seven outside products
also contain `-DF=b`.  The common product list already contains `b`.
Therefore the complete twelve-product map is not injective, and all four
forced-`DF` cells are empty before matching.

For either colored forced type, substitute `p_xi=-b` into the universal
residual forms.  This gives `(KB44F-4)`.  The parent signed-pair theorem
removes the three matchings that pair the two unsigned entries.  Reversal of
`F` pairs the remaining twelve matchings, with representatives
`3,4,5,9,10,11`.

When `sigma=-tau`, clear denominators in the three copies of `(KB44F-3)`.
Eliminate `x` from the first equation with each of the other two and then
eliminate `a`.  Every factor has nonzero norm against `P_tau`; factoring the
integer norms gives `(KB44F-5)`.  Sharing the second equation instead gives
the same support unions independently.  The deployed characteristic avoids
all listed primes, so these four cells are empty.

It remains to consider `sigma=tau`.  For each of the twelve row/type/
representative cases, compute the lexicographic Groebner basis of
`(P_tau,E_1,E_2,E_3)` over `Q`.  The `cD` bases all reduce `a^2-b^2` to zero.
The `sigma DE` bases are unit at representatives `5,10` and reduce
`a^2-b^2` to zero at `3,4,9,11`.  These are exact identities, not modular
samples.  The F-sign partners inherit the same alternatives.

In a field of odd characteristic, `a^2=b^2` implies `a=+/-b`.  In both
colored forms, `a` denotes the colored product not fixed to `-b`; it then
collides with either the common singleton product `b` or the forced product.
The injectivity guard rules out the entire collision divisor.  As an
independent deployed-field audit, adjoining
`z(a^2-b^2)-1` makes all 24 aligned representative ideals unit; the 24
opposite-sign representative ideals are unit without saturation.

The H8 rows were deleted by the parent.  The H6 deletion therefore exhausts
all six common rows and all 36 invariant cells of the `442` router. QED.
