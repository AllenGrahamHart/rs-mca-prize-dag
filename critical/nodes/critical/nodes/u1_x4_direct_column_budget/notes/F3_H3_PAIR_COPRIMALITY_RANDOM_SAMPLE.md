# F3 h=3 pair-coprimality random norm sample (Terminal C, 2026-07-08)

Status: PRE-REGISTERED RANDOM SAMPLE.  This is falsification evidence for
Terminal C, not the full all-shapes `n=96` census.

## Pre-registration

Naive target under stress:

> A random normalized non-toral h=3 shape `sigma=(A,B)` in `mu_96` should have
> no common obstruction norm prime `p = 1 mod 96`, `p >= 96^2`.

Falsifier:

- compute exact cyclotomic norms of `E1(sigma)` and `E2(sigma)` in
  `Q(zeta_96)`;
- factor `gcd(N(E1),N(E2))`;
- record any factor `p = 1 mod 96`, `p >= 9216`;
- separately check whether such a factor is an actual simultaneous activation
  prime, i.e. whether some primitive 96th root modulo `p` zeros both
  obstructions.

Compute discipline:

- Modal only;
- each shard has timeout `60s`;
- the script prints partial results even if a later shard fails;
- default run is small (`8` shards, `250` unique shapes per shard) to avoid
  wasting compute on a still-unoptimized exact resultant loop.

## Replay

```text
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_coprimality_random_modal.py
```

Expected digest if no exception is found:

```text
H3_RANDOM_ACTIVATION_SAMPLE_PASS
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-bYVtU4rZenbBi4NAsSmUEc
```

Output summary:

```text
TOTAL unique_shapes=2000 norm_exceptions=22 activation_exceptions=0
H3_RANDOM_ACTIVATION_SAMPLE_PASS
```

Representative rational norm exceptions (none are actual simultaneous
activation exceptions):

```text
[0, 1, 20 | 12, 53, 60]  threshold_norm_primes=[3584641]
[0, 5, 13 | 55, 68, 87]  threshold_norm_primes=[585601]
[0, 3, 37 | 66, 71, 95]  threshold_norm_primes=[42337]
```

Verdict:

- The naive rational norm-coprimality statement is **REFUTED as a universal
  random-shape heuristic** at this sample size: `22/2000` random shapes had a
  shared rational obstruction norm prime `p = 1 mod 96`, `p >= 96^2`.
- The actual activation criterion survived: none of those shared rational norm
  primes was a simultaneous primitive-root zero of both obstructions.

Refined Terminal C target:

> Pair-coprimality must be stated at the prime-ideal/common-root level, not at
> the rational norm-gcd level.  The relevant exceptional list is shapes with a
> common primitive 96th-root zero modulo a threshold prime.
