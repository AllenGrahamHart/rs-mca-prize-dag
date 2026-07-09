# F3 h=3 repeat lambda-one scale h=2 cap

Status: PROVED COUNT REFINEMENT, NOT `H3-VALUE-SCALE-INJECTIVE`.

This packet improves the count route for the exceptional `lambda=1` scale
branch by importing the already-proved h=2 affine-coset pair corollary.

## Scale Branch

The lambda-one scale branch consists of scale orbits

```text
{x, omega x, omega^2 x}
```

such that

```text
1+x, 1+omega x, 1+omega^2 x in H.
```

Dropping the third condition gives the two-affine-form system

```text
1+x in H,
1+omega x in H.
```

Normalize by `Y=1+x`.  Then

```text
1+omega x = omega Y + (1-omega).
```

Since `omega != 0` and `1-omega != 0`, this is exactly the shifted affine
coset-pair setting of `F3_H2_AFFINE_COSET_PAIR_STEPANOV.md`.  On official rows
`p >= n^2`, the h=2 hypothesis `n^4 < p^3` is automatic.

Therefore the number of admissible `x` values is at most

```text
66 n^(2/3).
```

Each nonzero scale orbit has three representatives, so

```text
K_1 <= floor(ceil(66 n^(2/3))/3).
```

## Combined Payment

The previous trivial bound

```text
K_1 <= floor((n-1)/3)
```

is sharper on small official rows.  The combined count route uses the minimum
of the two bounds.

The compiler verifies:

```text
first official row n=2^13: combined K_1 <= 2730
first row where h=2 cap is sharper: n=2^19
last official row n=2^41: combined K_1 <= 3720282297
```

The first-official same-lambda scale pair bound remains

```text
3725085.
```

Thus this refinement does not change the first-row ledger, but it makes the
scale payment asymptotically `O(n^(4/3))` instead of quadratic.

## Role

This still does not prove strict scale injectivity.  It strengthens the
alternate count route used when the proof can tolerate a paid exceptional
scale branch.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_one_scale_h2_cap.py
```

Expected digest:

```text
H3_REPEAT_LAMBDA_ONE_SCALE_H2_CAP_PASS
```
