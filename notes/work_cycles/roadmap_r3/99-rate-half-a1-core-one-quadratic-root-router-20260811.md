# Cycle 99: core-one quadratic root router (2026-08-11)

## Cycle pins

```text
our start:       dfed5a88a
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Uniform first-fifth dichotomy

The core-one scalar quadratic has exact identities `u+v=e+2` and `O=u-4`.
Combining new-root demand with simple-row vertical capacity gives

```text
(2-r)e<=3u+2I_0<=5u
```

when all heavy residual roots are simple. Therefore throughout `5u<e`, the
residual is either one heavy double root or two heavy simple roots. This
routes every official gap

```text
4<=u<=36650387592
```

and eliminates the squarefree one-heavy/one-nonheavy branch over that whole
range.

## Burn-down

```text
result:                  ROUTED first fifth of quadratic gap to 2 patterns
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next seek a global ambient or recurrence constraint common to both retained
patterns; local simple-row capacity alone is now exhausted.
