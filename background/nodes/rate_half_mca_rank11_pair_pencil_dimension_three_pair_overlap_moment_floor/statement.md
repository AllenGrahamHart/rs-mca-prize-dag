# Dimension-three pair-overlap moment floor

- **status:** PROVED
- **scope:** the shortened scalar-dimension-three quotient pair-pencil branch

Let `J` be the complete received-pair core common to the 520 selected types
and put `K'=K-|J|`. The residual domain and pair-core sizes are

```text
n'=1048576+K',       s'=67470+K'.
```

Every two distinct residual pair cores intersect in at most `K'-1`
coordinates. If `d_x` is the residual owner multiplicity, then

```text
sum_x d_x=520s',
sum_x C(d_x,2)<=C(520,2)(K'-1).                     (PM-1)
```

The exact minimum of the left second moment at fixed first moment excludes
every `K'<=4835`. Combined with the proved rich-plane ceiling, the complete
dimension-three interval is

```text
4836<=K'<=595763,
452813<=|J|<=1043740.                               (PM-2)
```

At `K'=4835`, pair-overlap capacity is short by 2,110. At `K'=4836`, it has
slack 115,260. This is adjacency for the pair-moment feasibility formula,
not an MCA safe/unsafe certificate.

## Falsifier

Two residual pair cores intersecting in at least `K'` coordinates; an owner
multiplicity sequence with a smaller second moment than the balanced
sequence; a feasible dimension-three row with `K'<=4835`; or an incorrect
endpoint gap.
