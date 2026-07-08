# F3 h=3 repeat loose slope multiplicity

Status: PROVED COMBINATORIAL/ALGEBRAIC LEDGER PLUS FINITE GUARDRAILS.

This packet records the effective number of distinct affine-slope conditions
in the normalized loose target.

## Multiplicity

The six coordinate slopes

```text
1,
1/a,
1/b,
-1/(1+a),
-1/(1+b),
-1/(a+b)
```

are distinct under the full normalized loose-system hypotheses: non-poles plus
six-point distinctness.  This is the coordinate-slope distinctness packet.  The
three lambda slopes are also mutually distinct in a genuine loose system; this
is the lambda-slope collision packet.  They can still collide with coordinate
slopes along nine explicit divisors, so a future counting theorem should use
the distinct slope count rather than blindly assuming nine distinct conditions.

## Guardrails

Boundary-style witness rows have no loose systems, hence no slope patterns.

The contrast row has two loose systems and twelve ordered normalizations.  In
that row six ordered normalizations have nine distinct slopes and six have
eight distinct slopes with one duplicate:

```text
p=97 n=32 distinct_range=8..9 max_multiplicity=2
patterns=(1,1,1,1,1,1,1,1,1):6; (2,1,1,1,1,1,1,1):6
```

## Role in h=3

The loose affine-line target should be stated as:

```text
all distinct slopes in C(a,b) hit H on one affine line X -> 1+cX.
```

For generic nondegenerate systems this may be nine conditions, but the compiler
keeps the effective condition count explicit.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_slope_multiplicity.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_SLOPE_MULTIPLICITY_PASS
```
