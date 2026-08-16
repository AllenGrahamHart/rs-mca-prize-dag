## Preregistered K'=84 adjacent-support route pilot

- **decision:** determine whether the first new row already breaks the
  proved K'=83 adjacent-support router, and identify the exact first
  obstruction if it does
- **scope:** `ordinary`, exact offsets `1`, `2`, `7`, and the new terminal
  offset `73`, in both primary and independent implementations
- **primary wrapper SHA-256:**
  `a3f55cf0627f63b9786d3f44f526bb44c62d223152424099f1039df04d272a20`
- **audit wrapper SHA-256:**
  `a9a323316bcbef966ad97ca3e24f66220aa41baf8d5115e7ca3f3205e3e37249`
- **hash-pinned K'=83 code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **batch runner SHA-256:**
  `bbe9f1100d8d6add611794e24e02d57ab0f57903a15195a944e6fe640ca98922`
- **envelope:** ten remote containers, one CPU and 1 GB each, 645-second
  child wall; projected cost below `$0.20`
- **local safety:** one RAM-guarded Modal client; no local enumeration

The wrappers change only the row parameters to `K'=84`, `q=74`,
`m'=67556`, and `n'=1048660`. The theorem and router sources imported by
the wrappers are the unchanged hash-pinned K'=83 implementations. The five
lanes are route-locating, not an exhaustive row certificate.

```text
PASS:       both implementations agree and all five lanes are safe;
            analyze the active templates symbolically before authorizing
            any remaining-lane wave
FAIL:       both implementations agree on an unsafe lane; retain its exact
            branch as the next analytic wall and do not launch broadly
INCOMPLETE: any timeout, missing lane, or implementation disagreement;
            retain no mathematical conclusion
```

No outcome of this pilot promotes `K'=84` or changes a DAG status.
