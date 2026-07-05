# conditional: petal_realizable_extra_uniformity

## Predicate nodes

- `petal_realizable_kernel_injection`
- `petal_kernel_realizable_sparsity`

## Claim

Conditional on uniform sparsity of realizable kernel locator points, the exact
number of realizable full-petal extras is uniformly polynomial in the
growing-excess corridor.

## Proof

The proved node `petal_realizable_kernel_injection` maps every exact
realizable full-petal extra injectively to a squarefree locator point lying in
the residue-line kernel `K_{I,d}`.

The predicate `petal_kernel_realizable_sparsity` bounds those squarefree
realizable locator points by a polynomial whose exponent is independent of
the excess `c`.

An injective map cannot increase cardinality. Therefore the number of exact
realizable full-petal extras is bounded by the same uniform polynomial. This
is the desired realizable-extra uniformity statement.
