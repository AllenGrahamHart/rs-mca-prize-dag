# cluster_certificates

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

(a) Diameter-d* class sets are fully certified free cliques (~2^33 at N'=128) by graded_collision_radius. (b) For clusters with center-difference Delta EVERYWHERE-BIG (min conjugate >= spread/(budget-1)): every cross-pair diff = Delta(1 + Delta^{-1} eta) with quotient norm < p, so ONE precomputable norm check on Delta certifies ALL cross-pairs of the two clusters. (c) FREEBIE: integer factors are self-certified (p does not divide integers < p), so integer multiples of certified elements are certified.

## Ledger (migrated notes)

certification compresses quadratically: pairs -> cluster pairs -> generator checks | PROVED-IN-FLIGHT: #206 | PROVED 2026-07-04: free cliques by graded_collision_radius, cross-cluster checks by the everywhere-big quotient norm bound, integer freebies by p > integer factor.
