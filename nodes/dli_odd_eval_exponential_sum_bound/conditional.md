# conditional: dli_odd_eval_exponential_sum_bound

## Predicate nodes

- `dli_deligne_weyl_transfer`
- `dli_odd_phase_noncollapse_conductor`

## Claim

Conditional on noncollapse and conductor control for the actual odd-evaluation
phase, the finite-frequency Weyl-sum bounds required by
`dli_et_peak_mass_reduction` hold.

## Proof

The predicate `dli_odd_phase_noncollapse_conductor` supplies the
project-specific geometric input: for every central profile, nonzero
frequency, and harmonic in range, the odd-evaluation phase on each square-root
component is geometrically nontrivial and has a conductor budget whose
harmonic total is `o(t)`.

The proved transfer `dli_deligne_weyl_transfer` applies the Weil/Deligne
square-root cancellation theorem to those phases and sums the resulting
conductor-weighted bounds over the harmonic ranges. The total error is `o(t)`
by the conductor-budget predicate.

Thus the normalized odd low-degree evaluations have exactly the Weyl-sum
bounds needed by the Erdos-Turan peak-mass reduction.
