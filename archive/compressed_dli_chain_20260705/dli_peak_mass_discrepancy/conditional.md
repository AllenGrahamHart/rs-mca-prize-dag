# conditional: dli_peak_mass_discrepancy

## Predicate nodes

- `dli_et_peak_mass_reduction`
- `dli_odd_eval_exponential_sum_bound`

## Claim

Conditional on the odd-evaluation exponential-sum predicate, the peak-mass
discrepancy bounds required by the DLI transfer hold.

## Proof

The proved Erdos-Turan reduction is deterministic. It says that finite-range
Weyl-sum bounds for the normalized odd-evaluation sequence imply interval
discrepancy bounds at every reciprocal scale used by the DLI Dirichlet peak
neighborhoods. Applying those interval bounds to dyadic annuli around each
peak gives both the required peak-mass tails and the truncated-log discrepancy
estimates.

The remaining exponential-sum predicate supplies exactly those Weyl-sum
bounds for the actual sequence `P_lambda(sigma(y))`, uniformly over central
profiles and nonzero frequencies, with total error `sum_j eps_j=o(t)`.
Composing the two statements proves this node.
