# Cycle 75: `A=1` core-free contact reduction (2026-08-11)

## Cycle pins

```text
our start:       8b43ca249
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   38 PRs; relevant overlap re-audited
critical open:   28
```

## Contact section

The half-distance `A=1` Hankel pencil has `rho` recurrence rows, two fewer
than the strict `A=3` pencil. On every core-free failure its canonical Forney
numerator therefore has contact order `2rho` and gives

```text
s_F in H^0(C,O_C(-rho-1,e+1)),
deg L_F=rho-e.
```

The proved leaf is
`rate_half_ca_hankel_a1_core_free_forney_contact_section`.

## Pole-slack reduction

Let `p` be the actual pole-ideal colength and `ell=4e-T`. Choose the largest
domain interpolation degree compatible with both component avoidance and
surface cohomology:

```text
alpha=2 for e<=rho/2-1,
alpha=1 for rho/2<=e<=rho-1,
alpha=0 for e=rho.
```

A form of bidegree `(alpha,floor(p/(alpha+1)))` clears the poles. Three
contact copies produce a forbidden section whenever

```text
floor(p/(alpha+1))+ell+3<e.
```

Thus every survivor has `p>=(alpha+1)(e-ell-3)`. At the first live degree
`e=m+1`, only `ell=0,1,2` occur, and their pole deficiencies `Delta-p` are
at most `5,8,11`. The proved leaf is
`rate_half_ca_hankel_a1_core_free_pole_slack_exclusion`.

## Upstream refresh

Upstream still points at `main@93fba1be3f`. Of 38 open PRs, the relevant
ones are `#1151/#1125` on LIST FPC5/Hankel structure, `#1156` on MCA
exception routing, and `#1150` on the corrected F2 branch. Their stated
nonclaims leave this `A=1` endpoint untouched.

## Burn-down

```text
result:                  NARROWED core-free A=1 by an exact pole inequality
DAG delta:               +2 PROVED leaves, +3 req edges, +2 ev edges
critical status delta:   none
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next prioritize the three `e=m+1` finite pole-deficiency chambers, while
keeping the fixed-core `s=1,2` profiles explicit and separate.
