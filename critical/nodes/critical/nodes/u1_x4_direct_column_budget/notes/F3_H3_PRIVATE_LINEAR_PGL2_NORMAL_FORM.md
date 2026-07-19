# F3 h=3 private-linear PGL2 normal form

Status: PROVED RANK-INTERFACE NORMAL FORM, NOT `RC-RANK`.

This packet reduces the private-linear rank-avoidance target to a smaller
parameter space.  It uses the source-Mobius rank invariance from
`F3_H3_RC_RANK_NORMALIZATION_INVARIANCE.md`: changing the source coordinate by
`PGL_2` and rescaling target coordinates does not change the cleared
substitution rank.

## Pre-registration

Question:

```text
After quotienting by source Mobius changes and target scalings, what normal
form represents a repaired private-linear h=3 triple?
```

Success criterion:

- give an explicit source Mobius transformation;
- reduce an ordered triple of private-linear maps to three parameters;
- verify the normal form over finite fields and in the small rank replay;
- keep the rank-good minor theorem separate.

Failure criterion:

- promote the normal form to `RC-RANK`;
- hide collision exclusions among zeros and poles;
- use a normalization that changes the cleared substitution rank.

## Normal Form

Let

```text
r_i(X) = (X-alpha_i)/(X-beta_i),     i=1,2,3,
```

with the six points distinct in `P^1`.  Assume, after permuting coordinates if
needed, that `alpha_1`, `beta_1`, and `alpha_2` are distinct finite points.
Define

```text
T(X) =
  ((X-alpha_1)/(X-beta_1))
  / ((alpha_2-alpha_1)/(alpha_2-beta_1)).
```

Then

```text
T(alpha_1)=0,        T(beta_1)=infinity,        T(alpha_2)=1.
```

In the source coordinate `Y=T(X)`, and after harmless target scalings, the
triple has the form

```text
r_1(Y) = Y,
r_2(Y) = (Y-1)/(Y-lambda),
r_3(Y) = (Y-eta)/(Y-theta),
```

where

```text
lambda = T(beta_2),
eta    = T(alpha_3),
theta  = T(beta_3).
```

The distinctness assumptions become the usual open conditions that
`lambda, eta, theta` are finite and avoid the relevant collisions with
`0,1,infinity` and each other.

## Rank Role

By source-Mobius invariance, target scaling invariance, target permutation, and
target inversion, the private-linear rank theorem may be stated on this
three-parameter normal-form family without changing the `RC-RANK` inequality.

Thus the remaining private-linear rank-avoidance theorem can be sharpened to:

```text
For the repaired F3 private-linear parameter image in
  (lambda, eta, theta),
at least one rank-good minor for the printed official-row box remains nonzero
over the actual row field.
```

This packet proves only the normalization.  It does not prove that the F3
parameter image avoids the bad-minor locus.

## Replay

Standalone only:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_pgl2_normal_form.py
```

Expected digest:

```text
H3_PRIVATE_LINEAR_PGL2_NORMAL_FORM_PASS
```
