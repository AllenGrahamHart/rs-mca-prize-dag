# Audit

1. The solver derives the touched label ratio from all remaining second-petal
   equations; it does not rely on random labels.
2. `W` is checked nonzero at every missed core point, so the defect is exact.
3. Untouched labels are chosen outside the exact rational-value sets on their
   petals, so there are no hidden petal agreements.
4. The evaluation domain is the full smooth subgroup `H_32`, not an arbitrary
   32-point subset.
5. The witness has bounded root excess three. It cuts only an emptiness route.
6. The aggregate census is deterministic by seeds `0..49`; the explicit seed
   `3` witness is replayed independently in `verify.py`.
