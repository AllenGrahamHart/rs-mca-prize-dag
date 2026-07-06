# conditional proof: strip

- **status:** CONDITIONAL
- **closure:** proof

## Predicate nodes

- `periodic_strata`
- `q_recursion`
- `confinement`
- `isotypic`
- `gap1_noneq_mass`
- `gap2_seam`

## Claim

Conditional on the predicate nodes, the strip-periodic contribution is exactly
partitioned into rate-preserving quotient-recursive columns plus a residual
non-equivariant periodic mass bounded by `poly(n) * FM`.

## Proof

The predicates `periodic_strata` and `q_recursion` identify the
rate-preserving periodic buckets: if the periodicity modulus divides the row
parameters, the stratum descends to the quotient row and is counted by the
banked quotient recursion.

The predicates `confinement` and `isotypic` put every remaining stable escape
object into the equivariant/non-equivariant split.  Equivariant pieces are the
quotient-recursive pieces already accounted for.  Non-equivariant pieces are
exactly the multi-isotypic periodic escape stratum.

The predicate `gap1_noneq_mass` bounds that multi-isotypic residual by
`poly(n) * FM`, using the product-model/TR terminal reserve.  This is the only
unproved pricing input in the strip decomposition.

Finally, `gap2_seam` proves that the line-side aperiodic strip and the
support-side quotient strip agree on rate-preserving folds, and classifies the
non-rate-preserving folds as seam buckets that remain on the aperiodic side
without quotient-recursion boost.  Hence the two stripping conventions do not
double-count or omit a periodic bucket.

Combining these inputs gives the exact partition and the advertised
`rate-preserving quotient columns + O(poly(n) * FM)` bound consumed by
`mca_safe`.
