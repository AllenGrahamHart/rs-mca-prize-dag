# F3 h=3 bridge-budget compiler

Status: CONDITIONAL BRIDGE COMPILER, NOT THE GEOMETRIC BATCHING THEOREM.

This packet makes the missing h=3 geometry interface explicit.  It asks how
many repaired degree-2 signature curves the current rank-form Stepanov
arithmetic can tolerate while still proving the target

```text
H3-ACT(16): A_3(n,p) <= 16 n.
```

It does not prove that activated shape pairs actually batch into that many
curves.

This is the legacy diagonal-box budget table.  The active h=3 bridge target now
uses the strictly larger non-diagonal table in
`F3_H3_NONDIAGONAL_LOWROW_BUDGET.md` and
`F3_H3_NONDIAGONAL_HIGHROW_BUDGET.md`; see
`F3_H3_BRIDGE_BUDGET_LINEAGE.md` for the replayed comparison.

## Pre-registration

Question:

```text
Assuming RC-RED(13), RC-RANK, and a geometric bridge from activated shape
pairs into repaired curve images, how small must the rank-capacity consumption
Z be to deduce H3-ACT(16) on each official row n=2^13..2^41?
```

Success criterion:

- verify the maximum rank-capacity budget for every official power of two;
- use only exact integer inequalities from the rank-parameter compiler;
- state the bridge contract as an explicit remaining theorem.

Failure criterion:

- treat the bridge contract as proved;
- use a broad asymptotic statement without checking official rows;
- hide the `B_max` and diagonal-box limitations.

## Bridge Contract

For a fixed official row `(n,p)`, let `A_3(n,p)` be the activated h=3
dilation-shape count from `F3_H3_ACTIVATION_BOUND_COMPILER.md`.

The original raw-family version of the missing geometric theorem was:

```text
H3-BRIDGE(Z):
  The activated non-toral h=3 shape pairs inject into the points counted by a
  repaired degree-2 signature-curve family of size at most Z, after the toral,
  constant-ratio, and hyperbola-line degeneracies are paid or excluded.
```

After `F3_H3_RANK_EFFECTIVE_BRIDGE.md`, this should be read in the
rank-effective form:

```text
H3-BRIDGE-RANKCAP(Z):
  After toral, constant-ratio, and hyperbola-line degeneracies are paid or
  excluded, activated non-toral h=3 shape pairs are assigned to repaired
  signature-curve images with total consumed rank capacity at most Z.
```

This distinction matters because repeated copies of the same curve image do
not increase substitution rank.

Then the conditional chain is:

```text
RC-RED(13) + RC-RANK + H3-BRIDGE-RANKCAP(Z_budget(n)) => H3-ACT(16).
```

## Replayed Budgets

The exact diagonal-box compiler with `B_max=50000` verifies the following
budgets:

```text
n=2^13: Z_budget=11
n=2^20: Z_budget=58
n=2^23: Z_budget=116
n=2^32: Z_budget=927
n=2^39: Z_budget=4674
n=2^40: Z_budget=5889
n=2^41: Z_budget=7420
```

The full replay prints every exponent `13 <= s <= 41`.  For each row, it
checks a pinned passing diagonal-box witness at `Z_budget`, and exhaustively
scans the stated `B_max=50000` diagonal search at `Z_budget+1` to verify that
the next budget fails.  Since the compiled bound is nondecreasing in `Z`, this
proves maximality within the stated search box.  This is still not a proof that
larger families are impossible under other parameter families.

## Interpretation

This is useful because the remaining h=3 problem is now sharply split:

- prove `RC-RANK` for repaired signature-curve families;
- prove the geometric bridge/batching theorem with total rank-capacity
  consumption `<= Z_budget(n)`;
- or replace the uncovered low/bad rows with certificates.

No red node closes from this packet alone.

## Optional B_max stress

The aggregate replay uses `B_max=50000`.  The optional stress verifier checks
the cheaper monotone certificate for a ten-times larger box: it recomputes only
`Z_budget+1` for every row with `B_max=500000`.  If every next budget still
fails, then no larger `Z` can pass inside that larger diagonal box.

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_bmax_stress.py
```

Expected digest:

```text
H3_BRIDGE_BUDGET_BMAX_STRESS_PASS
```

Result: all printed next budgets still fail.  The closest stressed failures are

```text
s=13, Z=12, margin=6297
s=14, Z=15, margin=9836
s=15, Z=19, margin=22892
s=16, Z=24, margin=51554
s=18, Z=37, margin=53037
```

Thus the current `Z_budget` table is not a `B_max=50000` artifact up to this
larger diagonal search box.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_compiler.py
```

Expected digest:

```text
H3_BRIDGE_BUDGET_COMPILER_PASS
```
