# Wave-66 addendum: positive 433-1b cell-4 xi3/xi4 pairings 1-2 closure (2026-08-08)

The two fixed matching-exchange orbits after matching 0 are now closed. The
PROVED direct node

```text
rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_pairings1_2_reciprocal_linear_exclusion
```

excludes missing `df` at canonical matchings 1 and 2.

## Reciprocal-linear cut

Both matchings retain `paired(de,de)=0`, giving the same three exhaustive
branches `q=B_i/A_i`. With `m=df`, `s=(d+f)^2`, and `z=1/d`, the missing
equation is

```text
M(z)=1+(2m-s)z^2+m^2z^4=0.
```

The matching-specific second paired equation is quadratic in `z`. Dividing
`M` by that quadratic in the exact four-basis source tower leaves a linear
remainder in every row. Its division-free common-root cut gives

```text
branch rows                    36
candidate r roots             360
guarded source points         216
empty q-branch points          36
reciprocal-linear candidates   32
final paired evaluations       64
target boundary / witness     0 / 0
free branch / unresolved      0 / 0
```

Matching 1 has no common `z` lift. Matching 2 has 32 common lifts, and all
64 final lane evaluations are nonzero. The independent verifier recomputes
all norm and guard roots and rebuilds every source and target lift. Final
full-census Modal app: `ap-FvpQcJ8FuxEK0TRI6DiZet`.

## Transport payment

The separate PROVED corollary

```text
rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi4_xi3_pairings1_2_transport_exclusion
```

uses the universal outside-role involution to pay both corresponding
missing-`ef` labels without duplicate computation.

## New campaign boundary

Cell 4 is now

```text
paid labels                   81 / 105
live labels                   24
paid quotient orbits          48 / 60
live quotient orbits          12
paid raw cases               576
```

The independent live obligation is the 12 missing-`df` labels in the six
matching-exchange pairs `{3,6}`, `{4,9}`, `{5,12}`, `{7,10}`, `{8,13}`, and
`{11,14}`. Each future `df` payment transports to its `ef` partner. No
complete cell, route, K3 value, or Prize endpoint closes at this stage.
