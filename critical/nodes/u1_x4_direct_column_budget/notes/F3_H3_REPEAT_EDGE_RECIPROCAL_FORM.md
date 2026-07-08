# F3 h=3 repeat edge reciprocal form

Status: PROVED ALGEBRAIC NORMAL FORM PLUS FINITE ROW CHECKS.

This packet records the symmetric shifted form of the repeat-boundary edge
condition.  It is the algebraic language in which the star-obstruction problem
should be attacked.

## Normal Form

For an active ordered triple `(u,v,w)`, set

```text
x = u-1,  y = v-1,  z = w-1.
```

The repeat-boundary formula is

```text
w = 1 - (u-1)(v-1)/(u+v-2).
```

Since `u+v-2=x+y`, this is equivalent to

```text
z = -xy/(x+y).
```

Therefore

```text
xy+xz+yz = 0,
```

or, because active triples have nonzero shifted coordinates,

```text
1/x + 1/y + 1/z = 0.
```

Conversely, if `x,y,z` are nonzero and `xy+xz+yz=0`, then `x+y` cannot be
zero; otherwise `xy=0`.  Hence `z=-xy/(x+y)`, recovering the repeat-boundary
formula.

The fourth membership condition is simply

```text
lambda = u+v+w-2 = 1+x+y+z in H.
```

Thus active coordinate edges are exactly shifted subgroup triples satisfying
the reciprocal equation, the `lambda` membership condition, and the usual
distinctness exclusions.

## Finite Checks

The replay checks the reciprocal form on both older support rows and the
new hitting witnesses:

```text
p=97    n=16  B_line=0
p=97    n=32  B_line=90
p=193   n=64  B_line=342
p=337   n=16  B_line=6
p=2017  n=32  B_line=6
p=65537 n=256 B_line=48
p=91393 n=256 B_line=12
```

## Role in h=3

A four-edge star obstruction is now a configuration of four shifted reciprocal
triples

```text
x_i y_i + x_i z_i + y_i z_i = 0,
1+x_i+y_i+z_i in H,
```

with no common unshifted coordinate.  This is the concrete algebraic
incidence pattern that remains to exclude for the singleton-hitting route.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_edge_reciprocal_form.py
```

Expected digest:

```text
H3_REPEAT_EDGE_RECIPROCAL_FORM_PASS
```
