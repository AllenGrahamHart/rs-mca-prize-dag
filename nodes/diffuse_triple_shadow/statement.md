# diffuse_triple_shadow
- **status:** TARGET
## Statement
After tangent/Luroth/extension/same-slope pricing: the number of supported
slopes whose FIRST rank-stagnating certificate is a diffuse m >= 4 syzygy
(triple-covered shadows spread across many small triple intersections, no
single k+1-point triple core) is poly(n). The final residue of the slope
sieve after the three PROVED reductions: (1) fresh-rank slopes <= 2n
(dimension count in K^n + K^n); (2) the Vandermonde syzygy lemma — every
nonzero dual word in a stagnating dependency is supported on the >= 3-covered
shadow, forcing k+1 triple-covered points; (3) m = 3 stagnations are
TANGENT-PAID (|T1 cap T2 cap T3| >= k+1; solving u + z_i v = c_i on the core
makes u AND v RS-tangent on k+1 points). Connects to the F-lattice machinery.

## Stress evidence

`experiments/amber_stress/diffuse_shadow_circuit_scan.py` searches small
finite-field Hankel locator models for minimal first-stagnating circuits whose
triple-covered agreement shadow has size `< k+1`.  The current deterministic
run covers three rows (`F_13/mu_12`, `F_17/mu_8`, `F_17/mu_16`) and found
`11,785` minimal dependent circuits, including `10,691` diffuse `m >= 4`
residues and `1,094` tangent-core circuits, with `0` shadow violations.

This is falsification evidence only.  It does not prove the required
polynomial count for the diffuse residue.
