# Clean-endpoint four-Hankel bi-isotropic frame

- **status:** PROVED
- **closure:** exact minimal-kernel coefficient chain
- **consumer:** `rate_half_band_crossing_location`

Retain the clean boundary-saturated endpoint and choose the affine parameter
coordinate so that `0` and infinity are generic-rank pencil values, the
constant and top `X`-coefficients of both endpoint locators are nonzero, and
the normalization used for `q_inf` remains valid. Write

```text
M(z)=M^(0)+zM^(1),
Q(z;X)=sum_(j=0)^m z^j Q_j(X),
q_j=coefficient vector of Q_j in Fbar^(rho+1),
W_Q=span{q_0,...,q_m}.                              (FHB1)
```

Then

```text
dim W_Q=m+1.                                         (FHB2)
```

For `epsilon in {0,1}` and `s in {0,1}`, define the adjacent square Hankel
blocks

```text
H_(epsilon,s)=(y^(s)_(a+b+epsilon))_(0<=a,b<=rho).  (FHB3)
```

All four endpoint forms have rank `rho` and exact radicals

```text
ker H_(epsilon,0)=span{q_0},
ker H_(epsilon,1)=span{q_m}.                         (FHB4)
```

The coefficient plane is simultaneously totally isotropic for all four:

```text
q_i^T H_(epsilon,s) q_j=0
for 0<=i,j<=m, epsilon,s in {0,1}.                  (FHB5)
```

In particular the infinity polynomial in the resultant theorem is

```text
q_inf(X)=Q_m(X),                                    (FHB6)
```

and its coefficient vector is the common radical line of the two infinity
Hankel blocks.

If the endpoint syndrome sources are written

```text
y^(s)_ell=sum_(x in D) omega_x^(s)x^ell
```

and `v_x=(Q_0(x),...,Q_m(x))^T`, then `(FHB5)` is equivalently the four exact
rank-one frame cancellations

```text
sum_x omega_x^(s) v_x v_x^T=0,
sum_x x omega_x^(s) v_x v_x^T=0       for s=0,1.    (FHB7)
```

For every saturated point `x!=x_0`, `v_x` is a nonzero scalar multiple of
the coefficient vector of its supported degree-`m` root locator; at `x_0`
it is the coefficient vector of `A_0S`.

## Scope

This is the exact Hankel interface missing from the general resultant gate.
It does not classify common bi-isotropic planes or prove that `(FHB5)` is
incompatible with `(RBS2)--(RBS6)`.
