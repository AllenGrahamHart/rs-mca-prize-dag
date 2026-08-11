# `A=1` quadratic zero heavy row forces full correction-center overlap

- **status:** PROVED
- **closure:** localization of every zero heavy row to full correction-center overlap
- **consumer:** `rate_half_band_crossing_location`

Retain the separated double-root extremal profile:

```text
S_B squarefree,       gcd(g_*,S_B)=1,
Q(t,x_*)=a_Q g_*(t)S_B(t)^3,
E_4=c_E S_B^2,       c_E!=0.                       (HZF1)
```

For the center-overlap factorization put

```text
J=gcd(Lambda,g_*S_B^2),       j=deg J<=3,
H=g_*S_B^2/J,
G(t,x_*)=H(t)T_j(t),          deg T_j<=j.           (HZF2)
```

If the heavy row vanishes identically, then the full correction quadratic
is supported on the center divisor:

```text
G(t,x_*)=0
   => S_B divides Lambda
   => S_B divides J
   => j>=2.                                          (HZF3)
```

Equivalently,

```text
deg gcd(S_B,Lambda)<=1       => G(t,x_*)!=0.         (HZF4)
```

For a connected-weld candidate passing the row coefficient gate,
`R_lambda=G(t,x_*)`; hence a zero barycentric remainder is possible only on
the same full correction-center overlap locus.

## Scope

This does not exclude the residual cases `S_B|Lambda`, which have `j=2` or
`j=3`. Nonreduced `S_B` and supported/correction collisions remain outside
the inherited separated hypotheses. The theorem does not assert that the
connected weld exists or passes its earlier gates.
