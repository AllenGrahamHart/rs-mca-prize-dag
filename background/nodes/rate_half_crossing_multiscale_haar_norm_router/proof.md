# Proof

## 1. Shared Haar energy

Write

```text
Q_(j,u)=A_(j,u)+A_(j,u+N_j/2).
```

The next fold is `A_(j+1,u)=Q_(j,u)`.  The parallelogram identity gives

```text
sum_(u<N_j) A_(j,u)^2
 = (1/2)E_j+(1/2)sum_(u<N_(j+1))A_(j+1,u)^2.         (1)
```

Divide the identity after the `j`th fold by `2^j` and telescope.  The
initial square sum is `r`, while the terminal fold is the single value `r`
and contributes `r^2/n`.  This proves `(MH2)`.

## 2. One norm at each active scale

Since `zeta_(N_j)^(N_j/2)=-1`, folding the evaluation gives

```text
beta_j=sum_(u<N_j/2) eps_(j,u) zeta_(N_j)^u.         (2)
```

The right side has degree below `phi(N_j)=N_j/2`.  Hence `beta_j=0` over
the cyclotomic field if and only if every `eps_(j,u)` is zero.  Odd-frequency
orthogonality gives

```text
sum_(t mod N_j, t odd)|sigma_t(beta_j)|^2
  =(N_j/2)E_j.
```

AM-GM over the `N_j/2` embeddings therefore yields

```text
|Norm(beta_j)|<=E_j^(N_j/4).                         (3)
```

Because `p=1 mod n`, it splits completely at every order `N_j`.  The
moment equations with indices `2^j t<w`, `t` odd, put `beta_j` in `c_j`
distinct primes above `p`.  Thus

```text
p^c_j divides |Norm(beta_j)|                         (4)
```

whenever `beta_j` is nonzero.

## 3. Exact payment for zero scales

If `z` is an inactive scale, equation `(2)` and Gauss division give
`Phi_(N_z)|F` in `Z[X]`.  The inactive dyadic cyclotomic polynomials are
pairwise coprime, so their product divides `F`.  At a distinct active order
`N_j`, direct evaluation gives

```text
|Norm_(Q(zeta_(N_j))/Q)(Phi_(N_z)(zeta_(N_j)))|
  =2^(min(N_j,N_z)/2).                               (5)
```

Multiplying `(4)` and `(5)` over the active scales proves the divisibility
in `(MH4)`.  Multiplying `(3)` gives its first upper bound.

For the last bound, put

```text
x_j=E_j/2^(j+1),       lambda_j=a_j/A_J.
```

By `(MH2)`, `sum_(j in J)x_j<=r-r^2/n`.  Weighted AM-GM gives

```text
product_(j in J)(x_j/lambda_j)^a_j
 <=(r-r^2/n)^A_J.
```

Since `2^(j+1)a_j=n/2` at every scale, restoring the powers of two yields
exactly

```text
product_(j in J)E_j^a_j
 <=(n(r-r^2/n)/(2A_J))^A_J.
```

This completes `(MH4)`.  The empty-pattern statement follows from the
zero criterion after `(2)` and the standard dyadic Haar reconstruction.

## 4. The all-active route fence

For `w=2^v`, the odd indices at scale `j<v` number
`c_j=2^(v-j-1)`.  Hence

```text
C_J=sum_(j=0)^(v-1)c_j=w-1,
A_J=sum_(j=0)^(v-1)n/(4*2^j)=n(w-1)/(2w).
```

There are no zero-scale powers of two.  Substitution in `(MH4)` gives
`(MH5)`.  At `n=2^41`, `r=n/2-w`, the quantity

```text
r-r^2/n=n/4-w^2/n
```

is an integer.  The verifier checks the equivalent exact integer comparison

```text
2^256 (w-1)^d <= ((n/4-w^2/n)w)^d,
d=n/(2w),
```

at `w=2^37`, and its strict reverse at `w=2^38`.  No floating-point
comparison enters the claim.  Since every official `p<2^256`, the
`w=2^37` gate cannot fire.  This is a limitation of this norm-product
certificate, not an existence theorem for an accidental window.  QED.
