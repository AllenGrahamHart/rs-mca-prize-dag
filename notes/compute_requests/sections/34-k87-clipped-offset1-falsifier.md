## Preregistered K'=87 raw-clipped offset-1 falsifier

- **decision:** exhaust offset 1 using the proved raw-clipped support-5/6 cap
  on every eligible carrier, combined only with support-disjoint adjacent
  edges
- **scope:** paired primary and independent traversals of offset 1; no other
  residual offset
- **generic clipped evaluator SHA-256:**
  `514cbeabc44f04ea4e153415dcddab1878069cefeaa12dea931f60edf9c0e18a`
- **charge-retaining traversal core SHA-256:**
  `ea0cc3fc67e7079a34a0bbabbe8c5953b0791944f05bc64659d80c9470036c13`
- **primary adapter SHA-256:**
  `27e0eaa88d6238de3d86205ab907d2caa1f997212ad0ea2b9ea4533f7924f8d8`
- **independent adapter SHA-256:**
  `289ade06dfcb706efb8dcb020f20afe1ec9ccf25061d450438867ef2f59deb72`
- **dispatcher SHA-256:**
  `ab148aeea28ca762620ce24784e8e28c27a2f92a20bfeebe5d8294e570f2eb36`
- **checker SHA-256:**
  `21de7c78cbf9200fc01d506ce7fd3b389a6546df0285627ca4fe4a61a6018c8f`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** two jobs, one CPU and 256 MB each, 720-second child wall and
  735-second container wall; projected total cost below `$0.15`
- **local safety:** one `modal`-profile RAMguard client; no local enumeration

The primary adapter evaluates the clipped LP by fixing support 5; the audit
fixes support 6. For each profile, the resulting edge-5 cap is minimized with
the previously proved adjacent cap. The final optimizer enumerates only
support-disjoint edge subsets. No overlapping pair bounds are composed.

`FALSIFIED` requires a paired exact over-leader witness. `SURVIVED` requires
agreement on all 462,384 source units and every deduplicated carrier profile.
`INCOMPLETE` retains partial checkpoints and changes no status. Survival
authorizes a separately preregistered complete offsets-`1..43` wave; this
campaign alone cannot promote `K'=87`.

**First deployment:** `INCOMPLETE`. Modal app
`ap-VqJehuBkAEPuuHaRhAYPg6` produced one complete primary survival and one
timed-out audit. The primary exhausted all 462,384 source units, all 23,104
raw-unsafe units, and 267,056 deduplicated profiles. The audit reached the
end of `m2=38` without a counterexample before its 720-second child wall.
Capture SHA-256:
`7fd211a2ca2a19de5f483eebcc69a29549e529cdaa713431b86645434f0f11ff`.

The primary result is retained, but this capture does not establish paired
survival and authorizes no full wave. A separately pinned cached audit resume
will rerun only the independent orientation under a longer Modal wall.
