# Cycle 507: dimension-three rich-plane recurrence

## Result: PROVED common-core sharpening

After reversible common-core shortening in scalar dimension three, residual
coordinate owners lie in affine planes of at most 218 selected types. Three
distinct planes containing at least 189 types would have pairwise overlaps
of at most 15 and hence union size at least

```text
3*189-3*15=522>520.
```

Thus at most two 189-rich planes exist. A rich plane spans its two-dimensional
direction space; two independent direction polynomials have gcd degree at
most `K'-2`, so that plane can recur on at most `K'-2` residual coordinates.
The exact incidence ledger becomes

```text
520(67470+K')<=188(1048576+K')+60(K'-2),
272K'<=162047768.
```

Consequently

```text
K'<=595763,       |J|>=452813.
```

The capacity slack is 232 at the endpoint and becomes a deficit of 40 at
the adjacent row.

## Burn-down

```text
starting local pin:       9bb0cfe1b
canonical prize pin:      0dd5b3244
upstream PR #1170 pin:    e66f6da3
DAG delta:                +1 PROVED rich-plane node, +2 edges
critical status delta:    none
compute spend:            none
closed interface:         dimension-three residual dimensions 595764..640745
next action:              couple recurrent planes or price the shortened family
```

## Nonclaims

- the shortened dimension-three branch is not paid;
- occupancy 218 and the symmetric `218_15` endpoint are not excluded;
- dimension four, rank eleven, and the prize problems remain open;
- the endpoint adjacency is for this incidence formula, not the prize
  safe/unsafe crossing.
