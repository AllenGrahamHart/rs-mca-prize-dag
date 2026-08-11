# Cycle 82: `A=1` bounded first-degree residuals (2026-08-11)

## Cycle pins

```text
our start:       1b5afe92c
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   38 PRs; no new overlap
critical open:   28
```

## Ambient boundary lift

For the three slacks of each core, put `j=ell-e+3-beta`. The direct contact
section extends uniquely to

```text
A_j in H^0(O(d-3,j)),       j in {0,1,2}.
```

At each residual domain row, the degree-`c_x=e-d_x` missing-root factor
`Qbar(x)/gcd(Qbar(x),H)` divides `A_j(x)`. Therefore every row with
`c_x>j` is a common split domain factor of `A_j`. The proved leaf is
`rate_half_ca_hankel_a1_first_degree_ambient_defect_factorization`.

## Bounded residual table

Let `B_j` be the product of all heavy rows. Exact capacity bounds its
complementary domain degree by

```text
                 j=0     j=1     j=2
s=0:             5       12      18
s=1:             2       9       15.
```

Thus `A_j/B_j` has one of the six bidegrees

```text
(5,0), (12,1), (18,2), (2,0), (9,1), (15,2).
```

The proved leaf is
`rate_half_ca_hankel_a1_first_degree_bounded_residual_table`.

## Burn-down

```text
result:                  REDUCED six huge corners to degree <=18
DAG delta:               +2 PROVED leaves, +5 req edges, +2 ev edges
critical status delta:   none
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Attack the parameter-constant residuals `(5,0)` and `(2,0)` first, then the
linear and quadratic cases. These are symbolic finite-degree problems; no
large computation is indicated.
