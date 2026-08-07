# Audit

1. The quotient polynomial is called `Q`; field order is not used here.
2. The conclusion `D=T_Q` uses the strict high-range inequality `s<e`.
3. The guard transport uses `gcd(D,M)=1`, supplied by core/petal disjointness.
4. The inverse gate uses the exact LS6 guard, not merely the unguarded slice.
5. The live hypothesis `a<=ell/2` is automatic but remains printed.
6. `(HP5)` is an affine high-coefficient constraint on `Q`, not a count.
7. No rank, splitness, or maximum-fiber conclusion is inferred from the
   coordinate bijection.
