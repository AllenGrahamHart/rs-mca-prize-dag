# Claim contract

## Inputs

- `collision_norm_criterion`, including characteristic-zero nonvanishing;
- `e1_pair_feasible_prime_field_reduction`;
- the canonical quotient orders `N in {256,512}` and exact budget intervals.

## Output

- an exact collision-free radius `s<=4` at `N=256`;
- an exact collision-free radius `s=1` at `N=512`.

## Guards

1. `s` is raw-subset swap distance between representatives of distinct
   antipodal-rearrangement classes; the routed class-pair band uses the minimum
   over representatives.
2. The all-even folded case divides by two before applying the odd-prime
   divisibility test.
3. The theorem uses only the lower field endpoint `2^250`.
4. The remaining distance bands are not bounded.

## Falsifier

A named-interval prime and two distinct classes colliding at one of the
excluded distances, or a coefficient profile violating the printed Parseval
or folding bound.
