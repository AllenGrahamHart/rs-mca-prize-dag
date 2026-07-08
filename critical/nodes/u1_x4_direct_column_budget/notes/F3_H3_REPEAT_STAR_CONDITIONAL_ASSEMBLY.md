# F3 h=3 repeat star conditional assembly

Status: CONDITIONAL ASSEMBLY COMPILER, NOT A STAR THEOREM.

This packet records the exact dependency path from the current open gates to
the repeat-boundary residue payment.

## Open Gates

The current surviving gates for the repeat-boundary star theorem are:

```text
H3-VALUE-INJECTIVE:
  no fixed lambda has two admissible active edge orbits, including the
  lambda=1 scale branch.

H3-SLOPE-RATIO-HIT:
  for lambda-distinct active edge pairs, the denominator-cleared slope
  numerator product vanishes.

LOOSE-GEN-RANK/NV:
  the generic two-parameter nine-map loose target has the needed rank /
  nonvanishing.

LOOSE-A-RANK/NV:
  the branch-A one-parameter eight-map loose target has the needed rank /
  nonvanishing.

LOOSE-B-RANK/NV:
  the branch-B one-parameter eight-map loose target has the needed rank /
  nonvanishing.
```

## Assembly

The disjoint-edge half is:

```text
H3-VALUE-INJECTIVE + H3-SLOPE-RATIO-HIT
  => H3-NO-DISJOINT-EDGES.
```

The pairwise-coreless half is:

```text
LOOSE-GEN-RANK/NV + LOOSE-A-RANK/NV + LOOSE-B-RANK/NV
  => H3-NO-LOOSE-TRIANGLE
  => H3-NO-PAIRWISE-CORELESS.
```

The second implication uses the proved linear-hypergraph compiler: pinched
triangles and tetrahedra are impossible, so loose triangles are the only
surviving pairwise-coreless obstruction.

Combining the two halves with the star-obstruction taxonomy gives

```text
H3-NO-DISJOINT-EDGES + H3-NO-PAIRWISE-CORELESS
  => H3-STAR-OBSTRUCTION
  => tau_coord <= 1.
```

Finally, the coordinate-hitting ledger gives

```text
tau_coord <= 1
  => B_line <= 6n
  => repeat_residue <= (72+18)n^2 = 90n^2.
```

For every official row `n=2^s`, `13 <= s <= 41`, this is below `n^3`.

## Role in h=3

This packet does not close the star theorem.  It removes ambiguity about what
remains: the repeat-boundary star route is closed by exactly the five open
gates listed above.  Proving them would pay the repeat residue quadratically
on all official rows.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_star_conditional_assembly.py
```

Expected digest:

```text
H3_REPEAT_STAR_CONDITIONAL_ASSEMBLY_PASS
```
