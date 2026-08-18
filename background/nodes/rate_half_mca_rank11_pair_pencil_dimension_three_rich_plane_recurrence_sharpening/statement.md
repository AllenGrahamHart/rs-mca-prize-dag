# Dimension-three rich-plane recurrence sharpening

- **status:** PROVED
- **scope:** the scalar-dimension-three quotient pair-pencil branch

Let `J` be the complete received-pair core common to the 520 selected
quotient types, and shorten reversibly by `J`. Write

```text
K'=K-|J|,       n'=1048576+K',       s'=67470+K'.
```

At most two affine scalar planes contain 189 or more selected types. Every
such plane can occur as a residual coordinate owner fiber at most `K'-2`
times. Consequently the number `N_189` of residual coordinates with owner
multiplicity at least 189 satisfies

```text
N_189<=2(K'-2).                                      (RP-1)
```

Combining `(RP-1)` with the affine-plane cap 218 gives

```text
520s'<=188n'+30N_189
      <=188n'+60(K'-2).                              (RP-2)
```

Exact substitution in `(RP-2)` forces

```text
K'<=595763,       |J|>=452813.                       (RP-3)
```

At `K'=595763` the incidence capacity has slack 232. At the adjacent row
`K'=595764` it is short by 40, so the endpoint is exact for this ledger.

This theorem does not pay the shortened residual, classify its rich planes,
exclude occupancy 218, or close rank eleven.

## Falsifier

Three distinct affine planes each containing at least 189 selected types; a
pair of independent plane directions with `K'-1` common residual roots; a
rich plane recurring more than `K'-2` times; or a feasible residual row with
`K'>595763`.
