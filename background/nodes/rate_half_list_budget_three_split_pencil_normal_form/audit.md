# Audit

1. Pair locators use selected support intersections, not all accidental
   codeword agreements. Extra roots are retained honestly in `q_ij`.
2. `q_ij` is nonzero because the codewords are distinct; its degree cap is an
   inequality, not an assertion that every pair difference has full degree.
3. The omitted-triple labels in `A_k A_l` are complementary to the pair
   labels. Reversing this convention is caught by the toy replay.
4. Cancellation in `(SP2)` removes only the common nonzero polynomial
   `J A_l`; no evaluation or division by possibly zero field values occurs.
5. The degree table distinguishes edge multiplicity `p_ij` from pair deficit
   `delta_ij`. Their sum, not either quantity alone, controls `b_ij`.
6. The independent replay reconstructs the exact `F_17,mu_8` path witness,
   divides every pair difference by its printed locator, verifies all four
   triangle identities and both product identities, and rejects a mutated
   edge coefficient.
