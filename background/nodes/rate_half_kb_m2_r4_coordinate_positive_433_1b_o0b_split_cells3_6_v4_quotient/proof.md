# Proof

The parent B/C--E/F theorem gives

```text
(cell, epsilon_1, epsilon_2) -> (9-cell, epsilon_1, -epsilon_2)
```

for `cell` in `{3,6}`, together with the permutation of all seven outside
records and all fifteen residual matchings. The parent S0 and repeated-lane
theorems give the second label action in each lane. That action changes no
cell or source sign. Direct enumeration verifies that both actions preserve
the 5,040-tuple domain, are involutions, and commute.

Partitioning by lane gives the printed orbit profiles. Selecting the
lexicographically first tuple in every orbit gives 456 S0 and 960 SDE/SDF
representatives. Their ordered concatenation has SHA-256
`39fb277a94d8ee3a24e3a8f9e1f0bb50014665ca7c151659d4dc8fcd912392d6`.
The manifest is regenerated and compared byte-for-structure by the verifier.
QED.
