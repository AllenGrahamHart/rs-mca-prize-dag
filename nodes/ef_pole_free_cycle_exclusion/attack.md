# ATTACK - ef_pole_free_cycle_exclusion

This is now an assembly node. The live EF leaf is
`ef_descended_cycle_classification_payload`.

The proved descent node `ef_full_orbit_cycle_descent` shows that a pole-free
full Galois orbit would descend to a `B`-defined reduced horizontal cycle in
the pole complement. The proved classification-soundness node shows that an
exhaustive base/tower/noncontainment classification rules out that descended
cycle.

Useful payload routes:

- show that every `B`-defined horizontal cycle in the pole complement is
  base-descended;
- show that any non-base-descended pole-free cycle is confined to a proper
  intermediate subfield;
- show that the only remaining pole-free cycle is the degenerate pencil
  excluded by `noncontain_degeneracy`.

The banked pole arithmetic prices cycles that meet the pole divisor; it does
not by itself exclude pole-free cycles.
