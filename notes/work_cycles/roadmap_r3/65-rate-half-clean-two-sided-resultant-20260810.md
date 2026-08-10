# Cycle 65: clean two-sided weld and linear resultant (2026-08-10)

## Cycle pins

```text
our start:       a27208846
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   38 PRs; newest #1159 is K3 and does not overlap this route
critical open:   28
crosswalk:       passing at the start pin
```

## Dual complement and weld

On the clean branch every supported specialization `Q(gamma;X)` divides
`G=X^N-1`. Interpolating the exact quotients over the `T=4m+1` slopes gives

```text
Q A+H B=G,
deg_z B<=m-1.
```

Eliminating this identity against the banked domain complement

```text
Q V+P_sat W=H,
P_sat=(X^N-1)/(X-x_0),
```

uses `gcd(Q,P_sat)=1` and yields

```text
W B-(X-x_0)=Q K,
V B+A=-P_sat K,
deg_z K<=4m,       deg_X K<=N-1.
```

Thus `WB=X-x_0` in the function field of the remaining absolutely
irreducible curve. This is the proved node
`rate_half_ca_hankel_clean_endpoint_two_sided_complement_weld`.

## Exact resultant split

Choose parameter infinity away from the finite support, the linear norm
defect, the exceptional fibre, and the leading-`X` degree-drop set. Put
`q_inf=[z^m]Q`, and let `b,w` be the actual parameter degrees of `B,W`.
Taking the parameter resultant of the weld proves

```text
Res_z(Q,W)Res_z(Q,B)=q_inf^(w+b)(X-x_0)^m.
```

The exceptional fibre is

```text
Q(z;x_0)=c A_0(z)S(z),       deg A_0=m-1.
```

The original complement makes `A_0` divide `W(z;x_0)`; the dual complement
makes the residual factor `S` divide `B(z;x_0)`. Since the product resultant
has exact `(X-x_0)`-order `m`, the split is forced:

```text
ord_(X-x_0)Res_z(Q,B)=1,
ord_(X-x_0)Res_z(Q,W)=m-1.
```

Every other resultant factor lies on `q_inf=0`. Neither factor can be
parameter-independent: otherwise its resultant order would be divisible by
`m`. Hence

```text
1<=deg_z B<=m-1,
1<=deg_z W,
deg_z K=deg_z W+deg_z B-m>=0.
```

The proved node is
`rate_half_ca_hankel_clean_endpoint_linear_unit_resultant_gate`.

## Burn-down

```text
result:                  NARROWED
DAG delta:               +2 PROVED leaves, +1 req edge, +2 ev edges
critical status delta:   none
upstream terminal delta: none; no live PR overlaps the theorem
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The clean endpoint is now a maximal-separation-rank Hankel kernel curve
carrying a degree-`<m` element whose norm, after deleting one infinity fibre,
has one simple zero. General curves can exhibit this pattern, so the next
route-deciding theorem must couple the linear unit-resultant gate to the
Hankel/apolar coefficient identities or classify the `q_inf` boundary
allocation. No critical status changes.
