# Audit

The 5.2 MB primary packet is split into three digest-pinned JSONL shards.
The verifier checks each shard digest, byte count, record count, and JSON
record before streaming it. The unordered full run completed all 96 rows
without recovery or a remote exception.

Root ownership is independent: FLINT computes each field-root part by
Frobenius gcd. The direct audit independently reconstructs both common-`f`
quadratic roots, their intersection, every even-quartic lift, and the final
colored cut. Its formulas were matched directly to pairing-14 source
matching `((0,5),(1,4),(2,3))`. It also joins each paid free row to the exact
tower-boundary or regularized-base certificate that owns it. The first
direct-audit launch failed before arithmetic on a metadata-string order; the
corrected audit and both certificate verifiers passed.
