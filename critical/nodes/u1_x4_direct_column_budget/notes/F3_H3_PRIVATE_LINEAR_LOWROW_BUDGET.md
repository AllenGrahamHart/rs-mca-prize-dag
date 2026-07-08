# F3 h=3 private-linear low-row budget

Status: CONDITIONAL ARITHMETIC COMPILER SLICE, NOT `RC-RANK` AND NOT `H3-ACT`.

The private-linear compiler guard shows that a private-linear rank theorem
cannot reuse the current degree-2 non-diagonal budget table.  This packet starts
the required retuning: it gives exact private-linear rank-capacity budgets for
the first five official rows.

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
- verify a pinned passing witness for each row `s=13..17`;
- scan the exact finite `B` cap for `Z+1` and prove the next budget fails;
- keep the result conditional on a future private-linear rank theorem and the
  geometric bridge.

Failure criterion:

- mix the private-linear degree cap with the existing degree-2 budget table;
- claim rows `s >= 18` are covered by this low-row slice;
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

The exact low-row private-linear budgets are:

```text
s=13: Z_private=23
s=14: Z_private=29
s=15: Z_private=37
s=16: Z_private=47
s=17: Z_private=59
```

For comparison, the current degree-2 non-diagonal budgets at these rows are:

```text
s=13: Z_degree2=16
s=14: Z_degree2=21
s=15: Z_degree2=26
s=16: Z_degree2=33
s=17: Z_degree2=42
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
