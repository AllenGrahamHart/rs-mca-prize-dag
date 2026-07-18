# Component-profile rigidity at the strict endpoint

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

Retain the hypothetical failing endpoint profile from
`rate_half_ca_hankel_endpoint_norm_factorization`:

```text
m>1,       rho=4m-1,       N=16m,       T=4m+1,
I=T*rho-O,       0<=O<=m-1.                           (CPR1)
```

Factor the primitive generic apolar generator over the algebraic closure of
the constant field:

```text
Q(U,V;X)=product_i Q_i(U,V;X),
(r_i,e_i)=(deg_X Q_i,deg_(U,V) Q_i).                  (CPR2)
```

Every `r_i,e_i` is positive.  There is a unique component `i_*` such that

```text
r_(i_*)=4e_(i_*)-1,                                   (CPR3)
```

while every other component is balanced:

```text
r_i=4e_i.                                             (CPR4)
```

Moreover the defect-one component is dominant:

```text
e_(i_*)>=ceil((3m+1)/4),
sum_(i!=i_*)e_i<=floor((m-1)/4).                      (CPR5)
```

In particular `e_(i_*)>=2`, so `Q`, viewed over `Fbar(X)`, has a
parameter-irreducible factor of degree at least two.  It cannot split into
`m` rational moving-root branches.

For the official `m=2^37`, the dominant component satisfies

```text
e_(i_*)>=3*2^35+1,
r_(i_*)>=3*2^37+3,
sum_(i!=i_*)e_i<=2^35-1.                              (CPR6)
```

This theorem does not exclude the dominant nonlinear component and therefore
does not close the strict endpoint.
