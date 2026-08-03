# KoalaBear m2 r4 positive 433-1b cell-14 rank-one target-projection exclusion

- **status:** PROVED
- **scope:** the guarded principal quadratic-cover branch of deployed positive
  `433-1b -> O0a` role cell `14`
- **dependencies:** the cell-14 quadratic-curve structure, signed outside
  atlas, and complete-fiber Vieta compiler

## Claim `(KBP1B14-RANKONE-1)`

Write the seven signed outside product records as

```text
y = (de,de,-de,df,sigma_o ef,bf,sigma_c cf).
```

For every source-sign pair, every target lane `(sigma_c,sigma_o)`, every
perfect matching of the six residual records, and every missing-record index
in `{3,4,5,6}`, the guarded cell-14 outside system is empty over
`F_2130706433`.

The claim excludes exactly

```text
4 source signs * 4 target lanes * 4 missing records * 15 matchings = 960
```

raw outside cases. Together with the disjoint 144-case linear-pair theorem,
this leaves exactly 576 of the original 1680 cell-14 cases open. Those 576
cases have a missing `de` record and do not pair the two residual `de`
records.

This theorem does not close cell `14`, `433-1b -> O0a`, K3, LIST, MCA, or
either Prize problem.

## Falsifier

A guarded deployed-field zero in any one of the 960 systems, a live boundary
discarded by a rank-one division or quadratic reduction, or failure of the
exact Cartesian census.
