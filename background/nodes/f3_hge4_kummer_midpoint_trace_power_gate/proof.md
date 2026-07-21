# Proof

Write

```text
s=[y^h]S=(u+v)/2,       a=(v-u)/2,
w=[y^c]W,               z=[y^e]Z.                 (1)
```

The outside factors are reciprocals of monic split divisors `P,Q` of
`X^m-1`. Their leading reciprocal coefficients are `P(0),Q(0)`, so
`u,v in mu_m`; here `-1 in mu_m` absorbs the signs of the root products.
The pair is nonconstant, so `u!=v`. The Belyi theorem proves `deg S=h`, so
`s!=0` and therefore `u!=-v`. Thus `x=v/u` belongs to
`mu_m\{1,-1}`.

Compare endpoint coefficients in the two proved complement identities. From

```text
UVW=1-y^m
```

one gets

```text
uvw=-1.                                             (2)
```

The separator identity at zero gives

```text
G(0)=(u+v)/(uv),       d=v-u=2a.                  (3)
```

The leading coefficient in the Belyi polynomial is

```text
z=-3G(0)/d^2=-3(u+v)/(uv(v-u)^2).                 (4)
```

Finally `W=ZS+lambda y^c` gives

```text
lambda=w-zs.                                       (5)
```

Substitute `(1)--(5)` into `kappa=1-a^2lambda`. Since
`uv=s^2-a^2`, exact cancellation gives

```text
kappa=-s^2/(2uv)
     =-(u+v)^2/(8uv)
     =-(1+x)^2/(8x).                               (6)
```

This proves `(KTP1)`. The exclusions on `x` make the displayed scalar
nonzero.

The primitive Kummer theorem supplies a base-field element `alpha` with

```text
alpha^m=kappa^(-1).
```

Therefore `kappa=(alpha^(-1))^m` is an `m`-th power. Because `m|(p-1)`, an
element of `F_p^*` is an `m`-th power exactly when its `(p-1)/m` power is one.
This proves `(KTP2)`.

For `tau=x+x^(-1)`, induction in the displayed recursion gives

```text
C_j(tau)=x^j+x^(-j).
```

Since `x^m=1`, this is `(KTP3)`. If
`x+x^(-1)=y+y^(-1)`, then

```text
(x-y)(xy-1)=0.
```

Thus each trace comes from exactly the inverse pair `{x,x^(-1)}` away from
`x=+/-1`. The `m-2` allowed elements of `mu_m` give exactly `(m-2)/2`
traces. Swapping `U,V` replaces `x` by its inverse and leaves `(6)` unchanged.

Finally `m>=8` is dyadic and `m|(p-1)`, so `p=1 (mod 8)`. Both `-1` and `2`
are squares in `F_p`, and hence so is `-1/8`. Taking quadratic characters in
`(KTP1)` gives

```text
chi(kappa)=chi(x).
```

The `m`-th power `kappa` is a square because `m` is even. Therefore `x` is a
square. Write `q=(p-1)/m` and fix a generator `g` of `F_p^*`. The elements of
`mu_m` are `g^(qj)`. If `q` is odd, such an element is a square exactly when
`j` is even, which is exactly `mu_(m/2)`. Excluding `+/-1` and pairing under
inversion leaves `(m/2-2)/2=m/4-1` traces. If `m<n`, the dyadic factor `n/m`
divides `q`, so `q` is even. This proves `(KTP4)`. QED.
