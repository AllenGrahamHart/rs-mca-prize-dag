# ATTACK - dli_odd_phase_noncollapse_conductor

This node is now an assembly node.

The standard transfer from nontrivial bounded-conductor phases to Weyl
cancellation is isolated in `dli_deligne_weyl_transfer`. The standard
Artin-Schreier/conductor criterion is isolated in
`dli_artin_schreier_conductor_criterion`.

The active leaves are `dli_odd_phase_polar_obstruction_payload` and
`dli_reduced_pole_majorant_table_payload`, the project-specific geometry of
the actual odd-evaluation map:

- construct reduced local pole certificates proving that no central-profile
  component makes the nonzero frequency phase Artin-Schreier trivial;
- build the reduced-pole majorant table uniformly over all central profiles
  and harmonics used by `dli_et_peak_mass_reduction`;
- check that the resulting harmonic conductor sum is `o(t)`.

Equivalent routes are acceptable: big monodromy for the odd-evaluation map or
a collision-energy theorem strong enough to imply the same Weyl bounds.
