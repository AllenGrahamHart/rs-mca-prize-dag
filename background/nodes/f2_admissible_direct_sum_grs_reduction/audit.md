# Audit

1. The ambient degree `e` is not the order of `p mod n`; the trace bound
   uses `k=ord_n(p)`. This distinction is load-bearing on non-generating
   rows.
2. The class split is an exact direct sum, not only a dimension identity.
   Independence is proved only because admissibility forces `D<=2`.
3. The class code is the kernel of the displayed GRS parity-check matrix and
   has parameters `[S,S-R,R+1]_p` when `R<S`; `min(S,R)` covers saturation.
4. `Z(L)=Z_1^C` follows from direct-sum support and additive weight. It does
   not imply `Z_1` is small.
5. The K1 kernel is invariant under a domain coset, but the separate
   Frobenius antipodal-descent identity need not be.

The canonical verifier was replayed in a clean Modal worker and returned
373/373 PASS. Its toy checks exercise class kernels at set level, dimensions
up to six, exact GRS parameters, mass factorization, trace collapse, and
coset behavior. The general result rests on the written proof, not toy scale.

The final route node verifier ran in Modal app
`ap-bMpQIqA5drSKk82JQgIgGa` and returned `3/3 PASS` across this theorem, the
counterexample node, and the repaired critical route.
