# F3 h=3 repeat loose reciprocal-closure compiler

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet rewrites the loose-triangle shadow condition in the reciprocal
chart

```text
r(u) = 1/(u-1).
```

## Pair Closure

For an active edge `{u,v,w}`, set

```text
r = 1/(u-1),  s = 1/(v-1),  t = 1/(w-1).
```

The shifted reciprocal form `xy+xz+yz=0` is exactly

```text
r+s+t = 0.
```

Thus an active shadow pair `{r,s}` has forced third reciprocal coordinate

```text
t = -(r+s).
```

The lambda condition for that pair is

```text
Lambda(r,s) = 1 + 1/r + 1/s - 1/(r+s) in H.
```

So the active-pair shadow graph is intrinsic in the reciprocal image

```text
S = {1/(u-1) : u in H, u != 1}.
```

A pair `{r,s}` is active exactly when:

```text
r+s != 0,
-(r+s) in S \ {r,s},
Lambda(r,s) in H.
```

## Loose Triangles

Let `{r,s,t}` be a triangle in this active-pair graph.  If

```text
r+s+t = 0,
```

then each pair has the third vertex of the triangle as its active-edge owner,
so the shadow triangle is contained in one active edge.

If

```text
r+s+t != 0,
```

then the three pair owners are distinct and the shadow triangle is exactly the
loose obstruction

```text
{a,b,x}, {a,c,y}, {b,c,z}.
```

Therefore `H3-NO-LOOSE-TRIANGLE` is equivalent to:

```text
every triangle in the reciprocal active-pair graph has r+s+t=0.
```

Equivalently, whenever `r,s,t in S` and all three pair closures

```text
-(r+s), -(r+t), -(s+t)
```

also satisfy the active-pair membership and lambda tests, then

```text
r+s+t = 0.
```

## Guardrails

Finite row checks agree with the coordinate-shadow compiler:

```text
p=337   n=16  active_edges=1 active_pairs=3  contained=1  loose=0
p=2017  n=32  active_edges=1 active_pairs=3  contained=1  loose=0
p=4801  n=64  active_edges=1 active_pairs=3  contained=1  loose=0
p=7937  n=64  active_edges=2 active_pairs=6  contained=2  loose=0
p=65537 n=256 active_edges=8 active_pairs=24 contained=8  loose=0
p=91393 n=256 active_edges=2 active_pairs=6  contained=2  loose=0
```

The non-boundary contrast row has reciprocal closure violations:

```text
p=97 n=32 active_edges=15 active_pairs=45 contained=15 loose=2
```

## Role in h=3

The remaining pairwise-coreless target can now be stated as a pure additive
closure theorem inside the reciprocal image of the multiplicative subgroup.
Together with `H3-VALUE-INJECTIVE` and `H3-SLOPE-HIT`, this would force
`tau_coord <= 1`, hence `repeat_residue <= 90n^2`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_reciprocal_closure_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_RECIPROCAL_CLOSURE_COMPILER_PASS
```
