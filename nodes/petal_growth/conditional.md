# petal_growth conditional proof

- **status:** CONDITIONAL
- **closure:** proof from predicate nodes

## Predicate nodes

- `petal_fixed_excess`
- `petal_excess_induction`

Alternate route:

- `petal_mixed_amplification`

## Claim

Conditional on the predicate nodes, full-petal extras at cofactor excess
`d - ell = c` are bounded by `poly(n)` uniformly in `c`.

## Proof

`petal_fixed_excess` proves the base statement for every fixed excess: at fixed
`c`, the full-petal extras inject into a bounded-dimensional kernel object, so
their count is polynomial in `n` in the generated-field window.

The remaining issue is uniformity as `c` grows. The predicate
`petal_excess_induction` is exactly the bridge from fixed excess to growing
excess: it supplies the mixed-amplification induction with polynomial
constants controlled uniformly over the corridor range.

Combining the fixed-`c` base with that uniform induction proves the stated
full-petal growth bound and closes the Thm 21/B11 escape route.

The refuted `route_exact_rank` alternative is not used. The separate
`petal_mixed_amplification` node remains an alternate way to prove the same
uniform bridge.
