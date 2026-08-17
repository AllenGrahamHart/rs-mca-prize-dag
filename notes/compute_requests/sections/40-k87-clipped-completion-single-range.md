## Preregistered K'=87 clipped completion single-call ranges

- **decision:** preserve the accepted offsets `1..12`, then execute each
  remaining fixed range through one remote Modal call
- **fixed remaining ranges:** `13..20`, `21..28`, `29..36`, `37..43`
- **single-call dispatcher SHA-256:**
  `56353323d5f4f322a9f26a6602228bd6245773d6a48979e3be2f7a39af4d38be`
- **flexible contiguous merger SHA-256:**
  `2fc0c0408227dd3cfdf175304bfad6e7b13a77782d33a4a4041b8ff1f8fd12dd`
- **unchanged full-wave checker SHA-256:**
  `92caef3cb3872b2c75ffa91bad21e0a745f281c1b2a8590005b7632368bd3f5e`
- **accepted prefix captures:** offsets `1..4` at
  `544b603dac9fd1ea858c36e530bb0263f6e11392a6d3b284d3baa1c266b9f7ca`;
  offsets `5..12` at
  `4f3f1d9e5f81aa3f8afdb3727d266eaa9f557ad2140b9d8b1c469919785918dd`
- **envelope:** one Modal container per launch, one CPU and 256 MB; primary
  and independent-audit children execute sequentially with the unchanged
  900-second child wall and a 14415-second range wall; projected aggregate
  cost below `$1`
- **local safety:** one synchronous Modal remote call under the `modal`
  RAMguard profile; the client inherits a 2 MB thread-stack soft limit while
  retaining RAMguard's 1536 MB address-space ceiling; no local enumeration,
  starmap, or concurrent dispatch

The remote container runs the unchanged primary and audit source files as
separate subprocesses and emits the same per-offset records. Sharing transport
does not share implementation state: each child starts a fresh interpreter,
constructs its own cache, and is hashed separately. Acceptance still requires
both implementations at every offset, exact count agreement in the unchanged
full-wave checker, exit zero, no timeout, and peak RSS at most 128 MB. The
single-call protocol changes only the local Modal client's thread demand.

**First single-call launch:** infrastructure `INCOMPLETE` before remote work.
Modal app `ap-vFYKr9rxnNXfxQ7m8XpvLQ` initialized but the local client again
returned `can't start new thread` before creating objects. No capture is
accepted. Inspection showed that this WSL host uses RAMguard's `prlimit`
fallback: the client has a 1536 MB virtual-address ceiling and an inherited
8 MB stack reservation per thread. The retry retains the address-space
ceiling and lowers only the inherited stack soft limit to 2 MB via
`prlimit --stack=2097152`. This transport adjustment does not alter remote
resources, source hashes, range boundaries, or acceptance criteria.
