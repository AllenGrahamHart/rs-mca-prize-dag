# F3 h=3 repeat-boundary LP4 rank guardrail

Status: REFUTED LP4 FULL-DEGREE-SPACE SHORTCUT.

This packet prevents a false shortcut in the repeat-boundary LP4 route.  The
LP4 compiler needs a genuine rank/nonvanishing theorem; it cannot be replaced
by the assertion that products of distinct affine factors span the whole
available degree space.

## Pre-registration

Question:

```text
Can the LP4 nonvanishing gate be shortcut by claiming generic affine-factor
products span every polynomial degree up to the degree cap?
```

Success criterion:

- test the smallest exact two-factor affine model;
- record an exact rational relation if the shortcut fails;
- state the corrected proof obligation.

Failure criterion:

- use only a finite-field rank drop without an exact relation;
- confuse this guardrail with a refutation of the LP4 route itself.

## Refuted Shortcut

For distinct affine roots `alpha_i`, a tempting claim is:

```text
span { X^a prod_i (X-alpha_i)^(H b_i) }
```

has dimension

```text
min(A B^m, A + m H (B-1)).
```

This is already false for two factors.

Take

```text
A=1, B=3, H=2, alpha_1=2, alpha_2=5.
```

For

```text
P_ij(X) = (X-2)^(2i) (X-5)^(2j),    0 <= i,j <= 2,
```

there are nine polynomials of degree at most eight, so the shortcut predicts
rank `9`.  The exact rank over `Q` is `8`, with integer relation

```text
81 P_00 - 18 P_01 + P_02 - 18 P_10 - 2 P_11 + P_20 = 0.
```

## Consequence

The repeat-boundary LP4 theorem cannot be proved by a naive full-degree-space
claim for each line.  A valid proof must use one of:

- the actual line-pencil family structure across `r`;
- a weaker rank threshold matching `5D(A+D)|R|`;
- a different support or incidence argument.

This does not refute the LP4 route.  It only removes an overstrong shortcut.

## Replay

Standalone exact replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_lp4_rank_guardrail.py
```

Expected digest:

```text
H3_REPEAT_BOUNDARY_LP4_RANK_GUARDRAIL_PASS
```
