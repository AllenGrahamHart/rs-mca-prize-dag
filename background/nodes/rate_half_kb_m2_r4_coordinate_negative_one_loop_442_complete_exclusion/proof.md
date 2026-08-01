# Proof

The common atlas has five roles.  Choosing its singleton gives five
possibilities; the other four roles have three perfect matchings, for
fifteen cells total.  Direct enumeration in the atlas order gives exactly
the six disjoint sets in `(KB41C-1)`.  Their cardinalities

```text
1+2+2+4+4+2=15
```

show that no common matching is omitted or duplicated.

For cell `0`, the aligned classifier leaves two common families and the
outside product router leaves only `S1-DE`, `S1-DF`, and `S2`.  The aligned
loop-q theorem deletes all three.  Cells `1,2` are deleted directly by the
crossed-pair theorem.

Cells `3,6` have sixteen finite common packets.  Their terminal AB `S1`
node depends on the corresponding `S0/S2` closes and states that all twenty
canonical product cells are empty.  Cells `4,5,7,8` are deleted at the
common stage by the mixed-pair theorem.  Cells `9,10,12,13` feed the
rank-six sextic product atlas; its terminal internal-`S0` node depends on
the full `S1/S2/S0` chain and states that all eighty invariant-product cells
are empty.  Finally cells `11,14` are deleted at the common stage by the
opposite-pair theorem.

Each parent includes its target-sign or common-root-sign transport.  Every
complete outside skeleton is either deleted at common stage or included in
the terminal product close for its surviving common orbit.  Hence all
fifteen cells are empty, proving the claim. QED.
