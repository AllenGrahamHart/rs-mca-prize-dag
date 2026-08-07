# Proof

Let the complementary triple have elementary symmetric functions
`e_1(T),e_2(T),e_3(T)`. The first moment gives `e_1(T)=-u`, while the third
moment is equivalent to the vanishing of the global third elementary
symmetric function. Splitting that function across `Q union T` gives

```text
0=B-uA+u e_2(T)+d.
```

Hence `u e_2(T)=W`. Multiplying all three complementary roots by `u`
proves `(QCR2)`.

For three values `s_1,s_2,s_3`, let `sigma_m=sum_i s_i^m`,
`theta_m=sum_(i<j)(s_i s_j)^m`, and `pi_m=(s_1s_2s_3)^m`. Expanding the
squares gives `(QCR3)`. Put `a_i=(s_i/u)^1024`. Since `d^1024=1`, equations
`(QCR4)` say

```text
e_1(a_1,a_2,a_3)=3,
e_2(a_1,a_2,a_3)=3,
e_3(a_1,a_2,a_3)=1.
```

Their locator is `(T-1)^3`, so all `a_i=1`. The converse is immediate.
This proves the exact cubic router in every characteristic greater than
three with `u!=0`.

If `u=0` at an actual official relation, the complementary triple is a
reduced signed weight-three zero sum at an order-1024 root. The dependency
excludes this. If `F=G=0` identically in characteristic zero, the preceding
argument reconstructs seven 1024th roots with zero sum. A nonnegative
vanishing sum of roots of two-power order has even total multiplicity:
reducing its exponent polynomial modulo `X^512+1` pairs every coefficient
with its antipode. Total multiplicity seven is impossible. Thus the two
obstruction elements are not simultaneously zero in the cyclotomic field.

For the prime filter, an official prime splits `Phi_1024` completely and
without repetition. A supporting embedding is therefore exactly a common
linear factor of `Phi_1024,F,G` at which `u` is nonzero. The roots of `H_p`
are all common embeddings, and division by `gcd(H_p,u)` deletes exactly the
ones at which `u` vanishes. This proves `(QCR6)`. In particular, integer
saturation by `U` is sound only after every shared rational prime has passed
this embedding-aware test.

It remains to count presentation orbits. Fix an odd multiplier `a`. For an
affine element `(a,r)`, the fixed-`c` equation is

```text
(a-1)c=-3r mod 1024.
```

Writing `g=gcd(a-1,1024)`, this has `g` solutions exactly when `g|r`.
Those `1024/g` admissible translations are conjugate to multiplication by
`a`, because `r` lies in the image of `1-a`. Thus the sum over `(r,c)` of
the fixed presentation count is `1024 N_4(a)`, where `N_4(a)` is the number
of legal four-subsets invariant under multiplication by `a`. Burnside gives

```text
|W_4/AGL|=(1/512) sum_(a odd) N_4(a).                  (QCR9)
```

Cycles of multiplication by `a` are paired by the antipodal involution.
An invariant legal set chooses at most one cycle from each clean pair. The
coefficient of `z^4` in

```text
product_(clean cycle pairs C) (1+2z^|C|)               (QCR10)
```

is exactly `N_4(a)`. Evaluating `(QCR9)--(QCR10)` gives `94,652,815`.
The primary verifier performs this generating-function computation; the
independent audit uses the closed cycle-type formula and a direct full
affine-orbit census at order 16. QED.
