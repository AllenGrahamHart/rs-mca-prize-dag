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

## Pre-registration

Question:

```text
Assuming RC-RED(13), RC-RANK, and a geometric bridge from activated shape
pairs into repaired curve families, how small must the family size |Z| be to
deduce H3-ACT(16) on each official row n=2^13..2^41?
```

Success criterion:

- verify the maximum `|Z|` budget for every official power of two;
- use only exact integer inequalities from the rank-parameter compiler;
- state the bridge contract as an explicit remaining theorem.

Failure criterion:

- treat the bridge contract as proved;
- use a broad asymptotic statement without checking official rows;
- hide the `B_max` and diagonal-box limitations.

## Bridge Contract

For a fixed official row `(n,p)`, let `A_3(n,p)` be the activated h=3
dilation-shape count from `F3_H3_ACTIVATION_BOUND_COMPILER.md`.

The missing geometric theorem can now be stated as:

```text
H3-BRIDGE(Z):
  The activated non-toral h=3 shape pairs inject into the points counted by a
  repaired degree-2 signature-curve family of size at most Z, after the toral,
  constant-ratio, and hyperbola-line degeneracies are paid or excluded.
```

Then the conditional chain is:

```text
RC-RED(13) + RC-RANK + H3-BRIDGE(Z_budget(n)) => H3-ACT(16).
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

The full replay prints every exponent `13 <= s <= 41`.  For each row, the
printed bound at `Z_budget` is at most `16n`, and the printed bound at
`Z_budget+1` is larger than `16n` under the stated `B_max=50000` diagonal
search.  This is still not a proof that larger families are impossible under
other parameter families.

## Interpretation

This is useful because the remaining h=3 problem is now sharply split:

- prove `RC-RANK` for repaired signature-curve families;
- prove the geometric bridge/batching theorem with `|Z| <= Z_budget(n)`;
- or replace the uncovered low/bad rows with certificates.

No red node closes from this packet alone.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_compiler.py
```

Expected digest:

```text
H3_BRIDGE_BUDGET_COMPILER_PASS
```
