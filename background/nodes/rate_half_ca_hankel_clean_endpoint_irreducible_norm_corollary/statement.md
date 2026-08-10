# Clean-endpoint irreducible norm corollary

- **status:** PROVED
- **closure:** exact specialization of the component-defect ledger
- **consumer:** `rate_half_band_crossing_location`

Retain the hypothetical strict endpoint with `m>1` and impose the clean
branch `O=0`:

```text
rho=4m-1,       N=16m,       T=4m+1,
sum_gamma (rho-u_gamma)=0.                            (CIN1)
```

Then every supported slope has exactly `rho` distinct roots in `D`. There is
a unique point `x_0 in D` with `d_(x_0)=m-1`, while every other domain point
has `d_x=m`.

The primitive generic apolar generator

```text
Q(U,V;X),       (deg_X Q,deg_(U,V)Q)=(4m-1,m),       (CIN2)
```

is absolutely irreducible over the algebraic closure of the constant field.
If

```text
H(U,V)=product_(gamma in Z)L_gamma(U,V),
R(U,V)=product_(x in D)Q(U,V;x),
```

then the endpoint norm has exactly one linear defect:

```text
R=H^rho S,       deg S=1.                             (CIN3)
```

The unique-column complementary identity is

```text
P_sat(X)=(X^N-1)/(X-x_0),
Q Vbar+P_sat W=H,                                     (CIN4)
```

with

```text
deg_(U,V)Vbar=3m+1,       deg_X Vbar<N-1,
deg_(U,V)W<=4m+1,         deg_X W<=4m-2.              (CIN5)
```

At least `3m+1` supported slopes are also generic-rank and
parameter-transverse at every one of their `rho` roots.

## Scope

This closes all reducible and product-of-rational-moving-branches
continuations on the clean branch. It does not exclude the remaining
absolutely irreducible bidegree-`(4m-1,m)` curve with cyclic norm `(CIN3)`,
and it says nothing about `O>0` branches.
