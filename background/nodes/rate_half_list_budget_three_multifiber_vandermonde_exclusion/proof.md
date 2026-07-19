# Proof

Put `c_i=r_i^m` and

```text
Q_i(X)=(X^m-c_i)/(X-r_i)
      =sum_(j=0)^(m-1) r_i^(m-1-j) X^j.               (1)
```

The remaining factor

```text
C_i^*(X)=product_(c in C_i\{c_i})(X^m-c)              (2)
```

is a monic polynomial in `X^m` of degree `s-1`. Hence

```text
A_i(X)=Q_i(X)C_i^*(X).                                 (3)
```

The leading term of `(2)` is `X^(m(s-1))`; every other term has degree at
most `m(s-2)`. Since `deg Q_i=m-1`, the coefficient interval

```text
m(s-1),...,ms-1                                       (4)
```

of `A_i` is exactly the coefficient vector of `Q_i`, shifted by
`m(s-1)`. Lower terms of `(2)` cannot enter `(4)`.

Suppose `sum_i lambda_i A_i=0`. Reading interval `(4)` and then reversing its
coefficient order gives

```text
sum_i lambda_i (1,r_i,...,r_i^(m-1))=0.               (5)
```

The first `t` coordinates in `(5)` form a square Vandermonde matrix on the
distinct `r_i`. Its determinant is

```text
product_(i<j)(r_j-r_i) !=0.
```

Thus every `lambda_i=0`, proving `(MVE2)`.

For a completed quotient block, its full locator is exactly `B_i`; deleting
one exceptional root gives `A_i`. The linear Grassmann atlas proves that the
four cycle locators satisfy a nondegenerate constant relation and that the
three path locators in the tight triangle satisfy one. Applying `(MVE2)` with
`t=4` or `t=3` gives the two contradictions in the statement.

Finally, every quotient-fiber size of a power-of-two domain is a power of two.
At `d=2^39`, all such sizes other than `1,2` meet `m>=4`. This proves the
official arithmetic consequence and the stated residual list. QED.
