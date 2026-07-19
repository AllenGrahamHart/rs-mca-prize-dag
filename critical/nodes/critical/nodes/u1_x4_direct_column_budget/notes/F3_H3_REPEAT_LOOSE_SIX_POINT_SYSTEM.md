# F3 h=3 repeat loose six-point system

Status: PROVED COMBINATORIAL/ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet rewrites the loose-triangle obstruction as an explicit six-point
additive system in the reciprocal image

```text
S = {1/(u-1) : u in H, u != 1}.
```

## System

A triangle in the active-pair graph has core vertices `r,s,t`.  The three
active-pair owners have reciprocal third coordinates

```text
a = -(r+s),
b = -(r+t),
c = -(s+t).
```

The triangle is contained in one active edge exactly when

```text
r+s+t = 0.
```

The genuine loose obstruction is the complementary case:

```text
r+s+t != 0.
```

Then the six reciprocal coordinates

```text
r, s, t, -(r+s), -(r+t), -(s+t)
```

are distinct, lie in `S`, and form the three active zero-sum edges

```text
{r,s,-(r+s)},
{r,t,-(r+t)},
{s,t,-(s+t)}.
```

The pairwise intersections are exactly `{r}`, `{s}`, and `{t}`, and the total
intersection is empty.

## Algebraic Conditions

A loose six-point system is therefore:

```text
r,s,t in S,
-(r+s), -(r+t), -(s+t) in S,
Lambda(r,s), Lambda(r,t), Lambda(s,t) in H,
r+s+t != 0,
```

where

```text
Lambda(x,y)=1+1/x+1/y-1/(x+y).
```

Thus `H3-NO-LOOSE-TRIANGLE` is equivalent to absence of this system.

## Guardrails

Boundary-style witness rows have no loose six-point systems:

```text
p=337   n=16  active_pairs=3  six_point_systems=0
p=2017  n=32  active_pairs=3  six_point_systems=0
p=4801  n=64  active_pairs=3  six_point_systems=0
p=7937  n=64  active_pairs=6  six_point_systems=0
p=65537 n=256 active_pairs=24 six_point_systems=0
p=91393 n=256 active_pairs=6  six_point_systems=0
```

The contrast row has two loose six-point systems:

```text
p=97 n=32 active_pairs=45 six_point_systems=2
```

## Role in h=3

The pairwise-coreless branch is now an explicit additive incidence theorem on
`S`: prove that the six-point system above has no boundary-regime solutions.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_six_point_system.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_SIX_POINT_SYSTEM_PASS
```
