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

**Outcome:** `PASS` as a route-locating pilot, with no row promotion.
Modal app `ap-Srv9CDnQL721xYGzAUZoR6` completed all ten jobs without a
timeout at 58--62 MB peak RSS. The raw capture SHA-256 is
`4024f6ad84c050540bfa3c32088e4768a3ca5abf798f95bc8624d054178f9ff4`.
Primary and audit agree exactly on every maximum:

```text
ordinary:  41388798786059119503097492734939028640066114130
           margin 44581160171407926086602515730765812413619
offset 1:  41388509655129434578015936172698056050247199551
           margin 333712089856333007643164756703355631328198
offset 2:  41387937303860893532474667943101838831996305858
           margin 906063358397378548911394352920573882221891
offset 7:  41388695386454290912259500164616925968496091874
           margin 147980764999998764079172837833437382435875
offset 73:   207313827489437078117773167012308731551794440
           margin 41181529539729853832905806170442450674326733309
```

The new leading branch is

```text
s2=74/s3=55/s4=45/s5=37/ordinary-single/
c6d3/c7d2/c8d1/c9d0/raw-safe.
```

Thus the adjacent-support router has not failed at the first new row, but
the maximizer changed from K'=83's offset-two/full-fallback template to an
ordinary single-support-three template. Analyze this branch and the
unsampled-offset domination problem symbolically before any full K'=84
wave.
