# F3 h=3 repeat-boundary q0 cell

Status: PROVED CELL BOUND FROM THE H2 STEPANOV COROLLARY.

This packet pays the special line-pencil cell

```text
q(r)=r^2+r+1=0.
```

In this cell the fourth LP4 form is constant:

```text
lambda = 1.
```

It is exactly the triple-repeat boundary cell.  It does not need the full LP4
theorem.

## Pre-registration

Question:

```text
Can the q(r)=0 triple-repeat line cell be bounded using already-proved h=2
Stepanov machinery?
```

Success criterion:

- identify the cell as a fixed finite set of line parameters;
- reduce each line to a two-affine-form multiplicative-coset intersection;
- import only the h=2 rich-coset Stepanov proof pattern;
- keep the remaining non-q0 line-pencil cell separate.

Failure criterion:

- count the q0 cell as generic LP4 proof debt;
- assume the primitive cube roots lie in `H`;
- use a numerical row count as the proof.

## Coset-Pair h=2 Input

Use `F3_H2_AFFINE_COSET_PAIR_STEPANOV.md`: under `n^4 < p^3`, any shifted
two-affine multiplicative-coset intersection has size at most `66 n^(2/3)`.

## q0 Cell Bound

When `q(r)=0`, there are at most two values of `r`.  Also

```text
-r/(r+1)
```

is the other primitive cube root, so the line forms are

```text
1+t,     1+rt,     1+r^2 t,     1.
```

The q0 contribution `B_q0` is bounded by dropping the third nonconstant form:
for each fixed `r`, count only the conditions

```text
1+t in H,     1+rt in H.
```

These are two affine multiplicative-coset conditions, so the coset-pair h=2
corollary gives at most `66 n^(2/3)` points for each `r`.  Therefore

```text
B_q0 <= 132 n^(2/3).
```

Consequently the q0 part of the repeat residue is paid by

```text
12 n B_q0 <= 1584 n^(5/3),
```

which is far below the cubic floor.  The remaining line-pencil theorem may
exclude `q(r)=0` and handle only the genuinely four-form cell.

## Replay

Standalone row ledger:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_q0_cell.py
```

Expected digest:

```text
H3_REPEAT_BOUNDARY_Q0_CELL_PASS
```
