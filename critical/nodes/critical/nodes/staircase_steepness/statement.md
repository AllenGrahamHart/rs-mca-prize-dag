# staircase_steepness

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

At consecutive grid points t changes by 1, so the leading-order stratum counts jump by factors ~ q (from the exact C(n,j) q^{1-t} shape and the Acl formulas). Hence B* is crossed in ONE step, and each candidate-point comparison B_C(A) vs B* is decided by relative precision far coarser than the step factor — EXCEPT on a knife-edge set where the count sits within the estimate's error band of B*.

## Ledger (migrated notes)

the reason the endgame is tractable: steep staircases make comparisons cheap | IN FLIGHT: #193 | PROVED 2026-07-04: exact adjacent-ratio algebra plus the stated knife-edge exception.
