# Frontier

The parallel-`DE` block is now proved for matching indices
`0,1,2,3,4,5,6,7,8,9`: the previous theorems pay 144 first-pair cases and
336 pairing-3 through pairing-9 cases.

The next cell-3 route decision is between:

1. matching indices `10,...,14` for `xi in {0,1,2}`, where the two
   residual `DE` records remain separated; and
2. `xi=3,pairing=0`, where the missing record is `df` and the direct
   colored/missing-sum quartic resultant exceeded the 300-second cap.

Pairing 10 changes the pairs to `(de,bf)`, `(second_de,sigma_o ef)`, and
`(df,sigma_c cf)`.  Derive its lowest-degree paired cut
before another norm run.  Do not return to dense SymPy rational-function
resultants, and do not infer complete cell-3 closure from the ten paid
matching indices.
