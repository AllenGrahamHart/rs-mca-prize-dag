# Claim contract

- **Claim:** `(A1Q2)--(A1Q3)` exclude the profile and imply the official
  prefixes `(A1Q4)`.
- **Dependencies:** the core-stripped contact section and core slope ledger.
- **Output:** removal of every core-free first-degree chamber and explicit
  lower endpoints for the remaining `s=0,1` degree ranges.
- **Consumer:** `rate_half_band_crossing_location`.
- **Nonclaim:** the threshold equality profiles and higher degrees remain
  open.
- **Falsifier:** a contact-active component of domain degree at most three,
  incorrect target degree `-s-1`, or an off-by-one error in either official
  threshold.
- **Replay:** run this directory's verifiers under `tools/ramguard tiny --`.
