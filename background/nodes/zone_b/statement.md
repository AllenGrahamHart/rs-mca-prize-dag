# zone_b

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

On a row assigned to the direct quotient-value E1 route, determine

```text
|{e_1(B) mod p : B in binom(Q,ell')}|
```

for quotient orders `80 < N' < 512`: near-full signed-core image or an exact
quantitative collision profile. On 2-power rows the open cells are the
2-power divisors in that interval; for Row C they are `N' in {128,256}`.

This is a route-local value-set determination. It does not by itself prove
universal adjacent unsafety.

## Attack surface

extend the split-prime transfer range, or the norm threshold, or prove e1-fullness directly

## Falsifier

Row-C birthday sampling showing collision rates far from either the full or the heavily-collided prediction

## Ledger (migrated notes)

PREFERRED ROUTE (evidence-backed): direct fullness via norm criterion, density,
and a pointwise transfer. A merely collided image does not satisfy the
quantitative premise of `averaged_slope_conversion`; that row-instantiation
obligation is recorded separately.
