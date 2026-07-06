# proof: dli_reduced_pole_majorant_table_soundness

Let `T` be a table indexed by the DLI tuples

```text
(central profile, nonzero frequency, harmonic, square-root component).
```

Assume `T` is complete: every tuple used by the DLI odd-evaluation Weyl sums
appears exactly once or is represented by a stated disjoint row class whose
multiplicity is included in the table total.

For each tuple `tau`, let `D_tau` be the true degree or weighted size of the
Artin-Schreier-reduced polar divisor of the actual phase

```text
P_lambda(sigma(y)).
```

The table gives a certified majorant `M_tau` with `D_tau <= M_tau`. Therefore
the true reduced-pole total over any collection of DLI tuples is bounded by
the corresponding table total:

```text
sum_tau D_tau <= sum_tau M_tau.
```

By hypothesis the table's full harmonic-range total is `o(t)`. Hence the true
sum of reduced polar-divisor contributions over all central profiles,
nonzero frequencies, harmonics, and square-root components is also `o(t)`.
That is exactly the assertion of `dli_reduced_pole_harmonic_ledger`.
