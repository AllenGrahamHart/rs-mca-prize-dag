# conditional: ef_ru

## Predicate nodes

- `ef_component_control_alignment`
- `ef_galois_stabilizer_descent`
- `ef_full_orbit_pole_forcing`

## Claim

Conditional on full-orbit pole forcing, the row-uniform extension-fiber
hypothesis holds.

## Proof

The proved predicate `ef_component_control_alignment` applies the banked
component-control theorem to the extension-fiber alignment incidence. Thus the
horizontal components to classify are finite in number and have controlled
degree.

The proved predicate `ef_galois_stabilizer_descent` classifies every horizontal
component by its stabilizer under `Gal(E/B)`. Full stabilizer gives a
base-descended component. A proper nontrivial stabilizer gives a component
defined over an intermediate field, hence a proper-subfield pullback/tower
case.

The only remaining case is a genuinely full Galois orbit of components, not
base-descended and not subfield-confined. The predicate
`ef_full_orbit_pole_forcing` says that such an orbit must meet the
extension-pole divisor, so it is paid by the existing extension-pole ledger
rather than forming an unpaid hidden-fiber component.

These cases exhaust all horizontal components. Therefore no Galois-skew unpaid
horizontal component remains beyond the declared extension-pole divisor and
proper-subfield pullbacks, which is the statement of `ef_ru`.
