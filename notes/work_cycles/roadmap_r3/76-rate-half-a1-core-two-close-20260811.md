# Cycle 76: `A=1` fixed-core-two closure (2026-08-11)

## Cycle pins

```text
our start:       e53cc6f71
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   38 PRs; no new overlap
critical open:   28
```

## Contracted contact

After stripping a fixed core of size `s`, the residual generator has degree
`d=rho-s`, while the contracted Hankel matrix still has `rho` rows. Its
Forney numerator has contact order `d+rho` and yields

```text
s_F in H^0(C,O_C(-rho-1,e+1)),
deg L_F=d-(s+1)e=Delta.
```

The proved leaf is
`rate_half_ca_hankel_a1_core_stripped_forney_contact_section`.

## Fixed-core exclusion

For `s=1,2`, a form of bidegree `(2,floor(p/3))` clears the pole scheme and
cannot contain a contact-active component. Three contact copies exclude

```text
floor(p/3)+ell+3-beta<e,
beta=T_max-4e.
```

This removes the first `s=1` degree `e=m+1`. For `s=2`, the inequality holds
throughout the complete integer range, including the boundary
`Delta=0,beta=2`; hence the entire core-two branch is impossible. The proved
leaf is `rate_half_ca_hankel_a1_fixed_core_pole_slack_exclusion`.

## Burn-down

```text
result:                  CLOSED the complete A=1 fixed-core-two branch
DAG delta:               +2 PROVED leaves, +4 req edges, +2 ev edges
critical status delta:   none; s=0 and higher s=1 remain
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next attack the higher `s=1` survivors subject to
`p>=3(e-ell-2)`, alongside the finite-deficiency first core-free chambers.
