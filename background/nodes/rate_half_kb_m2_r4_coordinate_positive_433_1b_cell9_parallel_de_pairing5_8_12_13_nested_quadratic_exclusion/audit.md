# Audit

The 68.2 MB primary packet is split into six digest-pinned JSONL shards. The
verifier checks each shard digest, byte count, record count, and JSON record
before streaming it.

The full unordered run flushed 189 complete rows before its Modal client
terminated, leaving five finalized shards and a 29-record temporary shard.
A bounded recovery app recomputed exactly the three absent Cartesian indices
`175,176,177`. The checked recovery merger required the exact missing-key
join, rejected duplicate or nonterminal records, rebuilt all six shards in
canonical Cartesian order, and verified the sealed 192-record manifest.

Root ownership is independent: FLINT computes each field-root part by
Frobenius gcd. The direct audit independently reconstructs the quadratic
roots, Cartesian products, missing-relation values, and colored cuts. It
also joins each paid free row to the exact tower-boundary or regularized-base
certificate that owns it. Both independent audits passed the sealed packet.
