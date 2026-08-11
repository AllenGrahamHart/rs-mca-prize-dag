# `A=1` quadratic extremal dual-MDS split-biform reduction

- **status:** PROVED
- **closure:** exact lower-degree biform with dense two-directional splitting
- **consumer:** `rate_half_band_crossing_location`

Retain the extremal branch. Let

```text
Lambda_A(t)=ell_alpha(t)ell_beta(t)ell_theta(t),
n_0=|U_0|=3p-2,
d=rho-1=2p-1.                                      (DSB1)
```

For every `x in U_0`, define

```text
H_x(t)=omega_x(t)Qbar(t;x)/Lambda_A(t).             (DSB2)
```

The quotient is a polynomial of parameter degree at most `e-2`, and

```text
sum_(x in U_0)H_x(t)x^j=0,
0<=j<=d.                                            (DSB3)
```

There is a unique biform `G(t,X)` with

```text
deg_t G<=e-2,
deg_X G<=p-3,
H_x(t)=G(t,x)/L_U0'(x)       (x in U_0).            (DSB4)
```

Both degree bounds are exact. More precisely, for every classified source
coordinate `x in M_gamma`,

```text
deg_t G(t,x)=e-2,
Z(G(-,x))={delta notin A:x in S_delta}.             (DSB5)
```

Thus at least

```text
|M_alpha|+|M_beta|+|M_theta|=3p-3+d_A              (DSB6)
```

distinct domain rows split into `e-2` distinct roots among the `3e`
off-line supported slopes.

Let `Z_clean` be the off-line slopes satisfying

```text
a_delta=r_delta=0.                                  (DSB7)
```

Then

```text
|Z_clean|>=e+6+d_A.                                 (DSB8)
```

For `delta in Z_clean`, put

```text
A_delta(X)=product_(x in I_delta)(X-x),
|I_delta|=p-3.                                      (DSB9)
```

There is a nonzero scalar `zeta_delta` such that

```text
G(delta,X)=zeta_delta A_delta(X).                  (DSB10)
```

Hence all these parameter fibers have exact degree `p-3` and split
completely over `U_0`.

For the official row, the bidegree and guaranteed split counts are

```text
(e-2,p-3)=(183251937961,274877906941),
split domain rows >=824633720829+d_A,
split parameter fibers >=183251937969+d_A.          (DSB11)
```

## Scope

The theorem constructs the lower-degree split biform but does not classify
or exclude it. The possible exceptional coordinate when `d_A=0` is not
claimed to have all of its parameter roots in the supported set.
