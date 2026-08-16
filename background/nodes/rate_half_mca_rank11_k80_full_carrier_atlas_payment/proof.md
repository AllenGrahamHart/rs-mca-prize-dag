# Proof

At `K'=80`, `q=70`, `m=67552`, and `n=1048656`. The conservative stream has
11,929,729 leaves and 26,104 above-ceiling tuples, with canonical digest

```text
911406bd5364eea9ad69c2d82d6263db31f43f5e9d3d04f0cfdedd9a36eb47bc.
```

The largest safe conservative leaf is

```text
s2=66/s3=40/s4=40/s5=41/c6d3/c7d2/c8d1/c9d0/carrier32_plain,
```

with premium `(P80)` and margin `(M80)`. The exhaustive pairwise atlas
reroutes every exceptional tuple in 24,962,791 exact evaluations. Their
maximum is `37883477302563580100728788160734085033920217692`, below the
ceiling by `3409233574168250899830880688091381321579526144`.

The seven geometry lanes contain 164,858,603 evaluations. Their maximum is
the one-step value `39668547314355452559959739197487065940915191238`, below
`(P80)`. Every lane used the bounded-long runner and stayed below 63 MB peak
RSS. Exact component arithmetic gives `(G80)`. QED.
