# Cycle 72: strict `A=3` single-corner reduction (2026-08-11)

## Cycle pins

```text
our start:       fa77ab766
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   11 PRs; no new overlap
critical open:   28
```

## General moving-degree contact

For every failing strict profile with moving degree `e`, the full Hankel
recurrence gives a nonzero section

```text
s_F in H^0(C,O_C(-rho-3,e+1)),
deg_C s_F line bundle=rho-3e=delta.
```

The curve is reduced: there are at least `3e+2` generic squarefree split
fibres, more than the parameter degree available to hide a repeated factor.
Primitivity and the core-free condition rule out one-coordinate components.

## Slope-slack exclusion

For `T=4e+1-h`, the pole scheme of `G(X)/H(z)` has length at most
`O<=delta`. Put

```text
ell=floor(delta/2).
```

The surface space `H^0(O(1,ell))` has dimension `2(ell+1)>delta`, so one
biform clears every pole. On any component where `s_F` is nonzero, the
contact line bundle has nonnegative degree; such a component cannot have
domain degree one. The clearing biform is therefore nonzero there.

Three contact copies and the cleared grid section produce a nonzero section
of

```text
O_C(rho-4,-e+ell+h+2).
```

If `ell+h+2<e`, the ambient bundle has no sections and its restriction
kernel has bidegree `(-4,negative)`, whose `H^1` vanishes. This excludes the
profile.

## Official survivor

Write the official `m=2^37` as `m=3q+2`. Exact integer reduction shows every
allowed `(e,h)` satisfies the strict inequality except

```text
e=floor(rho/3)=(4m-2)/3,
delta=1,
h=e-2,
T=rho+2=4m+1.
```

This corner has `O<=1` and total rank loss at most one. It is the only
remaining strict `A=3` profile.

The generalized proved node is
`rate_half_ca_hankel_endpoint_forney_infinity_contact_section`; the new
proved node is
`rate_half_ca_hankel_strict_a3_slope_slack_contact_exclusion`.

## Burn-down

```text
result:                  NARROWED all strict A=3 failures to one corner
DAG delta:               +1 PROVED leaf, net +2 edges after scope expansion
critical status delta:   none
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The next strict action should attack only the pinned corner
`delta=1,T=rho+2,e=floor(rho/3)`. Broad `e>m` sweeps, separate slope-slack
tables, and further work on the already closed `e=m` endpoint have zero
remaining value.
