# Proof - L1 Mersenne next-to-maximal Belyi shifted-value gate

Put `lambda=m alpha/q` and `Q(Y)=(Y-r_0)(Y-z)`. In the preceding reduction,
`T` has leading coefficient `2a`, its nonzero-root factor and possible zero
factor are exactly those removed from `G-lambda Y`, and the remaining monic
quadratic is `Q`. Hence

```text
G-lambda Y=Q T/(2a).                                  (1)
```

Cancelling `T(R)` in the Euler identity gives

```text
XDR'=(q/(2a))Q(R).                                    (2)
```

## 1. Shifted split values lie in the domain subgroup

Every root of `R-z`, counted with multiplicity, lies in the domain coset,
because its radical is a factor of `D`. The same is true for every complete
split fiber `R-beta_i`. For a monic degree-`p` polynomial, the products of
the roots of these two fibers are respectively

```text
z-r_0,       beta_i-r_0.
```

Both products lie in the same coset of `mu_n`, so their ratio `x_i` lies in
`mu_n`. The `beta_i` are distinct, and `P` is their monic normalized root
polynomial. This proves `(BSG2)`.

At a nonzero root `beta_i` of `G`, equation (1) gives

```text
Q(beta_i)G'(beta_i)=2a lambda.
```

Writing `beta_i=r_0+(z-r_0)x_i` turns this into `(BSG2a)`. If
`ord_0(T)=0`, every root of `G` is nonzero, so the degree-`h` polynomial `P`
divides the degree-`h+1` polynomial on the left of `(BSG2b)`. Their leading
terms make the quotient linear with leading coefficient `h`, proving
`(BSG2b)`. If `ord_0(T)=1`, zero is the unique removed split value and its
normalized coordinate is `-1/(c-1)`; all remaining roots give the stated
degree-`h-1` divisibility.

## 2. The zero quadratic root is impossible

Suppose `z=0`. The chamber `ord_0(T)=0` has `G(0)!=0`, so zero cannot be a
root of the quadratic quotient. Hence `ord_0(T)=1`, and zero is a simple root
of the squarefree split-value polynomial `G`. The complete fiber `R=0` has
`p` simple nonzero domain roots, and `D` is a unit at each one.

The factorization (1) now has one zero factor from `T` and one from
`Q`, so `qG-m alpha Y` has order two at `Y=0`. At a root of `R=0`, the left
side of the Euler identity `D T(R)XR'` has order one, while its right side
has order two. This contradiction proves `z!=0`.

## 3. The rational derivative

Assume `z!=0` and `c,theta in F_p`. In `F_p`, put

```text
t=theta-h,
u=theta r_0/(z-r_0)=theta/(c-1),
w=theta z/(z-r_0)=theta c/(c-1).                     (3)
```

Choose integer representatives in `{0,...,p-1}` and define

```text
Psi=X^n R^t(R-z)^u/(D(R-r_0)^w).                     (4)
```

Equation (1) gives

```text
QG'=hQG/Y-(2a/Y)(G-lambda Y).                        (5)
```

Using `theta=2a/(r_0z)`, the three coefficient equations in (3) show

```text
QG'+tQG/Y+u(Y-r_0)G-w(Y-z)G=2a lambda.               (6)
```

Take the logarithmic derivative of (4), use
`G(R)D=X^n-alpha`, and then substitute (2) and (6). Since `n=m` in
characteristic `p`, the two remaining terms are

```text
-m alpha/(XG(R)D) + q lambda/(XG(R)D)=0.
```

Thus `Psi'=0`. The coefficient field is finite and perfect, so `Psi` is a
`p`th power in the rational function field. Every valuation of `Psi` is
therefore divisible by `p`.

## 4. Valuations force the impossible packet

First prove `theta=h`. If `ord_0(T)=0`, evaluation of (1) at `Y=0`, using
`G(0)!=0`, gives `2a=h r_0z`, hence `theta=h`. If `ord_0(T)=1`, then zero is
a simple root of `G`, so `R=0` is a complete squarefree split fiber. At each
of its roots, all factors in (4) except `R^t` are units. Divisibility of the
valuation by `p` gives `t=0`, again `theta=h`.

At a root of `R-z` of multiplicity `f`, squarefreeness of `D` and (4) give

```text
uf-1=0 mod p.                                         (7)
```

Every multiplicity is in `{1,...,p-1}`, so all equal the same integer `f`.
Their sum is the prime `p`; hence `f=1` and `u=1`. From (3),

```text
h/(c-1)=1,       c=m,       w=m.                     (8)
```

Let `e_0=ord_0(R-r_0)`. At zero, (4) gives

```text
n-me_0=0 mod p.
```

Since `n=m(p+1)` and `1<=e_0<p`, one has `e_0=1`. At every nonzero root of
`R-r_0` of multiplicity `e`, the valuation is `-1-me`, so

```text
me=-1 mod p.
```

The official relation `p=-1 mod m` gives the unique value

```text
e=((m-1)p-1)/m.                                      (9)
```

For `m in {8,16}` and `p>m`,

```text
e<p-1<2e.
```

But the nonzero roots of `R-r_0` must contribute total multiplicity `p-1`,
and every contribution is `e`. This is impossible, proving `(BSG4)--(BSG5)`.
