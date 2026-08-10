# Proof

The signed-edge atlas partitions the target lanes into six split-`BC` and
four repeated-`BC` lanes.  Every lane has fifteen role cells and four source
root-sign rows.  Hence the split side has `6*15*4=360` formal common rows.
The split rank-drop parent excludes the complete rank-at-most-four branch,
so every possible split survivor belongs to the rank-five principal branch.

The repeated saturation parent starts with `4*15*4=240` formal rows, deletes
160 common-unit rows, and leaves 80.  Its exact survivor table is

```text
cells 1/2:   16 formal rows,
cells 3/6:   32 formal rows,
cells 11/14: 32 formal rows.
```

The two cells-3/6 complete parents exclude the middle block for both `BC`
signs.  Therefore 48 repeated rows remain, split disjointly as 16 and 32.

For each formal common row there are seven missing-record choices and
fifteen matchings of the remaining six records, exactly 105 raw outside
labels.  Thus the three blocks contain `37,800`, `1,680`, and `3,360` labels,
whose sum is `42,840`; their common-row sum is `408`.  QED.
