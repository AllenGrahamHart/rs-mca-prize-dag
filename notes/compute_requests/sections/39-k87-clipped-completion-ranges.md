## Preregistered K'=87 clipped completion ranges

- **decision:** retain the completed paired offsets `1..4`, then process the
  remaining offsets in five sequential ranges with exactly two remote
  workers per range
- **fixed remaining ranges:** `5..12`, `13..20`, `21..28`, `29..36`,
  `37..43`
- **range dispatcher SHA-256:**
  `97354bbbb4d1900e022028b569a46de00799f9724d79697e4281deb22cef1494`
- **flexible contiguous merger SHA-256:**
  `2fc0c0408227dd3cfdf175304bfad6e7b13a77782d33a4a4041b8ff1f8fd12dd`
- **unchanged full-wave checker SHA-256:**
  `92caef3cb3872b2c75ffa91bad21e0a745f281c1b2a8590005b7632368bd3f5e`
- **pinned completed range:** offsets `1..4`, capture SHA-256
  `544b603dac9fd1ea858c36e530bb0263f6e11392a6d3b284d3baa1c266b9f7ca`
- **envelope:** exactly two simultaneous Modal containers per launch, one
  primary and one independent audit, each with one CPU and 256 MB; offsets
  execute sequentially inside each container with the unchanged 900-second
  child wall and 7215-second range wall; projected aggregate cost below `$1`
- **local safety:** one two-call Modal dispatch client at a time under the
  `modal` RAMguard profile; no local enumeration or many-call fanout

Each remote worker emits the unchanged per-offset `JOB_RESULT` records. The
range terminal is accepted only when both implementations return one complete
result for every assigned offset, with exit zero and peak RSS at most 128 MB.
After all five launches, the existing flexible merger verifies capture hashes,
paired job sets, and the exact contiguous partition `1..43`; the unchanged
full-wave checker then applies the preregistered mathematical acceptance
contract. This changes dispatch topology only. It does not weaken the paired
independence, completeness, resource, or numerical criteria.

**Observed launches.** Range `5..12` completed under Modal app
`ap-dJ2eUU9a0u0jcJjXZiefIU`; both implementations survived every offset and
agreed exactly, with peak RSS `39..43` MB. Its capture SHA-256 is
`4f3f1d9e5f81aa3f8afdb3727d266eaa9f557ad2140b9d8b1c469919785918dd`.
The first `13..20` attempt, app `ap-Lgc9MUPG1puo4Eua60ex2D`, failed in the
local Modal client with `can't start new thread` before creating remote
objects. No capture from that attempt is accepted. Intermittent failure at
two calls motivates the one-call transport below.
