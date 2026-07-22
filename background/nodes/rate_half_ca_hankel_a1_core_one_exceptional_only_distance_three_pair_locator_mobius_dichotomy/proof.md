# Proof

All `D_i` have degree two and leading coefficient one, so their span has
dimension at most three. Distinctness rules out dimension one, proving
`(PMD2)`.

Assume first that the span has dimension two. The coefficient points
`(s_i,p_i)` lie on one affine line. Hence there are scalars
`alpha,beta,gamma`, not both `alpha,beta` zero, such that

```text
beta p_i+alpha s_i=gamma.                            (1)
```

Using `s_i=a_i+b_i` and `p_i=a_i b_i` gives `(PMD4)`.

The symmetric bidegree-`(1,1)` form

```text
F(x,y)=beta xy+alpha(x+y)-gamma                     (2)
```

is irreducible. Indeed, reducibility is equivalent to
`alpha^2+beta gamma=0`, in which case `(2)` is a product of one factor in
`x` and one in `y`. Every pair on that union must then contain the same
fixed point, impossible for two disjoint pairs. Since `e>=2`, this case is
excluded.

Consequently the matrix

```text
[ -alpha  gamma ]
[  beta   alpha ]                                    (3)
```

is nonsingular and defines `(PMD5)`. Equation `(PMD4)` says exactly that
`b_i=phi(a_i)`. Symmetry gives `a_i=phi(b_i)`. Equivalently, the square of
the matrix in `(3)` is `(alpha^2+beta gamma)` times the identity, so `phi`
is a nonidentity projective involution. This proves `(PMD3)`.

Conversely, in odd characteristic every nonidentity Mobius involution has a
nonsingular trace-zero representative. After naming its entries as in
`(3)`, each two-cycle obeys `(PMD4)`. Thus all coefficient points
`(s_i,p_i)` lie on one affine line, and the distinct monic quadratics span
dimension exactly two. QED.
