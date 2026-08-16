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

**Offset-11 outcome:** `SURVIVED` exhaustively. Modal app
`ap-x4S2u8ZAef1I0q9N7AK45d` checked all 369,664 source units, all 12,281
raw-unsafe units, and 936,749 deduplicated carrier profiles. Every best-single
price is at most the exact raw-safe leader. Capture SHA-256:
`3b2e0e353e54a4c1f20ab35a5f2775c0a956beb2db6b5c3de411e326daf24989`.
This proves the printed finite offset-11 domination statement and authorizes
the next preregistered lane, offset 1; it does not promote the full row.

**Offset-1 outcome:** `SURVIVED` exhaustively. Modal app
`ap-Wl6GfzOdL4g1bsp7AD8kx8` checked all 427,424 source units, all 15,702
raw-unsafe units, and 181,450 deduplicated carrier profiles. Capture SHA-256:
`9b34ca0dfa9b28db03f3568af47c848e8e4728912273c57ed3166565d1ceec59`.
This proves the printed finite offset-1 domination statement and authorizes
the preregistered offset-23 lane; the full row remains open.

**Offset-23 outcome:** `SURVIVED` exhaustively. Modal app
`ap-ybr2br69sCjzR8D3bGRARc` checked all 300,352 source units, all 7,598
raw-unsafe units, and 2,018,406 deduplicated carrier profiles. Capture
SHA-256:
`539350d9dff7c463386adc9a571d3151e605b7711315c5ea293ab2e37003c3bb`.
This proves the printed finite offset-23 domination statement and authorizes
offset 41, the last lane containing any raw-unsafe unit.
