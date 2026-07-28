# Audit

- The primary generator uses folded pairs and balanced shards; the audit uses
  lexicographic shards and direct 128-slot convolution.
- The exact norm engines are FLINT in Modal app
  `ap-5RZLHmXH21jJetiYlXEvLU` and PARI in
  `ap-Hcr26R9gJ1DnC1bLMkYf5f`.
- Their aggregate worker times were 146.715916962 and 700.302430224 seconds.
- Both returned all 32 shards and all 511,272 rows with no error or interval
  candidate.
- Exact agreement is checked in all fields of all 64 multiset fingerprint
  buckets, in every per-energy region count, and at both interval extremizers.
- The compact packets retain commitments and extremizers instead of a raw norm
  dump.
- The verifier pins both generators, launchers, result packets, and the parent
  theorem statement.
