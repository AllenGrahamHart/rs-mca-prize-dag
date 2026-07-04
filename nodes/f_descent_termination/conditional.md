# f_descent_termination conditional proof

- **status:** CONDITIONAL
- **closure:** proof from predicate nodes

## Predicate nodes

- `f_sparse_descent_step`
- `f_support_lattice`
- `f_termination_mds`
- `f_termination_hankel`
- `f_spread_moment_count`

## Claim

Conditional on these predicates, iterating sparse-dual descents produces only a
polynomial-size descent tree for the consumer families, with spread/moment
base cases at the leaves.

## Proof

The proved `f_sparse_descent_step` gives the local recursion rule. A minimal
weight-`w` dual word splits the current flat into descent branches where either
the degree drops by at least `w` while the dimension drops by at most `w-1`, or
the residual domain loses the closed sparse support. Thus every strict descent
step buys net divisor-depth progress.

The proved `f_support_lattice` removes the naive binary-tree danger. Branches
with the same closed sparse-support state and residual data have identical
future recursion, so memoized descent states are counted by the closed sets of
the generated support lattice rather than by all branch histories.

The proved `f_termination_mds` handles the coordinate/fiber consumer branch:
the shortened-MDS dual has no relevant sparse words, so its support lattice is
trivial and the descent tree has one state.

The predicate `f_termination_hankel` supplies the remaining family-specific
closed-set count for Hankel-kernel flats. Once that count is polynomial, the
support-lattice accounting bounds the Hankel descent tree polynomially as well.

At terminal spread states, the proved `f_spread_moment_count` supplies the
moment bound used as the leaf estimate. The sunflower-fiber escape branch is
priced by the PMA machinery and is not double-counted in this descent node.

Therefore the only open mathematical content is the Hankel closed-set bound.
Given it, the descent-termination parent follows as an assembly implication.
