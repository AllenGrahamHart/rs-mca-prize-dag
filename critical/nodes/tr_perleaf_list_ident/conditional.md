# tr_perleaf_list_ident conditional proof

## Predicate nodes

- `tr_joint_telescope`
- `x4_exactlist_staircase_split`

## Claim

The terminal-reserve per-leaf count is exactly a same-rate quotient-row
exact-list instance, so its bound is supplied by the corrected exact-list split.

## Proof

Fix a quotient scale `M` and an isotypic character `r`. A per-character
agreement object is stable on the fibers of `pi(x) = x^M` and has the
character form

```text
f(x) = x^r F(pi(x)).
```

Multiplication by `x^{-r}` converts this to a scalar received word on the
quotient domain `pi(H)`. Since the support is `K_M`-stable, agreement and exact
disagreement are both orbitwise conditions: a stable support upstairs is the
full preimage of a quotient support downstairs, and exactness is preserved
fiber by fiber. Conversely, any quotient-row list witness lifts by
`F(y) -> x^r F(x^M)` to the corresponding per-character witness upstairs.

The lifted joint-stabilizer identity in `tr_joint_telescope` supplies the
needed alignment transport for the actual TR objects, including the recorded
degenerate-tower correction column. Thus the per-character set `A_r` is not a
new counting problem; it is a worst-word exact-list count at the quotient row
with the same rate and scaled domain size.

The predicate `x4_exactlist_staircase_split` is precisely the corrected
exact-list statement needed at those quotient rows: quotient staircase,
dihedral staircase, moment-trade column, and the primitive remainder after
the strip. Transporting that split along the dictionary above gives the
per-leaf terminal-reserve bound. Therefore this node is conditional only on
the corrected exact-list split, not on any separate per-leaf theory.
