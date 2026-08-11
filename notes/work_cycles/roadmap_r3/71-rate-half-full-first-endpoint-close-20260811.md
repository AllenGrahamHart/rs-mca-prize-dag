# Cycle 71: full first strict endpoint close (2026-08-11)

## Cycle pins

```text
our start:       5834c982d
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   11 PRs; no new overlap
critical open:   28
```

## Universal contact section

The clean contact argument does not need `O=0`. For every strict `e=m`
endpoint, all `rho+2` rows of the rectangular Hankel kernel give

```text
q^vee(z;u)sum_(i=0)^(2rho+1)y_i(z)u^i
 =N(z;u)+u^(2rho+2)R(z;u).
```

The canonical numerator `N` is nonzero by a triangular recurrence argument:
if its first `rho` coefficients vanished, the remaining kernel rows would
force every moment in the full pencil to vanish. On the reduced endpoint
curve this yields a nonzero section

```text
s_F in H^0(C,O_C(-rho-3,m+1)).
```

This section may vanish on some components, but not all.

## Pole-ideal interpolation

Put

```text
G(X)=X^N-1,       H(z)=product_(gamma in Z)(z-gamma).
```

The rational grid section `G/H` has pole-cancellation ideal `J=(H:G)` on
`C`. At a supported fibre, with local equation `h`,

```text
length(O_C/(h:g))
 =length(O_C/(h))-length(O_C/(h,g))
 <=rho-u_gamma.
```

Hence

```text
d=length(O_C/J)<=O<=m-1.
```

For the official even row, let `ell=m/2-1`. The ambient space
`H^0(O(1,ell))` has dimension `m>d`, so a nonzero biform `F` can satisfy
`F|_C in J`. It clears all poles:

```text
s_G=FG/H in H^0(C,O_C(N+1,ell-T)).
```

Every endpoint component has domain degree at least four, so the
domain-degree-one form `F` cannot contain a component. Thus `s_G` is nonzero
on every component.

## Final contradiction

The reducedness of `C` makes the product `s_F^4s_G` nonzero. Its line bundle
is

```text
O_C(4(-rho-3)+N+1,4(m+1)+ell-T)=O_C(-7,ell+3).
```

But

```text
0 -> O(-rho-7,ell+3-m)
  -> O(-7,ell+3)
  -> O_C(-7,ell+3) -> 0,
ell+3-m=2-m/2<0.
```

The middle `H^0` and left `H^1` vanish, so the curve line bundle has no
section. This excludes every omission defect `0<=O<=m-1`, including all
reducible profiles.

The proved nodes are
`rate_half_ca_hankel_endpoint_forney_infinity_contact_section` and
`rate_half_ca_hankel_endpoint_residual_pole_interpolation_exclusion`.

## Burn-down

```text
result:                  CLOSED all strict A=3, e=m endpoint profiles
DAG delta:               +2 PROVED leaves, +4 req edges, +2 ev edges
critical status delta:   none; strict frontier now begins at e>m
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The next rate-half action should return to the existing `e>m` strict ledger
or the residual `A=1` profiles. The `e=m` endpoint, including every positive
omission-defect component pattern, needs no further classification or
computation.
