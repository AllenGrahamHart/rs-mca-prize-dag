# Audit

1. The proof selects a root of `S_B` over the algebraic closure; no
   base-field splitting of the correction quadratic is assumed.
2. Center-disjointness is load-bearing. It prevents the center cancellation
   in the exact resultant from masking the local valuation.
3. The unsupported case compares exact orders three and two, not only total
   degrees.
4. In the supported case, the complete gcd `A_sigma R_sigma` excludes an
   outside-support root before the actual/padding split is used.
5. Actual roots are rejected by the proved first jet; padding roots are
   rejected by the defining support set of `g_*`.
6. The argument proves `c!=0` only. It does not prove the unique weld vector
   exists or that its remainder has the required nonzero factorization.
