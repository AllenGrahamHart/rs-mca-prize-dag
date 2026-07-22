# Proof

Choose any row generator `G` for the evaluation code of `U_q` on the `2e`
roots of `A`. The non-MDS side of the complementary-minor router supplies an
`e`-set `I` and its complement `J` such that

```text
det G_I=det G_J=0.                                   (1)
```

The first singular matrix in `(1)` has a nonzero left-kernel vector. Its
linear combination of the rows of `G` is the evaluation vector of a nonzero
`u in U_q` that vanishes on `I`. The full evaluation map on `U_q` is
injective, so `u` is nonzero in `R_A`. The second singular matrix similarly
produces nonzero `v in U_q` vanishing on `J`.

At every exceptional root, either the root lies in `I` and `u` vanishes, or
it lies in `J` and `v` vanishes. Hence the evaluation of `uv` is zero at all
roots of `A`. Since `A` is squarefree, evaluation identifies `R_A` with the
product of its root fields, so

```text
uv=0 in R_A.                                         (2)
```

The roots in `I` all divide `D_u`, and the roots in `J` all divide `D_v`, so
both gcds have degree at least `e`. Their root sets together contain every
root of squarefree `A`, proving `lcm(D_u,D_v)=A`. If either degree exceeds
`e`, the excess-zero clause holds. Otherwise both root sets have size `e`;
their union has size `2e`, so they are disjoint and their monic locators
multiply to `A`. This proves `(HNA3)--(HNA4)`.

At every exceptional root `a`, write the two elements in the normalized
coefficient basis. Then

```text
u(a)=H_lambda(a)/q_1(a),       v(a)=H_nu(a)/q_1(a).
```

The denominator never vanishes, so each numerator has exactly the same
exceptional zero set as its normalized class. This proves `(HNA5)` and
removes quotient inversion from the certificate.

For `(HNA6)`, puncture `U_q` to `I`. The weighted orthogonal complement of
that puncturing is the shortening of the weighted dual code to `I`. Since
`U_q` is weighted self-dual, this shortening is precisely the restriction
of `U_J` to `I`. Hence

```text
e-r_I=dim U_J=e-r_J,
```

so `r_I=r_J`; write the common deficiency as `d`. The two shortening spaces
have disjoint supports and zero intersection, so their direct sum lies in
the `e`-dimensional space `U_q`. Therefore `2d<=e`. Every cross product
between them vanishes coordinatewise, proving `(HNA7)`.

The elements `u` and `v` cannot be scalar multiples. Otherwise `(2)` gives
`u^2=0`; the reduced algebra `R_A` has no nonzero nilpotents. This proves
linear independence and `(HNA1)--(HNA2)`. QED.
