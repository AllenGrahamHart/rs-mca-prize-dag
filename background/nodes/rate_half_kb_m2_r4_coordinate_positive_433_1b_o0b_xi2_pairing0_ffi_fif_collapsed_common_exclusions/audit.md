# Audit

The certificate is checked at three levels:

1. The dimension-zero source has a complete 43-polynomial custody hash.
2. FGLM preserves degree 65, and the first eliminant has the exact guarded
   factorization.
3. The final saturation transcript contains every route guard in order and
   all six rank cofactors.

Before guard index 5 the ideal is nonunit of size 22; immediately after
`b+1` it is unit. This catches omission or reordering of the decisive
boundary guard.
