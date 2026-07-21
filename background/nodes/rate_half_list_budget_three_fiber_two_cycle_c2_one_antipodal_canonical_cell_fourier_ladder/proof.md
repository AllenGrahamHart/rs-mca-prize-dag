# Proof

The transferred canonical factorization gives `(CFL2)`.  Every factor has
degree at most

```text
max(deg B,H+deg C)<=2H-3=r.
```

On the other hand, `deg Q=N-4=4r`.  Equality in the degree of the product
therefore forces every `G_i` to have degree exactly `r`.  The polynomial
`1-z^N` is squarefree in the official characteristic, and `E` removes four
distinct roots, so `Q` is squarefree.  Its four factors are consequently
pairwise coprime and give the partition `(CFL3)`.

Put `D=C/B` as a formal series at zero.  Since every factor has constant term
one,

```text
log G_i
 =log B+log(1+w_i z^H D)
 =log B+sum_(m>=1) (-1)^(m+1) w_i^m z^(mH)D^m/m.      (1)
```

The root-cell factorization also gives

```text
log G_i=-sum_(j>=1) p_(i,j)z^j/j.                    (2)
```

All indices used below are smaller than `3H<N` and hence invertible in the
official characteristic.

Multiply `(1)` by `lambda_i` and sum over `i`.  The `log B` term vanishes by
the `m=0` equation in `(CFL5)`.  Below degree `(s+1)H`, only the powers
`1<=m<=s` can occur, and their coefficients vanish by the other equations in
`(CFL5)`.  Comparing with `(2)` proves `(CFL6)` for positive `j`; the case
`j=0` follows from the common cell size and `sum_i lambda_i=0`.

Taking `s=0` and `lambda=e_i-e_k` shows that all four power sums agree for
`1<=j<H`.  Since `j<N`, the sum over the full group `mu_N` is zero.  Summing
over all four cells therefore gives

```text
sum_i p_(i,j)=-sum_(a in Omega)a^j,
```

which proves `(CFL4)`.  At degree `H`, equation `(1)` gives

```text
p_(i,H)=b_H-Hw_i
```

for a scalar `b_H` independent of `i`, because `D(0)=1`.  The centered
identity `sum_i w_i=0` and the same full-group sum identify
`b_H=-(1/4)sum_(a in Omega)a^H`.  Here `H` is odd, so the contributions of
`1,-1` cancel.  This proves `(CFL7)`.

It remains to prove the support statement.  For every `j`, changing the
variable `a` to `-a` gives

```text
sum_(a in mu_N) u_lambda(a)a^j
 =(1-(-1)^j) sum_i lambda_i p_(i,j).                  (3)
```

Equations `(CFL5)--(CFL6)` make `(3)` zero for every
`0<=j<(s+1)H`.  Suppose `u_lambda` is nonzero and has `t<=(s+1)H` support
points `x_1,...,x_t`.  The first `t` equations in `(3)` form a square
Vandermonde system in the nonzero values `u_lambda(x_l)`.  Its determinant is

```text
product_(k<l)(x_l-x_k)!=0,
```

so all those values would be zero, a contradiction.  This proves `(CFL9)`.

Finally `u_lambda(-a)=-u_lambda(a)`.  The characteristic is odd and no
element of `mu_N` equals its negative, so its support has even size.  For
`s=1`, the odd lower bound `2H+1` rounds up to `2H+2`; for `s=2`, `H` is odd
and `3H+1` is already even.  Substituting `H=R+1` proves `(CFL10)`. QED.
