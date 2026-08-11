# Cycle 81: `A=1` Forney pole absorption (2026-08-11)

## Cycle pins

```text
our start:       ff2c84c83
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   38 PRs; no new overlap
critical open:   28
```

## Exact pole absorption

On a supported residual fibre, the contracted split recurrence factor
divides both the generic locator and residual domain locator:

```text
Qbar=Q_min R,       G=Q_min G_1.
```

The recurrence numerator satisfies `N_F=R N_min`. Hence `Qbar|N_FG` in the
full fibre algebra, which is the scheme-theoretic membership

```text
N_F in (H:G).
```

The proved leaf is
`rate_half_ca_hankel_a1_forney_pole_ideal_absorption`.

## Direct three contacts

One contact copy now cancels every pole of `G/H`. Three copies yield

```text
s_F^3G/H in H^0(C,O_C(d-3,ell-e+3-beta)).
```

The restriction sequence has no sections when the second coordinate is
negative. Therefore every survivor obeys

```text
ell>=e-3+beta.
```

On the official row, both live core ranges now begin at

```text
e_0=ceil((rho-1)/3)=183251937963.
```

At `e_0`, each core has three slacks and the common slope counts
`T in {rho+2,rho+3,rho+4}`. The proved leaf is
`rate_half_ca_hankel_a1_direct_three_contact_exclusion`.

## Burn-down

```text
result:                  CLOSED both A=1 prefixes through e_0-1
DAG delta:               +2 PROVED leaves, +4 req edges, +2 ev edges
critical status delta:   none
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The earlier cubic-residual corner is no longer live. Next attack the six
boundary profiles at `e_0`, preserving the core and slope-count split.
