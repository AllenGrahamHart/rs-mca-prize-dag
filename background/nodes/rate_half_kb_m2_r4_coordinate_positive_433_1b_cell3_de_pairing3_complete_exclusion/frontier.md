# Frontier

The parallel-`DE` block is now proved for matching indices `0,1,2,3`:
the previous theorem pays 144 first-pair cases, and this theorem pays the
48 pairing-3 cases.

The next cell-3 route decision is between:

1. matching indices `4,...,14` for `xi in {0,1,2}`, where the two
   residual `DE` records remain separated; and
2. `xi=3,pairing=0`, where the missing record is `df` and the direct
   colored/missing-sum quartic resultant exceeded the 300-second cap.

Prefer another low-degree nested cut or a direct finite projection in the
FLINT function-field backend.  Do not return to dense SymPy rational-function
resultants, and do not infer complete cell-3 closure from the four paid
matching indices.
