# Wave-68 addendum: positive 433-1b cell-4 xi3/xi4 pairing-4/9 closure (2026-08-08)

The second non-fixed matching-exchange orbit is now closed. The direct PROVED
node

```text
rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_pairing4_nested_signfree_exclusion
```

excludes missing `df` at canonical matching 4.

## Nested q/z sign-free cut

Write `m=df`, `z=1/d`, `y=z^2`, and `q=de`. The missing equation is the
quadratic

```text
M(y)=1+(2m-s)y+m^2y^2=0.
```

The antipodal first pair `Pair(q,-q)` is quadratic in `u=q^2`. Multiplying
the second pair by its `q -> -q` conjugate and reducing modulo that quadratic
leaves a linear remainder in `u`; its division-free cut has degree eight in
`z`. Reduction modulo `M(z^2)`, followed by `z -> -z` elimination and a
second reduction modulo `M(y)`, leaves a linear base-tower remainder.

The exact four-basis norm and finite replay give

```text
source-sign rows                 4
degree of each norm          5108
candidate r roots               56
guarded source points           56
compatible z candidates         32
compatible q candidates         32
third-pair lane evaluations    128
target boundary / witness      0 / 0
free branch / unresolved       0 / 0
```

Every final lane evaluation is nonzero. The independent verifier recomputes
the base-field root unions, every source lift, both original q equations,
and the original third pair. It also checks the exact `r -> -r` relation
between opposite first-source-sign norm and guard polynomials before reusing
their root calculations. Final Modal app: `ap-wroUJycnzyUOJqETrQHZt4`.

## Two-transport payment

The separate PROVED composition node

```text
rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_xi4_pairing4_9_transport_exclusion
```

uses the parallel-`DE` exchange to pay `xi=3`, matching 9, then uses the
universal outside-role involution to pay both `xi=4` partners. This closes
four labels, two parallel-`DE` quotient orbits, and 64 raw cases.

## New campaign boundary

Cell 4 is now

```text
paid labels                   89 / 105
live labels                   16
paid quotient orbits          52 / 60
live quotient orbits           8
paid raw cases               704
```

The independent live obligation is eight missing-`df` labels in four
matching-exchange pairs: `{5,12}`, `{7,10}`, `{8,13}`, and `{11,14}`. Each
direct payment transports to three partners. No complete cell, route, K3
value, or Prize endpoint closes at this stage.
