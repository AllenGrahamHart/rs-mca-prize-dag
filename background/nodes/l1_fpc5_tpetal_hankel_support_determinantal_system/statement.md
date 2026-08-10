# FPC5 Hankel support-determinant system

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Let `mu_0,mu_1,...` be the weighted moment sequence of an owner-free FPC5
Padé-Hankel cell, and let

```text
G(X)=product_(i=1)^d (X-x_i)
    =X^d+sum_(a=0)^(d-1) g_a X^a                    (DS1)
```

be a monic degree-`d` divisor of the source-core locator. Official smooth
domains have distinct nonzero core points. If the Hankel block has `c`
rows, define for `0<=r<c`

```text
D_r(x_1,...,x_d;mu)=det
 [x_1^r       ... x_d^r       mu_r
  x_1^(r+1)   ... x_d^(r+1)   mu_(r+1)
  ...
  x_1^(r+d)   ... x_d^(r+d)   mu_(r+d)].             (DS2)
```

Then

```text
D_r=det(V_r(x_1,...,x_d))
    (mu_(r+d)+sum_(a=0)^(d-1)g_a mu_(r+a)),          (DS3)
```

where

```text
det V_r=(product_i x_i^r)(product_(i<j)(x_j-x_i))
```

is nonzero. Consequently

```text
coeff(G) in ker H_mu
iff D_r(x_1,...,x_d;mu)=0 for every 0<=r<c.           (DS4)
```

Let `w_1,...,w_d` be the unique amplitudes satisfying

```text
mu_a=sum_i w_i x_i^a,       0<=a<d.                  (DS5)
```

They are the usual Cramer ratios for the Vandermonde matrix. For every
selected root,

```text
M_0(G/(X-x_i))=w_i G'(x_i).                          (DS6)
```

Thus the primitive puncture condition is equivalent to

```text
w_i!=0 for every i,                                  (DS7)
```

or equivalently to nonvanishing of all support-column Cramer minors.

The primitive core-split locators in the cell are therefore exactly the
unordered points of the quasi-affine system

```text
x_i in Core,       x_i distinct,
D_r=0 for 0<=r<c,       product_i w_i!=0,             (DS8)
```

with the required background Cauchy equations and first-owner filters
appended. In a fixed required-background cell, `c=ell-1`.

## Scope

This theorem is an exact support-coordinate transport. It does not bound
the number of points of `(DS8)`, classify its components, remove periodic
supports, or pay the background/first-owner aggregation.
