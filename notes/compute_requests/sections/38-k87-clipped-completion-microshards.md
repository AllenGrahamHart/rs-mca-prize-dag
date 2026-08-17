## Preregistered K'=87 clipped completion microshards

- **decision:** dispatch the unchanged paired jobs in eleven sequential
  microshards of at most eight jobs
- **fixed offset partition:** `1..4`, `5..8`, `9..12`, `13..16`, `17..20`,
  `21..24`, `25..28`, `29..32`, `33..36`, `37..40`, `41..43`
- **unchanged shard dispatcher SHA-256:**
  `ac42c17cc5b8f6c9b318cc07a43f2a300d9ab74e21936e4279ea0783d1e9860b`
- **flexible contiguous merger SHA-256:**
  `2fc0c0408227dd3cfdf175304bfad6e7b13a77782d33a4a4041b8ff1f8fd12dd`
- **unchanged full-wave checker SHA-256:**
  `92caef3cb3872b2c75ffa91bad21e0a745f281c1b2a8590005b7632368bd3f5e`
- **envelope:** at most eight simultaneous Modal jobs, one CPU and 256 MB
  each; shards launch sequentially and retain the 900-second child wall;
  projected aggregate cost below `$1`
- **local safety:** one small dispatch client at a time under the `modal`
  RAMguard profile

The merger reads each shard's own `(start,end)` terminal, verifies every
capture hash and exact paired job set, proves that the ranges form a
nonoverlapping contiguous partition of `1..43`, and emits the canonical
86-job capture consumed by the unchanged checker. This is an infrastructure
repair only; all mathematical source hashes remain those of the parent wave.
