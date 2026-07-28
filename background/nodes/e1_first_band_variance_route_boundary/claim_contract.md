# Claim contract

## Inputs

- the proved `collision_norm_criterion`, which identifies exact cyclotomic
  norms as the collision gate;
- the fixed rational cubic-Hermite basis and affine moment model pinned in
  `source_pin.json`;
- nonnegative chamber maxima `M_3^max` when the route cut is invoked.

## Output

The named majorant is a live exclusion tool at even level `V=50`, with exact
threshold `13`, and is dead for every even `V<=48` already at `M_3=0`.

## Nonclaims

- no variance level or autocorrelation profile is empty by this result;
- no exact norm is evaluated or excluded;
- no claim is made for profile `(4,2,0)`, later swap bands, or `N!=256`;
- the route cut is not a collision or counterexample;
- the five higher thresholds are reproduced, but their underlying chamber
  censuses are not re-proved by this node.

## Falsifier

The node is false if the pinned majorant has nonnegative optimistic margin at
`(V,0)` for any even `V<=48`, fails either side of a printed threshold, is not
strictly decreasing in `M_3`, or has boundary slope outside `(107,108)`.

## Evidence-edge promotion test

This route-cut node cannot itself become a requirement supplier for either
open E1 terminal.  Promotion requires a separate proved finite-completeness
router plus exhaustive emptiness or exact-norm exclusion for every residual
`V<=48` chamber.  Such a closure node may cite this result to justify its
choice of method.
