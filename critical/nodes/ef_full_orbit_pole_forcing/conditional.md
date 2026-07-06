# conditional: ef_full_orbit_pole_forcing

## Predicate nodes

- `ef_full_orbit_cycle_descent`
- `ef_pole_free_cycle_exclusion`

## Claim

Conditional on excluding descended pole-free hidden cycles, every genuinely
full-field Galois orbit of horizontal components must meet the extension-pole
divisor.

## Proof

Assume a genuinely full-field Galois orbit of horizontal components is neither
base-descended nor confined to a proper intermediate subfield.

If the orbit meets the extension-pole divisor, it is paid by the existing
extension-pole ledger (`ext_import` and `paid_ext_fn`), and there is nothing
left to prove.

If the orbit avoids the extension-pole divisor, the proved node
`ef_full_orbit_cycle_descent` turns the whole orbit into a `B`-defined reduced
horizontal cycle in the pole complement.

The predicate `ef_pole_free_cycle_exclusion` rules out exactly such a cycle
after the base-descended, tower-confined, and noncontainment-degenerate cases
are removed. Therefore a surviving full-field orbit cannot avoid the pole
divisor.

Thus every genuinely full-field orbit either is paid by the pole ledger or is
excluded, proving the full-orbit pole-forcing statement conditional on the
pole-free-cycle exclusion.
