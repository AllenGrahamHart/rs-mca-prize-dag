# Proof

Scale the singular cubic by `r=cR`, `u=cU`, using `c^3=1`. It becomes

```text
R^2U+RU^2-3RU+1=0                                   (1)
```

with node `(1,1)`. Intersect `(1)` with the line
`U-1=theta(R-1)`. After removing the double node factor, the third
intersection gives

```text
R=-1/[theta(1+theta)],       U=-theta^2/(1+theta).
```

The product-one completion is `V=(RU)^(-1)=(1+theta)^2/theta`, proving
`(NTP1)`. The excluded parameters `0,-1,infinity` give points at infinity.
Parameters with `theta^2+theta+1=0` map back to the node along its two tangent
directions. Every affine nonnode point determines its remaining line through
the node uniquely.

Let `A=[theta]`, `B=[1+theta]`, and `C=[c]` in `Q`. Since `-1 in H`, the
first two roots in `(NTP1)` lie in `H` precisely when

```text
C A^(-1)B^(-1)=1,       C A^2B^(-1)=1.              (2)
```

Equations `(2)` are equivalent to `A^3=1` and `B=CA^2`. The third root then
has class `CB^2A^(-1)=C^3A^3=1`. This proves `(NTP2)` in both directions.

The cyclic quotient `Q` has at most three elements of order dividing three.
For each allowed `A`, condition `(NTP2)` asks that the two nonproportional
affine forms `theta` and `1+theta` lie in two fixed `H`-cosets. The optimized
one-fiber affine Stepanov theorem bounds that branch by `4n^(2/3)`. Hence the
nonnode part has fewer than `12n^(2/3)` points. The node `(c,c)` belongs to
`H^2` only when `c in H`; because `gcd(3,n)=1`, this forces `c=1`. Adding it
proves `(NTP3)`.

For a second parameter `phi`, substitute the first coordinates

```text
R=-1/[theta(1+theta)],       S=-1/[phi(1+phi)]
```

into the normalized target `t=1+RS(R+S-3)`. Clearing and factoring the
denominator gives `(NTP4)`. The scale `c` disappears because the target term
has total degree three.

There are at most three singular values of `sigma`. For a fixed one, every
raw DSP8 record chooses an ordered pair of points on its trace curve, so
there are at most `N_sigma^2` point pairs before imposing any favorable
predicate. For every retained target, the quotient multiplicity satisfies

```text
R(t)+1=#{z in H:1+t(z-1) in H}<4n^(2/3),             (3)
```

by the same optimized affine theorem; `t notin {0,1}` makes the two forms
nonconstant and nonproportional. Multiplying the three point-pair ceilings
from `(NTP3)` by `(3)` gives

```text
G_sing^0+G_sing^A
 <3(12n^(2/3)+1)^2 4n^(2/3),
```

which is `(NTP5)`. Applying the larger class coefficient `17` gives `(NTP6)`.
Its leading term is `17*12*144n^2=29376n^2`; comparison with `892n^2`
proves the stated constants barrier. QED.
