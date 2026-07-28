# Audit

Date: 2026-07-28.

Primary Modal app: `ap-EI0gpqKTVVsnR6sCbXZfB3`.
Independent audit app: `ap-52RCxiNtu4Oqe2G36sJqfJ`.

The primary engine enumerates unordered coefficient pairs into the positive
half of the negacyclic autocorrelation and balances first-position pairs by
predicted signed-vector weight. It completed 32/32 shards in 11.552424
aggregate worker-seconds.

The audit engine uses a different lexicographic enumeration, round-robin shard
assignment, and full ordered-pair 128-slot convolution. It completed 32/32
shards in 28.775821 aggregate worker-seconds. Both returned exactly
`10009125` support choices and `320292000` signed vectors, with count vector

```text
(E=5, E=9, E=5 and 257|R, E=9 and 257|R)=(0,16,0,0).
```

The local verifier reconstructs both coverage partitions, independently
replays every retained witness's autocorrelation energy, and tests all 128
primitive roots modulo 257. Source and result packets are hash-pinned. No
floating-point arithmetic, factorization, or probable-prime decision is
load-bearing.
