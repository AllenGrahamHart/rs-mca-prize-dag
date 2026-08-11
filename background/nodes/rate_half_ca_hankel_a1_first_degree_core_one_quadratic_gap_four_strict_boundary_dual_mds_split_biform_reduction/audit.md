# Audit

1. Divisibility by `Lambda_2` is termwise. An endpoint-missing coordinate
   gets one endpoint factor from its source form and the other from its
   locator row; a coordinate present at both endpoints gets both factors
   from its locator row.
2. The source form and locator row have total parameter degree `e+1`, so
   division by two endpoint factors leaves degree at most `e-1`.
3. The dual-GRS dimension is `p-1`, so its polynomial representatives have
   degree at most `p-2`, not `p-1`.
4. The Lagrange identity applies through degree `n_0-2`; the largest degree
   in the orthogonality check is `(p-2)+d=3p-3=n_0-2`.
5. Every coordinate in either endpoint-missing class has exactly `e-1`
   distinct off-line source roots. This pins the parameter degree sharply
   and counts `2p+r_A` split rows without using the remaining coordinates.
6. The clean-fiber count requires `a_delta=r_delta=0`; Cycle 131 proves at
   least `(e+15)/2+r_A` simultaneous events.
7. At a clean fiber there is no padded locator factor. The nonzero
   specialization scalar `chi_delta` is retained in `zeta_delta` rather
   than silently normalized away.
8. Equation `(8)` first gives agreement on `X_delta`. Equality on all of
   `U_0` additionally uses the common zeros `I_delta`, after which the
   degree bound gives polynomial equality.
