# proof: m720_h5_n32_gate_replay

The verifier in this folder is a standalone replay of the `full_census`
arithmetic used by `nodes/midlarge_h7_20/notes/modal_midlarge_h7_20.py`.

It enumerates every one of the `C(32,5)` exponent subsets of the 32nd roots of
unity in `F_97`, buckets them by the lower elementary-symmetric signature
`e_1,...,e_4`, and then counts disjoint unordered pairs with unequal top
coefficient `e_5`. This is exactly the M720 h=5 trade predicate.

The run returns:

```text
full_census(32,5,97) = {
  unordered_trades: 96,
  toral: 0,
  nontoral: 96,
  anchored_cores: 30
}
```

Thus the banked h=5 n=32 gate fact is replayed locally and this node is
`PROVED`.
