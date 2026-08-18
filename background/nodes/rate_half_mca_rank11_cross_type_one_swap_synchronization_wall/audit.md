# Audit

- Packet size: 32.
- Threshold 18 gives unique anchor and maximum cross-anchor overlap 28.
- Threshold 20 gives unique anchor and maximum cross-anchor overlap 24.
- Existing one-swap overlap: 31.
- Therefore one-swap components preserve anchor type.
- Primitive atom collision needs only two shared slopes; it was not assigned a
  false 31-overlap hypothesis.
- Distinct-atom 28-overlap collision core: at least `1079711-c`.
- After `h<=67472`: at least `1012239-c`, still 36,336 below `K'-1`.
- No assertion of actual cross-type incompatibility is made.
- **Verdict:** GREEN.
