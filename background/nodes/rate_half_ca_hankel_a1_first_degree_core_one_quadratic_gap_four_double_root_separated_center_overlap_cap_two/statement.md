# `A=1` quadratic separated center-overlap cap two

- **status:** PROVED
- **closure:** exclusion of the four-scalar heavy-row overlap case
- **consumer:** `rate_half_band_crossing_location`

Retain the separated double-root extremal profile, with the three assigned
centers and endpoint union

```text
A={alpha,beta,theta},       U=S_alpha union S_beta,
sum_(gamma in A)r_gamma<=1.                         (HOC1)
```

The fixed heavy root `x_*` lies outside `U`, and

```text
Q(t,x_*)=a_Q g_*(t)S_B(t)^3,
gcd(g_*,S_B)=1.                                     (HOC2)
```

Then

```text
deg gcd(S_B,Lambda)<=1,
deg gcd(g_*,Lambda)<=1,                             (HOC3)
```

where `Lambda=ell_alpha ell_beta ell_theta`. Consequently

```text
J=gcd(Lambda,g_*S_B^2),       j=deg J<=2.           (HOC4)
```

Thus the separated heavy-row factorization has

```text
G(t,x_*)=(g_*S_B^2/J)T_j,
deg T_j<=2,       gcd(T_j,S_B)=1,       T_j!=0.     (HOC5)
```

The augmented heavy row introduces at most three scalar coefficients, not
four.

## Scope

The theorem does not exclude `j=0,1,2` or prove failure of the nonzero
barycentric remainder gate. It uses the endpoint ordering in `(HOC1)`;
`theta` is the only center which can also be a correction root. Nonreduced
and supported/correction-collision loci remain outside the separated
hypotheses.
