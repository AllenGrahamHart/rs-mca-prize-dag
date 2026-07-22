# far_pair_separation

- **status:** CONDITIONAL
- **closure:** proved implication
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

Conditional on `generator_economy`, combine its pairwise-nonzero center
design with `cluster_certificates` to obtain a family `F` of size above the
printed budget whose internal and cross-cluster `e_1` differences are all
certified by polynomially many per-row generator checks. The implication is
proved in `conditional.md`; the generator design is the open premise.

## Attack surface

toy design search at small N' (measure achievable |F| vs g); telescoping-chain and hierarchical-core approaches provably fail by height_only_impossibility unless generator-factored; the difference-set literature in abelian groups is the import candidate

## Falsifier

n/a (construction target); partial designs have PROPORTIONAL value — census_window_arithmetic converts any achieved L into decided window fractions
