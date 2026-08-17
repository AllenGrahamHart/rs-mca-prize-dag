## Preregistered K'=87 clipped offset-1 audit completion

- **decision:** complete only the independent upper-oriented audit after the
  primary offset-1 traversal survived and the uncached audit timed out
- **starting capture SHA-256:**
  `7fd211a2ca2a19de5f483eebcc69a29549e529cdaa713431b86645434f0f11ff`
- **cached audit adapter SHA-256:**
  `9e4240355e5d5b1d59faf301d8087b63cf2fb2a1856d74f1551dc42e399f2296`
- **unchanged upper-oriented adapter SHA-256:**
  `289ade06dfcb706efb8dcb020f20afe1ec9ccf25061d450438867ef2f59deb72`
- **generic clipped evaluator SHA-256:**
  `514cbeabc44f04ea4e153415dcddab1878069cefeaa12dea931f60edf9c0e18a`
- **dispatcher SHA-256:**
  `1e8c9099c2485e7bc4d76e1dbd808fb1c80dfdbff4d363d3cea579ee25a69312`
- **merger/checker SHA-256:**
  `ce7f1b8ed7176434378bad780f6626a23fde00c50e30f92bb1333f2d89ad812d`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU and 256 MB, 1,920-second child wall and 1,935-second
  container wall; projected cost below `$0.10`
- **local safety:** one `modal`-profile RAMguard client; no local enumeration

The cache changes no formula. It keys the exact upper-oriented cap by
`(union,dimension,raw5,raw6)` and reuses repeated rational evaluations across
deduplicated profiles. The merger accepts the earlier primary result only by
its pinned capture hash and requires exact equality of all terminal coverage
counts with the resumed audit.

`FALSIFIED` is a paired route wall only after comparison with the pinned
primary traversal. `PASS` requires both complete traversals to survive all
462,384 source units and 23,104 raw-unsafe units with equal profile counts.
`INCOMPLETE` changes no status.
