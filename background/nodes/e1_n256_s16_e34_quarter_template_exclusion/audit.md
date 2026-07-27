# Audit

Primary Modal app `ap-kLTKBwJM3lNWUZA3hul5w7` completed 121 shards with
45.781851 aggregate worker-seconds. Independent app
`ap-XXTZkD7kcupvXULmbp2GKZ` completed the same shard partition with 52.691880
aggregate worker-seconds.

The implementations use different autocorrelation constructions: unordered
signed chord grouping versus direct ordered negacyclic polynomial
multiplication. The local checker validates both source hashes, every shard's
closed-form coverage, all count/max fields, and eight exact witnesses.

Both apps used one CPU, 256 MiB, 60-second function caps, at most 100
containers, and completed in under 30 seconds of client-observed wall time
each. The conservative combined cost ceiling is below `$0.15`; the actual
98.473731 worker-seconds are substantially below that ceiling.
