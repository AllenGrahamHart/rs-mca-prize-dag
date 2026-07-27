# Audit

Primary Modal app `ap-EfGZditRQm7eDLLLWpNiSA` completed all 31 shards with
271.301709 aggregate worker-seconds. Independent app
`ap-MQpKibQl8PBqzuhB5DKf2m` completed the same partition with 339.920267
worker-seconds.

The implementations differ in both load-bearing constructions: unordered
signed-chord grouping versus ordered negacyclic multiplication, and the
five-position weld formula versus direct circular-distance membership. The
checker validates source hashes, exact shard coverage, every count/max field,
the closed-form chamber size, and twelve retained witnesses.

Both apps used one CPU, 256 MiB, 60-second function caps, and at most 31
containers. They completed concurrently in under one minute of client wall
time. The combined 611.221976 worker-seconds remained below the declared
conservative `$0.90` campaign ceiling. No rerun is authorized.
