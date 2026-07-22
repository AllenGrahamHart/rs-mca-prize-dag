# Audit

1. The first coordinates must be distinct. Without the inverted full
   Vandermonde product, one representation can be repeated 25 times.
2. The prefix product includes all `binom(25,2)=300` differences. A partial
   adjacent-difference product is insufficient.
3. `B_(i,0)` is a separate variable. Substituting `(x_i-T)z_i` directly into
   its first square would make quartic equations.
4. Both `T` selectors and every `x_i` inverse are load-bearing.
5. The system has a `25!` permutation symmetry. A lower variable count does
   not imply a faster Groebner or SAT computation.
6. Characteristic-zero emptiness gives an outer characteristic certificate,
   not an exact support factorization without further elimination.
