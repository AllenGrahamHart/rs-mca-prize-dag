# Proof

Common saturation leaves exactly cells `1,2`, the two opposite source-sign
rows, two repeated-BC signs, and two outside-cycle signs: sixteen states.
In the repeated common compiler, roles `BC1,BC2` have identical product
`sigma*bc` and sum `b+sigma*c`. Exchanging them sends the role cell

```text
cell 1: singleton LA; (AB,BC1),(AC,BC2)
```

to cell `2`, with the two pairs crossed. Direct root placement shows that
`r,t,epsilon_1,epsilon_2` are unchanged. Hence this is an exact row
permutation of the complete common incidence matrix, fixes both target signs
and every outside record, and has no fixed survivor state.

The outside packet has split `DE` and `DF` pairs, so `d->-d` fixes the
sixteen states and gives the proved 105-label action with nine fixed labels.
The common swap acts only on common roles and the D-sign action only on
outside labels, so they commute.

The identity fixes all 1,680 rows. D-sign fixes `16*9=144`; the common swap
and its product with D-sign fix none because they exchange cells `1,2`.
Burnside gives

```text
(1,680+144)/4 = 456.
```

The exact router obtains 72 doubletons and 384 four-element orbits. Adding
the proved 10,620 split-principal representatives gives 11,076 for the
complete live O0b owner workboard. QED.
