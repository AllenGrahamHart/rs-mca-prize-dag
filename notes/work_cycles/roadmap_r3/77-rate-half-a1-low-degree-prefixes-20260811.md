# Cycle 77: `A=1` low-degree prefix exclusions (2026-08-11)

## Cycle pins

```text
our start:       907d222d4
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   38 PRs; no new overlap
critical open:   28
```

## Four-contact trade

Four contact copies make the ambient target's domain degree `-s-1`. This
permits a pole-clearing form of bidegree `(3,floor(p/4))`: its domain degree
is still too small to contain a contact-active component when
`3(e+1)<rho+1`. The restriction-kernel bundle is

```text
O(-rho-1,floor(p/4)-e+ell+4-beta).
```

It has zero `H^1` whenever

```text
floor(p/4)+ell+4-beta<e.
```

## Official prefixes

Using only `p<=Delta` and maximal slope slack excludes

```text
s=0: m+1<=e<=floor(12m/11)-1,
s=1: m+1<=e<=floor(6m/5)-1.
```

For `m=2^37`, the first unexcluded degrees are respectively
`149933403787` and `164926744166`. The prior `e=m+1` core-free chambers are
therefore empty. The proved node is
`rate_half_ca_hankel_a1_four_contact_low_degree_exclusion`.

## Burn-down

```text
result:                  CLOSED explicit initial degree prefixes for s=0,1
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The remaining `A=1` ranges now begin at `floor(12m/11)` for `s=0` and
`floor(6m/5)` for `s=1`; `s=2` is closed.
