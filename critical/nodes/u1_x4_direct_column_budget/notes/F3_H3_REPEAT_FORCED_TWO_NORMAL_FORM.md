# F3 h=3 repeat forced-coordinate-2 normal form

Status: PROVED ALGEBRAIC NORMAL FORM PLUS FINITE CERTIFICATES.

This packet explains the special role of the forced coordinate `2` in the
nonzero repeat-boundary row.  It does not prove that every active edge contains
`2`; it records what the support problem becomes on the `2`-hit cell.

The companion `F3_H3_REPEAT_FORCED_MOBIUS_INVOLUTION.md` proves the general
forced-coordinate normal form.  The `2`-cell below is the special case where
that Mobius involution becomes ordinary inversion.

## Normal Form

For a fixed forced coordinate `a`, the forced-fiber map is

```text
w_a(v) = 1 - (a-1)(v-1)/(a+v-2),
lambda_a(v) = a+v+w_a(v)-2.
```

At `a=2`, this collapses to

```text
w_2(v) = v^{-1},
lambda_2(v) = v+v^{-1}.
```

Therefore every active ordered triple with first coordinate `2` has the form

```text
(2, v, v^{-1}),
```

with

```text
v in H,
v+v^{-1} in H,
|{2,v,v^{-1}}| = 3.
```

By symmetry, any active coordinate edge containing `2` has the form

```text
{2, v, v^{-1}}.
```

Thus the `2`-hit part of the support is controlled by the trace count

```text
N_2 = #{v in H : v+v^{-1} in H and |{2,v,v^{-1}}|=3}.
```

If every active edge is hit by `2`, then the forced-point reduction gives

```text
B_line <= 3N_2.
```

In the finite row below this inequality is exact.

## Boundary Certificates

The replayed boundary rows give:

```text
p=257     n=16   B_line=0  N_2=0
p=1153    n=32   B_line=0  N_2=0
p=4289    n=64   B_line=0  N_2=0
p=17921   n=128  B_line=0  N_2=0
p=65537   n=256  B_line=48 N_2=16, trace_edges=8, all edges hit by 2
p=262657  n=512  B_line=0  N_2=0
p=1051649 n=1024 B_line=0  N_2=0
```

For the nonzero row, each of the eight coordinate edges is

```text
{2, v, v^{-1}},
```

and the ordered count is

```text
B_line = 48 = 3N_2.
```

Together with `N_2 <= 2n`, this recovers the coordinate-hitting payment

```text
repeat_residue <= (72*1+18)n^2
```

on that row.

## Role in h=3

This packet turns the observed singleton hitter into one explicit cell of the
structural problem.  The pure fixed-`2` target

```text
H3-FORCED-TWO-COVER:
  prove that all active non-q0 repeat-boundary edges are hit by 2
```

is false in the finite exception scan.  The surviving target is to prove a
small coordinate hitting set, with the inverse-pair `2`-cell as one component
and a separate hitting argument for edges not hit by `2`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_forced_two_normal_form.py
```

Expected digest:

```text
H3_REPEAT_FORCED_TWO_NORMAL_FORM_PASS
```
