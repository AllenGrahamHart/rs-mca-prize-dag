# Top-coefficient Vandermonde Schur reduction

- **status:** PROVED
- **closure:** exact block elimination
- **consumer:** `rate_half_band_crossing_location`

Retain the deficiency-aware matrix `M_W` with

```text
U_W=|W|+Delta_W,
Delta_W=sum_(x in W)(m-d_x),
```

and assume the live support range `|W|>=4m+2`. Since `|W|<q`, change the
projective parameter basis so that every joint-representation factor has

```text
L_x(Y)=c_(0,x)+Yc_(1,x),       c_(1,x)!=0.             (TVS1)
```

For each `x`, the highest clone column `(x,Delta_x)` has top parameter
coefficient `c_(1,x)`, while every lower clone column has top coefficient
zero. Hence the rows `j=m+1` and those highest columns contain

```text
(c_(1,x)x^i)_(0<=i<=4m, x in W),                      (TVS2)
```

a diagonally scaled Vandermonde matrix of rank `4m+1`.

Choose any `P subset W` of size `4m+1`, order the top rows first and the
highest columns from `P` first, and write

```text
M_W = [ V  B ],
      [ C  D ]                                           (TVS3)
```

where `V` is square. Then `V` is invertible and

```text
rank(M_W)=4m+1+rank(S_W),
S_W=D-C V^(-1) B.                                      (TVS4)
```

The residual matrix has exactly

```text
v_W=U_W-(4m+1)=|W|+Delta_W-(4m+1)                     (TVS5)
```

columns. In particular,

```text
v_W<=4m-2                    when |W|<=7m-1,
v_W<=3m-1                    when O=0 and |W|<=7m-1.   (TVS6)
```

Thus `M_W` has full column rank exactly when `S_W` does. At `m=1` the
proved route-fence matrices have `v_W=1` and zero residual rank; at `m=2`
the open-band search tests residual widths only `2..5`.

## Scope

This is a rank reduction, not the missing rank theorem. The Schur matrix
depends on the incidence roots, fibre roots, domain points, deficiencies, and
choice of pivot set `P`. Different choices are row/column-equivalent for the
full-rank question.
