## Work cycle 394: K'=87 disjoint-edge witness repair

### Pins

- starting Codex pin: `bf798b434`
- canonical Fable prize pin: `28a62b40060c39c8ee35deaac819f33f18824303`
- upstream main pin: `93fba1be3f3299b0ba4708d88715377bbb656e45`
- relevant upstream PR: `#1170` at K'=86 head `7214947e`
- critical snapshot before DAG changes: 27 `TARGET`, 37 `CONDITIONAL`

### Result: NARROWED

Modal app `ap-wLdIVTwSfqoHqcbrTReo02` evaluated every support-disjoint
adjacent-edge option on the exact best-single counterexample. Capture
SHA-256:
`9edcb2b46da5f9cb3aa97bcc8f230e0725bc7b2cd72e214477f4c5ece34ba82b`.
Primary and independent atlases agree exactly.

The valid non-overlapping edge set `4+6` lowers the witness to
`37213564927666895824914633823577105351210858112`, leaving positive margin
`4247334197808548012966412861445656980288186583` below the K'=87 raw-safe
leader. All single-edge choices fail on this profile.

### Burn-down

- node/workboard item attacked: local `rate_half_band_crossing_location`, at
  first open rank-nine component row `K'=87`
- DAG status delta: none; one witness is repaired, not the complete row
- upstream terminal delta: none; `K'=86` remains the last exported prefix
- route delta: the first best-single obstruction is paid by a proved
  support-disjoint composition; overlapping-edge composition remains forbidden
- delta-star bracket movement: none
- new assumptions: none
- next route-deciding action: exhaust offset 1 with paired support-disjoint
  pricing; best-single-surviving offsets 9, 23, and 43 inherit survival
  without recomputation
