## Preregistered K'=86 adjacent-support route pilot

- **decision:** test whether the complete K'=85 best-single mechanism still
  has positive room at the next row and identify the first exact unsafe lane
  if it does not
- **scope:** `ordinary`, offsets `11`, `23`, `41`, and terminal offset `75`,
  in both primary and independent implementations
- **primary wrapper SHA-256:**
  `ca6ffd6766d1e4aac72d98ea09fa30c5d1b100a01c2e51e5e7673bfc92f33106`
- **audit wrapper SHA-256:**
  `ceab00de841839ee0c76eb440e847f27aeb524d11dc6646742f774991817a2ef`
- **checker SHA-256:**
  `8373bebdc09e49f55281703c404ec44283fd10e1f766ad4d9eb066ef46b91eef`
- **hash-pinned K'=83 code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **batch runner SHA-256:**
  `bbe9f1100d8d6add611794e24e02d57ab0f57903a15195a944e6fe640ca98922`
- **envelope:** ten remote containers, one CPU and 1 GB each, 645-second
  child wall; projected cost below `$0.20`
- **local safety:** one RAM-guarded Modal client; no local enumeration

The wrappers change only the row parameters to `K'=86`, `q=76`,
`m'=67558`, and `n'=1048662`. The theorem and router sources are the same
hash-pinned implementations used at `K'=83..85`. An unsafe mathematical
lane exits normally and is retained as a route outcome; only timeout,
malformed output, or implementation disagreement makes the batch incomplete.

```text
SAFE PILOT:   both implementations agree and all five lanes are safe;
              locate unsampled and residual leaders before any broad wave
UNSAFE PILOT: both implementations agree and at least one lane is unsafe;
              retain the exact branch as the next theorem obstruction
INCOMPLETE:   timeout, missing lane, or implementation disagreement;
              retain no mathematical conclusion
```

No outcome promotes `K'=86`, changes a DAG status, or authorizes interval
extrapolation. A broader finite wave is permitted only if this pilot leaves
a sharply typed residual statement.
