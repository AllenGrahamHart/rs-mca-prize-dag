# F3 h=3 private-linear two-factor induction guardrail

Status: REFUTED NAIVE INDUCTION ROUTE / EXACT RATIONAL COUNTEREXAMPLE.

The one-factor private-linear rank lemma is true, but it cannot be promoted by
a naive factor-by-factor induction.  This packet records the smallest exact
obstruction found: the expected two-factor formula already fails in a rational
example.

## Refuted Claim

A tempting strengthening of `F3_H3_PRIVATE_LINEAR_ONE_FACTOR_RANK.md` is:

```text
dim span { X^a prod_{i=1}^2 (X-alpha_i)^(H b_i)
                         (X-beta_i)^(H(B-1-b_i)) }
  = min(A B^2, A + 2H(B-1)).
```

This is false.

## Counterexample

Over `Q`, take

```text
A=1, B=3, H=2,
(alpha_1,beta_1)=(2,3),
(alpha_2,beta_2)=(5,7).
```

There are `A B^2 = 9` coefficient-box monomials, all of degree at most

```text
A - 1 + 2H(B-1) = 8.
```

The tempting formula predicts rank `9`.  The exact rational rank is only `8`.

With rows ordered by `(b_1,b_2)` lexicographically, the following integer
relation holds:

```text
81 P_00 - 450 P_01 + 625 P_02
- 72 P_10 + 472 P_11 - 800 P_12
+ 16 P_20 - 128 P_21 + 256 P_22 = 0.
```

Thus the rank loss is not a finite-field artifact and not caused by repeated
divisors.

## Consequence

The remaining three-factor private-linear theorem cannot be proved by merely
iterating the one-factor valuation interval lemma.  A valid proof must use a
more global argument, or impose and exploit stronger repaired hypotheses than
pairwise distinct private zeros/poles alone.

This does not refute the official-row private-linear route.  The official
compiler only needs the full three-factor lower bound under the repaired F3
signature-curve hypotheses, and the existing toy three-factor witness still
has rank `293 = A + 3H(B-1)`.  The guardrail only removes a false induction
shortcut.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_two_factor_guardrail.py
```

Expected digest:

```text
H3_PRIVATE_LINEAR_TWO_FACTOR_GUARDRAIL_PASS
```
