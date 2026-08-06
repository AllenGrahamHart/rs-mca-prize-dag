# Exact-list first-match summed numerator budget

- **status:** TARGET
- **closure:** open

For every official `x4` row and every quotient row consumed by `TR`, print
one support-wise priority map and exact integer list-side numerators

```text
U_paid, U_QD, U_MT, U_prim.
```

They count, respectively, already discharged background classes,
quotient/dihedral classes, structured moment/U2 classes, and primitive star
classes. Prove coverage and no double payment, then prove

```text
U_paid+U_QD+U_MT+U_prim <= B*=floor(|F|/2^128).
```

The proposed component bounds are `U_MT<=n^3` from `u2c` and
`U_prim<=16n^3` from the `u1` F-4 minimal-record budget plus primitive-star
coverage. The final comparison
must use actual list members and include every consumed row. QA.22's MCA
bad-slope sum is evidence, not a substitute for this table.
