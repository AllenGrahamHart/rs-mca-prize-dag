# Attack

1. Keep the strict-caller verifier pinned to `imgfib` and
   `spi_point_counting`; any new `req` consumer re-opens the compiler.
2. Close `f_imgfib_consumer_descriptor`: replace the prose-level
   "plane sections" charge with an exhaustive branch-to-flat map.
3. Reuse the exact punctured root-free cell from
   `l1_rootfree_rational_q_projective_packing`, but do not label the full Pade
   section linear.
4. Print the exact quantitative gap required by the global packing theorem;
   `r<j` without a bound is not enough.
5. Mutation-test one omitted LIST branch, one nonlinear-section substitution,
   one duplicated owner, and one puncture that changes the domain.
