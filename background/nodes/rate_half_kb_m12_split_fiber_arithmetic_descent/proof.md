# Proof

## 1. Arithmetic monodromy

Let `G_geom` be the geometric monodromy of `F` and `G_ar` its arithmetic
monodromy over `K`. The geometric group is normal and the quotient is the
constant-field Galois group. Arithmetic Frobenius generates that cyclic
quotient.

The zero fiber of `F` consists of five distinct individually `K`-rational
points. It is unramified, and its Frobenius permutation on the five sheets is
the identity. The image of this identity in `G_ar/G_geom` is the arithmetic
Frobenius generator. Thus the quotient is trivial, proving `(KBA-1)`.

Arithmetic factors of `F(Y)-F(Z)` correspond to point-stabilizer orbits of
`G_ar`, while geometric factors correspond to those of `G_geom`. Equality
of the groups therefore descends every geometric outer component to `K`.

## 2. Three K-affine normalizations

Ramification index multisets are Galois invariant.

For the `S5` profile `(3,2),(2)`, the two finite branch values have distinct
types and hence belong to `K`. In the `(3,2)` fiber, the index-three and
index-two critical points are individually distinguished, hence also belong
to `K`. Sending them to zero and one and normalizing the two branch values
uses affine transformations over `K`; the derivative-integration proof then
gives `x^3(x-1)^2` over `K`.

The same argument applies to the `S5` profile `(4),(2)`: both branch values
and their uniquely indexed critical points are in `K`, giving
`x^4(5-4x)` by `K`-affine transformations.

For the `A5` profile `(3),(2,2)`, the different branch types again put both
branch values in `K`; the unique index-three point is in `K`. Translate it
to zero. The two index-two critical points form a Galois-stable pair
`{b,c}`. Over the algebraic closure, scale `b` to one and put `t=c/b`. The
normal-form calculation gives

```text
3t^2+4t+3=0.                                         (1)
```

Every nonzero element of the prime field is a square in its even-degree
extension `K`: for `d in F_p^*`,

```text
d^((p^6-1)/2)
=(d^((p-1)/2))^(1+p+p^2+p^3+p^4+p^5)=1,
```

because the final exponent is even. Thus the discriminant `-20` of `(1)`
is a square in `K`, and both possible values of `t` lie in `K`.

If `{b,c}` were nonsplit, Frobenius would exchange `b,c`, sending `t` to
`1/t`. But `t` is fixed because `t in K`, so `t^2=1`. Neither `1` nor `-1`
satisfies `(1)` in the deployed characteristic. Hence `b,c in K`, and the
source scaling and target normalization are over `K`. This proves `(KBA-2)`.

## 3. Twist boundary

The two finite branch values in the Dickson row have the same type. The two
index-three branch values in the `A5 (3),(3)` row also have the same type.
In the one-parameter `S5` row, the colliding index-two critical pair need not
split. The preceding distinguished-point argument does not decide these
three cases, so they are retained exactly as `(KBA-3)`. QED.
