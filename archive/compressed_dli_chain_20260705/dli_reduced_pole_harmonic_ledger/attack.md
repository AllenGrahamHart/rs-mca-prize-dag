# ATTACK - dli_reduced_pole_harmonic_ledger

This node is now conditional. The live reduced-pole leaf is
`dli_reduced_pole_majorant_table_payload`, alongside the nontriviality leaf
`dli_odd_phase_polar_obstruction_payload`.

The ledger-soundness rule is proved in
`dli_odd_phase_budget_ledger_soundness`, and the table-format soundness rule
is proved in `dli_reduced_pole_majorant_table_soundness`. What remains is the
actual reduced-pole accounting:

- compute or bound the Artin-Schreier-reduced polar divisor of
  `P_lambda(sigma(y))`;
- do this uniformly over the central profiles, nonzero frequencies, harmonics,
  and square-root components;
- prove the resulting harmonic total is `o(t)`.

The output should be a complete majorant table, an exact symbolic formula
that generates such a table, or an equivalent monodromy/collision bound
implying the same harmonic total.
