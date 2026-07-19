# Proof

Let `W` be the two-dimensional row space of `Lambda`. For every active
coordinate `x`, evaluation at `x` is a nonzero linear functional on `W`.
Its kernel is one projective point of `P(W)`. The selected rows are pairwise
nonproportional, so at most one of them vanishes at `x`. Hence every active
column has degree `t-1` or `t`.

Write `S_i=supp(lambda_i)`. Summing pairwise support intersections by
coordinates gives

```text
sum_(i<j)|S_i intersect S_j|
  =sum_(x in U) C(deg(x),2)
  >=R C(t-1,2).
```

The block intersection cap gives the opposite bound

```text
sum_(i<j)|S_i intersect S_j| <= kappa C(t,2).
```

Therefore

```text
R <= kappa t/(t-2).                                  (1)
```

Two selected supports have size at least five and intersection at most
`kappa`, so their union has size at least `10-kappa`. In particular, if
`kappa<=3`, then `R>=7`, whereas `(1)` and `t>=4` give `R<=2kappa<=6`.
This excludes rank two for pair cap at most three.

Now take `kappa=4`. The same union bound gives `R>=6`. Combining it with
`(1)` shows `t<=6`; it also gives

```text
t=4: R in {6,7,8},       t in {5,6}: R=6.            (2)
```

For each row let `Z_i=U\S_i` and `z_i=|Z_i|`. The projective-kernel argument
shows that the `Z_i` are pairwise disjoint, so

```text
sum_i z_i <= R.                                      (3)
```

No `z_i` is zero: a full-support row would meet every other row in at least
five coordinates. Row weight at least five gives `z_i<=R-5`. Finally,
disjointness of the zero sets makes the pair intersections exact:

```text
|S_i intersect S_j|=R-z_i-z_j<=4.                   (4)
```

For `R=6`, these inequalities force every `z_i=1`. For `(t,R)=(4,7)`,
they force one `z_i=1` and three `z_i=2`; for `(t,R)=(4,8)`, they force all
four `z_i=2`. This proves the zero and row-weight columns of `(SA2)`.
Every coordinate belongs to either no `Z_i` or exactly one, which gives the
printed active-column degrees.

Each row annihilates cubic evaluations, even after restriction to `U`, so

```text
W subset ev_U(F[X]_<4)^perp.
```

The code on the right has dimension `R-4`, proving equality when `R=6`.
Choose a basis `f,g` of `W` and write
`lambda_i=a_i f+b_i g`. The two trade identities become

```text
(sum_i a_i)f+(sum_i b_i)g=0,
(sum_i gamma_i a_i)f+(sum_i gamma_i b_i)g=0.
```

Independence of `f,g` shows that both coefficient vectors annihilate `1`
and `(gamma_i)_i`. Their span is therefore a two-dimensional subcode of the
dual `RS_2` code on the `t` slopes. That dual has dimension `t-2`, proving
equality for `t=4`.

It remains to show sharpness. Work in characteristic greater than `17`. Use
the following evaluation domains, exponents, and distinct row parameters:

```text
R=6: U={0,1,2,3,4,5},       d=1, a_i in {0,...,t-1};
R=7: U={0,+-1,+-2,+-3},     d=2, a_i in {0,1,4,9};
R=8: U={+-1,+-2,+-3,+-4},   d=2, a_i in {1,4,9,16}.
```

Put `gamma_i=a_i`,

```text
c_i=1/product_(j!=i)(a_i-a_j),
lambda_i(x)=c_i (x^d-a_i)/Lambda'_U(x).              (5)
```

The numerator degree is below `R-4`, so every row in `(5)` annihilates all
cubics on `U`. The barycentric identities

```text
sum_i c_i a_i^j=0,             0<=j<=t-2,
```

applied at `j=0,1,2` prove both trade identities. The row space is generated
by the two independent evaluations of `1` and `X^d`, so it has rank two.
The fibers of `X^d` on the three displayed domains give exactly the five
zero profiles in `(SA2)`. Their pairwise support intersections are at most
four. If larger agreement blocks are desired, append row-specific private
coordinates with zero coefficients; this preserves both trade identities
and all pair intersections. Thus every profile is an exact dual-product-code
trade, completing the proof.
