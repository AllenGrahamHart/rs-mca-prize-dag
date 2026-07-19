# Audit - PMA rate-half source cross-ratio fiber reduction

## Load-bearing inputs

| input | use | guard |
|---|---|---|
| `deg Q_0=K_0-1` | common label shifts are absorbed by the core RS code | an off-by-one dimension breaks affine invariance |
| distinct labels | normalization to `(0,1,lambda)` | `lambda` must avoid `0,1` |
| CRT zero residues | two petal-locator factors in each source basis numerator | arbitrary three-dimensional core words do not have (XR3) |
| petal/core disjointness | only `R_3` can vanish on the core | shared roots would enlarge the exceptional set |
| aligned overlap multiplicity | exceptional point costs at most two | triple overlap may not be charged once |

## Nonclaims

- The normalized `lambda` fiber is not yet bounded.
- The factorization does not make `R_3` split on the core.
- No generic rational-map or Fourier theorem is imported.
- No branch other than rate-half `M=4,t=3` is covered.

## Mutations

The verifier rejects an incorrect quotient degree, failure to absorb a common
label shift, a wrong cross-ratio, loss of either petal-locator factor, an
`ell`-point exceptional set, single charging of triple overlap, and deletion
of the positive residual `2b+3a-2`.
