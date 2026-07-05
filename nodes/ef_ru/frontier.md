# frontier: ef_ru

EF_ru is not a computation node. It is the row-uniform completeness theorem
for extension-fiber horizontal components.

## What is now wired

- `ef_component_control_alignment` is PROVED from `spi_component_control`.
- `ef_galois_stabilizer_descent` is PROVED by Galois descent.
- `ef_full_orbit_pole_forcing` is now CONDITIONAL.
- `ef_full_orbit_cycle_descent` is PROVED: a pole-free full Galois orbit
  descends to a `B`-defined pole-free cycle.
- `ef_pole_free_cycle_exclusion` is CONDITIONAL.
- `ef_descended_cycle_inventory_payload` is TARGET.

The maintainer/referee note says these do not by themselves discharge EF_ru:
they price known columns but do not prove that no Galois-skew hidden-fiber
component exists.

## Remaining theorem

For every admissible row `B <= E <= F` and B-rational pair `(u,v)`, classify
each horizontal component of the extension-fiber alignment incidence as one of:

1. base-descended / B-rational;
2. extension-pole divisor;
3. proper-subfield pullback / tower-confined.

There must be no fourth Galois-skew horizontal component.

## Smallest proof route

Use `spi_component_control` to reduce to finitely many controlled components.
Then classify each component by its Galois stabilizer over `Gal(E/B)`:

- full stabilizer implies base descent;
- intermediate stabilizer implies subfield pullback;
- trivial/full orbit must meet the pole divisor or else gives the named
  hidden-fiber leakage falsifier.

The missing algebra is now exactly `ef_descended_cycle_inventory_payload`:
inventory and classify the descended `B`-defined pole-free cycles so none can
survive the base, tower, and noncontainment removals.

## Falsifier

A Galois-skew hidden-fiber leakage class: an unpaid horizontal component over
a non-generating row, not B-descended, not subfield-confined, missing the pole
divisor, and surviving noncontainment.
