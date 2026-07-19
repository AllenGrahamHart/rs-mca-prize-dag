# F3 h=3 repeat-boundary line compiler

Status: PROVED ARITHMETIC COMPILER, NOT A LINE-COUNT BOUND.

This packet turns the repeat-residue boundary term into a normalized line-pencil
membership problem.  It follows the repeat-residue boundary compiler: once
`D_boundary` is controlled, the moment residue is controlled.

## Pre-registration

Question:

```text
Can D_boundary be reduced to a smaller explicit H-membership count?
```

Success criterion:

- normalize repeated signatures by their repeated value;
- eliminate the repeated value parameter;
- reduce the normalized boundary triples to a two-parameter line pencil;
- state the resulting residue target without claiming a new estimate.

Failure criterion:

- count repeated signatures twice as an equality;
- hide triple-repeat signatures;
- turn a compiler into an unproved asymptotic bound.

## Normalized Boundary

Let a repeated source be `(a,a,b)` with `a,b in H`; this includes `b=a`, the
triple-repeat case.  Since `a != 0`, divide a distinct same-signature ordered
triple `(x,y,z)` by `a` and write

```text
u=x/a, v=y/a, w=z/a, lambda=b/a.
```

Then `u,v,w,lambda in H`, the first three entries are distinct, and

```text
u+v+w = 2 + lambda,
uv+uw+vw = 1 + 2 lambda.
```

Eliminating `lambda` gives

```text
lambda = u+v+w-2 in H,
uv+uw+vw = 2(u+v+w)-3.
```

After centering at `1`, with

```text
U=u-1, V=v-1, W=w-1,
```

the second equation is simply

```text
UV + UW + VW = 0.
```

A distinct boundary triple cannot have any of `u,v,w` equal to `1`.  Hence
`U,V,W` are nonzero, and `U+V != 0`; otherwise `UV+W(U+V)=UV` would vanish.
Therefore `W` is forced by `U,V`:

```text
W = -UV/(U+V).
```

Equivalently,

```text
w = 1 - (u-1)(v-1)/(u+v-2).
```

Thus the normalized boundary count is a two-variable rational membership
count: choose ordered `u,v in H\{1}`, then test that this `w` lies in `H` and
that `lambda=u+v+w-2` lies in `H`.

## Line Pencil

Set

```text
t = v-1,    r = (u-1)/(v-1).
```

Then every normalized ordered boundary triple is represented uniquely by
`(r,t)` with `t != 0`, `r notin {0,-1}`, and

```text
v      = 1 + t,
u      = 1 + r t,
w      = 1 - (r/(r+1)) t,
lambda = 1 + ((r^2+r+1)/(r+1)) t.
```

Define `B_line` to be the number of pairs `(r,t)` for which these four affine
forms lie in `H` and the first three are distinct.  Then

```text
D_boundary <= n B_line.
```

The inequality, rather than equality, is deliberate: a double-repeat signature
can have two repeated sources related by the involution from the previous
packet, and the source-normalized count may count the same signature twice.

The repeated-signature count also has the elementary bound

```text
Z_repeat <= n^2,
```

because repeated signatures are images of the `n^2` choices `(a,b) in H^2`.

Combining with the repeat-residue boundary compiler gives the line-pencil
residue target:

```text
repeat_residue <= 12 n B_line + 18 n^2.
```

So the moment route can pay the residue by proving a line-pencil bound for
`B_line`.

## Degenerate Line Parameters

The first three affine coefficients are

```text
1,  r,  -r/(r+1).
```

In characteristic not `2`, they collide only at

```text
r in {0, -1, 1, -1/2, -2}.
```

The values `0` and `-1` are already invalid, while `1`, `-1/2`, and `-2`
force equality among `u,v,w` and are excluded by the distinctness condition.

The fourth coefficient vanishes when

```text
r^2+r+1 = 0.
```

This is the triple-repeat cell `lambda=1`; it is not invalid, but it is a
lower-condition subcell that a future line-pencil theorem may handle
separately.

## Replay

Standalone only:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_line_compiler.py
```

Expected digest:

```text
H3_REPEAT_BOUNDARY_LINE_COMPILER_PASS
```
