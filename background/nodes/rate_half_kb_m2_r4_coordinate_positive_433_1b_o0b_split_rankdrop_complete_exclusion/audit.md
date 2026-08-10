# Audit

The result is sharded by `S0`, `SDE`, and `SDF`; every shard is below 50,000
lines.  `verify.py` checks artifact custody, shard-manifest hashes, all 96
point/lane rows, all 10,080 distinct case positions, each printed unit
certificate, exact source-point metadata, and the required DAG parents.
`verify_audit.py` mutates a shard hash, lane, case, unit flag, and source
point identity.
