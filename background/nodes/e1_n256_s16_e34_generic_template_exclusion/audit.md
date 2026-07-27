# Audit

Primary Modal app `ap-XpmKEOhClEfy8STvFbMH9y` completed all 57 shards with
34.471246 aggregate worker-seconds. Independent app
`ap-GUW2NuOkVnhQDU4jUvepbZ` completed the same partition with 50.538048
worker-seconds.

The implementations use unordered chord grouping versus ordered negacyclic
multiplication, and generated weld sets versus direct distance membership.
The checker validates both source hashes, the immutable orbit packet, exact
support coverage, all shardwise fields, and twelve retained witnesses.

Both apps used one CPU, 256 MiB, 60-second function caps, and at most 45
containers. Concurrent use was capped below 100 containers. The combined
85.009294 worker-seconds remained below the conservative `$0.20` ceiling. No
rerun is authorized.
