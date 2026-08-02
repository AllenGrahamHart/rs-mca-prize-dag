# Audit

The following failure modes are explicitly excluded:

- **Pairwise-minor shortcut:** the proof records why the selected six-row
  base has rank six before replacing six minors by three determinants.
- **One-chart overclaim:** all six product cofactors are run independently.
- **Generic projection overclaim:** the `t` denominator is proved invertible,
  while the nonempty zero-dimensional `c` exception is retained.
- **Fixed-cofactor overclaim:** its zero-dimensional intersection is recorded,
  not deleted by saturation.
- **Kernel scaling:** the normalized `(-1,1)` interpolation kernel is checked
  against all ten original rows after reduction by `F(r,b)`.
- **Closure inflation:** neither the dense outside ledger nor the finite
  exception ledger is asserted.

Exploratory full outside ideals reached their time caps because projective
denominator clearing produced degree-45 to degree-49 inputs.  A
Gaussian-rational gcd route also reached its cap.  Neither failed run is
used as theorem evidence.
