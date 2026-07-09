# F3 h=3 repeat loose affine-slope compiler

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet rewrites the normalized loose system as a nine-slope affine line
problem.

## Slopes

With the normalized variables

```text
s=ar, t=br, X=1/r,
```

all subgroup membership tests have the form

```text
1 + c_i X in H.
```

The six coordinate slopes are

```text
1,
1/a,
1/b,
-1/(1+a),
-1/(1+b),
-1/(a+b).
```

The three lambda slopes are

```text
1 + 1/a - 1/(1+a),
1 + 1/b - 1/(1+b),
1/a + 1/b - 1/(a+b).
```

Therefore a loose obstruction is exactly a non-pole parameter pair `(a,b)`,
with `1+a+b != 0`, for which one affine line

```text
X -> 1 + c_i X
```

hits `H` at all nine listed slopes.

## Guardrails

Boundary-style witness rows have no such affine nine-slope systems:

```text
p=337   n=16  loose_systems=0
p=2017  n=32  loose_systems=0
p=4801  n=64  loose_systems=0
p=7937  n=64  loose_systems=0
p=65537 n=256 loose_systems=0
p=91393 n=256 loose_systems=0
```

The contrast row has two loose systems, twelve ordered normalizations, and six
distinct sorted nine-slope sets:

```text
p=97 n=32 loose_systems=2 ordered_normalizations=12 affine_slope_sets=6
```

## Role in h=3

The pairwise-coreless branch is now an explicit affine-line rich-subgroup
problem.  Proving that the nine-slope condition has no boundary-regime
solutions proves `H3-NO-LOOSE-TRIANGLE`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_affine_slope_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_AFFINE_SLOPE_COMPILER_PASS
```
