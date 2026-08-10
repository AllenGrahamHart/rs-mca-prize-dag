# Cycle 70: clean Picard--Forney endpoint close (2026-08-11)

## Cycle pins

```text
our start:       28f6ab4b6
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   11 PRs; no new overlap
critical open:   28
```

## Maximal Forney contact

On the domain-infinity chart put `u=X^(-1)`. The reciprocal locator and
homogenized Forney numerator are

```text
q^vee(z;u)=u^rho Q(z;u^(-1)),
N(z;u)=u^(rho-1)P(z;u^(-1)).
```

The full rectangular Hankel matrix has `rho+2` kernel rows. Therefore the
coefficients of

```text
q^vee(z;u)sum_(i=0)^(2rho+1)y_i(z)u^i
```

from `u^rho` through `u^(2rho+1)` all vanish, while the lower coefficients
are exactly `N`. On `C:Q=0`, this proves

```text
div_C(P)>=(2rho+2)H_X.
```

The normalized resultant makes the restricted section nonzero. Removing
the contact gives a nonzero section of

```text
L_F=O_C(-rho-3,m+1),       deg L_F=m-1.
```

The exact `m=1`, `F_17` pencil independently replays every vanished
convolution coefficient and detects the first permitted tail at order
`2rho+2=8`.

## Picard contradiction

The existing two-axis theorem supplies the effective point class

```text
O_C(P_*)=O_C(N,-T).
```

At `rho=4m-1`, `N=16m`, and `T=4m+1`,

```text
L_F^4 tensor O_C(P_*)=O_C(-8,3).
```

The two nonzero sections would therefore produce a nonzero section of the
right side. But restriction from `P^1_X x P^1_z` gives

```text
0 -> O(-rho-8,3-m) -> O(-8,3) -> O_C(-8,3) -> 0.
```

For `m>3`, both `H^0(O(-8,3))` and
`H^1(O(-rho-8,3-m))` vanish, the latter directly by Kunneth. Hence
`H^0(C,O_C(-8,3))=0`, a contradiction. No smoothness assumption is used.

The proved node is
`rate_half_ca_hankel_clean_endpoint_picard_forney_contact_exclusion`.

## Burn-down

```text
result:                  CLOSED the strict e=m, O=0 endpoint branch
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   none; live endpoint is now 1<=O<=m-1
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The next strict-endpoint action should transport the contact/Picard argument
to positive omission defect or prove that the defect components force enough
degree loss to restore a comparable forbidden low-bidegree section. The
clean branch should no longer receive computation or separate casework.
