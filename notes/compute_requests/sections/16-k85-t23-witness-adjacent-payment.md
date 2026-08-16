## Preregistered K'=85 first-witness adjacent payment

- **decision:** on the independently replayed offset-11 `T23` witness, print
  every support-disjoint adjacent-edge price and decide whether the primary
  and independent atlas both reduce it below the exact raw-safe leader
- **scope:** one fixed witness, union 16, dimension 7, available edges 4--5,
  5--6, and 6--7; choices `none`, `4`, `5`, `6`, and `4+6`
- **analyzer SHA-256:**
  `2a63f64023dc04c3a33de293797873dbc9c4d9275dd8486eb31286af2f78724b`
- **dispatcher SHA-256:**
  `be2379bf01c3261489b619a550102e22fc10767e59a019396bda2be3b6e5ef10`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU, 256 MB, 20-second child wall; projected cost below
  `$0.01`
- **local safety:** one RAM-guarded Modal client; no local mathematical run

`PASS` prints both exact option tables and their minimizing edge sets. A price
above the leader is a route wall, not a counterexample to the prize theorem.
`INCOMPLETE` changes no status. This witness calculation cannot promote K'=85.

**Outcome:** `PASS`. Modal app `ap-nJpFGfIsUMBAkL2Ni6Sh2O` completed the
exact analyzer, and the primary and independent formulas agreed on every edge
cap and every option price. The capture SHA-256 is
`9d64a2170614a3c0dae2aef3dd344be231410b1a1a856a38958208686688871e`.

The minimizing choice is the single support-4/5 edge. It lowers the witness
from `42141786157949900288596401924882914598461995992` to
`38031713645027467636162531245586474415179105992`, below the exact raw-safe
leader by `3381154371182309085066360141323405108127727362`. Choices `5`, `6`,
and `4+6` are all weaker on this witness. This identifies an edge-4-only
domination theorem as the next strict, falsifiable compression of the full
adjacent atlas.
