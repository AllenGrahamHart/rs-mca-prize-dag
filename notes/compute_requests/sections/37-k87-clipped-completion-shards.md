## Preregistered K'=87 clipped completion shards

- **decision:** execute the unchanged 86-job clipped wave in three sequential
  shards to stay below the WSL client's thread ceiling
- **fixed shards:** offsets `1..15` (30 jobs), `16..29` (28 jobs), and
  `30..43` (28 jobs)
- **shard dispatcher SHA-256:**
  `ac42c17cc5b8f6c9b318cc07a43f2a300d9ab74e21936e4279ea0783d1e9860b`
- **shard merger SHA-256:**
  `660f99833062b5073393e0351d5b7067c47d2b8e77c3474715a377a6e974a964`
- **unchanged full-wave checker SHA-256:**
  `92caef3cb3872b2c75ffa91bad21e0a745f281c1b2a8590005b7632368bd3f5e`
- **cached primary adapter SHA-256:**
  `dd652f005ee31ed3229bd16039f16a8961306fbfe21a45d95737406a3e716f31`
- **cached audit adapter SHA-256:**
  `9e4240355e5d5b1d59faf301d8087b63cf2fb2a1856d74f1551dc42e399f2296`
- **envelope:** no more than 30 simultaneous Modal jobs, one CPU and 256 MB
  each, with the unchanged 900-second child wall; projected aggregate cost
  below `$1`
- **local safety:** shards launch sequentially under the `modal` RAMguard
  profile; no local enumeration

The merger validates each capture hash, exact shard boundary, job set, and
batch terminal before emitting one canonical 86-job capture. The original
full-wave checker then applies the unchanged mathematical acceptance
contract. Sharding changes only local dispatch concurrency.

`FALSIFIED`, `INCOMPLETE`, and `PASS` retain exactly the meanings in the
parent completion-wave preregistration. No shard result alone changes the
status of `K'=87`.

**First shard launch:** infrastructure `INCOMPLETE` before remote work.
Modal app `ap-Hh3xMzcVM9z85G3diycuXu` returned the same local
`can't start new thread` error for the 30-job first shard. The current WSL
task headroom is therefore below this dispatch size. No capture is accepted;
the unchanged shard dispatcher will be used with at most eight jobs per
launch.
