# F3 h=3 rich-curve rank sample

Status: MACHINE-VERIFIED FINITE-FIELD SAMPLE, NOT `RC-RANK`.

This packet stress-tests the corrected rank-form nonvanishing target from
`F3_H3_RICH_CURVE_NV_RANK_AUDIT.md`.  It compares a deliberately collapsed
constant-ratio family against a deterministic repaired random degree-2
rational curve.

## Pre-registration

Question:

```text
Does the rank-form target separate repaired degree-2 curves from the known
constant-ratio degeneracy in an exact finite-field toy row?
```

Success criterion:

- compute the cleared substitution rank exactly over a finite field;
- verify that the constant-ratio collapsed control fails `RC-RANK`;
- verify that a deterministic repaired random curve has rank above the
  `RC-RED(13)` condition count;
- keep the result labelled as sample evidence, not a theorem.

Failure criterion:

- the collapsed control passes the rank target;
- the repaired random sample has rank below the condition count;
- the script requires a large local matrix.

## Toy row

The replay uses

```text
p=769, h=32, A=5, B=4, D=1.
```

The coefficient space has dimension

```text
A B^3 = 320.
```

The `RC-RED(13)` condition count for one curve is

```text
13 D (A + D) = 78.
```

The constant-ratio control

```text
r_1=X, r_2=3X, r_3=5X
```

has rank `50`, so it fails the rank target.  This is the intended behavior:
the known collapsed condition family must be excluded or paid.

The deterministic repaired random degree-2 curve has rank `320`, full
coefficient rank in this toy box, hence passes the toy `RC-RANK` inequality
with large margin:

```text
320 > 78.
```

## Interpretation

This does not prove `RC-RANK`.  It is a useful guardrail: the rank target
detects the already-known degeneracy while repaired random curves behave as
the proof strategy requires.  The next theorem still has to prove a uniform
rank lower bound for the actual repaired F3 signature-curve family.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_rank_sample.py
```

Expected digest:

```text
H3_RICH_CURVE_RANK_SAMPLE_PASS
```
