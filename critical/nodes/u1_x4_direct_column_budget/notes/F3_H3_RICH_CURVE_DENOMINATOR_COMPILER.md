# F3 h=3 rich-curve denominator-clearing compiler

Status: PROVED ARITHMETIC COMPILER, T1 groundwork only.

This is the first T1 packet from `notes/codex_briefs/F3_FLIP_20260708.md`.
It pins the denominator-clearing and degree bookkeeping for the proposed
rich-curve Stepanov auxiliary polynomial.  It does not prove the rich-curve
nonvanishing lemma or the final per-row h=3 accident bound.

## Pre-registration

Question:

```text
For degree-2 rational signature-curve maps r_i(X)=P_i(X)/Q_i(X), what is the
exact cleared degree of

    Phi(X, r_1(X)^h, r_2(X)^h, r_3(X)^h)

when Phi has X-degree < A and subgroup-variable degrees < B?
```

Success criterion:

- state a denominator-clearing identity with an explicit degree bound;
- verify it exactly over finite fields for multiple small rows and random
  degree-2 rational maps;
- separate this arithmetic compiler from the still-open T1 nonvanishing and
  coefficient-count steps.

Failure criterion:

- any exact modular check finds that the cleared polynomial does not evaluate
  to the rational expression times its clearing denominator;
- the degree bound needs a larger exponent than the printed formula.

## Compiler

Let

```text
r_i(X) = P_i(X)/Q_i(X),       deg P_i, deg Q_i <= 2,       i=1,2,3,
```

and let

```text
Phi(X,Y_1,Y_2,Y_3)
  = sum c_{a,b_1,b_2,b_3} X^a Y_1^{b_1} Y_2^{b_2} Y_3^{b_3}
```

with

```text
0 <= a < A,        0 <= b_i < B.
```

Define the clearing denominator

```text
D_Q(X) = Q_1(X)^{h(B-1)} Q_2(X)^{h(B-1)} Q_3(X)^{h(B-1)}.
```

Then

```text
D_Q(X) * Phi(X, r_1(X)^h, r_2(X)^h, r_3(X)^h)
```

is the polynomial

```text
sum c_{a,b}
    X^a
    prod_i P_i(X)^{h b_i} Q_i(X)^{h(B-1-b_i)}.
```

Its degree is at most

```text
(A - 1) + 6h(B - 1).
```

This is the degree input for the one-curve degree/multiplicity contradiction
in T1.  If the cleared auxiliary vanishes to multiplicity `D` at `M` non-pole
points and is not the zero polynomial, then

```text
M < ((A - 1) + 6h(B - 1)) / D.
```

The missing T1 work is to choose parameters and prove nonvanishing uniformly
for a family of inequivalent signature curves.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_denominator_compiler.py
```

Expected digest:

```text
H3_RICH_CURVE_DENOMINATOR_COMPILER_PASS
```
