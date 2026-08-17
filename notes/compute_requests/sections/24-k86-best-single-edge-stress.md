## Preregistered K'=86 best-single-edge stress falsifier

- **decision:** test whether the best of the raw price and each available
  single adjacent edge pays every deduplicated carrier profile below the exact
  K'=86 raw-safe leader on four route-deciding offsets
- **ordered scope:** offsets `32` (the raw-safe leader), `1` (largest lane),
  `23` (interior stress), and `42` (last raw-unsafe lane), evaluated in one
  paired deployment
- **primary adapter SHA-256:**
  `8a2ec9877e317798e615e14d0e23b2f0c65d927a109985c7aec160c1cc65db97`
- **independent-pricing adapter SHA-256:**
  `ad37ddbfa7920e57ad912b523751d9415944f8e16459c49bb7973a86e386cd10`
- **shared K'=86 traversal core SHA-256:**
  `2eb7f85cf6fb4311874f453c75fc868796dbc726599462e12b640e98fe2a9939`
- **K'=85 primary formula adapter SHA-256:**
  `2c94b7432cd4c9d37a49288298761cbff9227a07f694fe80ec259ef19e724505`
- **K'=85 independent formula adapter SHA-256:**
  `f9a01624b5a11fbc30f58a4f4afca2aa75d9af96b35c69edddcdc7eef5e1fa1f`
- **K'=85 residual base SHA-256:**
  `cd1e9d2706c48be390387953c4abeea46958af258f132700809cf2393a5e4a90`
- **dispatcher SHA-256:**
  `dc2e0c69e0aa8928e24cc3777f744d3394716f70ebd6970e3c8bcf27b72fe325`
- **checker SHA-256:**
  `8961626415452cf5de84e8cc5194c47c40eba8d56d1a13f6c4f3989828d5d3cd`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** eight jobs, one CPU and 256 MB each, 300-second child wall
  and 315-second container wall; projected total cost below `$0.10`
- **local safety:** one `modal`-profile RAMguard client; no local enumeration

The adapters alter only `K'=86`, `q=76`, `m'=67558`, `n'=1048662`, the
derived exact ceiling, and the exact raw-safe offset-32 leader. They retain
the proved K'=85 carrier formulas. Both implementations share the explicit
row-generic source-unit traversal, while the adjacent-edge prices are rebuilt
by the primary router and the separately implemented audit formulas.

`FALSIFIED` requires a paired exact over-leader witness and blocks a full
best-single campaign. `SURVIVED` requires paired agreement on all four lanes,
1,221,374 completed source units, and every carrier profile at or below the
leader. `INCOMPLETE` retains partial checkpoints and changes no mathematical
status. Survival authorizes a separately preregistered completion wave over
offsets `1..42`; this stress campaign alone cannot promote `K'=86`.
