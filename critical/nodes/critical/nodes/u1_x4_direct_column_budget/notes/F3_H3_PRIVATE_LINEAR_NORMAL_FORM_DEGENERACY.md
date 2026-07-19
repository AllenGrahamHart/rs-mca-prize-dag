# F3 h=3 private-linear normal-form degeneracy chart

Status: PROVED NORMAL-FORM OPEN-SET LEMMA, NOT `RC-RANK`.

This packet records the explicit degeneracy divisors in the private-linear
PGL2 normal form

```text
r_1(Y) = Y,
r_2(Y) = (Y-1)/(Y-lambda),
r_3(Y) = (Y-eta)/(Y-theta).
```

It is a theorem-statement hygiene lemma for the private-linear rank route.  It
does not prove any rank lower bound.

## Pre-registration

Question:

```text
In the three-parameter private-linear normal form, which parameter collisions
must be excluded before applying a private-linear rank theorem?
```

Success criterion:

- state the private-divisor open conditions in `(lambda,eta,theta)`;
- classify pairwise constant-ratio collapse in this chart;
- verify the classification over finite fields;
- keep the rank theorem and bridge theorem separate.

Failure criterion:

- hide zero/pole collisions behind generic wording;
- claim that excluding these divisors proves `RC-RANK`;
- forget that the constant-ratio filter is only one degeneracy class.

## Open Conditions

The six zero/pole points in the normal form are

```text
0, infinity, 1, lambda, eta, theta.
```

The private-divisor open set is therefore

```text
lambda, eta, theta notin {0,1},
lambda, eta, theta pairwise distinct.
```

These conditions say exactly that the three private-linear maps have distinct
zeros and poles.

## Constant-Ratio Collapse

The ratios `r_1/r_2` and `r_1/r_3` are never constant in this chart.  The only
possible pairwise constant-ratio collapse is between `r_2` and `r_3`.

Indeed,

```text
r_2/r_3 constant
  <=> (Y-1)(Y-theta) is proportional to (Y-lambda)(Y-eta).
```

Both sides are monic quadratics, so proportionality is equality.  Therefore

```text
{1, theta} = {lambda, eta}.
```

Equivalently,

```text
(lambda=1 and eta=theta) or (eta=1 and lambda=theta).
```

Both alternatives are outside the private-divisor open set.  Thus, in the
private-linear normal form, the private-divisor conditions automatically
exclude pairwise constant-ratio collapse.

## Role

The private-linear rank-avoidance theorem may now be stated on the explicit
normal-form open set:

```text
(lambda,eta,theta) in A^3
minus {lambda,eta,theta in {0,1} or lambda=eta or lambda=theta or eta=theta}.
```

On this open set, the constant-ratio degeneracy filter has nothing further to
remove.  The remaining task is still the finite-row rank-good minor avoidance
theorem over this parameter image, plus the geometric bridge.

## Replay

Standalone only:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_normal_form_degeneracy.py
```

Expected digest:

```text
H3_PRIVATE_LINEAR_NORMAL_FORM_DEGENERACY_PASS
```
