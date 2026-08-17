# Proof

In the split stratum, the two `BC` records have opposite signs. The signed-
edge atlas therefore prints the common packet

```text
-a^2; ab, ac; bc, -bc
```

in each of `S0`, `SDE`, and `SDF`, independently of the outside-cycle sign.
The associated sums are the universal complete-fiber sums
`0,1+b,1+c,b+c,b-c`. These are byte-for-formula the common target inputs of
the O0a compiler. The role-cell and source-sign construction is consequently
identical: 15 cells times four signs gives 60 rows, copied across the six
split O0b lanes to give 360.

The five-row product matrix has rank at most five. The required split
rank-drop theorem excludes every guarded point of rank at most four, so every
retained row lies on the rank-five principal branch. No outside equation has
been transported. QED.
