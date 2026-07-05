# ATTACK - ef_full_orbit_pole_forcing

This node is now an assembly node.

The row-uniform Galois transport part is closed in
`ef_full_orbit_cycle_descent`: a full orbit avoiding the pole divisor descends
to a `B`-defined pole-free horizontal cycle. The active leaf is now
`ef_pole_free_cycle_exclusion`.

Prove that the descended cycle cannot survive the base/tower/noncontainment
removals, or produce the named hidden-fiber leakage falsifier.

Banked context to reuse:

- `ext_import` and `paid_ext_fn` price the pole column;
- `noncontain_degeneracy` removes degenerate containment/pencil residues;
- `f1_case_tower` handles intermediate-subfield confinement.
