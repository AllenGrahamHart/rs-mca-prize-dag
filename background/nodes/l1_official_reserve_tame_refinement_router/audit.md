# Audit - L1 official-reserve tame-refinement router

1. The field is the generated evaluation field, so `n|p^f-1` is available.
2. The power-of-two order bound uses the exact 2-adic order formula.
3. Characteristics three and five are excluded using the finite `<2^256`
   cap and `n>=2^13`, not an asymptotic heuristic.
4. The cutoff uses `eta=min(epsilon,1/4)`; this preserves qualification of
   the original threshold while bounding the trial constant by `5/4`.
5. The trial cutoff remains below `n-k` for every scoped row.
6. The strict conclusion is `ell_0<p`; replacing it by `ell_0<=p` would not
   exclude the wild outer degree `r=p`.
7. Only fixed-petal map supply is removed. Tame role payment, partial fibers,
   and unanchored maps remain in the consumer.
8. No computation or probabilistic evidence is load-bearing.
