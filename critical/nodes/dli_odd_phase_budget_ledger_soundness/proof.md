# proof: dli_odd_phase_budget_ledger_soundness

The statement of `dli_odd_phase_reduced_pole_budget` has two requirements for
every DLI odd phase:

1. the phase is not of Artin-Schreier form `g^p-g+c`; and
2. the Artin-Schreier-reduced polar-divisor bounds have harmonic total `o(t)`.

Assume the ledger covers every tuple used in the DLI harmonic ranges. Coverage
means no central profile, nonzero frequency, harmonic, or square-root
component is omitted.

For each covered tuple, the ledger's nontriviality entry supplies requirement
1 directly. The polar-divisor entries are certified upper bounds for the
corresponding reduced polar divisors. Summing those upper bounds over exactly
the DLI harmonic ranges gives the ledger's declared harmonic total, which is
`o(t)` by hypothesis. Therefore the true harmonic total is also `o(t)`.

Thus both requirements of `dli_odd_phase_reduced_pole_budget` hold for the
actual list of DLI odd phases.
