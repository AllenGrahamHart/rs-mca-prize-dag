# `A=1`, core-one maximal-degree component localization

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger`

Retain the half-distance `A=1` family with

```text
m>=2,       rho=4m,       N=16m,
s=1,       e=2m-1,       d=rho-s=4m-1=2e+1.          (C1M1)
```

Assume the sharp-cap face of the residual router:

```text
Delta=d-2e=1,       T=T_max=4e+1=8m-3,
eta=e,       0<=O<=1,       C=e-1+O<=e.              (C1M2)
```

Factor the residual generator over the algebraic closure, with multiplicity,

```text
Qbar=product_i Q_i,
(r_i,e_i)=(deg_X Q_i,deg_(U,V)Q_i).                  (C1M3)
```

Every factor has positive bidegree. There is a unique component `Q_*` with

```text
r_*=2e_*+1,                                           (C1M4)
```

and every other component is balanced at slope two:

```text
r_i=2e_i.                                             (C1M5)
```

If

```text
b=sum_(i!=*)e_i=e-e_*,
```

then the residual components consume five units of the exact column-defect
budget per parameter degree:

```text
5b<=C-E<=e,       b<=floor(e/5),
e_*>=e-floor(e/5).                                    (C1M6)
```

Here `E` is the overlap excess of the component incidence sets, and
`0<=E<=O<=1`. The full residual generator has separation rank `e+1`, so

```text
sr(Q_*)>=ceil((e+1)/(b+1)).                           (C1M7)
```

For the official value `m=2^37`, one has `e=2^38-1=3 mod 5`, and therefore

```text
b<=54,975,581,388,
e_*>=219,902,325,555,
r_*>=439,804,651,111,
sr(Q_*)>=5.                                           (C1M8)
```

Thus every separated pullback and every separation-rank-one through
separation-rank-four model is excluded for the dominant component on this
face. If `b=0`, then `Q_*=Qbar` and `sr(Q_*)=e+1` exactly.

The residual generator is geometrically squarefree. At least

```text
T-1=8m-4                                             (C1M9)
```

supported slopes split every component over `D\S`, and at least

```text
(N-1)-e=14m                                          (C1M10)
```

residual domain rows split every component over the supported-slope set.
This theorem excludes low-rank component models but does not exclude the
rank-at-least-five dominant component or close the stratum.
