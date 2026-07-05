# proof: m720_h3_large_gate_replay

The verifier in this folder is a memory-controlled exact replay of the h=3
`full_census` arithmetic used by `nodes/midlarge_h7_20/notes/modal_midlarge_h7_20.py`.

For h=3, a triple is bucketed by the lower elementary signature

```text
e_1 = x + y + z
e_2 = xy + xz + yz.
```

The verifier enumerates every exponent triple, packs `(e_1,e_2,e_3,i,j,k)` as
a compact integer record, sorts the records, and scans equal `(e_1,e_2)`
buckets. Inside each bucket it applies exactly the `full_census` trade tests:
disjoint halves and unequal top coefficient `e_3`. Since `128` and `256` are
not divisible by `3`, no h=3 toral cosets exist in these two rows.

The exact replay returns:

```text
full_census(128,3,17921) = {
  unordered_trades: 384,
  toral: 0,
  nontoral: 384,
  anchored_cores: 18
}

full_census(256,3,65537) = {
  unordered_trades: 5504,
  toral: 0,
  nontoral: 5504,
  anchored_cores: 129
}
```

Thus both banked h=3 large calibration facts are replayed exactly, and this
node is `PROVED`.
