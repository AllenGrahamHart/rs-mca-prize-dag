# F3 h=3 repeat loose normalized orbit compiler

Status: PROVED COMBINATORIAL/ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet quotients the normalized loose system by the `S_3` relabeling of
the three core vertices.

## Orbit

For a normalized loose core

```text
s=ar, t=br,
```

the six orderings of the core vertices give the ratio pairs

```text
(a,b),
(b,a),
(1/a,b/a),
(b/a,1/a),
(1/b,a/b),
(a/b,1/b).
```

These are the `S_3` orbit of the normalized pair `(a,b)`.

## Target

The loose affine-slope target should therefore be stated on normalized
`S_3`-orbits:

```text
there is no admissible orbit (a,b) with 1+a+b != 0
whose nine affine slopes all hit H on one line X -> 1+c_i X.
```

## Guardrails

Boundary-style witness rows have no normalized loose orbits:

```text
p=337   n=16  normalized_orbits=0
p=2017  n=32  normalized_orbits=0
p=4801  n=64  normalized_orbits=0
p=7937  n=64  normalized_orbits=0
p=65537 n=256 normalized_orbits=0
p=91393 n=256 normalized_orbits=0
```

The contrast row has two normalized loose orbits.  Each orbit contributes
three distinct sorted nine-slope sets, for six total:

```text
p=97 n=32 loose_systems=2 normalized_orbits=2 representative_slope_sets=6
```

## Role in h=3

This removes the sixfold ordering artifact from the normalized loose target.
Future counting arguments should count normalized `S_3` orbits, not ordered
triples `(r,s,t)`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_normalized_orbit_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_NORMALIZED_ORBIT_COMPILER_PASS
```
