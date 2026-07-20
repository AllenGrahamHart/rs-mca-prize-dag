# Audit - L1 marked common-pencil next-strip boundary fiber bound

## Checked axes

1. The argument uses `h<=t ell+p`, not the false equality `h=t ell-p`.
2. The strict background cap `r<=ell-1` supplies the `-1` in `(2)`.
3. The condition `ell>2P_0` is what excludes `t=m` on the thin edge.
4. CRT uses selected support locators, whose degree is `t ell-v`.
5. When `v<g`, the result is singleton; otherwise the coefficient count is
   `v-g+1`, not `v-g`.
6. No Forney-basis conclusion is asserted on this boundary.

## Remaining attack

Compose this fiber bound with support and defect-locator counts; arbitrary
petal locators and cross-chart aggregation remain outside its scope.

