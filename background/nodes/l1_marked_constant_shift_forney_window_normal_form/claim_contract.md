# Claim contract - L1 marked constant-shift Forney-window normal form

## Inputs

- `l1_marked_constant_shift_multistrip_exclusion` for the marked strip and
  exact `P`-adic coefficient interface;
- `pma_saturated_mixed_support_kernel` for exact saturation in the L1
  application.

## Output

Every common-pencil survivor `t<=2m` is classified by one admissible Forney
pair `mu+nu=t`, `mu<=nu<=m`, with `2m-t+2` exact coefficient generators and
determinant `kappa Q`. Every pair is genuinely populated.

## Consumer Rule

Consumers may replace the common-pencil window by the finite Forney strata
and reconstruction `(FW7)--(FW9)`. They may not call those strata paid or
empty, and may not apply the result to arbitrary locator families.

## Falsifier

A saturated tuple satisfying `(FW1)` whose interpolation module lacks the
printed reduced basis, has `nu>m`, has dependent coefficient rows, violates
the reconstruction/gcd guard, or an admissible index pair for which `(FW10)`
fails.
