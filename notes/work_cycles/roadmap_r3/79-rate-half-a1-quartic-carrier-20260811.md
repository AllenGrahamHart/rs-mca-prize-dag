# Cycle 79: `A=1` core-one quartic-carrier exclusion (2026-08-11)

## Cycle pins

```text
our start:       6094d39b8
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   38 PRs; no new overlap
critical open:   28
```

## Degree-four pole clearing

On the core-one branch, a form of bidegree `(4,floor(p/5))` clears the pole
scheme. Four contact copies then land in

```text
O_C(-1,floor(p/5)+ell+3),
```

which has no sections when `floor(p/5)+ell+3<e`.

Unlike the degree-three proof, a degree-four clearing form can contain a
contact-active component. Contact degree forces such a component to have
bidegree exactly `(4,1)`. There can be only one. Every other component is
contact-inactive and therefore divides the Forney numerator. Cancelling
their product from the full recurrence produces a degree-four rational
kernel vector, contradicting the unique primitive kernel degree
`d=rho-1`.

## Official prefix

Using `p<=Delta` and maximal slope slack closes

```text
m+1<=e<=floor(16m/13)-1.
```

For `m=2^37`, the first unexcluded core-one degree is now
`169155635042`. The proved leaf is
`rate_half_ca_hankel_a1_core_one_quartic_carrier_exclusion`.

## Burn-down

```text
result:                  CLOSED a larger core-one degree prefix
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The remaining `A=1` ranges begin at `floor(12m/11)` for `s=0` and
`floor(16m/13)` for `s=1`; every survivor has positive slope slack.
