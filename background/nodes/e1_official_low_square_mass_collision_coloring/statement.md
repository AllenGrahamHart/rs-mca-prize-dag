# E1 official low-square-mass collision coloring

- **status:** TARGET
- **closure:** open
- **compiler:** `e1_low_square_mass_plotkin_coloring_compiler`

For every pair-feasible prime-field row at the six named RowC/prize
envelopes, form `G_p(ell)` on the antipodal-rearrangement classes: two distinct
classes are adjacent exactly when they have equal reduced E1 value and square
mass `S<=2ell`. Prove the row-specific bounds

| row | required `chi(G_p(ell))` upper bound |
|---|---:|
| RowC `1/4` | 3268165922105543787 |
| RowC `1/8` | 210 |
| RowC `1/16` | 18885148505476 |
| prize `1/4` | 54730211038721500 |
| prize `1/8` | 3 |
| prize `1/16` | 316259390691 |

By the proved compiler, these bounds force more than `B*` distinct reduced E1
values and supply a direct `V` payload on the assigned clean-anchor branch.
The prize rate-`1/8` three-color statement is the binding obligation.

## Falsifier

An admissible row whose certified low-mass collision graph has chromatic
number above its table entry. For the binding row, a certified four-chromatic
subgraph suffices; a `K_4` is the simplest witness.
