## Preregistered K'=85 fixed-union-only domination falsifier

- **decision:** test the deliberately stronger claim that every raw-unsafe
  residual carrier case is already at most the exact offset-11 leader after
  componentwise fixed-union caps, before any adjacent-support price
- **ordered scope:** offset 11 first; offsets 1, 23, and 41 only if every prior
  lane survives
- **falsifier SHA-256:**
  `a55a8353b837e3c83e39eb27fe65590c0f9f91eadcf9fa0d32ae2020ecc0502e`
- **independent witness audit SHA-256:**
  `3beb23b1ec7bfa09bf7e6c6ca67d8f450dde6707aed4d4661383965eb533b138`
- **dispatcher SHA-256:**
  `1efe1237d1ec5838aba4aceca30bd96cbe3ee045c66a22b1b3907017bc1aa14a`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **stopping rule:** stop at the first exact witness above the leader and replay
  only that witness in the independent implementation
- **envelope:** one CPU, 256 MB, 160-second scan wall and 15-second witness
  audit wall per launch; projected total cost below `$0.05`
- **partial output:** every completed `m2` slice prints units, unsafe units, and
  carrier cases checked
- **local safety:** one RAM-guarded Modal client; no local enumeration

`FALSIFIED` rejects only the fixed-union-only shortcut and names the exact
carrier case whose adjacent-support payment remains necessary. `SURVIVED`
authorizes the next offset but is not a proof outside the completed lane.
`INCOMPLETE` changes no mathematical status. No outcome promotes K'=85 by
itself.
