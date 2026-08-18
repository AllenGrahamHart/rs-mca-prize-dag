# Cycle 453: DLI spectral-hypothesis separation

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: 6e0eae14a
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
newest open upstream PR: #1173 (2788d5ec3)
critical mandatory-open count: 28 declarations / 27 orbit targets
```

Canonical and upstream remained unchanged.

## Action

Determine whether either remaining spectral safeguard, one-sidedness or
2-adic valuation purity, can support a primitive correlation theorem by
itself.

## Result: PROVED two-way scope fence

An exact order-16 certificate gives disjoint one-sided events on frequencies
`{2,3}` and `{4,6}` with primitive ratio

```text
8192/485 > sqrt(32).
```

They fail because each event mixes valuation classes.

A complementary tensor uses one event in each of valuations zero, one, and
two. Its local marginal counts are `3856,1296,5124`, with joint/owner counts
`20/4`. Complete-residue tensorization gives

```text
C^r(1-5^(-r)),       C=83886080/25006401,
```

which is `10.8031...>sqrt(64)` at `r=2`. These events are valuation-pure but
cross the one-sided boundary.

Thus neither safeguard alone is sufficient. C2'' theorem search is now
restricted to the exact conjunction of one-sidedness, valuation purity,
nested initial-prefix allocation, and primitive ownership. Both finite
certificates have independent exact enumerators; the tensor and field
existence are symbolic.

## Burn-down

```text
node/workboard item: reduced DLI C2'' / C2-INT
result: minimum viable spectral theorem scope frozen by counterexamples
DAG delta: +1 PROVED background node, +1 evidence edge
upstream delta: future Q/SPI scope fence recorded; no live-PR export
delta-star movement: none
new assumptions: none
live compute requests: none
Modal spend: zero
next action: attack the exact nested split-Pell/Haar prefix or change critical
             target; do not broaden the correlation theorem again
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/dli_spectral_hypothesis_separation_no_go/verify.py
tools/ramguard tiny -- python3 background/nodes/dli_spectral_hypothesis_separation_no_go/verify_audit.py
```
