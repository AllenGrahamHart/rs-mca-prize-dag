# `A=1` core-one quadratic residual-root multiplicity router

- **status:** PROVED
- **closure:** uniform first-fifth heavy-root dichotomy
- **consumer:** `rate_half_band_crossing_location`

Retain the core-one first-degree parameter-constant profile with scalar
residual degree `a=2`. Put

```text
Delta=e-2,
u=Delta-I_H,       v=Delta-O.                        (QRM1)
```

Then

```text
u+v=e+2,       O=u-4,       4<=u<=e-2,       I_0<=u. (QRM2)
```

Let `E` be the set of heavy rows at roots of the residual quadratic, let
`r=|E|`, and put `C_E=sum_(x in E)c_x`. If `epsilon_E` is the excess
multiplicity beyond one copy at each incidence on `E`, and `t_E` is the
number of those excess roots outside the squarefree minimal locators, then

```text
C_E=(r-1)e+2+u+I_0,                                  (QRM3)
t_E>=e+2-2u-I_0+epsilon_E.                           (QRM4)
```

At every simple heavy root of the residual quadratic,

```text
t_x<=c_x+epsilon_x.                                  (QRM5)
```

Consequently, if all heavy residual roots are simple,

```text
(2-r)e<=3u+2I_0<=5u.                                 (QRM6)
```

In particular, throughout

```text
5u<e,                                                (QRM7)
```

there are exactly two possible residual-root patterns:

```text
DOUBLE:     one double heavy root;
SQUAREFREE: two distinct heavy roots.                (QRM8)
```

Thus no squarefree residual root lies outside the heavy set for

```text
4<=u<=36650387592.                                   (QRM9)
```

## Scope

The theorem routes but does not exclude either pattern. It makes no claim
for `5u>=e`, the core-free scalar degrees, or parameter-dependent residual
biforms.
