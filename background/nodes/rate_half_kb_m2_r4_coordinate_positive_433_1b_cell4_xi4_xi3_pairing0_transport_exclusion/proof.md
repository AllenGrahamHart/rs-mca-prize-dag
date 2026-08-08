# Proof

Fix a source sign and target lane `(sigma_c,sigma_o)`. The universal
transport parent proves that

```text
(d,e,f) -> (D,E,F) = (sigma_o e, sigma_o d, f)
```

is a guarded involution on every positive deployed 433-1b common role cell.
It transposes exactly atlas rows `xi=3` and `xi=4`, fixes every other product
and squared-sum row, and preserves the compact residual order. Therefore it
maps a cell-4 system with missing `xi=4` to a cell-4 system with missing
`xi=3` at the identical canonical matching index.

The same theorem fixes the source sign, target lane, target guard divisor,
and role-cell assignment. In particular, matching 0 maps to matching 0.
The other required parent proves that every such `xi=3`, matching-0 system
is empty. A bijection into an empty system has empty domain.

There are four source signs and four target lanes, hence 16 transported raw
cases. QED.
