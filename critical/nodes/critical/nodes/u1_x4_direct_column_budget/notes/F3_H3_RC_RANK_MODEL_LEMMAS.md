# F3 h=3 RC-RANK model lemmas

Status: PROVED MODEL LEMMAS / THEOREM-STATEMENT REPAIR, NOT `RC-RANK`.

This packet records two algebraic facts that sharpen the remaining h=3
nonvanishing target.  It does not prove the needed rank lower bound for actual
F3 signature-curve families.

## Pre-registration

Question:

```text
Which parts of the finite-field RC-RANK guardrails are forced by algebra, and
which part is still the genuine lower-bound theorem?
```

Success criterion:

- prove the exact constant-ratio collapsed rank formula;
- prove the private-linear degree-space ceiling and the resulting `H` floor;
- keep the private-linear lower-bound theorem separate from these model facts.

Failure criterion:

- promote the private-linear model to `RC-RANK`;
- ignore the tiny-`H` dimension obstruction;
- treat duplicate curve images as new rank.

## Constant-ratio collapsed rank

For the collapsed model

```text
r_i(X) = c_i X,
0 <= a < A,
0 <= b_i < B,
```

the substituted monomial is a scalar multiple of

```text
X^(a + H(b_1 + b_2 + b_3)).
```

Thus the rank is exactly

```text
| { a + Hs : 0 <= a < A, 0 <= s <= 3(B-1) } |.
```

In particular, if `H >= A`, the intervals do not overlap and the rank is

```text
A(3B - 2).
```

For the pinned toy box `A=5, B=4, H=32`, this gives rank `50`, matching the
finite-field rank sample.  Since the one-curve condition count is `78`, this
collapsed image has rank capacity `0`.  This is why the constant-ratio cells
must remain excluded or paid before applying `RC-RANK`.

## Private-linear degree ceiling

For private-linear rational maps

```text
r_i(X) = (X-alpha_i)/(X-beta_i),
```

after clearing the common denominator, each coefficient-box monomial becomes

```text
X^a prod_i (X-alpha_i)^(H b_i) (X-beta_i)^(H(B-1-b_i)).
```

Every such polynomial has degree at most

```text
(A - 1) + 3H(B - 1),
```

so any one-curve private-linear substitution rank is bounded above by

```text
min(A B^3, A + 3H(B - 1)).
```

Consequently even a perfect degree-space fullness theorem cannot imply
one-curve `RC-RANK` unless

```text
A + 3H(B - 1) > 13 D (A + D).
```

For the pinned toy box `A=5, B=4, D=1`, this gives the exact floor `H >= 9`.
That explains the existing guardrail: `H=8` fails by dimension, while `H=16`
has degree-space room.

## Remaining theorem

The lower bound still needed for `RC-RANK` is not contained in this packet.  A
usable next theorem would be:

```text
Private-linear degree-space fullness:
  under explicit repaired/private-divisor hypotheses, the one-curve
  substitution rank equals min(A B^3, A + 3H(B - 1)).
```

The existing finite-field guardrail verifies this equality for one control at
`H in {4,8,16,32,64}`.  This packet explains why that equality is the right
target and why the theorem must print an `H` floor; it does not prove the
uniform equality.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rc_rank_model_lemmas.py
```

Expected digest:

```text
H3_RC_RANK_MODEL_LEMMAS_PASS
```
