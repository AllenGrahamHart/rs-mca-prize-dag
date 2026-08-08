# Wave-70 addendum: positive 433-1b cell-4 xi3/xi4 pairing-7/10 closure (2026-08-08)

The fourth non-fixed matching-exchange orbit is now closed. The direct
PROVED node

```text
rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_pairing7_quadratic_resultant_signfree_exclusion
```

excludes missing `df` at canonical matching 7.

## Quadratic-resultant sign-free cut

After omitting `df`, matching 7 is

```text
(de,sigma_o ef), (de,bf), (-de,sigma_c cf).
```

With `m=df`, `z=1/d`, `y=z^2`, and `q=de`, the last two paired equations
are quadratics in `q`. Their exact Sylvester resultant has degree eight in
`z`. Reduction modulo the missing-sum quartic, followed by `z -> -z`
elimination, leaves a linear common-root cut in the four-basis source tower.

The exact norm and finite replay give

```text
source-sign/sigma_c rows         8
degree of each norm           4068
target / candidate r roots   48 / 64
guarded source points            32
compatible z candidates          16
compatible q candidates          16
remaining-pair lane checks        32
source boundary / no-lift     56 / 16
target boundary / witness       0 / 0
free branch / unresolved        0 / 0
```

Every remaining-pair lane evaluation is nonzero. The independent verifier
recomputes the quadratic resultant identity, base-field root unions, every
source lift, both original quadratic equations, and the original final
pair. Exact duplicate polynomials and opposite first-source-sign
reflections are reused only after coefficient-level verification. Final
Modal app: `ap-CeL2YMFG6ppa6aHpWDhM3T`.

## Two-transport payment

The separate PROVED composition node

```text
rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_xi4_pairing7_10_transport_exclusion
```

uses the parallel-`DE` exchange to pay `xi=3`, matching 10, then uses the
universal outside-role involution to pay both `xi=4` partners. This closes
four labels, two parallel-`DE` quotient orbits, and 64 raw cases.

## New campaign boundary

Cell 4 is now

```text
paid labels                   97 / 105
live labels                    8
paid quotient orbits          56 / 60
live quotient orbits           4
paid raw cases               832
```

The independent live obligation is four missing-`df` labels in two
matching-exchange pairs: `{8,13}` and `{11,14}`. Each direct payment
transports to three partners. No complete cell, route, K3 value, or Prize
endpoint closes at this stage.
