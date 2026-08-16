## Preregistered K'=85 best-single-edge domination falsifier

- **decision:** test whether the best of the raw base and every available
  single adjacent edge pays every deduplicated carrier profile below the exact
  offset-11 leader, while deliberately excluding multi-edge choices
- **ordered scope:** offset 11 first; offsets 1, 23, and 41 only after survival
- **adapter SHA-256:**
  `2c94b7432cd4c9d37a49288298761cbff9227a07f694fe80ec259ef19e724505`
- **base residual scanner SHA-256:**
  `b8899f40cec67c03924cb1944341b76010a574212f0889387ccdd3f14cd74440`
- **independent witness audit SHA-256:**
  `4e938710a8668ed013050f5f1e0979a8c0eb1db76d9dfd47d2c8edf24092b7f6`
- **dispatcher SHA-256:**
  `cdd76442d2e303214a13e8b17f9491975cab5464d8e437fc98a0d01d91574d4c`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **stopping rule:** stop at the first over-leader profile and independently
  maximize the best-single price over every high-support branch
- **compression:** reuse the exact residual router and deduplicate by combined
  fixed-union vector plus the complete adjacent-edge tuple
- **envelope:** one CPU, 256 MB, 215-second child wall per offset; projected
  total cost below `$0.10`
- **partial output:** every completed `m2` slice prints exact coverage counts

`FALSIFIED` demonstrates that a disjoint multi-edge choice is genuinely
needed. `SURVIVED` proves only the completed offset. `INCOMPLETE` changes no
status. No pilot outcome promotes K'=85.
