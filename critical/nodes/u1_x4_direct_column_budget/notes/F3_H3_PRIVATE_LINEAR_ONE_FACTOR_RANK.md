# F3 h=3 private-linear one-factor rank lemma

Status: PROVED LOCAL RANK LEMMA, NOT THE THREE-FACTOR `RC-RANK` THEOREM.

This packet proves the one-generator version of the private-linear rank target.
It is a local algebra lemma for the remaining h=3 private-linear route: a
single private-linear factor has exactly the expected span dimension.  The full
h=3 theorem still needs the corresponding three-factor product lower bound and
the bridge/rank-capacity assignment.

## Statement

Let `alpha != beta` in a field, let `H,A,B >= 1`, and define

```text
V = span { X^a (X-alpha)^(H b) (X-beta)^(H(B-1-b))
           : 0 <= a < A, 0 <= b < B }.
```

Then

```text
dim V = min(A B, A + H(B-1)).
```

Equivalently, each new private-linear level contributes `A` dimensions while
the valuation windows are disjoint, and then contributes exactly `H` new
dimensions once the windows overlap.

## Proof

Use the `alpha`-adic valuation filtration.  For a fixed `b`, write

```text
F_b(X) = (X-alpha)^(H b) (X-beta)^(H(B-1-b)).
```

Since `alpha != beta`, the second factor is a unit at `alpha`.  Also
`{1,X,...,X^(A-1)}` maps invertibly to the first `A` jets at `alpha` by
translation.  Therefore

```text
F_b * span{1,X,...,X^(A-1)}
```

has nonzero associated-graded pieces exactly in valuation degrees

```text
H b, H b + 1, ..., H b + A - 1.
```

For a finite-dimensional subspace of `F[X]`, its dimension is the number of
nonzero one-dimensional associated-graded valuation pieces.  Hence `dim V` is
the size of the union of intervals

```text
[H b, H b + A - 1],  0 <= b < B.
```

If `A <= H`, these intervals are disjoint and the size is `AB`.  If `A > H`,
they overlap consecutively and the union is the single interval
`[0, H(B-1)+A-1]`, whose size is `A+H(B-1)`.

Thus in all cases

```text
dim V = min(A B, A + H(B-1)).
```

## Role in h=3

For the private-linear h=3 model the cleared three-factor monomials are
products of three such one-factor levels, together with the source factor
`X^a`.  This lemma proves that no rank loss is present in any single
private-linear generator.  The remaining private-linear `RC-RANK` theorem is
the genuinely multigenerator statement:

```text
rank span X^a prod_i (X-alpha_i)^(H b_i)(X-beta_i)^(H(B-1-b_i))
  = min(A B^3, A + 3H(B-1))
```

under repaired distinctness/nondegeneracy hypotheses.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_one_factor_rank.py
```

Expected digest:

```text
H3_PRIVATE_LINEAR_ONE_FACTOR_RANK_PASS
```
