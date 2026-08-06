# F2 Round-17 route-repair node verification - preregistration

- **date:** 2026-08-06
- **candidate proved node:** `f2_admissible_direct_sum_grs_reduction`
- **candidate refuted node:** `f2_all_admissible_o1_mass_bound`
- **repaired critical target:** `f2_conditional_close`

Run all three candidate node verifiers in one fresh Modal worker against the
compiled manifest DAG.  The counterexample verifier must produce and check a
Pocklington certificate for `p=3*2^41+1`, verify `p^6<2^256`, and confirm the
status split `PROVED / REFUTED / TARGET`.  The route verifier must confirm
that Myerson is evidence rather than a requirement and that the prize-facing
F2 conclusion remains a critical TARGET.

One CPU, 1 GiB RAM, 120-second function cap, 90-second subprocess cap, no
retry.  Only `3/3` PASS authorizes the route-repair commit.  Any failure
blocks the surgery without changing the canonical `prize` tree.
