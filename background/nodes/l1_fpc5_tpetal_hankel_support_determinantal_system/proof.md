# Proof: FPC5 Hankel support-determinant system

For fixed `r`, the first `d` columns and first `d` rows in `(DS2)` form the
generalized Vandermonde matrix `V_r`. Its determinant has the printed
factorization and is nonzero because the support points are distinct and
nonzero.

Expand `(DS2)` along its last column. The signed cofactor vector is

```text
det(V_r)(g_0,...,g_(d-1),1),
```

because this is the unique monic coefficient vector annihilating the
Vandermonde columns at `x_1,...,x_d`. This proves `(DS3)`. The parent
Hankel theorem says that its `r`-th row equation is precisely the recurrence
in parentheses, proving `(DS4)`.

The ordinary Vandermonde matrix on exponents `0,...,d-1` is invertible, so
`(DS5)` has unique amplitudes, given by Cramer's rule. Put

```text
Q_i=G/(X-x_i).
```

Since `deg Q_i=d-1`, equation `(DS5)` gives

```text
M_0(Q_i)=sum_a [X^a]Q_i mu_a
        =sum_j w_j Q_i(x_j)
        =w_i Q_i(x_i)
        =w_i G'(x_i).
```

Squarefreeness makes `G'(x_i)` nonzero. The parent Cauchy theorem identifies
primitivity with `M_0(Q_i)!=0` for every `i`, proving `(DS6)--(DS8)`. QED.
