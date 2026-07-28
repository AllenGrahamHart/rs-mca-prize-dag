# Audit

- The primary enumerator uses folded pairs and balanced shards; the audit uses
  lexicographic shards and a direct 128-slot convolution.
- The norm engines are independent exact libraries: FLINT in Modal app
  `ap-cqeedeWfHi2ZWPpADOVg8o` and PARI in
  `ap-UrU14R9jlfWWM2B50i9jwk`.
- Their aggregate worker times were 15.754747376 and 54.527383552 seconds.
- Both runs returned all 32 shards and all 21,376 rows with no error or
  interval candidate.
- Exact agreement is checked in every field of all 64 multiset fingerprint
  buckets, as well as in the per-energy region counts and the two interval
  extremizers.
- The compact packets deliberately retain commitments and extremizers rather
  than a large redundant norm dump.
- The verifier pins both generators, both launchers, both result packets, and
  the parent theorem statement.
