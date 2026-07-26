# conditional: unsafe_at_crossing

## Predicate nodes

- `unsafe_crossing_family_instantiation`
- `qfloor_exact`
- `averaged_slope_conversion`

## Claim

Every admissible row has more than `B*` bad slopes at `a_safe-1`.

## Proof

Fix a row and take its payload from
`unsafe_crossing_family_instantiation`.

- In branch `Q`, the payload verifies every prime-field, quotient-order, norm-
  threshold, endpoint, and count hypothesis of `qfloor_exact`. That theorem
  supplies `Acl(N',ell') > B*` distinct bad slopes.
- In branch `V`, the payload itself is an exact pairwise-distinct family of
  more than `B*` bad slopes at the required endpoint.
- In branch `M`, the payload supplies a deterministic post-paid family `A`,
  its exact strict-overlap profile, and
  `nu(A) = E[N(A)] - (q/2) C_t(A) > B*`. Apply
  `averaged_slope_conversion` with the integer `B=B*+1`; it gives a received
  pair with at least `B*+1` distinct slopes, hence strictly more than `B*`.

The payload also pins the ambient MCA slope field, generated-field transfer,
first-match ownership, and monotonicity from its construction radius to
`a_safe-1`. Hence each branch proves the adjacent unsafe inequality.
