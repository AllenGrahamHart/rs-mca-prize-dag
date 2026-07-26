# Conditional proof: e1_fullness

## Predicate nodes

- `e1_exceptional_set_reduction`
- `e1_clean_anchor_exact_collision_allowance`
- `e1_official_prime_exception_control`

## Claim

Conditional on the exact route-uniform collision-pair bound, every row in the
pair-feasible direct-E1 candidate class `|F_p(Q)|>=b_pair_min(K,B*)` has more
than `B*` distinct reduced E1 values at its clean candidate predecessor.

## Proof

Fix a candidate-class row. The exact class compiler gives the actual quotient
order `N`, class count `K=A_2(N,ell)`, and budget `B*`. Partition the `K`
characteristic-zero classes by their reduced ambient-field E1 value. If the
fiber sizes are `r_y`, then

```text
K-|image| = sum_y(r_y-1)
          <= sum_y binom(r_y,2)
          = P.
```

The remaining predicate `e1_official_prime_exception_control` supplies
`P<=K-B*-1`. Hence `|image|>=K-P>=B*+1`.

The canonical quotient locator construction makes every realized reduced
`-e_1` value a bad slope at agreement `m=k+n/N`; this realization does not use
the unavailable norm threshold. The row's field, embedding, owner, and
endpoint pins then turn the image into the required direct `V` payload.

`e1_exceptional_set_reduction` does not supply the inequality by itself. It
proves that every pair counted by `P` is controlled by the explicit
norm-divisor/folded-kernel object, which is the attack interface for the open
predicate.
