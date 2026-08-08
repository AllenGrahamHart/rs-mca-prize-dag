# Wave-69 addendum: positive 433-1b cell-4 xi3/xi4 pairing-5/12 closure (2026-08-08)

The third non-fixed matching-exchange orbit is now closed. The direct PROVED
node

```text
rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_pairing5_nested_signfree_exclusion
```

excludes missing `df` at canonical matching 5.

## Colored second-pair nested cut

After omitting `df`, matching 5 is

```text
(de,-de), (de,sigma_c cf), (sigma_o ef,bf).
```

With `m=df`, `z=1/d`, `y=z^2`, and `q=de`, the antipodal first pair is
quadratic in `u=q^2`. Multiplying the second pair by its `q -> -q`
conjugate, reducing modulo that quadratic, and taking the division-free
linear-remainder cut gives a degree-eight polynomial in `z`. Reduction
modulo the missing-sum quartic, followed by `z -> -z` elimination, leaves a
linear common-root cut in the four-basis source tower.

The exact norm and finite replay give

```text
source-sign/sigma_c rows        8
degree of each norm          5058
candidate r roots              104
guarded source points          128
compatible z candidates         32
compatible q candidates         32
third-pair lane evaluations      64
source boundary / no-lift     56 / 48
target boundary / witness       0 / 0
free branch / unresolved        0 / 0
```

Every final lane evaluation is nonzero. The independent verifier recomputes
the base-field root unions, every source lift, both original q equations,
and the original third pair. Exact duplicate `sigma_c` polynomials and
opposite first-source-sign reflections are reused only after coefficient-
level verification. Final Modal app: `ap-U8FZQRqn5ocilCEg0xtzQY`.

## Two-transport payment

The separate PROVED composition node

```text
rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_xi4_pairing5_12_transport_exclusion
```

uses the parallel-`DE` exchange to pay `xi=3`, matching 12, then uses the
universal outside-role involution to pay both `xi=4` partners. This closes
four labels, two parallel-`DE` quotient orbits, and 64 raw cases.

## New campaign boundary

Cell 4 is now

```text
paid labels                   93 / 105
live labels                   12
paid quotient orbits          54 / 60
live quotient orbits           6
paid raw cases               768
```

The independent live obligation is six missing-`df` labels in three
matching-exchange pairs: `{7,10}`, `{8,13}`, and `{11,14}`. Each direct
payment transports to three partners. No complete cell, route, K3 value, or
Prize endpoint closes at this stage.
