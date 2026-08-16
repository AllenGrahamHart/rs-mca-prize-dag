## Preregistered K'=85 edge-4-only domination falsifier

- **decision:** test whether the support-4/5 adjacent edge alone pays every
  deduplicated carrier profile of every raw-unsafe unit below the exact
  offset-11 leader
- **ordered scope:** offset 11 first; offsets 1, 23, and 41 only after survival
- **falsifier SHA-256:**
  `b8899f40cec67c03924cb1944341b76010a574212f0889387ccdd3f14cd74440`
- **independent witness audit SHA-256:**
  `8c80fa8e1d338b0366017a15f2f02cd6f1af388c0101019baa733361eebed2d6`
- **dispatcher SHA-256:**
  `32e7b9c7dcc76d84f2703a5111c658c8b5e07c63e676d3eebf92c21add94acca`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **stopping rule:** stop at the first exact over-leader profile and replay it
  with the independent adjacent-pair formula
- **compression:** carrier labels with the same combined fixed-union vector and
  edge-4 cap are evaluated once per residual unit
- **envelope:** one CPU, 256 MB, 215-second child wall per offset; projected
  total cost below `$0.10`
- **partial output:** every completed `m2` slice prints source, unsafe, and
  deduplicated-profile counts

`FALSIFIED` identifies the next adjacent edge or multi-edge obligation.
`SURVIVED` proves only the completed offset. `INCOMPLETE` changes no status.
No pilot outcome promotes K'=85.

**Outcome:** `FALSIFIED` with independent replay. Modal app
`ap-9vbq0eXPV4MZrebuGnSVQr` reached offset 11, `m2=13`, after 73,163 source
units, 2,013 raw-unsafe units, and 238,306 deduplicated geometry profiles. The
first witness is

```text
s2=62, s3=51, s4=s5=50, m4=m5=25
case=F23__N4_t12__N5_t12
charges=(28,7),(29,6), high=c6F/c7F/c8F/c9F
```

The raw premium is
`41678537170179082697698056961638084480681707238`. Replacing supports 4/5
by the edge-4 cap alone gives
`41744966619586153218005378051509525640461543488`, still above the exact
leader by `332098603376376496776486664599646117154710134`; the real minimizer
would therefore reject that replacement in favor of the raw base or another
edge choice. Primary and audit agree exactly. Capture SHA-256:
`c3730780f2404242608fbb2f32dee46f4e7cfa4adbad9cbd7226b9eb945042fa`.

Thus offsets 1, 23, and 41 are not launched. The next exact action is to print
all support-disjoint prices on this two-charge witness and identify the
minimal additional edge set.
