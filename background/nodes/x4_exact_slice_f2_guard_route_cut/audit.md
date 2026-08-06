# Audit

1. The proof is uniform in the real field-size parameter `L`; the printed
   `L=255.9` table is replay evidence, not a hypothesis.
2. Rate `1/2` is the worst binomial case at the comparison depth. The three
   lower rates are farther from the central slice.
3. The strict inequality uses the actual prize cap `L<256`. The lower field
   bound is used only to ensure `t0<N/128`.
4. The theorem is stronger than a non-generating-row scope cut: it also
   excludes all five generating signed types at exact-slice depth.
5. The conclusion is only that the guarded F2 route is unavailable. It does
   not refute the exact-slice extras budget.
