## Preregistered K'=87 raw-clipped support-4/5 witness probe

- **decision:** test the proved `(36,5)` support-4/5 stratum inequalities
  after imposing the witness's global raw support-4 and support-5 caps before
  the weighted optimization is collapsed
- **scope:** one exact support-disjoint counterexample; no residual lane scan
- **probe SHA-256:**
  `fa24a164437f518ff5a441ccd03bd68e1aedc3b50e20045ade278a45d50f9293`
- **dispatcher SHA-256:**
  `eea1153b5436678bcc3d946d0d1ee5e6dcd54a21fdab82720813f94525d01bfa`
- **K'=87 witness adapter SHA-256:**
  `a66f4235d0651bd35d3ccbe749beb6ea5f52c6b2198bc1460bf13f3fe7907a00`
- **base witness analyzer SHA-256:**
  `44faccd0305d374557650c8bfc3b40f3aaa97717e46b154568cbadb3ec77bf3a`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU, 256 MB, 20-second child wall and 30-second container
  wall; projected cost below `$0.01`
- **local safety:** one RAM-guarded Modal client; no local mathematical run

The primary implementation fixes the total support-4 count, fills uncoupled
strata first, and allocates the coupled count in increasing loss ratio. The
audit independently fixes total support 5 and allocates in the reverse dual
order. Both use exact rational arithmetic and must agree on the optimum and
the two aggregate counts. The raw selected-incidence caps are converted to
circuit caps by flooring against their exact extension factors, matching the
normalization already used by the proved adjacent-support router.

`PASS` requires exact agreement and prints the repaired witness price. A
nonpositive margin is a route wall. A positive margin authorizes packaging
the clipped fixed-union theorem and a separately preregistered offset-1
falsifier. This one-witness probe cannot promote `K'=87`.

**Outcome:** arithmetic `PASS`, route wall. Modal app
`ap-cCC7w2ZcDACsgqKNJS19Ij` completed the probe. The support-4-oriented and
support-5-oriented exact optimizers agree on cap
`15826982470121619978034510012906276872113956680`. The repaired premium is
`41987945497536424020866493137524475559167409625`, still above the K'=87
leader by `527046372060980182985446452501713227668364930`. Capture SHA-256:
`4f3bef9931e692f12b85432719730f433fcb0603cf894982c06a5e9458895120`.

The clipped support-4/5 route is therefore insufficient and does not
authorize a lane scan. The exact support-4 raw cap is active at the optimum,
so the clipping is nonvacuous; however, the witness's stronger existing
single edge is support 5/6. The next bounded action is the analogous
raw-clipped support-5/6 stratum LP for the `(34,6)` charge.
