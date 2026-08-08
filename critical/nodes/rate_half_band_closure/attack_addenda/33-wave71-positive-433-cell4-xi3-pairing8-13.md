# Wave-71 addendum: positive 433-1b cell-4 xi3/xi4 pairing-8/13 closure (2026-08-08)

The fifth non-fixed matching-exchange orbit is now closed. The direct
PROVED node

```text
rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_pairing8_quadratic_resultant_signfree_exclusion
```

excludes missing `df` at canonical matching 8.

## Exchanged-partner resultant

After omitting `df`, matching 8 is

```text
(de,sigma_o ef), (de,sigma_c cf), (-de,bf).
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
source lift, both original quadratic equations with their matching-8 signs,
and the original final pair. Final Modal app:
`ap-M2MiquWgaRzmJgiqN1Cumc`.

## Two-transport payment

The separate PROVED composition node

```text
rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_xi4_pairing8_13_transport_exclusion
```

uses the parallel-`DE` exchange to pay `xi=3`, matching 13, then uses the
universal outside-role involution to pay both `xi=4` partners. This closes
four labels, two parallel-`DE` quotient orbits, and 64 raw cases.

## New campaign boundary

Cell 4 is now

```text
paid labels                  101 / 105
live labels                    4
paid quotient orbits          58 / 60
live quotient orbits           2
paid raw cases               896
```

The independent live obligation is two missing-`df` labels in the single
matching-exchange pair `{11,14}`. One direct payment transports to three
partners. No complete cell, route, K3 value, or Prize endpoint closes at
this stage.
