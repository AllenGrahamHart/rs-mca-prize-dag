# F3 h=3 frontier ledger

Status: REPLAYED FRONTIER LEDGER, NOT `H3-ACT`, NOT `RC-RANK`.

This packet compiles the current h=3 proof surface for the F3 flip brief.  It
imports the activation-bound compiler, official bridge-budget tables, the
rank-effective bridge repair, the conic bridge accounting ledger, the
L2/level-set bridge compiler, and the h=3 repeat-boundary frontier ledger.  It
does not prove a new rank theorem or a new geometric batching theorem.

## Frontier Gates

```text
H3-ACT-COMPILER: REPLAYED/CONDITIONAL
  C=16 would imply T3<n^3 from n>=17.  The n=96 all-core evidence has
  720 oriented activation records over 82 threshold primes, with maximum
  92 oriented activations at p=37633.
  Residual: prove H3-ACT(16), or replace it with official-row activation
  certificates.

F3-RANK-AVOID / RC-NV: OPEN
  The non-diagonal official-row arithmetic covers s=13..41 with
  Z_budget=16..10795.  The older diagonal bridge-budget table is only
  11..7420 and is retained as a legacy lower bound.
  Residual: prove finite-row rank-good minor nonvanishing on repaired
  degree-2 signature-curve images.

H3-BRIDGE-RANKCAP: OPEN
  The bridge must count rank-effective capacity units, not raw duplicate
  curves.  Pinned toy capacities are collapsed=0, private=3, random=4.  The
  conic bridge accounting ledger proves that different base points in the same
  same-(e1,e2) fiber are not new conic images; the exact local L2 target is
  sum_z R_z(R_z-6) <= 1152 n, equivalently P_total <= 16 n.
  Residual: assign activated non-toral shape pairs to repaired chart images
  within the official rank-capacity budget.

F3-PRIVATE-LINEAR-RANK-AVOID: OPEN/ALTERNATE
  The retuned private-linear arithmetic covers s=13..41 with
  Z_private=23..15267.  Every official private-linear passing witness has
  max(A,D,B-1)<H with margin at least 7904.
  Residual: prove finite-row minor nonvanishing on the private-linear
  three-parameter normal-form image, plus the matching private-linear bridge.

H3-REPEAT-BOUNDARY-STAR: OPEN FRONTIER
  The repeat-boundary frontier ledger replays seven strict branch gates:
  H3-VALUE-GEN-INJECTIVE, H3-VALUE-SCALE-INJECTIVE, H3-SLOPE-GG-HIT,
  H3-SLOPE-MIXED-HIT, LOOSE-GEN-RANK/NV, LOOSE-A-RANK/NV, and LOOSE-B-RANK/NV.
  On the count route, H3-VALUE-SCALE-INJECTIVE is replaced by the paid
  quadratic scale-collision ledger, leaving six still-open strict gates.
  Residual: prove or replace the strict same-lambda, slope, and loose-triangle
  branch gates needed by the star route.
```

## Use In The F3 Brief

This ledger keeps T1/T2 honest:

```text
RC-RED(13) + F3-RANK-AVOID + H3-BRIDGE-RANKCAP
  => H3-ACT(16)
  => T3 < n^3 on all official rows.
```

The private-linear route is a separate alternate:

```text
F3-PRIVATE-LINEAR-RANK-AVOID + H3-BRIDGE-PRIVATE-RANKCAP
  => H3-ACT(16),
```

but it must use the private-linear degree cap and `Z_private` table.  It cannot
be mixed with the degree-2 non-diagonal compiler.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_frontier_ledger.py
```

Expected digest:

```text
H3_FRONTIER_LEDGER_PASS
```
