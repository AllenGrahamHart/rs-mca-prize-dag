# Rank-eight dense-owner terminal bridge

- **status:** PROVED
- **interval:** `22526<=K'<=37995`
- **output:** one fixed owner with at least `200632` records and core
  deficiency at most `4`

Let `B` be the weighted fixed nine-subset in the rank-eight affine-owner
lane. For every `22526<=K'<=37995`, one owner point in its affine `U^2`
flat owns at least `200632` selected records. Its complete pair core has
deficiency at most four.

At the first forcing row,

```text
W_B - 200631*C(n'-9,2) = 11714977255865.
```

At the preceding row the sign is negative:

```text
W_B - 200631*C(n'-9,2) = -1170919108090.
```

Thus the upper surviving rank-eight interval reaches the exact
`delta<=4`, `200632`-record dense-owner terminal imported from PR #1168.

## Nonclaim

The owner is chart-local and not chronology-assigned. The theorem does not
identify it with another minimizing pair, coalesce different dense owners,
move an active-v4 atom, or pay rank eleven.
