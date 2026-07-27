# Proof - L1 Mersenne HNF m=8 order-zero quadratic exclusion

Assume that `E_s` is quadratic. The two dependency theorems show that it is
not injective on the seven roots of `P_s` and that it has at most one repeated
color. Its color multiset therefore has exactly one double color, five other
colors, and two omitted colors.

## 1. Normalize the color pattern

Divide all colors by the double color and choose a primitive eighth root
`zeta`. The normalized color multiset is

```text
M_(i,j)=mu_8 \ {zeta^i,zeta^j} disjoint_union {1},
1<=i<j<=7.                                           (1)
```

These are exactly 21 patterns. Write

```text
E_s(W)/delta=A W^2+B W+C=y W(W-S)+x,
S=-B/A,       y=A!=0.                                (2)
```

The letters in `(2)` absorb the harmless division by the double color.

## 2. Three centered moments

Let `a_1,...,a_7` be the roots of `P_s`. Newton's identities for the
truncated-binomial coefficients give

```text
sum_r a_r^k=-s,       1<=k<=7.                       (3)
```

Put `u_r=a_r(a_r-S)` and `z=1-S`. For `k<=3`, expansion uses root moments
only through degree six, so `(3)` gives

```text
sum_r u_r^k=-s z^k.                                  (4)
```

The second and third centered moments of the seven `u_r` are consequently

```text
M_2=-s(7+s)z^2/7,
M_3=-s(7+s)(7+2s)z^3/49.                             (5)
```

For the color pattern `(1)`, put

```text
P_k=1-zeta^(ik)-zeta^(jk),
C_2=P_2-P_1^2/7,
C_3=P_3-3P_1P_2/7+2P_1^3/49.                        (6)
```

The full `mu_8` power sums vanish for `k=1,2,3`, which proves `(6)`.
Exact arithmetic in `F_p(mu_8)` verifies `C_2!=0` in all 21 patterns on
each printed row. Since affine maps multiply centered moments by `y^k`,
equations `(5)--(6)` imply

```text
I_(i,j):=C_3^2/C_2^3
         =-(7+2s)^2/[7s(7+s)].                       (7)
```

Here `s` and `s+7` are nonzero because `s notin F_p`; the nonzero left side
of the second-moment identity also excludes `z=0`. Thus no division in `(7)`
discards a candidate. Every survivor is a root of the quadratic

```text
q_(i,j)(X)=(7+2X)^2+7 I_(i,j) X(7+X).               (8)
```

## 3. The constant-coefficient torsion test

The constant coefficient of `P_s` is

```text
b_7(s)=binom(s+6,7).                                 (9)
```

Because `P_s` is monic of odd degree, the product of its roots is
`-b_7(s)`. All roots lie in `mu_n`, and `n` is even. Hence

```text
b_7(s)^n=1.                                          (10)
```

This necessary condition uses only `P_s | W^n-1`; it does not assume that
the centered-moment equations are sufficient.

## 4. Exact finite certificate

For every printed characteristic, `p=7 mod 8`, so
`K=F_p(mu_8)=F_(p^2)`. The primary verifier chooses `zeta` with

```text
zeta^2-r zeta+1=0,       r^2=2,
```

reduces `b_7(X)^n-1` modulo each quadratic `(8)`, and checks in `K[X]` that

```text
gcd(q_(i,j)(X), b_7(X)^n-1)=1                       (11)
```

for all `4*21=84` row-pattern pairs. A common root in any extension of the
official field would make this gcd nonconstant, so `(11)` excludes every
possible `s`.

The independent audit uses the different presentation
`K=F_p[u]/(u^2+2)`, takes `zeta=(r+u)/2`, and checks the nonzero Sylvester
resultant of `(8)` with the linear remainder of `(10)`. Its four row digests
are pinned in the source. Both implementations use exact modular arithmetic
and enumerate color patterns, not field elements.

The contradiction between `(8)`, `(10)`, and `(11)` proves `(MQ2)`. QED.
