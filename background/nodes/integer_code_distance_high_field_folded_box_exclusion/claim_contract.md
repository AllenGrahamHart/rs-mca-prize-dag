# Claim contract

## Inputs

- `collision_norm_criterion`;
- an odd prime field containing an element of exact order `128`;
- the strict field threshold `p>253^32`.

## Output

The full ternary cube has no non-cyclotomic order-128 kernel vector. The
result is stronger than any bounded-support certificate on this branch.

## Guards

1. The order is exactly `128`; the fold has dimension `64`.
2. The characteristic is prime and odd.
3. The all-even folded face is divided by two before comparing its norm with
   `p`.
4. The strict inequality in `(HFB1)` is retained.

## Nonclaims

- no statement for `p<=253^32` or order `256`;
- no assertion that the quotient cell count exceeds `B*`;
- no promotion of `integer_code_distance_cert`.

## Falsifier

An odd prime `p>253^32`, an order-128 root `zeta`, and a non-antipodal
`v in {-1,0,1}^128` with `sum v_i zeta^i=0 mod p`.
