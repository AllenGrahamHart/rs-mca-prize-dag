# Audit

## Verdict

The deletion dichotomy is exact. The only quotient remainder with a unique
profile-preserving predecessor is remainder one; every other remainder has
two deletions whose overlap is large enough for RS uniqueness.

## Scope checks

- `A>=k+1` is used as `B-2>=A-1>=k`.
- At remainder zero, deleting a point gives `c-1` residual points and one
  fewer complete fiber.
- At remainder at least two, two residual deletions stay in the same quotient
  profile family.
- At remainder one, the predecessor is a pure-fiber support and may genuinely
  be contained; this branch cannot be deleted from the theorem.
- The boundary codeword identity uses at least `k` common points.

## Limitations

The number of pure-fiber cores is large. Calling their one-point extensions
"tangent" does not by itself pay their union. The downstream boundary
agreement owner assigns all of them to the single threshold-coherent set
`B_(A+1)`.
