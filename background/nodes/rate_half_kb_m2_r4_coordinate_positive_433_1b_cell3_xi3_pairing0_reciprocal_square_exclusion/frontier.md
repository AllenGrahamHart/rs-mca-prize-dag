# Frontier

The `xi=3,pairing=0` block is proved empty, paying 16 new raw cell-3 cases.
Together with the complete parallel-`DE` block, 736 cell-3 cases are paid.

Pairings 1 and 2 retain the same `paired(de,de)` first pair. Reuse the three
`q` branches with `z=1/d`: the missing equation is the even quartic
`1+(2m-s)z^2+m^2z^4`, while the next paired equation is quadratic in
`z`. Reduce the quartic modulo that quadratic before taking a source norm.

Do not infer complete cell-3 closure. The remaining ledger is
`xi=3,pairing in {1,...,14}` and every pairing at `xi in {4,5,6}`.
