# Audit

1. `gcd(512L,256)=256`, so `omega^256` has exact order `2L` for every
   positive integer `L`.
2. The odd powers of `theta` are distinct because their exponents are the
   distinct odd residues modulo `2L`; the Vandermonde determinant is
   therefore nonzero.
3. Uniformity of each `C_a` is marginal.  All `C_a` use the same `lambda`
   and are coupled by `C_a=M^aC_0`.
4. The verifier checks exact finite instances and the displayed identities;
   the general theorem is the symbolic proof, not extrapolation from those
   instances.
