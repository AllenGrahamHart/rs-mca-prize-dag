# Audit

## Verdict

The support-union theorem and the numerical obstruction are both exact. The
logical direction is intentionally one-sided: an upper bound larger than the
budget proves only that this bound cannot certify safety.

## Scope checks

- Every displayed cell satisfies the load-bearing strict activity condition
  `B-k<c`; the tempting midpoint cell `B=n/2+1` is inactive and is not used.
- The RowC witness cells `(c,B)=(8,261),(8,135),(16,79)` are evaluated exactly.
- At the prize cells `B=A`, the residual binomial is `C(n-k,t)`. The verifier
  proves it exceeds `B*` through `C(n-k,t)>=C(n-k,4)>B*`; no large
  official-row support integer is materialized.
- The fixed-threshold replay uses the conservative `B_quot_ub`, not the
  parity-zero strict quotient count.

## Limitations

This packet does not preclude image-lcm coalescing, source-coupled tails, or a
first-match map whose union is much smaller than the support family. Those are
exactly the remaining useful routes.
