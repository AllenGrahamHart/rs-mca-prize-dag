# Audit

## Verdict

The router is exact and removes the need for a separate quotient-image
computation. It does not prove the common-core slope bound to which
multiplicity is routed.

## Scope checks

- `c|k` and strict activity `c>B-k` are both load-bearing: together they make
  the complete-fiber core have exactly `k` points.
- Grouping is global across every raised threshold. Reusing one key at two
  thresholds creates a collision group, not two singleton payments.
- The comparison `C(N,h)<=C(N,h+1)` uses `k/n<=1/4`; it is false in general
  at rate `1/2`.
- A nonsingleton group's recovered pair is unique on its `k`-point core.
- Support-wise noncontainment is part of the quotient-currency definition and
  guarantees a discrepancy tail point, so the support can be truncated back
  to the initial reserve without losing the live witness.

## Limitations

The generic collision group consumes P-A's existing `8n^3` allocation only
if P-A is proved. The complementary nongeneric group remains part of the
mismatch bridge's common-core/generic-chart aggregate.
