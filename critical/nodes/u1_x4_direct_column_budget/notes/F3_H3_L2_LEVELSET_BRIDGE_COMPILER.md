# F3 h=3 L2 and level-set bridge compiler

Status: PROVED ARITHMETIC INTERFACE, NOT THE GEOMETRIC BRIDGE AND NOT
`H3-ACT`.

This packet weakens the sufficient condition in
`F3_H3_PAIR_COUNT_FROM_CHARTS_COMPILER.md`.  The bridge does not intrinsically
need separate total-mass and max-fiber bounds.  It needs the exact quadratic
ledger that pays activated pairs, or an equivalent level-set/tail estimate.

## Pre-registration

Question:

```text
What is the weakest local arithmetic condition on same-fiber chart sizes that
implies the normalized h=3 target P_total <= 16 n?
```

Success criterion:

- derive the exact L2 ledger from `P_z = R_z(R_z-6)/72`;
- state the equivalent level-set identity for unordered triple counts
  `N_z=R_z/6`;
- show the earlier max-times-total condition is only a corollary;
- keep the geometric assignment of activated pairs to charts explicitly open.

Failure criterion:

- treat this arithmetic compiler as a proof of the bridge;
- require a max-fiber cap when an L2/tail theorem would suffice;
- lose the sixfold ordering factor between ordered and unordered triples.

## Exact L2 Ledger

For every repaired same-`(e1,e2)` chart `z`, let

```text
R_z = ordered pairwise-distinct same-fiber triple count,
N_z = R_z / 6.
```

The local pair contribution is

```text
P_z = binom(N_z,2) = R_z(R_z-6)/72.
```

Therefore, for a chart ledger that covers all normalized non-toral h=3
activations after the paid degeneracies are removed,

```text
P_total <= 16 n
```

is equivalent to the exact integer inequality

```text
sum_z R_z(R_z-6) <= 1152 n.
```

A stronger but often easier sufficient condition is

```text
sum_z R_z^2 <= 1152 n.
```

This is the native L2 form of the missing h=3 bridge theorem.

## Level-Set Form

Equivalently, define tail counts

```text
L_m = #{ z : N_z >= m },     m >= 2.
```

Then

```text
P_total = sum_{m >= 2} (m-1) L_m.
```

So a future level-set theorem proves `H3-ACT(16)` as soon as it gives

```text
sum_{m >= 2} (m-1) L_m <= 16 n.
```

This is sharper than asking for a uniform max-fiber cap.  The max-times-total
condition from the previous packet follows from

```text
sum_z R_z^2 <= (max_z R_z) sum_z R_z
             <= (M+1)(S+Z).
```

## Bridge Target

The h=3 bridge can now be stated in its weakest arithmetic form:

```text
After toral, constant-ratio, and hyperbola-line cells are paid or excluded,
assign every activated normalized non-toral h=3 shape-pair to repaired
same-fiber charts whose ordered triple counts R_z satisfy

  sum_z R_z(R_z-6) <= 1152 n.
```

Equivalently, prove the level-set tail inequality above.  This packet does not
construct that assignment and does not prove the needed rank/minor theorem.

## Replay

Standalone only:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_l2_levelset_bridge_compiler.py
```

Expected digest:

```text
H3_L2_LEVELSET_BRIDGE_COMPILER_PASS
```
