# F3 h=3 private-linear p-specific rank-drop guardrail

Status: VERIFIED FINITE-FIELD GUARDRAIL, NOT `RC-RANK`.

This packet records a characteristic-specific rank drop in the private-linear
model.  It does not refute the official-row private-linear route, but it
prevents a common overstatement: characteristic-zero degree-space fullness is
not enough by itself.  The actual theorem must be a finite-row rank-avoidance
statement, excluding primes where the relevant minors vanish.

## Setup

Take

```text
A=1, B=5, H=9,
(alpha_1,beta_1)=(2,3),
(alpha_2,beta_2)=(5,7),
(alpha_3,beta_3)=(11,13).
```

Consider the private-linear cleared span

```text
span prod_i (X-alpha_i)^(H b_i)(X-beta_i)^(H(B-1-b_i)),
0 <= b_i < B.
```

The coefficient-box size is `B^3=125`, while the degree-space dimension is

```text
A + 3H(B-1) = 109.
```

## Exact Rank Behavior

The verifier computes the same integer coefficient matrix modulo several
primes:

```text
p=1009:  rank 108
p=1013:  rank 109
p=1019:  rank 109
p=1231:  rank 109
p=2027:  rank 109
p=5003:  rank 109
p=10007: rank 109
p=65537: rank 109
```

Because the rank is `109` modulo `1013`, the rational rank of the integer
matrix is also `109`, the full degree-space dimension.  The drop at `p=1009`
is therefore a genuine p-specific minor-vanishing event, not a rational
dependency.

## Consequence

The remaining private-linear h=3 theorem cannot be stated as:

```text
prove degree-space fullness in characteristic zero, then reduce modulo p.
```

It must instead be a row-level finite-field statement:

```text
for the repaired F3 signature-curve parameter image and official row prime p,
at least one rank-good minor remains nonzero modulo p.
```

This is exactly why the rank-avoidance interface is phrased as
`F3-PRIVATE-LINEAR-RANK-AVOID`, not merely as a characteristic-zero fullness
lemma.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_bad_prime_guardrail.py
```

Expected digest:

```text
H3_PRIVATE_LINEAR_BAD_PRIME_GUARDRAIL_PASS
```
