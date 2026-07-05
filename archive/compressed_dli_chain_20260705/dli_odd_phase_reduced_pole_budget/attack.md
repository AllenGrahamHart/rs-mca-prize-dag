# ATTACK - dli_odd_phase_reduced_pole_budget

This is now an assembly node.

The standard Artin-Schreier/conductor criterion is proved in
`dli_artin_schreier_conductor_criterion`, and ledger soundness is proved in
`dli_odd_phase_budget_ledger_soundness`. What remains is specific to the
actual odd-evaluation map on the square-root section:

- prove `dli_odd_phase_nontriviality_payload`: rule out
  `P_lambda(sigma(y)) = g^p-g+c` on every relevant component for every
  nonzero frequency and harmonic;
- prove `dli_reduced_pole_harmonic_ledger`: bound the reduced polar divisor
  after Artin-Schreier reduction and sum those bounds over the DLI harmonics
  to get `o(t)`.

Equivalent collision-energy or monodromy arguments are acceptable if they
imply the same nontrivial bounded-conductor Weyl input.
