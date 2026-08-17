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

**Outcome:** `FALSIFIED` at the first checked residual case, with independent
exact replay. Modal app `ap-319YToKIcY6UC4VZUEIZ0a` returned the offset-11
witness

```text
m2=1, m3=12, s2=74, s3=63, s4=s5=37, m4=m5=38
case=T23, fixed-union charge=(16,7), high=c6F/c7F/c8F/c9F
```

after 2,850 source units, one unsafe unit, and one carrier case. The raw and
fixed-union-only premiums are both
`42141786157949900288596401924882914598461995992`, exceeding the exact
offset-11 leader by
`728918141740123567367510537973035075155162638`. The independent witness
audit agreed on every coordinate, charge, branch, and integer. The capture
SHA-256 is
`2e9a646df4e4fd6dc1626360d9fe8a78bfdccf93766f002422a646dfdf07e4d1`.

Thus the fixed-union-only route is dead and offsets 1, 23, and 41 are not
launched. This does not refute the proved adjacent-support theorem or K'=85;
it localizes the next obligation to the support-disjoint adjacent edges
available for the single `(16,7)` charge.
