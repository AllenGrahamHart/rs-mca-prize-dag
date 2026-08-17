## Preregistered K'=88 raw-clipped stress

- **decision:** test the proved raw-clipped adjacent-support theorem at four
  route-deciding K'=88 offsets before considering a complete residual wave
- **ordered scope:** offsets `1` (largest residual), `22` (interior), `30`
  (raw-safe leader), and `44` (last raw-unsafe lane)
- **primary adapter SHA-256:**
  `402274ed8f4aede86b091a08ffcf500e72139653f154fd2113481d7780e60ecc`
- **independent adapter SHA-256:**
  `ee48fe44cbd5a8af0783d3be097439eb6727c73d63e4a4ab5738a39603f47d7c`
- **shared traversal core SHA-256:**
  `8c549dde77e560a21fb4dac67eec29ccf642ac861475b89ceb59d3ba57acb4ca`
- **dispatcher SHA-256:**
  `df170f0abd75c3871cdb42199e6108df477d6f7af6aec16594575e4d1be8be94`
- **checker SHA-256:**
  `b68e84202dae1c974f7126c1e1c7af4bd3056d739c1b1b2acf5f6e6d8676f4d1`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** eight jobs, one CPU and 256 MB each, 900-second child wall
  and 915-second container wall; projected total cost below `$0.20`
- **local safety:** one RAM-guarded Modal client; no local enumeration

The adapters substitute only `K'=88`, `q=78`, `m'=67560`, `n'=1048664`,
the derived exact ceiling, and the exact raw-safe offset-30 leader. They use
the two proved orientations of the raw-clipped theorem. A paired offset-44
deployment smoke must pass before the eight-job stress.

`FALSIFIED` requires the same exact over-leader witness from both theorem
orientations. `PASS` requires paired survival on all four offsets, exact
coverage of 1,341,815 source units and 51,707 raw-unsafe units, and no
over-leader carrier profile. `INCOMPLETE` includes timeout, malformed output,
resource breach, or disagreement and changes no mathematical status.
Survival authorizes a separate value assessment; it neither launches a full
wave automatically nor promotes `K'=88`.
