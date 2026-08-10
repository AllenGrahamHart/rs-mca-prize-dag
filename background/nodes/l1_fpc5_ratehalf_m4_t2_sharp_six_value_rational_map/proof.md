# Proof: sharp six-value rational-map descriptor

The sharp arithmetic gives `5ell=k+4`, `n=2k`, `|C|=k-1`, and
`|B|=ell-3`. Hence `n=10ell-8`, and the disjoint core, background, and four
petals have the total size in `(SV6)`.

The guarded cofactor identities give `(SV1)`. We first show
`gcd(U_1,U_2)=1`. A common root outside `P_1 union P_2` would be a common
root of `A_1,A_2`, contradicting the exact primitive condition
`gcd(A_1,A_2)=1`. A common root on `P_1` or `P_2` would also be a root of
`U_1-U_2`, hence of `F`; this is impossible because `F` splits on the
disjoint core `C`. Thus `(SV2)` is in lowest terms. Since `U_1-U_2` has
degree exactly `deg F=2ell-3`, at least one `U_i` has that degree, so
`deg phi=2ell-3`.

The roots of `L_1` and `L_2` give the first two containments in `(SV3)`.
Moreover

```text
phi=1  iff  U_1-U_2=0  iff  F=0.
```

The denominator does not vanish at a root of `F`, because that would give a
common root of `U_1,U_2`. The monic locator `F` is squarefree, has degree
`2ell-3`, and splits on `C`; therefore this is the complete reduced
`1`-fiber.

Similarly, `W=0` is equivalent to `phi=c_1/c_2`. Every background point is
a root of `W` at the sharp endpoint, and the denominator is nonzero there:
from `W-c_2F=U_2` and the disjointness of `B` and `Z(F)`, it equals
`-c_2F`, which is nonzero. This proves the background assertion.

For `u=3,4`, direct substitution gives

```text
W-c_uF=((c_2-c_u)U_1+(c_u-c_1)U_2)/(c_2-c_1).
```

Because the source labels are distinct, its vanishing is equivalent to
`phi=alpha_u`. Exact nonagreement on the untouched petals proves `(SV4)`.
The fractional-linear map `z -> (c_1-z)/(c_2-z)` is injective away from
`c_2`; distinct nonzero labels show that the two `alpha_u` are distinct
from one another and from `0,1,c_1/c_2,infinity`, proving `(SV5)`.

Finally, a reduced rational function `phi` determines the coprime pair
`(U_1,U_2)` up to one common scalar. The condition that
`F=(U_1-U_2)/(c_2-c_1)` is monic fixes that scalar, after which `(SV1)`
recovers `(F,W)`. Exact contributor reconstruction is already injective in
the sharp projective-flat descriptor. Hence the displayed map descriptor is
injective. QED.
