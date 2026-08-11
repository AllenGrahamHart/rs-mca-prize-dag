# Cycle 86: first tangent packet pushforward dichotomy (2026-08-11)

## Cycle pins

```text
our start:       d09bd9557
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
compute:         none
critical open:   28
```

## Rank-two modification

The two effective Picard points lie above the same domain coordinate and
give an exponent-`(1,1)` elementary modification of

```text
pi_*O_C=O direct_sum O(-d)^(e-1).
```

Projection of the two modification directions to the negative block has
rank one or two. These give exactly

```text
PENCIL:    O(1) + O(1-d) + O(-d)^(e-2),       h^0=2;
CANONICAL: O + O(1-d)^2 + O(-d)^(e-3),        h^0=1.
```

The first branch has a degree-at-most-two pencil after removing base
points; the second has only the canonical two-point section. The proved
leaf is
`rate_half_ca_hankel_a1_first_degree_core_one_two_point_pushforward_dichotomy`.

## Burn-down

```text
result:                  REDUCED first tangent packet to two Picard splittings
DAG delta:               +1 PROVED leaf, +1 req edge, +1 ev edge
critical status delta:   none
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next use the Hankel frame to attack the pencil and unique-section branches;
do not substitute generic multiplication-map injectivity.
