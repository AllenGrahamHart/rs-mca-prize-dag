# Audit

Date: 2026-07-18.

## Forward audit

The residual size-two count is a nonnegative integer because the official
mass and every power-of-two block contribution are even. The tail proof treats
`tau=2` separately, where the residual is present; for `tau>=3` only the
geometric power-of-two ladder remains. The verifier checks only tail
breakpoints because the block count is constant and `tau^3` increases between
successive breakpoints.

## Consumer-backward audit

The clean energy compiler needs `(CT3)` with the opposite inequality. The
profile violates it while satisfying the two proposed marginal inputs, so no
logical deduction from only those inputs is possible. Subgroup realizability
is explicitly outside the claim; this is a route fence, not negative evidence
about the actual critical assertion.

## Replay scope

The verifier constructs all 29 official profiles, checks exact mass and the
constant-four tail, identifies exactly the twenty violating exponents, and
checks DAG mutations. It uses no Modal resource.
