# Cycle 380: MCA K'=83 triple-carrier route cut (2026-08-16)

The current complete pairwise carrier atlas first fails at `K'=83`. Its
active `one_geom` cell has defects `(50,49,49,48)`, completion maxima
`(23,24,24,25)`, and label `F23__N4_t0__N5_t2`. The exact premium is

```text
41411584407693108041789796771180703922717609427,
```

above the safe ceiling by

```text
46770156546844646871611081711174519620031307.
```

The cell forces two six-dimensional spaces inside the same
eight-dimensional `H_3`. Their intersection has dimension at least four
on a union of size `29..32`. A bounded exact replay applied all four
ordinary fixed-union caps; none changes the premium. This proves a route
cut, not a counterexample to MCA.

The inherited branch-free baseline is already far above the ceiling at
`K'=81` and worsens at sampled later checkpoints, so the finite route
cannot be continued by reverting to uncoupled total capacities.

```text
result:                PROVED first pairwise-atlas wall at K'=83
closed prefix:         10..82
remaining rank nine:  83..15528
new nodes:             1 PROVED route cut
new premise:           none
critical status delta: none
delta-star movement:   none
compute:               one active-cell Modal replay, 60 MB peak RSS
falsified continuation: pairwise atlas plus automatic Grassmann cap
next route action:     derive a nonseparable triple-carrier support-3/4/5
                       census for the explicit (23,24,24,25) cell
```
