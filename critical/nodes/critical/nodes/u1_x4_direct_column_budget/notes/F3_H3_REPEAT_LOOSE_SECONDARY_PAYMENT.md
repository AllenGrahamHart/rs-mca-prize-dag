# F3 h=3 repeat loose secondary payment

Status: PROVED TRIVIAL PAYMENT COMPILER.

This packet pays the finite secondary subcells inside the two special
one-parameter loose collision branches.

## Input

The secondary-subcell compiler gives residual parameter degrees

```text
branch A: 24,
branch B: 29.
```

So, before row-specific validity filtering, there are at most `24` branch-A
secondary parameters and at most `29` branch-B secondary parameters.

## Payment

For a fixed secondary parameter `a`, the loose target is still a set of
conditions of the form

```text
1 + c_i X in H.
```

The slope `1` condition is always present, so

```text
1 + X in H
```

alone gives at most `n` possible values of `X`.  Hence the total secondary
payment is bounded by

```text
24n + 29n = 53n.
```

For every official row `n=2^s`, `13 <= s <= 41`, this is below `n^2`.

## Role in h=3

The loose branch rank/nonvanishing gates no longer need to cover the finite
secondary subcells.  They may be stated on the clean branch-A and branch-B
loci where exactly eight distinct slopes remain after the primary duplicate.

This does not prove the clean eight-slope branch gates; it removes a finite
exceptional set from them with a direct `O(n)` payment.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_secondary_payment.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_SECONDARY_PAYMENT_PASS
```
