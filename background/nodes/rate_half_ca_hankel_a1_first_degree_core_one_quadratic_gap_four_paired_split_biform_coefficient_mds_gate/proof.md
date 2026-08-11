# Proof

Expand `G` as in `(CMG1)`. Exact row degree and the prescribed distinct root
set give one `lambda_x!=0` with

```text
G(t,x)=lambda_x P_x(t).                             (1)
```

Comparing coefficients of `t^j` proves the first equality in `(CMG3)`.
Each `g_j` has degree at most `n`, so its evaluation vector on `X` belongs
to `RS[F,X,n+1]`, proving the membership assertion.

For completeness, the standard dual-GRS parity checks for this evaluation
code are

```text
sum_(x in X) v_x x^l/L_X'(x)=0,
0<=l<=R-n-2.                                        (2)
```

Indeed, if `v_x=h(x)` with `deg h<=n`, the summand numerator has degree at
most `n+l<=R-2`; the Lagrange leading-coefficient identity makes `(2)`
zero. These checks have `R-(n+1)` independent rows, so they characterize
the code. Substituting `v_x=lambda_xp_(j,x)` gives exactly

```text
K lambda=0.                                         (3)
```

The monicity `p_(m,x)=1` gives `lambda_x=g_m(x)`. Dividing the other
coefficient equalities by this nonzero value proves `(CMG5)`.

For the extremal biform, Cycle 129 supplies exact bidegree `(e-2,p-3)` and
`R=3p-3+d_A` classified rows with exactly the required roots. Hence the
number of parity checks per coefficient is

```text
R-(n+1)
 =(3p-3+d_A)-(p-2)
 =2p-1+d_A.                                        (4)
```

There are `m+1=e-1` coefficient indices, proving `(CMG6)--(CMG7)`.

For the strict biform, Cycle 132 supplies exact bidegree `(e-1,p-2)` and
`R=2p+r_A` endpoint-missing rows. The checks per coefficient are

```text
R-(n+1)
 =(2p+r_A)-(p-1)
 =p+1+r_A.                                         (5)
```

There are `m+1=e` coefficient indices, proving `(CMG8)--(CMG9)`. QED.
