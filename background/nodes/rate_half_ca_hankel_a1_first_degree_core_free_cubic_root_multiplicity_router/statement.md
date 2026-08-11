# `A=1` core-free cubic residual-root multiplicity router

- **status:** PROVED
- **closure:** exact incidence/new-root capacity split
- **consumer:** `rate_half_band_crossing_location`

Retain the core-free first-degree scalar profile with residual degree `a=3`.
Put

```text
Delta=2e-1,
u=Delta-I_H,       v=Delta-O.                        (CRM1)
```

Then

```text
u+v=e+1,       0<=I_0<=u.                            (CRM2)
```

Let `E` be the set of heavy domain rows that are roots of `R_3`, let
`r=|E|`, and put `C_E=sum_(x in E)c_x`. If `epsilon_E` is the total excess
multiplicity beyond one copy at each incidence on `E`, and `t_E` is the
number of those excess roots that are new relative to the squarefree minimal
locator, then

```text
C_E=(r-2)e+1+u+I_0,                                  (CRM3)
t_E>=e+1-2u-I_0+epsilon_E.                           (CRM4)
```

At every simple heavy root of `R_3`,

```text
t_x<=c_x+epsilon_x.                                  (CRM5)
```

Consequently, if every heavy residual root is simple,

```text
(3-r)e<=3u+2I_0<=5u.                                 (CRM6)
```

A triple-root residual can occur only when

```text
2u>=e.                                               (CRM7)
```

In particular, throughout the exact low-gap range

```text
5u<e,                                                (CRM8)
```

there are only two residual-root branches:

```text
SQUAREFREE: R_3 has three distinct heavy roots;
DOUBLE:     R_3 has one double and one simple root, both heavy. (CRM9)
```

Thus no root of `R_3` can lie outside the heavy set in `(CRM8)`, and the
triple-root branch is empty there.

## Scope

The theorem routes but does not exclude the squarefree and double-root
branches. It makes no assertion for `5u>=e` or scalar degrees `4,5`.
