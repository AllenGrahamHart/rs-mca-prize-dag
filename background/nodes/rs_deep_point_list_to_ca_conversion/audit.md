# Audit

The proof was reconstructed from the simple-pole argument rather than merely
copying the theorem label. The audit checked the four scope-sensitive points:

1. `P_i-P_j` has degree at most `K`, not `K-1`;
2. the averaging set has size `q-N`, so `q>N` is necessary;
3. `floor(delta N)<=N-K-1` gives strictly more than `K` agreement points;
4. the denominator is `q-N-KQ`, so equality in `(DP4)` is not allowed.

The verifier checks the exact ceiling specialization and adjacent denominator
failure. The theorem itself rests on the printed algebraic proof, not on the
finite replay.
