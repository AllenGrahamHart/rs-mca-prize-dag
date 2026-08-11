# Proof

The top rows and pivot highest-clone columns form

```text
V[i,p]=c_(1,p)p^i,       0<=i<=s-1,       p in P.
```

For a nonpivot highest clone at `x`, its top-row vector is

```text
B[i,x]=c_(1,x)x^i.
```

Lagrange interpolation of the monomials `X^i`, `0<=i<s`, gives

```text
x^i=sum_(p in P)ell_p(x)p^i.
```

Consequently the solution of `Vw=B[:,x]` is

```text
w_p=c_(1,x)ell_p(x)/c_(1,p).                          (1)
```

The lower-row entry of the highest clone at `(i,j)` is

```text
c_(1,x)x^i h_j(x),
```

while the corresponding pivot entry is `c_(1,p)p^i h_j(p)`. Subtracting
the pivot combination `(1)` gives exactly `(SID3)`.

A lower clone has polynomial degree at most `m`, so its `j=m+1` coefficient
vanishes. Its top block `B` is therefore zero, and the Schur subtraction does
nothing to that column. This proves `(SID4)`.

Finally,

```text
H_x(Y)=Y^Delta_x (Y-mu_x) product_(gamma in A_x)(Y-gamma)
```

is monic of degree `m+1`. The standard coefficient formula for a monic
root-product is `(SID5)`.

When `Delta_W=0`, there are no lower clones. The rows with a fixed `j` form
`E_j(P)` up to nonzero column scalings `c_(1,x)`. If one such block has full
column rank, then the full Schur matrix does too. The preceding Schur
reduction then makes `M_W` full column rank. QED.
