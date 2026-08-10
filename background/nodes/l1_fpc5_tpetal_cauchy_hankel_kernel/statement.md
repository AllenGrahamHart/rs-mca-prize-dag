# FPC5 Cauchy-Hankel kernel

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Use the owner-free Cauchy divisor chart and put

```text
c=h-d-1,       e=2d+1-h,                              (HK1)
mu_s=sum_(z in T)c(z)z^s/Lambda'(z),       s>=0.      (HK2)
```

Write `G(X)=sum_(a=0)^d g_a X^a`. Then the complete low-numerator condition
is exactly

```text
H_mu g=0,
H_mu=(mu_(j+a))_(0<=j<c,0<=a<=d).                    (HK3)
```

Thus `H_mu` is a `c` by `d+1` Hankel matrix. If the pair slice contains a
saturated primitive monic anchor, then

```text
rank H_mu=c,       dim ker H_mu=e+1.                  (HK4)
```

The moments are canonical: at infinity,

```text
chi(X)/Lambda(X)=sum_(s>=0) mu_s X^(-s-1).            (HK5)
```

If

```text
Lambda=X^h+lambda_(h-1)X^(h-1)+...+lambda_0,
```

then they obey the exact order-`h` recurrence

```text
mu_(s+h)+lambda_(h-1)mu_(s+h-1)+...+lambda_0 mu_s=0
for every s>=0.                                      (HK6)
```

Consequently the core-split points in the cell are precisely the monic
degree-`d` divisors

```text
G|L_Core,       coeff(G) in ker H_mu.                 (HK7)
```

For `x in Z(G)`, write

```text
G/(X-x)=sum_(a=0)^(d-1) q_a X^a.
```

The primitive guard is exactly

```text
sum_(a=0)^(d-1) mu_a q_a!=0                          (HK8)
```

at every root `x`. The background equations remain the explicit Cauchy
tests from the incoming theorem.

## Scope

This theorem proves that the live flat is a canonical full-rank
Padé-Hankel kernel, not an arbitrary affine subspace. It does not bound its
split divisors, prove Hankel-kernel flatness, absorb the background guards,
or pay first-owner chronology.
