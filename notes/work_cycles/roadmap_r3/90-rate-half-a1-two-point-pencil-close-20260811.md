# Cycle 90: first tangent packet loses its pencil branch (2026-08-11)

## Cycle pins

```text
our start:       21e8796c5
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
open upstream:   39 PRs; #1160 is a local 2w MCA repair, no packet overlap
compute:         none
critical open:   28
```

## Fibre-algebra direction

At each of the two doubled roots, write `t=X-x_*=unit*s^2`. The elementary
modification direction is `t/s=s`, the nilpotent class in that double local
factor. Both directions vanish on the other `e-4` fibre factors, while the
constant class is nonzero there. Their span therefore has zero intersection
with the constant line and rank-two projection to the negative block.

The PENCIL splitting is excluded. The only possible pushforward is

```text
O direct_sum O(1-d)^2 direct_sum O(-d)^(e-3),
```

so the effective two-point line bundle has exactly one section. The proved
leaf is
`rate_half_ca_hankel_a1_first_degree_core_one_two_point_pencil_branch_exclusion`.

## Upstream reconciliation

The local upstream checkout advanced to `fde7d56d0`; `agents.md` still says
no adjacent MCA or LIST row is closed. The integrated cyclic rate-half result
is a finite-family ordinary-list lower construction, not MCA safety. New PR
`#1160` repairs a support-wise near-rational charge to `2w`; it has no direct
overlap with the first-degree Hankel packet geometry.

## Burn-down

```text
result:                  CLOSED first packet's two-section Picard branch
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next attack the unique-section branch using the cubic Forney quotient and
the two doubled row roots, while classifying the other five bounded packets.
