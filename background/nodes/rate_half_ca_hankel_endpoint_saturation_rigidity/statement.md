# Endpoint saturation rigidity for the strict `A=3` Hankel profile

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

Retain the strict-budget `A=3` notation from
`rate_half_ca_hankel_exceptional_root_charge`, and specialize to the first
unresolved parameter degree:

```text
m>=1,       rho=4m-1,       N=16m,       A=3,
e=m,        s=0,            delta=rho-3e=m-1.          (SAT1)
```

Let `Z` be the set of finite supported slopes and `T=|Z|`.  For
`gamma in Z`, let

```text
c_gamma=rho-rank M(gamma)
```

and let `u_gamma` be the number of distinct evaluation-domain roots of the
specialized generic apolar generator `Q_gamma`.  Put

```text
O=sum_(gamma in Z) (rho-u_gamma).
```

Then

```text
0<=O<=sum_(gamma in Z)c_gamma<=delta=m-1.              (SAT2)
```

If the strict target `T<=rho+1=4m` fails, the failure has only one possible
size:

```text
T=4m+1=rho+2.                                          (SAT3)
```

For each `x` in the evaluation domain, let

```text
d_x=|{gamma in Z: Q_gamma(x)=0}|.
```

Every `Q_Z(x)` is a nonzero parameter polynomial of degree at most `m`, so
`d_x<=m`.  Under `(SAT3)` the exact deficit identity is

```text
sum_(x in D)(m-d_x)=1+O<=m.                            (SAT4)
```

Consequently at least

```text
N-(1+O)>=15m=15N/16                                   (SAT5)
```

domain points are **parameter-saturated**: `d_x=m`.  At every such point,
`Q_Z(x)` has parameter degree exactly `m`, all its parameter roots are
distinct finite members of `Z`, and `Q_Z(x)` divides the squarefree
parameter polynomial

```text
H_Z(Z)=product_(gamma in Z)(Z-gamma).
```

Thus the first strict endpoint is no longer an arbitrary core-free
split-divisor curve.  Any counterexample must be a unique extremal
`(4m+1) x (16m)` incidence configuration in which at least fifteen
sixteenths of the domain columns exhaust their full degree-`m` parameter
capacity.

This theorem does **not** exclude that extremal configuration and does not
close the strict `e=m` endpoint.  It converts that endpoint into a
near-saturated divisor-selection problem; the remaining values `e>m` and all
residual `A=1` rows are outside this statement.
