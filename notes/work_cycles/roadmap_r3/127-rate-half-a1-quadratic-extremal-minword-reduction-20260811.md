# Cycle 127: quadratic extremal minimum-word reduction (2026-08-11)

## Cycle pins

```text
our start:       d9a0e8849
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
upstream PR:     #1161 amended through 09152eb
compute:         two local tiny integer verifiers
critical open:   28
```

## The sole floor case is an exact minimum-word family

Every pair either has union at least `3rho/2`, with no third center on its
endpoint codeword line, or attains `3rho/2-1`. Equality forces exactly one
third line center and total line deficit at most one.

For the `3e` off-line slopes in the equality case, define the triple-union
excess above `d_min=2rho+1`. Exact global incidence gives

```text
sum excess=e.
```

Hence at least `2e` slopes have zero excess. For each, the affine second
difference of its center with the two endpoint centers is a nonzero RS
codeword supported inside a `d_min`-set. It therefore has exact minimum
weight and support equal to the triple union.

## Burn-down

```text
result:                  REDUCED the sole floor profile to >=2e minimum words
DAG delta:               +1 PROVED leaf, +1 req edge, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: PR #1161 contains the macroscopic precursor
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next determine whether these minimum words are forced into a split pencil or
whether their zero locators violate the exact light-incidence ledger.
