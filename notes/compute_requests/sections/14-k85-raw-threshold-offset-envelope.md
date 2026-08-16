## Preregistered K'=85 raw-threshold offset envelope

- **decision:** identify the exact global raw-safe leader over all 74 positive
  support-2/3 offset lanes, and isolate the complete residual population whose
  raw premium exceeds the safe ceiling and therefore needs carrier geometry
- **scope:** offsets `1..74`, both a primary exact traversal and an independently
  written reconstruction of the support-2/3 and support-4/5 vectors
- **primary SHA-256:**
  `bba44a0511fa2ee5399c7c47fc2a16fe5449086665bb05d5caa5f5e390f03848`
- **audit SHA-256:**
  `5eabcec96084e3ed32a384dc9d93ea6cf44465c6dfbbbb655f2d0220c7c3eab0`
- **dispatcher SHA-256:**
  `a2e4217a49c371ab449aa914484d6a4f750c66ebdea862a6d002319b0eef89e5`
- **merger SHA-256:**
  `28d9289be8c0e741a364a72884e171154ff0186ea732b1f1cdda3990c3ea333c`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** 148 remote jobs, one CPU and 256 MB each, 165-second child
  timeout and 180-second container timeout; conservative campaign wall below
  five minutes and projected total cost below `$1`
- **partial-output contract:** every completed `m2` slice prints exact safe and
  unsafe counts plus extrema before the next slice begins
- **local safety:** one RAM-guarded Modal client; no local enumeration

The scan evaluates only the pre-geometry raw threshold split. It does not
price any unsafe unit and cannot promote K'=85. The complete paired capture is
accepted only if all 148 unique jobs finish below 128 MB, both traversals agree
on every offset classification digest and profile, and the exact coverage
identity

```text
sum_{d=1}^{74} (75-d) * 76^2
```

holds. `PASS` names the exact raw-safe maximizer and a finite residual geometry
population. `FAIL` is any disagreement or malformed coverage. `INCOMPLETE`
retains only printed partial slices and changes no mathematical status.

The first launch, Modal app `ap-fxCF0n6O4e0LYYDe0MaIPP`, was
`INCOMPLETE`: Modal relocated the dispatcher module to `/root`, exposing an
invalid local-only `parents[2]` path during container import. No mathematical
job started and no output was retained. The repaired dispatcher uses
module-relative mounted paths in both environments; all mathematical sources
and the merger are unchanged.

The second launch, Modal app `ap-ld231Otrj4iOwrf8WgXUbz`, was also
`INCOMPLETE`: all 148 workers started, but the mounted archives were in `/tmp`
while the subprocess working directory was `/root`, so every worker failed the
same archive-discovery check before enumeration (22--24 MB peak, about 0.05
seconds each). The dispatcher now runs workers from `/tmp` and exposes a
two-job offset-74 smoke mode that must pass before the full wave is retried.
