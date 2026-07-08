# F3 h=3 non-diagonal low/mid-row budget lift

Status: CONDITIONAL ARITHMETIC COMPILER, NOT `RC-RANK` AND NOT `H3-ACT`.

This packet improves the h=3 bridge-budget constants at the low and middle
official rows by dropping the conservative diagonal restriction `A = D` in the
Stepanov box.  It uses the same reduced-condition and rank-image inequalities
as `F3_H3_BRIDGE_BUDGET_COMPILER.md`; only the arithmetic search over `(A,B,D)`
is stronger.

## Pre-registration

Question:

```text
For s = 13..35, do non-diagonal boxes enlarge the bridge family size |Z|
that can be conditionally paid under RC-RED(13) + RC-RANK?
```

Success criterion:

- use exact integer inequalities only;
- verify a pinned passing witness `(A,B,D)` at the improved `Z`;
- exhaustively scan `Z+1` over `B <= 50000` using the same non-diagonal
  feasibility inequalities;
- keep the result explicitly conditional on `RC-RANK` and the geometric
  batching contract.

Failure criterion:

- a printed row violates either `LS3` or the rank-image cap;
- the note treats this as a proof of the geometric bridge or of `H3-ACT`;
- the verifier hides a broad unbounded parameter search behind the printed
  table.

## Compiler

For a repaired curve family of size `Z`, the same compiler inequalities are

```text
conditions = 13 D (A + D) Z,
coeffs     = A B^3,
L          = (A - 1) + 6 n (B - 1),
image cap  = Z (L + 1).
```

The diagonal compiler set `A = D`.  Here, for each fixed `B` and `D`, the
verifier chooses the least integer `A` satisfying `conditions < coeffs`, then
checks `conditions < image cap`.  This is enough to minimize the degree bound
for that `(B,D)` pair.  The verifier then maximizes over `D` for each `B` and
scans every `B <= 50000`.

## Result

The improved low/mid-row bridge budgets are:

```text
s=13:  11 -> 16
s=14:  14 -> 21
s=15:  18 -> 26
s=16:  23 -> 33
s=17:  29 -> 42
s=18:  36 -> 53
s=19:  46 -> 67
s=20:  58 -> 84
s=21:  73 -> 106
s=22:  92 -> 134
s=23: 116 -> 168
s=24: 146 -> 212
s=25: 184 -> 267
s=26: 232 -> 337
s=27: 292 -> 425
s=28: 368 -> 535
s=29: 463 -> 674
s=30: 584 -> 850
s=31: 736 -> 1071
s=32: 927 -> 1349
s=33: 1168 -> 1700
s=34: 1472 -> 2142
s=35: 1855 -> 2699
```

For every row, the replay verifies that the improved `Z` passes and `Z+1`
fails under the stated non-diagonal search box.  By monotonicity in `Z`, this
gives maximality inside `B <= 50000` for these low rows.

## Interpretation

This reduces the low/mid-row geometric batching burden.  For example, at the
first official row `n=2^13`, the h=3 bridge contract can now batch into `16`
repaired curve families instead of `11`; at `n=2^35`, it can batch into `2699`
instead of `1855`.  No red node closes from this packet: the open mathematics
remains `RC-RANK` plus the actual F3 batching/charging theorem, or replacement
finite certificates.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_nondiagonal_lowrow_budget.py
```

Expected digest:

```text
H3_NONDIAGONAL_LOWROW_BUDGET_PASS
```
