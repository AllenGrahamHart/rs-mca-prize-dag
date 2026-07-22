# Audit - L1 official Newton cofactor-window router

1. The generated field is used: `8192|p^f-1`, not merely containment in an
   unrelated ambient field.
2. Both `n>=8192` and the strict 256-bit cap are load-bearing.
3. The twelve congruence candidates below 3583 carry printed factor
   certificates; no primality oracle is part of the proof.
4. The reserve estimate uses the canonical cutoff, not an arbitrary larger
   threshold.
5. The Newton depth is `d=min(a,h-k)`, and strict `d<p` is required.
6. The received-word excess is measured at the lower threshold
   `e_0=h-a_0`; this controls every higher shell because `h-k` is fixed.
7. Power-sum coordinates preserve one fixed-cofactor prefix cell. They do not
   coalesce the `q^e` cells or prove flatness.
8. The F2 summit is not a requirement and remains a distinct special target.
9. No computation or probabilistic evidence is load-bearing.
