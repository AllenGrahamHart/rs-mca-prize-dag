# F3 h=3 repeat same-lambda scale count

Status: PROVED TRIVIAL COUNT COMPILER, NOT `H3-VALUE-INJECTIVE`.

This packet gives a direct count bound for the exceptional `lambda=1` scale
branch in the same-lambda collision target.

## Bound

When the field contains a primitive cube root `omega`, a `lambda=1` scale edge
has the form

```text
{1+x, 1+omega x, 1+omega^2 x} subset H,
```

with `x != 0`, modulo `x -> omega x`.

The condition `1+x in H` injects representatives into `H \ {1}`.  Each
nonzero scale orbit has three representatives, so the number of admissible
scale orbits satisfies

```text
K_1 <= floor((n-1)/3).
```

Therefore the number of same-lambda scale collision pairs is bounded by

```text
binom(floor((n-1)/3), 2).
```

If the field has no primitive cube root of unity, this branch is empty.

## Official Rows

For every official row `n=2^s`, `13 <= s <= 41`, this pair bound is below
`n^2`.

## Role in h=3

This does not prove the `lambda=1` scale part of `H3-VALUE-INJECTIVE`.
Instead, it shows that the exceptional scale branch is already quadratically
bounded and can be separated in count/payment routes.  The generic
`lambda != 1` same-lambda branch remains the main injectivity target.

The companion `F3_H3_REPEAT_LAMBDA_ONE_SCALE_H2_CAP.md` improves the count
route on larger official rows by applying the h=2 affine-coset pair corollary:

```text
K_1 <= floor(ceil(66 n^(2/3))/3).
```

This first beats the trivial orbit count at `n=2^19`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_scale_count.py
```

Expected digest:

```text
H3_REPEAT_SAME_LAMBDA_SCALE_COUNT_PASS
```
