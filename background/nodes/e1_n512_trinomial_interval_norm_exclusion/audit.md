# Audit

Date: 2026-07-27.

The primary verifier computes all 748 exact SymPy resultants and applies every
norm directly to both exact field intervals. Full repository-path replay in
Modal run `ap-fyc4m86CmfVSpz1HWo8etR` passed at 91 MB peak RSS.

An independent implementation uses FLINT `fmpz_poly.resultant`, reconstructs
the orbit partition, and replays the interval screen. Modal run
`ap-qSXsrD1Nlzsrndis9rfrPS` matched both certificate digests and all headline
counts.

No integer factorization is load-bearing. An exploratory bounded factor pass
left composite residuals and was superseded by the exact cofactor-window
identity. The two intervals are so narrow relative to the norms that every
cofactor window has width at most one.

The certificate is finite but route-uniform for this profile: it exhausts all
signed supports and every prime in both intervals. It is not a selected-field
exhibit. The result closes no `s>=3` band and supplies no total collision-pair
bound.
