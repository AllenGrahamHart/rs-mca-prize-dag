# Audit

## Claim boundary

The output is an actual 32-record seed, not an S/A/E classification. The
proof never treats pair types, graph edges, supports, or owners as slopes.
Singleton owners and heavy owners are counted in disjoint classes.

## Critical semantic checks

1. The distinct-pair cap is evaluated at the actual low-margin cutoff
   `tau=387`.
2. The shared-core payment is applied only to heavy pair types; singleton
   records are added separately.
3. Component differences span a subspace of `C'`, not a 20-dimensional
   abstract product: both components individually lie in `C'`.
4. Two distinct owned slopes are selected from every chosen heavy pair.
   Exception-set disjointness, not a simple-graph assumption, forces their
   support intersection into the pair core.
5. Padding to 32 uses distinct already-selected low-margin records and can
   only reduce the support intersection.

## Adversarial controls

The primary checker recomputes the binomial quotient, charges, minimum low
mass, and a deterministic component-span selection control. It rejects eight
metadata/arithmetic mutations. The independent checker derives the quotient
by a falling-product division and rejects four separate mutations.
