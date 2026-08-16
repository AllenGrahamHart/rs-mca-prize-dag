## Preregistered K'=85 two-charge witness adjacent payment

- **decision:** print every support-disjoint adjacent-edge price on the exact
  edge-4 counterexample and identify the minimal edge set in both the primary
  and independent atlas
- **scope:** offset 11, `m2=13`, `s4=s5=50`, case
  `F23__N4_t12__N5_t12`, charges `(28,7),(29,6)`
- **analyzer SHA-256:**
  `44faccd0305d374557650c8bfc3b40f3aaa97717e46b154568cbadb3ec77bf3a`
- **dispatcher SHA-256:**
  `d93bfb284f268fcbda93a75558c173538e341bb5420521c7692f45cf98427529`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU, 256 MB, 20-second child wall; projected cost below
  `$0.01`
- **local safety:** one RAM-guarded Modal client; no local mathematical run

`PASS` prints both exact option tables. A best price above the raw-safe leader
is a current-router wall; a lower price identifies the next compressed edge
family. `INCOMPLETE` changes no status. No outcome promotes K'=85.

**Outcome:** `PASS`. Modal app `ap-mnimiGFuHSPQ7gNIcB3gMN` completed the
exact option table; primary and independent values agree entry by entry. The
capture SHA-256 is
`d1ba20be24f8f86e8da708613f89f899341a4c3f34ee3eca515ce0c4a5ba0b1a`.

The minimizing choice is the single support-6/7 edge, with price
`36771696071065385390668923925145098778166086838`, below the exact raw-safe
leader by `4641171945144391330559967461764780745140746516`. The disjoint
choice `4+6` is slightly weaker, while edges 4 and 5 alone do not identify the
minimum. This motivates a best-single-edge domination falsifier before any
full support-disjoint replay.
