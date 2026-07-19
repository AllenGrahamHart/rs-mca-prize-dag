# F3 h=3 repeat forced-coordinate Mobius involution

Status: PROVED ALGEBRAIC NORMAL FORM.

This packet sharpens the forced-coordinate route from
`F3_H3_REPEAT_SUPPORT_FORCED_POINT_REDUCTION.md`.  It does not prove a small
forced-coordinate cover.  It identifies the exact one-dimensional quotient
inside each forced-coordinate cell.

## Normal Form

Fix a forced coordinate `a` and put

```text
A = a - 1,  X = v - 1.
```

The forced-fiber map

```text
w_a(v) = 1 - (a-1)(v-1)/(a+v-2)
```

satisfies

```text
w_a(v) - 1 = T_A(X),   T_A(X) = -A X/(A+X).
```

The map `T_A` is an involution:

```text
T_A(T_A(X)) = X.
```

Its fixed factors are

```text
X = 0,        X + 2A = 0,
```

which correspond to `v=1` and `v=3-2a`.  These are excluded from active
distinct triples by the usual non-pole/repeated-coordinate conditions.

The lambda value is invariant under the same involution:

```text
lambda_a(v) = a + v + w_a(v) - 2
lambda_a(w_a(v)) = lambda_a(v).
```

Therefore, after excluding fixed and pole points, every active edge hit by a
forced coordinate `a` is organized into an unordered pair

```text
{v, w_a(v)}
```

under this Mobius involution.

## Special Cell

For `a=2`, the involution is the ordinary inverse map:

```text
w_2(v) = v^-1,
lambda_2(v) = v + v^-1.
```

This recovers the inverse-pair normal form from
`F3_H3_REPEAT_FORCED_TWO_NORMAL_FORM.md` as one special forced-coordinate
cell, not as a separate phenomenon.

## Consequence

The forced-coordinate route can now be stated cell-by-cell:

```text
active edges hit by a
  <=> Mobius-involution pairs {v, w_a(v)}
      with v, w_a(v), lambda_a(v) in H.
```

Thus a future small hitting theorem may work by proving that the active
support is covered by a small collection of Mobius cells.  The elementary
degree payment remains unchanged:

```text
if |A0| = F covers every active edge, then
repeat_residue <= (72F + 18)n^2.
```

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_forced_mobius_involution.py
```

Expected digest:

```text
H3_REPEAT_FORCED_MOBIUS_INVOLUTION_PASS
```
