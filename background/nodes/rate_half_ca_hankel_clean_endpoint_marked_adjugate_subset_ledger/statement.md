# Clean-endpoint marked adjugate subset ledger

- **status:** PROVED
- **closure:** exact adjugate and Cauchy-Binet factorization
- **consumer:** `rate_half_band_crossing_location`

Put `n=rho+1=4m` and let

```text
M(t)=(y^(0)_(i+j)+t y^(1)_(i+j))_(0<=i<=n,0<=j<n)
```

be the full `(n+1) x n` Hankel pencil. For its top and bottom square blocks,
define the marked contraction

```text
L(t)=H_1(t)-x_0H_0(t).                                (MAS1)
```

After refining the existing generic parameter-coordinate choice by finitely
many avoidances,

```text
rank_F(t) L(t)=rho,
adj L(t)=D(t)q(t)q(t)^T,
deg D=2m-1.                                           (MAS2)
```

Here `q(t)` is the primitive coefficient vector of `Q(t;X)` and `D` is a
nonzero scalar polynomial. Its roots are exactly the projective rank-drop
parameters of the marked square pencil.

More precisely, if `Delta(t)` is the determinant of the size-`m-1` regular
Kronecker block of the full rectangular pencil, then

```text
D(t)=c Delta(t)Q(t;x_0)=c Delta(t)A_0(t)S(t),
deg Delta=m-1,       c!=0.                              (MAS3)
```

Retain the saturated support `U` and write

```text
mu_x(t)=(x-x_0)(omega_x^(0)+t omega_x^(1)),
R_U=(x^i)_(0<=i<=rho,x in U).                         (MAS4)
```

Then `L(t)=R_U diag(mu_x(t))R_U^T`. For `0<=i,j<=rho`, Cauchy-Binet gives
the exact cofactor ledger

```text
D(t)q_i(t)q_j(t)
 =(-1)^(i+j) sum_(J subset U, |J|=rho)
   det(R_(hat j,J)) det(R_(hat i,J))
   product_(x in J) mu_x(t).                          (MAS5)
```

Every determinant in `(MAS5)` is an explicit generalized Vandermonde minor.
For the corner cofactor `i=j=rho`, both are ordinary Vandermonde
determinants and are nonzero; interior deleted-exponent minors may vanish.
Exactly `m-1` distinct supported slopes are roots of `Q(t;x_0)`, while
`Delta` has degree `m-1`. Since the supported set has `T=4m+1` distinct
parameters, at least

```text
T-2(m-1)=2m+3                                          (MAS6)
```

supported slopes satisfy `D(gamma)!=0`. At each such slope, `(MAS5)` is a
nonzero rank-one matrix whose vector `q(gamma)` is a squarefree degree-`rho`
locator split on `D`.

## Scope

The subset sum in `(MAS5)` is signed and field-valued; positivity or
termwise noncancellation is not asserted. The live theorem is to combine its
rank-one specializations with the simultaneous degree-`m` motion of `q` and
the supported-root incidence. A raw count of the `rho`-subsets does not close
the endpoint.
