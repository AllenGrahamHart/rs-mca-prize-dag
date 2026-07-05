# proof: dli_reduced_phase_manifest_soundness

Let `M` be a reduced-phase manifest satisfying the stated predicates.

The manifest covers the same tuple universe used by both DLI payloads:

```text
(central profile, nonzero frequency, harmonic, square-root component).
```

For each tuple, it gives an Artin-Schreier-reduced local expansion of the
actual phase `P_lambda(sigma(y))` and records a pole of positive order not
divisible by `p`. These are exactly the local certificates required by
`dli_odd_phase_polar_obstruction_payload`. The already proved
`dli_odd_phase_polar_obstruction_soundness` confirms that this certificate
format has the intended non-Artin-Schreier meaning.

For the same tuple, the manifest records a certified upper bound for the
reduced polar divisor. The manifest also proves that the harmonic sum of
those majorants is `o(t)`. These are exactly the table rows and summation
assertion required by `dli_reduced_pole_majorant_table_payload`. The already
proved `dli_reduced_pole_majorant_table_soundness` confirms that this table
format has the intended reduced-pole ledger meaning.

Thus one verified reduced-phase manifest supplies both former payloads. The
construction of the actual manifest remains separate.
