# F3 h=3 rich-curve nonvanishing rank audit

Status: PROVED ARITHMETIC TARGET REPAIR, NOT `RC-NV`.

This packet clarifies the remaining h=3 rich-curve nonvanishing gate.  The
right target is not full injectivity of the substitution map from the
`A B^3`-dimensional auxiliary coefficient box.  In the parameter boxes used by
the reduced-condition compiler, full injectivity is sometimes impossible by
plain dimension.  What T1 needs is weaker and exact: the substitution image
rank over the curve family must exceed the number of imposed log-jet
conditions.

## Pre-registration

Question:

```text
After RC-RED(13), what is the exact linear-algebraic nonvanishing target?
Is it plausible as full injectivity, or must it be a rank statement?
```

Success criterion:

- compute the coefficient dimension, condition count, and one-curve degree cap
  for the current compiler rows;
- exhibit rows where full injectivity is dimensionally impossible;
- state the sufficient rank inequality that replaces the naive injectivity
  target.

Failure criterion:

- the audit silently treats the one-curve degree cap as a proved rank lower
  bound;
- the corrected target is strong enough to be impossible in the sampled rows;
- the note promotes `RC-NV`.

## Linear algebra

Let `V` be the auxiliary coefficient space, so

```text
dim V = A B^3.
```

Let `K: V -> conditions` be the over-imposed log-jet condition map supplied by
`RC-RED(13)`.  For a family `Z` of curves, the condition count is

```text
13 D (A + D) |Z|.
```

Let `S_Z` be the cleared substitution map from `V` to the direct sum of the
one-variable polynomial spaces on the curves in `Z`.  A nonzero auxiliary
survives nonvanishing if

```text
ker K is not contained in ker S_Z.
```

A sufficient rank condition is therefore

```text
rank(S_Z) > 13 D (A + D) |Z|.       (RC-RANK)
```

This is the rank form of the remaining `RC-NV` gate.

The exact reduced-condition profile strengthens the right-hand side to

```text
rank(S_Z) > (DA + 6D(D-1)) |Z|.
```

Existing legacy audits keep the larger `13D(A+D)|Z|` target as a conservative
sufficient form; future optimizers should use the exact profile.

## Why full injectivity is too strong

For one curve, the cleared substitution degree is

```text
L(A,B,h) = (A - 1) + 6 h (B - 1).
```

For `|Z|` curves, the direct-sum image dimension is at most

```text
|Z| (L(A,B,h) + 1).
```

In the first three compiler rows, `A B^3` exceeds this image cap.  Thus the
substitution map has a nontrivial kernel for dimension reasons alone, before
any degeneracy is considered.  A sparse nonvanishing proof cannot honestly
claim full injectivity on the whole h=3 coefficient box.

The good news is that every audited row has positive image-cap room above the
condition count.  Thus a rank theorem of the form `(RC-RANK)` is not ruled out
by dimension and is exactly the theorem the next T1 step should prove.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_nv_rank_audit.py
```

Expected digest:

```text
H3_RICH_CURVE_NV_RANK_AUDIT_PASS
```
