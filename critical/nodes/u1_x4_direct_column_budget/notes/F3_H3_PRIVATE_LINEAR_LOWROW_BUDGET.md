# F3 h=3 private-linear low/mid-row budget

Status: CONDITIONAL ARITHMETIC COMPILER SLICE, NOT `RC-RANK` AND NOT `H3-ACT`.

The private-linear compiler guard shows that a private-linear rank theorem
cannot reuse the current degree-2 non-diagonal budget table.  This packet starts
the required retuning: it gives exact private-linear rank-capacity budgets for
the official rows `s=13..32`.

## Pre-registration

Question:

```text
If the future h=3 rank theorem only proves private-linear degree-space
fullness, what exact bridge budgets can the private-linear compiler pay at the
lowest official rows?
```

Success criterion:

- use the private-linear degree cap
  `L_private = (A-1) + 3n(B-1)`;
- verify a pinned passing witness for each row `s=13..32`;
- scan the exact finite `B` cap for `Z+1` and prove the next budget fails;
- keep the result conditional on a future private-linear rank theorem and the
  geometric bridge.

Failure criterion:

- mix the private-linear degree cap with the existing degree-2 budget table;
- claim rows `s >= 33` are covered by this low/mid-row slice;
- treat the arithmetic compiler as `RC-RANK`.

## Compiler

For row `n=2^s` and rank-capacity budget `Z`, the private-linear compiler uses

```text
conditions = 13 D(A+D) Z,
coeffs     = A B^3,
L_private  = (A-1) + 3 n (B-1),
image cap  = Z (L_private + 1).
```

The passing inequalities are

```text
conditions < coeffs,
conditions < image cap,
ceil(Z L_private / D) <= 16 n.
```

For `Z+1`, the verifier scans every possible passing `B` up to the exact
analytic cap obtained from these same inequalities.

## Result

The exact low/mid-row private-linear budgets are:

```text
s=13: Z_private=23
s=14: Z_private=29
s=15: Z_private=37
s=16: Z_private=47
s=17: Z_private=59
s=18: Z_private=75
s=19: Z_private=94
s=20: Z_private=119
s=21: Z_private=150
s=22: Z_private=189
s=23: Z_private=238
s=24: Z_private=300
s=25: Z_private=378
s=26: Z_private=477
s=27: Z_private=601
s=28: Z_private=757
s=29: Z_private=954
s=30: Z_private=1202
s=31: Z_private=1514
s=32: Z_private=1908
```

For comparison, the current degree-2 non-diagonal budgets at these rows are:

```text
s=13: Z_degree2=16
s=14: Z_degree2=21
s=15: Z_degree2=26
s=16: Z_degree2=33
s=17: Z_degree2=42
s=18: Z_degree2=53
s=19: Z_degree2=67
s=20: Z_degree2=84
s=21: Z_degree2=106
s=22: Z_degree2=134
s=23: Z_degree2=168
s=24: Z_degree2=212
s=25: Z_degree2=267
s=26: Z_degree2=337
s=27: Z_degree2=425
s=28: Z_degree2=535
s=29: Z_degree2=674
s=30: Z_degree2=850
s=31: Z_degree2=1071
s=32: Z_degree2=1349
```

The private-linear retuning can pay more capacity at these low rows because the
degree bound is smaller.  This does not make the private-linear route superior
overall; it still depends on proving private-linear degree-space fullness and
completing the remaining official rows.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_lowrow_budget.py
```

Expected digest:

```text
H3_PRIVATE_LINEAR_LOWROW_BUDGET_PASS
```
