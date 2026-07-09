# F3 h=3 repeat star refined assembly

Status: CONDITIONAL BRANCH-LEVEL ASSEMBLY, NOT A STAR THEOREM.

This packet refines the coarse five-gate star assembly using the branch gates
introduced by the same-lambda and slope branch packets.

## Strict Primitive Gates

The strict branch-level route uses seven primitive gates:

```text
H3-VALUE-GEN-INJECTIVE,
H3-VALUE-SCALE-INJECTIVE,
H3-SLOPE-GG-HIT,
H3-SLOPE-MIXED-HIT,
LOOSE-GEN-RANK/NV,
LOOSE-A-RANK/NV,
LOOSE-B-RANK/NV.
```

The first two imply the coarse value gate:

```text
H3-VALUE-GEN-INJECTIVE + H3-VALUE-SCALE-INJECTIVE
  => H3-VALUE-INJECTIVE.
```

The next two imply the coarse slope gate:

```text
H3-SLOPE-GG-HIT + H3-SLOPE-MIXED-HIT
  => H3-SLOPE-RATIO-HIT.
```

Together with the three loose gates, the original star assembly then gives

```text
H3-NO-DISJOINT-EDGES,
H3-NO-LOOSE-TRIANGLE,
H3-NO-PAIRWISE-CORELESS,
H3-STAR-OBSTRUCTION,
tau_coord <= 1,
repeat_residue <= 90n^2.
```

For every official row `n=2^s`, `13 <= s <= 41`, this is below `n^3`.

## Paid Ledgers

Two paid ledgers are intentionally kept separate from the strict `tau_coord`
route:

```text
lambda=1 scale pairs:
  <= binom(min(floor((n-1)/3), floor(ceil(66 n^(2/3))/3)), 2);

loose secondary subcells:
  <= 53n.
```

Both are below `n^2` on every official row.  The h=2 affine cap first improves
the scale ledger at `n=2^19`.  These ledgers are useful for future
count/payment routes, but they do not by themselves imply `tau_coord<=1`.

## Role in h=3

The coarse star assembly remains valid.  This packet records the sharper
frontier beneath it:

```text
strict route:
  seven branch-level gates close the repeat-boundary star route;

count route ingredients:
  the scale same-lambda branch and loose secondary subcells already have
  paid ledgers, with the scale ledger becoming `O(n^(4/3))` after the h=2
  affine cap takes over, but they still need a bridge into any non-strict
  residue argument.
```

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_star_refined_assembly.py
```

Expected digest:

```text
H3_REPEAT_STAR_REFINED_ASSEMBLY_PASS
```
