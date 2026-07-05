# ATTACK - dli_odd_phase_nontriviality_payload

This node is now conditional. The live nontriviality leaf is
`dli_odd_phase_polar_obstruction_payload`.

The standard Artin-Schreier criterion is proved in
`dli_artin_schreier_conductor_criterion`, and ledger soundness is proved in
`dli_odd_phase_budget_ledger_soundness`. The new soundness node
`dli_odd_phase_polar_obstruction_soundness` proves that a reduced local pole
of order prime to `p` gives the required non-Artin-Schreier conclusion.

What remains is the actual project-specific local expansion proof for

```text
P_lambda(sigma(y))
```

on every square-root component and every nonzero frequency/harmonic: exhibit
an Artin-Schreier-reduced pole whose order is positive and not divisible by
`p`.

Alternative routes such as monodromy or collision-energy can still close the
node, but they should first be recorded as explicit certificate-soundness
nodes with a corresponding payload.
