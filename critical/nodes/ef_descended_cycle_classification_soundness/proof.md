# proof: ef_descended_cycle_classification_soundness

By `ef_full_orbit_cycle_descent`, any pole-free full Galois orbit that could
falsify `ef_full_orbit_pole_forcing` descends to a `B`-defined reduced
horizontal cycle in the extension-pole complement.

Assume the classification certificate covers every such descended cycle. If a
cycle is base-descended, it is paid by the base component. If it is
proper-subfield or tower-confined, it is not a full-field hidden leakage class.
If it is noncontainment-degenerate, it is excluded by the noncontainment gate.

These three classes are exactly the removals named in
`ef_pole_free_cycle_exclusion`. Therefore no descended pole-free horizontal
cycle remains that is simultaneously non-base, non-tower, nondegenerate, and
unpaid. This proves the EF pole-free hidden-cycle exclusion.
