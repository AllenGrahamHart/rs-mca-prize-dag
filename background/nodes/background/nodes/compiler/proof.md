# Proof

For each cell, a proved upper count at most `B*` implies `SAFE`, while a proved
lower count greater than `B*` implies `UNSAFE`. No other numeric comparison is
enough: an upper count above `B*` and a lower count at most `B*` are both
uninformative. If the useful comparison comes from a non-proved packet, the
cell is only `CONDITIONAL`.

Suppose agreement `a` is proved unsafe and `a+1` is proved safe. Monotonicity
of closed Hamming balls then puts the first safe agreement exactly at `a+1`.
The largest certified closed integer radius is `n-(a+1)`; the real boundary
supremum is `(n-a)/n` and is not attained. This is precisely the proved
`v13_finite_adjacent_compiler` implication.

The implementation checks these comparisons with integers only. It suppresses
the certificate unless every axis is proved, no conditional claim is consumed,
and exactly one adjacent crossing exists. It rejects a proved safe cell below a
proved unsafe cell and rejects simultaneous proved safe/unsafe packets at one
cell. Therefore every emitted prize-facing certificate satisfies the stated
adjacent inequalities, while incomplete or inconsistent inputs cannot emit
one.

`audit.py` checks the calibrated `F_17^32` transition and seven refusal or
mutation cases, including a missing required convention axis.
