# F3 h=3 repeat-boundary line fiber cap

Status: PROVED FIBER CAP, SUPPORT BOUND OPEN.

This packet records a theorem-side consequence of the h=2 Stepanov machinery
for the repeat-boundary line pencil.  It does not bound `B_line` by itself; it
reduces that task to bounding the number of active line parameters.

## Pre-registration

Question:

```text
Can each individual repeat-boundary line fiber be capped by an already-proved
h=2 argument?
```

Success criterion:

- prove a uniform cap for every fixed line parameter `r`;
- keep the remaining support-size problem explicit;
- combine the cap with the q0 cell payment and repeat-residue compiler.

Failure criterion:

- sum the fiber cap over the trivial `n^2` possible parameters and call it a
  useful bound;
- forget that the fourth membership condition is still needed for support;
- use row support sizes as proof.

## Fixed-Fiber Cap

For fixed nondegenerate `r`, a line-pencil point satisfies

```text
1+t in H,
1+rt in H,
1-(r/(r+1))t in H,
1+((r^2+r+1)/(r+1))t in H.
```

Drop the last two conditions.  The remaining two conditions are a two-affine
multiplicative-coset intersection.  By the coset-pair form of the optimized
h=2 rich-coset Stepanov theorem, under

```text
n^4 < p^3,
```

every fixed line fiber satisfies

```text
T_r <= 66 n^(2/3).
```

This applies to the q0 cell as well, but `F3_H3_REPEAT_BOUNDARY_Q0_CELL.md`
pays that cell more sharply using the fact that it has at most two parameters.

## Support Reduction

Let `R_genuine` be the number of active non-q0 line parameters:

```text
R_genuine = #{ r : r^2+r+1 != 0 and T_r > 0 }.
```

Then

```text
B_line_genuine <= 66 n^(2/3) R_genuine.
```

Combining with the q0 payment gives

```text
B_line <= 132 n^(2/3) + 66 n^(2/3) R_genuine.
```

Therefore

```text
repeat_residue
  <= 12n B_line + 18n^2
  <= 1584 n^(5/3) + 792 n^(5/3) R_genuine + 18n^2.
```

Thus a future theorem proving

```text
R_genuine <= C n^beta
```

with `beta < 4/3` makes the repeat residue subcubic.  The especially natural
target suggested by the small-row ledgers is a linear support bound
`R_genuine=O(n)`, which would give an `O(n^(8/3))` repeat-residue payment.

## Replay

Standalone row ledger:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_fiber_cap.py
```

Expected digest:

```text
H3_REPEAT_BOUNDARY_FIBER_CAP_PASS
```
