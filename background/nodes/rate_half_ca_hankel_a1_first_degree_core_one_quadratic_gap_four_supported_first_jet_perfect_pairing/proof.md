# Proof

The contracted error at a supported slope `gamma` has
`d-c_gamma` distinct nonzero moment sources. Its Vandermonde source matrix
has full column rank and all diagonal source weights are nonzero. Therefore

```text
rank M_gamma=d-c,
ker M_gamma=Q_min F[X]_(<=c),                        (1)
```

on both sides because the pencil is symmetric. This proves `(QFJ4)` and
gives a specialized kernel of dimension `c+1`. The primitive kernel vector
specializes to `Q_gamma=Q_min R_gamma` inside this space.

The exact regular-factor identities are

```text
double root: D_1=a g_* S_B^2,
two simple:  D_1=a G_1G_2S_1S_2,                    (2)
```

with `a!=0`. In the double-root arm every root of `g_*` has `c=1`. In the
two-simple arm

```text
c_gamma=1_(G_1(gamma)=0)+1_(G_2(gamma)=0).           (3)
```

The supported factors are squarefree, with their common roots counted once
in each factor. Under `(QFJ3)`, equations `(2),(3)` therefore give

```text
ord_gamma(D_1)=c.                                    (4)
```

Work over the local DVR at `gamma`. The primitive local kernel vector
`q(z)` extends to a basis. In that basis the symmetric pencil is a zero
row and column together with its regular block, whose determinant is
`D_1` up to a unit. The specialized rank loss supplies exactly `c`
positive Smith invariants. Their valuations are positive integers whose
sum is `(4)`, namely `c`; hence every positive Smith exponent is one.

It follows that the derivative of the regular block gives a nondegenerate
symmetric form on the `c` new kernel directions. In the original basis,
terms caused by differentiating the change of basis vanish when restricted
to `ker M_gamma`, so this induced form is simply the restriction of
`dot M`. For coefficient polynomials it is

```text
(Q_min A)^T dot M (Q_min B)
 =dot Phi(Q_min^2AB)=B_gamma(A,B).                   (5)
```

Thus `B_gamma` has rank `c`.

Differentiate the primitive kernel identity

```text
M(z)q(z)=0.                                         (6)
```

At `z=0`, pair `(6)'` with any vector in `ker M_gamma`. The term involving
`M_gamma q'(0)` vanishes, leaving

```text
B_gamma(A,R_gamma)=0       for every deg A<=c.       (7)
```

Symmetry gives the same left radical. Since the ambient kernel has
dimension `c+1` and the form has rank `c`, its radical is one-dimensional;
`(7)` proves `(QFJ6)` and `(QFJ7)`.

For `c=1`, the polynomials `1,X` form a basis and the radical is generated
by `X-r_gamma`. Pairing that radical with both basis elements gives the
first two equations in `(QFJ8)`. The class of `1` is nonzero in the
one-dimensional quotient and its induced form is nondegenerate, giving the
last equation.

Finally `deg S_B=2` and `deg(S_1S_2)=1+3=4`. These are the only points
removed by `(QFJ3)`, proving the exception caps. QED.
