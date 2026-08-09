# Audit

The 33.7 MB primary packet is split into three digest-pinned JSONL shards.
The verifier checks each shard digest, byte count, record count, and JSON
record before streaming it. The unordered full run completed all 96 rows
without recovery or a remote exception.

Root ownership is independent: FLINT computes each field-root part by
Frobenius gcd. The direct audit independently reconstructs the positive
pairing-12 quadratic roots, Cartesian products, missing-relation values, and
colored cuts. Its formulas were matched directly to pairing-12 source
matching `((0,5),(1,2),(3,4))`, not inherited by textual substitution from
pairing 9. It also joins each paid free row to the exact tower-boundary or
regularized-base certificate that owns it. Both independent audits passed.
