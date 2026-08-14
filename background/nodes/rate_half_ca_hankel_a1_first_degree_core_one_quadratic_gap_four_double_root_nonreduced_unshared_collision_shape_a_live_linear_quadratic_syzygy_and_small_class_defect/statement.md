# `A=1` shape-A live linear/quadratic syzygy and small-class defect

- **status:** PROVED
- **closure:** every live syzygy bundle has only degrees one and two, and
  each small source class forces one exact barycentric defect form
- **consumer:** `rate_half_band_crossing_location`

Retain Shape A with `r=sr(G)` in the live interval

```text
(e+1)/2<=r<=e-1.                                   (LQD1)
```

Let `V subset S_(e-2)` be the parameter coefficient space and let
`(c_1,c_2,c_3)` be its syzygy-bundle profile. Then the profile is uniquely
determined by `r`:

```text
c_1=2r-e,
c_2=e-r-1,
c_3=0.                                             (LQD2)
```

In particular,

```text
E=O(-1)^(2r-e) direct_sum O(-2)^(e-r-1),           (LQD3)
S_1 V=S_(e-1).                                     (LQD4)
```

At the lower boundary `r=(e+1)/2`, this is the unique profile

```text
(c_1,c_2,c_3)=(1,91625968980,0).                   (LQD5)
```

There is also an exact domain-coefficient defect. Choose a minimal
presentation

```text
G(t,X)=sum_(j=1)^r A_j(t)B_j(X),
W_X=span{B_1,...,B_r} subset F[X]_(<=n).           (LQD6)
```

For each of the two source classes `M_gamma` of size `n+2`, the
locator-interpolation projection

```text
T_gamma:S_n -> V                                  (LQD7)
```

has exact rank `r-1`. Consequently there is a unique projective nonzero
form `B_gamma in W_X` such that, for every `x in M_gamma`,

```text
B_gamma(x)
 =kappa_gamma eta_x L_U0'(x)^2/L_Mgamma'(x)
 =kappa_gamma eta_x L_Mgamma'(x)L_rest,gamma(x)^2, (LQD8)
```

where `kappa_gamma!=0` and

```text
L_U0=L_Mgamma L_rest,gamma.                        (LQD9)
```

Thus `B_gamma` is nonzero at every point of its own source class.

## Scope

The theorem does not exclude the linear/quadratic profile or the two defect
forms. The next route is to compare the two defects through the common
coefficient space `W_X`, the split row locators, or the collision/Hankel
identities.
