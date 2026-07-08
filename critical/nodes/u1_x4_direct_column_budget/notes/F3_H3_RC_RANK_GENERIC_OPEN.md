# F3 h=3 RC-RANK generic-open reduction

Status: PROVED ALGEBRAIC REDUCTION / NONEMPTY MODEL OPEN SET, NOT `RC-RANK`.

This packet turns part of the h=3 rank problem into a precise algebraic
avoidance statement.  It does not prove that the actual repaired F3
signature-curve families lie in the good locus.

## Pre-registration

Question:

```text
Can the private-linear degree-space fullness target be reformulated as a
nonzero-minor condition, and is that condition non-vacuous?
```

Success criterion:

- state the universal-minor reduction for fixed `A,B,D,H`;
- use the existing exact finite-field private-linear witness to prove the good
  locus is nonempty in the model family;
- keep the actual F3 curve-image avoidance theorem explicit.

Failure criterion:

- promote generic openness to `RC-RANK`;
- claim every private-linear curve has degree-space fullness;
- forget that repeated curve images do not add rank.

## Universal-Minor Reduction

Fix Stepanov parameters `A,B,D,H`.  In any algebraic family of repaired
rational curves, after clearing denominators the substitution map has a
coefficient matrix whose entries are polynomial functions of the curve
parameters.  Therefore

```text
rank >= r
```

is equivalent to the nonvanishing of at least one `r x r` minor of this
universal coefficient matrix.  The rank-good locus is consequently Zariski
open.  Proving `RC-RANK` for the actual F3 family can be phrased as proving
that the repaired signature-curve parameter image avoids the common zero set
of all minors of size

```text
13 D (A + D) |Z| + 1.
```

This is weaker and better targeted than full coefficient injectivity.

## Private-Linear Nonemptiness Witness

For the pinned toy row

```text
p = 769, H = 32, A = 5, B = 4, D = 1,
conditions = 13 D(A+D) = 78,
coefficients = A B^3 = 320,
```

the private-linear model

```text
(X-2)/(X-3), (X-5)/(X-7), (X-11)/(X-13)
```

has exact substitution rank

```text
293 = A + 3H(B-1).
```

Since this rank is computed over `F_769`, at least one `293 x 293` minor of
the corresponding integer universal matrix is nonzero modulo `769`, and hence
is not the zero polynomial.  Thus the private-linear degree-space-fullness
locus is nonempty.

The same rank gives finite rank-capacity `3` in the toy box:

```text
293 > 3 * 78,       293 < 4 * 78.
```

This agrees with the rank-effective bridge packet and again shows why
duplicate curve images must be charged by capacity rather than raw
multiplicity.

## Remaining Theorem

The useful next theorem is now sharply stated:

```text
F3-RANK-AVOID:
  after the toral, constant-ratio, and hyperbola-line cells are paid or
  excluded, the repaired h=3 signature-curve parameter image lies in a
  rank-good minor open set with enough rank capacity for the bridge budget.
```

This packet proves that such open sets are algebraically meaningful and
nonempty in the private-linear model.  It does not prove `F3-RANK-AVOID`.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rc_rank_generic_open.py
```

Expected digest:

```text
H3_RC_RANK_GENERIC_OPEN_PASS
```
