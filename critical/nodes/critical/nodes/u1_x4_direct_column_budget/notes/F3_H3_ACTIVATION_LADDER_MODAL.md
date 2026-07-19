# F3 h=3 activation ladder (Terminal C, 2026-07-08)

Status: PRE-REGISTERED COMMON-ROOT LADDER.  This tests the refined Terminal C
target directly over many threshold primes.  It is not the full all-shapes norm
census.

## Pre-registration

Refined target:

> A non-toral normalized h=3 shape should not activate at two different
> threshold primes `q = 1 mod 96`, `q >= 96^2`, where activation means a common
> primitive-root zero of both obstructions modulo `q`.

Falsifier:

- scan the first `64` actual primes `q = 1 mod 96` above `96^2`;
- enumerate all finite-field h=3 non-toral activated shape orbits at each row;
- canonicalize by dilation and side swap;
- a canonical shape appearing at two primes is a direct repeated-activation
  counterexample.

Compute discipline:

- Modal only;
- `8` shards, each scanning `8` primes;
- worker timeout `60s`;
- partial per-shard results are printed before the final repeat check.

## Replay

```text
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_activation_ladder_modal.py
```

Expected digest if no repeated activation appears:

```text
H3_ACTIVATION_LADDER_PASS
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-r767UbDESh7BN6TaDEC7S6
```

Summary:

```text
TOTAL primes=64 activated_shapes=71 distinct_shapes=71 repeats=0
H3_ACTIVATION_LADDER_PASS
```

The scan found many threshold activations, including rows with up to `9` shape
orbits, but no canonical shape appeared at two different primes.  This is direct
evidence for the refined common-root pair-coprimality target.
