# Audit - dense top decorated shift-pair router

## Checks

1. The argument uses exact-weight supports, not supports of size merely at
   least `m`.
2. Pair deficits are nonnegative integers because distinct residual
   polynomials have degree below `k`.
3. The 10% conclusion follows from a lower bound on total intersections;
   no random-pair or independence assumption is used.
4. The common locator has degree exactly `k-1`, so division leaves a
   constant, not an unspecified low-degree polynomial.
5. Cofactor primitivity follows from the nonzero constant identity and is
   not assumed.

## Verdict

**GREEN locally / OPEN GAP globally.** The terminal now lands on one exact
local primitive decorated shift-pair degree threshold, `215,792`.
