# Claim contract

## Inputs

- the six clean candidate agreements and budgets pinned by the XR consumption
  replay;
- `identity_prefix_flexible_budget_unsafe_floor`;
- for the surviving RowC rate-`1/16` branch, a proved containment `D subset B`
  and exact base-field order `b=|B|`.

## Output

- an exact route cut on five candidates;
- on RowC rate `1/16`, an if-and-only-if cutoff for the two numerical premises
  of the identity-prefix supplier.

## Guards

1. `M` is the MCA numerator budget `floor(q/2^128)`.
2. The agreement supplied to the theorem is the unsafe predecessor
   `m=a_safe-1`.
3. The prefix depth is `w=m-k-1`, not the safe-row depth.
4. A proper base field may be used only with a proved domain-containment
   statement.
5. Route failure is never emitted as a safe upper bound.

## Nonclaims

- The RowC characteristic is not pinned by this packet.
- No proper-subfield containment is inferred from the anchor budget.
- No prize-max or universal unsafe payload is produced.
