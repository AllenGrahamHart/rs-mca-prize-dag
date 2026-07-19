# F3 h=3 repeat loose pair-membership compiler

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet writes the active-pair graph used in the loose-triangle target as
explicit reciprocal pair membership functions.

## Pair Functions

Let

```text
S = {1/(u-1) : u in H, u != 1}.
```

For `r,s in S`, with `r+s != 0`, define

```text
U(r,s) = 1 + 1/r,
V(r,s) = 1 + 1/s,
W(r,s) = 1 - 1/(r+s),
Lambda(r,s) = 1 + 1/r + 1/s - 1/(r+s).
```

The first two values are in `H` by `r,s in S`.  The pair `{r,s}` is an active
shadow pair exactly when

```text
W(r,s) in H,
Lambda(r,s) in H,
```

with the registered non-pole and distinctness exclusions.  In reciprocal
coordinates, the active edge over the pair is

```text
{r, s, -(r+s)}.
```

## Loose Target

The loose-triangle target is therefore a triangle theorem for this explicit
pair graph:

```text
if {r,s}, {r,t}, {s,t} are active pairs, then r+s+t=0.
```

If `r+s+t != 0`, the three pair owners are distinct and give the loose
obstruction.

## Guardrails

The compiler agrees exactly with the existing reciprocal pair map.  Boundary
guardrail rows have no loose pair-graph triangle:

```text
p=337   n=16  active_pairs=3  loose=0
p=2017  n=32  active_pairs=3  loose=0
p=4801  n=64  active_pairs=3  loose=0
p=7937  n=64  active_pairs=6  loose=0
p=65537 n=256 active_pairs=24 loose=0
p=91393 n=256 active_pairs=6  loose=0
```

The contrast row has loose pair-graph triangles:

```text
p=97 n=32 active_pairs=45 loose=2
```

## Role in h=3

This is the pair-graph analogue of the ratio membership compilers: the
remaining pairwise-coreless target is now an explicit rational
membership/triangle statement on `S`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_pair_membership_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_PAIR_MEMBERSHIP_COMPILER_PASS
```
