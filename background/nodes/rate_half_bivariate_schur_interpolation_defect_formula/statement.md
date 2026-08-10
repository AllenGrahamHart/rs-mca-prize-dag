# Schur interpolation-defect formula

- **status:** PROVED
- **closure:** exact Lagrange elimination
- **consumer:** `rate_half_band_crossing_location`

Use the normalized parameter basis and notation of
`rate_half_bivariate_top_vandermonde_schur_reduction`. Put

```text
s=4m+1,
H_x(Y)=c_(1,x)^(-1)L_x(Y)A_x(Y)Y^Delta_x
      =sum_(j=0)^(m+1) h_j(x)Y^j,
h_(m+1)(x)=1.                                         (SID1)
```

Choose a pivot set `P subset W` with `|P|=s` and define its Lagrange basis

```text
ell_p(X)=product_(u in P, u!=p)(X-u)/(p-u).            (SID2)
```

For every nonpivot point `x in W\P`, the Schur column belonging to its
highest clone `(x,Delta_x)` has entries

```text
S_W[(i,j),x]
 =c_(1,x) ( x^i h_j(x)
             -sum_(p in P) ell_p(x)p^i h_j(p) ),       (SID3)
0<=i<=4m,       0<=j<=m.
```

For a lower clone `(x,t)` with `0<=t<Delta_x`, its top coefficient is zero,
so elimination leaves the original lower entries:

```text
S_W[(i,j),(x,t)]
 =x^i [Y^j](L_x(Y)A_x(Y)Y^t).                         (SID4)
```

The normalized coefficient data are elementary symmetric functions of the
coordinate roots:

```text
h_j(x)=(-1)^(m+1-j) e_(m+1-j)(
  A_x multiset_union {mu_x} multiset_union {0^Delta_x}
),                                                     (SID5)
```

where `L_x/c_(1,x)=Y-mu_x`.

In the saturated case `Delta_W=0`, the residual has only the columns in
`W\P`. For fixed `j`, define the interpolation-defect matrix

```text
E_j(P)[i,x]
 =x^i h_j(x)-sum_(p in P)ell_p(x)p^i h_j(p).           (SID6)
```

If any `E_j(P)` has full column rank `|W|-s`, then `M_W` has full column
rank. Thus a single normalized coefficient can certify the whole saturated
rank obstruction.

## Scope

The formulas are exact identities. They do not assert that a defect matrix
is full rank, nor that bad overlap forces one to be full rank. Deficiency
clones must be included through `(SID4)`.
