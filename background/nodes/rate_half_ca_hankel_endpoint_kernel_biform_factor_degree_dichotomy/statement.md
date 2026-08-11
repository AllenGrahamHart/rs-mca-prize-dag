# Endpoint kernel-biform factor-degree dichotomy

- **status:** PROVED
- **closure:** the strict endpoint kernel biform has one dominant
  parameter-irreducible factor
- **consumers:** `rate_half_band_closure`,
  `rate_half_band_crossing_location`

Retain the strict `A=3,e=m` endpoint and its saturation-failure profile:

```text
m>=1,       rho=4m-1,       N=16m,       T=4m+1,
0<=O<=m-1.                                             (KFD1)
```

Let the primitive kernel biform have parameter degree `m` and domain degree
at most `rho):

```text
Q(Z,X)=c(X) product_j Q_j(Z,X),                       (KFD2)
```

where the `Q_j` are primitive irreducibles over `F_q(X)). Put

```text
m_j=deg_Z Q_j,       d_j=deg_X Q_j.                  (KFD3)
```

Then

```text
sum_j m_j=m,       sum_j d_j<=rho,
T*rho-O <= sum_j min(T*d_j,N*m_j).                  (KFD4)
```

Call a factor small when `T*d_j<N*m_j). There is exactly one small
factor. If its parameter degree is `m_1), then

```text
m_1>=ceil((3m+1)/4).                                (KFD5)
```

Consequently:

1. for every `m>=2`, `Q` does not split into parameter-linear factors
   over `F_q(X));
2. for `m in {2,3,4}`, `Q` is irreducible over `F_q(X));
3. at the official `m=2^37`, one irreducible factor has parameter degree

```text
at least 103079215105=3*2^35+1.                     (KFD6)
```

## Scope

This is a factor-profile restriction, not an endpoint exclusion. It does not
prove that the surviving dominant factor is incompatible with the
multiplicative evaluation domain, Hankel origin, or norm/Bezout identities.
