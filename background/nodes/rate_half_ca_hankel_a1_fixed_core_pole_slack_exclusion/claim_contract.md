# Claim contract

- **Claim:** `(A1X2)` excludes fixed-core profiles; in particular all `s=2`
  profiles and the first `s=1` degree are impossible.
- **Dependencies:** the core-stripped contact section and the exact
  core-stratified slope ledger.
- **Output:** complete closure of `s=2` and pole lower bound `(A1X3)` for
  surviving `s=1`.
- **Consumer:** `rate_half_band_crossing_location`.
- **Nonclaim:** higher `s=1` profiles failing `(A1X2)` remain open.
- **Falsifier:** a fixed-core contact-active component of domain degree at
  most two, incorrect `beta` at `3e=d`, or an official `s=2` integer profile
  failing the strict inequality.
- **Replay:** run this directory's verifiers under `tools/ramguard tiny --`.
