# F3 h=3 rich-curve rank stress

Status: MACHINE-VERIFIED FINITE-FIELD STRESS TEST, NOT `RC-RANK`.

This packet strengthens the local evidence around the h=3 rank-form
nonvanishing target.  It does not prove the rich-curve theorem.  It checks that
the corrected `RC-RANK` inequality distinguishes known bad degeneracies from
several repaired or non-collapsed toy curves, and it records one family-level
warning: an individually passing low-rank curve cannot be counted with
arbitrary multiplicity.

## Pre-registration

Question:

```text
In the same exact finite-field toy row as the rank sample, does the weaker
rank target behave correctly on repaired curves, collapsed curves, and repeated
families?
```

Success criterion:

- compute exact substitution ranks over `F_769`;
- verify several non-collapsed controls pass the one-curve rank target without
  needing full coefficient rank;
- derive the repeated-family rank consequence for a low-rank passing curve;
- keep the result labelled as stress evidence only.

Failure criterion:

- every passing example requires full coefficient rank;
- an individually passing curve is silently treated as safe under unlimited
  multiplicity.

## Toy Row

The replay uses

```text
p=769, h=32, A=5, B=4, D=1.
```

The coefficient box has dimension

```text
A B^3 = 320.
```

The `RC-RED(13)` condition count per curve is

```text
13 D (A + D) = 78.
```

The companion rank sample already verifies the collapsed control and full-rank
random control:

```text
constant-ratio collapsed:  rank 50   < 78   (fails)
repaired random:           rank 320  > 78   (full coefficient rank)
```

This stress packet adds the following exact ranks:

```text
private-divisor rational:  rank 293  > 78   (passes, not full rank)
shifted polynomial:        rank 247  > 78   (passes, not full rank)
shared denominator:        rank 247  > 78   (passes, not full rank)
```

At the family level, repeating the same low-rank image does not increase rank.
The verifier derives the following consequences from the private-divisor rank:

```text
private curve repeated twice:       rank 293 > 156  (passes)
private curve repeated four times:  rank 293 < 312  (fails)
```

## Interpretation

This calibrates the theorem target:

- `RC-RANK` is genuinely weaker than full injectivity.  The private-divisor,
  shifted, and shared-denominator examples all pass the rank inequality while
  having rank below `A B^3`.
- Constant-ratio collapse is still detected and must stay excluded or paid.
- A low-rank one-curve pass is not enough to justify counting many copies of
  the same image.  The geometric batching theorem must count repaired
  inequivalent curve images, not raw multiplicity.
- The full-rank control remains in `F3_H3_RICH_CURVE_RANK_SAMPLE.md`: in this
  fixed box, a full-rank subcurve certifies any containing/duplicate family up
  to `Z=4`, after which the condition count exceeds the coefficient dimension.

The open theorem is unchanged: prove a uniform lower bound of the form

```text
rank(S_Z) > 13 D (A + D) |Z|
```

for the actual repaired F3 signature-curve families supplied by the geometric
bridge.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_rank_stress.py
```

Expected digest:

```text
H3_RICH_CURVE_RANK_STRESS_PASS
```
