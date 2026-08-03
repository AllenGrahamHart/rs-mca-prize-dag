# Frontier

The parallel-`DE` block is now proved for matching indices
`0,1,2,3,4,5,6,7`, paying `384` raw cases.

Matching 8 is the next canonical matching:

```text
((0,3),(1,5),(2,4))
= (de,sigma_o ef), (second_de,sigma_c cf), (df,bf).
```

It again has a shared-`f` nested-quadratic route, now fixing both target
signs in the two first cuts and leaving `paired(df,bf)` for direct replay.
The separate `xi=3,pairing=0` branch still needs a lower-degree shared-`f`
elimination.

Do not infer complete cell-3 closure from the eight paid matching indices.
