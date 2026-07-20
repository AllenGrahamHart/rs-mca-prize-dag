# Audit

1. The executable refuses `s>4`; accidental official-scale local use is not
   possible through its public entry point.
2. The proved packet is `n=8`, not merely a hand-selected subset of blocks.
3. Direct enumeration does not reuse orbit polynomials or resultants.
4. The prime set includes positive and negative support cases at both cutoffs.
5. Atomic output is rewritten after every completed block.
6. Timeout and partial selection retain `complete=false`.
7. Coefficient hashes are audit aids, not substitutes for the independent
   finite-field comparison.
8. The dense implementation is a correctness oracle, not an official-order
   algorithm or cost estimate.
