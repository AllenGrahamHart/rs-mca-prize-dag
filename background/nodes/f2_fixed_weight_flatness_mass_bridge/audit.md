# Audit

1. The proof uses the full-cube collision identity before splitting by
   Hamming weight; cross-weight collisions are retained through Minkowski.
2. The additive `1` in `(FW-1)` is load-bearing when `B_b/Q<1`.
3. The tail term is a raw number of binary vectors, not a probability;
   its threshold is therefore `2^(S/2+o(S))`.
4. Complementation shifts the syndrome by `A1`; it does not require
   `A1=0`.
5. The upstream split-locator and Q statements do not automatically apply
   to the weighted odd-power map or its unpruned full slice.
