# f_sparse_descent_step

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s3b_iii_3_fibers_and_noanchor.md#1']

## Statement

Given a minimal weight-w dual word on S: (a) members containing S in their roots form a subflat of codim <= w-1 (the relation makes one vanishing condition redundant) and factor as l_S x (degree j-w instance) — DEGREE drops w, DIMENSION drops <= w-1: net one unit of divisor depth gained, exactly F's j - dim P threshold shape; (b) by closure, all other members have <= w-2 roots in S: recurse on H minus S with root budget j-w+2. Single-step accounting elementary; assembly belongs to f_dim_induction.

## Ledger (migrated notes)

PROVED 2026-07-04 as a one-step lemma only; the global descent assembly remains in f_dim_induction/f_descent_termination.
