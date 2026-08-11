# `A=1` quadratic separated correction-center disjointness and overlap cap one

- **status:** PROVED
- **closure:** reduction of the separated heavy-row gate to at most two scalar coefficients
- **consumer:** `rate_half_band_crossing_location`

Retain the separated double-root extremal profile and its three assigned
centers. Then the correction quadratic is disjoint from every center:

```text
gcd(S_B,Lambda)=1.                                  (HOD1)
```

Moreover,

```text
J=gcd(Lambda,g_*S_B^2)=gcd(Lambda,g_*),
j=deg J<=1.                                         (HOD2)
```

Consequently the heavy row has the exact form

```text
G(t,x_*)=(g_*S_B^2/J)T_j,
T_j!=0,       deg T_j<=1,       gcd(T_j,S_B)=1.     (HOD3)
```

At each correction root `tau`,

```text
ord_tau G(t,x_*)=2.                                 (HOD4)
```

Thus the augmented barycentric remainder gate introduces at most two scalar
coefficients, not three or four.

## Scope

The theorem does not exclude the residual `j=0` or `j=1` nonzero remainder
cases. A center may still be a root of `g_*`, corresponding to the unique
allowed padded-heavy assigned center. Nonreduced and shared correction loci
remain outside the separated hypotheses.
