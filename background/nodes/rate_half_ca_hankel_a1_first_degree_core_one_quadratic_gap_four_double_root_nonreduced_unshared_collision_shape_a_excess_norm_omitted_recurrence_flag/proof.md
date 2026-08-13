# Proof

For each `x in U_0`, put

```text
H_x(t)=omega_x(t)Q(t,x)/Lambda(t).                 (1)
```

The dual-MDS reduction proves that these are polynomials and that

```text
H_x(t)=G(t,x)/L_U0'(x),
sum_x H_x(t)x^j=0       (0<=j<=d).                 (2)
```

Let `L=L_U0`, a monic polynomial of degree `R`. Lagrange interpolation gives

```text
G(t,X)=sum_x H_x(t)L(X)/(X-x).                     (3)
```

For `k>=0`, define

```text
c_k(x)=[X^(R-1-k)] L(X)/(X-x).                    (4)
```

Polynomial division by `X-x` shows that `c_k(x)` is a monic polynomial in
`x` of degree `k`. Taking the coefficient of `X^(R-1-k)` in `(3)` gives

```text
[X^(R-1-k)]G=sum_x H_x c_k(x).                    (5)
```

For `k<=d`, equation `(2)` makes `(5)` zero. For `k=d+1+r`, monicity and the
same vanishing give a unitriangular relation

```text
[X^(n-r)]G
 =S_(d+1+r)+sum_(j=d+1)^(d+r)a_(r,j)S_j,
S_j:=sum_x H_x x^j,                                (6)
```

because `R-1-(d+1+r)=n-r`. Therefore the first `r+1` top coefficients of
`G` vanish at a parameter value if and only if

```text
S_(d+1)=...=S_(d+1+r)=0.                           (7)
```

Multiplying `(1)` by `x^j`, summing over `x`, and expanding `Q` gives

```text
Lambda S_j
 =sum_x omega_xQ(t,x)x^j
 =sum_(i=0)^d q_i h_(i+j)
 =R_j.                                             (8)
```

At an off-line slope `delta`, `Lambda(delta)` is nonzero. Hence `(7)--(8)`
are equivalent to the recurrence-defect vanishing in `(ORF5)`. Since every
specialized fiber is nonzero, the number of consecutive zero top
coefficients is exactly `n-deg_X G(delta,X)=q_delta`. This proves
`(ORF5)` and, at `r=0`, `(ORF8)`.

The polynomial `H_off` is squarefree. Consequently `deg C_r` is exactly the
number of its roots `delta` for which `q_delta>=r+1`. The layer-cake identity
for nonnegative integers gives

```text
sum_delta q_delta
 =sum_(r=0)^(n-1)#{delta:q_delta>=r+1}
 =sum_(r=0)^(n-1)deg C_r.                          (9)
```

Finally, the shape-A norm concentration theorem gives

```text
deg T=e-sum_delta q_delta.                         (10)
```

Substitute `(9)` into `(10)` to obtain `(ORF7)`. QED.
