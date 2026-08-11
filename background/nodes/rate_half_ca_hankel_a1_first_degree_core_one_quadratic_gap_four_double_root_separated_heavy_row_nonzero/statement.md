# `A=1` quadratic separated heavy row is nonzero

- **status:** PROVED
- **closure:** exclusion of the zero heavy row on the complete separated double-root locus
- **consumer:** `rate_half_band_crossing_location`

Retain the separated double-root extremal profile:

```text
S_B squarefree,       gcd(g_*,S_B)=1,
Q(t,x_*)=a_Q g_*(t)S_B(t)^3,
E_4=c_E S_B^2,       a_Q c_E!=0.                   (HSN1)
```

There is no restriction on overlap between the correction quadratic and the
three center lines. Then

```text
G(t,x_*)!=0.                                        (HSN2)
```

For the center-overlap factorization

```text
J=gcd(Lambda,g_*S_B^2),       j=deg J<=3,
G(t,x_*)=(g_*S_B^2/J)T_j,
```

this says `T_j` is a nonzero form for every `j=0,1,2,3`. Consequently, if a
connected-weld candidate passes the row coefficient gate, its barycentric
remainder satisfies

```text
R_lambda(t)=G(t,x_*)!=0.                            (HSN3)
```

## Scope

This rules out only the zero heavy row. It does not prove the remainder
divisibility needed for a connected-weld candidate to pass, nor does it
exclude a nonzero passing row. Nonreduced `S_B` and roots shared by `S_B`
and `g_*` remain outside the inherited separated hypotheses.
