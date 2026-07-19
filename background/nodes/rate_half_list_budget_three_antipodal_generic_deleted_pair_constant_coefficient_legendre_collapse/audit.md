# Audit

The `z` in this packet is the reversal variable for the half-degree
coordinate `x=Y^2`. It equals the square of the reversal variable used before
the deleted-pair parity reduction. This is why the fourth-root truncation has
degree `m=2M-1`, not `4M-1`.

Equation `(5)` uses two different reversals of `R`: full degree `2a`, inherited
from `Q-A^2`, and actual degree `a+s`, inherited from `R=AS+T`. Their degree
difference is exactly `a-s=2M+1`; omitting this shift changes the coefficient
in `(LCC2)`.

The proof uses only the coefficient below `z^N`, so replacing
`(1-z^N)/E` by `1/E` in `(7)` is exact at degree `a`. It is not an identity of
the full series.

The name "Legendre" refers to `(LCC5)`. The root-free definition `(LCC1)` and
recurrence `(LCC4)` remain valid without choosing a square root of `t`.

Passing one equation in `(LCC6)` is only necessary. The torsion-trace, full
scalar identity, differential gcd, and exact fourth-power gates still remain.
No numerical nonvanishing evidence is promoted by this node.
