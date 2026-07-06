# census_bounded_scales

- **status:** PROVABLE
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

At agreement A the quotient stratum on scale N' has forced class ratio l'/N' = j/n, so counts grow strictly as 2^{N' H(j/n)} with H(j/n) bounded below on the corridor (j/n ~ 0.4-0.5 => H >= 0.97). Hence exactly ONE scale's count lands within the staircase-step factor of B*, and it lies in an ABSOLUTE window N' in [~120, ~400] — independent of n and k up to 2^40. The census is n-uniform because every crossing only sees bounded scales.

## Ledger (migrated notes)

the lemma that makes a symbolic census possible at all; also gives UNIQUENESS of the deciding scale (monotone counts, q-factor gaps)
