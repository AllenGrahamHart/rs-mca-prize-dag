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

**Outcome:** `PASS`. The accepted range captures are:

| Offsets | Modal app | Capture SHA-256 |
|---|---|---|
| `1..4` | `ap-iXONaPwRxMHjwZR515sOyi` | `544b603dac9fd1ea858c36e530bb0263f6e11392a6d3b284d3baa1c266b9f7ca` |
| `5..12` | `ap-dJ2eUU9a0u0jcJjXZiefIU` | `4f3f1d9e5f81aa3f8afdb3727d266eaa9f557ad2140b9d8b1c469919785918dd` |
| `13..20` | `ap-xr0f01RFscUvWkrGvn7VGk` | `1406c04aef22bfa96037221ebb6c47a94258fb3e54014e117a5b9a6090dba2fb` |
| `21..28` | `ap-qFATW8MSFF0dzBoqm4ekA9` | `ee4c260ba13112abd17f02d37957c5eae131c713cc1f51254a9e2387b65cfc0c` |
| `29..36` | `ap-KzzGy55iKSUXT04uVv7UOh` | `28bbc2311b0845e7deba6b8e5f4cacdafb32ed65d5b9057871ac043aab98b55b` |
| `37..43` | `ap-TLGJytlHAZRLOm0pn0e8Oh` | `e9d41feff81a9e2e809b54bcb80c2c802c6d2c140d9481bc8f527a5f5b9df784` |

The flexible merger accepted the exact contiguous partition `1..43` and
emitted canonical capture SHA-256
`6f8064320850e0009c18c967e2b61ec5b4d77c51e1c2afb4bee6fc41921e5cd8`.
The unchanged full-wave checker reports 86 jobs, 43 offsets, 14,388,660
source units, 511,677 raw-unsafe units, and 77,179,660 carrier profiles per
implementation. Primary and independent audit agree exactly; all offsets
survive and no falsifying witness remains. Observed peak RSS was `31..45` MB.

This closes the K'=87 nonordinary clipped-support residual. It does not by
itself promote the row: the ordinary lane and exact component payment remain
separate required gates.
