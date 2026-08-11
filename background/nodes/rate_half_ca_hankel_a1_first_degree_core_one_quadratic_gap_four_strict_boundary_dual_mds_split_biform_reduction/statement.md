# `A=1` quadratic strict-boundary dual-MDS split-biform reduction

- **status:** PROVED
- **closure:** exact split biform at the first strict pair boundary
- **consumer:** `rate_half_band_crossing_location`

Retain the strict boundary `(SBR1)`. Let `ell_alpha,ell_beta` be parameter
forms vanishing at the endpoints and put

```text
Lambda_2(t)=ell_alpha(t)ell_beta(t),
n_0=|U_0|=3p-1,
d=rho-1=2p-1.                                      (STB1)
```

For `x in U_0`, define

```text
H_x(t)=omega_x(t)Qbar(t;x)/Lambda_2(t).             (STB2)
```

This is a polynomial of parameter degree at most `e-1`, and

```text
sum_(x in U_0)H_x(t)x^j=0,
0<=j<=d.                                            (STB3)
```

There is a unique biform `G(t,X)` satisfying

```text
deg_t G<=e-1,
deg_X G<=p-2,
H_x(t)=G(t,x)/L_U0'(x)       (x in U_0).            (STB4)
```

Both degree bounds are exact. For every endpoint-missing coordinate

```text
x in M_alpha union M_beta,
```

the row `G(-,x)` has exact degree `e-1` and its roots are precisely the
off-line supported slopes whose actual supports contain `x`. Thus at least

```text
|M_alpha union M_beta|=2p+r_A                      (STB5)
```

fixed-domain rows split into `e-1` distinct off-line supported slopes.

Let `Z_clean` contain the off-line slopes with

```text
a_delta=r_delta=0.                                  (STB6)
```

Then

```text
|Z_clean|>=(e+15)/2+r_A.                            (STB7)
```

For each such slope, put

```text
A_delta(X)=product_(x in S_delta intersect U_0)(X-x),
deg A_delta=p-2.                                    (STB8)
```

There is a nonzero scalar `zeta_delta` with

```text
G(delta,X)=zeta_delta A_delta(X).                  (STB9)
```

For the official row, the bidegree and unconditional split lower bounds
are

```text
(e-1,p-2)=(183251937962,274877906942),
split domain rows >=549755813888,
clean split parameter fibers >=91625968989.         (STB10)
```

## Scope

This is a necessary split-biform profile, not its exclusion. The
`p-1-r_A` coordinates present at both endpoints may have an additional
source root away from the endpoint pair and are not counted in `(STB5)`.
